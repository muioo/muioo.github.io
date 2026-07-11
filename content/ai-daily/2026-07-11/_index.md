---
title: "AI日报 | 2026-07-11"
date: 2026-07-11T08:30:00+08:00
description: "2026-07-11 AI 热点日报"
comments: false
---

## 产品发布/更新

### 1. [百度搭子在成都AI Day发布四项更新：个人版升级、自媒体套件、企业版及搭子联盟](./01-ai-day/)

百度搭子在成都百度AI Day上发布四项更新。个人版新增浏览器调用、智能路由（平均任务耗时降20%，Token利用率提升25%）、多端共享记忆及强化PPT生成，并上架“一镜”数字人制作、“灵医”报告解读等Skill。行业首个自媒体专业套件支持选题到复盘全链路。企业版支持团队协作与权限管理。搭子联盟启...

### 2. [Claude Code桌面版新增应用内浏览器](./02-claude-code/)

Claude Code 桌面版现在有了应用内浏览器。 Claude 可以调出文档、设计稿或任何其他网站。它可以像操作本地开发服务器一样，进行阅读、点击浏览和交互。 该浏览器采用沙盒机制且可配置：你可以自行选择会话是否持久保留。

### 3. [Perplexity 推出跨模型信用额度分析功能](./03-perplexity/)

推出 Computer Analytics：你现在可以跨模型跟踪信用额度支出。 该功能现已面向个人和企业用户开放，可在账户设置的 Analytics 下使用。

### 4. [Claude Code v2.1.206 发布](./04-claude-code-v2-206/)

Claude Code v2.1.206 发布，主要更新包括：为 `/cd` 命令添加目录路径建议；新增 `/doctor` 检查以建议修剪 CLAUDE.md 文件中模型可从代码库推导的内容；`/commit-push-pr` 现在自动允许 git push 到仓库配置的推送远程仓库；`/logi...

### 5. [蚂蚁集团开源高性能大模型推理框架 SGLang](./05-sglang/)

蚂蚁集团通过 GitHub 新仓库 inclusionAI/sglang 开源了 SGLang，这是一个面向大语言模型和多模态模型的高性能推理服务框架。


## 行业动态

### 6. [Apple 起诉 OpenAI 窃取商业机密](./06-apple-openai/)

Apple 于周五向美国加州北区联邦法院提起诉讼，指控 OpenAI 窃取商业机密并违反合同。诉状称，OpenAI 高级领导层（包括首席硬件官 Tang Tan）指使前 Apple 员工在招聘过程中窃取机密，包括使用未发布产品的项目代号、要求应聘者携带硬件组件参加面试。Apple 还指控前高级系统电...

### 7. [扎克伯格首度回应 Meta“算力过剩”：没人会嫌算力太多，但租出去更赚钱](./07-meta/)

Meta CEO 扎克伯格首次正面回应公司筹划云基础设施业务一事，否认“算力过剩”猜测，称内部算力需求依然旺盛、满负荷运转。但他同时表示，当前市场对算力出价极高，将部分 AI 基础设施对外出租在财务上更划算。Meta 正制定代号“Meta Compute”的云计算计划，包括开放模型访问权限和直接出租...

### 8. [Cognition 如何信任 Claude Fable 5 通宵工作](./08-cognition-claude-fable/)

Cognition 研究高级副总裁 Silas Alberti 表示，其 AI 软件工程师 Devin 测试了几乎所有 Claude 模型，Claude Fable 5 是首个能信任其通宵运行的模型。在 Cognition 自建的 Frontier Code 基准测试最难子集上，此前 Opus 模型...


## 论文研究

### 9. [宇树G1人形机器人完成首例活体微创手术](./09-g1/)

一篇新的《自然》论文展示了宇树G1人形机器人执行研究人员所称的首例由人形机器人完成的活体标准微创手术。加州大学圣地亚哥团队使用G1，以常规手术器械完成了对两只活猪的腹腔镜胆囊切除术；第二次手术耗时32分钟。该机器人仍需反复校正，且尚无法满足手术无菌标准，但其成本可能仅为达芬奇系统的约5%。

### 10. [博科圣地如何利用前沿AI技术](./10-ai/)

2025至2026年间对尼日利亚东北部27名前“博科圣地”成员的半结构化访谈揭示了该组织在2024年系统性地利用前沿AI技术。两大派系均使用ChatGPT、Claude、Gemini、Grok、Meta AI和DeepSeek辅助作战与日常运作，AI应用已通过专门小组和内部培训实现制度化。成员成功绕...

### 11. [小红书发布大模型新架构 PIPO](./11-pipo/)

小红书提出 PIPO 架构，通过输入侧压缩器将两个 token 折叠为一个 latent，输出侧 MTP head 将隐藏状态展开为额外 token，实现输入长度减半、每步输出翻倍。基于 Qwen3.5-4B/9B backbone，在 AIME 2025 等基准上最高带来 +7.15 pass@4...

### 12. [DeepSeek-V4 Flash 强化学习训练登陆 AMD Instinct MI355X GPU，由 Miles 框架支持](./12-deepseek-v4-flash-amd-instinct-mi355x-gp/)

DeepSeek-V4 Flash 的强化学习训练现已在 AMD Instinct MI355X GPU 上通过 Miles 框架获得支持，基于 ROCm 软件栈运行。该 2840 亿参数 MoE 模型（每 token 激活 130 亿参数）需 SGLang 进行 rollout 生成、Megatr...


## 技巧与观点

### 13. [马斯克承认Anthropic是当前AI领导者](./13-anthropic-ai/)

马斯克在X上发文承认自己此前对Anthropic的判断有误，称其“显然是当前AI领域的领导者”。他表示，没有公司发布过像Mythos/Fable这样优秀的模型，并相信Anthropic很快会推出Mythos 2。他还强调，即使作为竞争对手，也不会以伤害对方的方式切断合作，并列举了特斯拉开源专利、开放...

### 14. [Elon Musk 转发用户称赞 Grok Build 的反馈](./14-elon-musk-grok-build/)

Elon Musk 转发用户 @0x0funky 对 Grok Build 的称赞。该用户称 Grok Build 是目前唯一集大成的 coding agentic workflow，内建图像生成和图片生视频功能，生图速度快且品质不输 Codex。Agent 可直接完成图像与视频生成，无需额外串接 ...

### 15. [Thinking Machines Lab：构建延伸人类意志与判断的 AI](./15-thinking-machines-lab-ai/)

Thinking Machines Lab 在官方博客中阐述其使命：构建能够延伸人类意志与判断的 AI。文章指出，当前多数 AI 在少数地方训练后便冻结，无法被使用者塑造。该实验室正致力于训练具备多模态交互和可定制化能力的强模型，开发允许用户训练模型权重的工具，并构建拓宽人机沟通渠道的界面。其核心理...

### 16. [GitHub Copilot 代码审查改用共享工具后性能下降，通过重写指令实现 20% 成本降低](./16-github-copilot-20/)

GitHub 在 Copilot 代码审查中尝试用 Copilot CLI 的共享代码探索工具（grep、glob、view）替换原有专用工具，结果导致审查成本上升、有效评论数量下降。分析 trace 发现，问题不在工具本身，而在于指令让智能体像通用编程助手一样大范围浏览仓库，而非像审查者一样从 d...

### 17. [Theory Ventures 三周年：AI 如何重塑软件栈与风投定义](./17-theory-ventures-ai/)

Theory Ventures 合伙人 Tomer Tunguz 发文总结 AI 带来的市场巨变。新模型每 41 天发布一次，公司达 1 亿美元收入速度创纪录。AI 压缩时间导致风投阶段定义失效，种子轮规模从 100 万到 5 亿美元不等。推理正取代模型成为 AI 主导市场，基础设施按视频、批处理、...
