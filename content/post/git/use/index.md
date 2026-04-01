---

author: muioo

title: "【Git命令】Git 操作笔记（协作+常用命令）"

date: 2026-01-23

description: "git的使用方法"

tags: ["Git", "版本控制", "多设备协作"]

categories: ["开发工具"]

---

## git操作

- **已有仓库?**

```bash
cd existing_git_repo
git remote add origin https://gitee.com/.../...
# 从仓库中拉取代码到本地
git pull origin master
```

- **更新本地仓库**

```bash
git pull --rebase 仓库地址 [分支名/master] 
```

- **推送到仓库**

```bash
git push [仓库地址] [分支名/master] 
```

要在两台电脑间协作开发（类似公司多设备办公），可以通过 **「主分支 + 功能分支」** 的 Git 分支策略来管理，既保证代码安全，又能顺畅同步。以下是具体步骤：

### 一、分支策略设计（适合个人多设备协作）

参考公司常用的 **「主分支 + 开发分支」** 模式（简单易维护）：

- **`main` 分支**：存放稳定的「已完成功能」代码（相当于生产环境代码）；
- **`dev` 分支**：日常开发的主分支（两台电脑都基于这个分支开发，同步代码）；
- （可选）**临时功能分支**：如果开发单个功能（比如 “订单支付模块”），可以从`dev`切出`feature/pay`分支，完成后合并回`dev`。

### 二、具体操作步骤（两台电脑分别执行）

#### 步骤 1：初始化仓库（第一台电脑）

1. 本地仓库关联远程仓库（已关联可跳过）：

   ```bash
   git remote add origin https://github.com/你的账号/OrderManagementSystem.git
   ```

2. 创建并切换到dev开发分支：

   ```bash
   # 从main分支切出dev分支（首次创建）
   git checkout -b dev
   # 推送dev分支到远程仓库（让第二台电脑能拉取）
   git push -u origin dev
   ```

#### 步骤 2：第一台电脑开发并提交代码

1. 在dev分支修改代码后，提交并推送到远程：

   ```bash
   # 确保当前在dev分支
   git checkout dev
   # 提交代码
   git add .
   git commit -m "完成订单列表页面开发"
   # 推送到远程dev分支
   git push origin dev
   ```

#### 步骤 3：第二台电脑拉取代码并继续开发

1. 克隆仓库（首次操作）：

   ```bash
   git clone https://github.com/你的账号/OrderManagementSystem.git
   cd OrderManagementSystem
   ```

2. 拉取远程的dev分支并切换：

   ```
   # 拉取远程所有分支信息
   git fetch origin
   # 切换到dev分支（自动关联远程dev）
   git checkout dev
   ```

3. 开发后提交代码（和第一台电脑操作相同）:

   ```
   git add .
   git commit -m "优化订单筛选功能"
   git push origin dev
   ```

#### 步骤 4：后续同步代码（两台电脑都要做）

每次开始开发前，**先拉取远程`dev`分支的最新代码**，避免冲突：

```
git checkout dev
git pull origin dev  # 拉取远程最新代码到本地dev
```

### 三、冲突解决（如果出现代码冲突）

如果两台电脑修改了同一文件的同一部分，`git pull`会提示冲突，解决步骤：

1.打开冲突文件，找到类似以下的标记：

```
<<<<<<< HEAD
你本地的代码
=======
远程的代码
```

   ```bash
# 远程分支名
2. 手动修改文件，保留需要的代码，删除冲突标记；
3. 提交解决后的代码：
   git add 冲突文件名
   git commit -m "解决订单列表页面的代码冲突"
   git push origin dev
   ```


### 四、合并主分支代码（合并别人的代码）

场景 dev分支 有人修改了代码，并且测试功能无误  需要在master主分支合并

```bash
# 切换到dev分支 拉取最新提交的代码
git checkout dev
git pull 
# 切换到mster分支 
git checkout master
# 合并代码
git merge dev
```

## git配置代理

```bash
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy https://127.0.0.1:7890
```

{{< figure src="git-note.png" title="Git代理配置" >}}
