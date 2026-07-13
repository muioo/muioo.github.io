---
title: "xAI Grok Build CLI 网络流量分析：上传仓库全部文件及 git 历史"
date: 2026-07-13T08:30:00+08:00
description: "对 xAI 官方 Grok Build 编码 CLI（grok 0.2.93）的网络流量分析显示，该工具在消费者登录后会向 xAI 发送三类数据：一是它读取的文件内容（包括 .env 密钥文件）以明文形式通过 POST /v1/responses 传输，并同时打包成 session_state 存档..."
category: "技巧与观点"
source_url: https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmrhagju201pqbir7t0tnsgfy
comments: false
---

## 摘要

对 xAI 官方 Grok Build 编码 CLI（grok 0.2.93）的网络流量分析显示，该工具在消费者登录后会向 xAI 发送三类数据：一是它读取的文件内容（包括 .env 密钥文件）以明文形式通过 POST /v1/responses 传输，并同时打包成 session_state 存档通过 POST /v1/storage 上传并获 HTTP 200 确认；二是整个仓库的全部文件内容及 git 历史，独立于 AI 智能体实际读取的文件——即使提示“不要读取任何文件”，Grok 仍将整个仓库作为 git bundle 上传至 Google Cloud Storage 的 grok-code-session-traces …

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrhagju201pqbir7t0tnsgfy)
