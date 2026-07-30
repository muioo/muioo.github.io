---
title: "Miles 在 Blackwell 架构上实现端到端 MXFP8 与逐 token NVFP4 强化学习方案"
date: 2026-07-30T08:30:00+08:00
description: "Miles 团队在 Blackwell 架构上实现了两种原生低精度强化学习方案：端到端 MXFP8 和 MoE 专家权重的逐 token NVFP4。在 8x B200 上对 Qwen3-30B-A3B 的消融实验中，BF16 与所有五种低精度配置的原始奖励曲线高度重合，且 MXFP8 和 NVFP..."
category: "论文研究"
source_url: https://www.lmsys.org/blog/2026-07-29-mxfp8-nvfp4-rl
source_name: "LMSYS：Blog（Chatbot Arena 团队）"
external_permalink: https://aihot.virxact.com/items/cms6drkj8001crohzuxf7kfy7
comments: false
---

## 摘要

Miles 团队在 Blackwell 架构上实现了两种原生低精度强化学习方案：端到端 MXFP8 和 MoE 专家权重的逐 token NVFP4。在 8x B200 上对 Qwen3-30B-A3B 的消融实验中，BF16 与所有五种低精度配置的原始奖励曲线高度重合，且 MXFP8 和 NVFP4 减少了推理时间。

## 原文链接

- [LMSYS：Blog（Chatbot Arena 团队）](https://www.lmsys.org/blog/2026-07-29-mxfp8-nvfp4-rl)
- [AI HOT 详情页](https://aihot.virxact.com/items/cms6drkj8001crohzuxf7kfy7)
