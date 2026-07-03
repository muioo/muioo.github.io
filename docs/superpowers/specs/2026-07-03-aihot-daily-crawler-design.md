# aihot.virxact.com 日报爬虫重写设计

- 日期: 2026-07-03
- 作者: wangbanglei + Claude
- 状态: 待实施

## 背景与目标

现有 `scripts/ai-daily/fetch.py` 抓取 `hex2077.dev` 的 GitHub 开源 TOP 项目，输出 `content/ai-daily/{date}.md` 单文件 + `data/ai-daily/latest.json`。该脚本 472 行，超过项目单文件 200 行限制，且依赖 Playwright 浏览器兜底抓取 HTML，复杂度高。

用户决定将数据源切换为 `aihot.virxact.com`，该站点提供干净的 JSON API（`/api/public/daily?date=YYYY-MM-DD`），返回结构化的 AI 日报内容（`sections[].items[]`，每个 item 含 `title/summary/sourceUrl/sourceName/permalink`）。

**目标**：

1. 替换数据源为 `aihot.virxact.com`，删除 HTML 解析与 Playwright 兜底代码
2. 每篇内容生成独立 md 文件，按日期分目录存放（Hugo branch bundle 结构）
3. 保留每日索引页与 `latest.json`，兼容现有 Hugo 主题
4. 保留服务器 cron 调度方式（不启用 GitHub Actions cron）
5. 单文件不超过 200 行，模块边界清晰

## 非目标

- 不启用 GitHub Actions 定时调度
- 不删除旧 hex2077 历史日报文件（保留为历史归档）
- 不新增 pypinyin 等第三方依赖（保持纯 stdlib）
- 不修改 Hugo 主题或 `latest.json` 数据结构

## 架构

### 模块拆分

```
scripts/ai-daily/
├── fetch.py              # 主入口，编排：取日期→拉数据→生成md→更新latest.json
├── aihot_client.py       # API 客户端：HTTP GET + 重试 + JSON 校验
├── markdown_builder.py   # Markdown 生成：日报索引页 + 单篇详情页
├── latest.py             # data/ai-daily/latest.json 重建
└── run-on-server.sh      # 服务器 cron 调用入口（无需修改）
```

### 模块职责

| 模块 | 输入 | 输出 | 行数估计 |
|---|---|---|---|
| `fetch.py` | env vars | 副作用：写 md + json | ~80 |
| `aihot_client.py` | `date` | `dict`（API 响应） | ~60 |
| `markdown_builder.py` | `date`, `sections` | `str`（日报md）, `list[(filename, md)]` | ~120 |
| `latest.py` | 无 | 副作用：写 latest.json | ~40 |

### 删除的旧代码

- `HexTopProjectParser`（HTML 解析器，JSON API 不需要）
- `fetch_source_html_with_browser`、`dismiss_global_notification`、`wait_for_browser_project_links`（Playwright 相关）
- `is_blocked_page`、`is_project_title_strong`（HTML 启发式判断）
- `BROWSER_HEADERS`、`BROWSER_FALLBACK`、`BROWSER_WAIT_UNTIL` 等浏览器配置常量
- `fetch_projects_with_browser_fallback`、`browser_fallback_error`

## 数据流

```
1. fetch.py main()
2.   → get_target_date()              # AI_DAILY_DATE 覆盖 / 否则 Asia/Shanghai 当天
3.   → aihot_client.fetch_daily(date) # GET https://aihot.virxact.com/api/public/daily?date=YYYY-MM-DD
4.   ← {"date":..., "sections":[{"label":"产品发布/更新","items":[...]}, ...]}
5.   → markdown_builder.build_item_pages(date, sections)
       ← [("01-ai-alipay.md", "...md content..."), ...]
6.   → markdown_builder.build_daily_index(date, sections)
       ← "...md content..."（用作 _index.md）
7.   → 写文件：
       content/ai-daily/{date}/_index.md         # 日报索引（branch bundle）
       content/ai-daily/{date}/{index}-{slug}.md # 每篇详情
8.   → latest.rebuild()                          # 扫描日期目录重建 latest.json
9.   ← data/ai-daily/latest.json
```

## 输出目录结构（Hugo branch bundle）

```
content/ai-daily/
├── _index.md                       # 顶层 section index（已存在，不动）
├── 2026-07-03/                     # 日期目录 = branch bundle
│   ├── _index.md                   # 日报索引页（当天总览）
│   ├── 01-ai-alipay.md             # 单篇详情页
│   ├── 02-google-health-api-cli-ghealth.md
│   ├── 03-senior-swe-bench.md
│   └── ...
├── 2026-07-02/
│   ├── _index.md
│   └── ...
├── 2026-05-15.md                   # 旧 hex2077 历史文件（顶层单文件，保留）
└── ...
```

**为什么用 branch bundle**：Hugo 中 `{date}.md` 与 `{date}/` 目录共存会把目录内文件当作 leaf bundle 资源（不渲染为独立页面）。改用 `{date}/_index.md` 让目录成为 branch bundle，目录内每个 `.md` 都渲染为独立页面。

**URL 结构**：
- 日报索引：`/ai-daily/2026-07-03/`
- 单篇详情：`/ai-daily/2026-07-03/01-ai-alipay/`

## Markdown 模板

### 单篇详情页

路径：`content/ai-daily/{date}/{index}-{slug}.md`

```markdown
---
title: "AI 版支付宝开放公测，蚂蚁阿宝无需邀请码即可体验"
date: 2026-07-03T08:30:00+08:00
description: "支付宝阿宝 AI 助手今日正式开放公测，iOS 和安卓用户..."
category: "产品发布/更新"
source_url: https://www.ithome.com/0/971/469.htm
source_name: "IT之家（RSS）"
external_permalink: https://aihot.virxact.com/items/cmr2x7ii20c2jsl8zygz5iw9n
comments: false
---

## 摘要

支付宝阿宝 AI 助手今日正式开放公测，iOS 和安卓用户可在应用商店...

## 原文链接

- [IT之家（RSS）](https://www.ithome.com/0/971/469.htm)
- [AI HOT 详情页](https://aihot.virxact.com/items/cmr2x7ii20c2jsl8zygz5iw9n)
```

**frontmatter 字段说明**：
- 不设 `slug`：让 Hugo 用文件名生成 URL，避免文件名与 URL 不一致
- `category`（非 `section`）：避免与 Hugo 内置 `section` 概念冲突
- `external_permalink`：原文在 aihot.virxact.com 的详情页 URL（非 Hugo 内部 permalink）
- `description`：截断到 150 字符（SEO 最佳实践）

### 日报索引页

路径：`content/ai-daily/{date}/_index.md`

```markdown
---
title: "AI日报 | 2026-07-03"
date: 2026-07-03T08:30:00+08:00
description: "2026-07-03 AI 热点日报"
comments: false
---

## 产品发布/更新

### 1. [AI 版支付宝开放公测…](./01-ai-alipay/)

支付宝阿宝 AI 助手今日正式开放公测，iOS 和安卓用户...

### 2. [Google Health API 推出 CLI…](./02-google-health-api-cli-ghealth/)

ghealth 是一款封装 Google Health API v4 的开源命令行工具...

## 论文/研究

### 1. [Senior SWE-Bench…](./03-senior-swe-bench/)

Senior SWE-Bench 是一个开源基准测试...
```

**链接格式**：`./{filename-without-ext}/`（Hugo 默认 URL 结构，相对路径）。

## slug 生成算法

零依赖，纯 stdlib 实现：

```python
def slugify(title: str, permalink: str) -> str:
    """从标题提取 ASCII 词作为 slug，纯中文标题回退到 permalink ID 前缀。"""
    # 1. 提取所有 ≥2 字符的 ASCII 串（字母/数字/连字符）
    # 2. 小写、用 - 连接
    # 3. 截断到 40 字符
    # 4. 若为空（纯中文标题），取 permalink 末段 ID 的前 12 字符
```

**示例**：

| 标题 | 文件名 |
|---|---|
| AI 版支付宝开放公测… | `01-ai.md` |
| Google Health API 推出 CLI: ghealth… | `02-google-health-api-cli-ghealth.md` |
| Senior SWE-Bench：评估AI智能体… | `03-senior-swe-bench.md` |
| 昆仑万维天工3.2发布Skywork Tags… | `04-skywork-tags-3-2.md` |
| （纯中文标题） | `05-cmr3uklx8008.md` |

**冲突处理**：同日内 slug 重复时追加 `-2`、`-3`。

## 配置

### 环境变量

| 变量 | 默认值 | 用途 |
|---|---|---|
| `AI_DAILY_TIMEZONE` | `Asia/Shanghai` | 计算目标日期用的时区 |
| `AI_DAILY_DATE` | （空） | 覆盖目标日期，格式 `YYYY-MM-DD` |
| `AIHOT_API_BASE` | `https://aihot.virxact.com` | API 基址（避免硬编码 URL） |
| `AI_DAILY_FETCH_RETRIES` | `4` | HTTP 重试次数 |
| `AI_DAILY_FETCH_TIMEOUT` | `30` | HTTP 超时秒数 |
| `AI_DAILY_MAX_ITEMS` | `50` | 单日 item 上限（防止异常数据爆盘） |

### 删除的旧变量

- `AI_DAILY_BROWSER_FALLBACK`
- `AI_DAILY_BROWSER_WAIT_UNTIL`
- `AI_DAILY_BROWSER_CONTENT_TIMEOUT`
- `AI_DAILY_BROWSER_DISMISS_TIMEOUT`

## 错误处理

| 场景 | 行为 | 退出码 |
|---|---|---|
| API HTTP 404 | 打印 "No source data for {date}, skipped." | 0 |
| API HTTP 5xx / 网络错误 | 重试 4 次，指数退避；全失败后打印错误到 stderr | 1 |
| JSON 解析失败 | 记录错误到 stderr | 1 |
| `sections` 为空 | 打印警告，不写文件 | 0 |
| 单个 item 缺 `title` 或 `summary` | 跳过该 item，记录警告，继续处理其他 | 0 |
| 文件写入失败 | 抛异常（禁止静默异常） | 1 |

## `latest.json` 重建逻辑

`latest.py` 中的 `rebuild_latest_json()` 同时扫描：
- 顶层 `*.md` 文件（兼容旧 hex2077 历史文件，如 `2026-05-15.md`）
- 顶层日期目录（如 `2026-07-03/`，新结构）

```python
entries = []
# 扫描旧结构：顶层 YYYY-MM-DD.md 文件
for path in CONTENT_DIR.glob("*.md"):
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", path.name):
        entries.append({"date": path.stem, ...})
# 扫描新结构：YYYY-MM-DD/ 目录
for path in CONTENT_DIR.iterdir():
    if path.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", path.name):
        entries.append({"date": path.name, ...})
# 去重 + 按日期降序 + 取前 7
```

输出 JSON 结构不变：

```json
{
  "updated_at": "2026-07-03T08:00:00Z",
  "days": [
    {"date": "2026-07-03", "title": "AI日报 | 2026-07-03", "url": "/ai-daily/2026-07-03/"},
    ...
  ]
}
```

## 旧文件迁移

- 旧 hex2077 日报文件（`content/ai-daily/2026-05-15.md` ~ `2026-06-30.md` 等）保留为历史归档
- 新脚本运行时，若目标日期的 `{date}/` 目录已存在，**覆盖** `_index.md` 与单篇 md（同日重跑场景）
- 先清理 `{date}/` 目录内旧的单篇 md（防止已删除的 item 残留），再写新文件
- `run-on-server.sh` 中 `git clean -fd -- content/ai-daily` 已能递归清理子目录中未跟踪文件，无需修改

## 测试用例

| 用例 | 输入 | 期望 |
|---|---|---|
| 正常抓取 | `AI_DAILY_DATE=2026-07-03` | 生成 `{date}/_index.md` + `{date}/*.md` + 更新 latest.json |
| 日期不存在 | `AI_DAILY_DATE=2025-01-01` | HTTP 404，不写文件，退出码 0 |
| 网络失败 | 模拟断网 | 重试 4 次后退出码 1 |
| sections 为空 | mock 返回 `{"sections":[]}` | 不写文件，退出码 0，打印警告 |
| item 缺 summary | mock 一个 item 无 summary | 跳过该 item，其他正常处理 |
| slug 冲突 | 两个 item ASCII 部分相同 | 第二个追加 `-2` |
| 旧文件保留 | 既有 `2026-05-15.md` | 不动旧文件 |
| 同日重跑 | `AI_DAILY_DATE=2026-07-03` 跑两次 | 第二次覆盖第一次结果，无残留旧 item |
| latest.json 兼容 | 既有旧 md 又有新目录 | 两者都出现在 latest.json，按日期降序 |

测试方式：`pytest` + mock API 响应，置于 `scripts/ai-daily/test_fetch.py`。暂不强制加 CI，先确保脚本可手动测试。

## 实施步骤概览

1. 新建 `scripts/ai-daily/aihot_client.py`：API 客户端（fetch_daily + 重试）
2. 新建 `scripts/ai-daily/markdown_builder.py`：Markdown 生成器（slugify + build_item_pages + build_daily_index）
3. 新建 `scripts/ai-daily/latest.py`：`latest.json` 重建逻辑（兼容旧 md + 新目录）
4. 重写 `scripts/ai-daily/fetch.py`：主入口，仅编排，删除所有 HTML/Playwright 代码
5. 验证：手动跑 `AI_DAILY_DATE=2026-07-03 python scripts/ai-daily/fetch.py`
6. 检查生成的 md 文件结构、`latest.json` 内容、Hugo 是否能正常构建
7. 更新 `AGENTS.md` 与项目 CLAUDE.md 中关于新源、新目录结构的说明
8. 提交并推送，让服务器 cron 自动接管

## 风险与权衡

- **slug 可读性**：纯中文标题会回退到 ID 前缀，可读性一般；但序号保证了排序，且零依赖。若未来可读性不足，再加 pypinyin
- **旧文件共存**：新旧文件混在 `content/ai-daily/` 顶层，可能让访客困惑。可接受，因为旧文件是已发布内容
- **API 限流**：`aihot.virxact.com` 未文档化限流策略。重试间隔已设为指数退避（3s/6s/12s/24s），降低被限流概率
- **API 变更**：JSON 结构若变化，脚本会失败。需关注上游 API 稳定性
- **同日重跑覆盖**：先清理 `{date}/` 目录会删除任何手动添加的内容。可接受，因为该目录是自动生成的
