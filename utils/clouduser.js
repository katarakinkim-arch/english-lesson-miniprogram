// utils/clouduser.js —— 用户云端数据封装
// 所有方法优先走云开发；若未配置云环境（游客模式 / 未开通云开发），自动降级到本地存储，保证可用。
const { ENV_ID } = require('../config');

let _inited = false;
function initCloud() {
  if (_inited) return;
  _inited = true;
  if (wx.cloud) {
    try {
      wx.cloud.init({ env: ENV_ID, traceUser: true });
    } catch (e) {
      // 初始化失败也无妨，下面会走本地降级
    }
  }
}

function cloudReady() {
  return !!(wx.cloud && ENV_ID && ENV_ID.indexOf('your-') !== 0);
}

function callCloud(action, data) {
  return new Promise((resolve, reject) => {
    wx.cloud.callFunction({
      name: 'user',
      data: Object.assign({ action }, data),
      success: (res) => resolve(res.result),
      fail: (err) => reject(err)
    });
  });
}

// ----- 本地降级存储 -----
const LS_KEY = 'local_user_actions';
function lsGet() {
  return wx.getStorageSync(LS_KEY) || { downloads: [], recents: [], favorites: [] };
}
function lsSet(d) {
  wx.setStorageSync(LS_KEY, d);
}
function lsEmpty() {
  return { downloads: [], recents: [], favorites: [] };
}

// 统一安全调用：云失败 -> 本地降级
async function safe(action, data, fallback) {
  if (cloudReady()) {
    try {
      initCloud();
      const r = await callCloud(action, data || {});
      if (r && r.error) throw new Error(r.error);
      return r;
    } catch (e) {
      console.warn('[clouduser] 云端失败，降级本地：', e);
    }
  }
  return fallback ? fallback() : null;
}

function now() {
  return Date.now();
}

module.exports = {
  // 登录 / 拉取用户与全部行为数据
  async login() {
    return safe('login', {}, () => Object.assign({ openid: 'local' }, lsEmpty()));
  },

  // 拉取 downloads / recents / favorites
  async getActions() {
    return safe('getActions', {}, () => lsGet());
  },

  // 新增行为：type = 'recent' | 'download' | 'favorite'
  //   recent:   payload = { lessonId }
  //   download: payload = { lessonId, format }
  //   favorite: payload = { lessonId }
  async addAction(type, payload) {
    return safe('addAction', { type, ...payload }, () => {
      const d = lsGet();
      if (type === 'download') {
        d.downloads = d.downloads.filter((x) => x.lessonId !== payload.lessonId);
        d.downloads.unshift({ lessonId: payload.lessonId, format: payload.format, time: now() });
      } else if (type === 'recent') {
        d.recents = d.recents.filter((x) => x !== payload.lessonId);
        d.recents.unshift(payload.lessonId);
      } else if (type === 'favorite') {
        if (!d.favorites.includes(payload.lessonId)) d.favorites.unshift(payload.lessonId);
      }
      lsSet(d);
      return { ok: true };
    });
  },

  // 移除行为
  async removeAction(type, lessonId) {
    return safe('removeAction', { type, lessonId }, () => {
      const d = lsGet();
      if (type === 'download') d.downloads = d.downloads.filter((x) => x.lessonId !== lessonId);
      else d[type] = d[type].filter((x) => x !== lessonId);
      lsSet(d);
      return { ok: true };
    });
  },

  // 清空某一类
  async clear(type) {
    return safe('clear', { type }, () => {
      const d = lsGet();
      d[type] = [];
      lsSet(d);
      return { ok: true };
    });
  },

  // 更新昵称头像
  async updateProfile(profile) {
    return safe('updateProfile', profile, () => ({ ok: true }));
  }
};
