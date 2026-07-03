#!/usr/bin/env python3
"""aihot_client 单元测试。"""
from __future__ import annotations

import datetime as dt
import pathlib
import sys
import unittest
from unittest import mock
from urllib.error import HTTPError

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from aihot_client import build_api_url, fetch_daily


class TestBuildApiUrl(unittest.TestCase):
    """验证 API URL 构建。"""

    def test_build_api_url_with_default_base(self) -> None:
        """默认 base 时 URL 应包含日期和正确 base。"""
        date = dt.date(2026, 7, 3)
        url = build_api_url(date)
        self.assertIn("2026-07-03", url)
        self.assertTrue(url.startswith("https://aihot.virxact.com/"))
        self.assertTrue(url.endswith("/api/public/daily?date=2026-07-03"))

    def test_build_api_url_with_custom_base(self) -> None:
        """自定义 base 应被使用。"""
        with mock.patch.dict("os.environ", {"AIHOT_API_BASE": "https://example.com"}):
            url = build_api_url(dt.date(2026, 7, 3))
            self.assertTrue(url.startswith("https://example.com/"))


class TestFetchDaily(unittest.TestCase):
    """验证 fetch_daily 的成功、404、重试行为。"""

    def test_fetch_daily_success(self) -> None:
        """成功响应应返回解析后的 dict。"""
        mock_resp = mock.MagicMock()
        mock_resp.read.return_value = b'{"date":"2026-07-03","sections":[]}'
        mock_resp.__enter__.return_value = mock_resp
        mock_resp.__exit__.return_value = None
        with mock.patch("urllib.request.urlopen", return_value=mock_resp):
            result = fetch_daily(dt.date(2026, 7, 3))
        self.assertEqual(result["date"], "2026-07-03")
        self.assertEqual(result["sections"], [])

    def test_fetch_daily_404_returns_none(self) -> None:
        """HTTP 404 应返回 None，不抛异常。"""
        error = HTTPError("http://x", 404, "Not Found", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=error):
            result = fetch_daily(dt.date(2025, 1, 1))
        self.assertIsNone(result)

    def test_fetch_daily_retries_on_network_error(self) -> None:
        """网络错误应重试，最终成功返回 dict。"""
        mock_resp = mock.MagicMock()
        mock_resp.read.return_value = b'{"date":"2026-07-03","sections":[]}'
        mock_resp.__enter__.return_value = mock_resp
        mock_resp.__exit__.return_value = None
        side_effects = [ConnectionError("fail"), ConnectionError("fail"), mock_resp]
        with mock.patch("urllib.request.urlopen", side_effect=side_effects):
            with mock.patch("time.sleep"):  # 加速测试
                result = fetch_daily(dt.date(2026, 7, 3))
        self.assertEqual(result["date"], "2026-07-03")

    def test_fetch_daily_raises_after_retries_exhausted(self) -> None:
        """重试耗尽后应抛 RuntimeError。"""
        with mock.patch("urllib.request.urlopen", side_effect=ConnectionError("fail")):
            with mock.patch("time.sleep"):
                with self.assertRaises(RuntimeError):
                    fetch_daily(dt.date(2026, 7, 3))


if __name__ == "__main__":
    unittest.main()
