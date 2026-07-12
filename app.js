// app.js — 小程序入口：加载教案数据、初始化云开发、登录用户
const lessons = require('./data/lessons.js');
const clouduser = require('./utils/clouduser.js');

App({
  globalData: {
    lessons: lessons,        // 内置 30 课英语教案
    user: null               // 当前云端用户（含 downloads/recents/favorites）
  },

  onLaunch() {
    // 云端登录（未配置云环境时内部自动降级，不影响启动）
    clouduser.login()
      .then((u) => { this.globalData.user = u; })
      .catch(() => {});
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
