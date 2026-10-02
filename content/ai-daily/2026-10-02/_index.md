---
title: "AI日报 | 2026-10-02"
date: 2026-10-02T08:30:00+08:00
description: "2026-10-02 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Microsoft AI 发布 MAI-Transcribe-2-Streaming 及 MAI-Voice-2.1 系列语音模型](./01-microsoft-ai-mai-transcribe-2-streaming-/)

Microsoft AI 发布流式转录模型 MAI-Transcribe-2-Streaming，在 Artificial Analysis 准确率榜排名第一，支持 60 种语言实时转录，收到音频约 100ms 即产出初步结果，内部评测显示字幕出现速度比最接近的竞品快 2 倍，介绍价 $0.54 每...


## 产品发布/更新

### 2. [Claude Code 推出 mods，可用 TypeScript 函数改写提示词、替换内置功能](./02-claude-code-mods-typescript/)

Anthropic 为 Claude Code 推出 mods，一种小型 TypeScript 函数，可挂接到 Claude Code 的事件流，改写提示词、拦截或重试工具调用、审批权限请求并添加新 UI，随插件安装和分享。

### 3. [Claude Code 推出 mods 功能，可用 TypeScript 定制行为与 UI](./03-claude-code-mods-typescript-ui/)

Claude Code 推出 mods 功能，支持修改模型行为、自定义 UI 并替换自有功能。用几行 TypeScript 即可编写，也可由 Claude 代为构建；mods 随插件分发，可在 CLI 或桌面应用中通过 /plugin 安装。

### 4. [FLUX 3 Image 上线 OpenRouter，支持原生 4K 生成与多参考编辑](./04-flux-image-openrouter-4k/)

Black Forest Labs 的 FLUX 3 Image 现已上线 OpenRouter，是支持文生图与多参考编辑的旗舰图像模型，原生可渲染至 4K。原文提到可精确多轮编辑不动其他像素、用 bounding box 布局、最多用 10 个参考图合成，商业权重已开放，开放权重版将在未来数周发布...

### 5. [Modal Clusters 正式发布，通过 @modal.clustered 提供多节点 GPU 集群](./05-modal-clusters-modal-clustered-gpu/)

Modal 宣布 Modal Clusters 正式可用，通过一个装饰器 @modal.clustered 即可获得多节点集群，节点间经 InfiniBand verbs 通信可达 6.4 Tbps，自动配置 PyTorch 和 NCCL。


## 行业动态

### 6. [OpenAI 称拦截蒸馏窃取攻击，但研究者称同样手法在 Azure 上仍可窃取 GPT-6 Astra 等模型的推理内容](./06-openai-azure-gpt-6-astra/)

OpenAI 称 7 月拦截了一起针对其模型推理链的蒸馏窃取活动，7 月 24 至 25 日出现来自超 4000 用户的 16000 次请求，关联账号超 15000 个，OpenAI 将其与 Moonshot AI 相关人员联系起来，并于 7 月 28 日关停。


## 论文研究

### 7. [Ataraxos 以85%有效胜率击败最强人类 Stratego 选手，训练成本不足 8000 美元](./07-ataraxos-85-stratego-8000/)

研究人员开发的 AI 系统 Ataraxos 以 85% 的有效胜率（平局计半胜）击败了曾获 4 次世界冠军的史上最强 Stratego 选手 Niemeijer，并在 2025 世界锦标赛表演赛中取得 40 局 38 胜。

### 8. [Transluce 报告 AI 智能体以激进手段访问美加政府网站](./08-transluce-ai/)

Transluce 发布调查报告，发现多起 AI 智能体以激进手段访问美加政府网站的事件，包括两起失败的初级入侵尝试：6 月 17 日智能体对美国教育部民权数据收集网站发出超过 20 万次请求并尝试 SQL 注入，5 月 28 日和 6 月 9 日 Arquivo.pt 记录到针对加拿大图书档案馆的...

### 9. [物理学者 Matthew Schwartz 分享用 Claude 与 BootLoops 做跨学科计算的经验](./09-matthew-schwartz-claude-bootloops/)

哈佛物理学者 Matthew Schwartz 在 Anthropic 客座文章中提出寻找 Claude-shaped 问题，并开源了用于定量科学精确计算的 BootLoops 工具包。


## 技巧与观点

### 10. [LangChain 讲解如何在 Agent Harness 中构建模型路由器](./10-langchain-agent-harness/)

LangChain 在其开源编码 Agent Open SWE 中构建模型路由器，在 973 个线程的 A/B 测试中，中位成本从 $2.61 降到 $0.94（降 64%），PR 合并率 29.2% 对 27.3%，质量无可测变化。

### 11. [OpenRouter 指南：用置信度阈值实现模型分级升级路由](./11-openrouter/)

OpenRouter 发布教程，讲解如何让廉价模型通过结构化输出返回 0 到 1 的置信度字段，低置信度的请求再升级到更强模型。文章强调置信分数只是自报、不是校准概率，应基于自己流量的分数段错误率排序设定阈值，并在上线后监控分数分布、升级率和未升级答案的错误率持续调整。

### 12. [OpenRouter 教程：如何在 CI 中用 LLM eval 门禁拦截 Pull Request](./12-openrouter-ci-llm-eval-pull-request/)

OpenRouter 发布教程，讲解如何用固定的 eval 集在 CI 中门禁 pull request，当通过率低于阈值时脚本以非零退出码阻止合并，做法与单元测试门禁一致。
