---
title: "Cactus 发布 Gemma 4 E2B Hybrid：可在设备端为每个回答输出置信度分数，低分时自动路由至更大模型"
date: 2026-07-24T08:30:00+08:00
description: "Cactus 推出基于 Gemma 4 的混合模型“Cactus Hybrid”，在模型检查点内嵌入置信度探针，为每个生成答案输出 0-1 之间的结构化置信度分数。高置信度时在设备端直接回答，低分时可自动路由至更大模型。该探针在零音频训练数据下，于四个音频基准上达到 0.79-0.88 AUROC，..."
category: "模型发布/更新"
source_url: https://github.com/cactus-compute/cactus-hybrid
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmrx3iki50075ro694xrjogs3
comments: false
---

## 摘要

Cactus 推出基于 Gemma 4 的混合模型“Cactus Hybrid”，在模型检查点内嵌入置信度探针，为每个生成答案输出 0-1 之间的结构化置信度分数。高置信度时在设备端直接回答，低分时可自动路由至更大模型。该探针在零音频训练数据下，于四个音频基准上达到 0.79-0.88 AUROC，远超 token 熵基线（均值 0.549），且 MIT 协议开源。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://github.com/cactus-compute/cactus-hybrid)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrx3iki50075ro694xrjogs3)
