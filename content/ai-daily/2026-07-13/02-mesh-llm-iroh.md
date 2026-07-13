---
title: "Mesh LLM：在 iroh 上进行分布式人工智能计算"
date: 2026-07-13T08:30:00+08:00
description: "Mesh LLM 是一个开源项目，能将用户多台机器上的 GPU 和内存池化，对外暴露兼容 OpenAI 的 API。它通过 iroh 网络库实现点对点连接，无需中央服务器。请求可在本地 GPU 运行、路由到已加载模型的节点，或将大模型按层分区（内部称“Skippy”）流水线式拆分到多台机器。系统内置..."
category: "产品发布/更新"
source_url: https://www.iroh.computer/blog/mesh-llm
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmrh78s5t00w5bir7mozf8oyb
comments: false
---

## 摘要

Mesh LLM 是一个开源项目，能将用户多台机器上的 GPU 和内存池化，对外暴露兼容 OpenAI 的 API。它通过 iroh 网络库实现点对点连接，无需中央服务器。请求可在本地 GPU 运行、路由到已加载模型的节点，或将大模型按层分区（内部称“Skippy”）流水线式拆分到多台机器。系统内置 40 多个模型，从 5 亿参数到 235B MoE 巨模型均可支持。软件体积约 18 MB，启动后以 `localhost:9337/v1` 提供服务。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://www.iroh.computer/blog/mesh-llm)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrh78s5t00w5bir7mozf8oyb)
