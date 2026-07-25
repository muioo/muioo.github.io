---
title: "Claude-thermos：保持 Claude 会话缓存热度，避免重新编码费用"
date: 2026-07-25T08:30:00+08:00
description: "Claude-thermos 通过本地反向代理监控 Claude Code 会话，在主智能体因等待子智能体而空闲超过 5 分钟时，自动发送预热请求刷新提示缓存。实测约 185 次本地会话中，缓存过期导致的重新编码占账单约 22%。工具以 uvx 运行，支持自定义空闲阈值和预热间隔。"
category: "技巧与观点"
source_url: https://github.com/izeigerman/claude-thermos
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmryrjtlb04ehrolgi1zd6eqv
comments: false
---

## 摘要

Claude-thermos 通过本地反向代理监控 Claude Code 会话，在主智能体因等待子智能体而空闲超过 5 分钟时，自动发送预热请求刷新提示缓存。实测约 185 次本地会话中，缓存过期导致的重新编码占账单约 22%。工具以 uvx 运行，支持自定义空闲阈值和预热间隔。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://github.com/izeigerman/claude-thermos)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmryrjtlb04ehrolgi1zd6eqv)
