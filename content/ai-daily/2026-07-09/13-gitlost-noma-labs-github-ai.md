---
title: "GitLost：Noma Labs 发现 GitHub AI 代理提示词注入漏洞"
date: 2026-07-09T08:30:00+08:00
description: "Noma Labs 在 GitHub Agentic Workflows 中发现严重提示词注入漏洞 GitLost。未认证攻击者仅需在属于同一组织的公共仓库中创建一个嵌有恶意指令的 Issue，即可诱使基于 Claude 或 GitHub Copilot 的 AI 代理读取并公开该组织内私有仓库的内..."
category: "行业动态"
source_url: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmrbu023x079pihl1q4rvhzky
comments: false
---

## 摘要

Noma Labs 在 GitHub Agentic Workflows 中发现严重提示词注入漏洞 GitLost。未认证攻击者仅需在属于同一组织的公共仓库中创建一个嵌有恶意指令的 Issue，即可诱使基于 Claude 或 GitHub Copilot 的 AI 代理读取并公开该组织内私有仓库的内容。攻击无需编码技能或凭证，根源在于代理将用户可控内容视为可信指令，且 GitHub 的防护措施因 "Additionally" 关键词被绕过。Noma Labs 已公开 PoC 并建议限制跨仓库权限、隔离用户输入。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrbu023x079pihl1q4rvhzky)
