---
title: "将 GitHub Copilot 置于中间人（MitM）代理之后后，我学到了什么"
date: 2026-08-12T08:30:00+08:00
description: "作者通过 mitmproxy 对 VS Code 中的 GitHub Copilot 进行中间人代理拦截，逆向分析其网络流量与内部架构。文章指出这些 AI 应用普遍基于 Electron 构建，共享相似的网络栈，因此探测结果可迁移至其他同类应用。作者借此揭示了 Copilot 的运行时行为，并分享了..."
category: "技巧与观点"
source_url: https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmsp0g9v20242rort4zh7mzx0
comments: false
---

## 摘要

作者通过 mitmproxy 对 VS Code 中的 GitHub Copilot 进行中间人代理拦截，逆向分析其网络流量与内部架构。文章指出这些 AI 应用普遍基于 Electron 构建，共享相似的网络栈，因此探测结果可迁移至其他同类应用。作者借此揭示了 Copilot 的运行时行为，并分享了配置代理的具体步骤。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmsp0g9v20242rort4zh7mzx0)
