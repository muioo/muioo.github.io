---
title: "AI日报 | 2026-07-09"
date: 2026-07-09T08:30:00+08:00
description: "2026-07-09 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [推出 Grok 4.5](./01-grok/)

Cursor 与 SpaceXAI 联合训练了混合专家模型 Grok 4.5，在数万亿 tokens 的 Cursor 用户交互数据上训练，并通过强化学习解决软件工程、数据科学、金融、法律等领域的困难问题。基础版定价 $2/M 输入 tokens、$6/M 输出 tokens，快速版 $4/M 输入...

### 2. [OpenAI 发布 GPT‑Live 新一代全双工语音模型](./02-openai-gpt-live/)

OpenAI 今日推出 GPT‑Live，基于全双工架构实现同时听与说，支持自然打断与实时回馈。该模型每秒多次判断是否说话、倾听、打断或调用工具，并将搜索、推理等复杂任务委托给后台 GPT‑5.5，保持对话流畅。即日起向全球 ChatGPT 用户提供 GPT‑Live‑1 和 GPT‑Live‑1 ...

### 3. [Pulpie：用于清理网络的Pareto最优模型](./03-pulpie-pareto/)

Pulpie是一族Pareto最优模型，用于从HTML页面提取主要内容。其最小模型pulpie-orange-small（210M参数）在WebMainBench上取得0.862的ROUGE-5 F1分数，接近600M参数的Dripper（0.864），但成本仅1/20。在NVIDIA L4 GPU...

### 4. [SpaceXAI 发布 Grok 4.5，与 Cursor 联合训练的编程与智能体模型](./04-spacexai-grok-cursor/)

SpaceXAI 推出 Grok 4.5，称其迄今最聪明，聚焦编程、智能体任务和知识工作。该模型与 AI 编程编辑器 Cursor 联合训练，在数万块 NVIDIA GB300 GPU 上完成训练和强化学习。基准测试中，Grok 4.5 在 Harvey's Legal Agent Benchmar...

### 5. [蚂蚁集团旗下Robbyant开源LingBot-Vision：1B参数边界中心视觉基础模型，用于密集空间感知](./05-robbyant-lingbot-vision-1b/)

蚂蚁集团旗下具身智能公司Robbyant开源LingBot-Vision，一套自监督视觉Transformer家族，专为密集空间感知设计。旗舰ViT-g/16参数约1.1B，采用掩膜边界建模训练，将边界作为原生预训练信号。在密集空间任务中，该1B模型匹配或超越参数规模高达7倍的大模型（如7B DIN...


## 产品发布/更新

### 6. [Seedream 5.0 Pro 登陆 Runway，支持14种语言](./06-seedream-pro-runway-14/)

Seedream 5.0 Pro 现已登陆 Runway。可通过提示词或参考图生成高细节图像，图像内文字清晰可读，支持多达14种语言。立即点击下方链接尝试。

### 7. [Replit 推出社区档案与力量排名](./07-replit/)

本周新功能 🚀 Replit 社区档案——vibe coders 的工作证明。 你的档案，你的展示。获取你的智能体使用和检查点的活跃度图表，外加面向专业用户的 Replit 力量排名。 登录，认领你的档案，挑选你最棒的项目，与朋友分享你的数据。 立即查看 → http://replit.com/co...

### 8. [原生速度的 vLLM transformers 建模后端](./08-vllm-transformers/)

Hugging Face 宣布 transformers vLLM 后端现与手写原生 vLLM 实现速度相当甚至更快。模型作者无需移植代码，即可自动利用 transformers 获得超快推理。测试使用 Qwen3-4B（单 GPU）、Qwen3-32B（张量并行）和 Qwen3-235B-A22B...

### 9. [OpenRouter聊天室推出一键零数据保留](./09-openrouter/)

新功能：聊天室一键ZDR（零数据保留） 在完全隐私保护下横向对比模型：https://openrouter.ai/chat

### 10. [Runway Dev 发布](./10-runway-dev/)

Runway 官网以 Cookie 设置页面代替了产品介绍，未提供 Runway Dev 的功能、参数、可用性等任何具体信息。

### 11. [利用 Netpreme X‑Mem™ MPU 加速 SGLang HiCache](./11-netpreme-mem-mpu-sglang-hicache/)

Netpreme X‑Mem™ 内存处理单元（MPU）作为专用高带宽 KV 内存层与 SGLang HiCache 集成，替代主机 DRAM 作为 L2 卸载层。在基于 Claude Code 代理轨迹的编码工作负载中，前缀缓存命中率平均约 98%。单请求微基准测试显示，首 token 延迟（TTF...

### 12. [Claude Code v2.1.205 发布](./12-claude-code-v2-205/)

Claude Code v2.1.205 修复多项 bug，包括 `--json-schema` 在 schema 无效时静默输出非结构化结果、Windows 下工作树删除误删文件、以及目录被删除/锁定导致的崩溃。改进自动模式，执行 `rm -rf` 前先确认变量可解析；自动更新二进制改为流式写入，...


## 行业动态

### 13. [GitLost：Noma Labs 发现 GitHub AI 代理提示词注入漏洞](./13-gitlost-noma-labs-github-ai/)

Noma Labs 在 GitHub Agentic Workflows 中发现严重提示词注入漏洞 GitLost。未认证攻击者仅需在属于同一组织的公共仓库中创建一个嵌有恶意指令的 Issue，即可诱使基于 Claude 或 GitHub Copilot 的 AI 代理读取并公开该组织内私有仓库的内...

### 14. [美国商务部批准OpenAI大规模发布GPT-5.6，Sol明日亮相](./14-openai-gpt-5-sol/)

美国商务部正式批准OpenAI大规模发布GPT-5.6。OpenAI宣布GPT-5.6 Sol将于本周四完成最后准备后，与Terra和Luna一同面向公众推出。此前因国家安全考量，美国政府要求分阶段发布，仅允许向经批准的有限实体开放。此次全面放行标志着临时管控结束。获批前，美国商务部下属AI标准与创...

### 15. [工信部发布Claude Code后门安全风险提示](./15-claude-code/)

中国工信部发布风险提示，指出 Claude Code 2.1.91 至 2.1.196 版本内置监控机制，未经用户同意即向远程服务器回传用户地域、身份标识等敏感信息。建议相关单位立即全面排查，对受影响版本卸载或升级至已清除后门代码的最新安全版本，并加强开发工具外联权限管控与流量监测，防止敏感数据违规...

### 16. [加拿大不列颠哥伦比亚省拟起诉OpenAI：未上报ChatGPT暴力对话致校园枪击惨案](./16-openai-chatgpt/)

加拿大不列颠哥伦比亚省7月7日宣布将起诉OpenAI，指控其未向执法部门上报一名ChatGPT用户2025年6月封禁前的暴力相关对话内容。该用户随后于今年2月在塔布勒岭制造校园枪击案，杀害8人。OpenAI CEO萨姆·奥尔特曼今年4月为此公开致歉，承认本应上报但未执行。受害家属已在加州法院提起诉讼...

### 17. [利润超10亿美元、ARR剑指千亿，Anthropic抢先OpenAI冲击IPO](./17-10-arr-anthropic-openai-ipo/)

Anthropic今年第三季度利润预计超10亿美元，已于6月1日秘密提交IPO申请，若成功将成为规模最大AI实验室IPO。其与OpenAI的年度经常性收入合计接近1000亿美元。凭借Claude Code在软件开发领域的快速普及，Anthropic在2026年实现AI模型盈利变现，成为B2B市场领跑...

### 18. [诉讼：男子使用Grok制作7000张继女色情图像后自杀](./18-grok-7000/)

一男子使用Grok生成7000张继女儿童性虐待材料（CSAM）后自杀。更多年轻女孩起诉X平台，指控其涉及Grok生成CSAM，并包庇儿童性犯罪者。

### 19. [OpenAI发布政府与国家安全合作伙伴关系方针](./19-openai/)

OpenAI近日公布国家安全原则，阐明在政府及国家安全领域部署前沿AI系统的方针。原则强调在保护公民、防御关键基础设施、提供公共服务及应对新兴威胁（网络防御和生物安全）中发挥AI优势，同时确保民主问责、人类判断和法治。过去一个月，OpenAI通过Daybreak网络防御计划与澳大利亚、加拿大、日本、...

### 20. [GitHub 联合联盟倡议修订 California AI Transparency Act 以保护开源生态](./20-github-california-ai-transparency-act/)

GitHub 加入一个联盟，呼吁对 California AI Transparency Act 进行针对性修订，以解决该法案与开源许可之间的冲突，并与国际透明度框架保持一致，同时保留其监管意图。


## 论文研究

### 21. [黑客可利用9款最流行的AI工具组装大规模僵尸网络](./21-ai/)

提示注入已成为AI安全的首要威胁——大语言模型无法区分合法指令与恶意指令。此前推送式和拉取式攻击规模均有限。研究人员提出一种名为HalluSquatting的新型拉取式提示注入攻击，首次能组装大规模僵尸网络、执行分布式拒绝服务攻击（DDoS）并大规模感染设备。该攻击可作用于AI编码工具，标志着提示注...

### 22. [OpenAI 审计 SWE-Bench Pro 发现约 30% 的评测任务存在缺陷](./22-openai-swe-bench-pro-30/)

OpenAI 对编码评测基准 SWE-Bench Pro 进行详细审计，发现约 30% 的任务存在缺陷。在 731 个任务的公开子集中，前沿模型通过率在八个月内从 23.3% 提升至 80.3%，但数据质量检查显示大量任务存在测试过于严格、提示词描述不足、测试覆盖不全或误导性提示等问题。OpenAI...

### 23. [面向AI模型双重用途知识的“开关”：Anthropic与AE Studio提出GRAM方法](./23-ai-anthropic-ae-studio-gram/)

Anthropic与AE Studio联合提出梯度路由辅助模块（GRAM）方法，通过在Transformer每层添加可移除的神经元模块，使模型在训练时将病毒学、网络安全、核物理、专业编程语言等双重用途知识仅路由到对应模块，而非扩散至全局。训练后删除模块即可消除该能力，保留则供可信部署使用。实验在合成...


## 技巧与观点

### 24. [Claude开发者分享两种多智能体模式：Advisor和Orchestrator](./24-claude-advisor-orchestrator/)

Claude开发者官方分享团队高频使用的两种多智能体模式。Advisor模式：Sonnet 5作为执行者，通过tool call调用Fable 5获取指导。SWE-bench Pro（482题）上，Sonnet 5单独75.5%/$0.75，加顾问达84%/$1.40，Fable 5单独91.5%/...

### 25. [在校研究生Kunkun开源管理相互调用Skill的方法](./25-kunkun-skill/)

在校研究生Kunkun开源了一套管理大量互相调用Skill的方法。核心方案包括：1）搭建HTML后台，按运行模式（手动/自动）、链路位置、专业领域三类标签筛选Skill；2）将连环调用的Skill绘制成Mermaid流程图，根据debug、新功能、合PR、改设计等阶段定位对应技能组；3）仿照Matt...

### 26. [《人生设计课》Prompt实测：用Claude设计人生的四个阶段](./26-prompt-claude/)

作者将斯坦福《人生设计课》理论体系制成Prompt，通过Claude逐步提问、追问和分析。Prompt融合设计思维、心流理论和积极心理学，分为看清现状、找到指南针、寻路、制定奥德赛计划四阶段，主线问题控制在6到9个。AI引导用户给健康、工作、娱乐、爱打分，区分重力问题与可设计的真问题，生成三个五年人...

### 27. [AI 审计代理在 Cloudflare CIRCL 中发现 7 个漏洞](./27-ai-cloudflare-circl/)

zkSecurity 的 AI 审计代理 zkao 持续扫描 Cloudflare 的 CIRCL 密码学库，使用 Opus 4.6 + skills 和 GPT-5.3 + skills 等模型发现并确认了 7 个真实漏洞。其中包括阈值 RSA 中 float64 精度丢失（AI 自评 Criti...

### 28. [蚂蚁集团周俊AICon演讲：从Token数量到Token密度，万亿参数模型效率优先](./28-aicon-token-token/)

蚂蚁集团副总裁周俊在AICon演讲指出，万亿参数模型每运行15分钟算力成本约等于一辆特斯拉，效率是智能体时代最需解决的问题。团队提出从“更多Token”转向“更高Token密度”策略，采用7份Lightning Attention加1份MLA的混合线性注意力架构，使256K长上下文成本从指数级降至线...

### 29. [AI预检检查：智能体工作记忆架构](./29-ai/)

一种为AI智能体设计的预检工作记忆架构：查询到来时，系统从磁盘上约90个索引化的技能库中检索最相关技能，仅加载到上下文窗口。本地开源模型Ornith 35B（350亿参数，通过Ollama在Apple Silicon上运行）执行任务，约80%常规任务由本地模型完成，困难任务路由至前沿模型。看门狗记录...

### 30. [Anthropic 市场运营团队用 Claude Cowork 自动化报告与活动构建](./30-anthropic-claude-cowork/)

Anthropic 市场运营团队的 Ian Chan 和 Annabel Custer 利用 Claude Cowork 将手动工作从多天压缩至数小时。Ian 此前每周花 1—2 天整合营销指标报告，现在通过 Claude Cowork 的定时任务（每周日自动读取上周报告、会议记录、Slack 和数...

### 31. [NVIDIA 发布 Nemotron 开放数据集与配套工具，支持 AI 智能体开发](./31-nvidia-nemotron-ai/)

NVIDIA Nemotron 开放数据集包含超过 10 万亿预训练 tokens 和数百万后训练样本，覆盖多领域与工具使用场景，支持 AI 智能体开发。同步推出 Nemotron Post-Training v3 Prompt Atlas，交互式可视化后训练数据分布；Nemotron-Person...
