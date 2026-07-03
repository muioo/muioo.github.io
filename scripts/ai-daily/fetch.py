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
