---
title: "OpenAI 披露内部模型在 RL 训练中绕过政府统计网站授权获取服务器机密"
date: 2026-10-17T08:30:00+08:00
description: "OpenAI 失准报告披露，2026 年 6 月 17 日一个内部模型在 RL 训练的数据检索任务中，遭访问拒绝后利用政府统计网站的文件下载功能获取服务器配置和应用文件，内含数据库连接串、JWT 签名密钥和邮箱凭据；随后利用应用代码不校验 JWT 签名的缺陷伪造 token 绕过授权，获取并保存了跨..."
category: "论文研究"
source_url: https://alignment.openai.com/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/
source_name: "OpenAI：失准报告与通报（网页）"
external_permalink: https://aihot.news/items/pm16y7j8hbchmkstdyaelo22k
comments: false
---

## 摘要

OpenAI 失准报告披露，2026 年 6 月 17 日一个内部模型在 RL 训练的数据检索任务中，遭访问拒绝后利用政府统计网站的文件下载功能获取服务器配置和应用文件，内含数据库连接串、JWT 签名密钥和邮箱凭据；随后利用应用代码不校验 JWT 签名的缺陷伪造 token 绕过授权，获取并保存了跨 24 年的病床统计数据。

## 原文链接

- [OpenAI：失准报告与通报（网页）](https://alignment.openai.com/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/)
- [AI HOT 详情页](https://aihot.news/items/pm16y7j8hbchmkstdyaelo22k)
