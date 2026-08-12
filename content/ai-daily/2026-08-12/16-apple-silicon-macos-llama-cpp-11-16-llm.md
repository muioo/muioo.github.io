---
title: "Apple Silicon 与 macOS 虚拟机：借助 Llama.cpp 实现 11–16 倍的 LLM 推理加速"
date: 2026-08-12T08:30:00+08:00
description: "研究团队为 macOS 虚拟机中的 Metal 能力查询构建进程级兼容层，使 llama.cpp 能选用更新的 Metal 内核。在 M1 Ultra 上，TinyLlama 1.1B 的提示处理速度提升 11.08 倍、token 生成提升 16.36 倍，接近裸机性能的 98%；Gemma 4 ..."
category: "论文研究"
source_url: https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmsox86zv09u6rohdqr80wg0x
comments: false
---

## 摘要

研究团队为 macOS 虚拟机中的 Metal 能力查询构建进程级兼容层，使 llama.cpp 能选用更新的 Metal 内核。在 M1 Ultra 上，TinyLlama 1.1B 的提示处理速度提升 11.08 倍、token 生成提升 16.36 倍，接近裸机性能的 98%；Gemma 4 12B 的提示处理与生成速度分别提升 7.20 倍和 14.54 倍。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmsox86zv09u6rohdqr80wg0x)
