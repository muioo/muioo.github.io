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
