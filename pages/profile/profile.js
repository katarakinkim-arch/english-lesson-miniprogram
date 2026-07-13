// pages/profile/profile.js — 我的（昵称头像 + 统计 + 下载/浏览记录 + 数据管理）
const app = getApp();
const clouduser = require('../../utils/clouduser.js');

function normIds(a) {
  return (a || []).map((x) => (typeof x === 'string' ? x : (x.lessonId || x.id))).filter(Boolean);
}
function toCards(ids) {
  return app.getLessonsByIds(ids).map((l) => ({
    id: l.id,
    title: l.title,
    sub: l.book + ' · ' + l.unitTitle + ' · ' + l.lessonTypeName
  }));
}

Page({
  data: {
    openid: '',
    nickName: '',
    avatarUrl: '',
    isLocal: false,
    stats: { downloads: 0, recents: 0, favorites: 0 },
    downloads: [],
    recents: []
  },

  onShow() {
    this.refresh();
  },

  async refresh() {
    try {
      const u = await clouduser.login();
      const a = await clouduser.getActions();
      const dIds = normIds(a && a.downloads);
      const rIds = normIds(a && a.recents);
      const fIds = normIds(a && a.favorites);
      this.setData({
        openid: u.openid || '',
        nickName: u.nickName || '',
        avatarUrl: u.avatarUrl || '',
        isLocal: (u.openid || '') === 'local',
        stats: {
          downloads: dIds.length,
          recents: rIds.length,
          favorites: fIds.length
        },
        downloads: toCards(dIds),
        recents: toCards(rIds)
      });
    } catch (e) {
      this.setData({ isLocal: true });
    }
  },

  onChooseAvatar(e) {
    const avatarUrl = e.detail.avatarUrl;
    this.setData({ avatarUrl });
    clouduser.updateProfile({ nickName: this.data.nickName, avatarUrl });
  },

  onNickname(e) {
    const nickName = e.detail.value;
    this.setData({ nickName });
    clouduser.updateProfile({ nickName, avatarUrl: this.data.avatarUrl });
  },

  openDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({ url: '/pages/detail/detail?id=' + id });
  },

  clearDownloads() {
    if (!this.data.downloads.length) return;
    wx.showModal({
      title: '清空下载记录',
      content: '确定清空全部下载记录？',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('downloads');
          this.refresh();
        }
      }
    });
  },

  clearRecents() {
    if (!this.data.recents.length) return;
    wx.showModal({
      title: '清空浏览历史',
      content: '确定清空全部浏览历史？',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('recents');
          this.refresh();
        }
      }
    });
  },

  openPrivacy() {
    wx.navigateTo({ url: '/pages/privacy/privacy' });
  },

  clearAll() {
    wx.showModal({
      title: '清空全部云端数据',
      content: '将清空下载记录、浏览历史与收藏，此操作不可恢复。',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('downloads');
          await clouduser.clear('recents');
          await clouduser.clear('favorites');
          this.refresh();
        }
      }
    });
  }
});
