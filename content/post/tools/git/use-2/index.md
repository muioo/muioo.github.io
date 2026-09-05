---
author: muioo

title: "【Git命令】Git协作"

date: 2026-08-07

description: "git的使用方法"

tags: ["Git", "版本控制", "多设备协作"]

categories: ["工具与环境"]
---

## 不直接在 `release` 上开发需求!!!!!!

### 1 `upstream` 的职责

`upstream` 表示团队正式仓库，主要用于：

- 获取团队成员已经合并的最新代码。
- 获取正式的公共分支。
- 作为创建个人开发分支时的基线来源。
- 作为合并请求的目标仓库。

日常开发中，建议把 `upstream` 当作“团队代码的权威来源”。

一般情况下，不直接向 `upstream/release` 推送代码。

### 2 `origin` 的职责

`origin` 表示个人仓库，主要用于：

- 保存自己的开发分支。
- 备份尚未合并的工作。
- 向 GitLab 提供合并请求的源分支。
- 同步个人仓库中的 `release` 镜像。

### 3 开发基本流程

总览

```text
upstream/release
       │
       │ 创建个人分支
       ▼
feature/姓名或账号/需求编号-描述
       │
       │ 提交并推送
       ▼
origin/feature/姓名或账号/需求编号-描述
       │
       │ GitLab Merge Request + 代码审查
       ▼
团队指定目标分支，通常为 upstream/release 或指定版本分支
```

#### 4 同步

```bash
# 1. 先同步 upstream 最新代码（不要直接在 release 上改）
git fetch upstream
git checkout release
git merge upstream/release        # 或 git rebase upstream/release
git push origin release           # 让你 fork 的 origin 也保持最新

# 2. 基于最新 release 拉一个特性分支干活
git checkout -b feature/xxx release

# 3. 本地修改、提交
git add <files>
git commit -m "feat: xxx"

# 4. 推送到自己的 origin
git push origin feature/xxx

# 5. 去 GitHub/GitLab 网页上向 upstream 发 PR
#    target: upstream/release  ←  source: origin/feature/xxx
```

### 5 一些常用命令

```bash
# 看 upstream 主干到底叫什么
git remote -v
git ls-remote --heads upstream

# 看 origin 上有哪些分支（fork 时可能带过来一个没用的 master）
git ls-remote --heads origin

git checkout main
git merge --no-ff feature/xxx -m "merge: 合并xxx功能"
```

