---
title: "SGLang 重构 CUDA Graph 支持，Breakable CUDA Graph 成 prefill 默认方案"
date: 2026-08-18T08:30:00+08:00
description: "SGLang 重构 CUDA Graph 支持，通过 runner/backend 接口拆分使不同捕获策略可复用。其社区首创的 Breakable CUDA Graph（BCG）现为 prefill 默认方案，代码量仅为 torch.compile 方案的约四分之一（521 行对比 1,771 行）..."
category: "技巧与观点"
source_url: https://www.lmsys.org/blog/2026-08-17-advanced-cuda-graph
source_name: "LMSYS：Blog（Chatbot Arena 团队）"
external_permalink: https://aihot.virxact.com/items/cmsxjbtk6018lroz0ywmuve4h
comments: false
---

## 摘要

SGLang 重构 CUDA Graph 支持，通过 runner/backend 接口拆分使不同捕获策略可复用。其社区首创的 Breakable CUDA Graph（BCG）现为 prefill 默认方案，代码量仅为 torch.compile 方案的约四分之一（521 行对比 1,771 行），构建速度快 3.8–5.2 倍。

## 原文链接

- [LMSYS：Blog（Chatbot Arena 团队）](https://www.lmsys.org/blog/2026-08-17-advanced-cuda-graph)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmsxjbtk6018lroz0ywmuve4h)
