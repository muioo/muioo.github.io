---
title: "独立调查：ChatGPT 的 __obi 跨站 Cookie 可将站外浏览行为关联到 ChatGPT 账号"
date: 2026-09-21T08:30:00+08:00
description: "作者通过自己手机上的流量捕获复现了 OpenAI 广告收集器机制：bzr.openai.com 在 .openai.com 域设置 __obi Cookie，绑定 ChatGPT 账号（或稳定的匿名主体），投放广告的商家站点加载 OpenAI 像素代码时会把 __obi 连同浏览和购买数据回传给 O..."
category: "论文研究"
source_url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.news/items/cmua567e703tmro5t558lzx7o
comments: false
---

## 摘要

作者通过自己手机上的流量捕获复现了 OpenAI 广告收集器机制：bzr.openai.com 在 .openai.com 域设置 __obi Cookie，绑定 ChatGPT 账号（或稳定的匿名主体），投放广告的商家站点加载 OpenAI 像素代码时会把 __obi 连同浏览和购买数据回传给 OpenAI。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector)
- [AI HOT 详情页](https://aihot.news/items/cmua567e703tmro5t558lzx7o)
