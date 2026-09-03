---
title: "Google AI 团队分享如何为 LLM-as-a-Judge 评测编写可靠的评分标准"
date: 2026-09-03T08:30:00+08:00
description: "Google AI 团队发布教程，讲解如何为 LLM-as-a-Judge 评测编写可靠的布尔式评分标准，指出模糊提示会导致评估不一致和浪费 token。文中给出四条经验：问题保持原子化且互不重叠、只让评判模型评估客观事实（可用 RFC 2119 术语如 MUST 表述）、只评 prompt 中明确..."
category: "技巧与观点"
source_url: https://dev.to/googleai/how-to-write-reliable-rubrics-for-llm-as-a-judge-evaluations-ndp
source_name: "Google AI：DEV 作者专属（RSS）"
external_permalink: https://aihot.virxact.com/items/cmtkbz92801nmrowy61g2fsob
comments: false
---

## 摘要

Google AI 团队发布教程，讲解如何为 LLM-as-a-Judge 评测编写可靠的布尔式评分标准，指出模糊提示会导致评估不一致和浪费 token。文中给出四条经验：问题保持原子化且互不重叠、只让评判模型评估客观事实（可用 RFC 2119 术语如 MUST 表述）、只评 prompt 中明确要求的内容、用专家标注的 golden set 校准评判模型直至与人类评分一致。

## 原文链接

- [Google AI：DEV 作者专属（RSS）](https://dev.to/googleai/how-to-write-reliable-rubrics-for-llm-as-a-judge-evaluations-ndp)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmtkbz92801nmrowy61g2fsob)
