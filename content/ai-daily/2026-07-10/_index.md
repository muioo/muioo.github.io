---
title: "AI日报 | 2026-07-10"
date: 2026-07-10T08:30:00+08:00
description: "2026-07-10 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [OpenAI 推出 ChatGPT Work：可跨应用自主工作的 AI 智能体](./01-openai-chatgpt-work-ai/)

OpenAI 发布 ChatGPT Work，一个能跨应用和文件收集信息、将复杂项目分解为小步骤独立完成并持续工作数小时的 AI 智能体。它内置 Codex 技术，目前每周超 500 万用户使用 Codex，其中超 100 万用于非软件开发场景。ChatGPT Work 由今天同步推出的最新前沿模型...

### 2. [蚂蚁灵波开源实时交互世界模型 LingBot-World 2.0](./02-lingbot-world/)

蚂蚁灵波开源新一代实时交互世界模型 LingBot-World 2.0（14B 参数），支持施法、攻击、跳跃等丰富角色动作及文本驱动事件（如切换场景、召唤风暴），内置 Pilot Agent 与 Director Agent 实现世界持续演化，并支持多人同时交互。模型采用因果预训练范式和混合双向自回...

### 3. [OpenAI 发布最强模型与最佳博文](./03-openai/)

显然是我们有史以来最好的模型，也是我们写得最好的博文之一： https://openai.com/index/gpt-5-6/

### 4. [蚂蚁灵波开源全球首个面向具身智能的MoE视频基模LingBot-Video](./04-moe-lingbot-video/)

蚂蚁灵波科技正式开源LingBot-Video，这是全球首个基于MoE架构、面向具身智能的视频生成基础模型。总参数30B，推理时仅激活约3B，效率较同规模Dense架构提升约3倍。模型引入7万小时VLA、VLN、Ego等机器人数据，并通过多维强化学习奖励系统对齐物理合理性与任务完成度。在RBench...

### 5. [NVIDIA 发布 Nemotron-Labs-3-Puzzle-75B-A9B：压缩混合 MoE 模型，服务器吞吐量提升 2.03 倍](./05-nvidia-nemotron-labs-3-puzzle-75b-a9b-mo/)

NVIDIA 发布 Nemotron-3-Super 的压缩变体 Nemotron-Labs-3-Puzzle-75B-A9B，总参数从 120.7B 降至 75.3B，活跃参数从 12.8B 降至 9.3B，保持 88 块混合布局（40 Mamba、40 MoE、8 注意力）。在 8×B200 节...

### 6. [Robbyant 发布 LingBot-VLA 2.0：开源 6B 跨实体机器人视觉-语言-动作模型](./06-robbyant-lingbot-vla-6b/)

Robbyant 推出 LingBot-VLA 2.0，一个 6B 参数的开源视觉-语言-动作（VLA）基础模型。它以 Qwen3-VL-4B-Instruct 为骨干，采用 MoE 动作专家架构，通过 55 维规范向量统一表示不同机器人的状态和动作。训练数据涵盖约 60,000 小时高质量数据（5...

### 7. [Meta 发布 Muse Spark 1.1 模型](./07-meta-muse-spark/)

来自 @finkd 的消息 — Muse Spark 1.1 已上线。


## 产品发布/更新

### 8. [微软发布Flint：面向AI智能体的可视化语言](./08-flint-ai/)

微软研究院推出Flint，一种可视化中间语言，让AI智能体通过简洁的人类可编辑spec自动生成美观图表。用户只需提供数据、语义类型和图表类型，Flint编译器即可推导坐标轴、配色、布局等底层参数。支持46种图表类型，可渲染到Vega-Lite、ECharts和Chart.js三个后端。项目通过npm...

### 9. [Claude 推出反思功能（Beta）](./09-claude-beta/)

Anthropic 为 Claude 推出一项反思功能（Beta），帮助用户追踪使用模式。用户可回顾过去 1、3、6 或 12 个月的活动总结，涵盖关键主题、使用频率和任务类型。功能结合 4D AI Fluency Framework（委托、描述、辨别、勤勉）提供协作分析，支持设定静音时段或定时休息...

### 10. [ChatGPT Sites将创意变可发布网站](./10-chatgpt-sites/)

将一个想法变成可发布和分享的实时网站 以下是OpenAI团队的一些成员用Sites构建的示例👇 @prd_008 用Sites将一个想法变成了个人专注应用：

### 11. [Google 推出 LiteRT.js：高性能 Web AI 推理运行时](./11-google-litert-js-web-ai/)

Google 发布 LiteRT.js，这是 LiteRT 跨平台边缘 AI 运行时的最新成员，专为 JavaScript 开发者设计，可直接在浏览器中运行机器学习模型。LiteRT.js 基于 WebGPU 和即将推出的 WebNN 实现 SOTA 推理性能，同时支持回退到 WebAssembly...

### 12. [Mistral 推出 Studio，为 AI 提示词和技能提供系统记录](./12-mistral-studio-ai/)

Mistral 今日推出 Studio，为 AI 提示词和技能提供集中式系统记录。平台将 prompts 和 skills 视为生产资产，支持不可变版本、回滚、明确所有权、分类标签和审计日志，保证变更可追溯。非开发者可直接编辑测试，通过标签将变更推送至生产，保留原有 CI/CD 流程。可观测性让生产...


## 行业动态

### 13. [Elon Musk称赞Anthropic并承诺不切断其算力](./13-elon-musk-anthropic/)

Elon Musk近日在X上承认此前对Anthropic的判断有误，称其“显然是当前AI领域的领导者”，盛赞Mythos/Fable模型“目前最好”，并承诺不会恶意切断其计算资源。2026年7月起，Anthropic成为SpaceX最大客户之一——双方5月签署协议，Anthropic以每月12.5亿...

### 14. [消息称特斯拉三代擎天柱人形机器人初步定型，马斯克放话达不成产能目标就开掉整个采购团队](./14-cmrdpmgpg05z/)

据晚点LatePost报道，特斯拉Optimus Gen 3经马斯克评审通过，即将量产。供应链要求供应商9月产能达1000台/周，年底升至2000-2500台/周，届时年产能可达10万台。马斯克六月底高管会上要求年底前实现产能目标，否则开除整个Optimus采购团队。弗里蒙特工厂已改造为Optimu...

### 15. [Ollama 开发者数达890万，B轮融资由Theory领投](./15-ollama-890-theory/)

Ollama 让开源模型在本地或云端轻松运行，保持体验一致。目前拥有890万开发者、6.7万集成，并与各大模型实验室及硬件供应商建立合作。B轮融资由Theory领投。

### 16. [Anthropic发起“硬问题”倡议，邀请公众提出AI相关尖锐问题](./16-anthropic-ai/)

Anthropic作为公益公司，发起“硬问题”倡议，邀请公众就AI对就业、社会、家庭、科学医学等领域的影响提出最尖锐的问题。此前已通过多种方式收集看法：首轮调查询问5.2万美国人；通过Anthropic Interviewer调查了159个国家70种语言的8.1万Claude用户；开展数十场线下焦点...

### 17. [Anthropic长期利益信托任命本·伯南克为受托人](./17-anthropic/)

Anthropic的长期利益信托（LTBT）任命前美联储主席、2022年诺贝尔经济学奖得主本·伯南克为最新受托人。他将与另外三位受托人共同监督公司以对社会长期有益的方式负责任开发先进AI的使命。LTBT独立于管理团队和投资者，受托人不持股、不分红，仅按服务时间获酬。该信托有权向Anthropic董事...

### 18. [GPT-5.5 生物漏洞赏金计划](./18-gpt-5/)

OpenAI 将 GPT-5.5 Bio Bug Bounty 升级为持续私密项目 OpenAI Bio Bounty Program，以 GPT-5.6 为起点并覆盖后续前沿模型，旨在发现能突破预设生物安全挑战的通用越狱攻击。奖励从 $25,000 提高至 $50,000，适用于


## 论文研究

### 19. [揭密在线策略蒸馏：何时有益、何时有害及原因](./19-cmre05t8p000/)

Apple机器学习研究团队提出训练无关诊断框架，以每个token、每个问题、每个教师的分辨率分析on-policy蒸馏。通过可扩展targeted-rollout算法估计理想梯度，并计算蒸馏梯度与理想梯度的余弦相似度（梯度对齐分数）。实验发现，蒸馏指导在错误rollouts上的对齐程度显著高于正确r...

### 20. [TGPO：通过可验证奖励强化学习激励第一人称视频时序感知](./20-tgpo/)

多模态大语言模型（MLLM）在第一人称视频理解中缺乏时序感知，常依赖空间捷径。为此，研究者提出 Temporal Global Policy Optimization（TGPO），一种基于可验证奖励的强化学习算法。TGPO 通过对比模型在时序有序与打乱帧上的输出，生成全局归一化奖励信号，明确奖励时序...

### 21. [Apple 提出 SRLM：自反思程序搜索提升长上下文处理能力](./21-apple-srlm/)

Apple 机器学习研究团队提出 SRLM 框架，利用自一致性、推理链长度和口头置信度三种内在信号，让模型在推理时评估候选长上下文交互程序。实验表明，在相同时间预算下，SRLM 较传统递归语言模型（RLM）最高提升 22%。分析发现，递归本身并非 RLM 性能关键，简单的自反思程序搜索无需显式递归即...


## 技巧与观点

### 22. [AI 能否回答 3 万亿美元的问题？](./22-ai/)

Sequoia 合伙人 David Cahn 更新 AI 基础设施支出估算：2026 年全球投入达 1.5 万亿美元，行业需产生 3 万亿美元收入才能回本。Anthropic 年化收入（ARR）达 600 亿美元，OpenAI 2025 年收入 130 亿美元（11 月称 ARR 200 亿美元），...

### 23. [社交媒体AI生成内容泛滥：LinkedIn超过40%长文为AI写作](./23-ai-linkedin-40-ai/)

安全公司Pangram通过Chrome扩展收集超100万条帖子，分析发现社交媒体AI生成内容泛滥。整体AI检测率13.8%，长文（超250词）中25.72%完全由AI生成。LinkedIn最为严重，超40%长文帖子被标记为完全AI生成，占全部AI内容的62%；X/Twitter近一半文章（23.9%...

### 24. [Bun 被 Anthropic 收购后用 Rust 重写，月下载超 2200 万](./24-bun-anthropic-rust-2200/)

Bun 于 2025 年 12 月被 Anthropic 收购，作者使用预发布版 Claude Fable 5 进行了大量 Rust 重写。Bun 最初用 Zig 在一年内构建，如今 CLI 月下载超 2200 万，被 Claude Code 等采用。广泛功能带来稳定性挑战，v1.3.14 修复了多...

### 25. [TeXada：基于MiniCPM的本地数学Agent发布](./25-texada-minicpm-agent/)

社区开发者基于MiniCPM5-1B和MiniCPM-V 4.6构建了本地优先的数学智能体TeXada。该Agent支持自然语言直接转LaTeX、手写/图像公式OCR转可编辑LaTeX、LaTeX补全与错误修复等核心功能。所有推理在本地完成，无需依赖云服务，保障隐私安全，适用于学生、研究人员和开发者...
