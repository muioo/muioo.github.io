---
title: "Pulpie：用于清理网络的Pareto最优模型"
date: 2026-07-09T08:30:00+08:00
description: "Pulpie是一族Pareto最优模型，用于从HTML页面提取主要内容。其最小模型pulpie-orange-small（210M参数）在WebMainBench上取得0.862的ROUGE-5 F1分数，接近600M参数的Dripper（0.864），但成本仅1/20。在NVIDIA L4 GPU..."
category: "模型发布/更新"
source_url: https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmrbez8y903b9ihl133b5wr18
comments: false
---

## 摘要

Pulpie是一族Pareto最优模型，用于从HTML页面提取主要内容。其最小模型pulpie-orange-small（210M参数）在WebMainBench上取得0.862的ROUGE-5 F1分数，接近600M参数的Dripper（0.864），但成本仅1/20。在NVIDIA L4 GPU上，Pulpie处理速度13.7页/秒，Dripper仅0.68页/秒。清理10亿页HTML，Pulpie成本约$7,900，Dripper需$159,000。模型采用编码器架构，单次前向传播即可标记每个HTML块为内容或模板，已在HuggingFace开源。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrbez8y903b9ihl133b5wr18)
