---
author: muioo

title: "【爬虫基本方法】爬虫request基本框架 + scrapy框架 + crawl4ai"

date: 2026-02-14

description: "爬虫基本方法"

tags: ["爬虫"]

categories: ["开发技术"]

---

## 爬虫基本框架

### 发送请求

#### 以b站评论区为例子

1、找到对应的数据包

{{< figure src="1.png" title="找到目标数据包" >}}

2、应对反爬

{{< figure src="2.png" title="处理反爬" >}}

```python
headers = {
    "cookie":"buvid3=7178F649-B51E-3511-52F3-F35BBADC24AD07347infoc; b_nut=1766219807; _uuid=7885107F6-10532-5A53-3DE1-49762D4BF86A89782infoc; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; buvid4=D98C240B-1FA4-8D02-C9B3-DD7693AFC8DF90828-025122016-lD92PdnjNqMMVtStsO1Yaw%3D%3D; rpdid=|(J|lmkkkuJ|0J'u~YYkkul~u; DedeUserID=123152920; DedeUserID__ckMd5=14a440f25b863dcc; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; CURRENT_QUALITY=0; PEA_AU=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiaWQiOjEyMzE1MjkyMCwicGlkIjozNzUyOTM4LCJleHAiOjE4MDIyNzAyMzAsImlzcyI6InRlc3QifQ.-Ki8KKoVKdTUYDeIL6zR10rl5t-RlYiDsIiLLJjK3ik; fingerprint=a4e5b37b8876bfe9b2ac49851b255d83; buvid_fp_plain=undefined; buvid_fp=a4e5b37b8876bfe9b2ac49851b255d83; bsource=search_bing; bp_t_offset_123152920=1167965937526112256; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzEwMzc2MjMsImlhdCI6MTc3MDc3ODM2MywicGx0IjotMX0.YmqjaqFACN6HQkPvqSSujttyA0mmbQgrWYeHlb2Bhbg; bili_ticket_expires=1771037563; SESSDATA=8a9db992%2C1786523177%2C39356%2A21CjByGR1LZxP1_8VO6q6NMNeD7uaHBtFysH7X6KMHQD7BNzjXNZn8xey1B5Kzzpt74q0SVm14c1U4VkpZMUhkYl9uNnpjZGMyUmNibnc2NUs2eUdMS0kzSlZRT3hMOU1WZGR4ckJjMmx5NGwwcHZnVlBESnFQRkp3TWpSdUoyb3NLSndxUnBEOU9RIIEC; bili_jct=3900ae6a5e204b3a0afb02e5dbbb4a40; home_feed_column=5; browser_resolution=1536-695; sid=4j8dvybo; CURRENT_FNVAL=4048; b_lsid=C0839A2E_19C56CDB713",
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
# get 查询参数
data = {
    'spm_id_from' : '333.337.search-card.all.click',
    'vd_source' : '18d0a338800faafff98255fb11dc47ba'
}

```

3、发送请求

```python
response = request.get(url=url,params=data,headers=headers)
```

### 解析数据

- json_data 字典取值

```python
import requests


url = "https://www.bilibili.com/video/BV1K9Hse8EwM/?spm_id_from=333.337.search-card.all.click&vd_source=18d0a338800faafff98255fb11dc47ba"

headers = {
    "cookie":"buvid3=7178F649-B51E-3511-52F3-F35BBADC24AD07347infoc; b_nut=1766219807; _uuid=7885107F6-10532-5A53-3DE1-49762D4BF86A89782infoc; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; buvid4=D98C240B-1FA4-8D02-C9B3-DD7693AFC8DF90828-025122016-lD92PdnjNqMMVtStsO1Yaw%3D%3D; rpdid=|(J|lmkkkuJ|0J'u~YYkkul~u; DedeUserID=123152920; DedeUserID__ckMd5=14a440f25b863dcc; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; CURRENT_QUALITY=0; PEA_AU=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiaWQiOjEyMzE1MjkyMCwicGlkIjozNzUyOTM4LCJleHAiOjE4MDIyNzAyMzAsImlzcyI6InRlc3QifQ.-Ki8KKoVKdTUYDeIL6zR10rl5t-RlYiDsIiLLJjK3ik; fingerprint=a4e5b37b8876bfe9b2ac49851b255d83; buvid_fp_plain=undefined; buvid_fp=a4e5b37b8876bfe9b2ac49851b255d83; bsource=search_bing; bp_t_offset_123152920=1167965937526112256; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzEwMzc2MjMsImlhdCI6MTc3MDc3ODM2MywicGx0IjotMX0.YmqjaqFACN6HQkPvqSSujttyA0mmbQgrWYeHlb2Bhbg; bili_ticket_expires=1771037563; SESSDATA=8a9db992%2C1786523177%2C39356%2A21CjByGR1LZxP1_8VO6q6NMNeD7uaHBtFysH7X6KMHQD7BNzjXNZn8xey1B5Kzzpt74q0SVm14c1U4VkpZMUhkYl9uNnpjZGMyUmNibnc2NUs2eUdMS0kzSlZRT3hMOU1WZGR4ckJjMmx5NGwwcHZnVlBESnFQRkp3TWpSdUoyb3NLSndxUnBEOU9RIIEC; bili_jct=3900ae6a5e204b3a0afb02e5dbbb4a40; home_feed_column=5; browser_resolution=1536-695; sid=4j8dvybo; CURRENT_FNVAL=4048; b_lsid=C0839A2E_19C56CDB713",
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
# .content .text 获取html数据 .json 获取json数据
print(response.content)
```







### 保存数据





