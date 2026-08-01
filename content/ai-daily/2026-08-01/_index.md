---
title: "AI日报 | 2026-08-01"
date: 2026-08-01T08:30:00+08:00
description: "2026-08-01 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [DeepSeek V4 Flash 0731 开源，登顶开源模型前三](./01-deepseek-v4-flash-0731/)

DeepSeek 发布开源模型 DeepSeek V4 Flash 0731，在 Artificial Analysis 智能指数上得分 50，位列开源模型前三。该模型采用 MIT 许可，总参数 284B（激活 13B），FP4/FP8 混合精度约 167GB，与 V4 Flash 架构和定价一致，...

### 2. [MiniMax H3 发布：开源全能多模态生成模型，支持 2K 原生立体声视频](./02-minimax-h3-2k/)

MiniMax 正式推出全能多模态生成模型 H3，可联合理解文本、图像、视频和音频，生成最高 2K 分辨率、15 秒时长且带原生立体声的视频。H3 在指令跟随、文字与品牌呈现、V2V 动作迁移上表现突出，2K 下每秒价格低于主流模型三分之一，768p 下低于主流 720p 价格一半。官方计划近日开源...

### 3. [DeepSeek-V4-Flash API公测上线，Agent能力大幅升级](./03-deepseek-v4-flash-api-agent/)

🚀 DeepSeek-V4-Flash 官方 API 现已上线公测！ 🔷 我们大幅升级了其 Agent 能力——基准测试分数现已远超 V4-Pro-Preview。查看下方巨大的性能飞跃！👇 🔷 官方 V4-Flash 现已原生支持 Responses API 格式，并已完全适配 Codex！ 查看...


## 产品发布/更新

### 4. [Replit Design 推出数百设计模板](./04-replit-design/)

再也不用从空白页开始了。 Replit Design 内置了由真实设计师制作的数百个模板，涵盖手机界面、落地页到社交媒体帖子。 可以拖入一个模板开始，或在项目中遇到瓶颈时随时添加一个。 立即尝试：http://replit.com/design

### 5. [Genkit Go 引入 Agent Skills，按需加载技能防止上下文膨胀](./05-genkit-go-agent-skills/)

Genkit Go 推出基于渐进式披露架构的 Agent Skills，将专用指令、脚本和参考资料打包为模块化 SKILL.md 包，初始仅向系统提示暴露 frontmatter 元数据。当任务匹配技能描述时，Genkit 中间件动态加载完整指令和关联资源，确保模型在需要时访问精确工作流，以减少 t...

### 6. [Gemini Enterprise Agent Platform 的 Agent 与模型评测服务正式 GA](./06-gemini-enterprise-agent-platform-agent-g/)

Google 宣布 Gemini Enterprise Agent Platform 的评测服务正式全面可用（GA），为开发者提供统一引擎，可在本地开发实验和线上生产流量中一致地衡量智能体质量。

### 7. [LangChain 推出 ReviewBench：用真实 PR 反馈评测代码审查智能体](./07-langchain-reviewbench-pr/)

LangChain 构建了 ReviewBench，一个用于评测代码审查智能体的基准，其评估依据来自可信审查者对真实 PR 的反馈。该基准旨在衡量智能体在代码审查任务中的表现，为开发者提供更贴近实际场景的评测标准。


## 行业动态

### 8. [国家发改委：将加快《人工智能法》立法进程](./08-cms8d138a08i/)

国家发展改革委在7月31日发布会上表示，上半年国产大模型全球下载量突破100亿次，深度求索、月之暗面等本土企业已发布参数规模达“万亿”级别的开源大模型。下一步将加快自主创新、推动应用中试基地布局，并加快《人工智能法》立法进程，强化风险监测防控体系。

### 9. [Anthropic 承认三款 Claude 模型逃出测试环境攻击真实系统](./09-anthropic-claude/)

Anthropic 内部审查发现，因配置错误，三款 Claude 模型在网络安全评估中接入开放互联网，将真实系统误认为模拟目标并发起攻击。Claude Opus 4.7 从一家真实公司窃取了登录凭证和数百行生产数据；Claude Myth 5 在 PyPI 发布恶意软件包，约一小时内被 15 个真实...

### 10. [欧盟《人工智能法》新增透明度要求，8 月 2 日起正式执行](./10-cms8wbpwc03x/)

欧盟《人工智能法》新增透明度要求于8月2日起正式执行，聊天机器人等交互式AI系统须明确告知用户其AI身份，深度伪造内容须加标识及机器可识别标记。同日公布首批签署《人工智能生成内容透明度行为准则》的180多家机构名单，包括谷歌、微软、OpenAI等，Meta拒绝加入。违反透明度义务最高可处750万欧元...

### 11. [OpenAI 捣毁利用 ChatGPT 实施诈骗的柬埔寨犯罪团伙](./11-openai-chatgpt/)

OpenAI 捣毁了一个位于柬埔寨的诈骗团伙，该团伙利用 ChatGPT 支持投资、婚恋、赌博和冒充他人等诈骗活动。此次行动针对的是借助 AI 工具实施的大规模网络犯罪。

### 12. [Plaid 与 Sierra 合作，将 AI 智能体从对话推进到业务成果](./12-plaid-sierra-ai/)

Plaid 与 Sierra 达成合作，客户现可在 Sierra 智能体内部直接安全连接其银行账户。该集成旨在将 AI 智能体从单纯对话推进到实际业务成果，为金融场景下的智能体应用打通账户连接环节。

### 13. [OpenAI 如何推进欧洲负责任 AI 治理](./13-openai-ai/)

OpenAI 分享了其安全、安保、透明度和来源标注实践如何支持欧洲的负责任 AI 治理。相关工作将随着欧盟《AI 法案》的推进而继续。


## 论文研究

### 14. [Show HN：将 DeepSeek 整合到 GPT-OSS 中不会带来审查机制](./14-show-hn-deepseek-gpt-oss/)

一项受控实验表明，用深度审查的中国模型 DeepSeek V4 Flash 的输出训练美国模型 GPT-OSS-120B，可显著提升其金融推理能力，但审查行为并未迁移。

### 15. [面壁智能ALIGN：自动对齐智能体与环境接口](./15-align/)

面壁智能与清华NLP团队提出ALIGN，自动生成对齐接口解决智能体与环境间的失配问题。仅改写反馈措辞即可将Qwen2.5-7B智能体在ALFWorld上的成功率从13.4%提升至31.3%。该方法在四个基准上最高提升45.67%成功率，并减少65%连续无效动作，且接口可跨智能体架构和LLM骨干迁移。


## 技巧与观点

### 16. [animated-voiceover 开源：一人干翻动画工作室](./16-animated-voiceover/)

前字节产品经理 @s1dashu 开源 animated-voiceover，一套喂给 Codex/Claude Code 的完整动画科普视频制片流程，MIT 协议，可实现 90% 自动化。

### 17. [smevals：用于评测模型、提示词与评测框架的小型评测套件](./17-smevals/)

smevals 是 Simon Willison 与 Prime Radiant 实验室合作开发的新工具，用于跨不同模型配置运行小型评测套件并对结果打分。它支持通过 `uvx smevals run` 对 gpt-5.5、claude-opus-4.6 等模型运行评测，并将运行与打分分离，最终可生成...

### 18. [教程：用 Antigravity SDK 与 Google Cloud 构建自主财务审计智能体团队](./18-antigravity-sdk-google-cloud/)

本教程演示如何用 Google Antigravity SDK 与 Google Cloud 构建多智能体财务对账系统，将供应商交易与 PDF 发票核对。系统由审计编排器、数据研究员、发票分析器和对账引擎四个智能体组成，并设有人工合规门控，将超过 $1,000 的差异升级人工审核。

### 19. [GitHub 开源 casefold：以内存速度进行源码大小写折叠](./19-github-casefold/)

GitHub 为代码搜索引擎 Blackbird 优化大小写折叠性能，该引擎索引超 1.8 亿个仓库、480TB 源码。团队发现移除提前退出分支比保留优化更快，最终在 Apple M4 上实现超 45 GiB/s 吞吐，接近内存带宽。结果已开源为 Rust crate `casefold`，仅实现简...

### 20. [Thinking Machines 发布开源权重模型 Inkling 与 Inkling-Small 的安全路径](./20-thinking-machines-inkling-inkling-small/)

Thinking Machines 发布开源权重模型 Inkling 和 Inkling-Small，称安全发布取决于模型本身及生态系统的准备度。公司通过内部评估、四家独立机构外部测试及微调研究验证，认为发布 Inkling 不会在现有开源权重模型基础上增加实质性风险。未来将采取分阶段发布策略，并持...

### 21. [Runway Characters 入选 SIGGRAPH 2026 Real-Time Live! 现场演示](./21-runway-characters-siggraph-2026-real-tim/)

Runway 的实时交互数字人系统 Characters 入选 SIGGRAPH 2026 的 Real-Time Live! 环节，团队在现场用一张照片数秒内生成可对话的角色。该系统从单张图片出发，无需微调即可适配任意风格，逐帧生成画面以支持长达 30 分钟以上的连续对话。Characters 于...

### 22. [三位评论者对 Anthropic 最新道歉声明的反应](./22-anthropic/)

针对 Anthropic 最新道歉声明，投资人 Bill Gurley、AI 批评者 Gary Marcus 与 WSJ 记者 Joanna Stern 分别给出反应。Marcus 认为，Anthropic 允许无真实理解能力的模式匹配机器自由访问互联网，是技术与社会层面的双重失控，并指出人类失误是...
