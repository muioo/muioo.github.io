#!/usr/bin/env python3
"""markdown_builder 单元测试。"""

from __future__ import annotations

import datetime as dt
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from markdown_builder import build_day_page

TARGET_DATE = dt.date(2026, 9, 7)


def _repo(**overrides: object) -> dict:
    """构造一个字段齐全的仓库 dict，可按需覆盖。"""
    repo = {
        "owner": "vllm-project",
        "name": "vllm",
        "url": "https://github.com/vllm-project/vllm",
        "description": "A high-throughput inference engine for LLMs.",
        "language": "Python",
        "stars_total": 45234,
        "stars_today": 1234,
        "forks": 3456,
    }
    repo.update(overrides)
    return repo


class TestBuildDayPage(unittest.TestCase):
    """验证日页 Markdown 生成。"""

    def test_frontmatter(self) -> None:
        """frontmatter 应包含标题、日期、描述。"""
        md = build_day_page(TARGET_DATE, [_repo()])
        self.assertIn('title: "GitHub 趋势 | 2026-09-07"', md)
        self.assertIn("date: 2026-09-07T08:30:00+08:00", md)
        self.assertIn('description: "2026-09-07 GitHub 热门仓库"', md)
        self.assertIn("comments: false", md)

    def test_repo_heading_with_stars_and_language(self) -> None:
        """标题行应包含排名、链接、千分位 star 与今日增量、语言。"""
        md = build_day_page(TARGET_DATE, [_repo()])
        self.assertIn(
            "### 1. [vllm-project/vllm](https://github.com/vllm-project/vllm) "
            "⭐ 45,234（今日 +1,234） · Python",
            md,
        )

    def test_omits_language_and_today_stars_when_missing(self) -> None:
        """缺语言或缺今日 star 时相应部分应省略。"""
        md = build_day_page(TARGET_DATE, [_repo(language="", stars_today=None)])
        self.assertIn(
            "### 1. [vllm-project/vllm](https://github.com/vllm-project/vllm) ⭐ 45,234",
            md,
        )
        self.assertNotIn("今日 +", md)
        self.assertNotIn("·", md.split("\n\n")[0])

    def test_omits_stars_total_when_missing(self) -> None:
        """缺总 star 时只保留链接与语言。"""
        md = build_day_page(TARGET_DATE, [_repo(stars_total=None, stars_today=None)])
        self.assertIn(
            "### 1. [vllm-project/vllm](https://github.com/vllm-project/vllm) · Python",
            md,
        )
        self.assertNotIn("⭐", md)

    def test_description_truncated_to_150_chars(self) -> None:
        """超长描述应被截断并加省略号。"""
        long_desc = "字" * 200
        md = build_day_page(TARGET_DATE, [_repo(description=long_desc)])
        self.assertIn("字" * 150 + "...", md)
        self.assertNotIn("字" * 151, md)

    def test_empty_description_omits_paragraph(self) -> None:
        """空描述时不应出现描述段落，只保留标题行。"""
        md = build_day_page(TARGET_DATE, [_repo(description="")])
        self.assertIn("### 1.", md)
        self.assertNotIn("A high-throughput", md)

    def test_multiple_repos_ranked(self) -> None:
        """多个仓库按序号排列。"""
        repos = [_repo(), _repo(owner="openai", name="openai-go", stars_total=1024)]
        md = build_day_page(TARGET_DATE, repos)
        self.assertIn("### 1.", md)
        self.assertIn("### 2. [openai/openai-go]", md)


if __name__ == "__main__":
    unittest.main()
