// pages/recent/recent.js — 最近浏览（云端，自动降级本地）
const app = getApp();
const clouduser = require('../../utils/clouduser.js');

Page({
  data: {
    list: [],
    loading: true,
    error: false
  },

  onShow() {
    this.refresh();
  },

  async refresh() {
    this.setData({ loading: true, error: false });
    try {
      const a = await clouduser.getActions();
      const ids = (a && a.recents) || [];
      const all = app.globalData.lessons || [];
      const map = {};
      all.forEach((l) => { map[l.id] = l; });

      const list = ids
        .slice()
        .reverse() // 云端按时间追加，最新在前
        .map((id) => map[id])
        .filter((l) => l)
        .map((l) => ({
          id: l.id,
          title: l.title,
          sub: '第' + l.unitNumber + '单元 · ' + l.lessonTypeName,
          desc: (l.overview || '').substring(0, 46) + ((l.overview || '').length > 46 ? '…' : '')
        }));
      this.setData({ list, loading: false, error: false });
    } catch (e) {
      this.setData({ list: [], loading: false, error: true });
    }
  },

  onRetry() {
    this.refresh();
  },

  onPullDownRefresh() {
    this.refresh().then(() => wx.stopPullDownRefresh());
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
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('recent');
          this.refresh();
        }
      }
    });
  }
});
