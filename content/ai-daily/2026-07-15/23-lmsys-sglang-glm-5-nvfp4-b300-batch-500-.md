---
title: "LMSYS 与 SGLang 团队为 GLM-5.2 NVFP4 推出推理优化，8×B300 单 batch 解码超 500 TPS"
date: 2026-07-15T08:30:00+08:00
description: "LMSYS 与 SGLang 团队针对智谱 GLM-5.2 NVFP4 模型在 Grace Blackwell 硬件上推出多项优化。运行时方面，Spec V2 重叠调度消除 GPU 气泡，端到端 TPS 提升 11%；IndexShare MTP 在 draft 步骤间复用 DSA indexer ..."
category: "技巧与观点"
source_url: https://www.lmsys.org/blog/2026-07-13-glm52-optimization
source_name: "LMSYS：Blog（Chatbot Arena 团队）"
external_permalink: https://aihot.virxact.com/items/cmrkxc995000cbim4oputx7jf
comments: false
---

## 摘要

LMSYS 与 SGLang 团队针对智谱 GLM-5.2 NVFP4 模型在 Grace Blackwell 硬件上推出多项优化。运行时方面，Spec V2 重叠调度消除 GPU 气泡，端到端 TPS 提升 11%；IndexShare MTP 在 draft 步骤间复用 DSA indexer 的 top-k，长上下文下 draft 步骤成本降低约 1.9 倍。内核方面，TopK-V2 将 TopK 视为选择问题，80K ISL 下平均延迟从 40.7 µs 降至 17.5 µs（2.33× 加速），1M ISL 下从 372.1 µs 降至 36.6 µs（10.17× 加速）。优化后 8×B300 单 batch 解码吞吐超…

## 原文链接

- [LMSYS：Blog（Chatbot Arena 团队）](https://www.lmsys.org/blog/2026-07-13-glm52-optimization)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrkxc995000cbim4oputx7jf)
