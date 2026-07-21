---
title: "Apple 提出 Length Value Model (LenVM)：token 级长度建模框架"
date: 2026-07-21T08:30:00+08:00
description: "Apple 研究团队提出 LenVM，一种在每步解码时预测剩余生成长度的 token 级框架，将长度建模转化为无需标注的价值估计问题。在 LIFEBench 精确长度匹配任务上，LenVM 将 7B 模型的长度分数从 30.9 提升至 64.8，超越前沿闭源模型；在 GSM8K 上以 200 tok..."
category: "论文研究"
source_url: https://machinelearning.apple.com/research/length-value-model
source_name: "Apple Machine Learning Research（RSS）"
external_permalink: https://aihot.virxact.com/items/cmrttgtky2de6bihzoa2eza08
comments: false
---

## 摘要

Apple 研究团队提出 LenVM，一种在每步解码时预测剩余生成长度的 token 级框架，将长度建模转化为无需标注的价值估计问题。在 LIFEBench 精确长度匹配任务上，LenVM 将 7B 模型的长度分数从 30.9 提升至 64.8，超越前沿闭源模型；在 GSM8K 上以 200 token 预算维持 63% 准确率（基线仅 6%）。

## 原文链接

- [Apple Machine Learning Research（RSS）](https://machinelearning.apple.com/research/length-value-model)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrttgtky2de6bihzoa2eza08)
