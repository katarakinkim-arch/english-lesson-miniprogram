const app = getApp();
const clouduser = require('../../utils/clouduser.js');

Page({
  data: {
    keyword: '',
    bookFilter: '0',
    typeFilter: 'all',
    loading: true,
    list: [],
    books: [
      { value: '0', label: '全部' },
      { value: '1', label: '必修一' },
      { value: '2', label: '必修二' }
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
      if (tf !== 'all' && l.lessonType !== tf) return false;
      if (kw) {
        const hay = (l.title + ' ' + l.unitTitle + ' ' + (l.tags || []).join(' ') + ' ' + (l.overview || '')).toLowerCase();
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
    clouduser.addAction('recent', { lessonId: id });
    wx.navigateTo({ url: '/pages/detail/detail?id=' + id });
  },

  onShareAppMessage() {
    return {
      title: '高中英语教案库｜人教版2019 必修一二册 30课，Word/PPT/PDF 一键生成',
      path: '/pages/index/index'
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
