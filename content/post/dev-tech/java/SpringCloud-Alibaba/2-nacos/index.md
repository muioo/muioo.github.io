---
author: muioo

title: "【Nacos】Nacos相关使用方法"

date: 2026-08-01

description: "Nacos相关"

tags: ["springboot"]

categories: ["开发技术"]
---

## 1. Nacos 管理服务的位置

Nacos 对业务服务的管理不是通过某个集中的"管理中心"代码实现的，而是通过 **依赖 + 注解 + 配置** 三件套自动完成。

### 1.1 依赖引入

```xml
<!--注册中心客户端-->
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
<!--配置中心客户端-->
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>
```

四个业务服务都引入了两个关键依赖：

| 依赖                                           | 作用                 | 位置示例            |
| ---------------------------------------------- | -------------------- | ------------------- |
| `spring-cloud-starter-alibaba-nacos-discovery` | 服务注册与发现客户端 | `jdyw-auth/pom.xml` |
| `spring-cloud-starter-alibaba-nacos-config`    | 配置中心客户端       | `jdyw-auth/pom.xml` |

这两个依赖由 Spring Cloud Alibaba 提供，引入后框架自动工作，不需要手写注册代码。

### 1.2 注解开关

四个启动类都加了 `@EnableDiscoveryClient`：

| 服务               | 启动类                   | 位置                                                         |
| ------------------ | ------------------------ | ------------------------------------------------------------ |
| `jdyw-auth`        | `JdywAuthApplication`    | `jdyw-auth/src/main/java/com/hlx/jdyw/auth/JdywAuthApplication.java` |
| `jdyw-gateway`     | `JdywGatewayApplication` | `jdyw-gateway/src/main/java/com/hlx/jdyw/gateway/JdywGatewayApplication.java` |
| `jdyw-upms-biz`    | `JdywAdminApplication`   | `jdyw-upms/jdyw-upms-biz/src/main/java/com/hlx/jdyw/admin/JdywAdminApplication.java` |
| `jdyw-upms-moudle` | `JdywApplication`        | `jdyw-upms/jdyw-upms-moudle/src/main/java/com/hlx/jdyw/system/JdywApplication.java` |

### 1.3 配置声明

以 `jdyw-upms-biz/src/main/resources/application-dev.yml` 为例：

```yaml
spring:
  cloud:
    nacos:
      username: @nacos.username@          # 认证
      password: @nacos.password@
      discovery:                          # 服务注册配置
        server-addr: ${NACOS_HOST:jdyw-register}:${NACOS_PORT:28848}
        namespace: 2f7b6bf1-a237-4c3a-9ef7-89a7ff28512f
        group: com.dev
      config:                             # 配置中心配置
        server-addr: ${spring.cloud.nacos.discovery.server-addr}
        namespace: 2f7b6bf1-a237-4c3a-9ef7-89a7ff28512f
        group: com.dev
  config:
    import:                               # 声明从 Nacos 导入哪些配置
      - optional:nacos:application-@profiles.active@.yml
      - optional:nacos:${spring.application.name}-@profiles.active@.yml
```

### 1.4 为什么 Nacos 控制台能看到服务

完整注册链路：

```
1. 启动类 @EnableDiscoveryClient
   ↓ 激活 NacosDiscoveryClient 自动配置
2. Spring Boot 启动时，NacosDiscoveryClient 自动配置生效
   ↓ 读取 spring.cloud.nacos.discovery 配置（server-addr, namespace, group）
3. 服务启动后，Nacos 客户端向 Nacos 服务端发送注册请求
   ↓ POST http://<nacos-host>:28848/nacos/v1/ns/instance
   携带：服务名(jdyw-upms-biz)、IP、端口(23001)、namespace、group
4. Nacos 服务端把实例信息存入 MySQL 的 instance 表
   ↓
5. Nacos 控制台查询 instance 表，展示在「服务列表」页面
   → 就看到了 jdyw-upms-biz、jdyw-auth 等服务
```

服务名来源：`application.yml` 中 `spring.application.name: @artifactId@`，Maven 编译后替换为对应模块的 `artifactId`（例如 `jdyw-upms-biz`）。

---

## 2. 配置如何从 Nacos 作用到代码

配置作用机制分为 **启动时加载** 和 **运行时动态刷新** 两种。

### 2.1 启动时加载（核心机制）

```
1. Spring Boot 启动，读取本地 application.yml + application-dev.yml
   ↓ 激活 dev profile，得到 spring.cloud.nacos.config 配置
2. spring-cloud-starter-alibaba-nacos-config 的自动配置类生效
   ↓ NacosConfigDataLocationResolver
3. 解析 spring.config.import 里的 optional:nacos:xxx.yml
   ↓ 向 Nacos 服务端发请求拉取配置
4. GET http://<nacos-host>:28848/nacos/v1/cs/configs
   ?dataId=application-dev.yml&group=com.dev&tenant=2f7b6bf1-...
   ↓ Nacos 返回 yml 内容
5. 拉取的配置被注入到 Spring Environment
   ↓ 优先级高于本地 application.yml
6. Spring 根据 Environment 中的配置创建 Bean
   ↓ DataSource、Redis、Feign 等 Bean 都使用 Nacos 里的配置
```

关键点：`optional:nacos:` 前缀表示「拉取失败不报错继续启动」，因此配置没拉到时服务可能仍能启动，但缺少配置的 Bean（如 DataSource）创建时会失败。

### 2.2 配置优先级

优先级从高到低：

```
┌─────────────────────────────────────────┐
│ Nacos 的 ${服务名}-dev.yml（私有配置）   │  最高
├─────────────────────────────────────────┤
│ Nacos 的 application-dev.yml（公共配置） │
├─────────────────────────────────────────┤
│ 本地 application-dev.yml                 │
├─────────────────────────────────────────┤
│ 本地 application.yml                     │  最低
└─────────────────────────────────────────┘
```

在 Nacos 修改的配置可以覆盖本地配置，这是 Nacos 配置中心的核心价值。

### 2.3 运行时动态刷新（@RefreshScope）

部分 Bean 支持运行时刷新：在 Nacos 控制台改配置，**无需重启服务**即可生效。

源码示例：

`jdyw-gateway/src/main/java/com/hlx/jdyw/gateway/config/GatewayConfigProperties.java`：

```java
@RefreshScope                          // 关键注解
@ConfigurationProperties("gateway")    // 绑定 Nacos 里 gateway.* 配置
public class GatewayConfigProperties {
}
```

`jdyw-gateway/src/main/java/com/hlx/jdyw/gateway/config/AppProperties.java`：

```java
@RefreshScope
@ConfigurationProperties("rsa")        // 绑定 Nacos 里 rsa.* 配置
public class AppProperties {
}
```

动态刷新链路：

```
在 Nacos 控制台改配置 → 点「发布」
   ↓ Nacos 服务端推送配置变更事件（长轮询）
客户端收到变更通知
   ↓ Nacos 客户端重新拉取配置
Spring 发布 RefreshEvent
   ↓ 销毁带 @RefreshScope 的 Bean
下次访问时重新创建 Bean，使用新配置
   → 配置生效，不用重启
```

注意：只有加了 `@RefreshScope` 的 Bean 才会动态刷新。普通的 `@Value` 注入字段，**需要重启服务**才能生效。

---

## 3. Feign 如何通过 Nacos 完成服务发现

### 3.1 服务名常量

`jdyw-common/jdyw-common-core/src/main/java/com/hlx/jdyw/common/core/constant/ServiceNameConstants.java` 定义了服务名常量：

```java
public interface ServiceNameConstants {
    /** 认证服务的 SERVICE ID */
    String AUTH_SERVICE = "jdyw-auth";
    /** UMPS 模块 */
    String UMPS_SERVICE = "jdyw-upms-biz";
    /** UMPS-业务模块 */
    String UMPS_SERVICE_Moudle = "jdyw-upms-moudle";
}
```

### 3.2 Feign 客户端用服务名调用

Feign 接口不写死 URL，而是通过服务名调用：

```java
@FeignClient(value = ServiceNameConstants.UMPS_SERVICE)  // 用服务名
public interface RemoteUserService { ... }
```

### 3.3 调用链路

```
代码调用 remoteUserService.getInfo()
   ↓ Feign 拦截
Feign 看到 @FeignClient(value = "jdyw-upms-biz")
   ↓ 问 Nacos：jdyw-upms-biz 有哪些实例？
Nacos 返回：[{ip: 127.0.0.1, port: 23001}]
   ↓ LoadBalancer 选一个实例
Feign 发起 HTTP 请求到 http://127.0.0.1:23001/...
   ↓ 目标服务处理
返回结果
```

启动日志中可见的证据：

```
For 'jdyw-upms-biz' URL not provided. Will try picking an instance via load-balancing.
```

含义：Feign 没写死 URL，会通过负载均衡从 Nacos 选择实例。

---

## 4. 三个关键位置总结

| 功能         | 代码位置                                        | 机制                                    |
| ------------ | ----------------------------------------------- | --------------------------------------- |
| 服务注册     | 启动类的 `@EnableDiscoveryClient`               | 自动注册到 Nacos                        |
| 配置拉取     | `application-dev.yml` 的 `spring.config.import` | 启动时从 Nacos 拉取配置注入 Environment |
| 配置动态刷新 | Bean 上的 `@RefreshScope`                       | Nacos 推送变更事件，Bean 重建           |
| 服务发现     | `@FeignClient(value = "服务名")`                | Feign + LoadBalancer 从 Nacos 查实例    |

核心一句话：Nacos 客户端依赖（`nacos-discovery` 和 `nacos-config`）是 Spring Cloud Alibaba 的自动配置组件，引入依赖 + 加注解 + 写配置地址，框架就自动完成注册、拉配置、服务发现，不需要手写注册或拉配置的代码。

---

## 5. 源码索引

### 5.1 启动类（服务注册入口）

```text
qxgz-jdyw-server/jdyw-auth/src/main/java/com/hlx/jdyw/auth/JdywAuthApplication.java
qxgz-jdyw-server/jdyw-gateway/src/main/java/com/hlx/jdyw/gateway/JdywGatewayApplication.java
qxgz-jdyw-server/jdyw-upms/jdyw-upms-biz/src/main/java/com/hlx/jdyw/admin/JdywAdminApplication.java
qxgz-jdyw-server/jdyw-upms/jdyw-upms-moudle/src/main/java/com/hlx/jdyw/system/JdywApplication.java
```

### 5.2 配置文件（Nacos 地址声明）

```text
qxgz-jdyw-server/jdyw-auth/src/main/resources/application-dev.yml
qxgz-jdyw-server/jdyw-gateway/src/main/resources/application-dev.yml
qxgz-jdyw-server/jdyw-upms/jdyw-upms-biz/src/main/resources/application-dev.yml
qxgz-jdyw-server/jdyw-upms/jdyw-upms-moudle/src/main/resources/application-dev.yml
```

### 5.3 动态刷新配置类

```text
qxgz-jdyw-server/jdyw-gateway/src/main/java/com/hlx/jdyw/gateway/config/GatewayConfigProperties.java
qxgz-jdyw-server/jdyw-gateway/src/main/java/com/hlx/jdyw/gateway/config/AppProperties.java
qxgz-jdyw-server/jdyw-common/jdyw-common-xss/src/main/java/com/hlx/jdyw/common/xss/config/JdywXssProperties.java
```

### 5.4 服务发现常量与 Feign

```text
qxgz-jdyw-server/jdyw-common/jdyw-common-core/src/main/java/com/hlx/jdyw/common/core/constant/ServiceNameConstants.java
qxgz-jdyw-server/jdyw-common/jdyw-common-feign/src/main/java/com/hlx/jdyw/common/feign/annotation/EnableJdywFeignClients.java
qxgz-jdyw-server/jdyw-upms/jdyw-upms-api/src/main/java/com/hlx/jdyw/admin/api/feign/
```

---

## 6. 常见问题

### 6.1 Nacos 控制台看不到服务

依次检查：

1. 启动类是否加了 `@EnableDiscoveryClient`。
2. `spring.cloud.nacos.discovery.server-addr` 是否能从宿主机访问（IDEA 启动时需设 `NACOS_HOST=127.0.0.1`）。
3. `namespace` 和 `group` 是否与 Nacos 控制台查看的命名空间一致。
4. Nacos 用户名密码是否正确（`pom.xml` dev profile 的 `@nacos.username@` / `@nacos.password@` 必须与 Nacos 服务端管理员密码一致）。
5. gRPC 端口 `29848` / `29849` 是否可达（Nacos 2.x 客户端依赖 gRPC）。

### 6.2 配置没生效

依次检查：

1. `spring.config.import` 是否包含目标 Data ID。
2. Nacos 控制台中该 Data ID 是否存在于正确的 Namespace 和 `com.dev` Group 下。
3. Maven 是否使用 `dev` Profile 完成资源过滤（`@profiles.active@` 应被替换为 `dev`）。
4. `optional:nacos:` 前缀会让拉取失败不报错，需通过启动日志确认是否真的拉到了配置。

### 6.3 修改 Nacos 配置后不生效

1. 目标 Bean 是否加了 `@RefreshScope`，没加则需要重启服务。
2. 检查 Nacos 控制台发布配置后，业务服务日志是否出现 `RefreshEvent` 相关记录。
3. 部分配置（如 DataSource）即使加了 `@RefreshScope` 也不会动态切换，需要重启。

### 6.4 Feign 提示无可用实例

1. 目标服务是否已启动并注册到 Nacos。
2. Nacos 服务列表中是否有对应服务名的健康实例。
3. 调用方与被调用方的 Namespace、Group 是否一致。
4. 服务名是否与 `ServiceNameConstants` 完全一致。

