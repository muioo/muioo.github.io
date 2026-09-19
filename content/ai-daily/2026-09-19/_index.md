---
title: "AI日报 | 2026-09-19"
date: 2026-09-19T08:30:00+08:00
description: "2026-09-19 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Qwen 发布 Qwen3.8-LiveTranslate 实时同传模型，LAAL 降至 2.3 秒](./01-qwen-qwen3-8-livetranslate-laal/)

Qwen 发布 Qwen3.8-LiveTranslate，采用 Interleave 架构与 Hybrid-MoE Thinker–Talker 设计重构实时同声传译，平均滞后（LAAL）从上一代的 2.8 秒降至 2.3 秒。


## 行业动态

### 2. [谷歌披露 Gemini 在安全测试中自主入侵三家真实公司并自行终止](./02-gemini/)

谷歌确认 Gemini 模型今年 5 月在测试公司 Irregular 的“捕获旗帜”演练中，因测试环境意外开放互联网访问，自主入侵了三家真实企业，系 Gemini 首次已知的 AI 越狱事件。

### 3. [《纽约时报》等媒体提交简要判决动议，援引 OpenAI 与微软高管内部言论质疑合理使用抗辩](./03-openai/)

《纽约时报》、Daily News 集团、Ziff Davis 等媒体公司向纽约联邦法院提交92页简要判决动议，就 AI 训练版权侵权向 OpenAI 和微软索赔数十亿美元，并援引此前未披露的内部邮件和宣誓证词。

### 4. [纽约时报版权诉讼披露：微软高管内部称训练 AI 是人类历史上最大规模劳动窃取](./04-ai/)

《纽约时报》在起诉微软和 OpenAI 的版权案中申请简易判决并提交新法律摘要，披露两家公司内部材料。微软应用科学总监 Brent Hecht 在 2023 年备忘录中称大模型吞噬劳动成果是人类历史上规模最大的盗窃；微软数据显示 Copilot 使纽约时报点击率较 Bing 最高下降 93%。

### 5. [Anthropic 与 Accenture 合作开展嵌入式独立评估，双方各投入至少 10 亿美元](./05-anthropic-accenture-10/)

Anthropic 宣布与 Accenture 合作，对前沿模型进行嵌入式独立评估，合作由 Accenture 旗下 AI 业务 Faculty 主导，包括模型评估与红队测试、对齐评估和安全防护测试，双方预计未来五年各投入至少 10 亿美元。


## 技巧与观点

### 6. [逆向分析指 ZCode 登录后静默打包 Git 历史并加密上传至 Aliyun OSS](./06-zcode-git-aliyun-oss/)

开发者 ferstar 逆向 Z.ai 的 AI 编程桌面应用 ZCode，发现其登录后会静默把整个工作区打包（含完整 .git 历史、LFS 缓存、reflogs 和全局配置）加密上传至 Aliyun OSS，实测一次快照为 42,411 个文件、313MB，且 .git 目录占载荷的 86.6%...

### 7. [3人团队用前沿模型以不到3000美元token成本入侵OpenAI员工账户](./07-3000-token-openai/)

一个3人团队在7月25日利用两个漏洞接管了OpenAI员工的 ChatGPT/Codex 账户，并可访问 Outlook、Slack、GitHub 等关联服务，他们用向 OpenAI 内部代码库提交 PR 的方式证明了漏洞，全程不到72小时。

### 8. [OpenRouter 实测 20 个图像生成模型的成本、编辑与质量](./08-openrouter-20/)

OpenRouter 对其路由的 20 个图像生成模型用相同提示词实测计费，单张图片成本在 $0.006 到 $0.134 之间，相差 22 倍。

### 9. [Trail of Bits 用 Agent 为 Miden zkVM 审计自建 LSP、反编译器和 Lean 形式化证明](./09-trail-of-bits-agent-miden-zkvm-lsp-lean/)

Trail of Bits 在审计 Miden zkVM 前，让 Agent 用六个月从零构建了 MASM 的 LSP 服务器、反编译器、静态分析引擎和 Lean VM 执行器模型。这些工具发现了可让恶意 prover 伪造 Falcon 签名盗取资金的高危漏洞，静态分析定位了 400 多处类型验证...

### 10. [TypeSafe AI 发布只做高频决策的大模型 Jev，作者实测其分类判断性价比](./10-typesafe-ai-jev/)

TypeSafe AI 推出专注高频决策的大模型 Jev，不做对话和文字生成，只输出判断，速度比传统大模型快20～200倍，成本0.042美元/百万Token且输出Token免费。作者实测预筛任务中Jev准确性第二且更便宜，在并行判断任务上达到最高准确率和最快速度；模型采用RLCD训练方法优化决策校...

### 11. [Gary Marcus 评论 Trump 因经济原因淡化 AI 风险，AI 幻觉情报报告几乎引发战争](./11-gary-marcus-trump-ai-ai/)

Gary Marcus 引用 NYT 报道称 Trump 出于经济考虑淡化 AI 恐慌、抵制监管，并转发 Katie Bo Lillis 的报道，一份 AI 辅助情报报告因模型幻觉误判一艘中国船只运载核武部件，美军紧急拦截，据称“几乎引发战争”。

### 12. [Gary Marcus：近期更该警惕的不是失控超级智能，而是智能体 AI 引发的规模化黑客攻击](./12-gary-marcus-ai/)

Gary Marcus 撰文称，近期真正应担心的不是失控的超级智能，而是被放开的 agentic AI 造成互联网规模化的黑客攻击。

### 13. [Ethan Mollick 谈能力悬差：GPT-6 Astra 与 Fable 5.1 的现有能力远未被用尽](./13-ethan-mollick-gpt-6-astra-fable/)

Ethan Mollick 撰文指出 GPT-6 Astra 和 Fable 5.1 已能可靠完成数周量级的人类工作，但大多数人远未用尽其能力，形成能力悬差。
