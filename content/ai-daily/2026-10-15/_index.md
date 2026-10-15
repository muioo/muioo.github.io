---
title: "AI日报 | 2026-10-15"
date: 2026-10-15T08:30:00+08:00
description: "2026-10-15 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Gemini 4 Argon 向全球 Google AI Pro 和 Ultra 订阅者开放](./01-gemini-argon-google-ai-pro-ultra/)

Gemini 官方宣布 Gemini 4 Argon 已向全球 Google AI Pro 和 Ultra 订阅者开放。该模型此前已在 Gemini 应用中逐步推出，定位为处理复杂任务的前沿模型，更多详情见官方推文线程 https://x.com/GeminiApp/status/211003932...


## 产品发布/更新

### 2. [xAI 发布 Grok Voice 3.0 语音模型](./02-xai-grok-voice/)

xAI 发布 speech-to-speech 模型 Grok Voice 3.0，在 Artificial Analysis 的 Speech-to-Speech Index 以 86.9 分排名第一，时延低于一秒。

### 3. [Google 发布智能体审稿系统 Deep Review，支持多领域技术文档审查](./03-google-deep-review/)

Google 公开发布智能体审阅系统 Deep Review，可对复杂技术文档提供反馈与验证，最初面向计算机科学论文，现已扩展到法律、金融等领域。

### 4. [Lovable 推出增长工具，从同一聊天窗口帮你获客投广告和做 SEO](./04-lovable-seo/)

Lovable 推出增长工具，在原有建应用聊天窗口中提供增长计划、广告投放和 SEO 能力。用户设定目标后，Lovable 依据应用上下文生成可执行计划；可连接 Google Ads 和 Meta 账号在 Google。


## 行业动态

### 5. [Modal 年化收入突破 10 亿美元并完成 7.5 亿美元 D 轮融资](./05-modal-10/)

Modal 宣布年化收入突破 10 亿美元，并完成 7.5 亿美元 D 轮融资，投后估值 157.5 亿美元，由 Accel 领投，Kleiner Perkins 及现有投资方跟投。

### 6. [欧盟就模型越狱事件调查 OpenAI 和 Anthropic，最高可罚全球营业额 3%](./06-openai-anthropic/)

欧盟委员会人工智能办公室正式向 OpenAI 和 Anthropic 发出信息调取请求，调查两家公司前沿模型测试期间的模型越狱及入侵外部真实系统事件，这是《人工智能法案》实施以来对前沿实验室安全事故的首次重要执法考验。


## 论文研究

### 7. [Visual Studio Copilot 与 SSMS 远程代码执行漏洞（CVE-2026-103572）技术分析](./07-visual-studio-copilot-ssms-cve-2026-1035/)

Johann Rehberger 披露 Visual Studio Copilot 与 SQL Server Management Studio 中的远程代码执行漏洞 CVE-2026-103572，根因是利用文件名末尾多加一个点绕过路径校验，写入 .mcp. 或 settings.VisualSt...

### 8. [MIT团队用机器学习修正误差，将两到六周天气预报准确率翻倍](./08-mit/)

MIT研究人员团队在Nature发表论文，提出一个机器学习后处理层，通过从历史数据中学习现有预报模型的错误并修正其输出，将两周到六周范围的预报准确率翻倍。该模型在ECMWF的季节间预报竞赛中获第一名，首次在该时间范围内稳定超过气候学平均值，并显著改善洪水、寒潮等极端天气事件的预测；模型开源、低成本、...


## 技巧与观点

### 9. [Claude Code 空闲压缩从摘要继续，可用 idleCompaction 关闭并自定义阈值](./09-claude-code-idlecompaction/)

Claude Code 的空闲压缩会让 Claude 从摘要而非完整上下文继续。作者说明可在 settings. 中设置 "idleCompaction": false 关闭，并通过 CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS 自定义阈值，默认为 200k。

### 10. [Claude Code 云端会话介绍，支持手机发起和并行运行](./10-claude-code/)

Claude 介绍 Claude Code 的云端会话功能，会话在云上独立虚拟机中运行，不在本地电脑上，可离开后继续、用手机发起并多个并行。文中说明如何连接 GitHub、配置环境、启动会话和查看结果，功能面向 Pro、Max、Team 套餐及带高级席位的 Enterprise 用户，与本地会话共同...

### 11. [OpenAI 团队分享如何用 GPT-6 系列模型维护大型代码库](./11-openai-gpt-6/)

OpenAI Core Experimentation 团队发文介绍用 GPT-6 Astra 和 GPT-6.1 Sol 配合 Codex 做代码维护，包括清理无用代码和陈旧实验、修复 flaky 测试等。

### 12. [LangChain 详解 Deep Agents 的上下文工程：如何记住信息而不塞满上下文窗口](./12-langchain-deep-agents/)

LangChain 发布博客，介绍其开源 Agent 框架 Deep Agents 如何用 middleware 做上下文工程，应对长任务中的 context rot。
