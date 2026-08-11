---
author: muioo

title: "【application】开发环境和生产环境隔离的一些说明"

date: 2026-08-01

description: "配置文件相关"

tags: ["springboot"]

categories: ["开发技术"]

---

Spring Boot 启动时**固定**加载 `application.yaml`,然后**根据激活的 Profile** 再加载对应的 `application-{profile}.yaml`:

Plain Text

```
启动 → 加载 application.yaml (必读)
     ↓
     激活 profile = dev
     ↓
     加载 application-dev.yaml (覆盖/补充同名配置)
```

`application.yaml` 是**公共配置**,`application-dev.yaml` 是**环境特有配置**,两者合并(后者覆盖前者同名 key)。

### 二、Profile 激活方式(3 种)

#### 方式 1:`application.yaml` 里指定(默认 dev)

```yaml
spring:
  profiles:
    active: dev    # 启动时自动加载 application-dev.yaml
```

本地 IDE 直接运行就激活 dev。

#### 方式 2:启动参数覆盖

```bash
# 命令行
java -jar app.jar --spring.profiles.active=prod

# Docker
docker run -e SPRING_PROFILES_ACTIVE=prod app
```

启动参数会**覆盖** `application.yaml` 里的 `active`,所以 Docker 里跑 prod。

#### 方式 3:环境变量

```bash
export SPRING_PROFILES_ACTIVE=prod
java -jar app.jar
```

### 三、本地 vs Docker 怎么分开运行

```
┌─────────────────────────────────────────────────────────────┐
│  本地 IDE 运行                                              │
│  ────────────────                                           │
│  application.yaml:                                          │
│    spring.profiles.active: dev   ← 默认激活 dev             │
│  ↓                                                          │
│  加载 application-dev.yaml                                  │
│    MySQL: 127.0.0.1:3308                                    │
│    Redis: 127.0.0.1:6379                                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Docker 运行                                                │
│  ────────────                                               │
│  docker-compose.yml:                                        │
│    environment:                                             │
│      SPRING_PROFILES_ACTIVE: prod  ← 覆盖为 prod            │
│  ↓                                                          │
│  加载 application-prod.yaml                                 │
│    MySQL: mysql (容器服务名)                                │
│    Redis: redis (容器服务名)                                │
└─────────────────────────────────────────────────────────────┘
```

**关键:同一份 jar 包,只是启动时传入的 profile 不同,加载的配置文件就不同。**

### 四、具体配置示例

#### `application.yaml`(公共)

```yaml
server:
  port: 8081

spring:
  profiles:
    active: dev    # 默认 dev,本地 IDE 直接跑就走这里

mybatis-plus:
  type-aliases-package: com.hmdp.entity
```

#### `application-dev.yaml`(本地开发)

```yaml
spring:
  datasource:
    url: jdbc:mysql://127.0.0.1:3308/hmdp?useSSL=false&serverTimezone=Asia/Shanghai&allowPublicKeyRetrieval=true
    username: root
    password: 123456

redis-node:
  node1:
    host: 127.0.0.1
    port: 6379
    password: redis123
```

#### `application-prod.yaml`(Docker)

```yaml
spring:
  datasource:
    url: jdbc:mysql://mysql:3306/hmdp?useSSL=false&serverTimezone=Asia/Shanghai&allowPublicKeyRetrieval=true
    username: ${MYSQL_USER:root}
    password: ${MYSQL_PASSWORD:123456}

redis-node:
  node1:
    host: redis
    port: 6379
    password: ${REDIS_PASSWORD:redis123}
```

#### `docker-compose.yml`(传参)

```yaml
services:
  backend:
    image: hmdp-backend
    environment:
      SPRING_PROFILES_ACTIVE: prod    # 关键!覆盖为 prod
    depends_on:
      - mysql
      - redis
```