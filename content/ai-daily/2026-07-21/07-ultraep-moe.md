---
title: "小红书与北大开源 UltraEP：面向大规模 MoE 训推的实时负载均衡方案"
date: 2026-07-21T08:30:00+08:00
description: "小红书与北大提出 UltraEP，首次将基于精确路由信息的实时负载均衡引入生产系统，在每个 microbatch 和每一层动态复制热点专家。在 Qwen3-235B 等模型上，训练吞吐平均达到理想性能的 94.6%，相比 Megatron-LM 提升 42%；推理 prefill 吞吐相比 SGLa..."
category: "产品发布/更新"
source_url: https://mp.weixin.qq.com/s/rAoF65ywi5trWbI-heJieg
source_name: "公众号：小红书技术（dots.llm）"
external_permalink: https://aihot.virxact.com/items/cmrsy2z9e03wpbitlqgh25fol
comments: false
---

## 摘要

小红书与北大提出 UltraEP，首次将基于精确路由信息的实时负载均衡引入生产系统，在每个 microbatch 和每一层动态复制热点专家。在 Qwen3-235B 等模型上，训练吞吐平均达到理想性能的 94.6%，相比 Megatron-LM 提升 42%；推理 prefill 吞吐相比 SGLang 提升 1.56 倍。

## 原文链接

- [公众号：小红书技术（dots.llm）](https://mp.weixin.qq.com/s/rAoF65ywi5trWbI-heJieg)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrsy2z9e03wpbitlqgh25fol)
