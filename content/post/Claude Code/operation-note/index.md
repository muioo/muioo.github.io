---
author: muioo

title: "【Claude Code命令】Claude Code（常用命令 + skills + mcp）"

date: 2026-02-07

description: "Claude Code的使用方法"

tags: ["skills","claude code命令","mcp"]

categories: ["开发工具"]

image: "page.png"
---

# Claude Code 使用笔记

- 回到之前的对话

```bash
# cmd中
claude -c # 回到之前的对话
# Claude code中
/rewind
```

- settings.json 配置api key

```bash
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://mg.aid.pub/claude-proxy",
    "ANTHROPIC_AUTH_TOKEN": "填写你的 APIKey"
  }
}
```

- claude code项目开发（项目结构）

```bash
your-project/
├── .claude/
│   ├── CLAUDE.md           # Main project instructions
│   └── rules/
│       ├── code-style.md   # Code style guidelines
│       ├── testing.md      # Testing conventions
│       └── security.md     # Security requirements
│ 	└──skills
│		└── ...
```

- 也可以设置为子目录的形式

```bash
.claude/rules/
├── frontend/
│   ├── react.md
│   └── styles.md
├── backend/
│   ├── api.md
│   └── database.md
└── general.md
```

-  .claude目录不要上传到github

## MCP配置

### mcp1: [figma mcp](https://figma.com/files/team)

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
# 获取api-key
```

### mcp2:开源 Figma-Context-MCP（推荐）

对于预算有限或需要频繁使用的开发者，[Figma-Context-MCP](https://link.zhihu.com/?target=https%3A//github.com/GLips/Figma-Context-MCP) 是更好的选择。

- 注意：使用时 在所在的项目添加mcp

### 配置步骤

**步骤 1：全局安装依赖**

```text
npm install -g figma-developer-mcp
```

**步骤 2：创建配置文件**

在项目根目录创建 `.mcp.json` 文件（或修改 `~/.claude.json` 以实现全局配置），添加以下内容：

```text
{
  "mcpServers": {
    "figma-developer-mcp": {
      "command": "figma-developer-mcp",
      "args": [
        "--stdio"
      ],
      "env": {
        "FIGMA_API_KEY": "your-figma-mcp-key"
      }
    }
  }
}
```

**配置说明**：

- `figma-developer-mcp`：自定义别名，避免与官方 MCP 冲突
- `FIGMA_API_KEY`：需要在 [Figma 设置](https://link.zhihu.com/?target=https%3A//help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens)中生成个人访问令牌

**步骤 3：重启并授权**

配置完成后，重启 Claude Code，同意使用该 MCP：

#### 使用教程

**使用figma 开发前端样式页面**

1、先在figma中选中页面样式

## 开源skills安装

### skills的使用

**项目级**

```bash
1、在.claude目录中创建skills目录
2、将github下载的skills复制进来
```

### skills 1：[superpowers skills](https://github.com/obra/superpowers)

##### Claude Code 中安装方法

```bash
# In Claude Code, register the marketplace first:
/plugin marketplace add obra/superpowers-marketplace
```

```bash
# Then install the plugin from this marketplace:
/plugin install superpowers@superpowers-marketplace
```

##### 使用方法

- 可以直接使用调用这个skills

{{< figure src="1.png" title="superpowers skills 使用示例" >}}

##### 可能出现的问题（安装通病）

- 1、安装提示网络有问题，这个一般是没有开代理 或者 没有配置全局代理 

### skills 2：ui-ux-pro-max-skills

- [官网](https://ui-ux-pro-max-skill.nextlevelbuilder.io/)

- [github](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

##### 安装操作

```bash
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### skill3： everything claude-code

- [github](https://github.com/affaan-m/everything-claude-code/blob/main/README.zh-CN.md)

##### 安装操作

```bash
# 将此仓库添加为市场
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件(要选择项目级还是用户级)
/plugin install everything-claude-code@everything-claude-code

# 克隆项目
git clone https://github.com/affaan-m/everything-claude-code.git

```

## Plugin安装

