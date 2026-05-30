---
author: muioo

title: "【Ai编程】记录一些常用的skills以及一些ai辅助工具"

date: 2026-05-21

description: "一些常用skills安装"

tags: [ "SKILLS"]

categories: ["Ai编程"]
---

## 开源skills安装（通用可以用于codex）

### skills的使用

**项目级**

```bash
# Claude Code
1、在.claude目录中创建skills目录
2、将github下载的skills复制进来
# Codex
1、在.codex目录中创建skills
2、将github下载的skills复制进来
```

### skills 1：superpowers skills

**[下载地址](https://github.com/obra/superpowers)**

**Claude Code 中安装方法**

```bash
# In Claude Code, register the marketplace first:
/plugin marketplace add obra/superpowers-marketplace
```

```bash
# Then install the plugin from this marketplace:
/plugin install superpowers@superpowers-marketplace
```

##### 可能出现的问题（安装通病）

- 1、安装提示网络有问题，这个一般是没有开代理 或者 没有配置全局代理 

### skills 2：ui-ux-pro-max-skills

**[下载地址](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**

**[官网](https://ui-ux-pro-max-skill.nextlevelbuilder.io/)**

**安装操作**

```bash
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### skill3： everything claude-code

**[下载地址](https://github.com/affaan-m/everything-claude-code/blob/main/README.zh-CN.md)**

**安装操作**

```bash
# 将此仓库添加为市场
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件(要选择项目级还是用户级)
/plugin install everything-claude-code@everything-claude-code

# 克隆项目
git clone https://github.com/affaan-m/everything-claude-code.git

```

### skill4： frontend-design

**[下载地址](https://github.com/anthropics/skills.git)**

**安装操作**

```git
git clone https://github.com/anthropics/skills.git
```

### skill5： awesome-codex-skills

**[下载地址](https://github.com/ComposioHQ/awesome-codex-skills)**

```git
git clone https://github.com/ComposioHQ/awesome-codex-skills.git
```

## 插件

### CodeGraph

**[下载地址](https://github.com/colbymchenry/codegraph)**

```bash
npx @colbymchenry/codegraph
```

