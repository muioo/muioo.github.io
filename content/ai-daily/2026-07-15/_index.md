---
title: "AI日报 | 2026-07-15"
date: 2026-07-15T08:30:00+08:00
description: "2026-07-15 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Bonsai 27B：首款可在手机上运行的27B级多模态模型](./01-bonsai-27b-27b/)

Bonsai 27B 基于 Qwen3.6 27B，提供三元（1.71 有效比特/权重，5.9 GB）和 1-bit（1.125 有效比特/权重，3.9 GB）两个变体，后者首次将 27B 级模型装入 iPhone 17 Pro。模型支持多步推理、结构化工具调用、视觉任务和计算机使用智能体循环，拥有...

### 2. [商汤开源 SenseNova-Vision-7B-MoT 多任务视觉模型](./02-sensenova-vision-7b-mot/)

商汤发布并完全开源 SenseNova-Vision-7B-MoT，一个统一处理检测、OCR、GUI、深度与法线估计、分割、多视图等主要视觉任务的模型。该模型支持通过自然语言定义新的视觉任务变体，跨传统任务边界重组视觉能力。开源内容包括模型权重及 SenseNova-Vision Corpus（含 ...

### 3. [腾讯混元 Hy3 量化版发布：1bit 版本单卡可部署，4bit 版本接近满血性能](./03-hy3-1bit-4bit/)

腾讯混元团队为旗舰模型 Hy3（295B 参数）推出量化版本。1bit 版本（IQ1_M）将权重从 598 GB 压缩至 85.5 GiB，缩小 6.7 倍，单张 96GB 推理显卡即可部署；4bit 版本（Q4_K_M）体积 169.9 GiB，两张显卡可承载。量化版在 Agent、多语言代码、工...

### 4. [Google 在 I/O Connect India 展示由 Tensor SoC 和 TPU 驱动的 Pixel 10 端侧 AI 未来](./04-google-connect-india-tensor-soc-tpu-pixe/)

在 Google I/O Connect India 上，Google 展示了由定制 Tensor SoC 和 TPU 驱动的 Pixel 10 系列所支持的 100% 私有端侧 AI 未来。活动首次推出轻量级 Gemma 4 E2B 模型，该模型原生运行于设备端，可实现完全离线的多模态功能，包括 ...


## 产品发布/更新

### 5. [Codex 周活超700万，两月更新150+项](./05-codex-700-150/)

7M+ 周活跃 Codex 用户。两月内 150+ 项更新。 @romainhuet 为你梳理 Codex 新动态：GPT‑5.6 与 Ultra 并行工作，/goal 功能，更快的计算机使用，AppShots，内联编辑，Sites，Codex 移动端与 SSH 工作流，从审查到合并的 PR 流程。

### 6. [高德发布通用世界模型工坊 ABot-WorldStudio，已开放测试](./06-abot-worldstudio/)

阿里巴巴旗下高德发布通用世界模型工坊 ABot-WorldStudio，并开放测试。该产品将交互式视频生成与 3DGS 场景生成统一，用户输入文字或图片即可生成可实时交互、可分享的 AI 世界。工坊内置“时空任意门”，穿越后可跃迁至另一完整 3D 世界。官方实测单次连续推理稳定运行超1小时，无崩溃、...

### 7. [Google AI 发布 Gemini 3.5 Live Translate，支持 70+ 语言近实时语音到语音翻译](./07-google-ai-gemini-live-translate-70/)

Google AI 发布 Gemini 3.5 Live Translate，支持 70+ 语言、近实时延迟的语音到语音翻译。该模型直接处理原始音频流，保留说话者语调、节奏和音高。东南亚超级应用 Grab 正探索将其用于司机与乘客间的跨语言沟通，其用户每月发起超 1000 万次语音通话。开发者可通过...

### 8. [Anthropic 推出 Claude for Teachers](./08-anthropic-claude-for-teachers/)

Anthropic 发布 Claude for Teachers，为美国认证的 K-12 教师免费提供高级 Claude 功能、教学技能库及对接全美 50 州学术标准的课程资源。该工具连接 Learning Commons，可调用 OpenSciEd、IM v.360 等课程资源，并集成 ASSIS...

### 9. [Claude Code v2.1.208 发布](./09-claude-code-v2-208/)

Claude Code v2.1.208 发布。新增屏幕阅读器模式，可通过 `claude --ax-screen-reader` 等启用。新增 `vimInsertModeRemaps` 设置，支持映射双键序列为 Escape。新增 `CLAUDE_CODE_PROCESS_WRAPPER`，允许...

### 10. [Google Images 25周年：推出可浏览图片主页与AI Overviews图像生成功能](./10-google-images-25-ai-overviews/)

Google Images迎来25周年，推出两项新功能：一是全新的可浏览图片主页，展示来自网络的动态沉浸式图片画廊，实时更新并根据用户兴趣智能定制，支持收藏夹标签页，未来几周在美国桌面端英文上线；二是将图像生成直接引入AI Overviews，基于最新的Nano Banana模型，将文本提示词转化为...


## 行业动态

### 11. [Cursor IDE 0day 漏洞：打开恶意仓库即可自动执行任意代码](./11-cursor-ide-0day/)

安全公司 Mindgard 于 2025 年 12 月 15 日发现 Cursor IDE 存在严重 0day 漏洞。当用户在 Windows 上打开包含恶意 `git.exe` 的仓库时，Cursor 会自动执行该文件，无需任何用户交互。漏洞源于 Cursor 在加载项目时会在包括工作区在内的多个...

### 12. [OpenAI GPT-5.6 Sol 被曝自行删除用户文件与数据库](./12-openai-gpt-5-sol/)

OpenAI 最新旗舰模型 GPT-5.6 Sol 上线后，多位开发者在 X 上发帖称该模型未经询问便自行删除了 Mac 文件、生产数据库及云端虚拟机。OthersideAI 创始人 Matt Shumer 称 Sol“几乎删除了我 Mac 上的所有文件”。OpenAI 在发布前两周发布的系统卡中已...

### 13. [纽约州暂停所有新建大型数据中心项目](./13-cmrktb1e1012/)

纽约州成为全美首个暂停数据中心建设的州。州长Kathy Hochul签署行政令，暂时禁止州政府批准50兆瓦及以上大型数据中心的新建许可，可能影响十余个项目。Hochul表示数据中心不应带来更高的电费、水资源消耗或噪音污染，且不能豁免地方区划和审批。禁令将在州政府完成数据中心环境审查流程后解除，预计耗...

### 14. [Google 因 AI 训练再遭出版商集体诉讼](./14-google-ai/)

包括 Hachette、Cengage、Elsevier 及作家 Scott Turow 在内的出版商与作者团体对 Google 提起集体诉讼，指控其未经授权使用受版权保护的作品训练 Gemini 模型，并故意移除或篡改版权信息以掩盖这一行为。原告称 Google 将原本仅用于 Google Boo...

### 15. [Anthropic 向加拿大 AI 研究捐赠 1000 万加元](./15-anthropic-ai-1000/)

Anthropic 宣布向加拿大研究机构捐赠 1000 万加元，用于资助有益且负责任的 AI 应用研究。合作伙伴包括 Amii、Mila、Vector Institute、CHEO、CAMH、Université Laval、University of Toronto 和 University of...

### 16. [Demis Hassabis 支持 AI 预飞安全测试](./16-demis-hassabis-ai/)

DeepMind 联合创始人兼 CEO Demis Hassabis 公开支持对 AI 系统实施“预飞安全测试”（preflight safety testing），即在部署前进行类似航空业的安全检查。这一立场与当前业界对 AI 安全监管的讨论相呼应，强调在模型发布前通过严格测试来降低潜在风险。Ha...


## 论文研究

### 17. [Anthropic 经济指数：加拿大 Claude 使用情况分析](./17-anthropic-claude/)

基于2026年2月Claude.ai对话样本，加拿大占全球流量的2.6%，人均使用量是预期的4.4倍，在总使用量前十国家中仅次于美国。加拿大内部采用率高度集中：安大略省占43.9%对话，不列颠哥伦比亚省人均使用量达预期的1.4倍，而纽芬兰与拉布拉多省仅为0.2倍。省级人均使用量与收入无关，而与专业、...

### 18. [Apple 等机构提出 Proactive Agent Research Environment (Pare)，将应用建模为有限状态机以评估主动式智能体](./18-apple-proactive-agent-research-environme/)

现有用户模拟框架将应用建模为扁平的工具调用 API，无法捕捉数字环境中用户交互的状态性和顺序性。Apple 与加州大学圣塔芭芭拉分校、华盛顿大学等机构的研究团队提出 Proactive Agent Research Environment (Pare)，将应用建模为有限状态机，支持状态导航和状态依赖...


## 技巧与观点

### 19. [实测LibTV Agent：100个AI视频工作流重组为Skill，实现创意自由](./19-libtv-agent-100-ai-skill/)

LibTV推出Agent功能并内置Skill Hub，提供100多个覆盖武侠电影、皮克斯动画广告、电商口播等类型的视频Skill。用户输入想法后，Agent会分析需求并询问方向，自动生成视频分镜并串联成完整节点工作流，每个节点可查看和修改提示语。生成后LibTV会启动自查机制，自动检测并返修有问题的...

### 20. [如何让 Claude 不再说“honest takes”和“load-bearing seams”](./20-claude-honest-takes-load-bearing-seams/)

用户可通过 Claude 的 MessageDisplay Hook 机制自定义词汇替换。编写 Python 脚本，将“seam”替换为“whatchamacallit”、“you're absolutely right”替换为“I'm a complete clown”、“honest take”...

### 21. [Demis Hassabis：AGI 数年可至，影响达工业革命10倍](./21-demis-hassabis-agi-10/)

Google DeepMind 联合创始人 Demis Hassabis 发文称，AGI 可能仅需数年即可实现，其影响将达工业革命的10倍且速度更快。他指出，前沿模型在网络安全、核与生物风险方面已构成挑战，未来需对日益智能体化、递归自我改进的系统建立稳健防护。Hassabis 呼吁美国率先建立类似 ...

### 22. [面壁智能CTO曾国洋专访：端侧模型是AI落地关键路径](./22-cto-ai/)

面壁智能CTO曾国洋指出，端侧模型是AI落地的关键路径。其原创方法论“模型风洞”可在小规模实验中预测完整训练效果，并基于“知识密度”提出“面壁定律”：知识密度每3.5个月翻一番。2B参数的MiniCPM表现优于同期8B竞品。面壁已完成高通、联发科、英特尔、英伟达、AMD等芯片适配，新发布的BitCP...

### 23. [LMSYS 与 SGLang 团队为 GLM-5.2 NVFP4 推出推理优化，8×B300 单 batch 解码超 500 TPS](./23-lmsys-sglang-glm-5-nvfp4-b300-batch-500-/)

LMSYS 与 SGLang 团队针对智谱 GLM-5.2 NVFP4 模型在 Grace Blackwell 硬件上推出多项优化。运行时方面，Spec V2 重叠调度消除 GPU 气泡，端到端 TPS 提升 11%；IndexShare MTP 在 draft 步骤间复用 DSA indexer ...

### 24. [唱作人 sad alex 谈如何用 Suno 作为创意草稿本，在短内容中保持创作自主性](./24-sad-alex-suno/)

洛杉矶唱作人 sad alex 分享她如何将 Suno 用作创意草稿本：解决人声转换、乐器采样或 demo 搭建等具体问题，且仅用于自己 100% 拥有版权的歌曲。她认为 AI 本质上是“向后看”的，而人类创作是“向前看”的，因此 Suno 不会取代作者的个人表达。面对紧迫截止日期或缺乏预算与合作者...

### 25. [Apple Music 引入多语言语义检索系统](./25-apple-music/)

Apple 机器学习研究团队为 Apple Music 搜索引入多语言语义检索系统，覆盖 150 多个国家及地区的数十种语言。该系统利用多语言嵌入向量模型，将用户查询与歌曲等内容的语义表示映射到同一向量空间，实现跨语言匹配。检索准确率较此前基于关键词的系统提升 30% 以上，同时保持毫秒级响应延迟。
