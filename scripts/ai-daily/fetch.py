#!/usr/bin/env python3
"""Generate Hugo AI daily pages from hex2077.dev open-source top projects."""

from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import random
import re
import sys
import time
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
FETCH_RETRIES = int(os.getenv("AI_DAILY_FETCH_RETRIES", "4"))
FETCH_TIMEOUT = int(os.getenv("AI_DAILY_FETCH_TIMEOUT", "30"))
BROWSER_FALLBACK = os.getenv("AI_DAILY_BROWSER_FALLBACK", "auto").strip().lower()
BROWSER_WAIT_UNTIL = (
    os.getenv("AI_DAILY_BROWSER_WAIT_UNTIL", "domcontentloaded").strip().lower() or "domcontentloaded"
)
BROWSER_CONTENT_TIMEOUT = int(os.getenv("AI_DAILY_BROWSER_CONTENT_TIMEOUT", str(FETCH_TIMEOUT)))
BROWSER_DISMISS_TIMEOUT = int(os.getenv("AI_DAILY_BROWSER_DISMISS_TIMEOUT", "5"))
BROWSER_PROJECT_LINK_SELECTOR = "a[href*='github.com/']"

GLOBAL_NOTIFICATION_ID = "domain_update_v1"
GLOBAL_NOTIFICATION_LOCAL_STORAGE_KEY = f"hide_global_notif_{GLOBAL_NOTIFICATION_ID}"
GLOBAL_NOTIFICATION_SESSION_STORAGE_KEY = f"session_notif_{GLOBAL_NOTIFICATION_ID}"

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
}


def get_target_date() -> dt.date:
    if DATE_OVERRIDE:
        return dt.date.fromisoformat(DATE_OVERRIDE)
    return dt.datetime.now(ZoneInfo(TIMEZONE)).date()


def build_source_url(target_date: dt.date) -> str:
    return f"https://hex2077.dev/docs/{target_date:%Y-%m}/{target_date:%Y-%m-%d}/"


def normalize_text(value: str) -> str:
    """清理页面文本中的 HTML 实体和多余空白。"""
    text = unescape(value)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_project_title_strong(classes: str) -> bool:
    """判断 strong 标签是否为来源页面中的项目中文标题。"""
    class_names = classes.split()
    return "font-semibold" in class_names and "text-[var(--color-text-primary)]" in class_names


def is_blocked_page(html: str) -> bool:
    """判断响应内容是否为验证码或反爬拦截页面。"""
    blocked_markers = [
        "cf-challenge",
        "cf-browser-verification",
        "cf-turnstile",
        "g-recaptcha",
        "hcaptcha",
        "attention required",
        "verify you are human",
        "访问过于频繁",
        "请完成验证",
    ]
    lower_html = html.lower()
    return any(marker in lower_html for marker in blocked_markers)


def should_try_browser_fallback() -> bool:
    """判断是否启用 Playwright 浏览器兜底抓取。"""
    return BROWSER_FALLBACK not in {"0", "false", "off", "no"}


def browser_fallback_error() -> RuntimeError:
    """生成缺少 Playwright 或浏览器依赖时的安装提示。"""
    return RuntimeError(
        "browser fallback requires Playwright. Install with: "
        "python -m pip install playwright && python -m playwright install --with-deps chromium"
    )


def wait_for_browser_project_links(page: object) -> None:
    """等待浏览器渲染出 GitHub 项目链接，避免过早读取空壳 HTML。"""
    try:
        page.wait_for_selector(BROWSER_PROJECT_LINK_SELECTOR, timeout=BROWSER_CONTENT_TIMEOUT * 1000)
    except Exception as exc:  # noqa: BLE001
        try:
            html = page.content()
        except Exception as content_exc:  # noqa: BLE001
            raise RuntimeError(
                "browser fallback could not read page content after waiting for project links"
            ) from content_exc

        if is_blocked_page(html):
            raise RuntimeError("source page returned a verification or anti-bot page") from exc

        raise RuntimeError(
            "browser fallback loaded the page, but no GitHub project link appeared "
            f"within {BROWSER_CONTENT_TIMEOUT}s"
        ) from exc


def fetch_source_html_with_browser(url: str) -> str:
    """使用 Playwright 渲染来源页，并在项目链接出现后返回完整 HTML。"""
    try:
        from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise browser_fallback_error() from exc

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            context = browser.new_context(
                locale="zh-CN",
                user_agent=BROWSER_HEADERS["User-Agent"],
                extra_http_headers={
                    "Accept-Language": BROWSER_HEADERS["Accept-Language"],
                },
            )
            context.add_init_script(
                """
                (() => {
                  const localKey = "hide_global_notif_domain_update_v1";
                  const sessionKey = "session_notif_domain_update_v1";
                  try { window.localStorage.setItem(localKey, "true"); } catch (_) {}
                  try { window.sessionStorage.setItem(sessionKey, "true"); } catch (_) {}
                })();
                """
            )
            page = context.new_page()
            try:
                page.goto(url, wait_until=BROWSER_WAIT_UNTIL, timeout=FETCH_TIMEOUT * 1000)
            except PlaywrightTimeoutError as exc:
                raise RuntimeError(
                    "browser fallback timed out waiting for "
                    f"'{BROWSER_WAIT_UNTIL}' page load state within {FETCH_TIMEOUT}s"
                ) from exc
            dismiss_global_notification(page)
            wait_for_browser_project_links(page)
            html = page.content()
            if is_blocked_page(html):
                raise RuntimeError("source page returned a verification or anti-bot page")
            return html
        finally:
            browser.close()


def dismiss_global_notification(page: object) -> None:
    """关闭来源站的入口弹层，允许后续读取页面正文内容。"""
    # 来源站会显示“进入站点 / ENTER SITE”入口弹层；先写入存储位，再用文本按钮兜底点击。
    try:
        page.evaluate(
            """
            ([localKey, sessionKey]) => {
              try { window.localStorage.setItem(localKey, "true"); } catch (_) {}
              try { window.sessionStorage.setItem(sessionKey, "true"); } catch (_) {}
            }
            """,
            [GLOBAL_NOTIFICATION_LOCAL_STORAGE_KEY, GLOBAL_NOTIFICATION_SESSION_STORAGE_KEY],
        )
    except Exception:
        pass

    for selector in [
        "button:has-text('进入站点 / ENTER SITE')",
        "button:has-text('进入站点')",
        "button:has-text('ENTER SITE')",
        "[role='button']:has-text('进入站点 / ENTER SITE')",
        "[role='button']:has-text('进入站点')",
        "[role='button']:has-text('ENTER SITE')",
    ]:
        try:
            locator = page.locator(selector).first
            locator.wait_for(state="visible", timeout=BROWSER_DISMISS_TIMEOUT * 1000)
            locator.click(timeout=BROWSER_DISMISS_TIMEOUT * 1000)
            return
        except Exception:
            continue

    try:
        page.keyboard.press("Escape")
    except Exception:
        pass


def fetch_projects_with_browser_fallback(source_url: str, errors: list[str]) -> list[dict[str, str]]:
    if not should_try_browser_fallback():
        return []

    try:
        html = fetch_source_html_with_browser(source_url)
        projects = extract_projects(html)
        if projects:
            return projects
        errors.append(f"浏览器渲染后仍未提取到开源 TOP 项目：{source_url}")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"浏览器回退抓取失败: {exc} - {source_url}")

    return []


class HexTopProjectParser(HTMLParser):
    def __init__(self) -> None:
        """初始化用于提取来源页面项目条目的解析状态。"""
        super().__init__()
        self.in_paragraph = False
        self.in_anchor = False
        self.in_title_strong = False
        self.current_href = ""
        self.current_anchor_text: list[str] = []
        self.current_title_text: list[str] = []
        self.current_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """进入段落、GitHub 链接或目标 strong 标题时记录状态。"""
        attrs_dict = dict(attrs)
        if tag == "p":
            classes = attrs_dict.get("class", "") or ""
            if "leading-7" in classes and "text-base" in classes:
                self.in_paragraph = True
                self.current_text = []
                self.current_href = ""
                self.current_anchor_text = []
                self.current_title_text = []
        elif self.in_paragraph and tag == "a":
            href = attrs_dict.get("href", "") or ""
            if "github.com" in href and "/issues" not in href and "/pull" not in href:
                self.in_anchor = True
                self.current_href = href
                self.current_anchor_text = []
        elif self.in_paragraph and tag == "strong":
            classes = attrs_dict.get("class", "") or ""
            if is_project_title_strong(classes):
                self.in_title_strong = True

    def handle_endtag(self, tag: str) -> None:
        """离开标签时生成完整项目条目并重置当前段落状态。"""
        if tag == "a" and self.in_anchor:
            self.in_anchor = False
        elif tag == "strong" and self.in_title_strong:
            self.in_title_strong = False
        elif tag == "p" and self.in_paragraph:
            paragraph_text = normalize_text("".join(self.current_text))
            anchor_text = normalize_text("".join(self.current_anchor_text))
            title_text = normalize_text("".join(self.current_title_text))
            title = title_text or anchor_text
            if self.current_href and paragraph_text and anchor_text and anchor_text != "关于作者":
                self.items.append(
                    {
                        "repo_url": self.current_href,
                        "title": title,
                        "summary": paragraph_text,
                    }
                )
            self.in_paragraph = False
            self.in_anchor = False
            self.in_title_strong = False
            self.current_href = ""
            self.current_anchor_text = []
            self.current_title_text = []
            self.current_text = []

    def handle_data(self, data: str) -> None:
        """收集段落、GitHub 链接和目标 strong 标题中的文本。"""
        if self.in_paragraph:
            self.current_text.append(data)
            if self.in_anchor:
                self.current_anchor_text.append(data)
            if self.in_title_strong:
                self.current_title_text.append(data)


def fetch_source_html(url: str) -> str:
    last_error: Exception | None = None

    for attempt in range(1, FETCH_RETRIES + 1):
        request = urllib.request.Request(url, headers=BROWSER_HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=FETCH_TIMEOUT) as response:
                html = response.read().decode("utf-8", errors="replace")
                if is_blocked_page(html):
                    raise RuntimeError("source page returned a verification or anti-bot page")
                return html
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 404:
                raise
        except Exception as exc:  # noqa: BLE001
            last_error = exc

        if attempt < FETCH_RETRIES:
            sleep_seconds = min(20, attempt * 3 + random.uniform(0.5, 1.5))
            time.sleep(sleep_seconds)

    if last_error is None:
        raise RuntimeError("failed to fetch source page for unknown reason")
    raise last_error


def extract_projects(html: str) -> list[dict[str, str]]:
    parser = HexTopProjectParser()
    parser.feed(html)

    filtered: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for item in parser.items:
        url = item["repo_url"]
        if url in seen_urls:
            continue
        seen_urls.add(url)

        if not re.search(r"github\.com/[^/]+/[^/]+/?$", url):
            continue

        filtered.append(item)

    return filtered[:MAX_ITEMS]


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def md_link(label: str, url: str) -> str:
    return f"[{label}]({url})"


def build_markdown(target_date: dt.date, projects: list[dict[str, str]]) -> str:
    title = f"AI日报 | {target_date.isoformat()}"
    date_text = f"{target_date.isoformat()}T08:30:00+08:00"

    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"date: {date_text}",
        f"slug: {target_date.isoformat()}",
        f"description: {yaml_quote('开源 TOP 项目 AI 日报')}",
        "comments: false",
        "---",
        "",
        "## 开源 TOP 项目",
        "",
    ]

    if projects:
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
                "今天没有从来源页面提取到可用项目数据。",
                "",
            ]
        )

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


def fetch_projects_for_date(target_date: dt.date) -> tuple[list[dict[str, str]], list[str]]:
    source_url = build_source_url(target_date)
    errors: list[str] = []

    try:
        html = fetch_source_html(source_url)
        projects = extract_projects(html)
        if projects:
            return projects, errors
        errors.append(f"来源页面存在，但没有提取到开源 TOP 项目：{source_url}")
        projects = fetch_projects_with_browser_fallback(source_url, errors)
        if projects:
            return projects, errors
    except urllib.error.HTTPError as exc:
        errors.append(f"抓取来源失败: HTTP {exc.code} - {source_url}")
        if exc.code != 404:
            projects = fetch_projects_with_browser_fallback(source_url, errors)
            if projects:
                return projects, errors
    except Exception as exc:  # noqa: BLE001
        errors.append(f"抓取来源失败: {exc} - {source_url}")
        projects = fetch_projects_with_browser_fallback(source_url, errors)
        if projects:
            return projects, errors

    return [], errors


def main() -> int:
    target_date = get_target_date()
    projects, errors = fetch_projects_for_date(target_date)
    if not projects:
        print(f"No source data for {target_date.isoformat()}, skipped.")
        for error in errors:
            print(error, file=sys.stderr)
        return 0

    content = build_markdown(target_date, projects)
    write_daily_page(target_date, content)
    rebuild_latest_json()
    print(f"Generated AI daily page for {target_date.isoformat()} with {len(projects)} projects.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
