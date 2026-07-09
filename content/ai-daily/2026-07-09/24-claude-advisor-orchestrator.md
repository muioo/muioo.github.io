---
title: "Claude开发者分享两种多智能体模式：Advisor和Orchestrator"
date: 2026-07-09T08:30:00+08:00
description: "Claude开发者官方分享团队高频使用的两种多智能体模式。Advisor模式：Sonnet 5作为执行者，通过tool call调用Fable 5获取指导。SWE-bench Pro（482题）上，Sonnet 5单独75.5%/$0.75，加顾问达84%/$1.40，Fable 5单独91.5%/..."
category: "技巧与观点"
source_url: https://x.com/shao__meng/status/2074661249804366310
source_name: "X：邵猛 (@shao__meng)"
external_permalink: https://aihot.virxact.com/items/cmrbdqlcv02y4ihl11xbxx9xs
comments: false
---

## 摘要

Claude开发者官方分享团队高频使用的两种多智能体模式。Advisor模式：Sonnet 5作为执行者，通过tool call调用Fable 5获取指导。SWE-bench Pro（482题）上，Sonnet 5单独75.5%/$0.75，加顾问达84%/$1.40，Fable 5单独91.5%/$2.25；组合方案约92%性能、63%成本。Orchestrator模式：Fable 5作为编排者规划并向多个Sonnet 5 worker扇出任务。BrowseComp上，全Sonnet 5 77.8%/$16.01，编排方案86.8%/$18.53，全Fable 5 90.8%/$40.56；编排方案约96%性能、46%成本。

## 原文链接

- [X：邵猛 (@shao__meng)](https://x.com/shao__meng/status/2074661249804366310)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrbdqlcv02y4ihl11xbxx9xs)
