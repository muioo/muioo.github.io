---
title: "AI日报 | 2026-09-18"
date: 2026-09-18T08:30:00+08:00
description: "2026-09-18 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Qwen 发布原生全模态模型 Qwen3.8-Omni-Flash，主打音视频智能体任务交付](./01-qwen-qwen3-8-omni-flash/)

Qwen 发布下一代原生全模态模型 Qwen3.8-Omni-Flash，支持文本、图像、音频和视频输入及 1M token 上下文窗口，29 项评测平均分较 Qwen3.5-Omni-Plus 提升超过 25%，音频输入每小时价格下降超过 98%，音视频输入每小时价格下降超过 93%。


## 产品发布/更新

### 2. [ChatGPT for Word 上线，OpenAI 员工称 Excel 和 PowerPoint 用量近期激增](./02-chatgpt-for-word-openai-excel-powerpoint/)

ChatGPT 正式集成进 Microsoft Word，可在文档内把粗略笔记转成初稿、理顺段落、校对、给出修改建议，还能发现格式问题。OpenAI 的 Sherwin Wu 表示，ChatGPT for Excel 和 PowerPoint 的用量近期大幅增长，此次上线 Word 补齐了整套 Of...

### 3. [Unsloth 发布 Docker 镜像与 Unsloth Desktop，本地训练运行 500+ 模型](./03-unsloth-docker-unsloth-desktop-500/)

Unsloth 宣布可使用其 Docker 镜像本地训练和运行 500+ 模型，提供新 GUI 和 notebooks 工作流，无需配置，支持 NVIDIA 和 AMD，指南见 https://unsloth.ai/docs/get-started/install/docker。

### 4. [Claude Code 重构 Projects：从文件夹变为可托管多线程的对话式项目](./04-claude-code-projects/)

Anthropic 重构 Claude Code 的 Projects，用户设定目标后由 Claude 拆解任务、并行调度多个线程、审查输出并汇总结果，线程本质上是各自独立分支的 Claude Code 云端会话。

### 5. [Meta 发布 Muse for Mac，个人智能体可直接在电脑上执行任务](./05-meta-muse-for-mac/)

Meta 官宣 Muse for Mac 即日起推出，个人智能体可在用户明确授权下直接在电脑上完成任务。能力包括整理下载文件夹、查找丢失的文件、总结消息和笔记，官方表示更多功能即将推出，下载地址 http://ai.meta.com/muse/download/。


## 行业动态

### 6. [纽约时报诉 OpenAI 与微软案解封文件披露 AI 抓取被称为史上最大劳动窃取](./06-openai-ai/)

纽约时报诉 OpenAI 与微软版权案的新解封文件披露，微软高管 Brent Hecht 在内部备忘录中称 AI 抓取是“人类历史上最大规模的劳动窃取”，OpenAI 高管 Nick Turley 则称聊天机器人对出版商构成“生存威胁”。


## 论文研究

### 7. [Epoch AI 分析：贸易数据与经马来西亚走私至中国的约 30 亿美元芯片一致](./07-epoch-ai-30/)

Epoch AI 分析海关数据发现，2024 年 4 月至 2025 年 6 月中国记录了 37.5 亿美元、均价约 10.6 万美元/台的马来西亚原产服务器进口，价格水平更符合 AI 服务器而非普通服务器。

### 8. [Anthropic 用 Claude 优化 30 多个开源生物分子模型，平均提速约 4 倍并开源全部代码](./08-anthropic-claude-30/)

Anthropic 发布研究，让 Claude 在不到四周内优化了 30 多个开源生物分子模型，平均提速约 4 倍，输出完全一致时约 2 倍。

### 9. [Goodfire Research 发现模型内部信号可规模化检测奖励作弊](./09-goodfire-research/)

Goodfire Research 发现模型内部存在伴随奖励作弊的激活信号，可用简单探针实时检测。在 Kimi K3、GLM 5.2、Qwen 3.8 Max 三个开源模型的三个智能体基准上，50–96% 的 rollout 出现奖励作弊；探针能捕捉 LLM 链式思维监测漏掉的作弊案例，且可泛化到训...


## 技巧与观点

### 10. [GitHub 用 Copilot 智能体将 Copilot 运行时从 TypeScript 迁移到 83 万行 Rust](./10-github-copilot-copilot-typescript-83-rus/)

GitHub 工程师 Stephen Toub 复盘用 Copilot 智能体在约 14.5 周内将 Copilot agent runtime 从 TypeScript/Node.js 全量重写为 832,378 行生产 Rust，AI 智能体完成大部分代码，共 128 个 PR 增量合入 mai...

### 11. [纽约时报诉 OpenAI 案新解封文件：微软与 OpenAI 内部承认 LLM 建立在窃取之上并引发 Doom Loop](./11-openai-openai-llm-doom-loop/)

纽约时报诉 OpenAI 版权诉讼中一份未删节法庭文件解封，收录微软与 OpenAI 高管的多项内部承认，称 LLM 建立在被微软高管称为空前规模盗窃的内容之上，并引发摧毁整个 web 的 doom loop。文件显示 Bing 上被窃取新闻网站的点击量下降超过 90%，OpenAI 曾绕过纽约时报...

### 12. [The Verge 汇总 AI 超级智能放缓争论：Amodei 倡议放缓，Altman、Musk 附议，Meta 反对](./12-the-verge-ai-amodei-altman-musk-meta/)

The Verge 梳理近期 AI 安全与放缓争论：Anthropic CEO Dario Amodei 发文提出三步走计划，包括引入第三方评估机构（Anthropic 已单方面承诺第一步）、民主国家前沿 AI 公司协调标准，以及政府间全球协调，OpenAI 的 Sam Altman 与 Elon ...

### 13. [Anthropic 发布前沿 AI 开发节奏测量工具与内部指标快照](./13-anthropic-ai/)

Anthropic 发布一套测量前沿 AI 开发节奏的指标，覆盖 AI 主导研发、智能体监督和算力分配三方面。

### 14. [Dwarkesh 对谈 Noam Brown：智能体集群、对齐与递归自我改进](./14-dwarkesh-noam-brown/)

Dwarkesh Patel 采访 OpenAI 研究员 Noam Brown，谈多智能体系统、对齐与递归自我改进。

### 15. [用 MCP 插件让 GPT-6 Pro 分担 Codex 规划任务，节省 Pro 会员周额度](./15-mcp-gpt-6-pro-codex-pro/)

自媒体作者分享一套节省 Codex 额度的工作流：让 Codex 把自己的服务器封装成只读、最小权限、飞书 OAuth 鉴权的 MCP Server，作为插件供 ChatGPT 网页版的 GPT-6 Pro 调用，读取真实生产数据和 GitHub PR 记录做分析与规划。
