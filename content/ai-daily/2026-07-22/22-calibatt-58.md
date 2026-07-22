---
title: "CalibAtt：无需训练的稀疏注意力方法，将文生视频速度提升至 1.58 倍"
date: 2026-07-22T08:30:00+08:00
description: "Apple 与特拉维夫大学联合提出 CalibAtt，一种无需训练的校准稀疏注意力方法，通过离线识别 token 间可跳过的低分连接并编译为优化操作，在推理时跳过无关计算。在 Wan 2.1 14B、Mochi 1 及少步蒸馏模型上，CalibAtt 实现最高 1.58 倍端到端加速，在保持视频质量..."
category: "论文研究"
source_url: https://machinelearning.apple.com/research/calibrated-sparse-attention
source_name: "Apple Machine Learning Research（RSS）"
external_permalink: https://aihot.virxact.com/items/cmruw1v74005vbiymxxxmhf22
comments: false
---

## 摘要

Apple 与特拉维夫大学联合提出 CalibAtt，一种无需训练的校准稀疏注意力方法，通过离线识别 token 间可跳过的低分连接并编译为优化操作，在推理时跳过无关计算。在 Wan 2.1 14B、Mochi 1 及少步蒸馏模型上，CalibAtt 实现最高 1.58 倍端到端加速，在保持视频质量和文本-视频对齐的同时优于现有免训练方法。

## 原文链接

- [Apple Machine Learning Research（RSS）](https://machinelearning.apple.com/research/calibrated-sparse-attention)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmruw1v74005vbiymxxxmhf22)
