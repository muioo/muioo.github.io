---
title: "小红书发布大模型新架构 PIPO"
date: 2026-07-11T08:30:00+08:00
description: "小红书提出 PIPO 架构，通过输入侧压缩器将两个 token 折叠为一个 latent，输出侧 MTP head 将隐藏状态展开为额外 token，实现输入长度减半、每步输出翻倍。基于 Qwen3.5-4B/9B backbone，在 AIME 2025 等基准上最高带来 +7.15 pass@4..."
category: "论文研究"
source_url: https://mp.weixin.qq.com/s/1eo7rrCAH-OA0TnXwwqJEg
source_name: "公众号：小红书技术（dots.llm）"
external_permalink: https://aihot.virxact.com/items/cmrerlfrs0046ihm87smc2el4
comments: false
---

## 摘要

小红书提出 PIPO 架构，通过输入侧压缩器将两个 token 折叠为一个 latent，输出侧 MTP head 将隐藏状态展开为额外 token，实现输入长度减半、每步输出翻倍。基于 Qwen3.5-4B/9B backbone，在 AIME 2025 等基准上最高带来 +7.15 pass@4 提升。部署测评中，TTFT 加速约 1.23×，TPOT 加速约 1.86×。训练采用 SFT 和 On-Policy Distillation 两阶段，将 verifier 校验能力蒸馏进轻量 confidence head。

## 原文链接

- [公众号：小红书技术（dots.llm）](https://mp.weixin.qq.com/s/1eo7rrCAH-OA0TnXwwqJEg)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrerlfrs0046ihm87smc2el4)
