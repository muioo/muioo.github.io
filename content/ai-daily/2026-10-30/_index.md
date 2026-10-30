---
title: "AI日报 | 2026-10-30"
date: 2026-10-30T08:30:00+08:00
description: "2026-10-30 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Mistral Large 4（Le Chonk）登陆 Hugging Face：1T 参数 MoE 多模态开源权重模型](./01-mistral-large-le-chonk-hugging-face-1t-m/)

Hugging Face 发布 Mistral Large 4（Le Chonk）的上线博客，模型为多模态多语言 MoE 架构，总参数约 1T、激活 49B、上下文窗口 1M token。

### 2. [Pika 基于MiniMax H3后训练并开源 Pika H3 Flex 视频生成模型](./02-pika-minimax-h3-pika-h3-flex/)

Pika Labs 在 MiniMax H3 上做后训练，推出并开源 Pika H3 Flex，采样步数从 50 步压缩到 6 步，生成时间大幅降低且质量有所提升。


## 产品发布/更新

### 3. [Codex 宣布即日起 Pro 及 Business Premium 各档位用量上限翻倍](./03-codex-pro-business-premium/)

Tibo 宣布即日起将 Pro 100/200/500 档位与 Business Premium 的所有用量上限翻倍。Pro 200 的上限不会下调，Work 与 Codex 用量保持不变；dots 的扩展用量上限继续提供，且仍与默认用量分开计算，后续还会通过更好的模型和效率改进提升实际可用量。

### 4. [Factory 发布 Droid 1.0，以程序化工具调用构建企业级 Agent harness](./04-factory-droid-agent-harness/)

Factory 发布 Droid 1.0，一个模型无关的 agent harness，主打程序化工具调用（PTC），模型通过编写 JavaScript 程序在沙箱中一次执行数百个工具调用。

### 5. [OpenRouter 重建默认路由算法：TTFT 降 16.9%、429 错误减少 67%](./05-openrouter-ttft-16-429-67/)

OpenRouter 宣布重建默认 provider 路由算法，从只按价格排序改为按 Routing Cost 综合 effective price、TTFT、吞吐、错误率和输出质量选路。


## 行业动态

### 6. [纽约时报称中国情报人员瞄准英伟达 CEO 黄仁勋](./06-ceo/)

据《纽约时报》报道，美国情报机构认为英伟达 CEO 黄仁勋身边一名高管为中国提供情报，此人是新加坡数据中心运营商 Megaspeed 的 Alice Huang（黄乐）。

### 7. [Reddit 宣布转向以登录为主的体验，以应对 AI 搜索带来的流量下滑](./07-reddit-ai/)

Reddit 在 Q3 财报中宣布将转向以登录为主的体验，以保护数据免受 AI 抓取并提升广告变现。10 月搜索流量平均每周减少超 100 万次引荐，Q3 全球日活为 1.303 亿，其中美国日活降至 5070 万，同比降 2%。Q3 收入同比增长 53% 至 8.95 亿美元，净利润 2.83 亿...

### 8. [Google 三季度搜索增速不及预期，投资者担忧 AI 搜索变现拖累核心业务](./08-google-ai/)

Google 三季度搜索收入增长约 12%，低于分析师预期的 15%，市值一度缩水最多 10%。高管 Philipp Schindler 承认 AI mode 查询的强劲增长因变现率较低产生了影响，同时公司称搜索查询年增速达五年来最高，并计划在美国及国际市场扩大聊天机器人广告项目。

### 9. [404 Media 起底 Proton 内部 AI 转型之争：CEO Andy Yen 强推 AI 引发恐惧文化](./09-404-media-proton-ai-ceo-andy-yen-ai/)

404 Media 采访九名现任与离职 Proton 员工并查阅内部文件，报道 CEO Andy Yen 强推 AI 转型引发的内部冲突。10 月公司 90% 代码由 AI 编写，多使用 Anthropic 的 Claude；Yen 称今年是最后一年招聘工程师，并宣布将以可能决定去留的重新面试评估员...


## 论文研究

### 10. [OpenAI 详解如何检测前沿模型失准行为](./10-openai/)

OpenAI 发布长文，详解其针对前沿模型失准行为的多层监测系统，包括激活探针、基于模型的审查、调查智能体和自动化调查四层架构，并对 GPT‑6 Astra 及以上模型的全部 RL 运行、评估和内部 Codex 流量进行监测。

### 11. [Trakkr 研究：追踪 1285 条 AI 引用统计的溯源路径](./11-trakkr-1285-ai/)

Trakkr Research 向 ChatGPT、Perplexity、Gemini、Claude 和 Google AI Overviews 提出 200 个要求数字的问题，并追踪其中 1285 条统计的引用链路，结果只有 40% 到达说法一致的研究，8% 到达但数字或语境已变，40% 无法核查...


## 技巧与观点

### 12. [OpenRouter 教程：用 LLM 从 PDF 中抽取表格](./12-openrouter-llm-pdf/)

OpenRouter 发布教程，讲解如何把 PDF 以文件形式连同严格 JSON schema 发给能读文件的模型，让表格以带类型的行返回，括号亏损、千分位和脚注标记等清理都写进字段描述。
