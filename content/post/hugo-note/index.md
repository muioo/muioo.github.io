---
author: muioo

title: "【Hugo 网站搭建】Hugo搭建静态页面网站"

date: 2026-01-27

description: "记录一些hugo搭建网站所需要修改的地方"

tags: [ "hugo网站搭建"]

categories: ["开发技术"]

---

## hugo搭建静态网站（样式修改和新增功能基本就是对照theme的目录和文件来修覆盖)

- 下载hugo.exe

- 下载主题（[Hugo Themes](https://themes.gohugo.io/)）到hugo项目根目录的theme中 

- 删除主题的版本号后缀，将exampleSite/content目录和配置文件移动到根目录

- 删除content中的rich-content

#### 自定义firstblog\layouts\_default目录的作用

- **基础模板”**，所有页面（文章、首页、归档等）都会继承它

#### 添加背景图片

- 在static\images中添加图片
- 在assets\scss中custom.html添加样式

```css
#dark-mode-toggle {
    margin-top: auto;
    color: var(--body-text-color);
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: var(--menu-icon-separation);
    margin-bottom: 30px;
}
body {
    background-image: url("/images/background2.jpg") !important; /* 对应static/images/bg.jpg */
    background-size: cover !important; /* 背景图覆盖整个页面 */
    background-position: center !important; /* 背景图居中显示 */
    background-attachment: fixed !important; /* 背景图固定（滚动时不跟随） */
    background-repeat: no-repeat !important; /* 禁止背景图重复 */
    /* 可选：添加半透明遮罩，避免背景干扰文字 */
    background-color: rgba(255, 255, 255, 0.8) !important;
    background-blend-mode: overlay !important;
}

/* 修复文章背景首次加载透明问题 */
.article-page .main-article {
    background: #fff !important;
}

/* Swup 过渡期间保持背景色 */
html.is-animating .main-article {
    background: #fff !important;
}

/* 为浅色和深色模式分别设置 */
:root .article-page .main-article {
    background: #fff !important;
}

[data-scheme="dark"] .article-page .main-article {
    background: #424242 !important;
}

/* 修复图片首次加载超出内容框的问题 */
.article-content figure {
    max-width: 100%;
    overflow: hidden;
}

.article-content figure img {
    max-width: 100%;
    height: auto;
    display: block;
}
```

- 如果遇到文章内容背景加载不出来的情况， layouts/partials/head/custom.html

```html
<script>
    /*!
 * Live2D Widget
 * https://github.com/stevenjoezhang/live2d-widget
 */

// Recommended to use absolute path for live2d_path parameter
// live2d_path 参数建议使用绝对路径
const live2d_path = 'https://fastly.jsdelivr.net/npm/live2d-widgets@1.0.0-rc.6/dist/';
// const live2d_path = '/dist/';

// Method to encapsulate asynchronous resource loading
// 封装异步加载资源的方法
function loadExternalResource(url, type) {
  return new Promise((resolve, reject) => {
    let tag;

    if (type === 'css') {
      tag = document.createElement('link');
      tag.rel = 'stylesheet';
      tag.href = url;
    }
    else if (type === 'js') {
      tag = document.createElement('script');
      tag.type = 'module';
      tag.src = url;
    }
    if (tag) {
      tag.onload = () => resolve(url);
      tag.onerror = () => reject(url);
      document.head.appendChild(tag);
    }
  });
}

(async () => {
  // If you are concerned about display issues on mobile devices, you can use screen.width to determine whether to load
  // 如果担心手机上显示效果不佳，可以根据屏幕宽度来判断是否加载
  // if (screen.width < 768) return;

  // Avoid cross-origin issues with image resources
  // 避免图片资源跨域问题
  const OriginalImage = window.Image;
  window.Image = function(...args) {
    const img = new OriginalImage(...args);
    img.crossOrigin = "anonymous";
    return img;
  };
  window.Image.prototype = OriginalImage.prototype;
  // Load waifu.css and waifu-tips.js
  // 加载 waifu.css 和 waifu-tips.js
  await Promise.all([
    loadExternalResource(live2d_path + 'waifu.css', 'css'),
    loadExternalResource(live2d_path + 'waifu-tips.js', 'js')
  ]);
  // For detailed usage of configuration options, see README.en.md
  // 配置选项的具体用法见 README.md
  initWidget({
    waifuPath: live2d_path + 'waifu-tips.json',
    // cdnPath: 'https://fastly.jsdelivr.net/gh/fghrsh/live2d_api/',
    cubism2Path: live2d_path + 'live2d.min.js',
    cubism5Path: 'https://cubism.live2d.com/sdk-web/cubismcore/live2dcubismcore.min.js',
    tools: ['hitokoto', 'asteroids', 'switch-model', 'switch-texture', 'photo', 'info', 'quit'],
    logLevel: 'warn',
    drag: false,
  });
})();

console.log(`\n%cLive2D%cWidget%c\n`, 'padding: 8px; background: #cd3e45; font-weight: bold; font-size: large; color: white;', 'padding: 8px; background: #ff5450; font-size: large; color: #eee;', '');

/*
く__,.ヘヽ.        /  ,ー､ 〉
         ＼ ', !-─‐-i  /  /´
         ／｀ｰ'       L/／｀ヽ､
       /   ／,   /|   ,   ,       ',
     ｲ   / /-‐/  ｉ  L_ ﾊ ヽ!   i
      ﾚ ﾍ 7ｲ｀ﾄ   ﾚ'ｧ-ﾄ､!ハ|   |
        !,/7 '0'     ´0iソ|    |
        |.从"    _     ,,,, / |./    |
        ﾚ'| i＞.､,,__  _,.イ /   .i   |
          ﾚ'| | / k_７_/ﾚ'ヽ,  ﾊ.  |
            | |/i 〈|/   i  ,.ﾍ |  i  |
           .|/ /  ｉ：    ﾍ!    ＼  |
            kヽ>､ﾊ    _,.ﾍ､    /､!
            !'〈//｀Ｔ´', ＼ ｀'7'ｰr'
            ﾚ'ヽL__|___i,___,ンﾚ|ノ
                ﾄ-,/  |___./
                'ｰ'    !_,.:
*/


</script>

<!-- 关键 CSS：防止首次加载时文章背景透明 -->
<style>
    /* 确保文章容器始终有白色背景 */
    .article-page .main-article,
    main .main-article {
        background: #fff !important;
    }

    /* 深色模式 */
    [data-scheme="dark"] .article-page .main-article,
    [data-scheme="dark"] main .main-article {
        background: #424242 !important;
    }
</style>

<!-- 自定义样式：将看板娘移动到右下角 -->
<style>
    #waifu {
        left: auto !important;
        right: 0 !important;
        bottom: 0 !important;
    }

    #waifu-tips {
        left: auto !important;
        right: 0 !important;
    }

    #waifu-tool {
        left: auto !important;
        right: 0 !important;
    }
</style>
```

#### 文章底部的计数

- 效果图

{{< figure src="count.png" title="底部运行统计效果" >}}

- 新建baseof.html在layouts/_default目录下

```html
<!DOCTYPE html>
<html lang="{{ .Site.LanguageCode }}" dir="{{ default `ltr` .Language.LanguageDirection }}">
    <head>
        {{- partial "head/head.html" . -}}
        {{- block "head" . -}}{{ end }}

        <!-- giscus 预优化：DNS 预解析 + 预连接 -->
        <link rel="dns-prefetch" href="https://giscus.app">
        <link rel="preconnect" href="https://giscus.app" crossorigin>

        <!-- Swup for seamless page transitions -->
        <script src="https://unpkg.com/swup@4"></script>
        <style>
            /* Swup transition styles */
            .transition-fade {
                transition: opacity 0.3s;
                opacity: 1;
            }

            html.is-animating .transition-fade {
                opacity: 0;
            }
        </style>
    </head>
    <body class="{{ block `body-class` . }}{{ end }}">
        {{- partial "head/colorScheme" . -}}

        {{/* The container is wider when there's any activated widget */}}
        {{- $hasWidget := false -}}
        {{- range .Site.Params.widgets -}}
            {{- if gt (len .) 0 -}}
                {{- $hasWidget = true -}}
            {{- end -}}
        {{- end -}}

        <!-- Swup transition container -->
        <div id="swup" class="transition-fade">
            <div class="container main-container flex on-phone--column {{ if $hasWidget }}extended{{ else }}compact{{ end }}">
                {{- block "left-sidebar" . -}}
                    {{ partial "sidebar/left.html" . }}
                {{- end -}}
                {{- block "right-sidebar" . -}}{{ end }}
                <main class="main full-width">
                    {{- block "main" . }}{{- end }}
                </main>
            </div>
        </div>

        <!-- Audio player outside Swup container to prevent reload -->
        {{ partial "footer/aplayer.html" . }}

        <!-- 全局 giscus 状态管理（与 giscus.html 配合） -->
        <script>
        (function() {
            // 全局 giscus 状态
            window.giscusState = {
                loaded: false,
                ready: false
            };

            // 监听 giscus 加载完成事件
            document.addEventListener('giscus:loaded', function() {
                window.giscusState.ready = true;
                console.log('[Giscus] 全局状态已更新为 ready');
            });
        })();
        </script>

        <!-- Other footer scripts -->
        {{ partialCached "footer/components/script.html" . }}
        {{ partialCached "footer/components/custom-font.html" . }}

        <!-- giscus 评论脚本（放在 body 末尾确保执行） -->
        <script>
        (function() {
            'use strict';

            console.log('[GISCUS-MAIN] Script loaded');

            var giscusConfig = {
                src: 'https://giscus.app/client.js',
                repo: 'muioo/muioo.github.io',
                repoId: 'R_kgDOQ_pqAA',
                category: 'Announcements',
                categoryId: 'DIC_kwDOQ_pqAM4C2CEc',
                mapping: 'pathname',
                strict: '0',
                reactionsEnabled: '1',
                emitMetadata: '0',
                inputPosition: 'bottom',
                theme: 'preferred_color_scheme',
                lang: 'zh-CN'
            };

            var loaded = false;
            var observer = null;
            var timeoutId = null;

            function loadGiscus(container) {
                if (loaded) return;
                loaded = true;

                console.log('[GISCUS-MAIN] Loading giscus...');

                if (observer) {
                    observer.disconnect();
                    observer = null;
                }
                if (timeoutId) {
                    clearTimeout(timeoutId);
                    timeoutId = null;
                }

                var script = document.createElement('script');
                script.src = giscusConfig.src;
                script.async = true;
                script.crossOrigin = 'anonymous';

                for (var key in giscusConfig) {
                    if (key !== 'src' && giscusConfig.hasOwnProperty(key)) {
                        var dataKey = 'data-' + key.replace(/([A-Z])/g, '-$1').toLowerCase();
                        script.setAttribute(dataKey, giscusConfig[key]);
                    }
                }

                script.onload = function() {
                    console.log('[GISCUS-MAIN] giscus loaded successfully');
                    container.classList.remove('giscus-placeholder');
                    initFeatures();
                };

                script.onerror = function() {
                    console.error('[GISCUS-MAIN] Failed to load giscus');
                    container.innerHTML = '<p style="color: #ef4444; text-align: center; padding: 2rem;">评论加载失败，请刷新页面重试</p>';
                };

                container.innerHTML = '';
                container.appendChild(script);
            }

            function initFeatures() {
                var observer = new MutationObserver(function(mutations) {
                    mutations.forEach(function(mutation) {
                        if (mutation.attributeName === 'class') {
                            var iframe = document.querySelector('iframe[src*="giscus.app"]');
                            if (iframe) {
                                var isDark = document.body.classList.contains('dark');
                                var theme = isDark ? 'dark' : 'light';
                                try {
                                    iframe.contentWindow.postMessage({
                                        giscus: { setConfig: { theme: theme } }
                                    }, 'https://giscus.app');
                                } catch (e) {
                                    // Ignore cross-origin errors on first load
                                }
                            }
                        }
                    });
                });

                observer.observe(document.body, {
                    attributes: true,
                    attributeFilter: ['class']
                });

                setTimeout(function() {
                    var iframe = document.querySelector('iframe[src*="giscus.app"]');
                    if (iframe) {
                        var isDark = document.body.classList.contains('dark');
                        var theme = isDark ? 'dark' : 'light';
                        try {
                            iframe.contentWindow.postMessage({
                                giscus: { setConfig: { theme: theme } }
                            }, 'https://giscus.app');
                        } catch (e) {}
                    }
                }, 1000);
            }

            function isNearViewport(el, margin) {
                var rect = el.getBoundingClientRect();
                var windowHeight = window.innerHeight || document.documentElement.clientHeight;
                return rect.top <= windowHeight + margin;
            }

            function initLazyLoad() {
                console.log('[GISCUS-MAIN] initLazyLoad called');

                var container = document.getElementById('giscus-container');
                if (!container) {
                    console.log('[GISCUS-MAIN] Container not found, will retry');
                    setTimeout(initLazyLoad, 100);
                    return;
                }

                console.log('[GISCUS-MAIN] Container found');

                if (isNearViewport(container, 200)) {
                    console.log('[GISCUS-MAIN] Container in viewport, loading immediately');
                    loadGiscus(container);
                    return;
                }

                if ('IntersectionObserver' in window) {
                    console.log('[GISCUS-MAIN] Using IntersectionObserver');
                    observer = new IntersectionObserver(function(entries) {
                        entries.forEach(function(entry) {
                            if (entry.isIntersecting) {
                                console.log('[GISCUS-MAIN] IntersectionObserver triggered');
                                observer.disconnect();
                                observer = null;
                                loadGiscus(container);
                            }
                        });
                    }, {
                        root: null,
                        rootMargin: '200px',
                        threshold: 0
                    });

                    observer.observe(container);

                    timeoutId = setTimeout(function() {
                        if (!loaded) {
                            console.log('[GISCUS-MAIN] Timeout fallback triggered');
                            if (observer) {
                                observer.disconnect();
                                observer = null;
                            }
                            loadGiscus(container);
                        }
                    }, 3000);
                } else {
                    console.log('[GISCUS-MAIN] IntersectionObserver not supported, loading immediately');
                    loadGiscus(container);
                }
            }

            function init() {
                console.log('[GISCUS-MAIN] init() called');
                initLazyLoad();
            }

            function resetForNewPage() {
                console.log('[GISCUS-MAIN] Swup page change, resetting');
                loaded = false;

                var container = document.getElementById('giscus-container');
                if (container) {
                    container.classList.add('giscus-placeholder');
                    container.innerHTML = '<div class="giscus-loading"><div class="loading-spinner"></div><p class="loading-text">评论区加载中...</p></div>';
                }

                setTimeout(function() {
                    initLazyLoad();
                }, 100);
            }

            if (document.readyState === 'loading') {
                console.log('[GISCUS-MAIN] Waiting for DOMContentLoaded');
                document.addEventListener('DOMContentLoaded', init);
            } else {
                console.log('[GISCUS-MAIN] DOM ready, calling init');
                init();
            }

            document.addEventListener('swup:page:view', resetForNewPage);

            console.log('[GISCUS-MAIN] Script registered');
        })();
        </script>

        <!-- Swup initialization -->
        <script>
            const swup = new Swup();
        </script>
    </body>
    <script>

    // ✅ 定义更新运行天数的函数
    function updateRunningDays() {
        const BLOG_LAUNCH_DATE = '2026-01-22';
        const startDate = new Date(BLOG_LAUNCH_DATE + 'T00:00:00Z');
        const today = new Date();
        const utcToday = new Date(Date.UTC(today.getFullYear(), today.getMonth(), today.getDate()));
        const timeDiff = utcToday - startDate;
        const runningDays = Math.max(0, Math.floor(timeDiff / (1000 * 60 * 60 * 24)));

        const daysElement = document.getElementById('running-days');
        if (daysElement) {
            daysElement.textContent = runningDays;
        }
    }

    // 🔄 首次加载时立即执行
    updateRunningDays();

    // 🔄 监听 Swup 页面切换完成事件
    document.addEventListener('swup:page:view', () => {
        updateRunningDays();
    });
</script>
</html>
```

- layouts\partials\footer目录下

```html
{{- $ThemeVersion := "3.33.0" -}}
<footer class="site-footer">
    <section class="copyright">
        &copy;
        {{ if and (.Site.Params.footer.since) (ne .Site.Params.footer.since (int (now.Format "2006"))) }}
            {{ .Site.Params.footer.since }} -
        {{ end }}
        {{ now.Format "2006" }} {{ default .Site.Title .Site.Copyright }}
    </section>

    <section class="powerby">
        {{- /* 计算统计数据 */ -}}
        {{- $postCount := len (where .Site.RegularPages "Type" "post") -}}
        {{- $totalWords := 0 -}}
        {{- range where .Site.RegularPages "Type" "post" -}}
            {{- $totalWords = add $totalWords .WordCount -}}
        {{- end -}}

        {{- /* 动态生成统计文本 */ -}}
        <div id="blog-stats" style="margin-bottom: 5px;" data-launch-date="2026-01-22">
            本站已稳定运行: <strong id="running-days">计算中...</strong> 天 |
            博客: <strong>{{ $postCount }}</strong> 篇 |
            字数: <strong>{{ $totalWords }}</strong> 字
        </div>

        {{- $Generator := `<a href="https://gohugo.io/" target="_blank" rel="noopener">Hugo</a>` -}}
        {{- $Theme := printf `<b><a href="https://github.com/CaiJimmy/hugo-theme-stack" target="_blank" rel="noopener" data-version="%s">Stack</a></b>` $ThemeVersion -}}
        {{- $DesignedBy := `<a href="https://jimmycai.com" target="_blank" rel="noopener">Jimmy</a>` -}}

        {{ T "footer.builtWith" (dict "Generator" $Generator) | safeHTML }} <br />
        {{ T "footer.designedBy" (dict "Theme" $Theme "DesignedBy" $DesignedBy) | safeHTML }}
    </section>
</footer>
```

#### 看板娘功能



#### 评论区功能

1、相关链接

- **[giscus评论](https://giscus.app/zh-CN)**按照流程注册giscus

- 下载giscus评论到仓库中[github](https://github.com/giscus/giscus?tab=readme-ov-file)

2、在layouts\partials\comments目录下新建giscus.html、include.html覆盖掉下载的主题中的文件

- giscus.html文件

```html
{{/* DNS 预连接优化 */}}
<link rel="preconnect" href="https://giscus.app" crossorigin>
<link rel="dns-prefetch" href="https://giscus.app">

{{/* giscus 容器 */}}
<div id="giscus-container" class="giscus-placeholder">
    <div class="giscus-loading">
        <div class="loading-spinner"></div>
        <p class="loading-text">评论区加载中...</p>
    </div>
</div>

{{/* 优化样式 */}}
<style>
    .giscus-placeholder {
        min-height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .giscus-loading {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        padding: 2rem 1rem;
        color: var(--text-secondary, #666);
        transition: opacity 0.3s ease;
    }

    .loading-spinner {
        width: 32px;
        height: 32px;
        border: 3px solid var(--border-color, #e0e0e0);
        border-top-color: var(--accent-color, #3b82f6);
        border-radius: 50%;
        animation: giscus-spin 0.8s linear infinite;
    }

    @keyframes giscus-spin {
        to { transform: rotate(360deg); }
    }

    .loading-text {
        font-size: 0.875rem;
        opacity: 0.7;
    }

    .giscus-frame {
        min-height: 200px;
        width: 100%;
    }

    #giscus-container:not(.giscus-placeholder) {
        min-height: 400px;
    }

    /* 确保 giscus iframe 可见 */
    #giscus-container iframe {
        width: 100% !important;
        min-height: 200px !important;
        border: none !important;
    }
</style>
```

- include.html文件

```html
{{/* 评论功能主入口 - 懒加载版本 */}}
{{ if .Params.comments | default true }}
    <section class="comments-section" aria-label="评论" data-comments-section>
        <div class="comments-container">
            <h2 class="comments-title">评论</h2>
            {{ partial "comments/giscus.html" . }}
        </div>
    </section>

    <style>
        .comments-section {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border-color, #e0e0e0);
        }

        .comments-container {
            max-width: 100%;
        }

        .comments-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: var(--text-primary, #1a1a1a);
        }

        #giscus-container {
            margin-top: 1rem;
        }

        body.dark .comments-title {
            color: var(--text-primary, #e0e0e0);
        }

        body.dark .loading-text {
            color: var(--text-secondary, #999);
        }

        body.dark .loading-spinner {
            border-color: var(--border-color, #333);
            border-top-color: var(--accent-color, #60a5fa);
        }
    </style>
{{ end }}

```

3、在_default目录中的baseof.html文件中加载上述文件（如果评论区加载不出来或者有问题可能是因为baseof.html文件中渲染的顺序有问题）

#### github actions自动构建

- 创建.github/workflows/hugo.yml文件

```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches:
      - main  # 或 master，根据你的主分支名
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: true  # 如果你的主题是子模块，需要开启
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```







