<<<<<<< HEAD
---
author: muioo

title: "【stm32】FreeRTOS实时操作系统1"

date: 2026-04-21

description: "stm32f103rct6开发板实现FreeRtos，使用Tsk进行对比"

tags: [ "stm32"]

categories: ["开发技术"]
---

### FreeRtos

Freertos可以理解为并发，一个cpu快速切换多个任务执行。

### 原生串行代码，独占cpu

```c
int __io_putchar(int ch)
{
    HAL_UART_Transmit(&huart1, (uint8_t*)&ch, 1, HAL_MAX_DELAY);
    return ch;
}

void UART_TASK(){
  uart_time = HAL_GetTick();
  printf("UART OUTPUT,time:%d!!\r\n",uart_time);

}
void ADC_TASK(){
  HAL_Delay(200);
  adc_time = HAL_GetTick();
  printf("ADC GET DATA,time:%d\r\n",adc_time);
  HAL_Delay(300);

}
void KEY_TASK(){
  
  //如果按键被按下
  if (HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_5) == GPIO_PIN_RESET) {
    //消抖
    HAL_Delay(10);
    if (HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_5) == GPIO_PIN_RESET) {
       HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_8);
    }
  
  }

}
void ALL_TASK(){
    UART_TASK();
    ADC_TASK();
    KEY_TASK();
}
```

=======
---
author: muioo

title: "【stm32】FreeRTOS实时操作系统1"

date: 2026-04-21

description: "stm32f103rct6开发板实现FreeRtos，使用Tsk进行对比"

tags: [ "stm32"]

categories: ["开发技术"]
---

### FreeRtos

Freertos可以理解为并发，一个cpu快速切换多个任务执行。

### 原生串行代码，独占cpu

```c
int __io_putchar(int ch)
{
    HAL_UART_Transmit(&huart1, (uint8_t*)&ch, 1, HAL_MAX_DELAY);
    return ch;
}

void UART_TASK(){
  uart_time = HAL_GetTick();
  printf("UART OUTPUT,time:%d!!\r\n",uart_time);

}
void ADC_TASK(){
  HAL_Delay(200);
  adc_time = HAL_GetTick();
  printf("ADC GET DATA,time:%d\r\n",adc_time);
  HAL_Delay(300);

}
void KEY_TASK(){
  
  //如果按键被按下
  if (HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_5) == GPIO_PIN_RESET) {
    //消抖
    HAL_Delay(10);
    if (HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_5) == GPIO_PIN_RESET) {
       HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_8);
    }
  
  }

}
void ALL_TASK(){
    UART_TASK();
    ADC_TASK();
    KEY_TASK();
}
```

>>>>>>> origin/main
