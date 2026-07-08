---
title: "Gemini API Managed Agents 新增后台执行、远程 MCP 与自定义函数等能力"
date: 2026-07-08T08:30:00+08:00
description: "Google 为 Gemini API 的 Managed Agents 新增后台执行、远程 MCP 服务器集成、自定义函数调用与凭证刷新功能。后台执行通过传入 `background: true` 异步运行任务，立即返回 ID 供轮询状态或流式获取进度。Managed Agents 可直接连接远程..."
category: "产品发布/更新"
source_url: https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api
source_name: "Google Blog：AI（RSS）"
external_permalink: https://aihot.virxact.com/items/cmraw22r701jjihogh1k8hbu6
comments: false
---

## 摘要

Google 为 Gemini API 的 Managed Agents 新增后台执行、远程 MCP 服务器集成、自定义函数调用与凭证刷新功能。后台执行通过传入 `background: true` 异步运行任务，立即返回 ID 供轮询状态或流式获取进度。Managed Agents 可直接连接远程 MCP 服务器，无需自定义代理中间件，并能与内置沙箱工具（如 Google 搜索、代码执行）混合使用。自定义函数调用支持本地执行业务逻辑，内置工具自动在服务端运行。凭证刷新通过传递现有环境 ID 和新网络配置完成，沙箱内文件系统、已安装包和仓库保持不变。这些更新旨在帮助开发者构建可靠的生产级 AI 智能体。

## 原文链接

- [Google Blog：AI（RSS）](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmraw22r701jjihogh1k8hbu6)
