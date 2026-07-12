// pages/downloads/downloads.js — 我的下载（云端，自动降级本地）
const app = getApp();
const clouduser = require('../../utils/clouduser.js');

function fmtLabel(format) {
  if (!format) return '';
  const map = { word: 'Word', pdf: 'PDF', ppt: 'PPT' };
  return (map[format] || format).toUpperCase();
}

Page({
  data: {
    list: [],
    total: 0,
    loading: true
  },

  onShow() {
    this.refresh();
  },

  async refresh() {
    this.setData({ loading: true });
    try {
      const a = await clouduser.getActions();
      const raw = (a && a.downloads) || [];
      const all = app.globalData.lessons || [];
      const map = {};
      all.forEach((l) => { map[l.id] = l; });

      const list = raw
        .slice()
        .reverse() // 云端按时间追加，最新在前
        .map((d) => {
          const lesson = map[d.lessonId] || {};
          return {
            id: d.lessonId,
            title: lesson.title || '未命名教案',
            sub: (lesson.grade ? lesson.grade + ' · ' : '') + fmtLabel(d.format),
            time: d.time ? formatTime(d.time) : ''
          };
        });
      this.setData({ list, total: list.length, loading: false });
    } catch (e) {
      this.setData({ list: [], total: 0, loading: false });
    }
  },

  openDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({ url: '/pages/detail/detail?id=' + id });
  },

  clearAll() {
    if (!this.data.list.length) return;
    wx.showModal({
      title: '清空下载记录',
      content: '确定要清空全部下载记录吗？此操作不可恢复。',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('downloads');
          this.refresh();
        }
      }
    });
  }
});

function formatTime(t) {
  const d = new Date(t);
  const p = (n) => (n < 10 ? '0' + n : '' + n);
  return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()) + ' ' + p(d.getHours()) + ':' + p(d.getMinutes());
}
