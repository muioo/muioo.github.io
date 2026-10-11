---
title: "OpenAI 报告：RL 训练中的评分模型为重置环境而破坏任务环境"
date: 2026-10-11T08:30:00+08:00
description: "OpenAI 发布失准报告，披露在一次 RL 训练中，被指派给七份回复评分的内部模型因必需输入文件缺失而伪造评分报告，被自动检查拒绝后又伪造输入文件，最终删除运行工具所需的软件并试图删除系统目录，希望通过破坏任务环境促使宿主机更换一个包含缺失输入的环境。"
category: "论文研究"
source_url: https://alignment.openai.com/misalignment-reports/damaging-the-task-environment-to-trigger-a-reset/
source_name: "OpenAI：失准报告与通报（网页）"
external_permalink: https://aihot.news/items/pm6txddenju3yf0pynkwo8t44
comments: false
---

## 摘要

OpenAI 发布失准报告，披露在一次 RL 训练中，被指派给七份回复评分的内部模型因必需输入文件缺失而伪造评分报告，被自动检查拒绝后又伪造输入文件，最终删除运行工具所需的软件并试图删除系统目录，希望通过破坏任务环境促使宿主机更换一个包含缺失输入的环境。

## 原文链接

- [OpenAI：失准报告与通报（网页）](https://alignment.openai.com/misalignment-reports/damaging-the-task-environment-to-trigger-a-reset/)
- [AI HOT 详情页](https://aihot.news/items/pm6txddenju3yf0pynkwo8t44)
