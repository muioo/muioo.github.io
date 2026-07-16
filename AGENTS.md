# 项目目标

- 本仓库是基于 Hugo 的个人博客，内容主要放在 `content/`，静态构建产物放在 `public/`。
- `scripts/ai-daily/` 从 `aihot.virxact.com` JSON API 抓取 AI 日报数据，生成 `content/ai-daily/{date}/_index.md`（日报索引）+ `content/ai-daily/{date}/{NN}-{slug}.md`（单篇详情）+ `data/ai-daily/latest.json`。
- AI 日报日期页以文章形式渲染 `_index.md` 中的分类、标题和摘要；标题链接到单篇详情，顶层 `/ai-daily/` 保留日期归档。
- 自动化脚本应优先保证生成内容稳定、可追踪，失败时输出明确错误信息。
- API 基址可通过 `AIHOT_API_BASE` 环境变量覆盖；HTTP 404 视为当天无数据，正常退出。
- 本地负责编辑普通笔记并推送到 GitHub；服务器负责拉取最新笔记后，只生成并推送 AI 日报相关文件。
- `public/`、`resources/`、`.hugo_build.lock`、运行日志和缓存不提交到仓库，由本地或部署流程按需生成。

# 代码风格 / 命名 / 格式

- Python 脚本使用类型标注，函数名和变量名使用 `snake_case`。
- 每个函数必须有简短中文注释或 docstring，复杂解析逻辑需要补充关键步骤说明。
- 只修改与当前需求直接相关的代码，不做无关重构或格式化。
- 端口、URL、超时、数量等配置优先使用环境变量，避免硬编码业务配置。
- AI 日报抓取使用 `AIHOT_API_BASE`、`AI_DAILY_FETCH_RETRIES`、`AI_DAILY_FETCH_TIMEOUT`、`AI_DAILY_TIMEZONE`、`AI_DAILY_DATE` 配置。
- 导航栏和备用入口必须从 `/ai-daily` 的直接子页面动态选择最新日报日期，不得写死日期，也不得从 `.Site.RegularPages` 选择单条详情。
- 不静默吞掉异常；需要忽略的兼容性错误必须有明确原因，业务错误要记录到错误列表或标准错误。
- 文件超过 300 行时，应优先拆分职责清晰的新文件，而不是继续堆叠逻辑。
- 服务器脚本不得自动提交 `content/post/` 等手写笔记；发现普通源码或笔记有未提交改动时应停止并提示。
- 本地执行 `hugo server` 后，只提交内容和源码文件，不提交 Hugo 生成物。

# 目录结构

- `content/`：Hugo Markdown 内容。
- `content/ai-daily/`：AI 日报生成结果。新结构为 `{date}/_index.md` + `{date}/{NN}-{slug}.md`（branch bundle）；旧 hex2077 文件保留为顶层 `{date}.md` 历史归档。
- `data/ai-daily/`：AI 日报侧边栏和最新数据 JSON。
- `layouts/`：Hugo 模板。
- `layouts/ai-daily/`：AI 日报日期文章视图与顶层归档视图；日期页复用主题文章组件。
- `assets/`：SCSS 等前端源码资源。
- `public/`：Hugo 构建输出，不作为脚本业务逻辑来源。
- `scripts/ai-daily/`：AI 日报抓取、生成和服务器执行脚本。
