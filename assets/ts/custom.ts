/**
 * 自定义脚本 - 处理博客统计信息的动态更新
 */

/**
 * 更新网站运行天数
 */
function updateRunningDays(): void {
    const blogStats = document.getElementById('blog-stats');
    const daysElement = document.getElementById('running-days');

    if (!blogStats || !daysElement) {
        return;
    }

    // 从 data 属性获取启动日期
    const launchDateStr = blogStats.getAttribute('data-launch-date');
    if (!launchDateStr) {
        daysElement.textContent = '0';
        return;
    }

    try {
        // 使用 UTC 时区避免时区问题
        const startDate = new Date(launchDateStr + 'T00:00:00Z');
        const today = new Date();
        const utcToday = new Date(Date.UTC(today.getFullYear(), today.getMonth(), today.getDate()));

        // 计算天数
        const timeDiff = utcToday.getTime() - startDate.getTime();
        const runningDays = Math.max(0, Math.floor(timeDiff / (1000 * 60 * 60 * 24)));

        // 更新显示
        daysElement.textContent = runningDays.toString();
    } catch (error) {
        console.error('计算运行天数时出错:', error);
        daysElement.textContent = '0';
    }
}

/**
 * 初始化函数 - 在页面加载和导航时调用
 */
function initBlogStats(): void {
    updateRunningDays();
}

// 页面加载时执行
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBlogStats);
} else {
    // DOM 已经加载完成
    initBlogStats();
}

// 监听 Stack 主题的初始化
window.addEventListener('load', () => {
    initBlogStats();

    // 如果 Stack.init 存在，hook 它
    if (window.Stack && window.Stack.init) {
        const originalInit = window.Stack.init;
        window.Stack.init = function() {
            originalInit.apply(this, arguments);
            // 延迟执行以确保 DOM 已更新
            setTimeout(initBlogStats, 100);
        };
    }
});

// 暴露到全局以便手动调用
declare global {
    interface Window {
        updateRunningDays: () => void;
    }
}

window.updateRunningDays = updateRunningDays;
