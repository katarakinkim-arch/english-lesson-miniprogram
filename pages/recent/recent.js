// pages/recent/recent.js — 最近浏览（本地存储，无需服务器）
const app = getApp();

Page({
  data: {
    list: []
  },

  onShow() {
    this.refresh();
  },

  refresh() {
    const ids = app.globalData.recentlyViewed || [];
    const all = app.globalData.lessons || [];
    const map = {};
    all.forEach((l) => { map[l.id] = l; });

    const list = ids
      .map((id) => map[id])
      .filter((l) => l)
      .map((l) => ({
        id: l.id,
        title: l.title,
        sub: '第' + l.unitNumber + '单元 · ' + l.lessonTypeName,
        desc: (l.overview || '').substring(0, 46) + ((l.overview || '').length > 46 ? '…' : '')
      }));
    this.setData({ list });
  },

  openDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({ url: '/pages/detail/detail?id=' + id });
  },

  clearAll() {
    if (!this.data.list.length) return;
    wx.showModal({
      title: '清空浏览记录',
      content: '确定要清空最近浏览记录吗？此操作不可恢复。',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: (res) => {
        if (res.confirm) {
          app.globalData.recentlyViewed = [];
          wx.setStorageSync('recentlyViewed', []);
          this.refresh();
        }
      }
    });
  }
});
