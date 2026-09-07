#!/usr/bin/env python3
"""latest 单元测试。"""
from __future__ import annotations

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
        """创建临时 content/github-trending 与 data/github-trending 目录。"""
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmpdir.name)
        self.content_dir = self.root / "content" / "github-trending"
        self.data_dir = self.root / "data" / "github-trending"
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

    def test_scan_date_files_only(self) -> None:
        """只收录 YYYY-MM-DD.md 命名文件，_index.md 忽略。"""
        (self.content_dir / "2026-09-06.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "2026-09-07.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "_index.md").write_text("---\n---\n", encoding="utf-8")
        (self.content_dir / "random.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        dates = [d["date"] for d in data["days"]]
        self.assertEqual(dates, ["2026-09-07", "2026-09-06"])

    def test_sorted_descending_and_limited_to_7(self) -> None:
        """日期降序排列且最多 7 条。"""
        for i in range(10):
            d = f"2026-09-{i + 1:02d}"
            (self.content_dir / f"{d}.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        self.assertEqual(len(data["days"]), 7)
        self.assertEqual(data["days"][0]["date"], "2026-09-10")

    def test_url_and_title_format(self) -> None:
        """URL 与标题格式。"""
        (self.content_dir / "2026-09-07.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        self.assertEqual(data["days"][0]["url"], "/github-trending/2026-09-07/")
        self.assertEqual(data["days"][0]["title"], "GitHub 趋势 | 2026-09-07")

    def test_updated_at_is_iso_format(self) -> None:
        """updated_at 是 ISO 8601 格式。"""
        (self.content_dir / "2026-09-07.md").write_text("---\n---\n", encoding="utf-8")
        with self._patch_dirs():
            rebuild_latest_json()
        data = json.loads(self.latest_file.read_text(encoding="utf-8"))
        self.assertIn("updated_at", data)
        self.assertTrue(data["updated_at"].endswith("Z"))


if __name__ == "__main__":
    unittest.main()
