# Skills & Tools

- Use the "content-research-writer" skill for all blog writing tasks
- Apply research and citation guidelines from this skill
- Provide section-by-section feedback during drafting

---

## Hugo 博客笔记格式规则

### 新建笔记或者被要求修改笔记格式时必须遵循以下 front matter 格式：

```yaml
---
author: muioo

title: "【分类标签】文章标题"

date: YYYY-MM-DD

description: "文章简短描述"

tags: ["标签1", "标签2"]

categories: ["分类名称"]

---
```

### 格式规范：
| 字段 | 规则 | 示例 |
|------|------|------|
| `author` | 固定值 | `muioo` |
| `title` | 格式：`【分类标签】标题` | `【Git命令】Git 操作笔记` |
| `date` | 格式：`YYYY-MM-DD` | `2026-02-26` |
| `description` | 简短描述（一句话概括） | `记录git的使用方法` |
| `tags` | 数组格式，多个标签用逗号分隔 | `["Git", "版本控制"]` |
| `categories` | 数组格式，填写主分类 | `["工具安装"]` / `["开发技术"]` |

### 常用分类参考：
- `开发技术` - 编程语言、框架、开发相关
- `开发工具` - Git、VSCode等工具的使用命令
- `工具安装` - 软件的安装
- `开发工具问题` - 开发工具问题以及一些密钥破解
- `杂七杂八的应用`- 一些编程外的应用
- `ai编程`- 编程规则、提示词等

### 文件存放规则：
- 路径：`content/post/文章名称/index.md`
- 每篇笔记创建独立目录，目录内包含 `index.md` 

## 当你被要求将图片设置为笔记的封面这个要求时你必须要遵循一下几点

### 文件笔记的封面规则

- 必须要完整展示

```html
 object-fit: contain !important;
```

- 如果图片大小不一样则裁剪或者缩放但是必须要完整展示

