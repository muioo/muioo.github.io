# aihot.virxact.com 日报爬虫重写实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `scripts/ai-daily/fetch.py` 数据源从 hex2077.dev 切换为 aihot.virxact.com JSON API，输出 Hugo branch bundle 结构（每篇独立 md + 日期目录索引），删除 HTML/Playwright 兜底代码。

**Architecture:** 4 模块拆分（fetch.py 编排 / aihot_client.py API / markdown_builder.py 生成 / latest.json 重建）。纯 stdlib，零新依赖。测试用 unittest + unittest.mock。

**Tech Stack:** Python 3.14（兼容 3.9+），stdlib only（urllib/json/re/unittest），Hugo branch bundle。

**Spec:** `docs/superpowers/specs/2026-07-03-aihot-daily-crawler-design.md`

---

## 文件结构

| 文件 | 操作 | 职责 | 行数估计 |
|---|---|---|---|
| `scripts/ai-daily/aihot_client.py` | 新建 | API 客户端：fetch_daily + 重试 | ~55 |
| `scripts/ai-daily/markdown_builder.py` | 新建 | slugify + build_item_markdown + build_daily_index + build_item_pages | ~115 |
| `scripts/ai-daily/latest.py` | 新建 | rebuild_latest_json（兼容旧 md + 新目录） | ~45 |
| `scripts/ai-daily/fetch.py` | 重写 | 主入口编排，删除所有 HTML/Playwright 代码 | ~75 |
| `scripts/ai-daily/test_aihot_client.py` | 新建 | aihot_client 单元测试 | ~80 |
| `scripts/ai-daily/test_markdown_builder.py` | 新建 | markdown_builder 单元测试 | ~120 |
| `scripts/ai-daily/test_latest.py` | 新建 | latest 单元测试 | ~70 |
| `AGENTS.md` | 修改 | 更新源描述、目录结构、env 变量 | - |

**测试运行方式**：每个 test 文件可独立运行 `python scripts/ai-daily/test_xxx.py`，使用 unittest + sys.path 注入。

---

## Task 1: 创建 aihot_client.py（API 客户端）

**Files:**
- Create: `scripts/ai-daily/aihot_client.py`
- Create: `scripts/ai-daily/test_aihot_client.py`

- [ ] **Step 1.1: 写测试文件 test_aihot_client.py**

```python
#!/usr/bin/env python3
"""aihot_client 单元测试。"""
from __future__ import annotations

import datetime as dt
import pathlib
import sys
import unittest
from unittest import mock
from urllib.error import HTTPError

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from aihot_client import build_api_url, fetch_daily


class TestBuildApiUrl(unittest.TestCase):
    """验证 API URL 构建。"""

    def test_build_api_url_with_default_base(self) -> None:
        """默认 base 时 URL 应包含日期。"""
        date = dt.date(2026, 7, 3)
        url = build_api_url(date)
        self.assertIn("2026-07-03", url)
        self.assertTrue(url.endswith("/api/public/daily?date=2026-07-03"))

    def test_build_api_url_with_custom_base(self) -> None:
        """自定义 base 应被使用。"""
        with mock.patch.dict("os.environ", {"AIHOT_API_BASE": "https://example.com"}):
            from importlib import reload
            import aihot_client
            reload(aihot_client)
            url = aihot_client.build_api_url(dt.date(2026, 7, 3))
            self.assertTrue(url.startswith("https://example.com/"))


class TestFetchDaily(unittest.TestCase):
    """验证 fetch_daily 的成功、404、重试行为。"""

    def test_fetch_daily_success(self) -> None:
        """成功响应应返回解析后的 dict。"""
        sample_response = {"date": "2026-07-03", "sections": []}
        mock_resp = mock.MagicMock()
        mock_resp.read.return_value = b'{"date":"2026-07-03","sections":[]}'
        mock_resp.__enter__.return_value = mock_resp
        mock_resp.__exit__.return_value = None
        with mock.patch("urllib.request.urlopen", return_value=mock_resp):
            result = fetch_daily(dt.date(2026, 7, 3))
        self.assertEqual(result["date"], "2026-07-03")
        self.assertEqual(result["sections"], [])

    def test_fetch_daily_404_returns_none(self) -> None:
        """HTTP 404 应返回 None，不抛异常。"""
        error = HTTPError("http://x", 404, "Not Found", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=error):
            with mock.patch.dict("os.environ", {"AI_DAILY_FETCH_RETRIES": "1"}):
                from importlib import reload
                import aihot_client
                reload(aihot_client)
                result = aihot_client.fetch_daily(dt.date(2025, 1, 1))
        self.assertIsNone(result)

    def test_fetch_daily_retries_on_network_error(self) -> None:
        """网络错误应重试，最终成功返回 dict。"""
        mock_resp = mock.MagicMock()
        mock_resp.read.return_value = b'{"date":"2026-07-03","sections":[]}'
        mock_resp.__enter__.return_value = mock_resp
        mock_resp.__exit__.return_value = None
        side_effects = [ConnectionError("fail"), ConnectionError("fail"), mock_resp]
        with mock.patch("urllib.request.urlopen", side_effect=side_effects):
            with mock.patch("time.sleep"):  # 加速测试
                result = fetch_daily(dt.date(2026, 7, 3))
        self.assertEqual(result["date"], "2026-07-03")

    def test_fetch_daily_raises_after_retries_exhausted(self) -> None:
        """重试耗尽后应抛 RuntimeError。"""
        with mock.patch("urllib.request.urlopen", side_effect=ConnectionError("fail")):
            with mock.patch("time.sleep"):
                with self.assertRaises(RuntimeError):
                    fetch_daily(dt.date(2026, 7, 3))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 1.2: 运行测试验证失败**

Run: `python scripts/ai-daily/test_aihot_client.py`
Expected: FAIL with `ModuleNotFoundError: No module named 'aihot_client'`

- [ ] **Step 1.3: 实现 aihot_client.py**

```python
#!/usr/bin/env python3
"""aihot.virxact.com 日报 API 客户端。"""

from __future__ import annotations

import datetime as dt
import json
import os
import random
import time
import urllib.error
import urllib.request


API_BASE = os.getenv("AIHOT_API_BASE", "https://aihot.virxact.com").rstrip("/")
FETCH_RETRIES = int(os.getenv("AI_DAILY_FETCH_RETRIES", "4"))
FETCH_TIMEOUT = int(os.getenv("AI_DAILY_FETCH_TIMEOUT", "30"))

HTTP_HEADERS = {
    "User-Agent": "ai-daily-bot/1.0 (+https://github.com/wangbanglei/firstblog)",
    "Accept": "application/json",
}


def build_api_url(target_date: dt.date) -> str:
    """构建指定日期的 aihot 日报 API URL。"""
    return f"{API_BASE}/api/public/daily?date={target_date.isoformat()}"


def fetch_daily(target_date: dt.date) -> dict | None:
    """获取指定日期的日报数据。

    Returns:
        解析后的 JSON dict；HTTP 404 时返回 None。

    Raises:
        RuntimeError: 重试耗尽后仍失败。
    """
    url = build_api_url(target_date)
    last_error: Exception | None = None

    for attempt in range(1, FETCH_RETRIES + 1):
        request = urllib.request.Request(url, headers=HTTP_HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=FETCH_TIMEOUT) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            last_error = exc
        except Exception as exc:  # noqa: BLE001
            last_error = exc

        if attempt < FETCH_RETRIES:
            sleep_seconds = min(20, attempt * 3 + random.uniform(0.5, 1.5))
            time.sleep(sleep_seconds)

    raise RuntimeError(
        f"fetch_daily failed after {FETCH_RETRIES} attempts for {target_date.isoformat()}: {last_error}"
    )
```

- [ ] **Step 1.4: 运行测试验证通过**

Run: `python scripts/ai-daily/test_aihot_client.py`
Expected: OK (4 tests passed)

- [ ] **Step 1.5: 提交**

```bash
git add scripts/ai-daily/aihot_client.py scripts/ai-daily/test_aihot_client.py
git commit -m "feat(ai-daily): 添加 aihot.virxact.com API 客户端模块"
```

---

## Task 2: 创建 markdown_builder.py（Markdown 生成器）

**Files:**
- Create: `scripts/ai-daily/markdown_builder.py`
- Create: `scripts/ai-daily/test_markdown_builder.py`

### 2.A: slugify 函数

- [ ] **Step 2.1: 写 slugify 测试**

创建 `scripts/ai-daily/test_markdown_builder.py`，先写 slugify 测试：

```python
#!/usr/bin/env python3
"""markdown_builder 单元测试。"""
from __future__ import annotations

import datetime as dt
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from markdown_builder import slugify, build_item_markdown, build_daily_index, build_item_pages


class TestSlugify(unittest.TestCase):
    """验证 slug 生成。"""

    def test_pure_ascii_title(self) -> None:
        """纯 ASCII 标题直接小写连字符化。"""
        self.assertEqual(slugify("Google Health API CLI", ""), "google-health-api-cli")

    def test_mixed_cn_ascii_extracts_ascii(self) -> None:
        """中英混合标题只提取 ASCII 部分。"""
        self.assertEqual(
            slugify("Google Health API 推出 CLI：ghealth", ""),
            "google-health-api-cli-ghealth",
        )

    def test_pure_chinese_falls_back_to_id(self) -> None:
        """纯中文标题回退到 permalink 末段 ID 前 12 字符。"""
        permalink = "https://aihot.virxact.com/items/cmr3uklx8008dslbrcmev44qb"
        self.assertEqual(slugify("昆仑万维天工发布", permalink), "cmr3uklx8008")

    def test_slug_truncated_to_40_chars(self) -> None:
        """超长 slug 截断到 40 字符。"""
        long_title = "Senior SWE Bench Evaluate AI Agent Engineer Benchmark Test Very Long Title"
        slug = slugify(long_title, "")
        self.assertLessEqual(len(slug), 40)

    def test_empty_title_and_permalink(self) -> None:
        """标题和 permalink 都为空时返回 untitled。"""
        self.assertEqual(slugify("", ""), "untitled")

    def test_short_ascii_ignored(self) -> None:
        """单字符 ASCII 串被忽略（要求 ≥2 字符）；无 permalink 回退到 untitled。"""
        # "A" 和 "B" 都是单字符，被过滤；permalink 为空时回退到 "untitled"
        self.assertEqual(slugify("A 标题 B 项", ""), "untitled")

    def test_mixed_short_and_long_ascii(self) -> None:
        """混合标题中只保留 ≥2 字符的 ASCII 串。"""
        # "AI" 保留（2 字符），"A" 和 "B" 忽略
        self.assertEqual(slugify("A AI 标题 B 项", ""), "ai")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2.2: 运行测试验证失败**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: FAIL with `ModuleNotFoundError: No module named 'markdown_builder'`

- [ ] **Step 2.3: 实现 slugify 函数**

创建 `scripts/ai-daily/markdown_builder.py`：

```python
#!/usr/bin/env python3
"""生成 AI 日报 Markdown 文件（日报索引 + 单篇详情）。"""

from __future__ import annotations

import datetime as dt
import json
import re


MAX_DESCRIPTION_LENGTH = 150
MAX_SLUG_LENGTH = 40


def slugify(title: str, permalink: str) -> str:
    """从标题提取 ASCII 词作为 slug，纯中文标题回退到 permalink ID 前缀。

    Args:
        title: 文章标题（可能中英混合）。
        permalink: 文章在 aihot.virxact.com 的详情页 URL。

    Returns:
        URL 友好的 slug 字符串。
    """
    ascii_runs = re.findall(r"[A-Za-z0-9][A-Za-z0-9-]*", title)
    # 过滤掉长度 < 2 的串
    ascii_runs = [run for run in ascii_runs if len(run) >= 2]
    slug = "-".join(run.lower() for run in ascii_runs)
    slug = re.sub(r"-+", "-", slug).strip("-")

    if slug:
        return slug[:MAX_SLUG_LENGTH]

    # 纯中文标题：取 permalink 末段 ID 前 12 字符
    item_id = permalink.rstrip("/").rsplit("/", 1)[-1]
    return item_id[:12] if item_id else "untitled"
```

- [ ] **Step 2.4: 运行测试验证通过**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: OK (7 tests passed)

### 2.B: build_item_markdown 函数

- [ ] **Step 2.5: 在 test_markdown_builder.py 追加测试**

在 `TestSlugify` 类后追加：

```python
class TestBuildItemMarkdown(unittest.TestCase):
    """验证单篇详情页 Markdown 生成。"""

    def setUp(self) -> None:
        """准备测试用 item 数据。"""
        self.target_date = dt.date(2026, 7, 3)
        self.item = {
            "title": "AI 版支付宝开放公测",
            "summary": "支付宝阿宝 AI 助手今日正式开放公测，iOS 和安卓用户可体验。" * 5,
            "sourceUrl": "https://www.ithome.com/0/971/469.htm",
            "sourceName": "IT之家（RSS）",
            "permalink": "https://aihot.virxact.com/items/cmr2x7ii20c2jsl8zygz5iw9n",
        }

    def test_frontmatter_contains_required_fields(self) -> None:
        """frontmatter 必须包含 title/date/description/category/source_url/source_name/external_permalink。"""
        md = build_item_markdown(self.target_date, self.item, "产品发布/更新")
        self.assertIn('title: "AI 版支付宝开放公测"', md)
        self.assertIn("date: 2026-07-03T08:30:00+08:00", md)
        self.assertIn("description:", md)
        self.assertIn('category: "产品发布/更新"', md)
        self.assertIn("source_url: https://www.ithome.com/0/971/469.htm", md)
        self.assertIn('source_name: "IT之家（RSS）"', md)
        self.assertIn(
            "external_permalink: https://aihot.virxact.com/items/cmr2x7ii20c2jsl8zygz5iw9n",
            md,
        )
        self.assertIn("comments: false", md)

    def test_description_truncated_to_150_chars(self) -> None:
        """description 应截断到 150 字符并加省略号。"""
        md = build_item_markdown(self.target_date, self.item, "产品发布/更新")
        # 提取 description 行
        for line in md.splitlines():
            if line.startswith("description:"):
                value = line[len("description: "):].strip('"')
                self.assertLessEqual(len(value), 153)  # 150 + "..."
                self.assertTrue(value.endswith("..."))
                break
        else:
            self.fail("description line not found")

    def test_body_contains_summary_and_links(self) -> None:
        """正文应包含摘要、原文链接、AI HOT 详情页链接。"""
        md = build_item_markdown(self.target_date, self.item, "产品发布/更新")
        self.assertIn("## 摘要", md)
        self.assertIn("支付宝阿宝 AI 助手", md)
        self.assertIn("## 原文链接", md)
        self.assertIn("[IT之家（RSS）](https://www.ithome.com/0/971/469.htm)", md)
        self.assertIn(
            "[AI HOT 详情页](https://aihot.virxact.com/items/cmr2x7ii20c2jsl8zygz5iw9n)",
            md,
        )

    def test_missing_source_url_omits_link(self) -> None:
        """item 缺 sourceUrl 时不输出原文链接行。"""
        item = {**self.item, "sourceUrl": ""}
        md = build_item_markdown(self.target_date, item, "产品发布/更新")
        self.assertNotIn("[IT之家（RSS）]()", md)
```

- [ ] **Step 2.6: 运行测试验证失败**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: FAIL with `ImportError: cannot import name 'build_item_markdown'`

- [ ] **Step 2.7: 实现 build_item_markdown**

在 `markdown_builder.py` 中追加：

```python
def truncate_description(text: str) -> str:
    """截断 description 到 150 字符，超长加省略号。"""
    text = " ".join(text.split())
    if len(text) <= MAX_DESCRIPTION_LENGTH:
        return text
    return text[:MAX_DESCRIPTION_LENGTH] + "..."


def build_item_markdown(target_date: dt.date, item: dict, category: str) -> str:
    """生成单篇详情页 Markdown。

    Args:
        target_date: 日报日期。
        item: API 返回的单个 item dict。
        category: 所属 section 名称（如"产品发布/更新"）。

    Returns:
        完整 Markdown 字符串，含 frontmatter。
    """
    title = item.get("title", "")
    summary = item.get("summary", "")
    source_url = item.get("sourceUrl", "")
    source_name = item.get("sourceName", "")
    permalink = item.get("permalink", "")
    date_text = f"{target_date.isoformat()}T08:30:00+08:00"

    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"date: {date_text}",
        f"description: {json.dumps(truncate_description(summary), ensure_ascii=False)}",
        f"category: {json.dumps(category, ensure_ascii=False)}",
        f"source_url: {source_url}",
        f"source_name: {json.dumps(source_name, ensure_ascii=False)}",
        f"external_permalink: {permalink}",
        "comments: false",
        "---",
        "",
        "## 摘要",
        "",
        summary,
        "",
        "## 原文链接",
        "",
    ]
    if source_url:
        lines.append(f"- [{source_name}]({source_url})")
    if permalink:
        lines.append(f"- [AI HOT 详情页]({permalink})")
    return "\n".join(lines) + "\n"
```

- [ ] **Step 2.8: 运行测试验证通过**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: OK (11 tests passed)

### 2.C: build_daily_index 函数

- [ ] **Step 2.9: 在 test_markdown_builder.py 追加测试**

```python
class TestBuildDailyIndex(unittest.TestCase):
    """验证日报索引页 Markdown 生成。"""

    def setUp(self) -> None:
        """准备测试 sections 数据。"""
        self.target_date = dt.date(2026, 7, 3)
        self.sections = [
            {
                "label": "产品发布/更新",
                "items": [
                    {
                        "title": "AI 版支付宝开放公测",
                        "summary": "支付宝阿宝 AI 助手今日正式开放公测。",
                        "permalink": "https://aihot.virxact.com/items/aaa",
                    },
                    {
                        "title": "Google Health API CLI",
                        "summary": "ghealth 是一款封装 Google Health API 的开源工具。",
                        "permalink": "https://aihot.virxact.com/items/bbb",
                    },
                ],
            },
            {
                "label": "论文/研究",
                "items": [
                    {
                        "title": "Senior SWE-Bench",
                        "summary": "开源基准测试评估 AI 智能体作为高级工程师的能力。",
                        "permalink": "https://aihot.virxact.com/items/ccc",
                    },
                ],
            },
        ]

    def test_frontmatter_has_title_and_date(self) -> None:
        """索引页 frontmatter 包含正确的 title 和 date。"""
        md = build_daily_index(self.target_date, self.sections)
        self.assertIn('title: "AI日报 | 2026-07-03"', md)
        self.assertIn("date: 2026-07-03T08:30:00+08:00", md)
        self.assertIn("comments: false", md)

    def test_sections_grouped_by_label(self) -> None:
        """每个 section label 作为二级标题。"""
        md = build_daily_index(self.target_date, self.sections)
        self.assertIn("## 产品发布/更新", md)
        self.assertIn("## 论文/研究", md)

    def test_items_numbered_globally_across_sections(self) -> None:
        """item 序号跨 section 全局递增（1, 2, 3...）。"""
        md = build_daily_index(self.target_date, self.sections)
        self.assertIn("### 1. [AI 版支付宝开放公测", md)
        self.assertIn("### 2. [Google Health API CLI", md)
        self.assertIn("### 3. [Senior SWE-Bench", md)

    def test_links_use_relative_path_with_filename(self) -> None:
        """链接使用相对路径 ./NN-slug/ 格式。"""
        md = build_daily_index(self.target_date, self.sections)
        self.assertIn("](./01-ai/)", md)
        self.assertIn("](./02-google-health-api-cli/)", md)
        self.assertIn("](./03-senior-swe-bench/)", md)

    def test_empty_sections_produce_no_content(self) -> None:
        """空 sections 列表只生成 frontmatter。"""
        md = build_daily_index(self.target_date, [])
        self.assertIn("---", md)
        # frontmatter 之后应只有空行
        body = md.split("---\n", 2)[2] if md.count("---\n") >= 2 else ""
        self.assertEqual(body.strip(), "")

    def test_section_with_empty_items_skipped(self) -> None:
        """items 为空的 section 不输出。"""
        sections = [{"label": "空分类", "items": []}]
        md = build_daily_index(self.target_date, sections)
        self.assertNotIn("## 空分类", md)
```

- [ ] **Step 2.10: 运行测试验证失败**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: FAIL with `ImportError: cannot import name 'build_daily_index'`

- [ ] **Step 2.11: 实现 build_daily_index**

在 `markdown_builder.py` 中追加：

```python
def _iter_valid_items(
    sections: list[dict],
) -> list[tuple[int, str, dict]]:
    """遍历 sections，跳过缺 title 或 summary 的 item，返回 [(全局序号, 分类, item), ...]。"""
    result: list[tuple[int, str, dict]] = []
    global_index = 0
    for section in sections:
        label = section.get("label", "")
        for item in section.get("items", []):
            if not item.get("title") or not item.get("summary"):
                continue
            global_index += 1
            result.append((global_index, label, item))
    return result


def build_daily_index(target_date: dt.date, sections: list[dict]) -> str:
    """生成日报索引页 Markdown（用作 {date}/_index.md）。

    Args:
        target_date: 日报日期。
        sections: API 返回的 sections 列表。

    Returns:
        完整 Markdown 字符串，含 frontmatter 和所有 item 索引。
    """
    date_text = f"{target_date.isoformat()}T08:30:00+08:00"
    title = f"AI日报 | {target_date.isoformat()}"
    description = f"{target_date.isoformat()} AI 热点日报"

    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"date: {date_text}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "comments: false",
        "---",
        "",
    ]

    valid_items = _iter_valid_items(sections)
    current_label: str | None = None
    for index, label, item in valid_items:
        if label != current_label:
            if current_label is not None:
                lines.append("")
            lines.append(f"## {label}")
            lines.append("")
            current_label = label
        item_title = item.get("title", "")
        summary = item.get("summary", "")
        permalink = item.get("permalink", "")
        slug = slugify(item_title, permalink)
        filename = f"{index:02d}-{slug}"
        lines.append(f"### {index}. [{item_title}](./{filename}/)")
        lines.append("")
        lines.append(summary)
        lines.append("")

    # lines 末尾始终为 ""（来自 append("")），"\n".join 会产生尾随换行
    return "\n".join(lines)
```

- [ ] **Step 2.12: 运行测试验证通过**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: OK (17 tests passed)

### 2.D: build_item_pages 函数

- [ ] **Step 2.13: 在 test_markdown_builder.py 追加测试**

```python
class TestBuildItemPages(unittest.TestCase):
    """验证单篇详情页批量生成与文件名处理。"""

    def setUp(self) -> None:
        """准备测试 sections。"""
        self.target_date = dt.date(2026, 7, 3)
        self.sections = [
            {
                "label": "产品发布/更新",
                "items": [
                    {
                        "title": "AI 版支付宝开放公测",
                        "summary": "支付宝阿宝 AI 助手开放公测。",
                        "sourceUrl": "https://ithome.com/1",
                        "sourceName": "IT之家",
                        "permalink": "https://aihot.virxact.com/items/aaa",
                    },
                    {
                        "title": "Google Health API CLI",
                        "summary": "ghealth 开源工具。",
                        "sourceUrl": "https://marktechpost.com/1",
                        "sourceName": "MarkTechPost",
                        "permalink": "https://aihot.virxact.com/items/bbb",
                    },
                ],
            },
        ]

    def test_returns_filename_content_pairs(self) -> None:
        """返回 [(filename, content), ...] 列表，长度匹配 item 数。"""
        pages = build_item_pages(self.target_date, self.sections)
        self.assertEqual(len(pages), 2)
        self.assertTrue(all(isinstance(f, str) and f.endswith(".md") for f, _ in pages))
        self.assertTrue(all(isinstance(c, str) and c.startswith("---") for _, c in pages))

    def test_filename_uses_index_and_slug(self) -> None:
        """文件名格式为 NN-slug.md。"""
        pages = build_item_pages(self.target_date, self.sections)
        self.assertEqual(pages[0][0], "01-ai.md")
        self.assertEqual(pages[1][0], "02-google-health-api-cli.md")

    def test_slug_collision_appends_suffix(self) -> None:
        """同日 slug 冲突时第二个追加 -2。"""
        sections = [
            {
                "label": "分类",
                "items": [
                    {"title": "AI Report", "summary": "s1", "permalink": "https://x/aaa"},
                    {"title": "AI Report", "summary": "s2", "permalink": "https://x/bbb"},
                    {"title": "AI Report", "summary": "s3", "permalink": "https://x/ccc"},
                ],
            }
        ]
        pages = build_item_pages(self.target_date, sections)
        self.assertEqual(pages[0][0], "01-ai-report.md")
        self.assertEqual(pages[1][0], "02-ai-report-2.md")
        self.assertEqual(pages[2][0], "03-ai-report-3.md")

    def test_item_missing_title_skipped(self) -> None:
        """缺 title 的 item 被跳过。"""
        sections = [
            {
                "label": "分类",
                "items": [
                    {"title": "", "summary": "s1", "permalink": "https://x/aaa"},
                    {"title": "AI Report", "summary": "s2", "permalink": "https://x/bbb"},
                ],
            }
        ]
        pages = build_item_pages(self.target_date, sections)
        self.assertEqual(len(pages), 1)
        self.assertEqual(pages[0][0], "01-ai-report.md")

    def test_item_missing_summary_skipped(self) -> None:
        """缺 summary 的 item 被跳过。"""
        sections = [
            {
                "label": "分类",
                "items": [
                    {"title": "AI Report", "summary": "", "permalink": "https://x/aaa"},
                ],
            }
        ]
        pages = build_item_pages(self.target_date, sections)
        self.assertEqual(len(pages), 0)

    def test_content_includes_category_frontmatter(self) -> None:
        """生成的 md 包含 category frontmatter。"""
        pages = build_item_pages(self.target_date, self.sections)
        self.assertIn('category: "产品发布/更新"', pages[0][1])
```

- [ ] **Step 2.14: 运行测试验证失败**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: FAIL with `ImportError: cannot import name 'build_item_pages'`

- [ ] **Step 2.15: 实现 build_item_pages**

在 `markdown_builder.py` 中追加：

```python
def build_item_pages(
    target_date: dt.date, sections: list[dict]
) -> list[tuple[str, str]]:
    """生成所有单篇详情页，返回 [(filename, content), ...] 列表，处理 slug 冲突。

    Args:
        target_date: 日报日期。
        sections: API 返回的 sections 列表。

    Returns:
        列表，每项为 (文件名, Markdown 内容)。
    """
    pages: list[tuple[str, str]] = []
    seen_slugs: dict[str, int] = {}

    for index, category, item in _iter_valid_items(sections):
        title = item.get("title", "")
        permalink = item.get("permalink", "")
        base_slug = slugify(title, permalink)

        slug = base_slug
        if base_slug in seen_slugs:
            seen_slugs[base_slug] += 1
            slug = f"{base_slug}-{seen_slugs[base_slug]}"
        else:
            seen_slugs[base_slug] = 1

        filename = f"{index:02d}-{slug}.md"
        pages.append((filename, build_item_markdown(target_date, item, category)))

    return pages
```

- [ ] **Step 2.16: 运行所有测试验证通过**

Run: `python scripts/ai-daily/test_markdown_builder.py`
Expected: OK (23 tests passed)

- [ ] **Step 2.17: 提交**

```bash
git add scripts/ai-daily/markdown_builder.py scripts/ai-daily/test_markdown_builder.py
git commit -m "feat(ai-daily): 添加 markdown_builder 模块（slugify+索引+详情页生成）"
```

---

## Task 3: 创建 latest.py（latest.json 重建）

**Files:**
- Create: `scripts/ai-daily/latest.py`
- Create: `scripts/ai-daily/test_latest.py`

- [ ] **Step 3.1: 写测试文件 test_latest.py**

```python
#!/usr/bin/env python3
"""latest 单元测试。"""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from latest import rebuild_latest_json


class TestRebuildLatestJson(unittest.TestCase):
    """验证 latest.json 重建逻辑。"""

    def setUp(self) -> None:
        """创建临时 content/ai-daily 与 data/ai-daily 目录。"""
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmpdir.name)
        self.content_dir = self.root / "content" / "ai-daily"
        self.data_dir = self.root / "data" / "ai-daily"
        self.content_dir.mkdir(parents=True)
        self.data_dir.mkdir(parents=True)
        self.latest_file = self.data_dir / "latest.json"

    def tearDown(self) -> None:
        """清理临时目录。"""
        self.tmpdir.cleanup()

    def _patch_dirs(self) -> "mock._patch":
        """patch latest 模块的 CONTENT_DIR 和 DATA_DIR 指向临时目录。"""
        import latest
        return mock.patch.multiple(
            latest,
            CONTENT_DIR=self.content_dir,
            DATA_DIR=self.data_dir,
            LATEST_FILE=self.latest_file,
        )

    def test_scan_old_style_md_files(self) -> None:
        """兼容旧 hex2077 顶层 YYYY-MM-DD.md 文件。"""
        (self.content_dir / "2026-05-15.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "2026-05-16.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        dates = [d["date"] for d in data["days"]]
        self.assertEqual(dates, ["2026-05-16", "2026-05-15"])

    def test_scan_new_style_date_directories(self) -> None:
        """扫描 YYYY-MM-DD/ 目录结构。"""
        (self.content_dir / "2026-07-03").mkdir()
        (self.content_dir / "2026-07-03" / "_index.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "2026-07-02").mkdir()
        (self.content_dir / "2026-07-02" / "_index.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        dates = [d["date"] for d in data["days"]]
        self.assertEqual(dates, ["2026-07-03", "2026-07-02"])

    def test_mixed_old_md_and_new_dirs_deduplicated(self) -> None:
        """同日期的旧 md 和新目录不重复（按日期去重，新目录优先）。"""
        (self.content_dir / "2026-07-03.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "2026-07-03").mkdir()
        (self.content_dir / "2026-07-03" / "_index.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        dates = [d["date"] for d in data["days"]]
        self.assertEqual(dates, ["2026-07-03"])  # 去重后只一个

    def test_sorted_descending_by_date(self) -> None:
        """日期降序排列。"""
        for d in ["2026-07-01", "2026-07-03", "2026-07-02"]:
            (self.content_dir / d).mkdir()
            (self.content_dir / d / "_index.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        dates = [d["date"] for d in data["days"]]
        self.assertEqual(dates, ["2026-07-03", "2026-07-02", "2026-07-01"])

    def test_limited_to_7_entries(self) -> None:
        """最多保留 7 条。"""
        for i in range(10):
            d = f"2026-07-{i:02d}"
            (self.content_dir / d).mkdir()
            (self.content_dir / d / "_index.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        self.assertEqual(len(data["days"]), 7)

    def test_url_uses_date_path(self) -> None:
        """URL 格式为 /ai-daily/{date}/。"""
        (self.content_dir / "2026-07-03").mkdir()
        (self.content_dir / "2026-07-03" / "_index.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        self.assertEqual(data["days"][0]["url"], "/ai-daily/2026-07-03/")

    def test_ignored_non_date_files(self) -> None:
        """非日期格式的文件/目录被忽略。"""
        (self.content_dir / "_index.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "random.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "not-a-date").mkdir()
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        self.assertEqual(data["days"], [])

    def test_updated_at_is_iso_format(self) -> None:
        """updated_at 是 ISO 8601 格式。"""
        (self.content_dir / "2026-07-03").mkdir()
        (self.content_dir / "2026-07-03" / "_index.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        self.assertIn("updated_at", data)
        self.assertTrue(data["updated_at"].endswith("Z"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3.2: 运行测试验证失败**

Run: `python scripts/ai-daily/test_latest.py`
Expected: FAIL with `ModuleNotFoundError: No module named 'latest'`

- [ ] **Step 3.3: 实现 latest.py**

```python
#!/usr/bin/env python3
"""重建 data/ai-daily/latest.json 索引文件。"""

from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content" / "ai-daily"
DATA_DIR = ROOT / "data" / "ai-daily"
LATEST_FILE = DATA_DIR / "latest.json"

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"
MAX_ENTRIES = 7


def rebuild_latest_json() -> None:
    """扫描 content/ai-daily/ 下的旧 md 文件与新日期目录，重建 latest.json。

    兼容两种结构：
    - 旧：content/ai-daily/YYYY-MM-DD.md（hex2077 历史文件）
    - 新：content/ai-daily/YYYY-MM-DD/（branch bundle 目录）

    同日期两者并存时去重，目录结构优先。
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    dates: set[str] = set()

    # 扫描旧结构：顶层 YYYY-MM-DD.md 文件
    for path in CONTENT_DIR.glob("*.md"):
        if path.name == "_index.md":
            continue
        if re.fullmatch(f"{DATE_PATTERN}\\.md", path.name):
            dates.add(path.stem)

    # 扫描新结构：YYYY-MM-DD/ 目录
    for path in CONTENT_DIR.iterdir():
        if path.is_dir() and re.fullmatch(DATE_PATTERN, path.name):
            dates.add(path.name)

    entries = [
        {
            "date": date_str,
            "title": f"AI日报 | {date_str}",
            "url": f"/ai-daily/{date_str}/",
        }
        for date_str in sorted(dates, reverse=True)[:MAX_ENTRIES]
    ]

    payload = {
        "updated_at": (
            dt.datetime.now(dt.timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        ),
        "days": entries,
    }

    LATEST_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
```

- [ ] **Step 3.4: 运行测试验证通过**

Run: `python scripts/ai-daily/test_latest.py`
Expected: OK (8 tests passed)

- [ ] **Step 3.5: 提交**

```bash
git add scripts/ai-daily/latest.py scripts/ai-daily/test_latest.py
git commit -m "feat(ai-daily): 添加 latest.json 重建模块（兼容旧 md + 新目录）"
```

---

## Task 4: 重写 fetch.py（主入口编排）

**Files:**
- Modify: `scripts/ai-daily/fetch.py`（完全重写）

- [ ] **Step 4.1: 备份并重写 fetch.py**

将 `scripts/ai-daily/fetch.py` 完全替换为：

```python
#!/usr/bin/env python3
"""生成 AI 日报 Hugo 页面：从 aihot.virxact.com 拉取数据，输出 branch bundle 结构。

输出：
- content/ai-daily/{date}/_index.md       日报索引页
- content/ai-daily/{date}/{NN}-{slug}.md  单篇详情页
- data/ai-daily/latest.json               最近 7 天索引
"""

from __future__ import annotations

import datetime as dt
import os
import pathlib
import shutil
import sys
from zoneinfo import ZoneInfo

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from aihot_client import fetch_daily
from latest import rebuild_latest_json
from markdown_builder import build_daily_index, build_item_pages


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content" / "ai-daily"
DATA_DIR = ROOT / "data" / "ai-daily"

TIMEZONE = os.getenv("AI_DAILY_TIMEZONE", "Asia/Shanghai")
DATE_OVERRIDE = os.getenv("AI_DAILY_DATE", "").strip()
MAX_ITEMS = int(os.getenv("AI_DAILY_MAX_ITEMS", "50"))


def get_target_date() -> dt.date:
    """获取目标日期：优先 AI_DAILY_DATE 环境变量，否则用指定时区的当天。"""
    if DATE_OVERRIDE:
        return dt.date.fromisoformat(DATE_OVERRIDE)
    return dt.datetime.now(ZoneInfo(TIMEZONE)).date()


def write_daily_pages(
    target_date: dt.date, sections: list[dict]
) -> tuple[int, pathlib.Path]:
    """写出日报索引页和单篇详情页，返回 (篇数, 目录路径)。"""
    date_dir = CONTENT_DIR / target_date.isoformat()
    # 清理旧文件（同日重跑场景）：删除目录内所有 md，保留目录本身
    if date_dir.exists():
        for md_file in date_dir.glob("*.md"):
            md_file.unlink()
    else:
        date_dir.mkdir(parents=True, exist_ok=True)

    # 限制单日 item 数量，防止异常数据爆盘
    truncated_sections: list[dict] = []
    remaining = MAX_ITEMS
    for section in sections:
        if remaining <= 0:
            break
        items = section.get("items", [])[:remaining]
        truncated_sections.append({**section, "items": items})
        remaining -= len(items)

    # 写日报索引
    index_md = build_daily_index(target_date, truncated_sections)
    (date_dir / "_index.md").write_text(index_md, encoding="utf-8")

    # 写单篇详情
    pages = build_item_pages(target_date, truncated_sections)
    for filename, content in pages:
        (date_dir / filename).write_text(content, encoding="utf-8")

    return len(pages), date_dir


def main() -> int:
    """主入口：取日期→拉数据→写文件→更新 latest.json。"""
    target_date = get_target_date()
    data = fetch_daily(target_date)

    if data is None:
        print(f"No source data for {target_date.isoformat()}, skipped.")
        return 0

    sections = data.get("sections", [])
    if not sections:
        print(f"Warning: empty sections for {target_date.isoformat()}, skipped.")
        return 0

    count, date_dir = write_daily_pages(target_date, sections)
    rebuild_latest_json()
    print(
        f"Generated AI daily for {target_date.isoformat()}: "
        f"{count} items in {date_dir.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4.2: 删除旧的测试残留（如有）**

检查并删除 `scripts/ai-daily/__pycache__/`：

```bash
rm -rf scripts/ai-daily/__pycache__
```

- [ ] **Step 4.3: 手动冒烟测试（用真实 API）**

Run: `AI_DAILY_DATE=2026-07-03 python scripts/ai-daily/fetch.py`
Expected output:
```
Generated AI daily for 2026-07-03: NN items in content/ai-daily/2026-07-03
```

- [ ] **Step 4.4: 验证生成的文件结构**

Run: `ls -la D:/blog/firstblog/content/ai-daily/2026-07-03/`
Expected: 看到 `_index.md` + 多个 `NN-*.md` 文件

Run: `head -20 D:/blog/firstblog/content/ai-daily/2026-07-03/_index.md`
Expected: 看到 frontmatter 和 section 标题

Run: `head -20 D:/blog/firstblog/content/ai-daily/2026-07-03/01-*.md`
Expected: 看到单篇详情页 frontmatter

- [ ] **Step 4.5: 验证 latest.json 更新**

Run: `cat D:/blog/firstblog/data/ai-daily/latest.json`
Expected: JSON 包含 `2026-07-03` 在 days 数组首位

- [ ] **Step 4.6: 运行全部单元测试**

Run:
```bash
python scripts/ai-daily/test_aihot_client.py
python scripts/ai-daily/test_markdown_builder.py
python scripts/ai-daily/test_latest.py
```
Expected: 三个文件均 OK，总 35 tests passed

- [ ] **Step 4.7: 提交**

```bash
git add scripts/ai-daily/fetch.py
git commit -m "feat(ai-daily): 重写 fetch.py 使用 aihot API + branch bundle 输出

- 删除 HexTopProjectParser/Playwright 兜底等 392 行旧代码
- 改用 aihot.virxact.com JSON API
- 输出 content/ai-daily/{date}/_index.md + 单篇 md"
```

---

## Task 5: 端到端验证与清理

**Files:**
- Verify: `content/ai-daily/2026-07-03/`
- Verify: `data/ai-daily/latest.json`
- Verify: 旧 hex2077 文件未被破坏

- [ ] **Step 5.1: 验证旧 hex2077 文件未被破坏**

Run: `ls D:/blog/firstblog/content/ai-daily/2026-05-*.md | head -5`
Expected: 看到 `2026-05-15.md` 等旧文件仍在

Run: `head -5 D:/blog/firstblog/content/ai-daily/2026-05-15.md`
Expected: 旧 hex2077 内容（"开源 TOP 项目"）仍在

- [ ] **Step 5.2: 同日重跑幂等性测试**

再次运行：`AI_DAILY_DATE=2026-07-03 python scripts/ai-daily/fetch.py`

Run: `ls D:/blog/firstblog/content/ai-daily/2026-07-03/*.md | wc -l`
Expected: 文件数与第一次运行相同（无残留旧文件）

- [ ] **Step 5.3: 测试 404 场景**

Run: `AI_DAILY_DATE=2025-01-01 python scripts/ai-daily/fetch.py`
Expected output:
```
No source data for 2025-01-01, skipped.
```
退出码 0。

Run: `echo $?`
Expected: `0`

- [ ] **Step 5.4: 验证 Hugo 能构建（如果 hugo 可用）**

Run: `cd D:/blog/firstblog && ./hugo.exe --quiet --buildDrafts 2>&1 | head -20`
Expected: 无错误，或仅有无关警告

如果 hugo 不在 PATH，跳过此步并记录：
```
Note: hugo not available for local build verification. Server will verify on next deploy.
```

- [ ] **Step 5.5: 清理测试残留**

如果 Step 5.3 生成了任何文件（不应该），清理：
```bash
ls D:/blog/firstblog/content/ai-daily/2025-01-01 2>/dev/null && rm -rf D:/blog/firstblog/content/ai-daily/2025-01-01
```

- [ ] **Step 5.6: 提交最终生成的日报内容**

```bash
git add content/ai-daily/2026-07-03 data/ai-daily/latest.json
git commit -m "chore: update ai daily 2026-07-03 from aihot.virxact.com"
```

---

## Task 6: 更新 AGENTS.md 文档

**Files:**
- Modify: `AGENTS.md`

- [ ] **Step 6.1: 读取当前 AGENTS.md 内容**

Run: `cat D:/blog/firstblog/AGENTS.md`

记下需要修改的段落：
- "scripts/ai-daily/ 负责从来源页面抓取 AI 日报数据..."
- "AI 日报浏览器兜底抓取默认等待 DOM 就绪后..."
- "AI 日报浏览器兜底等待策略使用 AI_DAILY_BROWSER_WAIT_UNTIL..."

- [ ] **Step 6.2: 更新 AGENTS.md**

将以下段落替换：

旧：
```
- `scripts/ai-daily/` 负责从来源页面抓取 AI 日报数据，并生成 `content/ai-daily/*.md` 与 `data/ai-daily/latest.json`。
- 自动化脚本应优先保证生成内容稳定、可追踪，失败时输出明确错误信息。
- AI 日报浏览器兜底抓取默认等待 DOM 就绪后，再等待 GitHub 项目链接出现，避免 `networkidle` 被长连接或懒加载误拖超时。
```

新：
```
- `scripts/ai-daily/` 从 `aihot.virxact.com` JSON API 抓取 AI 日报数据，生成 `content/ai-daily/{date}/_index.md`（日报索引）+ `content/ai-daily/{date}/{NN}-{slug}.md`（单篇详情）+ `data/ai-daily/latest.json`。
- 自动化脚本应优先保证生成内容稳定、可追踪，失败时输出明确错误信息。
- API 基址可通过 `AIHOT_API_BASE` 环境变量覆盖；HTTP 404 视为当天无数据，正常退出。
```

旧：
```
- AI 日报浏览器兜底等待策略使用 `AI_DAILY_BROWSER_WAIT_UNTIL`、`AI_DAILY_BROWSER_CONTENT_TIMEOUT`、`AI_DAILY_BROWSER_DISMISS_TIMEOUT` 和 `AI_DAILY_FETCH_TIMEOUT` 配置。
```

新：
```
- AI 日报抓取使用 `AIHOT_API_BASE`、`AI_DAILY_FETCH_RETRIES`、`AI_DAILY_FETCH_TIMEOUT`、`AI_DAILY_TIMEZONE`、`AI_DAILY_DATE` 配置。
```

旧目录结构段：
```
- `content/ai-daily/`：AI 日报生成结果。
```

新：
```
- `content/ai-daily/`：AI 日报生成结果。新结构为 `{date}/_index.md` + `{date}/{NN}-{slug}.md`（branch bundle）；旧 hex2077 文件保留为顶层 `{date}.md` 历史归档。
```

- [ ] **Step 6.3: 提交文档更新**

```bash
git add AGENTS.md
git commit -m "docs: 更新 AGENTS.md 反映 aihot API 源与 branch bundle 结构"
```

---

## Self-Review 自审记录

**Spec 覆盖检查**：
- ✅ 替换数据源 → Task 1 (aihot_client) + Task 4 (fetch.py)
- ✅ 删除 HTML/Playwright 代码 → Task 4 (fetch.py 重写)
- ✅ 每篇独立 md → Task 2 (build_item_pages)
- ✅ Hugo branch bundle → Task 2 (build_daily_index 用作 _index.md) + Task 4 (write_daily_pages)
- ✅ 保留 latest.json → Task 3 (latest.py)
- ✅ 服务器 cron 不变 → Task 6 (AGENTS.md 不提 workflow 调度变更)
- ✅ 单文件 ≤200 行 → 各模块行数估计 55/115/45/75
- ✅ slug 算法 → Task 2.A
- ✅ 错误处理 6 类 → Task 1 (404/重试) + Task 4 (空 sections/写文件失败)
- ✅ 旧文件迁移 → Task 5.1 验证
- ✅ 同日重跑 → Task 4 (write_daily_pages 清理旧 md) + Task 5.2 验证
- ✅ 9 个测试用例 → Tasks 1-3 共 35 个 unittest 用例覆盖

**类型一致性检查**：
- `fetch_daily(target_date: dt.date) -> dict | None` — Task 1 定义，Task 4 调用 ✓
- `build_daily_index(target_date, sections) -> str` — Task 2 定义，Task 4 调用 ✓
- `build_item_pages(target_date, sections) -> list[tuple[str, str]]` — Task 2 定义，Task 4 调用 ✓
- `rebuild_latest_json() -> None` — Task 3 定义，Task 4 调用 ✓
- `_iter_valid_items(sections) -> list[tuple[int, str, dict]]` — Task 2 内部辅助 ✓

**占位符扫描**：无 TBD/TODO，所有代码块完整。

**已知偏离 spec**：
- spec 说测试置于 `test_fetch.py`，计划拆为 `test_aihot_client.py`/`test_markdown_builder.py`/`test_latest.py`（更清晰）
- spec 说用 pytest，计划用 unittest（避免新增依赖，符合"暂不强制加 CI"）
