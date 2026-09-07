#!/usr/bin/env python3
"""trending_client 单元测试。"""

from __future__ import annotations

import os
import pathlib
import sys
import unittest
from unittest import mock
from urllib.error import HTTPError

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from trending_client import build_trending_url, fetch_trending, parse_trending_page

# 模拟 github.com/trending 页面的行结构（Box-row），"stars today" 与真实页面一致为 span。
FIXTURE_HTML = """
<!DOCTYPE html>
<html>
<head><title>Trending repositories on GitHub today</title></head>
<body>
  <article class="Box-row">
    <h2 class="h3 lh-condensed">
      <a class="Link--primary" href="/vllm-project/vllm">
        <span>vllm-project</span> / <span>vllm</span>
      </a>
    </h2>
    <p class="col-9 color-fg-muted my-1 pr-4">A high-throughput and memory-efficient inference and serving engine for LLMs.</p>
    <div class="f6 color-fg-muted mt-2">
      <span class="tmp-mr-3 d-inline-block ml-0 tmp-ml-0">
        <span class="repo-language-color" style="background-color: #3572A5"></span>
        <span itemprop="programmingLanguage">Python</span>
      </span>
      <a class="tmp-mr-3 Link Link--muted d-inline-block" href="/vllm-project/vllm/stargazers">
        <svg class="octicon octicon-star"></svg>45,234
      </a>
      <a class="tmp-mr-3 Link Link--muted d-inline-block" href="/vllm-project/vllm/forks">
        <svg class="octicon octicon-repo-forked"></svg>3,456
      </a>
      <span class="tmp-mr-3 d-inline-block float-sm-right">1,234 stars today</span>
    </div>
  </article>
  <article class="Box-row">
    <h2 class="h3 lh-condensed">
      <a class="Link--primary" href="/openai/openai-go">
        <span>openai</span> / <span>openai-go</span>
      </a>
    </h2>
    <p class="col-9 color-fg-muted my-1 pr-4">Go client library for the OpenAI API.</p>
    <div class="f6 color-fg-muted mt-2">
      <span class="tmp-mr-3 d-inline-block ml-0 tmp-ml-0">
        <span itemprop="programmingLanguage">Go</span>
      </span>
      <a class="tmp-mr-3 Link Link--muted d-inline-block" href="/openai/openai-go/stargazers"><svg></svg>1,024</a>
      <a class="tmp-mr-3 Link Link--muted d-inline-block" href="/openai/openai-go/forks"><svg></svg>88</a>
      <span class="tmp-mr-3 d-inline-block float-sm-right">450 stars today</span>
    </div>
  </article>
  <article class="Box-row">
    <h2 class="h3 lh-condensed">
      <a class="Link--primary" href="/no-desc/repo">
        <span>no-desc</span> / <span>repo</span>
      </a>
    </h2>
    <div class="f6 color-fg-muted mt-2">
      <a class="tmp-mr-3 Link Link--muted d-inline-block" href="/no-desc/repo/stargazers"><svg></svg>999</a>
      <a class="tmp-mr-3 Link Link--muted d-inline-block" href="/no-desc/repo/forks"><svg></svg>1</a>
    </div>
  </article>
  <article class="Box-row">
    <p class="col-9 color-fg-muted my-1 pr-4">Malformed row without heading, should be skipped.</p>
  </article>
</body>
</html>
"""


class TestBuildTrendingUrl(unittest.TestCase):
    """验证趋势页 URL 构建与周期校验。"""

    def test_default_base_and_period(self) -> None:
        """默认 base 与 daily 周期。"""
        url = build_trending_url()
        self.assertEqual(url, "https://github.com/trending?since=daily")

    def test_custom_base(self) -> None:
        """自定义 base 应被使用。"""
        with mock.patch.dict("os.environ", {"GH_TRENDING_BASE": "https://example.com"}):
            url = build_trending_url("weekly")
            self.assertEqual(url, "https://example.com/trending?since=weekly")

    def test_invalid_period_raises(self) -> None:
        """非法周期应抛 ValueError。"""
        with self.assertRaises(ValueError):
            build_trending_url("hourly")


class TestParseTrendingPage(unittest.TestCase):
    """验证 HTML 解析。"""

    def test_parse_full_rows(self) -> None:
        """完整行应解析出全部字段。"""
        repos = parse_trending_page(FIXTURE_HTML)
        vllm = repos[0]
        self.assertEqual(vllm["owner"], "vllm-project")
        self.assertEqual(vllm["name"], "vllm")
        self.assertEqual(vllm["url"], "https://github.com/vllm-project/vllm")
        self.assertEqual(vllm["description"], "A high-throughput and memory-efficient inference and serving engine for LLMs.")
        self.assertEqual(vllm["language"], "Python")
        self.assertEqual(vllm["stars_total"], 45234)
        self.assertEqual(vllm["stars_today"], 1234)
        self.assertEqual(vllm["forks"], 3456)

    def test_parse_skips_missing_description_and_language(self) -> None:
        """缺描述/缺语言/缺今日 star 的行应解析为空值而不是报错。"""
        repos = parse_trending_page(FIXTURE_HTML)
        no_desc = repos[2]
        self.assertEqual(no_desc["owner"], "no-desc")
        self.assertEqual(no_desc["description"], "")
        self.assertEqual(no_desc["language"], "")
        self.assertEqual(no_desc["stars_today"], None)
        self.assertEqual(no_desc["stars_total"], 999)

    def test_parse_skips_malformed_rows(self) -> None:
        """无标题行的行应被跳过，不中断解析。"""
        repos = parse_trending_page(FIXTURE_HTML)
        self.assertEqual(len(repos), 3)


class TestFetchTrending(unittest.TestCase):
    """验证 fetch_trending 的成功、404、重试行为。"""

    def _mock_response(self, html: str) -> mock.MagicMock:
        """构造一个返回指定 HTML 的上下文管理器 mock 响应。"""
        mock_resp = mock.MagicMock()
        mock_resp.read.return_value = html.encode("utf-8")
        mock_resp.__enter__.return_value = mock_resp
        mock_resp.__exit__.return_value = None
        return mock_resp

    def test_fetch_success(self) -> None:
        """成功响应应返回解析后的仓库列表。"""
        with mock.patch(
            "urllib.request.urlopen", return_value=self._mock_response(FIXTURE_HTML)
        ):
            repos = fetch_trending()
        self.assertEqual(len(repos), 3)
        self.assertEqual(repos[0]["owner"], "vllm-project")

    def test_fetch_404_returns_none(self) -> None:
        """HTTP 404 应返回 None，不抛异常。"""
        error = HTTPError("http://x", 404, "Not Found", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=error):
            result = fetch_trending()
        self.assertIsNone(result)

    def test_fetch_retries_then_raises(self) -> None:
        """重试耗尽后应抛 RuntimeError。"""
        error = HTTPError("http://x", 500, "Server Error", {}, None)
        with mock.patch.dict("os.environ", {"GH_TRENDING_FETCH_RETRIES": "2"}):
            with mock.patch("urllib.request.urlopen", side_effect=error):
                with mock.patch("time.sleep"):
                    with self.assertRaises(RuntimeError):
                        fetch_trending()

    def test_fetch_sends_token_header_when_configured(self) -> None:
        """配置 GH_TRENDING_TOKEN 时请求头应带 Authorization。"""
        with mock.patch.dict(
            "os.environ", {"GH_TRENDING_TOKEN": "ghp_test_token"}
        ):
            with mock.patch("urllib.request.urlopen") as mock_open:
                mock_open.return_value = self._mock_response(FIXTURE_HTML)
                fetch_trending()
            request = mock_open.call_args.args[0]
            self.assertEqual(request.get_header("Authorization"), "Bearer ghp_test_token")

    def test_fetch_no_token_header_by_default(self) -> None:
        """未配置 token 时请求头不应带 Authorization。"""
        with mock.patch.dict("os.environ", {}, clear=False):
            with mock.patch("urllib.request.urlopen") as mock_open:
                mock_open.return_value = self._mock_response(FIXTURE_HTML)
                fetch_trending()
            request = mock_open.call_args.args[0]
            self.assertIsNone(request.get_header("Authorization"))


if __name__ == "__main__":
    unittest.main()
