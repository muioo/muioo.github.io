---
author: muioo

title: "【Linux应用层开发】文件IO"

date: 2026-05-21

description: "Linux应用层开发，文件IO"

tags: ["Linux应用层开发"]

categories: ["开发技术"]

---

## struct file 结构体逐字段解析

```c
struct file {
    atomic_long_t f_count;          // 文件对象引用计数（核心！）
    struct mutex f_pos_lock;        // 读写位置的互斥锁，多进程/线程读写时保护偏移量
    loff_t f_pos;                   // 当前文件读写偏移位置（光标位置）
    struct path f_path;             // 记录文件路径信息
    struct inode *f_inode;          // 指向磁盘inode（文件本体，存权限、硬链接数、大小）
    const struct file_operations *f_op; // 文件操作函数集：read/write/open/close 等内核实现
    void *private_data;             // 驱动/模块私有数据（设备文件专用）
}
```

1. `f_count` 引用计数
   - 作用：管理`struct file`生命周期
   - 变化：`open()` → +1；`close()` → -1；减到 0 时内核释放该`struct file`
   - 和 inode 硬链接计数**完全独立**：`ls -l`看到的是 inode 计数，不是这个
2. `f_pos` 文件偏移
   - 每个打开的文件 fd，**独立拥有自己的读写位置**
   - 例：两个进程同时`open("io.txt")`，`f_pos`互不干扰；硬链接共享 inode 但独立`struct file`
3. `f_inode` 指向 inode
   - 多个`struct file`可以指向**同一个 inode**（硬链接、多进程打开同一文件）
4. `f_op` 函数集
   - 用户态`read/write`最终调用这里的内核函数，是 Linux 一切文件（普通文件、设备、管道）的统一接口

------

## 文件描述符 fd 核心知识点（用户态重点）

### 1. 标准文件描述符（默认打开）

| fd 值 |     名称      |       作用       |
| :---: | :-----------: | :--------------: |
|   0   | STDIN_FILENO  | 标准输入（键盘） |
|   1   | STDOUT_FILENO | 标准输出（屏幕） |
|   2   | STDERR_FILENO | 标准错误（屏幕） |

### 2. fd 本质

- 是**进程私有的数组下标**，数组叫`files_struct`
- 进程打开文件越多，fd 数字越大（3、4、5…）
- **进程间 fd 相互独立**，A 进程的 fd=3 和 B 进程的 fd=3 毫无关系

### 3. fd、struct file、inode 三者关系

1. 进程 fd → 找到内核`struct file`（1 次 open 对应 1 个）
2. `struct file` → 指向磁盘`inode`（文件本体）
3. 多个 fd 可以指向**同一个 struct file**（父子进程继承）
4. 多个 struct file 可以指向**同一个 inode**（多进程打开同一文件）

------

## 引用计数完整区分

### 1. inode 硬链接计数（磁盘层，`ls -l`第二列）

- 变化：`ln`硬链接 + 1，`rm`删除文件名 - 1
- 减到 0：磁盘文件数据真正删除
- **open/fopen 不改变它**

### 2. struct file 的`f_count`（内核打开计数）

- 变化：`open`+1，`close`-1
- 减到 0：释放内核文件对象
- 例：打开文件后`rm`删除文件名，只要不 close，文件数据还在！

### 3. 进程 fd 引用

- 进程复制 fd（`fork`/`dup`）：`f_count`+1
- 所有 fd 都 close 后，`f_count`归零

------

## 用户态常用系统调用（对应 struct file 操作）

1. `open()`：分配 fd，创建 / 获取`struct file`，`f_count=1`
2. `read/write()`：操作`f_pos`偏移，调用`f_op->read/write`
3. `lseek()`：修改`f_pos`读写位置
4. `close()`：`f_count--`，为 0 则释放 struct file
5. `dup()`：复制 fd，`f_count++`