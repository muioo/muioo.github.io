---
title: "借用夜晚：将闲置推理GPU回收用于研究"
date: 2026-07-03T08:30:00+08:00
description: "Runway 开发了名为 deckard 的容量控制器，在生产推理集群与研究集群间动态重分配 GPU。生产流量在北美工作日上午 9 点 ET 达峰，晚 8 点 ET 跌至不足一半。控制器基于预计算的时间窗口（如工作日 8:30–12:30 ET 高峰子窗口）提前扩容和回收，每次集群间转移耗时 20–..."
category: "技巧与观点"
source_url: https://runwayml.com/news/borrowing-the-night-reclaiming-idle-inference-gpus-for-research
source_name: "Runway：News（网页）"
external_permalink: https://aihot.virxact.com/items/cmr41g5dr001ssln2uyz531b9
comments: false
---

## 摘要

Runway 开发了名为 deckard 的容量控制器，在生产推理集群与研究集群间动态重分配 GPU。生产流量在北美工作日上午 9 点 ET 达峰，晚 8 点 ET 跌至不足一半。控制器基于预计算的时间窗口（如工作日 8:30–12:30 ET 高峰子窗口）提前扩容和回收，每次集群间转移耗时 20–60 分钟。利用排队论（Erlang‑C、Little's Law）确定目标利用率，避免接近 85% 后的队列发散（90% 利用率下等待时间约为服务时间的 10 倍）。此方案使夜间闲置 GPU 回归研究、白天排队等待缩短。

## 原文链接

- [Runway：News（网页）](https://runwayml.com/news/borrowing-the-night-reclaiming-idle-inference-gpus-for-research)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmr41g5dr001ssln2uyz531b9)
