---
title: "Mooncake 如何为 Miles 强化学习系统实现高效批量 Rollout 数据传输"
date: 2026-08-21T08:30:00+08:00
description: "大规模 LLM 强化学习采用解耦架构后，rollout 数据从推理侧到训练侧的传输成为瓶颈。Mooncake 针对 Miles 系统中异构、碎片化的 rollout 数据（如 list[np.ndarray] 形式的 tokens、loss_masks、rollout_log_probs），通过批量..."
category: "产品发布/更新"
source_url: https://www.lmsys.org/blog/2026-08-20-miles-mooncake-rollout-data-transfer
source_name: "LMSYS：Blog（Chatbot Arena 团队）"
external_permalink: https://aihot.virxact.com/items/cmt1tnrvi07h4roov529jj7fn
comments: false
---

## 摘要

大规模 LLM 强化学习采用解耦架构后，rollout 数据从推理侧到训练侧的传输成为瓶颈。Mooncake 针对 Miles 系统中异构、碎片化的 rollout 数据（如 list[np.ndarray] 形式的 tokens、loss_masks、rollout_log_probs），通过批量 I/O 优化实现高效传输，同时满足效率、正确性、可扩展性、灵活性和可预测的交接延迟等要求。

## 原文链接

- [LMSYS：Blog（Chatbot Arena 团队）](https://www.lmsys.org/blog/2026-08-20-miles-mooncake-rollout-data-transfer)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmt1tnrvi07h4roov529jj7fn)
