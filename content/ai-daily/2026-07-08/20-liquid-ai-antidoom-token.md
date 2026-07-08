---
title: "Liquid AI 开源 Antidoom：基于最终 Token 偏好优化的推理模型死循环修复方法"
date: 2026-07-08T08:30:00+08:00
description: "Liquid AI 开源了 Antidoom，一种基于 Final Token Preference Optimization (FTPO) 的针对性修复方法，用于减少推理模型中的 doom loop（死循环）问题。该方法定位循环开始的第一个 token，训练模型选择连贯替代项，而不改变整体输出分布..."
category: "技巧与观点"
source_url: https://www.marktechpost.com/2026/07/07/liquid-ai-antidoom-doom-loops-ftpo
source_name: "MarkTechPost（RSS）"
external_permalink: https://aihot.virxact.com/items/cmraw21y401jhihog3tcrfsp4
comments: false
---

## 摘要

Liquid AI 开源了 Antidoom，一种基于 Final Token Preference Optimization (FTPO) 的针对性修复方法，用于减少推理模型中的 doom loop（死循环）问题。该方法定位循环开始的第一个 token，训练模型选择连贯替代项，而不改变整体输出分布。在 LFM2.5-2.6B 上，硬数学和编程任务中的循环率从 10.2% 降至 1.4%；Qwen3.5-4B 上从 22.9% 降至 1%。整套流程可在数小时内完成，全部代码和数据集（LiquidAI/antidoom-mix-v1.0）已开源。

## 原文链接

- [MarkTechPost（RSS）](https://www.marktechpost.com/2026/07/07/liquid-ai-antidoom-doom-loops-ftpo)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmraw21y401jhihog3tcrfsp4)
