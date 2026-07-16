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
            f'href="./{self.item_slug}/"',
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
menu:
    main:
        identifier: ai-daily-entry
        weight: -55
        params:
            icon: messages
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


if __name__ == "__main__":
    unittest.main()
