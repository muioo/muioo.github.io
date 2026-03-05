---
author: muioo

title: "【VUE 项目部署笔记】如何部署vue项目到linux服务器"

date: 2026-01-26

description: "项目部署笔记"

tags: [ "vue","项目部署"]

categories: ["开发技术"]

---

## 项目部署

#### 前端部署

```ts
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 8891,
    host: '0.0.0.0',
    proxy: {
    // 转发所有以 /api 开头的接口请求
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      '/baike_img': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
})
```





#### 后端部署



