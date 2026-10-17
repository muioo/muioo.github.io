---
title: "Anthropic 用 Claude 揭开 NIST ECDSA 曲线种子来源之谜"
date: 2026-10-17T08:30:00+08:00
description: "Anthropic 团队让内部研究模型在不到半小时内发现 NIST P-192、P-224、P-256、P-384、P-521 等曲线种子的来源：它们并非哈希结果，而是以 Unix 时间戳初始化的 C 库 lrand48 随机数生成器的输出，例如 P-256 需要 1842 次迭代。"
category: "论文研究"
source_url: https://www.anthropic.com/research/ecdsa-curve-origins
source_name: "Anthropic：Research（发表成果 · 网页）"
external_permalink: https://aihot.news/items/ckrtcqc9dnngil5ev7m60ns4v
comments: false
---

## 摘要

Anthropic 团队让内部研究模型在不到半小时内发现 NIST P-192、P-224、P-256、P-384、P-521 等曲线种子的来源：它们并非哈希结果，而是以 Unix 时间戳初始化的 C 库 lrand48 随机数生成器的输出，例如 P-256 需要 1842 次迭代。

## 原文链接

- [Anthropic：Research（发表成果 · 网页）](https://www.anthropic.com/research/ecdsa-curve-origins)
- [AI HOT 详情页](https://aihot.news/items/ckrtcqc9dnngil5ev7m60ns4v)
