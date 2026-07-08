---
title: "Hugging Face Storage 成为 SkyPilot 一级后端：零出站费跨云存储"
date: 2026-07-08T08:30:00+08:00
description: "Hugging Face Storage 现为 SkyPilot 的一级后端。用户通过 `hf://` URL 和现有 HFTOKEN 即可将 Hugging Face Bucket（读写）或模型/数据集/Space 仓库（只读）挂载到 SkyPilot 任务中，支持 MOUNT（FUSE 懒加载）..."
category: "产品发布/更新"
source_url: https://huggingface.co/blog/skypilot-hf-storage
source_name: "Hugging Face：Blog（RSS）"
external_permalink: https://aihot.virxact.com/items/cmrb18k7802uuihogxse92jx2
comments: false
---

## 摘要

Hugging Face Storage 现为 SkyPilot 的一级后端。用户通过 `hf://` URL 和现有 HFTOKEN 即可将 Hugging Face Bucket（读写）或模型/数据集/Space 仓库（只读）挂载到 SkyPilot 任务中，支持 MOUNT（FUSE 懒加载）或 COPY 模式。SkyPilot 可将任务调度到 20+ 云、Kubernetes、Slurm 及本地集群的任意可用 GPU 上。Hugging Face 不收取出站及 CDN 费用，故跨云读取数据无额外成本。存储价格 $12–18/TB/月，低于 AWS S3 加出站费。Bucket 基于 Xet，增量检查点和模型变体仅存储和传输改…

## 原文链接

- [Hugging Face：Blog（RSS）](https://huggingface.co/blog/skypilot-hf-storage)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrb18k7802uuihogxse92jx2)
