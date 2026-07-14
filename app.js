// app.js — 小程序入口：加载轻量索引、初始化云开发、登录用户
const index = require('./data/index.js');
const clouduser = require('./utils/clouduser.js');
const privacy = require('./utils/privacy.js');
const analytics = require('./utils/analytics.js');
const { rootOf } = require('./utils/subjects.js');

App({
  globalData: {
    index: index,           // 轻量元数据索引（主包，用于学科选择/收藏/记录解析）
    user: null
  },

  onLaunch() {
    privacy.tryShowAtLaunch();
    analytics.init();
    clouduser.login()
      .then((u) => { this.globalData.user = u; })
      .catch(() => {});
  },

  onError(err) {
    analytics.recordError(err);
  },

  // 按 id 取单课元数据（来自索引，不含全文）
  getLessonById(id) {
    return (this.globalData.index || []).find((l) => l.id === id);
  },

  // 按 id 数组取多课元数据（顺序保持入参顺序）
  getLessonsByIds(ids) {
    const map = {};
    (this.globalData.index || []).forEach((l) => { map[l.id] = l; });
    return (ids || []).map((id) => map[id]).filter(Boolean);
  },

  // 学科名 -> 子包根目录
  subjectRoot(subject) {
    return rootOf(subject);
  }
});
