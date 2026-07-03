#!/usr/bin/env python3
"""aihot.virxact.com 日报 API 客户端。"""

from __future__ import annotations

import datetime as dt
import json
import os
import random
import time
import urllib.error
import urllib.request


HTTP_HEADERS = {
    "User-Agent": "ai-daily-bot/1.0 (+https://github.com/wangbanglei/firstblog)",
    "Accept": "application/json",
}


def build_api_url(target_date: dt.date) -> str:
    """构建指定日期的 aihot 日报 API URL。"""
    # 每次调用时读取环境变量，避免模块重载后状态污染其它测试
    api_base = os.getenv("AIHOT_API_BASE", "https://aihot.virxact.com").rstrip("/")
    return f"{api_base}/api/public/daily?date={target_date.isoformat()}"


def fetch_daily(target_date: dt.date) -> dict | None:
    """获取指定日期的日报数据。

    Returns:
        解析后的 JSON dict；HTTP 404 时返回 None。

    Raises:
        RuntimeError: 重试耗尽后仍失败。
    """
    url = build_api_url(target_date)
    # 每次调用时读取环境变量，避免模块重载后状态污染其它测试
    retries = int(os.getenv("AI_DAILY_FETCH_RETRIES", "4"))
    timeout = int(os.getenv("AI_DAILY_FETCH_TIMEOUT", "30"))
    last_error: Exception | None = None

    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, headers=HTTP_HEADERS)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
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
        f"fetch_daily failed after {retries} attempts for {target_date.isoformat()}: {last_error}"
    )
