---
title: "browser-use 发布开源 AI 视频剪辑 Skill「video-use」"
date: 2026-07-03T08:30:00+08:00
description: "browser-use 团队推出面向 Codex、Claude Code 等 AI 编码智能体的开源 Skill「video-use」，让 LLM 通过 ElevenLabs Scribe 将音频转写为约 12KB 文本（含逐词时间戳、说话人分离、事件标记），仅在决策点调用 timeline_vie..."
category: "技巧与观点"
source_url: https://x.com/shao__meng/status/2072644710523691110
source_name: "X：邵猛 (@shao__meng)"
external_permalink: https://aihot.virxact.com/items/cmr3fluhr00i3sllxli2a5uko
comments: false
---

## 摘要

browser-use 团队推出面向 Codex、Claude Code 等 AI 编码智能体的开源 Skill「video-use」，让 LLM 通过 ElevenLabs Scribe 将音频转写为约 12KB 文本（含逐词时间戳、说话人分离、事件标记），仅在决策点调用 timeline_view.py 生成 PNG 帧图。技术流水线包括转写、打包、生成 JSON 格式 EDL、ffmpeg 渲染及最多 3 轮自评估。渲染关键细节：分段提取 + `-c copy` 拼接、30ms 音频淡入淡出、PTS 时移、字幕最后叠加、HDR 自动映射、竖屏缩放、两-pass loudnorm。动画支持 HyperFrames、Remotio…

## 原文链接

- [X：邵猛 (@shao__meng)](https://x.com/shao__meng/status/2072644710523691110)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmr3fluhr00i3sllxli2a5uko)
