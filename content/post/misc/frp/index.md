---
author: muioo

title: "【frp】FRP内网穿透P2P远程桌面控制（RDP）"

date: 2026-04-09

description: "frp远程桌面的使用方法"

tags: ["frp"]

categories: ["杂七杂八应用"]
---

## frp下载

链接https://github.com/fatedier/frp/releases/tag/v0.68.0

## 服务器配置

服务器上frps.toml

```toml
bindAddr = "0.0.0.0" #服务端监听的 IP 地址，0.0.0.0表示监听所有网络接口
bindPort = 6000 #指定 FRP 服务端的监听端口，客户端将通过这个端口连接到 FRP 服务端

vhostHTTPPort = 28080 #指定虚拟主机 HTTP 服务监听的端口 
webServer.addr = "0.0.0.0" #指定 FRP Web UI（管理界面）的绑定地址
webServer.port = 7001 #指定 FRP Web UI 的端口号，可以通过 7500 端口访问管理界面，可以设置成别的
webServer.user = "admin" #Web UI 登录所需的用户名，自由设置
webServer.password = "admin123" #Web UI 登录所需的密码，自由设置

log.to = "/frpslog/frps.log" #指定日志输出的文件路径
log.level = "info" #日志的记录级别，info 表示记录一般的信息
log.maxDays = 3 #设置日志文件保留的天数，超过 3 天的日志文件将被自动删除

auth.method = "token" #指定认证方式，token 表示客户端和服务端通过 Token 进行身份认证
auth.token = "abcdef" #Token 用于客户端和服务端的身份认证，自由设置

allowPorts = [
    { start = 6389, end = 6389}, #定义允许客户端使用的端口范围
]

```

服务器需要启动服务配置

```bash
#进入文件
cd /etc/systemd/system
#创建frps.service文件进行配置
vim frps.service
```

写入内容

```bash
[Unit]
Description = frp server # 服务名称，可自定义
After = network.target syslog.target
Wants = network.target
 
[Service]
Type = simple
#启动frps的命令，修改为frps的安装路径
ExecStart = /root/wbl/frp/frp_0.68.0_linux_amd64/frps -c /root/wbl/frp/frp_0.68.0_linux_amd64/frps.toml
 
[Install]
WantedBy = multi-user.target

```

- 注意：服务器需要打开7001、6389、6000三个端口

## 控制端配置（win）

打开frpc.toml文件

```bash
serverAddr = "服务器ip"
serverPort = 6000 #与服务器上的端口一致
auth.token = "abcdef" # 与服务器上的token一致

[transport.tls]
enable = true

[[proxies]]
name = "windows-rdp"
type = "tcp"
localIP = "127.0.0.1"
localPort = 3389
remotePort = 6389
```

在安装路径中打开cmd，执行frpc -c frpc.toml，最好将这个服务设置为开机自启，可以使用nssm