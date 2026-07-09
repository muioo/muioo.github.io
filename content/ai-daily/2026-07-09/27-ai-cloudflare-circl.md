---
title: "AI 审计代理在 Cloudflare CIRCL 中发现 7 个漏洞"
date: 2026-07-09T08:30:00+08:00
description: "zkSecurity 的 AI 审计代理 zkao 持续扫描 Cloudflare 的 CIRCL 密码学库，使用 Opus 4.6 + skills 和 GPT-5.3 + skills 等模型发现并确认了 7 个真实漏洞。其中包括阈值 RSA 中 float64 精度丢失（AI 自评 Criti..."
category: "技巧与观点"
source_url: https://blog.zksecurity.xyz/posts/circl-bugs
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmrblfb8a050sihl1484pa3wo
comments: false
---

## 摘要

zkSecurity 的 AI 审计代理 zkao 持续扫描 Cloudflare 的 CIRCL 密码学库，使用 Opus 4.6 + skills 和 GPT-5.3 + skills 等模型发现并确认了 7 个真实漏洞。其中包括阈值 RSA 中 float64 精度丢失（AI 自评 Critical）和属性基加密（CP-ABE）访问控制完全失效（Critical，由 zkao 自行发现）。所有漏洞已在上游修复，多数在 HackerOne 上获得确认和奖励。AI 生成的候选发现仍需人工验证，但 zkao 已能自动完成大部分验证工作。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://blog.zksecurity.xyz/posts/circl-bugs)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrblfb8a050sihl1484pa3wo)
