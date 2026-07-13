---
title: "AI日报 | 2026-07-13"
date: 2026-07-13T08:30:00+08:00
description: "2026-07-13 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [腾讯混元发布Hy3模型：295B参数MoE架构，Agent向LLM定位，已集成微信服务10亿+用户](./01-hy3-295b-moe-agent-llm-10/)

腾讯混元团队发布Hy3模型，采用295B总参数、21B激活参数的MoE架构，推理效率可打平参数规模2-5倍的旗舰模型。Hy3定位为Agent向LLM，从preview到正式版基于50多个真实业务反馈迭代，内部WorkBuddy任务成功率从72%提升至90%，耗时降低34%，幻觉和常识错误持续下降。实...


## 产品发布/更新

### 2. [Mesh LLM：在 iroh 上进行分布式人工智能计算](./02-mesh-llm-iroh/)

Mesh LLM 是一个开源项目，能将用户多台机器上的 GPU 和内存池化，对外暴露兼容 OpenAI 的 API。它通过 iroh 网络库实现点对点连接，无需中央服务器。请求可在本地 GPU 运行、路由到已加载模型的节点，或将大模型按层分区（内部称“Skippy”）流水线式拆分到多台机器。系统内置...

### 3. [Codex与ChatGPT Work多项更新：取消5小时限制](./03-codex-chatgpt-work/)

早上好。过去48小时里，Codex和ChatGPT Work非常忙碌！三项重要更新： - 暂时取消所有Plus、Business和Pro计划的5小时使用限制 - 正在推出变更，使GPT 5.6 Sol整体更高效，这将体现在使用量减少上，从而让你能走得更远。具体影响待量化后公布 - 我们已达到600万...

### 4. [Mindwalk：在代码库 3D 地图上回放编码代理会话](./04-mindwalk-3d/)

Mindwalk 是一款可视化工具，可将 Claude Code 和 Codex 的会话日志在代码库的 3D 地图上回放。它将仓库绘制成夜间地图，代理搜索、读取和编辑过的文件会发光，未触及区域保持黑暗，让用户一眼看清代理对任务的理解范围。单个 Go 二进制文件即可运行，所有会话数据完全本地处理，不会...


## 行业动态

### 5. [苹果起诉OpenAI挖角窃密，分析师称即使指控未证实也可能重创其硬件计划](./05-openai/)

苹果在美国起诉OpenAI，指控其挖角400名员工、窃取工程机和机密文件。分析师Paolo Pescatore认为，即使指控最终无法证实，OpenAI的硬件计划仍可能受拖累，双方本就脆弱的合作关系将进一步削弱。斯坦福大学教授Mark Lemley指出，若前苹果员工确实带走机密文件并在OpenAI使用...


## 论文研究

### 6. [OpenAI GPT-5.6 Sol Ultra 一小时证明 50 年图论猜想](./06-openai-gpt-5-sol-ultra-50/)

OpenAI 宣布其 GPT-5.6 Sol Ultra 模型在不到一小时内生成了图论难题“循环双覆盖猜想”的完整证明。该猜想由数学家 George Szekeres 和 Paul Seymour 于 1970 年代提出，悬而未决超过 50 年。模型通过调用 64 个并行子智能体及对抗智能体，在预留...


## 技巧与观点

### 7. [纳德拉提出“反向信息悖论”：企业使用AI时需保护自身知识](./07-ai/)

微软CEO萨提亚·纳德拉提出“反向信息悖论”：AI时代，买家为使用AI支付金钱，同时必须暴露专有知识（提示词、工具使用、纠正反馈等），这些“智力废气”被模型学习，导致信息不对称向卖家倾斜。企业需要真正的信任边界，确保自身数据、痕迹、评估、适配权重和记忆在边界内积累，未经同意不得外泄。纳德拉呼吁企业拥...

### 8. [Tibo 分享通过 CLIProxyAPI 将 Claude Code 后端模型切换为 GPT-5.6 Sol 的方法](./08-tibo-cliproxyapi-claude-code-gpt-5-sol/)

用户 Tibo 分享了一种通过 CLIProxyAPI 将 Claude Code 后端模型切换为 GPT-5.6 Sol 的方法。只需三步：安装 CLIProxyAPI、连接认证、设置环境变量别名 `claudex`。该别名配置了子智能体模型、始终启用 Effort、最大并发工具调用数等参数。引用...

### 9. [xAI Grok Build CLI 网络流量分析：上传仓库全部文件及 git 历史](./09-xai-grok-build-cli-git/)

对 xAI 官方 Grok Build 编码 CLI（grok 0.2.93）的网络流量分析显示，该工具在消费者登录后会向 xAI 发送三类数据：一是它读取的文件内容（包括 .env 密钥文件）以明文形式通过 POST /v1/responses 传输，并同时打包成 session_state 存档...

### 10. [OpenAI CEO Altman 改口称 AI 净创造就业，Anthropic CEO 也修正早期言论](./10-openai-ceo-altman-ai-anthropic-ceo/)

OpenAI CEO Sam Altman 表示，他“相当确信”AI 迄今为止净创造了就业，并承认“这并非我预期”。此前他曾警告 AI 影响可能快得“有点吓人”。Anthropic CEO Dario Amodei 也修正了早期言论，将自动化描述为生产力倍增器而非岗位杀手。然而，多项研究未发现 AI...

### 11. [开源模型面临未来6个月的生存考验](./11-cmri2qrwo00a/)

美国白宫正讨论通过新行政令管理开源模型，最可能在未来6个月内禁止或无限期延迟能力接近GPT 5.5、Claude Opus 4.8或GLM-5.2水平的开源权重模型发布。Anthropic主导的反中国模型政治运动以知识蒸馏为由推动监管，实质是监管捕获。Reflection AI代表在相关会议上主张开...
