---
title: "Apple 提出 SRLM：自反思程序搜索提升长上下文处理能力"
date: 2026-07-10T08:30:00+08:00
description: "Apple 机器学习研究团队提出 SRLM 框架，利用自一致性、推理链长度和口头置信度三种内在信号，让模型在推理时评估候选长上下文交互程序。实验表明，在相同时间预算下，SRLM 较传统递归语言模型（RLM）最高提升 22%。分析发现，递归本身并非 RLM 性能关键，简单的自反思程序搜索无需显式递归即..."
category: "论文研究"
source_url: https://machinelearning.apple.com/research/self-reflective-program-search
source_name: "Apple Machine Learning Research（RSS）"
external_permalink: https://aihot.virxact.com/items/cmre05t8p000eihwkokpjwaol
comments: false
---

## 摘要

Apple 机器学习研究团队提出 SRLM 框架，利用自一致性、推理链长度和口头置信度三种内在信号，让模型在推理时评估候选长上下文交互程序。实验表明，在相同时间预算下，SRLM 较传统递归语言模型（RLM）最高提升 22%。分析发现，递归本身并非 RLM 性能关键，简单的自反思程序搜索无需显式递归即可匹配或超越 RLM；在模型上下文窗口内，RLM 反而降低性能，而 SRLM 在短上下文和长上下文中均实现稳定增益。

## 原文链接

- [Apple Machine Learning Research（RSS）](https://machinelearning.apple.com/research/self-reflective-program-search)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmre05t8p000eihwkokpjwaol)
