---
title: "AI日报 | 2026-08-25"
date: 2026-08-25T08:30:00+08:00
description: "2026-08-25 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [GPT-5.6 登陆 Kiro，为开发者提升性价比](./01-gpt-5-kiro/)

GPT-5.6 模型家族现已登陆软件开发智能体 Kiro，包含 Sol、Terra 和 Luna 三款模型。在 Terminal-Bench 2.1 测试中，GPT-5.6 Terra 在 Kiro 内完成任务成本降低约 82%。该更新由 OpenAI 与 AWS 合作优化，旨在以更少迭代和更高 t...


## 产品发布/更新

### 2. [NVIDIA Vera Rubin NVL72 树立 AI 智能体效率新标准：每瓦特工作量提升至 30 倍](./02-nvidia-vera-rubin-nvl72-ai-30/)

NVIDIA 实测数据显示，Vera Rubin NVL72 在智能体工作负载下每兆瓦吞吐量较 GB300 NVL72 最高提升 30 倍，每百万 token 成本降低至 35 倍。

### 3. [MetaRoCE：为 AI 规模以太网打造的全新 RDMA 传输协议](./03-metaroce-ai-rdma/)

Meta 设计并开源了 MetaRoCE，一个专为 AI 工作负载在通用以太网上打造的 RDMA 传输协议，已通过 Open Compute Project（OCP）发布规范、参考软件实现和合规测试套件。该协议将智能移至端点，原生支持乱序交付、多路径、无损容忍和双向拥塞控制，无需 PFC，可在百万 ...

### 4. [NVIDIA 如何用 NVLink Fusion 让定制 XPU 融入世界级 AI 工厂](./04-nvidia-nvlink-fusion-xpu-ai/)

NVIDIA 推出 NVLink Fusion，将定制 XPU 接入其 NVLink 扩展域，使 XPU 间端到端延迟比基于现成以太网的方案低 3 倍、数据包速率高 10 倍。

### 5. [MTIA 300：Meta 首款内置 NIC 与通信卸载引擎的训练芯片](./05-mtia-300-meta-nic/)

Meta 发布 MTIA 300，这是其自研加速器家族中首款针对推荐与排序模型训练优化的芯片。芯片封装内集成 12 个 800 Gbps RDMA NIC，提供 1.2 TB/s 总 I/O 带宽，并通过 16 个专用消息引擎卸载通信，使大规模 GEMM 与集合通信并发时计算吞吐损耗低于 0.5%。

### 6. [NVIDIA 扩展 Vera Rubin 推理能力，Groq 3 LPX 全面投产支持智能体系统](./06-nvidia-vera-rubin-groq-lpx/)

NVIDIA 宣布 Vera Rubin NVL72 扩展快速 token 生成能力，以支持智能体系统。其机架级系统 NVIDIA Groq 3 LPX 已全面投产，旨在通过 AI 工厂各层协同工作来定义下一代 AI 推理，而非依赖单一芯片、网络或系统的突破。


## 行业动态

### 7. [Mistral 与 HUMAIN 达成战略合作，推进沙特及中东主权 AI](./07-mistral-humain-ai/)

Mistral 与 HUMAIN 宣布达成战略合作，覆盖 AI 基础设施、先进模型开发及 AI 解决方案部署，聚焦沙特阿拉伯及更广泛地区。双方将合作开发本地化 AI 模型，初期重点包括网络安全和语音，并计划开发在阿拉伯语上表现强劲的前沿模型。该合作金额达数亿欧元，Mistral 将探索使用 HUMA...

### 8. [丰田北美如何用 Deep Agents 和 LangSmith 规模化企业 AI](./08-deep-agents-langsmith-ai/)

丰田北美借助 Deep Agents 和 LangSmith 运行 50 多个生产环境 AI 智能体，将交付周期从 6 个月缩短至 4 天。文章展示了其如何通过 LangSmith 追踪 AI 投资回报率（ROI），并以此支撑企业级 AI 的规模化落地。


## 论文研究

### 9. [Beyond Visual CoT：Internalized Visual Thinking 实现主动视频推理](./09-beyond-visual-cot-internalized-visual-th/)

多模态大语言模型常用视觉思维链（Visual CoT）进行空间、时间与具身环境推理，但生成中间推理图像带来大量推理开销。新提出的后训练框架 Internalized Visual Thinking（IVT）在训练阶段内化视觉思考，推理时直接进行文本预测与优化，从而在不增加推理成本的前提下实现主动视频...


## 技巧与观点

### 10. [OpenAI 正为一切构建 AI 智能体，但用户会愿意交出控制权吗？](./10-openai-ai/)

OpenAI 推出 ChatGPT Work，将 Codex 改造为面向非工程师的智能体产品，最低订阅档每月 20 美元即可使用，旨在让白领通过 LLM 自主完成多步骤工作。OpenAI 内部 6 月有 98% 员工使用 Codex，但组织订阅者仅 17%、个人订阅者不足 1%。公司正通过简化界面扩...

### 11. [ADK 如何评估实时语音智能体](./11-adk/)

Google 为 ADK 带来原生实时评估能力，可用模拟用户以音频驱动实时语音智能体、对语音回复打分，并在与文本智能体相同的评估循环中完成。示例采用三个基于 gemini-live-2.5-flash-native-audio 的智能体组成工作流，支持对话场景与固定对话两种测试用例，内置 NOVIC...

### 12. [Databricks 如何从本地 IDE 运行、调试和扩展工作负载](./12-databricks-ide/)

Databricks 工作区专为数据分析和数据工程而构建，现支持从本地 IDE 直接运行、调试和扩展工作负载。该功能旨在弥合本地开发环境与云端 Databricks 平台之间的差距，让开发者无需切换上下文即可完成编码、测试和部署。

### 13. [你的alt文本能通过自动化检查，不代表它真的合格](./13-alt/)

WebAIM Million报告显示，主流网页中16.2%的图片缺少alt文本，另有10.8%的alt文本模糊或重复。GitHub为Accessibility Scanner构建了alt文本插件，采用五条确定性规则检测缺失、文件名、占位符、泛化词及相邻重复，并引入基于布局的重复检测和可选视觉模型审查...

### 14. [Anthropic 市场人员如何用 Claude Code 每周为每位销售代表发送个性化更新](./14-anthropic-claude-code/)

Anthropic 市场团队成员 Adam Ward 分享如何用 Claude Code 将每周销售报告转化为每位客户经理的个性化周一简报。他通过 MCP 连接 BigQuery 和 CRM 数据，并依据销售与经理反馈迭代提示词，加入“绝不编造 URL”等九条内容规则。该简报现已推广至所有销售团队，...
