---
title: "DynaMiCS：带性能约束的大语言模型动态混合微调"
date: 2026-07-08T08:30:00+08:00
description: "DynaMiCS是一种动态混合优化器，将多领域微调建模为带性能约束的优化问题。它通过短领域特定探测运行估计跨领域效应斜率矩阵，再基于概率单纯形优化计算混合权重，在提升目标领域性能的同时将约束领域损失维持在参考水平以下。实验表明，DynaMiCS相比固定混合基线取得更强的目标领域提升和约束满足，且计算..."
category: "论文研究"
source_url: https://machinelearning.apple.com/research/dynamics-fine-tuning-llms
source_name: "Apple Machine Learning Research（RSS）"
external_permalink: https://aihot.virxact.com/items/cmrasd6r300hxihog9hxmteoz
comments: false
---

## 摘要

DynaMiCS是一种动态混合优化器，将多领域微调建模为带性能约束的优化问题。它通过短领域特定探测运行估计跨领域效应斜率矩阵，再基于概率单纯形优化计算混合权重，在提升目标领域性能的同时将约束领域损失维持在参考水平以下。实验表明，DynaMiCS相比固定混合基线取得更强的目标领域提升和约束满足，且计算成本更低，无需参考模型、逐样本评分或手动调节混合权重。

## 原文链接

- [Apple Machine Learning Research（RSS）](https://machinelearning.apple.com/research/dynamics-fine-tuning-llms)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrasd6r300hxihog9hxmteoz)
