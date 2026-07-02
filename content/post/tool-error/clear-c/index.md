---
author: muioo

title: "【Win11磁盘清理】清理c盘"

date: 2026-07-02

description: "win11清理C:\ProgramData\Microsoft\Windows\CapabilityAccessManager下sqlite缓存文件"

tags: [ "win11 c盘清理"]

categories: ["杂七杂八应用"]

---

## 清理方法

```bash
# 停止camsvc服务
net stop camsvc
# 强制杀掉承载camsvc的svchost进程，释放文件锁
taskkill /f /im svchost.exe /fi "SERVICES eq camsvc"
# 删除超大日志文件
del /f /q "C:\ProgramData\Microsoft\Windows\CapabilityAccessManager\CapabilityAccessManager.db-wal"
del /f /q "C:\ProgramData\Microsoft\Windows\CapabilityAccessManager\CapabilityAccessManager.db-shm"
# 重启服务
net start camsvc
```

