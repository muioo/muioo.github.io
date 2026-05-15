#!/usr/bin/env python3
"""Generate a Hugo AI daily page from hex2077.dev open-source top projects."""

from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import re
import sys
import textwrap
import urllib.error
import urllib.request
from html import unescape
from html.parser import HTMLParser
from zoneinfo import ZoneInfo


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content" / "ai-daily"
DATA_DIR = ROOT / "data" / "ai-daily"
LATEST_FILE = DATA_DIR / "latest.json"

TIMEZONE = os.getenv("AI_DAILY_TIMEZONE", "Asia/Shanghai")
DATE_OVERRIDE = os.getenv("AI_DAILY_DATE", "").strip()
MAX_ITEMS = int(os.getenv("AI_DAILY_MAX_ITEMS", "12"))


def get_target_date() -> dt.date:
    if DATE_OVERRIDE:
        return dt.date.fromisoformat(DATE_OVERRIDE)
    return dt.datetime.now(ZoneInfo(TIMEZONE)).date()


def build_source_url(target_date: dt.date) -> str:
    return f"https://hex2077.dev/docs/{target_date:%Y-%m}/{target_date:%Y-%m-%d}/"


def normalize_text(value: str) -> str:
    text = unescape(value)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


class HexTopProjectParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_paragraph = False
        self.in_anchor = False
        self.current_href = ""
        self.current_anchor_text: list[str] = []
        self.current_text: list[str] = []
        self.items: list[dict] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "p":
            classes = attrs_dict.get("class", "") or ""
            if "leading-7" in classes and "text-base" in classes:
                self.in_paragraph = True
                self.current_text = []
        elif self.in_paragraph and tag == "a":
            href = attrs_dict.get("href", "") or ""
            if "github.com" in href and "/issues" not in href and "/pull" not in href:
                self.in_anchor = True
                self.current_href = href
                self.current_anchor_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self.in_anchor:
            self.in_anchor = False
        elif tag == "p" and self.in_paragraph:
            paragraph_text = normalize_text("".join(self.current_text))
            if self.current_href and paragraph_text:
                anchor_text = normalize_text("".join(self.current_anchor_text))
                if anchor_text and anchor_text != "关于我":
                    self.items.append(
                        {
                            "repo_url": self.current_href,
                            "title": anchor_text,
                            "summary": paragraph_text,
                        }
                    )
            self.in_paragraph = False
            self.current_href = ""
            self.current_anchor_text = []
            self.current_text = []

    def handle_data(self, data: str) -> None:
        if self.in_paragraph:
            self.current_text.append(data)
            if self.in_anchor:
                self.current_anchor_text.append(data)


def fetch_source_html(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "muioo-ai-daily-bot"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def extract_projects(html: str) -> list[dict]:
    parser = HexTopProjectParser()
    parser.feed(html)

    filtered: list[dict] = []
    seen_urls: set[str] = set()
    for item in parser.items:
        url = item["repo_url"]
        if url in seen_urls:
            continue
        seen_urls.add(url)

        if not re.search(r"github\.com/[^/]+/[^/]+", url):
            continue

        title = item["title"]
        summary = item["summary"]

        if "AI资讯" not in title and "GitHub" not in summary and "开源" not in summary and "项目" not in summary:
            continue

        filtered.append(
            {
                "title": title,
                "repo_url": url,
                "summary": summary,
            }
        )

    return filtered[:MAX_ITEMS]


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def md_link(label: str, url: str) -> str:
    return f"[{label}]({url})"


def build_markdown(
    target_date: dt.date,
    source_url: str,
    projects: list[dict],
    errors: list[str],
) -> str:
    title = f"AI日报 | {target_date.isoformat()}"
    date_text = f"{target_date.isoformat()}T08:30:00+08:00"
    intro = "本日报仅采集 `hex2077.dev` 对应日期页面中的开源 TOP 项目，并同步整理项目摘要与仓库链接。"

    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"date: {date_text}",
        f"slug: {target_date.isoformat()}",
        f"description: {yaml_quote('Hex2077 开源 TOP 项目 AI 日报')}",
        "comments: false",
        "---",
        "",
        intro,
        "",
        f"- 生成日期：`{target_date.isoformat()}`",
        f"- 数据来源：{md_link('hex2077 原始页面', source_url)}",
    ]

    lines.append("")

    if projects:
        lines.extend(["## 开源 TOP 项目", ""])
        for index, item in enumerate(projects, start=1):
            lines.extend(
                [
                    f"### {index}. {item['title']}",
                    "",
                    f"- 仓库链接：{md_link('GitHub', item['repo_url'])}",
                    f"- 中文摘要：{item['summary']}",
                    "",
                ]
            )
    else:
        lines.extend(
            [
                "## 开源 TOP 项目",
                "",
                "今天没有从来源页面提取到可用项目数据。",
                "",
            ]
        )

    if errors:
        lines.extend(["## 抓取备注", ""])
        lines.extend(f"- {textwrap.shorten(error, width=180, placeholder='...')}" for error in errors)
        lines.append("")

    return "\n".join(lines)


def write_daily_page(target_date: dt.date, content: str) -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    (CONTENT_DIR / f"{target_date.isoformat()}.md").write_text(content, encoding="utf-8")


def rebuild_latest_json() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    entries = []

    for path in sorted(CONTENT_DIR.glob("*.md"), reverse=True):
        if path.name == "_index.md":
            continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", path.name):
            continue
        date_text = path.stem
        entries.append(
            {
                "date": date_text,
                "title": f"AI日报 | {date_text}",
                "url": f"/ai-daily/{date_text}/",
            }
        )

    payload = {
        "updated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "days": entries[:7],
    }
    LATEST_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fetch_projects_for_date(target_date: dt.date) -> tuple[list[dict], list[str], str]:
    source_url = build_source_url(target_date)
    errors: list[str] = []

    try:
        html = fetch_source_html(source_url)
        projects = extract_projects(html)
        if projects:
            return projects, errors, source_url
        errors.append("来源页面存在，但未提取到开源 TOP 项目。")
    except urllib.error.HTTPError as exc:
        errors.append(f"抓取来源失败: HTTP {exc.code}")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"抓取来源失败: {exc}")

    return [], errors, source_url


def main() -> int:
    target_date = get_target_date()
    projects, errors, source_url = fetch_projects_for_date(target_date)
    if not projects:
        print(f"No source data for {target_date.isoformat()}, skipped.")
        for error in errors:
            print(error, file=sys.stderr)
        return 0

    content = build_markdown(target_date, source_url, projects, errors)
    write_daily_page(target_date, content)
    rebuild_latest_json()
    print(f"Generated AI daily page for {target_date.isoformat()} with {len(projects)} projects.")
    if errors:
        print("Fetch completed with warnings:", file=sys.stderr)
        for error in errors:
            print(error, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
