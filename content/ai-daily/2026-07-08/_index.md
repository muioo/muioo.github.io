---
title: "AI日报 | 2026-07-08"
date: 2026-07-08T08:30:00+08:00
description: "2026-07-08 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Meta Superintelligence Labs 推出 Muse Image 和 Muse Video](./01-meta-superintelligence-labs-muse-image-m/)

Meta Superintelligence Labs 发布首个媒体生成模型 Muse Image 和 Muse Video。Muse Image 是目前最先进的图像生成模型，能精确遵循指令、精准编辑、多参考构图，并利用 Instagram 社交上下文。它还具备智能体工具使用能力并集成 Muse S...


## 产品发布/更新

### 2. [MIRA：可玩多人世界模型，20 FPS实时生成“火箭联盟的梦”](./02-mira-20-fps/)

MIRA是一个可玩、多人的世界模型，被形容为“火箭联盟的梦”。它基于10k小时公开机器人收集的数据训练，学习四玩家游戏动态，根据按键实时生成画面，帧率达20 FPS。模型由General Intuition与Kyutai Labs联合构建，Epic Games提供协作。Ethan Mollick称从...

### 3. [Rowboat：开源、本地优先的桌面AI助手](./03-rowboat-ai/)

Rowboat 是一个开源、本地优先的桌面 AI 助手，将邮件、会议、Slack 等数据索引为 Obsidian 风格的知识图谱，提供持久上下文记忆。内置邮件客户端、浏览器、会议记录器、代码模式（可调用 Claude Code 或 Codex 代理），并支持按事件或定时运行的背景代理。用户可通过 M...

### 4. [Grok Imagine 更新：支持 15 秒视频](./04-grok-imagine-15/)

Grok Imagine 更新。请更新你的 Grok 应用！15 秒 Imagine 视频现已可用，质量令人难以置信。

### 5. [Claude Cowork 向移动端和网页端开放](./05-claude-cowork/)

Claude Cowork 正在向移动端和网页端开放，让会话和文件跨设备同步。Beta 版将在未来几周内首先面向 Max 用户推出。Cowork 可让 Claude 跨文件、日历、邮件、即时通讯等工具完成复杂任务，其中超过 90% 的使用场景并非软件开发，而是日常知识工作（业务运营和内容创作）。工作...

### 6. [Gemini API Managed Agents 新增后台执行、远程 MCP 与自定义函数等能力](./06-gemini-api-managed-agents-mcp/)

Google 为 Gemini API 的 Managed Agents 新增后台执行、远程 MCP 服务器集成、自定义函数调用与凭证刷新功能。后台执行通过传入 `background: true` 异步运行任务，立即返回 ID 供轮询状态或流式获取进度。Managed Agents 可直接连接远程...

### 7. [NotebookLM短视频概览正式上线](./07-notebooklm/)

短视频概览功能已正式在移动端和网页端面向所有英语用户全面上线！ 一如既往，您的意见对我们至关重要。请在下方分享您最喜欢的作品，并告诉我们接下来需要添加哪些功能！❤️

### 8. [Hugging Face Storage 成为 SkyPilot 一级后端：零出站费跨云存储](./08-hugging-face-storage-skypilot/)

Hugging Face Storage 现为 SkyPilot 的一级后端。用户通过 `hf://` URL 和现有 HFTOKEN 即可将 Hugging Face Bucket（读写）或模型/数据集/Space 仓库（只读）挂载到 SkyPilot 任务中，支持 MOUNT（FUSE 懒加载）...

### 9. [Claude Code v2.1.203 发布](./09-claude-code-v2-203/)

本次更新新增登录过期警告和手动权限模式标记，并将附加工作目录加入 MCP roots/list。修复了 macOS 下因内存检测误报导致后台会话卡顿 15–20 秒（回归自 2.1.196）、后台会话因 token 过期永久不可用（现自动恢复）、交互式会话中上下文指示器每轮重分析整个对话导致 CPU...


## 行业动态

### 10. [中国拟限制外国访问最强AI模型](./10-ai/)

中国计划限制外国访问其最强AI模型，近期与阿里巴巴、字节跳动、Z.ai等企业会谈，拟将先进模型（含未发布）留在中国国内。商务部主导、国家发改委参与，表明此举属出口管制而非平台监管。目标涵盖闭源和开源模型，不仅限API访问，还包括可下载权重。同时讨论将模型泄漏视为国家安全犯罪，并限制外国资本投资中国A...

### 11. [Ethan Mollick：开放权重模型供给难持续](./11-ethan-mollick/)

这是一个关键原因，我不期望前沿开放权重模型的流动会无限期持续，甚至不会持续更长时间。

### 12. [微软为降成本在Copilot中用自研MAI模型替换OpenAI和Anthropic模型](./12-copilot-mai-openai-anthropic/)

微软正用自研MAI模型替换Copilot产品中的OpenAI和Anthropic模型以降低支出。MAI模型已在Excel和Outlook中每周处理数万次请求，但占比仍小。Build大会上发布推理模型MAI-Thinking 1，声称编码媲美Sonnet 4.6和Opus 4.6，但基准测试大幅落后，...

### 13. [美国首批自主地面车辆在乌克兰参战](./13-cmrafv8m4009/)

美国自动驾驶车辆公司 Forterra 宣布，过去九个月已向乌克兰战场部署超过 100 辆基于 Polaris ATV 的 Lancer 自主地面车辆。这些汽油动力车辆可携带 750 公斤货物，加装 Starlink 天线实现远程操控，已执行 1100 多次任务，行驶 2500 英里，运送 777,...


## 论文研究

### 14. [苹果研究：单个神经元即可绕过大型语言模型的安全对齐](./14-cmrasd6r300i/)

苹果研究人员发现，安全对齐由两类神经元调控：拒绝神经元控制有害知识是否表达，概念神经元编码有害知识本身。在七个模型（1.7B至70B参数）中，仅需抑制单个拒绝神经元即可绕过安全对齐，回答有害请求；或放大单个概念神经元，从无害提示诱导出有害内容。整个过程无需训练或提示工程。结果表明安全对齐由个别神经元...

### 15. [Weblica：面向视觉网页智能体的可扩展可复现训练环境](./15-weblica/)

苹果研究团队提出Weblica框架，通过HTTP级缓存保存网页稳定视觉状态并保留交互行为，结合大语言模型基于真实网站与核心导航技能合成环境，构建可复现、可扩展的训练环境。该框架将强化学习训练扩展到数千个多样化的环境和任务。最佳模型Weblica-8B在多个网页导航基准上超越同等规模的开源模型，推理步...

### 16. [DynaMiCS：带性能约束的大语言模型动态混合微调](./16-dynamics/)

DynaMiCS是一种动态混合优化器，将多领域微调建模为带性能约束的优化问题。它通过短领域特定探测运行估计跨领域效应斜率矩阵，再基于概率单纯形优化计算混合权重，在提升目标领域性能的同时将约束领域损失维持在参考水平以下。实验表明，DynaMiCS相比固定混合基线取得更强的目标领域提升和约束满足，且计算...


## 技巧与观点

### 17. [Elvis Saravia 通过 HITL 和 DialAgent 提升 agentic loops 可靠性](./17-elvis-saravia-hitl-dialagent-agentic-loo/)

Elvis Saravia 介绍使用 human-in-the-loop（HITL）来提升 agentic loops 的可靠性。他所有 Claude 和 Codex agent 会话都通过 @DialAgent MCP 服务器，该服务器为 agent 提供专属号码，支持语音、SMS、iMessag...

### 18. [FDE爆发：AI公司12个月承诺97.5亿美元部署工程](./18-fde-ai-12-97/)

AI公司在12个月内合计承诺97.5亿美元用于建设前部署工程（FDE）团队。三种结构模型浮现：资产负债模型（微软、亚马逊从现有编制调配，Salesforce承诺1000个FDE岗位）；独立实体模型（OpenAI Deployment Company融资40亿美元，投后估值140亿；Anthropic...

### 19. [YC CEO声称每日用AI部署3.7万行代码，开发者审查发现前端代码大量臃肿低效](./19-yc-ceo-ai/)

Y Combinator CEO Garry Tan在X上宣称，他与AI编码代理每天在五个项目中部署37000行代码，并保持连续72天发布记录。波兰开发者Gregorein深入审查Tan网站前端代码，发现大量臃肿与低效问题：页面加载169次请求、总计6.42MB数据（对比Hacker News仅7次...

### 20. [Liquid AI 开源 Antidoom：基于最终 Token 偏好优化的推理模型死循环修复方法](./20-liquid-ai-antidoom-token/)

Liquid AI 开源了 Antidoom，一种基于 Final Token Preference Optimization (FTPO) 的针对性修复方法，用于减少推理模型中的 doom loop（死循环）问题。该方法定位循环开始的第一个 token，训练模型选择连贯替代项，而不改变整体输出分布...

### 21. [在网络不稳定的地区，小型AI模型正逐渐普及](./21-ai/)

2019年，Adebayo Alonge因服务器远在美国致RxScanner单次扫描超5分钟，工程师2小时内将AI模型缩小至可在Android手机本地运行，此后RxScanner能在无宽带、缺电地区验药。小AI模型参数通常至多几十亿，可在手机或Raspberry Pi上运行，功耗仅数瓦。类似案例包括...

### 22. [Krea 2 身份保留功能上线](./22-krea/)

Krea 2 的身份保留功能已发布，配套模型和 ComfyUI 节点也已上线。🔥

### 23. [人们如何使用Claude Cowork](./23-claude-cowork/)

基于2026年5月11-31日120万次匿名会话样本，Claude Cowork最大用途为业务流程与运营（33.4%），如整理报告、核对表格；其次为内容创作与文案（16.4%），如起草稿件、制作幻灯片；软件开发仅占8.7%。用户多用它处理跨团队衔接性任务，例如律师处理文档格式、招聘经理汇总面试反馈。...

### 24. [在 Claude Code 中选择 Claude 模型与努力级别](./24-claude-code-claude/)

Claude Code 提供模型（model）和努力级别（effort）两种设置。模型选择决定能力范围，更大模型（如 Claude Fable 5）在基准上优于 Claude Sonnet。努力级别不单是思考时间，还控制读取文件数、验证步骤及多步任务的推进深度。较高努力下 Claude 会自行读取文...
