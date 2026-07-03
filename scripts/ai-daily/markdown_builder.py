#!/usr/bin/env python3
"""生成 AI 日报 Markdown 文件（日报索引 + 单篇详情）。"""

from __future__ import annotations

import datetime as dt
import json
import re


MAX_DESCRIPTION_LENGTH = 150
MAX_SLUG_LENGTH = 40


def slugify(title: str, permalink: str) -> str:
    """从标题提取 ASCII 词作为 slug，纯中文标题回退到 permalink ID 前缀。

    Args:
        title: 文章标题（可能中英混合）。
        permalink: 文章在 aihot.virxact.com 的详情页 URL。

    Returns:
        URL 友好的 slug 字符串。
    """
    ascii_runs = re.findall(r"[A-Za-z0-9][A-Za-z0-9-]*", title)
    # 过滤掉长度 < 2 的串
    ascii_runs = [run for run in ascii_runs if len(run) >= 2]
    slug = "-".join(run.lower() for run in ascii_runs)
    slug = re.sub(r"-+", "-", slug).strip("-")

    if slug:
        return slug[:MAX_SLUG_LENGTH]

    # 纯中文标题：取 permalink 末段 ID 前 12 字符
    item_id = permalink.rstrip("/").rsplit("/", 1)[-1]
    return item_id[:12] if item_id else "untitled"


def _truncate_description(text: str) -> str:
    """截断 description 到 150 字符，超长加省略号。

    内部辅助函数，仅供 build_item_markdown 使用。
    """
    text = " ".join(text.split())
    if len(text) <= MAX_DESCRIPTION_LENGTH:
        return text
    return text[:MAX_DESCRIPTION_LENGTH] + "..."


def build_item_markdown(target_date: dt.date, item: dict, category: str) -> str:
    """生成单篇详情页 Markdown。

    Args:
        target_date: 日报日期。
        item: API 返回的单个 item dict。
        category: 所属 section 名称（如"产品发布/更新"）。

    Returns:
        完整 Markdown 字符串，含 frontmatter。
    """
    title = item.get("title", "")
    summary = item.get("summary", "")
    source_url = item.get("sourceUrl", "")
    source_name = item.get("sourceName", "")
    permalink = item.get("permalink", "")
    date_text = f"{target_date.isoformat()}T08:30:00+08:00"

    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"date: {date_text}",
        f"description: {json.dumps(_truncate_description(summary), ensure_ascii=False)}",
        f"category: {json.dumps(category, ensure_ascii=False)}",
        f"source_url: {source_url}",
        f"source_name: {json.dumps(source_name, ensure_ascii=False)}",
        f"external_permalink: {permalink}",
        "comments: false",
        "---",
        "",
        "## 摘要",
        "",
        summary,
        "",
        "## 原文链接",
        "",
    ]
    if source_url:
        lines.append(f"- [{source_name}]({source_url})")
    if permalink:
        lines.append(f"- [AI HOT 详情页]({permalink})")
    return "\n".join(lines) + "\n"


def _iter_valid_items(
    sections: list[dict],
) -> list[tuple[int, str, dict]]:
    """遍历 sections，跳过缺 title 或 summary 的 item，返回 [(全局序号, 分类, item), ...]。"""
    result: list[tuple[int, str, dict]] = []
    global_index = 0
    for section in sections:
        label = section.get("label", "")
        for item in section.get("items", []):
            if not item.get("title") or not item.get("summary"):
                continue
            global_index += 1
            result.append((global_index, label, item))
    return result


def build_daily_index(target_date: dt.date, sections: list[dict]) -> str:
    """生成日报索引页 Markdown（用作 {date}/_index.md）。

    Args:
        target_date: 日报日期。
        sections: API 返回的 sections 列表。

    Returns:
        完整 Markdown 字符串，含 frontmatter 和所有 item 索引。
    """
    date_text = f"{target_date.isoformat()}T08:30:00+08:00"
    title = f"AI日报 | {target_date.isoformat()}"
    description = f"{target_date.isoformat()} AI 热点日报"

    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"date: {date_text}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "comments: false",
        "---",
        "",
    ]

    valid_items = _iter_valid_items(sections)
    current_label: str | None = None
    for index, label, item in valid_items:
        if label != current_label:
            if current_label is not None:
                lines.append("")
            lines.append(f"## {label}")
            lines.append("")
            current_label = label
        item_title = item.get("title", "")
        summary = item.get("summary", "")
        permalink = item.get("permalink", "")
        slug = slugify(item_title, permalink)
        filename = f"{index:02d}-{slug}"
        lines.append(f"### {index}. [{item_title}](./{filename}/)")
        lines.append("")
        # 索引页只显示截断预览，全文在单篇详情页
        lines.append(_truncate_description(summary))
        lines.append("")

    # lines 末尾始终为 ""（来自 append("")），"\n".join 会产生尾随换行
    return "\n".join(lines)


def build_item_pages(
    target_date: dt.date, sections: list[dict]
) -> list[tuple[str, str]]:
    """生成所有单篇详情页，返回 [(filename, content), ...] 列表，处理 slug 冲突。

    Args:
        target_date: 日报日期。
        sections: API 返回的 sections 列表。

    Returns:
        列表，每项为 (文件名, Markdown 内容)。
    """
    pages: list[tuple[str, str]] = []
    seen_slugs: dict[str, int] = {}

    for index, category, item in _iter_valid_items(sections):
        title = item.get("title", "")
        permalink = item.get("permalink", "")
        base_slug = slugify(title, permalink)

        slug = base_slug
        if base_slug in seen_slugs:
            seen_slugs[base_slug] += 1
            slug = f"{base_slug}-{seen_slugs[base_slug]}"
        else:
            seen_slugs[base_slug] = 1

        filename = f"{index:02d}-{slug}.md"
        pages.append((filename, build_item_markdown(target_date, item, category)))

    return pages
