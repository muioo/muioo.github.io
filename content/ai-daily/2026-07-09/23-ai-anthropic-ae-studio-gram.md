---
title: "面向AI模型双重用途知识的“开关”：Anthropic与AE Studio提出GRAM方法"
date: 2026-07-09T08:30:00+08:00
description: "Anthropic与AE Studio联合提出梯度路由辅助模块（GRAM）方法，通过在Transformer每层添加可移除的神经元模块，使模型在训练时将病毒学、网络安全、核物理、专业编程语言等双重用途知识仅路由到对应模块，而非扩散至全局。训练后删除模块即可消除该能力，保留则供可信部署使用。实验在合成..."
category: "论文研究"
source_url: https://www.anthropic.com/research/off-switch-dual-use
source_name: "Anthropic：Research（发表成果 · 网页）"
external_permalink: https://aihot.virxact.com/items/cmrcpjgf00373ihx5mtyo2fsy
comments: false
---

## 摘要

Anthropic与AE Studio联合提出梯度路由辅助模块（GRAM）方法，通过在Transformer每层添加可移除的神经元模块，使模型在训练时将病毒学、网络安全、核物理、专业编程语言等双重用途知识仅路由到对应模块，而非扩散至全局。训练后删除模块即可消除该能力，保留则供可信部署使用。实验在合成数据、真实数据及50M到5B参数模型上测试，GRAM效果与数据过滤相当，移除模块不降低通用性能，且比事后“遗忘”技术更难恢复。该研究为平衡双重用途知识的安全访问与有益使用提供了更鲁棒的方案。

## 原文链接

- [Anthropic：Research（发表成果 · 网页）](https://www.anthropic.com/research/off-switch-dual-use)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrcpjgf00373ihx5mtyo2fsy)
