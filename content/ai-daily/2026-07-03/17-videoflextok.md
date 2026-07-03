---
title: "VideoFlexTok：可变长度粗到细视频分词"
date: 2026-07-03T08:30:00+08:00
description: "VideoFlexTok提出一种可变长度token序列的视频表示方法，采用粗到细结构——首个token捕捉语义和运动等抽象信息，后续token添加精细细节，生成流解码器支持任意token数量的视频重建。相比传统3D网格分词，该结构允许根据下游需求调整token数，在相同预算下编码更长视频。在类别和文..."
category: "论文研究"
source_url: https://machinelearning.apple.com/research/videoflextok
source_name: "Apple Machine Learning Research（RSS）"
external_permalink: https://aihot.virxact.com/items/cmr3rd0l901busl7l11krygj3
comments: false
---

## 摘要

VideoFlexTok提出一种可变长度token序列的视频表示方法，采用粗到细结构——首个token捕捉语义和运动等抽象信息，后续token添加精细细节，生成流解码器支持任意token数量的视频重建。相比传统3D网格分词，该结构允许根据下游需求调整token数，在相同预算下编码更长视频。在类别和文本到视频生成任务中，VideoFlexTok以1.1B参数（5.2B的1/5）达到可比生成质量（gFVD和ViCLIP Score）。训练一个处理10秒81帧视频的文本到视频模型仅需672个token，比同等3D网格分词器少8倍。

## 原文链接

- [Apple Machine Learning Research（RSS）](https://machinelearning.apple.com/research/videoflextok)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmr3rd0l901busl7l11krygj3)
