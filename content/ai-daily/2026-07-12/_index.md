---
title: "AI日报 | 2026-07-12"
date: 2026-07-12T08:30:00+08:00
description: "2026-07-12 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [蚂蚁集团 Robbyant 发布 LingBot-VA 2.0，首个原生具身基础模型](./01-robbyant-lingbot-va/)

蚂蚁集团旗下具身智能团队 Robbyant 发布 LingBot-VA 2.0，首个原生具身基础模型。该模型采用因果 DiT 架构，视频专家约 13.0B 参数（约 1.9B 激活），训练规模约 15.3B 参数，推理时每 token 约 2.5B 激活。模型引入多块预测（MCP）实现 2.3 倍训...

### 2. [OpenAI 发布 GPT-5.6 系列医疗评估结果](./02-openai-gpt-5/)

OpenAI 发布 GPT-5.6 系列在医疗领域的评估结果。最小变体 GPT-5.6 Luna 在最低推理强度下即超越最高推理强度的 GPT-5.5，且成本低 25 倍；最大变体 GPT-5.6 Sol 树立新标杆。在涵盖患者端与临床端的多样化任务中，专科医生被要求以无限时间和网络访问权限撰写回答...


## 产品发布/更新

### 3. [Claude Code v2.1.207 发布](./03-claude-code-v2-207/)

Claude Code v2.1.207 发布。Auto 模式在 Bedrock、Vertex AI 和 Foundry 上无需 `CLAUDE_CODE_ENABLE_AUTO_MODE` 即可使用，可通过 `disableAutoMode` 设置关闭。修复了流式响应中包含超长列表、表格、段落或代...


## 行业动态

### 4. [OpenAI GPT-5.6-Sol 删光 AI 创业者 Matt Shumer 的 Mac 硬盘](./04-openai-gpt-5-6-sol-ai-matt-shumer-mac/)

知名 AI 创业者 Matt Shumer 的 Mac 硬盘被 OpenAI 最新 Agent 模型 GPT-5.6-Sol 彻底清空。他在本地 Agent 上开启 Full Access 权限，让 subagent 执行文件清理任务，结果 shell 变量 $HOME 路径解析错误，Agent 直...

### 5. [研究：博科圣地已使用ChatGPT、Claude等主流AI聊天机器人用于袭击策划与武器开发](./05-chatgpt-claude-ai/)

剑桥大学CASP研究员Antonia Jülich对27名前成员的57次访谈显示，博科圣地已使用ChatGPT、Claude、Gemini、Grok、Meta AI和DeepSeek等主流AI聊天机器人，用于袭击策划、制造更强爆炸装置、武器维护及行动安全。该组织两个派系均设立了专门的AI部门。ISI...

### 6. [11天Claude Fable 5写超100万行代码：Rust重构JavaScript运行时Bun](./06-11-claude-fable-100-rust-javascript-bun/)

开发者Jarred Sumner借助Claude Fable 5模型，11天内将Bun从Zig重写为Rust，64个实例并行编写超100万行代码，API费用约16.5万美元。重构主因是Zig频繁内存错误，Rust可在编译时捕获。Bun v1.4.0以Canary版本发布，修复128个错误，速度提高约...

### 7. [彭博社揭秘苹果起诉 OpenAI 内幕：前员工一句“哈哈”成窃密关键](./07-openai/)

苹果起诉 OpenAI，指控前工程师 Chang Liu 离职时带走未归还的 MacBook、一名可分享内情的员工，并利用软件漏洞持续访问苹果内网。他发现漏洞后向同事分享“哈哈，我发现我还能访问网络存储”，后者协助其获取更多机密。苹果称 OpenAI 试图复制 iPhone 产品研发体系，核心从非法...


## 技巧与观点

### 8. [Ghost Font：一种人类能读懂但AI无法识别的反AI字体](./08-ghost-font-ai-ai/)

Ghost Font 是一种利用运动、视频、噪点和诱饵来隐藏文字的反AI字体。用户输入文字后可生成并下载视频片段，视频中的字母由与背景完全相同的点组成，单帧截图无法显示任何信息。该字体生成的视频被传递给Claude Fable和GPT Sol 5.6 Ultra等前沿模型时，这些模型即使具备编程能力...
