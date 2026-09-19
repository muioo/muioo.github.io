---
title: "Trail of Bits 用 Agent 为 Miden zkVM 审计自建 LSP、反编译器和 Lean 形式化证明"
date: 2026-09-19T08:30:00+08:00
description: "Trail of Bits 在审计 Miden zkVM 前，让 Agent 用六个月从零构建了 MASM 的 LSP 服务器、反编译器、静态分析引擎和 Lean VM 执行器模型。这些工具发现了可让恶意 prover 伪造 Falcon 签名盗取资金的高危漏洞，静态分析定位了 400 多处类型验证..."
category: "技巧与观点"
source_url: https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai
source_name: "Trail of Bits：AI安全研究"
external_permalink: https://aihot.news/items/cmu6w30lt0dnhrowkh7qwiped
comments: false
---

## 摘要

Trail of Bits 在审计 Miden zkVM 前，让 Agent 用六个月从零构建了 MASM 的 LSP 服务器、反编译器、静态分析引擎和 Lean VM 执行器模型。这些工具发现了可让恶意 prover 伪造 Falcon 签名盗取资金的高危漏洞，静态分析定位了 400 多处类型验证缺陷，Lean 工作产出 95 个机器验证的正确性证明，还发现两个单元测试未捕获的细微 bug。

## 原文链接

- [Trail of Bits：AI安全研究](https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai)
- [AI HOT 详情页](https://aihot.news/items/cmu6w30lt0dnhrowkh7qwiped)
