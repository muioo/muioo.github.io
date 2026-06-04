# 项目目标

- 本仓库是基于 Hugo 的个人博客，内容主要放在 `content/`，静态构建产物放在 `public/`。
- `scripts/ai-daily/` 负责从来源页面抓取 AI 日报数据，并生成 `content/ai-daily/*.md` 与 `data/ai-daily/latest.json`。
- 自动化脚本应优先保证生成内容稳定、可追踪，失败时输出明确错误信息。
- AI 日报浏览器兜底抓取默认等待 DOM 就绪后，再等待 GitHub 项目链接出现，避免 `networkidle` 被长连接或懒加载误拖超时。
- 本地负责编辑普通笔记并推送到 GitHub；服务器负责拉取最新笔记后，只生成并推送 AI 日报相关文件。
- `public/`、`resources/`、`.hugo_build.lock`、运行日志和缓存不提交到仓库，由本地或部署流程按需生成。

# 代码风格 / 命名 / 格式

- Python 脚本使用类型标注，函数名和变量名使用 `snake_case`。
- 每个函数必须有简短中文注释或 docstring，复杂解析逻辑需要补充关键步骤说明。
- 只修改与当前需求直接相关的代码，不做无关重构或格式化。
- 端口、URL、超时、数量等配置优先使用环境变量，避免硬编码业务配置。
- AI 日报浏览器兜底等待策略使用 `AI_DAILY_BROWSER_WAIT_UNTIL`、`AI_DAILY_BROWSER_CONTENT_TIMEOUT` 和 `AI_DAILY_FETCH_TIMEOUT` 配置。
- 不静默吞掉异常；需要忽略的兼容性错误必须有明确原因，业务错误要记录到错误列表或标准错误。
- 文件超过 300 行时，应优先拆分职责清晰的新文件，而不是继续堆叠逻辑。
- 服务器脚本不得自动提交 `content/post/` 等手写笔记；发现普通源码或笔记有未提交改动时应停止并提示。
- 本地执行 `hugo server` 后，只提交内容和源码文件，不提交 Hugo 生成物。

# 目录结构

- `content/`：Hugo Markdown 内容。
- `content/ai-daily/`：AI 日报生成结果。
- `data/ai-daily/`：AI 日报侧边栏和最新数据 JSON。
- `layouts/`：Hugo 模板。
- `assets/`：SCSS 等前端源码资源。
- `public/`：Hugo 构建输出，不作为脚本业务逻辑来源。
- `scripts/ai-daily/`：AI 日报抓取、生成和服务器执行脚本。
