---
title: "AI日报 | 2026-10-21"
date: 2026-10-21T08:30:00+08:00
description: "2026-10-21 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Inception Labs 发布扩散大语言模型 Mercury 3，速度达 1068 tokens/秒](./01-inception-labs-mercury-1068-tokens/)

Inception Labs 发布扩散式大语言模型 Mercury 3，称其在多项基准上超过 GPT-6 Luna 和 Claude Haiku 5.5，速度达 1068 tokens/秒，参数量较 Mercury 1 扩大 40 倍以上。


## 产品发布/更新

### 2. [DeepSeek 全面开源内部推理框架 DeepInfer](./02-deepseek-deepinfer/)

DeepSeek 宣布将内部推理框架 DeepInfer 全面开源，并同步开源生产级 Token 编解码组件 deepseek-recipe。

### 3. [Google 与 Meta 发布 TorchTPU：PyTorch 原生 TPU 后端](./03-google-meta-torchtpu-pytorch-tpu/)

Google 与 Meta 发布开源项目 TorchTPU，为 Google TPU 提供原生 PyTorch 后端，模型迁移只需把 .to("cuda") 改为 .to("tpu")。

### 4. [ChatGPT 推出 Locked Chats，可用 PIN 或生物识别锁定敏感对话](./04-chatgpt-locked-chats-pin/)

ChatGPT 推出 Locked Chats 功能，把敏感对话从常规历史记录和搜索中移入受保护空间。用户在网页端和桌面端可用 PIN 解锁，支持的移动设备上可用 PIN、Face ID、Touch ID 或设备解锁；锁定会话中的新消息不会更新常规对话使用的记忆。该功能即日起向 Free、Go、Pl...

### 5. [Google 发布 vLLM 与 SGLang 的 TorchTPU 原生推理引擎](./05-google-vllm-sglang-torchtpu/)

Google 在 PyTorch 相关公告中推出基于 TorchTPU 的 vLLM 和 SGLang 原生 PyTorch 推理引擎，分别与 Inferact、RadixArk 合作开发，让开发者用熟悉的 PyTorch 工具在 TPU 上部署模型。


## 行业动态

### 6. [路透：OpenAI 拟在 Anthropic 上市前加速融资约 300 亿美元，估值超 1.4 万亿美元](./06-openai-anthropic-300/)

据 Reuters 报道，OpenAI 正赶在 Anthropic 上市前洽谈融资约 300 亿美元，估值超 1.4 万亿美元，比 3 月的 8520 亿美元至少高 64%。

### 7. [SpaceX 财报显示 AI 业务超预期，占收入 52%](./07-spacex-ai-52/)

SpaceX 发布第三季度监管文件，披露营收 146 亿美元、净利润 44 亿美元，扭转去年同期 10 亿美元亏损。其更名的“Super Intelligence”业务线（含 Cursor、Grok 和 neocloud 算力业务）表现好于投资者预期，AI 目前占公司收入 52%，算力规模达 1.7...

### 8. [美国陆军网络司令部 ECHOTRIBBLE 项目拟将 AI 智能体变成自主扩散的网络武器](./08-echotribble-ai/)

据 The Intercept 获取的文件，美国陆军网络司令部（ARCYBER）正在开发代号 ECHOTRIBBLE 的平台，让 AI 智能体自主在网络间移动、识别并清除威胁目标，之后自毁，且须在极少人工监督下运行。

### 9. [Redact 调查：WhatsApp 帮助页面隐藏 LLM 指令，让 AI 不推荐监管机构、不提 GDPR](./09-redact-whatsapp-llm-ai-gdpr/)

Redact 发现 WhatsApp 帮助中心页面向 LLM 发送用户看不到的隐藏指令，指示其支持聊天机器人不推荐数据保护监管机构，并在用户提到律师或法律行动后不引用 GDPR、LGPD 或 CCPA。

### 10. [OpenAI 收购药物研发平台 Orchestra Bio 并入 Rosalind 生命科学体系](./10-openai-orchestra-bio-rosalind/)

OpenAI 宣布收购 Orchestra Bio，一个帮助生物制药团队协调药物研发复杂流程的平台，其团队和技术将与 Rosalind 整合。Orchestra 的智能体可帮助团队追踪研究和项目进展，分析如生产批次失败对临床试验时间线的影响并提出应对方案。文中还提到与 Novo Nordisk 和 ...

### 11. [Anthropic 云合作生变：AWS、Google、微软视其为竞争者](./11-anthropic-aws-google/)

据泄露给华尔街日报的 S-1 文件，Anthropic 难以从 AWS、Google 和 Microsoft 获得足够云算力，这些厂商日益将其视为竞争者而非客户。


## 论文研究

### 12. [Anthropic 用 Claude 设计出针对蝎子神经毒素的蛋白质迷你结合剂](./12-anthropic-claude/)

Anthropic 让内部研究模型在 Claude Science 中主要自主运行 64 小时，设计针对五种蝎子神经毒素的蛋白质迷你结合剂，共生成 318,484 个设计、筛选出 180 个。
