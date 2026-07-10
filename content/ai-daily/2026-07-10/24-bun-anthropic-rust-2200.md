---
title: "Bun 被 Anthropic 收购后用 Rust 重写，月下载超 2200 万"
date: 2026-07-10T08:30:00+08:00
description: "Bun 于 2025 年 12 月被 Anthropic 收购，作者使用预发布版 Claude Fable 5 进行了大量 Rust 重写。Bun 最初用 Zig 在一年内构建，如今 CLI 月下载超 2200 万，被 Claude Code 等采用。广泛功能带来稳定性挑战，v1.3.14 修复了多..."
category: "技巧与观点"
source_url: https://bun.com/blog/bun-in-rust
source_name: "Hacker News 热门（buzzing.cc 中文翻译）"
external_permalink: https://aihot.virxact.com/items/cmre2mjao00ncihwk7foifcuk
comments: false
---

## 摘要

Bun 于 2025 年 12 月被 Anthropic 收购，作者使用预发布版 Claude Fable 5 进行了大量 Rust 重写。Bun 最初用 Zig 在一年内构建，如今 CLI 月下载超 2200 万，被 Claude Code 等采用。广泛功能带来稳定性挑战，v1.3.14 修复了多项 use-after-free、内存泄漏等 bug。团队通过 ASAN、Fuzzilli 模糊测试等系统性预防，并借助 Rust 的内存安全特性减少此类缺陷。

## 原文链接

- [Hacker News 热门（buzzing.cc 中文翻译）](https://bun.com/blog/bun-in-rust)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmre2mjao00ncihwk7foifcuk)
