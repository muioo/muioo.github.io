---
title: "OpenRouter 教程：如何从生产流量构建 golden 评测集并跨模型复测"
date: 2026-10-01T08:30:00+08:00
description: "OpenRouter 发布教程，讲解如何从生产流量构建 golden 评测集，作为每次部署前的回归测试。内容涵盖五步流程（抽样生产流量、去重聚类、添加预期输出、首轮评估修正 rubric、提交 Git 并接入 CI），建议从 20 至 50 条复审样本起步、扩展到 100 至 1,000 条完整回归..."
category: "技巧与观点"
source_url: https://openrouter.ai/blog/tutorials/building-a-golden-eval-dataset-from-production-traffic/
source_name: "OpenRouter：Announcements（RSS）"
external_permalink: https://aihot.news/items/fibq25b0liw1wvpxc0kg5kktn
comments: false
---

## 摘要

OpenRouter 发布教程，讲解如何从生产流量构建 golden 评测集，作为每次部署前的回归测试。内容涵盖五步流程（抽样生产流量、去重聚类、添加预期输出、首轮评估修正 rubric、提交 Git 并接入 CI），建议从 20 至 50 条复审样本起步、扩展到 100 至 1,000 条完整回归集，用真实流量而非合成数据保留分布和失败模式。

## 原文链接

- [OpenRouter：Announcements（RSS）](https://openrouter.ai/blog/tutorials/building-a-golden-eval-dataset-from-production-traffic/)
- [AI HOT 详情页](https://aihot.news/items/fibq25b0liw1wvpxc0kg5kktn)
