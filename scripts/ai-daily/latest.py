#!/usr/bin/env python3
"""重建 data/ai-daily/latest.json 索引文件。"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content" / "ai-daily"
DATA_DIR = ROOT / "data" / "ai-daily"
LATEST_FILE = DATA_DIR / "latest.json"

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"
MAX_ENTRIES = 7


def rebuild_latest_json() -> None:
    """扫描 content/ai-daily/ 下的旧 md 文件与新日期目录，重建 latest.json。

    兼容两种结构：
    - 旧：content/ai-daily/YYYY-MM-DD.md（hex2077 历史文件）
    - 新：content/ai-daily/YYYY-MM-DD/（branch bundle 目录）

    同日期两者并存时按日期字符串去重，仅保留一条。
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    dates: set[str] = set()

    # 扫描旧结构：顶层 YYYY-MM-DD.md 文件
    for path in CONTENT_DIR.glob("*.md"):
        if path.name == "_index.md":
            continue
        if re.fullmatch(f"{DATE_PATTERN}\\.md", path.name):
            dates.add(path.stem)

    # 扫描新结构：YYYY-MM-DD/ 目录
    for path in CONTENT_DIR.iterdir():
        if path.is_dir() and re.fullmatch(DATE_PATTERN, path.name):
            dates.add(path.name)

    entries = [
        {
            "date": date_str,
            "title": f"AI日报 | {date_str}",
            "url": f"/ai-daily/{date_str}/",
        }
        for date_str in sorted(dates, reverse=True)[:MAX_ENTRIES]
    ]

    payload = {
        "updated_at": (
            dt.datetime.now(dt.timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        ),
        "days": entries,
    }

    LATEST_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
