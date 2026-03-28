---
author: muioo

title: "【docker项目部署】服务器部署Docker配置+部署项目"

date: 2026-03-28

description: "记录阿里云Ubuntu服务器上Docker的安装、镜像加速和代理配置"

tags: ["Docker", "服务器部署", "Ubuntu"]

categories: ["项目部署"]

---

# Docker笔记



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































































