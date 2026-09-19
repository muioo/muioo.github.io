---
title: "逆向分析指 ZCode 登录后静默打包 Git 历史并加密上传至 Aliyun OSS"
date: 2026-09-19T08:30:00+08:00
description: "开发者 ferstar 逆向 Z.ai 的 AI 编程桌面应用 ZCode，发现其登录后会静默把整个工作区打包（含完整 .git 历史、LFS 缓存、reflogs 和全局配置）加密上传至 Aliyun OSS，实测一次快照为 42,411 个文件、313MB，且 .git 目录占载荷的 86.6%..."
category: "技巧与观点"
source_url: https://tokenstead.ai/guides/zcode-silent-git-history-upload
source_name: "Hacker News：AI 热帖"
external_permalink: https://aihot.news/items/cmu6y9sjz0jbyrowkh7tus28l
comments: false
---

## 摘要

开发者 ferstar 逆向 Z.ai 的 AI 编程桌面应用 ZCode，发现其登录后会静默把整个工作区打包（含完整 .git 历史、LFS 缓存、reflogs 和全局配置）加密上传至 Aliyun OSS，实测一次快照为 42,411 个文件、313MB，且 .git 目录占载荷的 86.6%。

## 原文链接

- [Hacker News：AI 热帖](https://tokenstead.ai/guides/zcode-silent-git-history-upload)
- [AI HOT 详情页](https://aihot.news/items/cmu6y9sjz0jbyrowkh7tus28l)
