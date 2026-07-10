---
title: "TGPO：通过可验证奖励强化学习激励第一人称视频时序感知"
date: 2026-07-10T08:30:00+08:00
description: "多模态大语言模型（MLLM）在第一人称视频理解中缺乏时序感知，常依赖空间捷径。为此，研究者提出 Temporal Global Policy Optimization（TGPO），一种基于可验证奖励的强化学习算法。TGPO 通过对比模型在时序有序与打乱帧上的输出，生成全局归一化奖励信号，明确奖励时序..."
category: "论文研究"
source_url: https://machinelearning.apple.com/research/incentivizing-temporal-awareness-egocentric
source_name: "Apple Machine Learning Research（RSS）"
external_permalink: https://aihot.virxact.com/items/cmrdpfzhr05x8ih4berz6jnks
comments: false
---

## 摘要

多模态大语言模型（MLLM）在第一人称视频理解中缺乏时序感知，常依赖空间捷径。为此，研究者提出 Temporal Global Policy Optimization（TGPO），一种基于可验证奖励的强化学习算法。TGPO 通过对比模型在时序有序与打乱帧上的输出，生成全局归一化奖励信号，明确奖励时序连贯推理。TGPO 可集成 GRPO 和 GSPO，支持冷启动 RL 训练，抑制 MLLM 的空间捷径行为。在五个第一人称视频基准上，TGPO 一致提升时序定位与因果连贯性，优于此前基于 RL 的视频推理方法。

## 原文链接

- [Apple Machine Learning Research（RSS）](https://machinelearning.apple.com/research/incentivizing-temporal-awareness-egocentric)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrdpfzhr05x8ih4berz6jnks)
