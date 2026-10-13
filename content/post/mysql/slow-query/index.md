---
author: muioo

title: "【pg慢日志】对于pg优化查询的理解"

date: 2026-10-11

description: "docker拉取pg对于查询操作的优化"

tags: [ "MySql"]

categories: ["数据库"]

---



进入容器

```bash
docker exec -it <容器名或ID> bash  
```

修改配置文件

```bash
vim  /var/lib/postgresql/data/postgresql.conf  
```

添加一下配置

```bash
#慢查询阈值（单位：毫秒）;记录超过10000ms（10秒）的查询  
log_min_duration_statement = 10000  

#日志记录格式（增强可读性）;时间戳、进程ID、用户、数据库名  
log_line_prefix = '%m [%p] %u@%d '  

#确保日志输出到标准输出
log_destination = 'stderr'  

#启动日志收集功能，将日志写入文件
logging_collector = on  

#【可选】自定义日志目录
log_directory = '/var/log/postgresql'  

#【可选】自定义日志文件[可选]
log_filename = 'postgresql-%a.log'  
```

在容器内执行

```bash
su - postgres  
```

```bash
# 容器内执行，进入psql
psql -U postgres
```

然后执行 SQL：

```bash
SELECT pg_reload_conf();
```

宿主机执行一条慢sql语句

```bash
docker exec bbq-postgres su - postgres -c 'pg_ctl reload'  
```

![image-20261011172025320](image-20261011172025320.png)

查看慢日志

```bash
docker logs -f bbq-postgres
```

