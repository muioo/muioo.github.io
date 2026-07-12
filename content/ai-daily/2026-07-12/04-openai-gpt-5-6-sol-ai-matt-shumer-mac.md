---
title: "OpenAI GPT-5.6-Sol 删光 AI 创业者 Matt Shumer 的 Mac 硬盘"
date: 2026-07-12T08:30:00+08:00
description: "知名 AI 创业者 Matt Shumer 的 Mac 硬盘被 OpenAI 最新 Agent 模型 GPT-5.6-Sol 彻底清空。他在本地 Agent 上开启 Full Access 权限，让 subagent 执行文件清理任务，结果 shell 变量 $HOME 路径解析错误，Agent 直..."
category: "行业动态"
source_url: https://x.com/AYi_AInotes/status/2075761215251312722
source_name: "X：阿易 AI Notes (@AYi_AInotes)"
external_permalink: https://aihot.virxact.com/items/cmrfr2xvi02brihjlp1tlzg1n
comments: false
---

## 摘要

知名 AI 创业者 Matt Shumer 的 Mac 硬盘被 OpenAI 最新 Agent 模型 GPT-5.6-Sol 彻底清空。他在本地 Agent 上开启 Full Access 权限，让 subagent 执行文件清理任务，结果 shell 变量 $HOME 路径解析错误，Agent 直接执行 `rm -rf /Users/mattsdevbox`，导致数年代码、文件、照片丢失。该任务此前已安全运行数百次。事后 Agent 自动生成事故报告承认错误。Matt 表示“1000x 更信任 Anthropic 的 Fable”。事件暴露 Agent 行业核心风险：顶级模型仍会在变量展开、路径等细节翻车；Subagent + 长…

## 原文链接

- [X：阿易 AI Notes (@AYi_AInotes)](https://x.com/AYi_AInotes/status/2075761215251312722)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmrfr2xvi02brihjlp1tlzg1n)
