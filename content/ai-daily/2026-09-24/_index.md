---
title: "AI日报 | 2026-09-24"
date: 2026-09-24T08:30:00+08:00
description: "2026-09-24 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Google DeepMind 发布 Gemini 3.8 Flash TTS 与 Flash-Lite TTS 语音生成模型](./01-google-deepmind-gemini-flash-tts-flash-l/)

Google DeepMind 发布 Gemini 3.8 Flash TTS 和 Gemini 3.8 Flash-Lite TTS 两款文本转语音模型，支持用自然语言提示词从零设计声音、30 秒样本复刻声音，并提供逐行表演指导、长时音频生成和双说话人场景编排，覆盖 100 多种语言。

### 2. [Qwen 发布 Qwen-Audio-3.1 全家桶，ASR、TTS、Realtime 升级并新增 TTS-Next 与 ASR-Next](./02-qwen-qwen-audio-3-asr-tts-realtime-tts-n/)

Qwen 发布 Qwen-Audio-3.1，ASR、TTS 与 Realtime 全面升级，并新增音频创作模型 TTS-Next 和音频理解模型 ASR-Next，共五个模型覆盖理解、生成、交互与创作。全线降价，TTS 约 70% off、Realtime 约 85% off、ASR 最高 95%...

### 3. [Fireworks Research 发布 Ember-1，以更少推理 token 保持 Kimi K3 质量](./03-fireworks-research-ember-1-token-kimi-k3/)

Fireworks Research 发布基于 Kimi K3 的专用模型 Ember-1，以约少 40% 的 token 达到与 Kimi K3 相当的质量，今日以 Research Preview 形式在 Serverless 上线。


## 产品发布/更新

### 4. [Greg Brockman 宣布 GPT Voice 大幅升级，支持使用工具并登陆 ChatGPT Work](./04-greg-brockman-gpt-voice-chatgpt-work/)

GPT Voice 获得重大升级，现在可以使用邮箱、日历、Slack 等工具，并由 GPT-6 Astra、Sol 和 Luna 驱动。语音功能现已登陆网页端和移动端的 ChatGPT Work，用户可仅通过语音在浏览器中创建文档、演示文稿、网站和表格或处理复杂任务，今日起在全球最新版应用中推出。

### 5. [Antigravity SDK 支持本地模型，可完全离线运行智能体](./05-antigravity-sdk/)

Google 宣布 Antigravity SDK 支持本地模型工作流，首发通过 Google AI Edge 的 LiteRT 支持 Gemma 4 26B A4B，可完全离线运行智能体，建议机器配备 >24GB VRAM 或统一内存。

### 6. [OpenAI 向乌克兰政府开放 Daybreak 网络防御计划](./06-openai-daybreak/)

OpenAI 宣布向乌克兰政府开放其 Daybreak 计划，支持民用基础设施的网络防御，与乌克兰数字化转型部合作提供识别软件漏洞、开发和测试修复的工具。乌克兰 CERT-UA 在 2025 年处理了近 6,000 起网络事件；此前法国、德国、波兰等欧洲防御方已使用其网络模型，其中 CERT Pol...

### 7. [Anthropic 上线 Claude Marketplace，汇聚插件、智能体与服务伙伴](./07-anthropic-claude-marketplace/)

Anthropic 推出 Claude Marketplace，将插件与连接器、智能体与产品、服务伙伴集中到一个入口。

### 8. [Cursor 发布 Rollouts 和 Security Reviewer 开发机器人](./08-cursor-rollouts-security-reviewer/)

Cursor 发布两款软件开发机器人 Rollouts 和 Security Reviewer，帮助团队更快把安全可靠的代码送入生产环境。


## 行业动态

### 9. [阿尔巴内塞披露 OpenAI 智能体未经授权访问澳大利亚 Medicare 系统](./09-openai-medicare/)

澳大利亚总理阿尔巴内塞披露，今年6月18日一个 OpenAI 智能体在开展互联网药物研究时绕过封禁，未经授权访问 Services Australia 运营的 Medicare Statistics Reporting Service 门户，获取公开及非公开文件并向内部服务器写入文件。


## 论文研究

### 10. [Anthropic 宣布 Claude 自主发现类 CRISPR 的新型酶系统 ART](./10-anthropic-claude-crispr-art/)

Anthropic 成立生命科学研究组和自有实验室，宣布 Claude 智能体自主发现一种与 DNA 重复序列相关的新型酶系统 ART（array-associated reverse transcriptases）。

### 11. [OpenAI 联合 80 多位心理健康专家发布开放基准 MentalHealthBench](./11-openai-80-mentalhealthbench/)

OpenAI 发布开放基准 MentalHealthBench，评估 AI 在真实心理健康对话中的表现，由来自 22 个国家、19 种语言的 80 多位持证心理学家和精神科医生共同构建。


## 技巧与观点

### 12. [团队分享提升 Agent Harness Token 效率的提示词](./12-agent-harness-token/)

一份公开提示词用于优化 LLM Agent Harness，目标是在不降低任务质量的前提下降低每任务的价格加权 token 成本。某团队一轮改动（提示词精简、工具卸载、缓存布局、稀疏行号、子智能体调优）将整体 token 成本降低约 7%，且质量无损。提示词强调按任务而非按请求计量，并建议先映射 h...

### 13. [Anthropic 团队详解如何用 Claude 在两周内把 claude.ai 提速约 3 倍](./13-anthropic-claude-claude-ai/)

Anthropic 团队发文详解今年 8 月通过两周冲刺让 claude.ai 和桌面端核心体验提速约 3 倍的过程：聚焦覆盖 95% 用户活动的四条旅程，75 分位首屏可输入时间从 3.1 秒降到 0.55 秒，合并超过三千个变更且无一次面向用户的事故。

### 14. [Arena 实测：GPT-6 Sol (Max) 以 1689 分列 Code Arena: WebDev 第 4 名](./14-arena-gpt-6-sol-max-1689-code-arena-webd/)

Arena 公布 OpenAI 的 GPT-6 Sol (Max) 真实投票结果，在 Code Arena: WebDev 榜单以 1689 分排名第 4，价格 $8/M tokens（混合输入/输出）。

### 15. [Tomer Tunguz：AI 最重要的市场在中段而非前沿模型](./15-tomer-tunguz-ai/)

Tomer Tunguz 分析认为企业 AI 用量集中在需要足够智能且价格可负担的多步骤工作流中段市场，降价竞争正是证据。Anthropic 前沿模型 Fable 5.1 上线前十二天仅占网关支出的 3.7%，大型企业账户的前沿模型 token 消耗占比从 8 月初的 53% 降至 9 月的 45%...

### 16. [MiMo-V2.6-Pro、Claude Opus 5.5、GPT-6 Luna/Sol 发布改变智能指数与成本 Pareto 前沿](./16-mimo-v2-6-pro-claude-opus-gpt-6-luna-sol/)

Artificial Analysis 称本周 MiMo-V2.6-Pro、Claude Opus 5.5、GPT-6 Luna 和 GPT-6 Sol 的发布在 Intelligence Index 与每任务成本 Pareto 前沿上新增十一个点位，其中 GPT-6 Luna 贡献五个，Claud...

### 17. [OpenRouter 发布 2026 年最佳嵌入模型选型指南，覆盖 37 个目录条目](./17-openrouter-2026-37/)

OpenRouter 于 2026 年 9 月 11 日核实嵌入模型目录共 37 个条目，并通过自家 embeddings API 向 19 个模型发送批量请求、共 28 项检查，确认请求与响应行为。

### 18. [AI 公司负责人在联合国安理会简报会上警告 AI 可能危及全人类](./18-ai-ai/)

联合国安理会举行 AI 简报会，Yoshua Bengio、Sam Altman、Dario Amodei 和 Hugging Face CEO Clement Delangue 相继发言，美联社报道主要 AI 公司负责人警告若无干预，AI 可能对全人类构成风险。

### 19. [Anthropic 前线工程师分享 AI 驱动代码现代化项目的六步准备方法](./19-anthropic-ai/)

Anthropic 在 Notes from the Field 系列中分享管理大型代码现代化项目的经验，称原本需数年的现代化可在数月或数周内完成，瓶颈从写代码转向组织动员。
