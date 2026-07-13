const app = getApp();
const clouduser = require('../../utils/clouduser.js');
const analytics = require('../../utils/analytics.js');

function getHistory() { return wx.getStorageSync('search_history') || []; }
function pushHistory(kw) {
  kw = (kw || '').trim();
  if (kw.length < 1) return;
  let h = getHistory().filter((x) => x !== kw);
  h.unshift(kw);
  if (h.length > 10) h = h.slice(0, 10);
  wx.setStorageSync('search_history', h);
}

Page({
  data: {
    keyword: '',
    bookFilter: '0',
    typeFilter: 'all',
    loading: true,
    list: [],
    showHistory: false,
    history: [],
    books: [
      { value: '0', label: '全部' },
      { value: '1', label: '必修一' },
      { value: '2', label: '必修二' },
      { value: '3', label: '必修三' }
    ],
    types: [
      { value: 'all', label: '全部课型' },
      { value: 'reading', label: '阅读' },
      { value: 'grammar', label: '语法' },
      { value: 'writing', label: '写作' }
    ]
  },

  onLoad() {
    this.all = app.globalData.lessons;
    this.applyFilter();
    setTimeout(() => { this.setData({ loading: false }); }, 250);
  },

  onSearch(e) {
    this.setData({ keyword: e.detail.value || '' });
    this.applyFilter();
  },

  onSearchFocus() {
    this.setData({ showHistory: true, history: getHistory() });
  },

  onSearchConfirm() {
    const kw = this.data.keyword.trim();
    if (kw) {
      pushHistory(kw);
      this.setData({ history: getHistory() });
    }
    this.setData({ showHistory: false });
  },

  hideHistory() {
    this.setData({ showHistory: false });
  },

  onHistoryTap(e) {
    const kw = e.currentTarget.dataset.kw;
    this.setData({ keyword: kw, showHistory: false });
    this.applyFilter();
  },

  clearHistory() {
    wx.removeStorageSync('search_history');
    this.setData({ history: [] });
  },

  clearSearch() {
    this.setData({ keyword: '' });
    this.applyFilter();
  },

  onBookTap(e) {
    this.setData({ bookFilter: e.currentTarget.dataset.v });
    this.applyFilter();
  },

  onTypeTap(e) {
    this.setData({ typeFilter: e.currentTarget.dataset.v });
    this.applyFilter();
  },

  applyFilter() {
    const kw = this.data.keyword.trim().toLowerCase();
    const bf = this.data.bookFilter;
    const tf = this.data.typeFilter;
    const list = this.all.filter((l) => {
      if (bf === '1' && l.book !== '必修第一册') return false;
      if (bf === '2' && l.book !== '必修第二册') return false;
      if (bf === '3' && l.book !== '必修第三册') return false;
      if (tf !== 'all' && l.lessonType !== tf) return false;
      if (kw) {
        const hay = (
          l.title + ' ' + l.unitTitle + ' ' + (l.tags || []).join(' ') + ' ' + (l.overview || '') + ' ' +
          (l.keyPoints || '') + ' ' + (l.difficulties || '') + ' ' + (l.preparation || '') + ' ' +
          (l.objectives || []).join(' ') + ' ' + (l.process || []).map((s) => s.step + ' ' + s.content).join(' ') + ' ' +
          (l.exercises || '') + ' ' + (l.reflection || '') + ' ' + (l.blackboard || '')
        ).toLowerCase();
        if (hay.indexOf(kw) === -1) return false;
      }
      return true;
    }).map((l) => ({
      id: l.id,
      title: l.title,
      sub: '第' + l.unitNumber + '单元 · ' + l.lessonTypeName,
      desc: (l.overview || '').substring(0, 46) + ((l.overview || '').length > 46 ? '…' : ''),
      views: l.viewCount || 0,
      dls: l.downloadCount || 0,
      duration: l.duration || 45
    }));
    this.setData({ list });
  },

  openDetail(e) {
    const id = e.currentTarget.dataset.id;
    this.setData({ showHistory: false });
    clouduser.addAction('recent', { lessonId: id });
    analytics.track('open_detail', { id });
    wx.navigateTo({ url: '/pages/detail/detail?id=' + id });
  },

  onShareAppMessage() {
    return {
      title: '高中英语教案库｜人教版2019 必修一二册 30课，Word/PPT/PDF 一键生成',
      path: '/pages/index/index',
      imageUrl: '/images/share-cover.png'
    };
  },

  onPullDownRefresh() {
    this.setData({ loading: true });
    this.applyFilter();
    setTimeout(() => {
      this.setData({ loading: false });
      wx.stopPullDownRefresh();
    }, 300);
  }
});
