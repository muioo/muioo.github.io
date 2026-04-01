---
author: muioo

title: "【docker 安装】docker多系统的安装"

date: 2026-03-28

description: "windows、ubutun等系统下docker的安装"

tags: ["Docker","install"]

categories: ["工具安装"]

image: "docker-page.png"


---

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

## Windows安装