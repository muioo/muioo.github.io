---
author: muioo

title: "【stm32】基于CubeMx的cmake项目开发规则"

date: 2026-06-01

description: "stm32开发规则"

tags: [ "STM32"]

categories: ["嵌入式"]
---

### 一、命名规范体系

#### 1.1 变量/函数命名

```c
// 好的示例
uint32_t sensor_raw_value;      // 小写下划线，名词结构
void adc_calibration(void);     // 动词+名词结构
GPIO_TypeDef* led_gpio_port;    // 类型标识明确

// 需避免的反例
int a;                          // 无意义命名
void func1();                   // 信息缺失
```

#### 1.2 宏定义规范

```c
#define ADC_SAMPLE_TIMES    (100)       // 全大写+下划线
#define BYTE_TO_BITS(x)     ((x)*8)     // 带参数的宏用括号包裹
#define IS_VALID_CHANNEL(c) ((c)>0 && (c)<16)
```

#### 1.3 类型定义

```c
typedef enum {
    LED_STATE_OFF = 0,
    LED_STATE_ON,
    LED_STATE_BLINK
} led_state_t;                  // _t类型后缀

typedef struct {
    GPIO_TypeDef* port;
    uint16_t pin;
    uint8_t active_level;
} gpio_config_t;                // 配置结构体
```

### 二、代码结构组织

```bash
 APP/
  ├── Inc/                     		#   全局类型和配置
  │   │   ├── config.h              #     系统常量（距离阈值、扇区参数、CAN ID）
  │   │   └── types.h               #     全局类型定义
  ├── Drivers/      			 	# 第2层：驱动/算法（纯逻辑，不含FreeRTOS任务）
  │   ├── Inc/
  │   │   ├── callback.h			# 中断服务函数的编写
  │   │   └── debug_print.h			# 串口调试打印
  │   └── Src/
  │   │   ├── callback.c
  │   │   └── debug_print.c
  └── Task/          				# 第3层：FreeRTOS任务（使用Drivers，运行在RTOS之上）
      ├── Inc/
      └── Src/
 Src/                          # STM32CubeMX生成的HAL层代码
 Inc/                          # STM32CubeMX生成的头文件
 Drivers/ 					   # STM32 HAL库（第三方驱动）
 Docs/                         # 项目文档
 Middlewares/ 				   # 第三方中间件
```

