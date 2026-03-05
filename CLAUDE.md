# Skills & Tools

- Use the "content-research-writer" skill for all blog writing tasks
- Apply research and citation guidelines from this skill
- Provide section-by-section feedback during drafting

---

## Hugo 博客笔记格式规则

### 新建笔记时必须遵循以下 front matter 格式：

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
| `categories` | 数组格式，填写主分类 | `["工具技巧"]` / `["开发技术"]` |

### 常用分类参考：
- `开发技术` - 编程语言、框架、开发相关
- `工具技巧` - Git、VSCode、部署等工具使用
- `前端开发` - Vue、React 等前端技术
- `后端开发` - Python、后端框架等

### 文件存放规则：
- 路径：`content/post/文章名称/index.md`
- 每篇笔记创建独立目录，目录内包含 `index.md` 文件