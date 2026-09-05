---
author: muioo

title: "【Spring Cloud】一个微服务架构框架"

date: 2026-07-06

description: "Spring Cloud Alibaba微服务架构"

tags: ["SpringCloud", "微服务"]
categories: ["Java"]
---

## Spring Cloud 以微服务为核心的分布式系统构建标准

- 这么多小服务，如何管理他们？(服务治理 注册中心 [服务注册 发现 剔除]) nacos
- 这么多小服务，他们之间如何通讯？ feign
- 这么多小服务，客户端怎么访问他们？(网关) gateway
- 这么多小服务，一旦出现问题了，应该如何自处理？ (容错) sentinel
- 这么多小服务，一旦出现问题了，应该如何排错？(链路追踪) skywalking
- 这么多小服务，怎么保证同一组事务一的一致性？seata