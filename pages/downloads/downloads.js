// pages/downloads/downloads.js — 我的下载（本地存储，无需服务器）
const app = getApp();

function fmtLabel(format) {
  if (!format) return '';
  const map = { word: 'Word', pdf: 'PDF', ppt: 'PPT' };
  return (map[format] || format).toUpperCase();
}

Page({
  data: {
    list: [],
    total: 0
  },

  onShow() {
    this.refresh();
  },

  refresh() {
    const raw = app.globalData.downloads || [];
    const list = raw.map((d) => ({
      id: d.id,
      lessonId: d.lessonId,
      title: d.lessonTitle || '未命名教案',
      sub: (d.grade ? d.grade + ' · ' : '') + fmtLabel(d.format),
      time: d.time || ''
    }));
    this.setData({ list, total: list.length });
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
      success: (res) => {
        if (res.confirm) {
          app.globalData.downloads = [];
          wx.setStorageSync('downloads', []);
          this.refresh();
        }
      }
    });
  }
});
