---
title: "利用 Netpreme X‑Mem™ MPU 加速 SGLang HiCache"
date: 2026-07-09T08:30:00+08:00
description: "Netpreme X‑Mem™ 内存处理单元（MPU）作为专用高带宽 KV 内存层与 SGLang HiCache 集成，替代主机 DRAM 作为 L2 卸载层。在基于 Claude Code 代理轨迹的编码工作负载中，前缀缓存命中率平均约 98%。单请求微基准测试显示，首 token 延迟（TTF..."
category: "产品发布/更新"
source_url: https://www.lmsys.org/blog/2026-06-27-netpreme-xmem
source_name: "LMSYS：Blog（Chatbot Arena 团队）"
external_permalink: https://aihot.virxact.com/items/cmrcc7x5901h7ihqc4ucfnsa2
comments: false
---

## 摘要

Netpreme X‑Mem™ 内存处理单元（MPU）作为专用高带宽 KV 内存层与 SGLang HiCache 集成，替代主机 DRAM 作为 L2 卸载层。在基于 Claude Code 代理轨迹的编码工作负载中，前缀缓存命中率平均约 98%。单请求微基准测试显示，首 token 延迟（TTFT）相比主机 DRAM 方案降低约 6.7 倍。在端到端推理基准测试中（20K token 上下文、26 token 输入、20 轮对话），中等负载下每用户吞吐量提升 33%，高负载下交互性提升 50%、系统吞吐量提升 30%。X‑Mem™ 通过 CUDA 和 PyTorch 兼容 API 集成，单节点提供最高 24 TB 内存、4 TB…

## 原文链接

- [LMSYS：Blog（Chatbot Arena 团队）](https://www.lmsys.org/blog/2026-06-27-netpreme-xmem)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrcc7x5901h7ihqc4ucfnsa2)
