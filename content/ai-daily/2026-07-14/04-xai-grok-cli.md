---
title: "xAI 官方 Grok CLI 被曝静默上传整个代码库及用户密钥"
date: 2026-07-14T08:30:00+08:00
description: "安全研究者发现，xAI 官方 Grok CLI（npm 包 `@xai-official/grok` 0.2.93 版）会在每轮任务前后，将当前工作目录打包为 `before_codebase.tar.gz` 和 `after_codebase.tar.gz`，通过独立旁路通道静默上传至 xAI 的..."
category: "行业动态"
source_url: https://mp.weixin.qq.com/s/6c6vGMJAVMbh6UhNVw4dcg
source_name: "公众号：数字生命卡兹克"
external_permalink: https://aihot.virxact.com/items/cmriguktg00arbijpt0l7c2vh
comments: false
---

## 摘要

安全研究者发现，xAI 官方 Grok CLI（npm 包 `@xai-official/grok` 0.2.93 版）会在每轮任务前后，将当前工作目录打包为 `before_codebase.tar.gz` 和 `after_codebase.tar.gz`，通过独立旁路通道静默上传至 xAI 的 Google Cloud 仓库。验证显示，即使模型仅回复一个单词，上传依然发生。上传包还包含仓库外的 `~/.claude.json`、Claude Code 设置、全局 AGENTS 规则、30 多个 Skill 文件及一个 API 密钥。7 月 13 日凌晨，xAI 通过服务端远程开关新增 `disable_codebase_upl…

## 原文链接

- [公众号：数字生命卡兹克](https://mp.weixin.qq.com/s/6c6vGMJAVMbh6UhNVw4dcg)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmriguktg00arbijpt0l7c2vh)
