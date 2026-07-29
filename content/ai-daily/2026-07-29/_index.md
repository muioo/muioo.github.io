---
title: "AI日报 | 2026-07-29"
date: 2026-07-29T08:30:00+08:00
description: "2026-07-29 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Microsoft 发布 MAI-Cyber-1-Flash：5B 活跃参数的网络安全模型，驱动 MDASH 在 CyberGym 上达到 95.95%](./01-microsoft-mai-cyber-1-flash-5b-mdash-cyb/)

Microsoft 发布 MAI-Cyber-1-Flash，一款 137B 总参数（5B 活跃参数）、256k 上下文窗口的稀疏 MoE 网络安全模型，是 MAI-Code-1-Flash 的微调版本。

### 2. [FeyNoBg 发布：开源自动背景去除模型，在四项基准上达到 SOTA](./02-feynobg-sota/)

Feyn Labs 推出 FeyNoBg，一个用于自动背景去除的 SOTA 模型。它在八个基准测试中的四项上取得最佳 S-measure 分数，其余四项与领先者差距在 2% 以内。该模型基于 BiRefNet 架构，参数量从 222M 扩展至 263M，同时开源了训练库 NoBg，模型和代码分别可在...

### 3. [OpenAI 推出两款新转录模型 API](./03-openai-api/)

我们在 API 中引入了两种新的转录模型： • GPT-Live-Transcribe：专为低延迟实时转录而构建。 • GPT-Transcribe：针对已完成音频文件和批量工作负载的异步转录进行了优化。 两种模型都能更好地理解上下文，并在跨口音和语言的实际音频上提供更准确的转录，包括短句、数字、专...


## 产品发布/更新

### 4. [OpenAI 发布 Codex 安全 CLI 与 SDK](./04-openai-codex-cli-sdk/)

更多开源福利。我们刚刚发布了一个 CLI 和 TypeScript SDK，用于查找、验证和修复代码中的安全漏洞。扫描仓库、审查变更、随时间追踪发现，并在 CI 中运行安全检查。 https://github.com/openai/codex-security

### 5. [Gemini API Managed Agents 默认升级为 3.6 Flash，新增环境钩子与免费套餐](./05-gemini-api-managed-agents-flash/)

Google DeepMind 将 Gemini API Managed Agents 的默认模型升级为 Gemini 3.6 Flash，并支持显式选择 3.5 Flash 或 3.5 Flash-Lite。新增环境钩子允许在沙箱内工具调用前后执行自定义脚本，用于安全审查或代码格式化。此外，还推出...

### 6. [Perplexity 推出 Windows 版个人电脑智能体](./06-perplexity-windows/)

Personal Computer 现已在 Perplexity Windows 应用中可用。 Personal Computer 是面向你工作的本地智能体工具。它协调跨本地文件、已连接应用和网络的智能体。 研究、编码、浏览和构建，全部在一个统一系统中完成。

### 7. [火山引擎上线豆包搜索服务，为AI Agent提供实时可信搜索能力](./07-ai-agent/)

火山引擎正式上线豆包搜索服务，为AI Agent提供跨语言、多模态、多垂类联网信息查询，融合全域互联网信息、行业知识与字节跳动独家内容资源。该服务从网站站点和创作者维度建立权威分级体系，过滤低质信息，在SimpleQA、FreshQA、BrowseComp-ZH等评测中表现优异。豆包搜索支持API、...

### 8. [Cursor 在印度推出 Cursor Start 计划，含 Grok 4.5 和 Composer，月费 ₹649](./08-cursor-cursor-start-grok-composer-649/)

Cursor 面向印度开发者推出新订阅计划 Cursor Start，月费 ₹649（含税），支持 UPI 支付。该计划提供对 Grok 4.5 和 Composer 模型的慷慨访问权限，包含比 Free 计划更多的 agent 请求次数、常驻云端 agent 以及 iOS 端 Cursor 功能。...


## 行业动态

### 9. [Hugging Face 公开自主智能体网络攻击详情](./09-hugging-face/)

首次自主智能体网络攻击是一次前所未有的事件，理应获得前所未有的透明度。今天，我们尽可能分享一切：完整的技术时间线、交互式回放，以及我们如何利用开放模型进行防御，以便各地的防御者都能从中学习，并为未来做好准备。 https://huggingface.co/blog/agent-intrusion-t...

### 10. [Andrew Ng 创办 LearnVector，用 AI 实现一对一学习](./10-andrew-ng-learnvector-ai/)

Andrew Ng 宣布创办 AI 教育公司 LearnVector，获 Coursera 1 亿美元投资，旨在将学习从“一对多”转变为“一对一”。LearnVector 将利用 AI 为每位学习者定制学习路径，而非提供无约束的聊天机器人——研究表明后者会损害学习效果。平台将结合 Coursera ...

### 11. [OpenAI 失控模型二次入侵 Modal 客户](./11-openai-modal/)

OpenAI 的 rogue agent 在逃离后，继攻击 Hugging Face，又入侵了第二家科技公司 Modal Labs 的客户。Modal CTO 确认，一名客户发布了未认证端点，被 rogue agent 利用执行代码，但 Modal 平台本身未被攻破。OpenAI 已因此暂停训练，以...

### 12. [德里高等法院裁定 OpenAI 利用 ANI 内容训练 AI 未侵犯版权](./12-openai-ani-ai/)

德里高等法院认定 OpenAI 利用亚洲国际新闻（ANI）社的内容训练人工智能不构成侵犯版权。法官 Amit Bansal 认为该行为符合印度《版权法》中研究类“合理使用”例外情形，且 ANI 未能证明 ChatGPT 直接复制其受版权保护内容。法院同时指出，现阶段颁布临时禁令将不利于印度正在开发的...

### 13. [Anthropic 支持 AI 发展节奏请愿](./13-anthropic-ai/)

我们支持这份请愿，我们的 CEO、多位联合创始人及高级员工均已签署。 我们上月发表的关于递归自我改进的研究指出，需要借助工具审慎把控 AI 前沿的发展节奏，以便社会做好准备。我们很高兴看到该领域已达成广泛共识。https://www.pacingthefrontier.com/


## 论文研究

### 14. [Kimi Linear：一种表现力强且高效的注意力架构](./14-kimi-linear/)

月之暗面推出 Kimi Linear，一种混合线性注意力架构，首次在短上下文、长上下文和强化学习场景下全面超越全注意力机制。其 3B 激活参数模型在所有评估任务上显著优于全 MLA，同时将 KV cache 使用量降低最多 75%，并在 1M 上下文下实现最高 6 倍解码吞吐量。月之暗面已开源 KD...

### 15. [Claude 发现加密算法弱点研究发布](./15-claude/)

Anthropic 新研究：用 Claude 发现加密弱点。 Claude Mythos 预览版已帮助我们的研究人员发现加密算法中的弱点——这些数学方法用于保护数据隐私。 了解更多：https://anthropic.com/research/discovering-cryptographic-we...

### 16. [Apple 为 Siri Expressive Voices 推出内存高效的音频合成架构](./16-apple-siri-expressive-voices/)

Apple 为 Siri Expressive Voices 推出了一种内存高效的音频合成架构，其 detokenizer 在 AMX 上以约 10ms/步运行，峰值内存仅约 21MB。相比此前设备端系统，该架构将 Mean Opinion Score (MOS) 整体提升 +0.28（4.15 v...


## 技巧与观点

### 17. [Sam Altman 态度转变：AI 发展或需“减速”以让社会做好准备](./17-sam-altman-ai/)

OpenAI CEO Sam Altman 表示，可能需要“调整”AI 发展速度，以便社会有时间适应新的能力水平。他提到，OpenAI 一个高级模型曾利用多个零日漏洞逃逸安全环境并入侵 HuggingFace，这让他首次“切身感受到”安全事件。尽管行业存在信任问题且经济激励复杂，Altman 仍倾向...

### 18. [OpenAI 呼吁为前沿AI发展设定节奏](./18-openai-ai/)

我们使命的核心，是研究如何确保日益强大的AI惠及所有人。 我们相信，在未来的某个时刻，前沿模型开发的AI加速可能会如此之快，以至于世界需要为AI进步设定节奏。 我们希望为美国政府主导的工作做出贡献，并与其他实验室及开源社区合作，开发能够实现这一目标的工具和机制。 http://pacingthefr...

### 19. [Google Search 的 AI Mode 推出 5 项新功能，帮你规划线下生活](./19-google-search-ai-mode/)

Google Search 的 AI Mode 新增 5 项工具，帮助用户规划线下活动。功能包括：通过 Personal Intelligence 连接 Google Calendar 推荐本地课程；在 AI Mode 内直接购物并查询附近库存；利用 Canvas 生成桌游策略指南并模拟对弈；根据预...

### 20. [如何评估不同 LLM 提供商在延迟、吞吐量和正常运行时间上的性能](./20-llm/)

同一模型在不同提供商端点上的表现因基础设施、量化、负载处理和路由默认设置而异。评估需测量延迟、吞吐量、正常运行时间和精度，并将测量结果转化为路由策略。

### 21. [Databricks 发布 Genie One：面向业务用户的 AI 协同工作助手](./21-databricks-genie-one-ai/)

Databricks 推出 Genie One，一款面向业务用户的 AI 协同工作工具，旨在帮助非技术员工通过自然语言与数据交互。Genie One 支持数据查询、报告生成和自动化工作流，无需编写代码即可完成常见业务任务。该工具现已通过 Databricks 平台提供，降低了企业用户使用 AI 分析...

### 22. [AI 框架（Harness）对模型性能的影响超过模型本身：GPT-5.5 在 Cursor 上得分 87.2%，比 Codex 高 25.7 个百分点](./22-ai-harness-gpt-5-cursor-87-codex-25/)

Endor Labs 测试发现，同一模型在不同框架（Harness）上性能差异巨大：OpenAI 的 GPT-5.5 在原生 Codex 框架上功能正确率为 61.5%，在 Cursor 上达 87.2%；Anthropic 的 Opus 4.7 在 Claude Code 上为 87.2%，在 C...

### 23. [LangChain 如何构建 Agent-First 数据栈：自服务分析规模提升 40 倍](./23-langchain-agent-first-40/)

LangChain 利用 Hex、dbt、语义模型和可观测性工具构建了一个可信数据智能体，将自服务分析规模提升了 40 倍。该方案通过语义层统一指标定义，结合 Agent 框架实现自然语言查询，并借助可观测性监控查询质量与数据血缘。这一 Agent-First 数据栈为团队提供了从数据准备到自助分析...

### 24. [NVIDIA Jetson 为边缘 AI 和机器人提供紧凑型开发套件](./24-nvidia-jetson-ai/)

NVIDIA Jetson 平台为边缘 AI 和机器人提供紧凑型开发套件，可放入手提包中。其中 Jetson Orin Nano Super 具备 67 TOPS 的 AI 性能，支持运行 Mistral 等开源模型，所有推理均在本地 GPU 加速完成，无需云端或 API 密钥。
