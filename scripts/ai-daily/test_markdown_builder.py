#!/usr/bin/env python3
"""markdown_builder 单元测试。"""
from __future__ import annotations

import datetime as dt
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from markdown_builder import slugify, build_item_markdown, build_daily_index, build_item_pages, _truncate_description


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

    def test_short_summary_not_truncated(self) -> None:
        """短 summary（≤150 字符）不应被截断，不含省略号。"""
        short_item = {**self.item, "summary": "短摘要，不应被截断。"}
        md = build_item_markdown(self.target_date, short_item, "产品发布/更新")
        for line in md.splitlines():
            if line.startswith("description:"):
                value = line[len("description: "):].strip('"')
                self.assertFalse(value.endswith("..."))
                self.assertEqual(value, "短摘要，不应被截断。")
                break
        else:
            self.fail("description line not found")


class TestTruncateDescription(unittest.TestCase):
    """验证 _truncate_description 内部辅助函数。"""

    def test_short_text_returned_as_is(self) -> None:
        """短文本（≤150 字符）原样返回。"""
        text = "这是一段短摘要。"
        self.assertEqual(_truncate_description(text), "这是一段短摘要。")

    def test_long_text_truncated_with_ellipsis(self) -> None:
        """超长文本截断到 150 字符并加省略号。"""
        text = "字" * 200
        result = _truncate_description(text)
        self.assertEqual(len(result), 153)  # 150 + "..."
        self.assertTrue(result.endswith("..."))
        self.assertEqual(result[:150], "字" * 150)

    def test_whitespace_normalized_to_single_space(self) -> None:
        """换行和连续空格被归一化为单个空格。"""
        text = "第一行\n\n第二行\t\t第三行  末尾"
        self.assertEqual(_truncate_description(text), "第一行 第二行 第三行 末尾")


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

    def test_long_summary_truncated_in_index(self) -> None:
        """索引页摘要应截断到 150 字符+省略号，不显示全文。"""
        long_summary = "字" * 300
        sections = [
            {
                "label": "分类",
                "items": [
                    {"title": "测试标题", "summary": long_summary, "permalink": "https://x/aaa"},
                ],
            }
        ]
        md = build_daily_index(self.target_date, sections)
        # 截断后的预览应出现在索引页
        self.assertIn("字" * 150 + "...", md)
        # 全文（300 字）不应完整出现
        self.assertNotIn("字" * 300, md)

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


if __name__ == "__main__":
    unittest.main()
