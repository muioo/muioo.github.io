---
author: muioo

title: "【docker项目部署】服务器部署Docker配置+部署项目"

date: 2026-03-01

description: "记录阿里云Ubuntu服务器上Docker的安装、镜像加速和代理配置"

tags: ["Docker", "服务器部署"]

categories: ["项目部署"]

image: "page.png"

---

# 服务器部署

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

## Docker部署网络图（以知识库项目为例）

![docker网络架构](docker网络架构.png)

## Docker使用

### 常用命令使用

![docker](docker.png)

### 数据库使用

![mysql-docker1](mysql-docker1.png)

```bash
# 进入数据库（mysql为docker创建的mysql名称，建议不要像我这样同名）
docker exec -it mysql mysql -uroot -proot123456
```

docker中的数据库可以看到与宿主机的mysql是隔离的，当前没有映射宿主机端口。

### Dockerfile文件使用

#### 常用关键字



#### 使用案例

- docker-compose.yml（没有创建数据库）

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
    volumes:
      # 挂载本地构建好的 dist 目录（本地构建后直接生效，无需重新构建镜像）
      - ./frontend/dist:/usr/share/nginx/html:ro
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
COPY backend/migrations ./migrations

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
# 生产阶段 - 直接使用本地构建好的 dist 目录
FROM nginx:alpine

# 只复制 nginx.conf，dist 目录通过 docker-compose volumes 挂载
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
```



## 部署流程

- 代码仓库https://github.com/muioo/knowledge-system.git
- 创建数据库

```bash
#!/bin/bash
# 在服务器上运行此脚本初始化数据库

echo "=== 初始化 MySQL 数据库 ==="

# 连接到 MySQL 容器并创建数据库和用户(docker创建的mysql容器名)
docker exec -i mysql mysql -uroot -proot123456 <<EOF
-- 创建数据库
CREATE DATABASE IF NOT EXISTS knowledge_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 创建用户（如果不存在）
CREATE USER IF NOT EXISTS 'knowledge_user'@'%' IDENTIFIED BY 'Knowledge@123';

-- 授予权限
GRANT ALL PRIVILEGES ON knowledge_system.* TO 'knowledge_user'@'%';
FLUSH PRIVILEGES;

-- 显示结果
SHOW DATABASES;
SELECT User, Host FROM mysql.user WHERE User='knowledge_user';
EOF

echo "=== 数据库初始化完成 ==="

```

- 数据库迁移
- 拉取代码

```bash
git clone -b production https://github.com/muioo/knowledge-system.git
```

- 配置.env文件

```bash
# 应用配置
SECRET_KEY=...
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
```

- 构建项目

```bash
docker compose -d build
```

- 后续更新代码

```bash
git pull origin production
docker compose up -d --build backend # 构建镜像 启动容器
docker compose up -d frontend # 启动容器 docker-compose.yml中的frontend
docker compose up -d backend
```





















































