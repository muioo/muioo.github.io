---
title: "GitHub Copilot 代码审查改用共享工具后性能下降，通过重写指令实现 20% 成本降低"
date: 2026-07-11T08:30:00+08:00
description: "GitHub 在 Copilot 代码审查中尝试用 Copilot CLI 的共享代码探索工具（grep、glob、view）替换原有专用工具，结果导致审查成本上升、有效评论数量下降。分析 trace 发现，问题不在工具本身，而在于指令让智能体像通用编程助手一样大范围浏览仓库，而非像审查者一样从 d..."
category: "技巧与观点"
source_url: https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it
source_name: "GitHub Blog"
external_permalink: https://aihot.virxact.com/items/cmrf54vpm006yihg8qjqnynnd
comments: false
---

## 摘要

GitHub 在 Copilot 代码审查中尝试用 Copilot CLI 的共享代码探索工具（grep、glob、view）替换原有专用工具，结果导致审查成本上升、有效评论数量下降。分析 trace 发现，问题不在工具本身，而在于指令让智能体像通用编程助手一样大范围浏览仓库，而非像审查者一样从 diff 出发进行定向搜索。重写指令后，审查平均成本降低约 20%，同时保持相同审查质量。

## 原文链接

- [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrf54vpm006yihg8qjqnynnd)
