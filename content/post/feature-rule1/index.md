---
author: muioo

title: "【功能开发规则】CRC校验算法分析"

date: 2026-03-31

description: "MAVLink v2 协议 CRC 校验算法分析与验证项目说明"

tags: ["MAVLink", "协议分析", "CRC", "嵌入式"]

categories: ["开发技术"]

---

# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此代码仓库中工作时提供指导。

## 设计提示词时要注意数据的处理 

- 尽量不要使用txt的格式读取文件

## 项目概述

这是一个 MAVLink v2 协议 CRC 分析项目。目标是理解和验证 MAVLink 消息帧中使用的 CRC 校验和计算方法。

## 参考资料

- `参考资料.txt` — 包含 MAVLink CRC 文档链接：
  - https://mavlink.io/zh/guide/crc.html#mavlink-crc (CRC 算法详情)
  - https://mavlink.io/zh/guide/serialization.html#crc_extra (CRC_EXTRA 机制)

## 数据说明

- `消息数据.csv` — 捕获的 MAVLink v2 帧及预解析字段。CSV 列包括：
  - 时间, 序号, 帧起始标志, 有效载荷长度, 序列号, 系统ID, 组件ID, 消息ID, 消息名称
  - 帧头信息, 载荷数据, CRC低字节, CRC高字节, CRC校验位, 帧长度, 原始帧数据

## 关键协议细节

- 所有帧使用 MAVLink v2（起始标志 `0xFD`）
- 系统ID = 1，组件ID = 1
- 使用 CRC-16/X.25 算法，在计算校验和之前将特定于消息的 `CRC_EXTRA` 种子字节附加到有效载荷
- CSV 文件使用中文编码（GBK/GB2312）— 使用 pandas/Python 读取时使用 `encoding='gbk'` 或类似编码

## 数据处理指南

编写 Python 脚本分析此数据时：

- 使用 `pd.read_csv(..., encoding='gbk')` 或 `encoding_errors='replace'` 读取 CSV
- 十六进制字段（消息ID、CRC字节、原始帧）以字符串形式存储，带 `0x` 前缀或纯十六进制
- `原始帧数据` 列包含完整的十六进制原始帧 — 可用于端到端验证 CRC 计算