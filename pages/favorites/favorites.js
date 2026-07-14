// pages/favorites/favorites.js —— 我的收藏（独立 tab）
const app = getApp();
const clouduser = require('../../utils/clouduser.js');

function normIds(a) {
  return (a || []).map((x) => (typeof x === 'string' ? x : (x.lessonId || x.id))).filter(Boolean);
}

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
      const ids = normIds(a && a.favorites);
      const list = app.getLessonsByIds(ids).map((l) => ({
        id: l.id,
        title: l.title,
        sub: l.book + ' · ' + l.unitTitle + ' · ' + l.lessonTypeName
      }));
      this.setData({ list, loading: false });
    } catch (e) {
      this.setData({ error: true, loading: false });
    }
  },

  onPullDownRefresh() {
    this.refresh().then(() => wx.stopPullDownRefresh());
  },

  openDetail(e) {
    const id = e.currentTarget.dataset.id;
    const meta = app.getLessonById(id);
    const root = app.subjectRoot(meta && meta.subject);
    wx.navigateTo({ url: '/subpackages/' + root + '/pages/detail/detail?id=' + id });
  },

  removeFav(e) {
    const id = e.currentTarget.dataset.id;
    wx.showModal({
      title: '取消收藏',
      content: '确定从收藏中移除该教案？',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.removeAction('favorite', id);
          this.refresh();
        }
      }
    });
  },

  clearAll() {
    if (!this.data.list.length) return;
    wx.showModal({
      title: '清空收藏',
      content: '确定清空全部收藏？此操作不可恢复。',
      confirmText: '清空',
      confirmColor: '#c0392b',
      success: async (res) => {
        if (res.confirm) {
          await clouduser.clear('favorites');
          this.refresh();
        }
      }
    });
  }
});
