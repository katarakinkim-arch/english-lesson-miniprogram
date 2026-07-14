// utils/lessonView.js — 列表页 / 详情页 的通用 Page 配置工厂（主包提供，子包 require 复用）
// 子包页面通过 getLessons() 传入本学科数据，避免主包直接 require 子包数据（微信限制）。
const clouduser = require('./clouduser.js');
const analytics = require('./analytics.js');
const { rootOf } = require('./subjects.js');

function calcPages(p) {
  const text = [
    p.textbookAnalysis,
    p.overview,
    (p.objectives || []).join(''),
    p.keyPoints,
    p.difficulties,
    p.teachingMethods,
    p.preparation,
    (p.process || []).map((s) => s.content).join(''),
    p.blackboard,
    p.exercises,
    p.reflection
  ].join('');
  const words = text.replace(/\s/g, '').length;
  return Math.max(4, Math.round(words / 520));
}

function buildDesc(p) {
  const d = [];
  d.push('适用：' + (p.grade || '高中') + ' · ' + (p.subject || '英语'));
  d.push('课型：' + (p.lessonTypeName || '') + '（' + (p.duration || 45) + '分钟）');
  if (p.process && p.process.length) d.push('含完整教学过程 ' + p.process.length + ' 步');
  if (p.exercises) d.push('含分层作业与参考答案');
  if (p.blackboard) d.push('含板书设计图');
  if (p.preparation) d.push('含课前准备清单');
  return d;
}

const CN_NUM = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'];
function buildSections(p) {
  const s = [];
  let i = 0;
  const add = (key, name, type, payload) => {
    if (payload) { i++; s.push(Object.assign({ key: key, no: CN_NUM[i - 1], title: name, type: type }, payload)); }
  };
  add('textbookAnalysis', '教材分析', 'text', p.textbookAnalysis && { body: p.textbookAnalysis, copyText: p.textbookAnalysis || '' });
  add('overview', '学情分析', 'text', p.overview && { body: p.overview, copyText: p.overview || '' });
  add('objectives', '教学目标', 'list', p.objectives && p.objectives.length && { items: p.objectives, copyText: (p.objectives || []).join('\n') });
  add('keyPoints', '教学重点', 'text', p.keyPoints && { body: p.keyPoints, copyText: p.keyPoints || '' });
  add('difficulties', '教学难点', 'text', p.difficulties && { body: p.difficulties, copyText: p.difficulties || '' });
  add('teachingMethods', '教学方法', 'text', p.teachingMethods && { body: p.teachingMethods, copyText: p.teachingMethods || '' });
  add('preparation', '课前准备', 'text', p.preparation && { body: p.preparation, copyText: p.preparation || '' });
  add('process', '教学过程', 'steps', p.process && p.process.length && { steps: p.process, copyText: (p.process || []).map((s) => s.step + '\n' + s.content).join('\n\n') });
  add('blackboard', '板书设计', 'pre', p.blackboard && { body: p.blackboard, copyText: p.blackboard || '' });
  add('exercises', '课后练习', 'text', p.exercises && { body: p.exercises, copyText: p.exercises || '' });
  add('reflection', '教学反思', 'text', p.reflection && { body: p.reflection, copyText: p.reflection || '' });
  return s;
}

// 详情页配置（数据由子包传入）
function makeDetailPage(getLessons) {
  return {
    data: {
      plan: null, pages: 0, desc: [], sections: [],
      fmt: 'word', loading: true, generating: false, favorited: false
    },
    onLoad(options) {
      const plan = (getLessons() || []).find((l) => l.id === options.id);
      if (!plan) {
        wx.showToast({ title: '未找到该教案', icon: 'none' });
        setTimeout(() => wx.navigateBack(), 800);
        return;
      }
      this.setData({
        plan: plan,
        pages: calcPages(plan),
        desc: buildDesc(plan),
        sections: buildSections(plan),
        loading: false
      });
      wx.setNavigationBarTitle({ title: plan.lessonTypeName || '教案详情' });
      clouduser.addAction('recent', { lessonId: plan.id });
      clouduser.getActions().then((a) => {
        const fav = (a && a.favorites) || [];
        this.setData({ favorited: fav.indexOf(plan.id) >= 0 });
      }).catch(() => {});
    },
    async toggleFavorite() {
      const plan = this.data.plan;
      if (!plan) return;
      const willFav = !this.data.favorited;
      this.setData({ favorited: willFav });
      try {
        if (willFav) await clouduser.addAction('favorite', { lessonId: plan.id });
        else await clouduser.removeAction('favorite', plan.id);
        analytics.track('favorite', { id: plan.id, on: willFav });
      } catch (e) {
        this.setData({ favorited: !willFav });
        wx.showToast({ title: '操作失败', icon: 'none' });
      }
    },
    selectFmt(e) { this.setData({ fmt: e.currentTarget.dataset.f }); },
    async onDownload() {
      const plan = this.data.plan;
      const fmt = this.data.fmt;
      if (!plan) return;
      this.setData({ generating: true });
      wx.showLoading({ title: '生成中...' });
      try {
        const docgen = require('./docgen.js');
        const filePath = await docgen.generateDoc(plan, fmt);
        wx.hideLoading();
        wx.openDocument({
          filePath: filePath,
          showMenu: true,
          fail: (err) => {
            console.error('openDocument fail', err);
            wx.showToast({ title: '打开失败，请重试', icon: 'none' });
          }
        });
        clouduser.addAction('download', { lessonId: plan.id, format: fmt });
        analytics.track('download', { id: plan.id, format: fmt });
      } catch (err) {
        wx.hideLoading();
        console.error('generateDoc error', err);
        wx.showToast({ title: '生成失败', icon: 'none' });
      }
      this.setData({ generating: false });
    },
    onCopySection(e) {
      const key = e.currentTarget.dataset.key;
      const sec = (this.data.sections || []).find((s) => s.key === key);
      const text = sec && sec.copyText;
      if (!text) { wx.showToast({ title: '暂无内容', icon: 'none' }); return; }
      wx.setClipboardData({
        data: text,
        success: () => { wx.showToast({ title: '已复制本节', icon: 'none' }); },
        fail: () => { wx.showToast({ title: '复制失败', icon: 'none' }); }
      });
    },
    onShareAppMessage() {
      const p = this.data.plan;
      if (!p) return { title: '高中教案库', path: '/pages/index/index', imageUrl: '/images/share-cover.png' };
      return {
        title: p.title + '｜' + (p.lessonTypeName || '教案') + '（人教版' + (p.book || '') + '）',
        path: '/subpackages/' + rootOf(p.subject) + '/pages/detail/detail?id=' + p.id,
        imageUrl: '/images/share-cover.png'
      };
    },
    onShareTimeline() {
      const p = this.data.plan;
      if (!p) return { title: '高中教案库', query: '', imageUrl: '/images/share-cover.png' };
      return {
        title: p.title + '｜' + (p.lessonTypeName || '教案'),
        query: 'id=' + p.id,
        imageUrl: '/images/share-cover.png'
      };
    }
  };
}

// 列表页配置（数据 + 学科元信息由子包传入）
function makeListPage(getLessons, meta) {
  const bookList = meta.books; // [{value,label,book}]
  const BOOK_ORDER = {};
  const VALUE_TO_BOOK = {};
  bookList.forEach((b, i) => {
    if (b.book !== '__all__') BOOK_ORDER[b.book] = i;
    VALUE_TO_BOOK[b.value] = b.book;
  });

  function getHistory() { return wx.getStorageSync('search_history') || []; }
  function pushHistory(kw) {
    kw = (kw || '').trim();
    if (kw.length < 1) return;
    let h = getHistory().filter((x) => x !== kw);
    h.unshift(kw);
    if (h.length > 10) h = h.slice(0, 10);
    wx.setStorageSync('search_history', h);
  }

  return {
    data: { keyword: '', bookFilter: '0', loading: true, groups: [], showHistory: false, history: [], books: bookList },
    onLoad() {
      this.all = getLessons();
      this.applyFilter();
      setTimeout(() => { this.setData({ loading: false }); }, 200);
    },
    onSearch(e) { this.setData({ keyword: e.detail.value || '' }); this.applyFilter(); },
    onSearchFocus() { this.setData({ showHistory: true, history: getHistory() }); },
    onSearchConfirm() {
      const kw = this.data.keyword.trim();
      if (kw) { pushHistory(kw); this.setData({ history: getHistory() }); }
      this.setData({ showHistory: false });
    },
    hideHistory() { this.setData({ showHistory: false }); },
    onHistoryTap(e) {
      const kw = e.currentTarget.dataset.kw;
      this.setData({ keyword: kw, showHistory: false });
      this.applyFilter();
    },
    clearHistory() { wx.removeStorageSync('search_history'); this.setData({ history: [] }); },
    clearSearch() { this.setData({ keyword: '' }); this.applyFilter(); },
    onBookTap(e) { this.setData({ bookFilter: e.currentTarget.dataset.v }); this.applyFilter(); },
    applyFilter() {
      const kw = this.data.keyword.trim().toLowerCase();
      const bf = this.data.bookFilter;
      const filtered = (this.all || []).slice().sort((a, b) =>
        ((BOOK_ORDER[a.book] || 99) - (BOOK_ORDER[b.book] || 99)) ||
        (a.unitNumber - b.unitNumber) ||
        ((a.periodNumber || 0) - (b.periodNumber || 0))
      ).filter((l) => {
        if (bf !== '0' && l.book !== VALUE_TO_BOOK[bf]) return false;
        if (kw) {
          const hay = (
            l.title + ' ' + (l.unitTitle || '') + ' ' + (l.tags || []).join(' ') + ' ' + (l.textbookAnalysis || '') + ' ' + (l.overview || '') + ' ' +
            (l.keyPoints || '') + ' ' + (l.difficulties || '') + ' ' + (l.teachingMethods || '') + ' ' + (l.preparation || '') + ' ' +
            (l.objectives || []).join(' ') + ' ' + (l.process || []).map((s) => s.step + ' ' + s.content).join(' ') + ' ' +
            (l.exercises || '') + ' ' + (l.reflection || '') + ' ' + (l.blackboard || '')
          ).toLowerCase();
          if (hay.indexOf(kw) === -1) return false;
        }
        return true;
      });

      const map = {};
      filtered.forEach((l) => {
        const key = l.book + '|' + l.unitNumber;
        if (!map[key]) {
          map[key] = { key: key, book: l.book, bookShort: l.book, unitNumber: l.unitNumber, unitTitle: l.unitTitle, lessons: [] };
        }
        map[key].lessons.push({
          id: l.id,
          title: l.title,
          sub: (l.lessonTypeName || '') + ' · ' + (l.duration || 45) + '分钟',
          icon: meta.emoji,
          iconBg: meta.color
        });
      });

      const groups = Object.keys(map).map((k) => map[k]).sort((a, b) =>
        ((BOOK_ORDER[a.book] || 99) - (BOOK_ORDER[b.book] || 99)) || (a.unitNumber - b.unitNumber)
      );
      this.setData({ groups });
    },
    openDetail(e) {
      const id = e.currentTarget.dataset.id;
      this.setData({ showHistory: false });
      clouduser.addAction('recent', { lessonId: id });
      analytics.track('open_detail', { id });
      wx.navigateTo({ url: '../detail/detail?id=' + id });
    },
    onShareAppMessage() {
      return {
        title: meta.subject + '教案库｜人教版2019 全套教案',
        path: '/subpackages/' + meta.root + '/pages/list/list',
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
  };
}

module.exports = { makeDetailPage, makeListPage, buildSections, buildDesc, calcPages };
