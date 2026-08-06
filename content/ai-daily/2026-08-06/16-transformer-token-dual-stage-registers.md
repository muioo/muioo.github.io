---
title: "驯服扩散 Transformer 中的离群 token：Dual-Stage Registers 干预"
date: 2026-08-06T08:30:00+08:00
description: "研究发现扩散 Transformer（DiT）图像生成流程中，预训练 ViT 编码器和 DiT 去噪器均会产生离群 token，尤其在中间层，且简单掩蔽高范数 token 无法改善性能，问题与局部 patch 语义损坏相关。为此提出 Dual-Stage Registers（DSR）干预方法，在 I..."
category: "论文研究"
source_url: https://machinelearning.apple.com/research/taming-outlier-tokens
source_name: "Apple Machine Learning Research（RSS）"
external_permalink: https://aihot.virxact.com/items/cmsgonfuv0bparo5q6a2ng1pd
comments: false
---

## 摘要

研究发现扩散 Transformer（DiT）图像生成流程中，预训练 ViT 编码器和 DiT 去噪器均会产生离群 token，尤其在中间层，且简单掩蔽高范数 token 无法改善性能，问题与局部 patch 语义损坏相关。为此提出 Dual-Stage Registers（DSR）干预方法，在 ImageNet 和文生图任务上持续减少离群伪影并提升生成质量。

## 原文链接

- [Apple Machine Learning Research（RSS）](https://machinelearning.apple.com/research/taming-outlier-tokens)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmsgonfuv0bparo5q6a2ng1pd)
