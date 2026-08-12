---
title: "AI日报 | 2026-08-12"
date: 2026-08-12T08:30:00+08:00
description: "2026-08-12 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [NVIDIA 推出 Nemotron 3.5 Lightning，加速本地智能体任务](./01-nvidia-nemotron-lightning/)

NVIDIA 发布 Nemotron 3.5 Lightning，一款可定制的开源 30B 混合专家（MoE）模型，专为常驻智能体设计。相比同类开源模型，其 token 生成速度最高提升 4 倍，任务完成时间缩短 30%。该模型采用开放权重，支持用户微调以匹配特定任务，并可在 RTX PC、DGX ...

### 2. [SGLang 宣布 Day-0 支持 NVIDIA Nemotron 3.5 Lightning](./02-sglang-day-0-nvidia-nemotron-lightning/)

SGLang 宣布对 NVIDIA Nemotron 3.5 Lightning 提供 Day-0 支持，该开源模型为 30B 总参数、3B 激活参数的混合专家架构，支持最长 1M token 上下文，可从 Hugging Face 下载 BF16 和 NVFP4 权重。模型支持 MTP、DFlas...

### 3. [Ling-3.0-tiny 正式开源：1.3B 激活参数如何进入真实任务](./03-ling-3-0-tiny-3b/)

蚂蚁百灵开源 Ling-3.0-tiny，一款总参数 7.9B、推理时仅激活 1.3B 参数的原生混合推理模型，同步提供 BF16、FP8 和 INT4 三个版本。


## 产品发布/更新

### 4. [Runway Seedance 2.5 上线，支持50角色参考](./04-runway-seedance-50/)

完整阵容，完整曲目，一次生成一个。 Seedance 2.5 已在 Runway 上线，支持 50 个独特角色参考，以及最长 30 秒、与音乐同步的片段。点击下方链接即可开始使用。

### 5. [Gemini 助力 Database Migration Service 加速 PostgreSQL 迁移](./05-gemini-database-migration-service-postgr/)

Google Cloud 在 Database Migration Service（DMS）中推出由 Gemini 驱动的 AI 辅助代码转换，可将 Oracle 或 SQL Server 的存储过程、触发器和自定义函数转换为 PostgreSQL PL/pgSQL 代码。

### 6. [ZCode全面升级：Goal、Subagents、Remote Control与闲时任务四大功能上线](./06-zcode-goal-subagents-remote-control/)

ZCode针对GLM深度优化，今日上线Goal、Subagents、Remote Control与闲时任务四大功能。在Z.ai Code Bench测试中，GLM-5.2搭配ZCode较搭配Claude Code任务整体通过率高2.39%；ZCode缓存命中率超98%，叠加1.5倍限时额度加成后，G...

### 7. [ChatGPT 桌面端支持导入其他智能体工作数据](./07-chatgpt/)

你现在可以将其他智能体的工作内容与 ChatGPT Work 和 Codex 保持同步。 可导入项目、聊天记录、技能和插件，查看导入历史，并可在设置中选择开启自动更新。 现已在 ChatGPT 桌面应用中提供。

### 8. [Databricks 开源 Metals v2：面向数百万行代码库的 Java 和 Scala 语言服务器](./08-databricks-metals-v2-java-scala/)

Databricks 开源 Metals v2，这是其面向数百万行代码库的 Java 和 Scala 语言服务器。Metals v2 专为智能体驱动的开发场景设计，旨在提升大规模代码库中的编辑与导航性能。目前 Databricks 的大部分代码已由智能体编写，该工具服务于工程师仍需要手动介入的环节。


## 行业动态

### 9. [研究人员发现可读取ChatGPT等模型加密推理过程的API漏洞](./09-chatgpt-api/)

Alexander Panfilov团队发现OpenAI、Anthropic、Google等主要AI提供商API存在漏洞，可读取推理模型的加密思考过程。扫描约7000条公开会话发现62个API密钥、33个邮箱和33个密码。通过越狱，Anthropic的Haiku 4.5可逐字转写Opus 4.8的原...

### 10. [消息称 Anthropic 最快今年 9 月上市，向投资者淡化 AI 模型竞争等挑战](./10-anthropic-ai/)

Anthropic 正与潜在投资者接触，为可能成为史上规模最大的 IPO 做准备，计划今年 9 月或 10 月初正式上市。公司估值高达 9,650 亿美元，年化收入已超 470 亿美元，并淡化来自中国 AI 企业的竞争影响。Anthropic 还计划拓展 AI 在医疗和生物学领域的应用，但尚未公布具...

### 11. [Gemini月活破10亿，成谷歌增长最快产品](./11-gemini-10/)

每月已有超过 10 亿人使用 @Geminiapp 激发新想法、完成工作。这是我们有史以来增长最快的产品，也是第 14 个达到 10 亿用户里程碑的产品。 感谢 @JoshWoodward 和整个 Gemini 团队，也感谢每一位与我们同行的伙伴——未来还有更多精彩！

### 12. [消息称英伟达开发万亿参数开源 AI 模型 Nemotron 4，目标挑战全球顶级](./12-ai-nemotron/)

英伟达正在研发新一代开源 AI 模型系列 Nemotron 4，规模最大的模型预计至少拥有 1 万亿个参数，旨在与全球最先进的开源模型竞争。英伟达尚未确定发布日期，最终训练也未完成，员工认为该模型最早可能在今年秋末准备就绪。此举意在通过开放模型生态扩大 AI 应用范围，并推动市场对其 GPU 算力的...

### 13. [NVIDIA 为何需要新供电架构以扩展 AI 算力性能](./13-nvidia-ai/)

NVIDIA 主张以 800 VDC 直流配电替代传统交流多次转换，以降低损耗、支撑 AI 算力扩展。NVIDIA 与 Google、Microsoft 通过 OCP 联合制定该架构，已发布白皮书及 LVDC 固态变压器规范 v0.3，超 80 家设备商正据此开发产品。

### 14. [英伟达循环融资达到新高度，黄仁勋是否过度出牌？](./14-cmsoq4td202g/)

英伟达股价在相关消息公布后小幅下滑，收盘报217.55美元，盘前略有回升。金融记者Holger Zschaepitz和曾预测安然倒闭的Jim Chanos均对英伟达的循环融资做法表示担忧。此外，英伟达将发布真正开源（非仅开放权重）的Nemotron模型新版本，这可能最终削弱其合作伙伴OpenAI和A...

### 15. [Electric 加入 Databricks，将 WASM Postgres 引入 AI 智能体沙箱](./15-electric-databricks-wasm-postgres-ai/)

Databricks 宣布 Electric 团队加入，将 WASM Postgres 引入 AI 智能体沙箱。该技术让智能体在隔离环境中运行本地数据库，支持实时数据同步与离线操作，提升构建可靠、可验证智能体应用的效率。Electric 的加入将强化 Databricks 在智能体基础设施领域的布局...


## 论文研究

### 16. [Apple Silicon 与 macOS 虚拟机：借助 Llama.cpp 实现 11–16 倍的 LLM 推理加速](./16-apple-silicon-macos-llama-cpp-11-16-llm/)

研究团队为 macOS 虚拟机中的 Metal 能力查询构建进程级兼容层，使 llama.cpp 能选用更新的 Metal 内核。在 M1 Ultra 上，TinyLlama 1.1B 的提示处理速度提升 11.08 倍、token 生成提升 16.36 倍，接近裸机性能的 98%；Gemma 4 ...

### 17. [统一 Radix 缓存：为混合模型前缀缓存构建单一树结构](./17-radix/)

LMSYS 团队提出 Unified Radix Cache，用单一 token 键控 radix 拓扑统一管理混合模型的 FULL、SWA 和 MAMBA 组件缓存，各组件独立执行路径、滑动窗口和检查点复用语义。

### 18. [AMIE 研究医疗 AI 系统首次展示实时临床视频问诊能力](./18-amie-ai/)

Google Research 与 Google DeepMind 推进医疗 AI 系统 AMIE，实现实时临床视频问诊，首次在此场景展示专家级 AI 能力。该系统基于 Gemini 和 Project Astra 构建，可解读视觉与听觉线索、引导虚拟体格检查并实时诊断推理。随机研究中，临床评估者对...


## 技巧与观点

### 19. [OpenAI 用 Astra 模型攻克 10 道数学难题，数学家既兴奋又担忧](./19-openai-astra-10/)

OpenAI 宣布其未发布的 Astra 模型解决了 10 道长期悬而未决的数学难题，涵盖球体堆积、纠错码、非 sofic 群存在性等领域，并发布超 250 页论文及 Lean 验证结果。

### 20. [用 ComfyUI API 实现 MiniMax-H3 多模态视频与音频生成流水线](./20-comfyui-api-minimax-h3/)

本教程演示如何以 ComfyUI 为无头推理后端，构建端到端的 MiniMax-H3 视频生成工作流。通过 Python 直接构建执行图，支持文生视频、首尾帧条件生成和参考图像条件生成，并自动根据 GPU 显存选择 quality、balanced、squeeze 三种权重配置。流水线涵盖模型自动下...

### 21. [将 GitHub Copilot 置于中间人（MitM）代理之后后，我学到了什么](./21-github-copilot-mitm/)

作者通过 mitmproxy 对 VS Code 中的 GitHub Copilot 进行中间人代理拦截，逆向分析其网络流量与内部架构。文章指出这些 AI 应用普遍基于 Electron 构建，共享相似的网络栈，因此探测结果可迁移至其他同类应用。作者借此揭示了 Copilot 的运行时行为，并分享了...

### 22. [编写智能体时，哪种编程语言最合适？](./22-cmso7i0al0dl/)

针对“动态语言比静态语言更省 LLM token”的流行说法，作者用 GPT-5.6 Sol 让智能体实现 zstd 解码器进行实测。结果显示，medium 努力度下动态语言表现更好，ultra 下静态语言反而更优，且此前评测存在测试路径错误等缺陷。作者认为，琐碎任务上的性能无法推广到更大问题。

### 23. [微信小微AI帮写与AI点评内测：朋友圈最后一点人味正在消失](./23-ai-ai/)

微信基于小微推出朋友圈AI帮写与AI点评内测功能，前者可根据图片和已写文字生成3条朋友圈文案，后者可长按文字生成评价或快捷评论。作者认为这两个功能将AI置于社交核心位置，可能鼓励AI内容、破坏朋友圈自2012年确立的“记录美好生活”基调。公众号端小微还常驻首位，自动总结常看公众号文章，作者担忧这会反...

### 24. [Ryan Greenblatt：人类级AI或于2032年前通过递归自我改进催生失控超级智能](./24-ryan-greenblatt-ai-2032/)

Dwarkesh Patel与Redwood Research首席科学家Ryan Greenblatt探讨递归自我改进（RSI）的可能性：一旦AI达到人类顶级专家水平，可能在一年内实现相当于4-5年的AI进展，Ryan的中位预期是2031年自动化AI研发。双方还讨论了超级智能的对齐对象、奖励黑客行为...

### 25. [每个类别都有赢家：AI 时代 SaaS 龙头的估值溢价](./25-ai-saas/)

SaaS 估值整体承压，但每个细分赛道都跑出了 AI 龙头：CrowdStrike 以 34.4x 前瞻收入领跑安全（中位数 3.9x），Cloudflare 32.6x 对 17.5x，Shopify 11.3x 对 1.4x。
