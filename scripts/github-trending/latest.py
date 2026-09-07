#!/usr/bin/env python3
"""重建 data/github-trending/latest.json 索引文件。"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content" / "github-trending"
DATA_DIR = ROOT / "data" / "github-trending"
LATEST_FILE = DATA_DIR / "latest.json"

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"
MAX_ENTRIES = 7


def rebuild_latest_json() -> None:
    """扫描 content/github-trending/ 下的每日叶子页面，重建 latest.json。

    仅识别顶层 YYYY-MM-DD.md 命名文件；_index.md 等非日期文件一律忽略。
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    dates: set[str] = set()
    for path in CONTENT_DIR.glob("*.md"):
        if path.name == "_index.md":
            continue
        if re.fullmatch(f"{DATE_PATTERN}\\.md", path.name):
            dates.add(path.stem)

    entries = [
        {
            "date": date_str,
            "title": f"GitHub 趋势 | {date_str}",
            "url": f"/github-trending/{date_str}/",
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
