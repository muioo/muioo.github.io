---
title: "SGLang 推出 Weight Cache Daemon，实现亚秒级引擎重启"
date: 2026-08-22T08:30:00+08:00
description: "SGLang 团队推出 Weight Cache Daemon，通过 CUDA IPC 零拷贝映射将模型权重加载从约 495 秒降至约 0.63 秒（约 785 倍加速），端到端启动时间减少 93.9%。该守护进程在 GPU 内存中持久化后量化权重，支持多实例共享和亚秒级主备切换，是 Fast En..."
category: "产品发布/更新"
source_url: https://www.lmsys.org/blog/2026-08-21-sglang-fast-recovery
source_name: "LMSYS：Blog（Chatbot Arena 团队）"
external_permalink: https://aihot.virxact.com/items/cmt393qow0kfiro6tpe87m4nu
comments: false
---

## 摘要

SGLang 团队推出 Weight Cache Daemon，通过 CUDA IPC 零拷贝映射将模型权重加载从约 495 秒降至约 0.63 秒（约 785 倍加速），端到端启动时间减少 93.9%。该守护进程在 GPU 内存中持久化后量化权重，支持多实例共享和亚秒级主备切换，是 Fast Engine Recovery Framework 的第一阶段。

## 原文链接

- [LMSYS：Blog（Chatbot Arena 团队）](https://www.lmsys.org/blog/2026-08-21-sglang-fast-recovery)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmt393qow0kfiro6tpe87m4nu)
