(() => {
  // <stdin>
  function updateRunningDays() {
    const blogStats = document.getElementById("blog-stats");
    const daysElement = document.getElementById("running-days");
    if (!blogStats || !daysElement) {
      return;
    }
    const launchDateStr = blogStats.getAttribute("data-launch-date");
    if (!launchDateStr) {
      daysElement.textContent = "0";
      return;
    }
    try {
      const startDate = /* @__PURE__ */ new Date(launchDateStr + "T00:00:00Z");
      const today = /* @__PURE__ */ new Date();
      const utcToday = new Date(Date.UTC(today.getFullYear(), today.getMonth(), today.getDate()));
      const timeDiff = utcToday.getTime() - startDate.getTime();
      const runningDays = Math.max(0, Math.floor(timeDiff / (1e3 * 60 * 60 * 24)));
      daysElement.textContent = runningDays.toString();
    } catch (error) {
      console.error("\u8BA1\u7B97\u8FD0\u884C\u5929\u6570\u65F6\u51FA\u9519:", error);
      daysElement.textContent = "0";
    }
  }
  function initBlogStats() {
    updateRunningDays();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initBlogStats);
  } else {
    initBlogStats();
  }
  window.addEventListener("load", () => {
    initBlogStats();
    if (window.Stack && window.Stack.init) {
      const originalInit = window.Stack.init;
      window.Stack.init = function() {
        originalInit.apply(this, arguments);
        setTimeout(initBlogStats, 100);
      };
    }
  });
  window.updateRunningDays = updateRunningDays;
})();
