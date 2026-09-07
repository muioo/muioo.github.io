"""测试 cleanup_expired_daily 的历史 AI 日报目录清理逻辑。

使用临时目录隔离，不触碰真实 content/。
"""

from __future__ import annotations

import datetime as dt
import shutil
import tempfile
from pathlib import Path

from fetch import cleanup_expired_daily


def _touch_daily(base: Path, date: dt.date) -> Path:
    """在临时目录下构造一个 YYYY-MM-DD 日报目录，内含索引文件。"""
    date_dir = base / date.isoformat()
    date_dir.mkdir(parents=True, exist_ok=True)
    (date_dir / "_index.md").write_text("test", encoding="utf-8")
    return date_dir


def test_only_expired_dirs_removed():
    """仅删除早于保留期限的日期目录，保留期内/非法名目录保留。"""
    today = dt.date.today()
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        expired = _touch_daily(base, today - dt.timedelta(days=91))  # 91 天前，应删
        boundary = _touch_daily(base, today - dt.timedelta(days=90))  # 恰在边界，保留
        today_dir = _touch_daily(base, today)  # 当天，保留
        _touch_daily(base, today + dt.timedelta(days=1))  # 未来，保留

        # 非法命名目录
        non_date = base / "not-a-date"
        if non_date.is_dir():  # 与某日期目录路径不冲突，安全创建
            shutil.rmtree(non_date)
        non_date.mkdir()
        (non_date / "x.md").write_text("x", encoding="utf-8")

        removed = cleanup_expired_daily(base, retention_days=90)

        assert removed == 1, removed
        assert not expired.exists()
        assert boundary.exists()
        assert today_dir.exists()
        assert non_date.exists()


def test_single_file_like_entry_ignored():
    """非目录条目（如顶层历史归档 {date}.md 单文件）不被清理。"""
    today = dt.date.today()
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        # 顶层单文件历史归档
        archive_file = base / ((today - dt.timedelta(days=500)).isoformat() + ".md")
        archive_file.write_text("old archive", encoding="utf-8")
        # 同时间的历史目录
        old_dir = _touch_daily(base, today - dt.timedelta(days=500))

        removed = cleanup_expired_daily(base, retention_days=90)

        assert removed == 1, removed
        assert archive_file.exists()  # 单文件归档保留
        assert not old_dir.exists()  # 日期目录仍被清理