---
title: "AI日报 | 2026-09-21"
date: 2026-09-21T08:30:00+08:00
description: "2026-09-21 AI 热点日报"
comments: false
---

## 模型发布/更新

### 1. [Qwen 开源 Qwen-Image-2.1：7B 统一生成与编辑并原生支持透明图像](./01-qwen-qwen-image-2-7b/)

Qwen 团队开源 Qwen-Image-2.1，将文生图与图像编辑统一到一个模型中，视觉生成组件仅 7B 参数，并原生支持生成和编辑透明图像。模型支持最多 10 张参考图、圆形/涂鸦/独立蒙版指定局部编辑，通过混合粒度注意力架构和 KV cache 复用提升推理效率，同时改进文字渲染、人像光照与人...

### 2. [阶跃星辰发布旗舰模型 Step 5 Preview，10 月 15 日开源权重](./02-step-preview-10-15/)

阶跃星辰发布旗舰基座模型 Step 5 Preview，采用稀疏 MoE 架构，总参数量 600B、激活 27B，支持 100 万 Token 上下文和文本与视觉输入，在 Artificial Analysis Intelligence Index 得 44 分，居全球开源模型前三，单任务成本为 C...


## 产品发布/更新

### 3. [Qwen-Image-2.1 已支持 ComfyUI，开源权重开放下载](./03-qwen-image-2-comfyui/)

Qwen 宣布 Qwen-Image-2.1 现已支持 ComfyUI，权重开放。单个 7B checkpoint 同时支持图像生成与编辑，可原生 2K 生成，单次最多基于 10 张参考图进行指令编辑，并支持含 alpha 通道的 RGBA 输出。


## 论文研究

### 4. [独立调查：ChatGPT 的 __obi 跨站 Cookie 可将站外浏览行为关联到 ChatGPT 账号](./04-chatgpt-obi-cookie-chatgpt/)

作者通过自己手机上的流量捕获复现了 OpenAI 广告收集器机制：bzr.openai.com 在 .openai.com 域设置 __obi Cookie，绑定 ChatGPT 账号（或稳定的匿名主体），投放广告的商家站点加载 OpenAI 像素代码时会把 __obi 连同浏览和购买数据回传给 O...
