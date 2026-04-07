---
author: muioo

title: "【stm32】项目搭建和FreeRTOS"

date: 2026-02-03

description: "stm32f103rct6开发板"

tags: [ "stm32","FreeRTOS"]

categories: ["开发技术"]

---

## STM32开发笔记

### STM32项目搭建

#### 编译工具

- cmake([安装教程](https://blog.csdn.net/weixin_52677672/article/details/135815928?ops_request_misc=elastic_search_misc&request_id=f41154c1922e9371d6d0ccc6d341e747&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-135815928-null-null.142^v102^pc_search_result_base9&utm_term=cmake%E5%AE%89%E8%A3%85&spm=1018.2226.3001.4187)）

  1、安装后配置环境变量

- ARM-GCC 编译器

  1、[安装链接](https://developer.arm.com/downloads/-/gnu-rm)

  2、配置环境变量，检验安装成功

  ```bash
  arm-none-eabi-gcc -v
  ```

- Ninja构建工具
  
  1、[安装链接](https://github.com/ninja-build/ninja/releases)
  
  2、配置环境变量

#### IDE

- VSCODE
  
  1、安装插件**STM32CubeIDE for Visual Studio Code**
  
  2、安装插件**STM32 VS Code Extension**，这个插件会自动下载**ARM-GCC 编译器**和**ninja构建工具**
  
  3、之后打开项目文件夹即可打开cubemx创建的项目
  
- STM32cubemx（用于创建项目）
  
  1、[下载地址](https://www.st.com/en/development-tools/stm32cubemx.html)
  
  2、[创建教程](https://blog.csdn.net/qq_47902937/article/details/154950893?ops_request_misc=elastic_search_misc&request_id=1e90bb222ec0ebf0b15bd457c34f36ba&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-154950893-null-null.142^v102^pc_search_result_base9&utm_term=stm32cubemx%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE&spm=1018.2226.3001.4187)

#### 烧录工具

- STM32cubeprogrammer

  1、[下载地址]()

- 连接成功演示图

​	{{< figure src="Snipaste_2026-01-31_17-15-55.png" title="连接成功演示" >}}

- [注意事项](http://blog.csdn.net/chenhuanqiangnihao/article/details/113663065?ops_request_misc=elastic_search_misc&request_id=26e57d522f72d9a0151d8dfefcee8244&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-113663065-null-null.142^v102^pc_search_result_base9&utm_term=boot0%E5%92%8Cboot1%E9%85%8D%E7%BD%AE&spm=1018.2226.3001.4187)：烧录时，启动模式得设置为boot0=1，boot1=0，boot0接高电平boot1接GND

#### 串口测试工具

- SSCOM

#### 使用CUBEMX初始化FreeRTOS项目

- <a href="/freertos-tutorial.html">FreeRTOS移植教程</a>

##### FreeRTOS

- 可以理解为并发（多核同时执行多个任务） 不可以理解为并行（需要单核切换来执行多个任务）

##### 代码结构

- 主要开发在core/Src和core/Inc目录中，Src目录中用来写具体功能，Inc定义函数和引脚

```bash
USV_BASE/
├── Core/                          # STM32CubeMX生成（不修改）
│   ├── Inc/
│   │   ├── main.h
│   │   ├── can.h                  # CubeMX配置
│   │   ├── usart.h                # CubeMX配置
│   │   └── ...
│   └── Src/
│       ├── freertos.c             # 任务创建（尽量不要与STM32CubeMX生成的任务代码冲突）
│       ├── can.c                  # CAN中断回调（修改USER CODE区）
│       ├── usart.c                # UART中断回调（修改USER CODE区）
│       └── ...
│
├── App/                           # 应用代码
│   ├── Inc/
│   │   ├── app_config.h           # 系统配置
│   │   ├── app_types.h            # 公共数据类型
│   │   └── app_def.h              # 宏定义
│   │
│   ├── Driver/                    # 驱动层（2个模块）
│   │   ├── Inc/
│   │   │   ├── driver_can_radar.h
│   │   │   └── driver_sbus.h
│   │   └── Src/
│   │       ├── driver_can_radar.c
│   │       └── driver_sbus.c
│   │
│   ├── Algorithm/                 # 算法模块（可选扩展）
│   │   ├── Inc/
│   │   │   └── algo_avoid.h       # 避障算法
│   │   └── Src/
│   │       └── algo_avoid.c
│   │
│   └── Task/                      # 任务层（3个任务）
│       ├── Inc/
│       │   ├── task_radar.h       # 雷达+避障
│       │   ├── task_sbus.h        # SBUS通信
│       │   └── task_control.h     # 控制决策
│       └── Src/
│           ├── task_radar.c
│           ├── task_sbus.c
│           └── task_control.c
│
└── Docs/                          # 文档
    └── ArchitectureDesign_Simple.md
```

- 修改CUBEMX中定义的引脚会自动修改宏定义和引脚

#### 遇到的问题

##### 1、stlink烧录问题

- 使用usb口给开发板供电，解决如下问题

​	{{< figure src="Snipaste_2026-02-03_17-17-03.png" title="ST-LINK烧录问题" >}}

- ST-LINK烧录 
  
  驱动更新：需要重启开发板或断开数据线才能识别
  
- 烧录时要按下reset键 点击连接后松开reset，否则会遇到如下问题

​	{{< figure src="Snipaste_2026-02-03_17-16-40.png"  >}}



