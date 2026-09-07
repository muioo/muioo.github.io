#!/usr/bin/env python3
"""测试 cleanup_expired_pages 的历史趋势页清理逻辑。

使用临时目录隔离，不触碰真实 content/。
"""

from __future__ import annotations

import datetime as dt
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from fetch import cleanup_expired_pages


def _touch_page(base: pathlib.Path, date: dt.date) -> pathlib.Path:
    """在临时目录下构造一个 YYYY-MM-DD.md 趋势页。"""
    page = base / f"{date.isoformat()}.md"
    page.write_text("test", encoding="utf-8")
    return page


def test_only_expired_pages_removed():
    """仅删除早于保留期限的日期页面，保留期内/非法名文件保留。"""
    today = dt.date.today()
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)

        expired = _touch_page(base, today - dt.timedelta(days=91))  # 91 天前，应删
        boundary = _touch_page(base, today - dt.timedelta(days=90))  # 恰在边界，保留
        today_page = _touch_page(base, today)  # 当天，保留
        _touch_page(base, today + dt.timedelta(days=1))  # 未来，保留

        removed = cleanup_expired_pages(base, retention_days=90)

        assert removed == 1, removed
        assert not expired.exists()
        assert boundary.exists()
        assert today_page.exists()


def test_index_and_non_date_files_kept():
    """_index.md 与非日期命名文件不被清理。"""
    today = dt.date.today()
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)

        index_file = base / "_index.md"
        index_file.write_text("archive index", encoding="utf-8")
        old_index = base / "README.md"
        old_index.write_text("doc", encoding="utf-8")
        _touch_page(base, today - dt.timedelta(days=500))

        removed = cleanup_expired_pages(base, retention_days=90)

        assert removed == 1, removed
        assert index_file.exists()
        assert old_index.exists()


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-v"]))
