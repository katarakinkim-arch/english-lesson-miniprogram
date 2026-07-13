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

const BOOK_ORDER = { '必修第一册': 1, '必修第二册': 2, '必修第三册': 3 };
const BOOK_SHORT = { '必修第一册': '必修一', '必修第二册': '必修二', '必修第三册': '必修三' };
const ICON = {
  'listening-speaking': '🎧', 'reading': '📖', 'grammar': '✏️',
  'listening-talking': '💬', 'writing': '✍️', 'project': '🎯'
};
const ICON_BG = {
  'listening-speaking': '#6b46c1', 'reading': '#1a365d', 'grammar': '#1a6840',
  'listening-talking': '#b7791f', 'writing': '#7b341e', 'project': '#2c5282'
};

Page({
  data: {
    keyword: '',
    bookFilter: '0',
    loading: true,
    groups: [],
    showHistory: false,
    history: [],
    books: [
      { value: '0', label: '全部' },
      { value: '1', label: '必修一' },
      { value: '2', label: '必修二' },
      { value: '3', label: '必修三' }
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

  applyFilter() {
    const kw = this.data.keyword.trim().toLowerCase();
    const bf = this.data.bookFilter;
    const filtered = this.all.slice().sort((a, b) =>
      (BOOK_ORDER[a.book] - BOOK_ORDER[b.book]) ||
      (a.unitNumber - b.unitNumber) ||
      ((a.periodNumber || 0) - (b.periodNumber || 0))
    ).filter((l) => {
      if (bf === '1' && l.book !== '必修第一册') return false;
      if (bf === '2' && l.book !== '必修第二册') return false;
      if (bf === '3' && l.book !== '必修第三册') return false;
      if (kw) {
        const hay = (
          l.title + ' ' + l.unitTitle + ' ' + (l.tags || []).join(' ') + ' ' + (l.textbookAnalysis || '') + ' ' + (l.overview || '') + ' ' +
          (l.keyPoints || '') + ' ' + (l.difficulties || '') + ' ' + (l.teachingMethods || '') + ' ' + (l.preparation || '') + ' ' +
          (l.objectives || []).join(' ') + ' ' + (l.process || []).map((s) => s.step + ' ' + s.content).join(' ') + ' ' +
          (l.exercises || '') + ' ' + (l.reflection || '') + ' ' + (l.blackboard || '')
        ).toLowerCase();
        if (hay.indexOf(kw) === -1) return false;
      }
      return true;
    });

    // 按 册+单元 分组（"全部"时 unitNumber 会跨册重复，必须用 册 区分）
    const map = {};
    filtered.forEach((l) => {
      const key = l.book + '|' + l.unitNumber;
      if (!map[key]) {
        map[key] = {
          key: key,
          book: l.book,
          bookShort: BOOK_SHORT[l.book] || l.book,
          unitNumber: l.unitNumber,
          unitTitle: l.unitTitle,
          lessons: []
        };
      }
      map[key].lessons.push({
        id: l.id,
        title: l.title,
        sub: (l.lessonTypeName || '') + ' · ' + (l.duration || 45) + '分钟',
        icon: ICON[l.lessonType] || '📄',
        iconBg: ICON_BG[l.lessonType] || '#555'
      });
    });

    const groups = Object.keys(map).map((k) => map[k]).sort((a, b) =>
      (BOOK_ORDER[a.book] - BOOK_ORDER[b.book]) || (a.unitNumber - b.unitNumber)
    );
    this.setData({ groups });
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
      title: '高中英语教案库｜人教版2019 必修一至三，按教材单元排列',
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
