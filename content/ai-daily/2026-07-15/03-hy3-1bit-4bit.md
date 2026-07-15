---
title: "腾讯混元 Hy3 量化版发布：1bit 版本单卡可部署，4bit 版本接近满血性能"
date: 2026-07-15T08:30:00+08:00
description: "腾讯混元团队为旗舰模型 Hy3（295B 参数）推出量化版本。1bit 版本（IQ1_M）将权重从 598 GB 压缩至 85.5 GiB，缩小 6.7 倍，单张 96GB 推理显卡即可部署；4bit 版本（Q4_K_M）体积 169.9 GiB，两张显卡可承载。量化版在 Agent、多语言代码、工..."
category: "模型发布/更新"
source_url: https://mp.weixin.qq.com/s/Kq30ftirASryPrUtjK2xSw
source_name: "公众号：腾讯混元"
external_permalink: https://aihot.virxact.com/items/cmrkf8gun01a4bizsthjytx6c
comments: false
---

## 摘要

腾讯混元团队为旗舰模型 Hy3（295B 参数）推出量化版本。1bit 版本（IQ1_M）将权重从 598 GB 压缩至 85.5 GiB，缩小 6.7 倍，单张 96GB 推理显卡即可部署；4bit 版本（Q4_K_M）体积 169.9 GiB，两张显卡可承载。量化版在 Agent、多语言代码、工具调用、长文理解等任务上表现接近满血模型。团队还提供 GPTQ Int4 版本，支持 vLLM 部署。配合 MTP 投机解码，1bit 版本解码速度提升约 50%，4bit 版本提升近 60%。所有版本已开源并打包为 GGUF 格式，适配 llama.cpp 生态。

## 原文链接

- [公众号：腾讯混元](https://mp.weixin.qq.com/s/Kq30ftirASryPrUtjK2xSw)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrkf8gun01a4bizsthjytx6c)
