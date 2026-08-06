---
title: "Cloudflare 提出智能体访问模型（Agent Access Model）"
date: 2026-08-06T08:30:00+08:00
description: "Cloudflare 发布《The Agent Access Model》论文，提出面向 AI 智能体的访问控制模型 AAM，核心规则是“不信任运行”，对任务执行图中的每个动作基于智能体身份、授权任务及已触达资源进行实时授权。该模型针对智能体的短暂性、机器速度、提示词非边界及跨跳组合权限四大特性设计..."
category: "论文研究"
source_url: https://blog.cloudflare.com/the-agent-access-model
source_name: "Cloudflare Blog"
external_permalink: https://aihot.virxact.com/items/cmsg5h9ax06dsrolg11p7nhvv
comments: false
---

## 摘要

Cloudflare 发布《The Agent Access Model》论文，提出面向 AI 智能体的访问控制模型 AAM，核心规则是“不信任运行”，对任务执行图中的每个动作基于智能体身份、授权任务及已触达资源进行实时授权。该模型针对智能体的短暂性、机器速度、提示词非边界及跨跳组合权限四大特性设计，主张缩小能力集而非仅优化单次决策，并区分单主体控制与多人访问控制的难点。

## 原文链接

- [Cloudflare Blog](https://blog.cloudflare.com/the-agent-access-model)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmsg5h9ax06dsrolg11p7nhvv)
