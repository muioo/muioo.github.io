#!/usr/bin/env python3
"""生成 GitHub 趋势日页 Markdown（每日一个叶子页面）。"""

from __future__ import annotations

import datetime as dt
import json

MAX_DESCRIPTION_LENGTH = 150


def _truncate_description(text: str) -> str:
    """截断描述到 150 字符，超长加省略号。"""
    text = " ".join(text.split())
    if len(text) <= MAX_DESCRIPTION_LENGTH:
        return text
    return text[:MAX_DESCRIPTION_LENGTH] + "..."


def _format_count(value: int | None) -> str:
    """格式化计数：None 返回空串，否则加千分位。"""
    if value is None:
        return ""
    return f"{value:,}"


def _repo_heading(repo: dict, rank: int) -> str:
    """生成单条仓库的标题行：排名 + 链接 + star/语言信息。"""
    owner = repo["owner"]
    name = repo["name"]
    url = repo["url"]

    parts = [f"### {rank}. [{owner}/{name}]({url})"]
    stars_total = _format_count(repo.get("stars_total"))
    stars_today = repo.get("stars_today")
    language = repo.get("language", "")

    if stars_total:
        today_text = f"（今日 +{stars_today:,}）" if stars_today else ""
        parts.append(f"⭐ {stars_total}{today_text}")
    if language:
        parts.append(f"· {language}")

    return " ".join(parts)


def build_day_page(target_date: dt.date, repos: list[dict]) -> str:
    """生成某天的 GitHub 趋势页 Markdown。

    Args:
        target_date: 趋势日期。
        repos: trending_client 返回的仓库列表（已截断到单日上限）。

    Returns:
        完整 Markdown 字符串，含 frontmatter。
    """
    date_text = f"{target_date.isoformat()}T08:30:00+08:00"
    title = f"GitHub 趋势 | {target_date.isoformat()}"
    description = f"{target_date.isoformat()} GitHub 热门仓库"

    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"date: {date_text}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "comments: false",
        "---",
        "",
        "## 今日热门",
        "",
    ]

    for rank, repo in enumerate(repos, start=1):
        lines.append(_repo_heading(repo, rank))
        lines.append("")
        if repo.get("description"):
            lines.append(_truncate_description(repo["description"]))
            lines.append("")

    # lines 末尾始终为 ""（来自 append("")），"\n".join 会产生尾随换行
    return "\n".join(lines)
