#!/usr/bin/env python3
"""GitHub 趋势页客户端：抓取并解析 github.com/trending HTML。"""

from __future__ import annotations

import os
import random
import re
import time
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

HTTP_HEADERS = {
    "User-Agent": "github-trending-bot/1.0 (+https://github.com/wangbanglei/firstblog)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

ALLOWED_PERIODS = ("daily", "weekly", "monthly")


def build_trending_url(period: str = "daily") -> str:
    """构建指定周期（daily/weekly/monthly）的 GitHub 趋势页 URL。"""
    if period not in ALLOWED_PERIODS:
        raise ValueError(
            f"invalid period {period!r}, expected one of {ALLOWED_PERIODS}"
        )
    # 每次调用时读取环境变量，避免模块重载后状态污染其它测试
    api_base = os.getenv("GH_TRENDING_BASE", "https://github.com").rstrip("/")
    return f"{api_base}/trending?since={period}"


def _parse_count(text: str) -> int | None:
    """从 GitHub 计数文本（如 '45,234'、'1,345 stars today'）提取整数。"""
    match = re.search(r"([\d,]+)", text or "")
    if not match:
        return None
    return int(match.group(1).replace(",", ""))


def parse_trending_page(html: str) -> list[dict]:
    """解析趋势页 HTML，返回仓库列表。

    每个仓库字段：owner/name/url/description/language/stars_total/stars_today/forks。
    单个行结构不完整时跳过该行，不中断整页解析。
    """
    soup = BeautifulSoup(html, "html.parser")
    repos: list[dict] = []

    for row in soup.select("article.Box-row"):
        heading = row.select_one("h2 a, h3 a")
        if heading is None:
            continue
        parts = heading.get("href", "").strip("/").split("/")
        if len(parts) < 2:
            continue
        owner, name = parts[0], parts[1]

        desc_el = row.select_one("p")
        description = " ".join(desc_el.get_text().split()) if desc_el else ""

        lang_el = row.select_one('span[itemprop="programmingLanguage"]')
        language = lang_el.get_text(strip=True) if lang_el else ""

        # 页面上有两个指向 stargazers 的链接：总数与"stars today"（真实页面为 span，
        # 按文本查找而不是 class，结构变动时更健壮）
        star_links = row.select("a[href$='/stargazers']")
        stars_total = _parse_count(star_links[0].get_text()) if star_links else None
        stars_today = None
        for text in row.stripped_strings:
            if "stars today" in text:
                stars_today = _parse_count(text)
                break

        fork_link = row.select_one("a[href$='/forks']")
        forks = _parse_count(fork_link.get_text()) if fork_link else None

        repos.append(
            {
                "owner": owner,
                "name": name,
                "url": f"https://github.com/{owner}/{name}",
                "description": description,
                "language": language,
                "stars_total": stars_total,
                "stars_today": stars_today,
                "forks": forks,
            }
        )

    return repos


def fetch_trending(period: str = "daily") -> list[dict] | None:
    """抓取指定周期的 GitHub 趋势仓库列表。

    Returns:
        解析后的仓库列表；HTTP 404 时返回 None。

    Raises:
        RuntimeError: 重试耗尽后仍失败。
    """
    url = build_trending_url(period)
    # 每次调用时读取环境变量，避免模块重载后状态污染其它测试
    retries = int(os.getenv("GH_TRENDING_FETCH_RETRIES", "4"))
    timeout = int(os.getenv("GH_TRENDING_FETCH_TIMEOUT", "30"))
    token = os.getenv("GH_TRENDING_TOKEN", "").strip()

    headers = dict(HTTP_HEADERS)
    if token:
        headers["Authorization"] = f"Bearer {token}"

    last_error: Exception | None = None

    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                html = response.read().decode("utf-8", errors="replace")
                return parse_trending_page(html)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            last_error = exc
        except Exception as exc:  # noqa: BLE001
            last_error = exc

        if attempt < retries:
            # 指数退避：3s/6s/12s/24s（上限 20s），叠加随机抖动避免惊群
            sleep_seconds = min(20, 3 * (2 ** (attempt - 1)) + random.uniform(0.5, 1.5))
            time.sleep(sleep_seconds)

    raise RuntimeError(
        f"fetch_trending failed after {retries} attempts for {url}: {last_error}"
    )
