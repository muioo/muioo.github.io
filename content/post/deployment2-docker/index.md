---
author: muioo

title: "【docker项目部署】服务器部署Docker配置+部署项目"

date: 2026-03-28

description: "记录阿里云Ubuntu服务器上Docker的安装、镜像加速和代理配置"

tags: ["Docker", "服务器部署", "Ubuntu"]

categories: ["项目部署","工具技巧"]

image: "docker-page.png"

---

# Docker笔记

- docker总概图

![docker](docker.png)

# 服务器部署

## 阿里云服务器Ubutun上docker安装

- 安装依赖

```bash
apt install -y apt-transport-https ca-certificates curl software-properties-common
```

- 添加阿里云镜像

```bash
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
```

- 更新源

```bash
apt update
```

- 安装docker

```bash
apt install -y docker-ce docker-ce-cli containerd.io
```

- 验证安装成功

```bash
docker --version
```

## 阿里云服务器docker配置镜像加速

- 创建/etc/docker目录

```bash
mkdir -p /etc/docker
```

- 写入镜像地址

```bash
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "https://docker.m.daocloud.io"
  ]
}
EOF
```

- 重启docker

```bash
systemctl daemon-reload && systemctl restart docker
```

## 阿里云服务器为docker配置本地代理

- 创建/etc/systemd/system/docker.service.d文件

```bash
mkdir -p /etc/systemd/system/docker.service.d
```

- 查看文件内容并且写入

```bash
cat > /etc/systemd/system/docker.service.d/proxy.conf << 'EOF'
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7890"
Environment="HTTPS_PROXY=http://127.0.0.1:7890"
EOF
```

- 重启docker

```bash
systemctl daemon-reload && systemctl restart docker
```

- 验证代理是否生效

```bash
systemctl show --property=Environment docker # 出现这个表示成功Environment=HTTP_PROXY=http://127.0.0.1:7890 HTTPS_PROXY=http://127.0.0.1:7890
```

## Docker部署网络图（以知识充电站项目为例）

![docker网络架构](docker网络架构.png)

## Docker使用

### 数据库使用

```mysql
# 进入数据库
docker exec -it mysql mysql -uroot -proot123456
# 创建用户、授权
CREATE DATABASE IF NOT EXISTS knowledge_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'knowledge_user'@'%' IDENTIFIED BY 'Knowledge@123';
GRANT ALL PRIVILEGES ON knowledge_system.* TO 'knowledge_user'@'%';
FLUSH PRIVILEGES;
```

### Dockerfile文件使用

- docker-compose.yml

```yaml
services:
  backend:
    build:
      context: .
      dockerfile: backend/Dockerfile
    container_name: knowledge-backend
    restart: unless-stopped
    env_file:
      - ./backend/.env
    environment:
      DB_HOST: mysql
      DB_PORT: 3306
      DB_USER: knowledge_user
      DB_PASSWORD: Knowledge@123
      DB_NAME: knowledge_system
    volumes:
      - ./backend/uploads:/app/backend/uploads
      - ./logs:/app/logs
    networks:
      - knowledge-net
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8022/health')"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 60s

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: knowledge-frontend
    restart: unless-stopped
    ports:
    # 服务器端口5173 映射 到docker容器内端口80
      - "5173:80"
    depends_on:
      - backend
    networks:
      - knowledge-net

networks:
  knowledge-net:
    driver: bridge
    external: false
```

- backend/dockfile

```dockerfile
FROM python:3.11-slim

# 工作目录设为 /app，backend 代码放在 /app/backend/ 下，保持包路径 backend.main:app
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件并安装（build context 是项目根目录）
COPY backend/requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

# 复制 aerich 配置和迁移文件（需要在 /app 根目录，aerich 从这里读取）
COPY pyproject.toml ./pyproject.toml
COPY migrations ./migrations

# 复制 backend 代码到 /app/backend/
COPY backend ./backend

# 修复 entrypoint.sh 换行符（CRLF -> LF）并设置可执行权限
RUN sed -i 's/\r$//' ./backend/entrypoint.sh && \
    chmod +x ./backend/entrypoint.sh

EXPOSE 8022

ENTRYPOINT ["./backend/entrypoint.sh"]

```

- frontend/dockerfile

```dockerfile
# 构建阶段
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# 生产阶段
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
# 暴露容器内端口80
EXPOSE 80
```

## 部署流程（以下面的知识充电站部署为例）

```bash
# 拉取代码

git clone -b production ...
# 配置.env文件

# 应用配置
SECRET_KEY=y6SB2eNLsr908-QAGUryHRf0V491BhXmYs7-74_MbJs
DEBUG=false

# 数据库配置（连接已有的 MySQL 容器）
DB_HOST=mysql
DB_PORT=3306
DB_USER=knowledge_user
DB_PASSWORD=Knowledge@123
DB_NAME=knowledge_system

# CORS 配置（填写你的服务器 IP 和前端端口）
CORS_ORIGINS=["ip:port"]

# 火山引擎 AI 配置
ARK_API_KEY=

# 前端端口（docker-compose 使用）
FRONTEND_PORT=5173

# 执行
docker compose -d build
```





















































