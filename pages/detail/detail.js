const app = getApp();
const clouduser = require('../../utils/clouduser.js');
const analytics = require('../../utils/analytics.js');

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

function fmtTime() {
  const d = new Date();
  const p = (n) => (n < 10 ? '0' + n : '' + n);
  return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()) + ' ' + p(d.getHours()) + ':' + p(d.getMinutes());
}

Page({
  data: {
    plan: null,
    pages: 0,
    desc: [],
    sections: [],
    fmt: 'word',
    loading: true,
    generating: false,
    favorited: false
  },

  onLoad(options) {
    const plan = (app.globalData.lessons || []).find((l) => l.id === options.id);
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

    // 记录最近浏览（云端，失败自动本地）
    clouduser.addAction('recent', { lessonId: plan.id });
    // 读取收藏态
    clouduser.getActions().then((a) => {
      const fav = (a && a.favorites) || [];
      this.setData({ favorited: fav.indexOf(plan.id) >= 0 });
    }).catch(() => {});
  },

  // 收藏 / 取消收藏
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

  selectFmt(e) {
    this.setData({ fmt: e.currentTarget.dataset.f });
  },

  async onDownload() {
    const that = this;
    const plan = this.data.plan;
    const fmt = this.data.fmt;
    if (!plan) return;
    this.setData({ generating: true });
    wx.showLoading({ title: '生成中...' });
    try {
      const docgen = require('../../utils/docgen.js');
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

  // 单段复制（长按或点"复制"按钮）
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
    if (!p) return { title: '高中英语教案库', path: '/pages/index/index', imageUrl: '/images/share-cover.png' };
    return {
      title: p.title + '｜' + (p.lessonTypeName || '教案') + '（人教版' + (p.book || '') + '）',
      path: '/pages/detail/detail?id=' + p.id,
      imageUrl: '/images/share-cover.png'
    };
  },

  onShareTimeline() {
    const p = this.data.plan;
    if (!p) return { title: '高中英语教案库', query: '', imageUrl: '/images/share-cover.png' };
    return {
      title: p.title + '｜' + (p.lessonTypeName || '教案'),
      query: 'id=' + p.id,
      imageUrl: '/images/share-cover.png'
    };
  }
});
