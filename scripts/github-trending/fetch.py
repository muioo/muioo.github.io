#!/usr/bin/env python3
"""生成 GitHub 趋势 Hugo 页面：抓取 github.com/trending，输出每日叶子页面。

输出：
- content/github-trending/{date}.md      每日趋势页
- data/github-trending/latest.json       最近 7 天索引
"""

from __future__ import annotations

import datetime as dt
import os
import pathlib
import sys
from zoneinfo import ZoneInfo

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from latest import rebuild_latest_json
from markdown_builder import build_day_page
from trending_client import fetch_trending


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content" / "github-trending"
DATA_DIR = ROOT / "data" / "github-trending"

TIMEZONE = os.getenv("GH_TRENDING_TIMEZONE", "Asia/Shanghai")
DATE_OVERRIDE = os.getenv("GH_TRENDING_DATE", "").strip()
MAX_ITEMS = int(os.getenv("GH_TRENDING_MAX_ITEMS", "25"))
PERIOD = os.getenv("GH_TRENDING_PERIOD", "daily").strip()


def get_target_date() -> dt.date:
    """获取目标日期：优先 GH_TRENDING_DATE 环境变量，否则用指定时区的当天。"""
    if DATE_OVERRIDE:
        return dt.date.fromisoformat(DATE_OVERRIDE)
    return dt.datetime.now(ZoneInfo(TIMEZONE)).date()


def write_day_page(target_date: dt.date, repos: list[dict]) -> pathlib.Path:
    """写出某天的趋势页（同日重跑直接覆盖），返回文件路径。"""
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    page_path = CONTENT_DIR / f"{target_date.isoformat()}.md"
    page_path.write_text(build_day_page(target_date, repos), encoding="utf-8")
    return page_path


def cleanup_expired_pages(
    content_dir: pathlib.Path | None = None,
    retention_days: int | None = None,
) -> int:
    """删除超过保留期限的每日趋势页文件，返回删除的文件个数。

    仅处理形如 'YYYY-MM-DD.md'、且日期早于（今天 - 保留期限）的文件；
    _index.md 等非日期命名文件一律保留。清理不中断主流程，临时异常仅记录到标准错误。
    """
    if content_dir is None:
        content_dir = CONTENT_DIR
    if retention_days is None:
        retention_days = int(os.getenv("GH_TRENDING_RETENTION_DAYS", "90"))

    now = dt.datetime.now(ZoneInfo(TIMEZONE)).date()
    cutoff = now - dt.timedelta(days=retention_days)
    removed = 0

    for path in sorted(content_dir.glob("*.md")):
        if path.name == "_index.md":
            continue
        try:
            candidate = dt.date.fromisoformat(path.stem)
        except ValueError:
            # 非日期命名的文件（如说明文档），不参与清理
            continue
        if candidate < cutoff:
            path.unlink()
            removed += 1
    return removed


def main() -> int:
    """主入口：取日期→抓取→写页面→更新 latest.json→清理过期。"""
    target_date = get_target_date()
    try:
        repos = fetch_trending(PERIOD)
    except ValueError as exc:
        # 非法的周期配置属于配置错误，输出明确信息后退出
        print(f"Invalid GH_TRENDING_PERIOD={PERIOD!r}: {exc}", file=sys.stderr)
        return 1

    if repos is None:
        print(f"No trending data for period={PERIOD}, skipped.")
        return 0
    if not repos:
        # 页面抓取成功但解析出 0 条，几乎可以确定是页面结构变化，必须大声失败
        raise RuntimeError(
            f"Fetched trending page for period={PERIOD} but parsed 0 repositories; "
            "the page structure may have changed."
        )

    truncated = repos[:MAX_ITEMS]
    page_path = write_day_page(target_date, truncated)
    rebuild_latest_json()
    removed = cleanup_expired_pages()
    print(
        f"Generated GitHub trending for {target_date.isoformat()}: "
        f"{len(truncated)} repos in {page_path.relative_to(ROOT)}"
    )
    if removed:
        print(f"Cleaned up {removed} expired GitHub trending page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
