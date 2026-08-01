---
title: "GitHub 开源 casefold：以内存速度进行源码大小写折叠"
date: 2026-08-01T08:30:00+08:00
description: "GitHub 为代码搜索引擎 Blackbird 优化大小写折叠性能，该引擎索引超 1.8 亿个仓库、480TB 源码。团队发现移除提前退出分支比保留优化更快，最终在 Apple M4 上实现超 45 GiB/s 吞吐，接近内存带宽。结果已开源为 Rust crate `casefold`，仅实现简..."
category: "技巧与观点"
source_url: https://github.blog/engineering/architecture-optimization/dont-stop-early-case-folding-source-code-at-memory-speed
source_name: "GitHub Blog"
external_permalink: https://aihot.virxact.com/items/cms96k3tf05w8ro9kmy0s9bjp
comments: false
---

## 摘要

GitHub 为代码搜索引擎 Blackbird 优化大小写折叠性能，该引擎索引超 1.8 亿个仓库、480TB 源码。团队发现移除提前退出分支比保留优化更快，最终在 Apple M4 上实现超 45 GiB/s 吞吐，接近内存带宽。结果已开源为 Rust crate `casefold`，仅实现简单（1 对 1）折叠，与 ripgrep 等工具保持一致。

## 原文链接

- [GitHub Blog](https://github.blog/engineering/architecture-optimization/dont-stop-early-case-folding-source-code-at-memory-speed)
- [AI HOT 详情页](https://aihot.virxact.com/items/cms96k3tf05w8ro9kmy0s9bjp)
