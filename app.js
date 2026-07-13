// app.js — 小程序入口：加载教案数据、初始化云开发、登录用户
const lessons = require('./data/lessons.js');
const clouduser = require('./utils/clouduser.js');
const privacy = require('./utils/privacy.js');
const analytics = require('./utils/analytics.js');

App({
  globalData: {
    lessons: lessons,        // 内置 30 课英语教案
    user: null               // 当前云端用户（含 downloads/recents/favorites）
  },

  onLaunch() {
    // 隐私合规：后台已配置《隐私保护指引》时，首次启动弹授权窗（未配置则 no-op）
    privacy.tryShowAtLaunch();
    // 轻量错误上报（本地记录，便于上线后排查）
    analytics.init();
    // 云端登录（未配置云环境时内部自动降级，不影响启动）
    clouduser.login()
      .then((u) => { this.globalData.user = u; })
      .catch(() => {});
  },

  // 全局错误捕获
  onError(err) {
    analytics.recordError(err);
  },

  // 按 id 取单课
  getLessonById(id) {
    return (this.globalData.lessons || []).find((l) => l.id === id);
  },

  // 按 id 数组取多课（顺序保持入参顺序）
  getLessonsByIds(ids) {
    const map = {};
    (this.globalData.lessons || []).forEach((l) => { map[l.id] = l; });
    return (ids || []).map((id) => map[id]).filter(Boolean);
  }
});
