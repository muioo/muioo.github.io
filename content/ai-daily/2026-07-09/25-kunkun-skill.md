---
title: "在校研究生Kunkun开源管理相互调用Skill的方法"
date: 2026-07-09T08:30:00+08:00
description: "在校研究生Kunkun开源了一套管理大量互相调用Skill的方法。核心方案包括：1）搭建HTML后台，按运行模式（手动/自动）、链路位置、专业领域三类标签筛选Skill；2）将连环调用的Skill绘制成Mermaid流程图，根据debug、新功能、合PR、改设计等阶段定位对应技能组；3）仿照Matt..."
category: "技巧与观点"
source_url: https://x.com/berryxia/status/2074827915779580055
source_name: "X：Berry Xia (@berryxia)"
external_permalink: https://aihot.virxact.com/items/cmrc1iygj00twihyfe1hkvycv
comments: false
---

## 摘要

在校研究生Kunkun开源了一套管理大量互相调用Skill的方法。核心方案包括：1）搭建HTML后台，按运行模式（手动/自动）、链路位置、专业领域三类标签筛选Skill；2）将连环调用的Skill绘制成Mermaid流程图，根据debug、新功能、合PR、改设计等阶段定位对应技能组；3）仿照Matt的ask Matt技能开发“ask me”技能，将调用决策浓缩成上下文喂给模型。该方法避免将所有调用交给模型自行判断，保持工程复杂场景下的人机对齐与可控性。项目已开源至GitHub。

## 原文链接

- [X：Berry Xia (@berryxia)](https://x.com/berryxia/status/2074827915779580055)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrc1iygj00twihyfe1hkvycv)
