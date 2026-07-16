# AI Daily Article View Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将每日 AI 日报日期页渲染为一篇包含全部新闻标题与摘要的文章，并让导航与备用入口始终指向最新日报日期页。

**Architecture:** 保留现有 `content/ai-daily/{date}/` branch bundle 和爬虫输出，只在 Hugo 模板层区分日期 section 与顶层归档 section。日期 section 复用 Stack 主题文章组件渲染 `_index.md` 的 `.Content`；顶层 section 保留归档视图；导航和备用入口统一从 `/ai-daily` 的直接子页面中选择最新日期。

**Tech Stack:** Hugo v0.154.5 Extended、Go Template、Stack Hugo Theme、Python 3 标准库 `unittest`、PowerShell。

## Global Constraints

- 不改变爬虫 API、抓取流程或 `content/ai-daily/{date}/_index.md` + `{NN}-{slug}.md` branch bundle 结构。
- 日期页只展示每条新闻的标题和摘要，标题继续链接现有详情页；不把详情全文合并进日期页。
- `/ai-daily/` 保持按月份和日期归档，不展开当天全部新闻。
- 不使用浏览器端 API 请求或 JavaScript 拼接日报内容。
- 最新日报从 Hugo 页面集合动态计算，不写死日期、URL 或端口。
- Hugo 模板新增关键分支时添加中文注释；Python 测试函数和方法必须有中文 docstring。
- 不静默吞掉构建错误；测试失败信息必须包含 Hugo 的合并输出。
- 不修改或提交 `public/`、`resources/`、`.hugo_build.lock` 与无关的未跟踪内容。
- `AGENTS.md` 保持 200 行以内，只记录项目目标、代码风格/规则与目录结构。
- 只修改本计划列出的文件；主题现有文章样式已满足需求，不修改 `assets/scss/custom.scss`。

## File Map

- Create `scripts/ai-daily/test_hugo_templates.py`：构建临时 Hugo 站点并验证日期文章、归档、导航、跳转和空状态。
- Modify `layouts/ai-daily/list.html`：根据日期 URL 在文章视图与归档视图之间分流。
- Modify `layouts/page/ai-daily-redirect.html`：从 `/ai-daily` 的直接子页面选择最新日报日期。
- Modify `AGENTS.md`：记录日期页文章化和动态最新日期规则。

---

### Task 1: Render a Daily Date Section as an Article

**Files:**
- Create: `scripts/ai-daily/test_hugo_templates.py`
- Modify: `layouts/ai-daily/list.html:1-52`

**Interfaces:**
- Consumes: `content/ai-daily/{date}/_index.md` 中的 front matter、`.Content`、二级分类标题和三级新闻链接。
- Produces: 日期页 HTML 中的 `.main-article`、`.article-content` 与详情链接；顶层归档继续产生 `.ai-daily-archive`。

- [ ] **Step 1: Write the failing Hugo rendering tests**

Create `scripts/ai-daily/test_hugo_templates.py` with the following complete content:

```python
#!/usr/bin/env python3
"""AI 日报 Hugo 模板回归测试。"""
from __future__ import annotations

import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
LATEST_DATA_PATH = ROOT / "data" / "ai-daily" / "latest.json"


def _resolve_hugo_binary() -> str:
    """优先使用环境变量，其次使用仓库 Hugo，最后查询 PATH。"""
    configured_binary = os.environ.get("HUGO_BINARY")
    if configured_binary:
        return configured_binary

    repository_binary = ROOT / "hugo.exe"
    if repository_binary.is_file():
        return str(repository_binary)

    path_binary = shutil.which("hugo")
    if path_binary:
        return path_binary

    raise RuntimeError("未找到 Hugo；请设置 HUGO_BINARY 或将 hugo 加入 PATH")


def _load_latest_day() -> tuple[str, str]:
    """读取最新日报日期及站内 URL，避免在测试中写死日期。"""
    latest_data = json.loads(LATEST_DATA_PATH.read_text(encoding="utf-8"))
    days = latest_data.get("days", [])
    if not days:
        raise AssertionError("data/ai-daily/latest.json 不包含可测试的日报日期")
    return days[0]["date"], days[0]["url"]


def _load_daily_markdown_markers(target_date: str) -> tuple[str, str, str]:
    """从日报 Markdown 提取首个分类、新闻标题和详情 slug。"""
    daily_path = ROOT / "content" / "ai-daily" / target_date / "_index.md"
    markdown = daily_path.read_text(encoding="utf-8")
    category_match = re.search(r"^##\s+(.+)$", markdown, re.MULTILINE)
    item_match = re.search(
        r"^###\s+\d+\.\s+\[([^\]]+)\]\(\./([^/]+)/\)",
        markdown,
        re.MULTILINE,
    )
    if category_match is None or item_match is None:
        raise AssertionError(f"{daily_path} 缺少可测试的分类或新闻链接")
    return category_match.group(1), item_match.group(1), item_match.group(2)


def _run_hugo_build(destination: pathlib.Path, *extra_args: str) -> str:
    """执行 Hugo 构建；失败时携带完整构建输出抛出断言。"""
    command = [
        _resolve_hugo_binary(),
        "--destination",
        str(destination),
        "--cacheDir",
        str(destination.parent / "hugo-cache"),
        "--cleanDestinationDir",
        "--noBuildLock",
        *extra_args,
    ]
    result = subprocess.run(
        command,
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(
            f"Hugo 构建失败，退出码 {result.returncode}:\n{result.stdout}"
        )
    return result.stdout


class TestHugoAIDailyTemplates(unittest.TestCase):
    """验证 AI 日报日期页和归档页的渲染边界。"""

    @classmethod
    def setUpClass(cls) -> None:
        """构建一次完整站点供模板断言复用。"""
        cls.temporary_directory = tempfile.TemporaryDirectory(
            prefix="ai-daily-hugo-test-"
        )
        cls.output_root = pathlib.Path(cls.temporary_directory.name) / "public"
        cls.latest_date, cls.latest_url = _load_latest_day()
        cls.category, cls.item_title, cls.item_slug = _load_daily_markdown_markers(
            cls.latest_date
        )
        _run_hugo_build(cls.output_root)

    @classmethod
    def tearDownClass(cls) -> None:
        """释放测试构建产生的临时目录。"""
        cls.temporary_directory.cleanup()

    def _read_output(self, *parts: str) -> str:
        """按 UTF-8 读取指定构建产物。"""
        output_path = self.output_root.joinpath(*parts)
        return output_path.read_text(encoding="utf-8")

    def test_daily_date_page_renders_article_content(self) -> None:
        """日期页应渲染文章正文、分类、新闻标题与详情链接。"""
        daily_html = self._read_output(
            "ai-daily", self.latest_date, "index.html"
        )

        self.assertIn('<article class="main-article">', daily_html)
        self.assertIn('<section class="article-content">', daily_html)
        self.assertIn('<h2 id="', daily_html)
        self.assertIn(html.escape(self.category), daily_html)
        self.assertIn(html.escape(self.item_title), daily_html)
        self.assertIn(
            f'href="/ai-daily/{self.latest_date}/{self.item_slug}/"',
            daily_html,
        )
        self.assertNotIn('<section class="ai-daily-archive">', daily_html)

    def test_top_level_page_remains_archive(self) -> None:
        """顶层 AI 日报页应保留归档视图且不渲染文章正文。"""
        archive_html = self._read_output("ai-daily", "index.html")

        archive_marker = '<section class="ai-daily-archive">'
        self.assertIn(archive_marker, archive_html)
        archive_section = archive_html.split(archive_marker, 1)[1].split(
            "</section>", 1
        )[0]
        self.assertIn(self.latest_url, archive_section)
        self.assertNotIn('<section class="article-content">', archive_html)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the date-page test and verify the current template fails**

Run:

```powershell
python scripts/ai-daily/test_hugo_templates.py -v
```

Expected: both tests fail: the current date page lacks `<article class="main-article">`, and the current top-level archive uses `.RegularPages`, so its archive section omits the latest branch-bundle date page.

- [ ] **Step 3: Add article/archive branching to the AI daily list template**

Replace `layouts/ai-daily/list.html` with:

```go-html-template
{{ define "body-class" }}
    {{- /* 日期 section 复用文章页 body class 与目录状态；顶层归档保持列表页状态。 */ -}}
    {{- $isDailyIndex := gt (len (findRE `^/ai-daily/\d{4}-\d{2}-\d{2}/?$` .RelPermalink)) 0 -}}
    {{- if $isDailyIndex -}}
        article-page
        {{- $hasWidgetNotTOC := false -}}
        {{- $tocWidgetEnabled := false -}}
        {{- range .Site.Params.widgets.page -}}
            {{- if ne .type "toc" -}}
                {{- $hasWidgetNotTOC = true -}}
            {{- else -}}
                {{- $tocWidgetEnabled = true -}}
            {{- end -}}
        {{- end -}}
        {{- $tocEnabled := and (not (eq .Params.toc false)) $tocWidgetEnabled -}}
        {{- $hasTOC := ge (len .TableOfContents) 100 -}}
        {{- .Scratch.Set "TOCEnabled" (and $tocEnabled $hasTOC) -}}
        {{- .Scratch.Set "hasWidget" (or $hasWidgetNotTOC (and $tocEnabled $hasTOC)) -}}
    {{- end -}}
{{ end }}

{{ define "main" }}
    {{- /* 日期页直接渲染已生成的 _index.md 正文；顶层 /ai-daily/ 继续显示历史归档。 */ -}}
    {{- $isDailyIndex := gt (len (findRE `^/ai-daily/\d{4}-\d{2}-\d{2}/?$` .RelPermalink)) 0 -}}

    {{ if $isDailyIndex }}
        {{ partial "article/article.html" . }}
    {{ else }}
        <header>
            <h3 class="section-title">AI日报</h3>
            <div class="section-card">
                <div class="section-details">
                    <h3 class="section-count">共 {{ len .Pages }} 篇</h3>
                    <h1 class="section-term">{{ .Title }}</h1>
                    {{ with .Params.description }}
                        <h2 class="section-description">{{ . }}</h2>
                    {{ end }}
                </div>
            </div>
        </header>

        {{/* 直接子页面同时覆盖旧日期 Markdown 和新日期 section，不包含单条新闻详情。 */}}
        {{ $pages := .Pages.ByDate.Reverse }}
        {{ $grouped := $pages.GroupByDate "2006-01" }}

        <section class="ai-daily-archive">
            {{ range $index, $group := $grouped }}
                <details class="ai-daily-month" {{ if eq $index 0 }}open{{ end }}>
                    <summary class="ai-daily-month-summary">
                        <span>{{ $group.Key }}</span>
                        <span>{{ len $group.Pages }} 篇</span>
                    </summary>
                    <div class="ai-daily-month-list">
                        {{ range $group.Pages }}
                            <article class="ai-daily-month-item">
                                <a href="{{ .RelPermalink }}" class="ai-daily-month-link">
                                    <span class="ai-daily-month-date">{{ .Date.Format "2006-01-02" }}</span>
                                    <span class="ai-daily-month-title">{{ .Title }}</span>
                                </a>
                            </article>
                        {{ end }}
                    </div>
                </details>
            {{ end }}
        </section>
    {{ end }}

    {{ partialCached "footer/footer" . }}
{{ end }}

{{ define "right-sidebar" }}
    {{- /* 日期页使用文章目录，归档页继续使用首页小组件。 */ -}}
    {{- $isDailyIndex := gt (len (findRE `^/ai-daily/\d{4}-\d{2}-\d{2}/?$` .RelPermalink)) 0 -}}
    {{ if $isDailyIndex }}
        {{ if .Scratch.Get "hasWidget" }}
            {{ partial "sidebar/right.html" (dict "Context" . "Scope" "page") }}
        {{ end }}
    {{ else }}
        {{ partial "sidebar/right.html" (dict "Context" . "Scope" "homepage") }}
    {{ end }}
{{ end }}
```

- [ ] **Step 4: Run the template tests and verify both pass**

Run:

```powershell
python scripts/ai-daily/test_hugo_templates.py -v
```

Expected: 2 tests pass; Hugo build output contains no template error.

- [ ] **Step 5: Commit the article rendering change**

Run:

```powershell
git add scripts/ai-daily/test_hugo_templates.py layouts/ai-daily/list.html
git commit -m "feat(ai-daily): render daily index as article"
```

Expected: one commit containing only the new template test and `layouts/ai-daily/list.html`.

---

### Task 2: Keep Navigation and Redirect on the Latest Date Page

**Files:**
- Modify: `scripts/ai-daily/test_hugo_templates.py`
- Modify: `layouts/page/ai-daily-redirect.html:1-31`

**Interfaces:**
- Consumes: `.Site.GetPage "/ai-daily"` and its direct `.Pages`, ordered with `.ByDate.Reverse`.
- Produces: navigation and `/ai-daily-entry/` target `/ai-daily/{latest-date}/`; empty content produces an explicit message and no redirect script.

- [ ] **Step 1: Add failing latest-target and empty-state tests**

Add these methods inside `TestHugoAIDailyTemplates`, after `test_top_level_page_remains_archive`:

```python
    def test_navigation_and_redirect_use_latest_date_page(self) -> None:
        """导航与备用入口都应使用 latest.json 对应的日报日期 URL。"""
        home_html = self._read_output("index.html")
        redirect_html = self._read_output("ai-daily-entry", "index.html")

        self.assertIn(f"<a href='{self.latest_url}'", home_html)
        self.assertIn("<span>AI日报 | Daily</span>", home_html)
        self.assertIn(
            f'window.location.replace("{self.latest_url}");',
            redirect_html,
        )

    def test_redirect_without_daily_pages_shows_empty_state(self) -> None:
        """没有任何日报日期页时应提示无内容，且不得执行跳转。"""
        fixture_root = pathlib.Path(self.temporary_directory.name) / "empty-content"
        entry_directory = fixture_root / "page" / "ai-daily"
        daily_directory = fixture_root / "ai-daily"
        entry_directory.mkdir(parents=True)
        daily_directory.mkdir(parents=True)
        (entry_directory / "index.md").write_text(
            """---
title: AI日报 | Daily
slug: ai-daily-entry
layout: ai-daily-redirect
comments: false
---
""",
            encoding="utf-8",
        )
        (daily_directory / "_index.md").write_text(
            """---
title: AI日报
comments: false
---
""",
            encoding="utf-8",
        )
        empty_output = pathlib.Path(self.temporary_directory.name) / "empty-public"

        _run_hugo_build(empty_output, "--contentDir", str(fixture_root))
        home_html = (empty_output / "index.html").read_text(encoding="utf-8")
        redirect_html = (
            empty_output / "ai-daily-entry" / "index.html"
        ).read_text(encoding="utf-8")

        self.assertIn("href='/ai-daily-entry/'", home_html)
        self.assertIn("当前还没有可用的 AI 日报内容。", redirect_html)
        self.assertNotIn("window.location.replace", redirect_html)
```

- [ ] **Step 2: Run the redirect tests and verify the existing selector fails**

Run:

```powershell
python scripts/ai-daily/test_hugo_templates.py -v
```

Expected: `test_navigation_and_redirect_use_latest_date_page` fails because `/ai-daily-entry/` currently redirects to a detail URL such as `/ai-daily/{date}/{slug}/`; the empty-state test passes.

- [ ] **Step 3: Select the latest direct child of the AI daily section**

Replace `layouts/page/ai-daily-redirect.html` with:

```go-html-template
{{ define "main" }}
    {{- /* 只读取 /ai-daily 的直接子页面，避免把单条新闻详情当成最新日报。 */ -}}
    {{- $dailyPage := .Site.GetPage "/ai-daily" -}}
    {{- $dailyPages := slice -}}
    {{- if $dailyPage -}}
        {{- $dailyPages = $dailyPage.Pages -}}
    {{- end -}}
    {{- $latestDaily := "" -}}
    {{- if gt (len $dailyPages) 0 -}}
        {{- $latestDaily = (index ($dailyPages.ByDate.Reverse) 0).RelPermalink -}}
    {{- end -}}

    <article class="main-article">
        <header class="article-header">
            <h1 class="article-title">{{ .Title }}</h1>
            <h2 class="article-subtitle">正在跳转到最新日报</h2>
        </header>

        <section class="article-content">
            {{ if $latestDaily }}
                <p>如果没有自动跳转，请点击：<a href="{{ $latestDaily }}">查看最新 AI 日报</a></p>
                <script>
                    window.location.replace({{ printf "%q" $latestDaily | safeJS }});
                </script>
            {{ else }}
                <p>当前还没有可用的 AI 日报内容。</p>
            {{ end }}
        </section>
    </article>

    {{ partialCached "footer/footer" . }}
{{ end }}

{{ define "right-sidebar" }}
    {{ partial "sidebar/right.html" (dict "Context" . "Scope" "page") }}
{{ end }}
```

- [ ] **Step 4: Run all Hugo template tests**

Run:

```powershell
python scripts/ai-daily/test_hugo_templates.py -v
```

Expected: 4 tests pass; the redirect assertion contains exactly the latest date URL and no detail slug.

- [ ] **Step 5: Commit the latest-date selector change**

Run:

```powershell
git add scripts/ai-daily/test_hugo_templates.py layouts/page/ai-daily-redirect.html
git commit -m "fix(ai-daily): redirect to latest daily page"
```

Expected: one commit containing the redirect regression tests and selector fix.

---

### Task 3: Document the Rules and Run Full Regression Verification

**Files:**
- Modify: `AGENTS.md:1-36`

**Interfaces:**
- Consumes: the completed template behavior from Tasks 1 and 2.
- Produces: project-level maintenance rules for future AI daily template and navigation changes.

- [ ] **Step 1: Update the project goal and template rules**

Add this bullet under `# 项目目标`, immediately after the AI 日报生成结构 bullet:

```markdown
- AI 日报日期页以文章形式渲染 `_index.md` 中的分类、标题和摘要；标题链接到单篇详情，顶层 `/ai-daily/` 保留日期归档。
```

Add this bullet under `# 代码风格 / 命名 / 格式`, immediately after the AI 日报环境变量 bullet:

```markdown
- 导航栏和备用入口必须从 `/ai-daily` 的直接子页面动态选择最新日报日期，不得写死日期，也不得从 `.Site.RegularPages` 选择单条详情。
```

Add this bullet under `# 目录结构`, immediately after the `layouts/` bullet:

```markdown
- `layouts/ai-daily/`：AI 日报日期文章视图与顶层归档视图；日期页复用主题文章组件。
```

- [ ] **Step 2: Run all Python tests**

Run:

```powershell
python -m unittest discover -s scripts/ai-daily -p "test_*.py" -v
```

Expected: all existing crawler tests and the 4 Hugo template tests pass; no test is skipped.

- [ ] **Step 3: Run a production-style Hugo build outside the repository output tree**

Run:

```powershell
.\hugo.exe --destination "$env:TEMP\firstblog-ai-daily-verification" --cacheDir "$env:TEMP\firstblog-hugo-cache" --cleanDestinationDir --noBuildLock
```

Expected: exit code 0, no template error, and the summary reports generated pages.

- [ ] **Step 4: Verify generated HTML targets and view types**

Run:

```powershell
$latest = (Get-Content -Raw -Encoding utf8 data/ai-daily/latest.json | ConvertFrom-Json).days[0]
$dailyHtml = Get-Content -Raw -Encoding utf8 "$env:TEMP\firstblog-ai-daily-verification\ai-daily\$($latest.date)\index.html"
$archiveHtml = Get-Content -Raw -Encoding utf8 "$env:TEMP\firstblog-ai-daily-verification\ai-daily\index.html"
$redirectHtml = Get-Content -Raw -Encoding utf8 "$env:TEMP\firstblog-ai-daily-verification\ai-daily-entry\index.html"
if ($dailyHtml -notmatch '<article class="main-article">') { throw '最新日报未渲染为文章' }
if ($dailyHtml -match '<section class="ai-daily-archive">') { throw '最新日报仍渲染为归档' }
if ($archiveHtml -notmatch '<section class="ai-daily-archive">') { throw '顶层日报归档缺失' }
if ($redirectHtml -notmatch [regex]::Escape("window.location.replace(`"$($latest.url)`");")) { throw '备用入口未指向最新日报日期' }
```

Expected: exit code 0 and no exception output.

- [ ] **Step 5: Check repository scope and formatting**

Run:

```powershell
git diff --check
git status --short
$agentsLineCount = (Get-Content -Encoding utf8 AGENTS.md).Count
if ($agentsLineCount -gt 200) { throw "AGENTS.md 超过 200 行：$agentsLineCount" }
```

Expected: no whitespace errors; `AGENTS.md` 不超过 200 行；only `AGENTS.md` is uncommitted at this task boundary, while the user's pre-existing untracked content remains untouched.

- [ ] **Step 6: Commit the project documentation**

Run:

```powershell
git add AGENTS.md
git commit -m "docs: record AI daily rendering rules"
```

Expected: one documentation-only commit; `public/`, `resources/`, `.hugo_build.lock`, temporary output, and unrelated content are absent from the commit.

## Completion Review

After all tasks:

1. Run `git log -3 --oneline` and verify the article rendering, redirect fix, and documentation commits exist.
2. Run `git status --short` and confirm only the user's pre-existing unrelated files remain untracked.
3. Report the changed behavior, verification commands and results.
4. List residual risks: unusually long titles, empty `_index.md` bodies, missing `latest.json`, and mobile wrapping.
5. Recommend manual browser checks for desktop width, mobile width, category table of contents, title wrapping, summary spacing, and detail-link navigation.
