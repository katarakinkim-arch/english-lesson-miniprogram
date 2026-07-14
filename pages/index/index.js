// pages/index/index.js —— 学科选择首页（主包）
const app = getApp();
const { SUBJECTS } = require('../../utils/subjects.js');

Page({
  data: {
    subjects: [],
    total: 0,
    loading: true
  },

  onLoad() {
    const idx = app.globalData.index || [];
    const counts = {};
    idx.forEach((l) => { counts[l.subject] = (counts[l.subject] || 0) + 1; });
    const subjects = SUBJECTS.map((s) => ({
      key: s.key, name: s.name, root: s.root, emoji: s.emoji, color: s.color,
      count: counts[s.name] || 0
    }));
    this.setData({ subjects: subjects, total: idx.length, loading: false });
  },

  openSubject(e) {
    const root = e.currentTarget.dataset.root;
    wx.navigateTo({ url: '/subpackages/' + root + '/pages/list/list' });
  },

  onShareAppMessage() {
    return {
      title: '高中全9科教案库｜人教版2019 · ' + (this.data.total || 0) + '课无脑可用',
      path: '/pages/index/index',
      imageUrl: '/images/share-cover.png'
    };
  }
});
