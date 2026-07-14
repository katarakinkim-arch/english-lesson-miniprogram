// 生成浏览器可预览的小程序模拟版 HTML
// 说明：<script> 内的动态 HTML 一律用单引号字符串拼接；内联 onclick 的属性值里的引号用 &quot; 实体，
// 避免反斜杠转义（在模板字符串里 \' 会被吞成 '）也避免反引号（会提前结束外层模板字符串）。
// 整段脚本内不含反引号与 ${}（除顶部注入数据那一行），本文件写在最外层模板字符串中也很安全。
const fs = require('fs');
const path = require('path');

const miniDir = path.join(__dirname, '..');
const lessons = require(path.join(miniDir, 'data', 'lessons-cn.js'));

// 安全嵌入 JSON 到 JS：转义 < 防止闭合 script 标签
function safeJsonStr(obj) {
  return JSON.stringify(obj).replace(/</g, '\\x3c');
}

const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<title>语文教案小程序 · 预览</title>
<style>
  :root{ --brand:#1a365d; --brand2:#2a4a7d; --bg:#f3f5f9; --txt:#1f2430; --sub:#6b7280; --line:#e6e9f0; --chip:#eef2f8; }
  *{ box-sizing:border-box; -webkit-tap-highlight-color:transparent; }
  body{ margin:0; font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif; background:#dfe3ea; color:var(--txt); }
  .phone{ max-width:390px; margin:24px auto; background:var(--bg); border-radius:38px; overflow:hidden; box-shadow:0 20px 60px rgba(20,30,60,.25); position:relative; min-height:844px; display:flex; flex-direction:column; }
  .statusbar{ height:44px; background:var(--brand); display:flex; align-items:center; justify-content:space-between; padding:0 22px; color:#fff; font-size:14px; font-weight:600; }
  .statusbar .icons{ letter-spacing:2px; }
  .navbar{ height:46px; background:var(--brand); color:#fff; display:flex; align-items:center; justify-content:center; position:relative; font-size:17px; font-weight:600; }
  .navbar .back{ position:absolute; left:14px; font-size:22px; line-height:1; cursor:pointer; pointer-events:auto; }
  .content{ flex:1; overflow-y:auto; -webkit-overflow-scrolling:touch; padding:14px; }
  .content::-webkit-scrollbar{ width:0; }
  .tabbar{ height:60px; background:#fff; border-top:1px solid var(--line); display:flex; flex-shrink:0; position:relative; z-index:20; }
  .tab{ flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#9aa1ad; font-size:11px; gap:3px; cursor:pointer; -webkit-user-select:none; user-select:none; }
  .tab .ico{ font-size:21px; }
  .tab.on{ color:var(--brand); }
  .search{ background:#fff; border-radius:14px; padding:11px 14px; display:flex; align-items:center; gap:8px; color:var(--sub); font-size:14px; box-shadow:0 2px 10px rgba(20,40,80,.05); }
  .search .sin{ flex:1; border:none; background:transparent; outline:none; font-size:14px; color:var(--txt); min-width:0; }
  .search .searchx{ color:#aab; font-size:16px; cursor:pointer; padding:0 2px; }
  .chips{ display:flex; gap:8px; margin:12px 0; flex-wrap:wrap; }
  .chip{ background:var(--chip); color:var(--sub); font-size:13px; padding:7px 14px; border-radius:20px; cursor:pointer; white-space:nowrap; }
  .chip.on{ background:var(--brand); color:#fff; }
  .card{ background:#fff; border-radius:16px; padding:16px; margin-bottom:10px; box-shadow:0 2px 10px rgba(20,40,80,.05); cursor:pointer; transition:transform .15s; display:flex; align-items:center; }
  .card:active{ transform:scale(.98); }
  .card .row1{ display:flex; gap:12px; align-items:center; width:100%; }
  .card .docico{ width:44px; height:44px; border-radius:12px; background:linear-gradient(135deg,var(--brand),var(--brand2)); color:#fff; display:flex; align-items:center; justify-content:center; font-size:20px; flex-shrink:0; }
  .card .ttl{ font-size:14.5px; font-weight:600; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
  .card .sub{ font-size:12px; color:#8a90a0; margin-top:4px; line-height:1.3; }
  .card-arrow{ font-size:24px; color:#d0d4dc; flex-shrink:0; }
  .empty{ text-align:center; color:var(--sub); padding:60px 20px; }
  .empty .e{ font-size:54px; }
  .empty .t{ margin-top:12px; font-size:15px; }
  .empty .p{ margin-top:6px; font-size:12px; color:#b3b8c4; }
  .unit-group{ margin-top:12px; }
  .unit-head{ display:flex; align-items:baseline; gap:8px; padding:12px 2px 8px; position:sticky; top:0; background:var(--bg); z-index:5; }
  .unit-no{ font-size:12px; font-weight:700; color:#fff; background:var(--brand); padding:3px 9px; border-radius:6px; flex-shrink:0; }
  .unit-name{ font-size:15px; font-weight:600; color:var(--txt); }
  .hero{ margin:-14px -14px 14px; padding:26px 18px 20px; background:linear-gradient(160deg,var(--brand),var(--brand2)); color:#fff; border-radius:0 0 22px 22px; }
  .hero .badges2{ display:flex; gap:8px; margin-bottom:14px; }
  .hero .badge2{ font-size:12px; padding:4px 11px; border-radius:9px; background:rgba(255,255,255,.18); }
  .hero h1{ font-size:20px; margin:0 0 8px; line-height:1.35; }
  .hero .hsub{ font-size:13px; opacity:.85; }
  .hero .hstat{ font-size:12px; opacity:.8; margin-top:12px; }
  .sec{ background:#fff; border-radius:16px; padding:16px; margin-bottom:12px; box-shadow:0 2px 10px rgba(20,40,80,.05); }
  .sec h3{ margin:0 0 12px; font-size:15px; display:flex; align-items:center; gap:8px; color:var(--brand); }
  .sec .scopy{ margin-left:auto; font-size:11px; color:var(--brand); background:var(--chip); border-radius:8px; padding:3px 9px; cursor:pointer; flex-shrink:0; }
  .sno{ flex-shrink:0; width:24px; height:24px; line-height:24px; text-align:center; background:linear-gradient(135deg,var(--brand),var(--brand2)); color:#fff; border-radius:50%; font-size:13px; font-weight:700; }
  .sno.sm{ width:20px; height:20px; line-height:20px; font-size:12px; }
  .sec p{ margin:0; font-size:13px; line-height:1.7; color:#3a4150; white-space:pre-wrap; word-break:break-word; }
  .sec ul{ margin:0; padding-left:18px; }
  .sec li{ font-size:13px; line-height:1.7; color:#3a4150; margin-bottom:4px; }
  .step{ background:#f7f9fc; border-left:4px solid var(--brand2); border-radius:12px; padding:10px 12px; margin-bottom:12px; }
  .step .sn{ font-size:13px; font-weight:600; color:var(--brand); display:flex; align-items:center; gap:7px; flex-wrap:wrap; }
  .step .st{ font-size:11px; color:#fff; background:var(--brand2); border-radius:7px; padding:1px 8px; margin-left:4px; }
  .step p{ margin:6px 0 0; font-size:12.5px; line-height:1.6; color:#444; white-space:pre-wrap; word-break:break-word; }
  .sc-text{ font-size:12.5px; line-height:1.7; color:#374151; margin:5px 0; white-space:pre-wrap; word-break:break-word; }
  .sc-block{ margin:7px 0; border-radius:10px; padding:8px 10px; font-size:12.5px; line-height:1.65; }
  .sc-tag{ display:inline-block; font-weight:700; font-size:11.5px; margin-bottom:3px; }
  .sc-bd{ white-space:pre-wrap; word-break:break-word; }
  .sc-ppt{ background:#eff6ff; border-left:3px solid #2563eb; }
  .sc-ppt .sc-tag{ color:#1e40af; }
  .sc-audio{ background:#ecfeff; border-left:3px solid #0891b2; }
  .sc-audio .sc-tag{ color:#0e7490; }
  .sc-teacher{ background:#fef2f2; border-left:3px solid #dc2626; }
  .sc-teacher .sc-tag{ color:#991b1b; }
  .sc-ans{ background:#f0fdf4; border-left:3px solid #16a34a; }
  .sc-ans .sc-tag{ color:#166534; }
  .sc-board{ background:#fefce8; border-left:3px solid #ca8a04; }
  .sc-board .sc-tag{ color:#854d0e; }
  .sc-diff{ background:#f5f3ff; border-left:3px solid #7c3aed; }
  .sc-diff .sc-tag{ color:#5b21b6; }
  .sc-warn{ background:#fff7ed; border-left:3px solid #ea580c; }
  .sc-warn .sc-tag{ color:#9a3412; }
  .ex-block{ margin:10px 0; border-radius:12px; overflow:hidden; border:1px solid #eef2f7; }
  .ex-h{ font-size:13px; font-weight:700; padding:8px 12px; color:#fff; }
  .ex-bd{ padding:10px 12px; font-size:13px; line-height:1.8; white-space:pre-wrap; word-break:break-word; color:#334155; }
  .ex-basic .ex-h{ background:#3b82f6; }
  .ex-basic .ex-bd{ background:#eff6ff; }
  .ex-adv .ex-h{ background:#8b5cf6; }
  .ex-adv .ex-bd{ background:#f5f3ff; }
  .ex-key .ex-h{ background:#22c55e; }
  .ex-key .ex-bd{ background:#f0fdf4; }

  .dlbar{ position:sticky; bottom:0; background:#fff; border-top:1px solid var(--line); padding:10px 12px; display:flex; align-items:center; gap:8px; z-index:5; }
  .dlbar .fmts{ display:flex; gap:5px; }
  .dlbar .fmt{ font-size:12px; padding:7px 9px; border-radius:10px; background:var(--chip); color:var(--sub); cursor:pointer; }
  .dlbar .fmt.on{ background:var(--brand); color:#fff; }
  .dlbar .btn{ flex:1; background:var(--brand); color:#fff; text-align:center; padding:13px 0; border-radius:13px; font-size:15px; font-weight:600; cursor:pointer; }
  .dlbar .fav{ font-size:24px; color:var(--brand); cursor:pointer; padding:0 6px; }
  .phead{ background:linear-gradient(160deg,var(--brand),var(--brand2)); border-radius:18px; padding:24px 18px; color:#fff; display:flex; align-items:center; gap:16px; margin-bottom:14px; }
  .pavatar{ width:62px; height:62px; border-radius:50%; background:rgba(255,255,255,.25); display:flex; align-items:center; justify-content:center; font-size:30px; overflow:hidden; border:2px solid rgba(255,255,255,.5); flex-shrink:0; }
  .pavatar img{ width:100%; height:100%; object-fit:cover; }
  .pname{ font-size:18px; font-weight:600; }
  .psub{ font-size:12px; opacity:.8; margin-top:4px; }
  .stats3{ display:flex; gap:10px; margin-bottom:14px; }
  .stat{ flex:1; background:#fff; border-radius:14px; padding:14px; text-align:center; box-shadow:0 2px 10px rgba(20,40,80,.05); }
  .stat .num{ font-size:22px; font-weight:700; color:var(--brand); }
  .stat .lbl{ font-size:12px; color:var(--sub); margin-top:4px; }
  .block{ background:#fff; border-radius:16px; padding:16px; margin-bottom:12px; box-shadow:0 2px 10px rgba(20,40,80,.05); }
  .block h3{ margin:0 0 12px; font-size:15px; display:flex; justify-content:space-between; align-items:center; }
  .block .clear{ font-size:12px; color:#c0392b; cursor:pointer; }
  .favitem{ display:flex; align-items:center; gap:10px; padding:9px 0; border-bottom:1px solid var(--line); cursor:pointer; }
  .favitem:last-child{ border-bottom:none; }
  .favitem .fi{ width:34px; height:34px; border-radius:9px; background:var(--chip); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0; }
  .favitem .ft{ font-size:13px; }
  .glabel{ font-size:12px; color:#888; padding:16px 4px 8px; display:flex; justify-content:space-between; }
  .glabel .clr{ color:#c0392b; cursor:pointer; }
  .toast{ position:fixed; left:50%; top:50%; transform:translate(-50%,-50%); background:rgba(0,0,0,.78); color:#fff; padding:12px 22px; border-radius:12px; font-size:14px; z-index:999; opacity:0; transition:opacity .25s; pointer-events:none; }
  .toast.show{ opacity:1; }
  .hint{ text-align:center; font-size:11px; color:#aab; padding:10px 0 4px; }
  .block p.rp{ margin:8px 0 0; font-size:13px; line-height:1.7; color:#3a4150; }
  .tip{ font-size:11px; color:#aab; text-align:center; margin-top:14px; line-height:1.6; }
</style>
</head>
<body>
<div class="phone">
  <div class="statusbar"><span>9:41</span><span class="icons">&#128246;&#128267;</span></div>
  <div class="navbar"><span class="back" id="backBtn" style="display:none">&#8249;</span><span id="navTitle">语文教案库</span></div>
  <div class="content" id="content"></div>
  <div class="tabbar" id="tabbar">
    <div class="tab on" data-tab="index" onclick="switchTab(&quot;index&quot;)"><div class="ico">&#128218;</div>教案库</div>
    <div class="tab" data-tab="favorites" onclick="switchTab(&quot;favorites&quot;)"><div class="ico">&#11088;</div>收藏</div>
    <div class="tab" data-tab="profile" onclick="switchTab(&quot;profile&quot;)"><div class="ico">&#128100;</div>我的</div>
  </div>
</div>
<div class="toast" id="toast"></div>
<script>
// ===== 数据（JSON安全嵌入）=====
const LESSONS = ${safeJsonStr(lessons)};

const BOOKS = [...new Set(LESSONS.map(function(l){ return l.book; }))];
const BOOK_ORDER = { '必修第一册':1, '必修第二册':2, '必修第三册':3 };
const BOOK_SHORT = { '必修第一册':'必修一', '必修第二册':'必修二', '必修第三册':'必修三' };

// ===== 状态管理 =====
let state = {
  tab: 'index',
  filterBook: '',
  detailId: null,
  privacy: false,
  keyword: '',
  history: [],
  favFmt: 'word',
  downloads: [],
  recents: [],
  favorites: [],
  profile: { nickName: '微信用户', avatarUrl: '' }
};

// ===== 工具函数 =====
function $(id) { return document.getElementById(id); }

function toast(msg) {
  const t = $('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(function(){ t.classList.remove('show'); }, 1400);
}

function getLesson(id) { return LESSONS.find(function(l){ return l.id === id; }); }



function escAttr(s) {
  return String(s || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function renderStepContent(raw) {
  const s = (raw || '').trim();
  if (!s) return '';
  const MARK = /(【PPT[^】]*】|【音频[^】]*】|【教师[^】]*】|教师[:：]|【预设回答[^】]*】|预设回答[:：]|【板书时机[^】]*】|板书时机[:：]|【差异化提示[^】]*】|差异化提示[:：]|【易错点提醒[^】]*】|易错点提醒[:：])/g;
  const parts = s.split(MARK);
  let out = '';
  if (parts[0] && parts[0].trim()) out += '<div class="sc-text">' + escAttr(parts[0].trim()) + '</div>';
  for (let i = 1; i < parts.length; i += 2) {
    const marker = parts[i];
    const text = (parts[i + 1] || '').trim();
    if (!marker) continue;
    out += stepBlock(marker, text);
  }
  return out || ('<div class="sc-text">' + escAttr(s) + '</div>');
}
function stepBlock(marker, text) {
  const t = marker.replace(/^【|】$/g, '');
  if (/^PPT/.test(t)) return '<div class="sc-block sc-ppt"><span class="sc-tag">' + escAttr(marker) + '</span>' + (text ? '<div class="sc-bd">' + escAttr(text) + '</div>' : '') + '</div>';
  if (/^音频/.test(t)) return '<div class="sc-block sc-audio"><span class="sc-tag">' + escAttr(marker) + '</span>' + (text ? '<div class="sc-bd">' + escAttr(text) + '</div>' : '') + '</div>';
  if (/^教师/.test(t)) return '<div class="sc-block sc-teacher"><span class="sc-tag">' + escAttr(marker) + '</span><div class="sc-bd">' + escAttr(text) + '</div></div>';
  if (/^预设回答/.test(t)) return '<div class="sc-block sc-ans"><span class="sc-tag">' + escAttr(marker) + '</span><div class="sc-bd">' + escAttr(text) + '</div></div>';
  if (/^板书时机/.test(t)) return '<div class="sc-block sc-board"><span class="sc-tag">' + escAttr(marker) + '</span><div class="sc-bd">' + escAttr(text) + '</div></div>';
  if (/^差异化提示/.test(t)) return '<div class="sc-block sc-diff"><span class="sc-tag">' + escAttr(marker) + '</span><div class="sc-bd">' + escAttr(text) + '</div></div>';
  if (/^易错点提醒/.test(t)) return '<div class="sc-block sc-warn"><span class="sc-tag">' + escAttr(marker) + '</span><div class="sc-bd">' + escAttr(text) + '</div></div>';
  return '<div class="sc-text">' + escAttr(marker + text) + '</div>';
}
function renderExercises(raw) {
  const s = (raw || '').trim();
  if (!s) return '';
  const basic = s.match(/【基础作业】([^]*?)(?=【提高作业】|【参考答案|$)/);
  const adv = s.match(/【提高作业】([^]*?)(?=【参考答案】|$)/);
  const ans = s.match(/【参考答案[^】]*】([^]*?)$/);
  let out = '';
  if (basic) out += '<div class="ex-block ex-basic"><div class="ex-h">📝 基础作业</div><div class="ex-bd">' + escAttr(basic[1].trim()) + '</div></div>';
  if (adv) out += '<div class="ex-block ex-adv"><div class="ex-h">🚀 提高作业</div><div class="ex-bd">' + escAttr(adv[1].trim()) + '</div></div>';
  if (ans) out += '<div class="ex-block ex-key"><div class="ex-h">🔑 参考答案（教师用）</div><div class="ex-bd">' + escAttr(ans[1].trim()) + '</div></div>';
  return out || ('<div class="sc-text">' + escAttr(s) + '</div>');
}

function setNav(title, showBack) {
  $('navTitle').textContent = title;
  $('backBtn').style.display = showBack ? 'block' : 'none';
}

// ===== 导航 =====
function switchTab(tab) {
  state.tab = tab;
  state.detailId = null;
  state.privacy = false;
  document.querySelectorAll('.tab').forEach(function(t){ t.classList.toggle('on', t.dataset.tab === tab); });
  setNav('语文教案库', false);
  const bar = document.querySelector('.dlbar');
  if (bar) bar.remove();
  render();
}

function goBack() {
  if (state.detailId) state.detailId = null;
  else if (state.privacy) state.privacy = false;
  render();
}

function openDetail(id) {
  state.detailId = id;
  if (state.recents.indexOf(id) < 0) {
    state.recents.unshift(id);
    if (state.recents.length > 50) state.recents.pop();
  }
  render();
}

function toggleFav(id) {
  const i = state.favorites.indexOf(id);
  if (i >= 0) {
    state.favorites.splice(i, 1);
    toast('已取消收藏');
  } else {
    state.favorites.unshift(id);
    toast('★ 已收藏');
  }
  render();
}

// ===== 渲染入口 =====
function render() {
  const tab = state.tab;
  if (state.detailId) { renderDetail(); return; }
  if (state.privacy) { renderPrivacy(); return; }
  if (tab === 'index') renderIndex();
  else if (tab === 'favorites') renderFavorites();
  else if (tab === 'profile') renderProfile();
}

// ===== 教案库页面（册 → 单元 → 板块，按书本顺序）=====
function renderIndex() {
  setNav('英语教案库', false);
  let list = LESSONS.slice();
  if (state.filterBook) list = list.filter(function(l){ return l.book === state.filterBook; });
  if (state.keyword.trim()) {
    const kw = state.keyword.trim().toLowerCase();
    list = list.filter(function(l) {
      const hay = (l.title + ' ' + l.unitTitle + ' ' + (l.tags || []).join(' ') + ' ' + (l.overview || '') + ' ' +
        (l.keyPoints || '') + ' ' + (l.difficulties || '') + ' ' + (l.preparation || '') + ' ' +
        (l.objectives || []).join(' ') + ' ' + (l.process || []).map(function(s){ return s.step + ' ' + s.content; }).join(' ') + ' ' +
        (l.exercises || '') + ' ' + (l.reflection || '') + ' ' + (l.blackboard || '')).toLowerCase();
      return hay.indexOf(kw) !== -1;
    });
  }

  list = list.slice().sort(function(a, b) {
    return ((BOOK_ORDER[a.book] || 0) - (BOOK_ORDER[b.book] || 0)) ||
      (a.unitNumber - b.unitNumber) ||
      ((a.periodNumber || 0) - (b.periodNumber || 0));
  });

  // 按 册+单元 分组（"全部"时 unitNumber 跨册重复，必须用册区分）
  const map = {};
  list.forEach(function(l) {
    const key = l.book + '|' + l.unitNumber;
    if (!map[key]) map[key] = { key: key, book: l.book, bookShort: BOOK_SHORT[l.book] || l.book, unitNumber: l.unitNumber, unitTitle: l.unitTitle, lessons: [] };
    map[key].lessons.push(l);
  });
  const groups = Object.keys(map).map(function(k){ return map[k]; }).sort(function(a, b) {
    return ((BOOK_ORDER[a.book] || 0) - (BOOK_ORDER[b.book] || 0)) || (a.unitNumber - b.unitNumber);
  });

  const TYPE_ICON = { 'listening-speaking':'🎧', 'reading':'📖', 'grammar':'✏️', 'listening-talking':'💬', 'writing':'✍️', 'project':'🎯' };
  const TYPE_BG = { 'listening-speaking':'#6b46c1', 'reading':'#1a365d', 'grammar':'#1a6840', 'listening-talking':'#b7791f', 'writing':'#7b341e', 'project':'#2c5282' };

  const bookChips = '<div class="chip ' + (state.filterBook ? '' : 'on') + '" data-book="">全部</div>' +
    BOOKS.map(function(b) {
      return '<div class="chip ' + (state.filterBook === b ? 'on' : '') + '" data-book="' + escAttr(b) + '">' + escAttr(b) + '</div>';
    }).join('');

  const groupHtml = groups.map(function(g) {
    const cards = g.lessons.map(function(l) {
      const fav = state.favorites.indexOf(l.id) >= 0;
      const ico = TYPE_ICON[l.lessonType] || '📄';
      const bg = TYPE_BG[l.lessonType] || '#555';
      const star = fav ? '<div style="color:#e6a23c;font-size:20px">★</div>' : '';
      return '<div class="card" data-id="' + escAttr(l.id) + '">' +
        '<div class="row1">' +
          '<div class="docico" style="background:linear-gradient(135deg,' + bg + ',' + bg + 'dd)">' + ico + '</div>' +
          '<div style="flex:1">' +
            '<div class="ttl">' + escAttr(l.title) + '</div>' +
            '<div class="sub">' + escAttr(l.lessonTypeName) + ' · ' + l.duration + '分钟</div>' +
          '</div>' +
          star +
          '<div class="card-arrow">›</div>' +
        '</div>' +
      '</div>';
    }).join('');

    return '<div class="unit-group">' +
      '<div class="unit-head"><span class="unit-no">' + escAttr(g.bookShort) + ' · Unit ' + g.unitNumber + '</span><span class="unit-name">' + escAttr(g.unitTitle) + '</span></div>' +
      cards +
    '</div>';
  }).join('');

  const histHtml = (!state.keyword.trim() && state.history.length)
    ? '<div class="chips">' + state.history.map(function(h){ return '<div class="chip" data-hist="' + escAttr(h) + '">' + escAttr(h) + '</div>'; }).join('') + '</div>'
    : '';
  const searchVal = escAttr(state.keyword);
  $('content').innerHTML =
    '<div class="search">🔍 <input class="sin" placeholder="搜索教案/单元/关键词" value="' + searchVal + '"> ' + (state.keyword ? '<span class="searchx" data-clear="search">✕</span>' : '') + '</div>' +
    histHtml +
    '<div class="chips">' + bookChips + '</div>' +
    (groupHtml || '<div class="empty"><div class="e">📭</div><div class="t">没有匹配的教案</div><div class="p">换个关键词或筛选条件试试</div></div>');
}

function setBook(b) { state.filterBook = b; renderIndex(); }
function onPrevSearch(kw) {
  state.keyword = kw;
  const t = kw.trim();
  if (t && state.history[0] !== t) {
    state.history = [t].concat(state.history.filter(function(x){ return x !== t; })).slice(0, 10);
  }
  renderIndex();
}
function onPrevHistory(h) { state.keyword = h; renderIndex(); }
function onPrevClear() { state.keyword = ''; renderIndex(); }

// ===== 收藏页面 =====
function renderFavorites() {
  setNav('我的收藏', false);
  let cards = '';
  state.favorites.forEach(function(id) {
    const l = getLesson(id);
    if (!l) return;
    cards += '<div class="card" data-id="' + escAttr(l.id) + '">' +
      '<div class="row1"><div class="docico">📄</div>' +
      '<div style="flex:1"><div class="ttl">' + escAttr(l.title) + '</div><div class="sub">' + escAttr(l.book) + ' · ' + escAttr(l.unitTitle) + ' · ' + escAttr(l.lessonTypeName) + '</div></div>' +
      '<div style="color:#c0392b;font-size:22px;cursor:pointer" data-fav-id="' + escAttr(l.id) + '">✕</div>' +
      '</div></div>';
  });
  $('content').innerHTML =
    '<div class="glabel"><span>已收藏 ' + state.favorites.length + ' 篇</span>' + (state.favorites.length ? '<span class="clr" onclick="clearAll(&quot;fav&quot;)">清空</span>' : '') + '</div>' +
    (cards || '<div class="empty"><div class="e">★</div><div class="t">还没有收藏</div><div class="p">在教案详情页点 ☆ 即可收藏</div></div>');
}

// ===== 我的页面 =====
function renderProfile() {
  setNav('我的', false);
  const p = state.profile;
  let dl = '';
  state.downloads.forEach(function(id) {
    const l = getLesson(id); if (!l) return;
    dl += '<div class="favitem" data-id="' + escAttr(l.id) + '"><div class="fi">📄</div><div class="ft">' + escAttr(l.title) + '</div></div>';
  });
  let rl = '';
  state.recents.forEach(function(id) {
    const l = getLesson(id); if (!l) return;
    rl += '<div class="favitem" data-id="' + escAttr(l.id) + '"><div class="fi">📄</div><div class="ft">' + escAttr(l.title) + '</div></div>';
  });
  let html = '';
  html += '<div class="phead"><div class="pavatar">' + (p.avatarUrl ? '<img src="' + escAttr(p.avatarUrl) + '">' : '👤') + '</div><div><div class="pname">' + escAttr(p.nickName) + '</div><div class="psub">微信用户 · 云端已同步</div></div></div>';
  html += '<div class="stats3"><div class="stat"><div class="num">' + state.favorites.length + '</div><div class="lbl">收藏</div></div><div class="stat"><div class="num">' + state.downloads.length + '</div><div class="lbl">下载</div></div><div class="stat"><div class="num">' + state.recents.length + '</div><div class="lbl">最近</div></div></div>';
  html += '<div class="block"><h3>📥 下载记录 <span class="clear" onclick="clearAll(&quot;dl&quot;)">清空</span></h3>' + (dl || '<div class="hint">暂无下载记录</div>') + '</div>';
  html += '<div class="block"><h3>🕑 浏览历史 <span class="clear" onclick="clearAll(&quot;rc&quot;)">清空</span></h3>' + (rl || '<div class="hint">暂无浏览历史</div>') + '</div>';
  html += '<div class="block"><h3>⚙ 设置</h3><div class="favitem" onclick="showPrivacy()"><div class="fi">🔒</div><div class="ft">隐私保护说明</div></div><div class="favitem" onclick="clearAll(&quot;all&quot;)"><div class="fi">🗑</div><div class="ft">清空全部本地数据</div></div></div>';
  html += '<div class="hint">此预览版数据仅存于当前页面，刷新即丢失。真机数据存储于微信云开发。</div>';
  $('content').innerHTML = html;
}

// ===== 隐私说明页 =====
function showPrivacy() { state.privacy = true; render(); }

function renderPrivacy() {
  setNav('隐私保护说明', true);
  const blocks = [
    { h: '我们收集哪些信息', p: [ '· 昵称、头像：你主动设置，用于「我的」页身份展示。', '· 收藏 / 下载记录 / 浏览历史：使用教案库时产生的操作记录，用于多设备同步与个性化展示。', '· 错误日志：应用崩溃时的堆栈摘要，仅用于修复问题，不含任何教学内容。' ] },
    { h: '信息存储在哪里', p: [ '所有数据默认存储于微信云开发（腾讯云）或本机缓存。我们不自建服务器，不向任何第三方出售或共享你的个人信息。' ] },
    { h: '你有哪些权利', p: [ '· 可随时在「我的」页清空下载记录、浏览历史或收藏。', '· 可一键清空全部个人数据。', '· 可在微信「设置 › 隐私 › 授权管理」中撤回本小程序的信息授权。' ] },
    { h: '联系方式', p: [ '如对本说明有疑问，可通过小程序内反馈渠道联系开发者。' ] }
  ];
  let html = '<div class="hint" style="text-align:left;padding:4px 2px 10px">最后更新：2026-07</div>';
  blocks.forEach(function(b) {
    html += '<div class="block"><h3>' + b.h + '</h3>' + b.p.map(function(x){ return '<p class="rp">' + escAttr(x) + '</p>'; }).join('') + '</div>';
  });
  html += '<div class="tip">本说明依据《中华人民共和国个人信息保护法》及微信平台隐私规范编写。</div>';
  $('content').innerHTML = html;
}

// ===== 详情页 =====
function renderDetail() {
  const l = getLesson(state.detailId);
  if (!l) { state.detailId = null; render(); return; }
  setNav((l.lessonTypeName || '教案详情'), true);

  const CN = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'];
  const secs = [];
  let si = 0;
  const add = function(name, payload) { if (payload) { si++; secs.push(Object.assign({ no: CN[si - 1], name: name, key: name }, payload)); } };
  add('教材分析', l.textbookAnalysis && { body: l.textbookAnalysis });
  add('学情分析', l.overview && { body: l.overview });
  add('教学目标', l.objectives && l.objectives.length && { list: l.objectives });
  add('教学重点', l.keyPoints && { body: l.keyPoints });
  add('教学难点', l.difficulties && { body: l.difficulties });
  add('教学方法', l.teachingMethods && { body: l.teachingMethods });
  add('课前准备', l.preparation && { body: l.preparation });
  add('教学过程', l.process && l.process.length && { steps: l.process.map(function(s, i){ return { n: i + 1, name: s.step || s.name || ('步骤' + (i + 1)), time: s.time || '', content: s.content || '' }; }) });
  add('板书设计', l.blackboard && { body: l.blackboard });
  add('课后练习', l.exercises && { html: renderExercises(l.exercises) });
  add('教学反思', l.reflection && { body: l.reflection });

  let secHtml = '';
  secs.forEach(function(sec) {
    if (sec.list) {
      secHtml += '<div class="sec"><h3><span class="sno">' + sec.no + '</span>' + sec.name + '<span class="scopy" data-copy-key="' + escAttr(sec.key) + '">复制</span></h3><ul>' + sec.list.map(function(x){ return '<li>' + escAttr(x) + '</li>'; }).join('') + '</ul></div>';
    } else if (sec.steps) {
      let stepsHtml = '';
      sec.steps.forEach(function(s) {
        stepsHtml += '<div class="step"><div class="sn"><span class="sno sm">' + s.n + '</span>' + escAttr(s.name) + '<span class="st">' + escAttr(s.time) + '</span></div>' + renderStepContent(s.content) + '</div>';
      });
      secHtml += '<div class="sec"><h3><span class="sno">' + sec.no + '</span>' + sec.name + '<span class="scopy" data-copy-key="' + escAttr(sec.key) + '">复制</span></h3>' + stepsHtml + '</div>';
    } else if (sec.html) {
      secHtml += '<div class="sec"><h3><span class="sno">' + sec.no + '</span>' + sec.name + '<span class="scopy" data-copy-key="' + escAttr(sec.key) + '">复制</span></h3>' + sec.html + '</div>';
    } else {
      secHtml += '<div class="sec"><h3><span class="sno">' + sec.no + '</span>' + sec.name + '<span class="scopy" data-copy-key="' + escAttr(sec.key) + '">复制</span></h3><p>' + escAttr(sec.body) + '</p></div>';
    }
  });

  const fav = state.favorites.indexOf(l.id) >= 0;
  const fid = escAttr(l.id);

  let html = '';
  html += '<div class="hero">';
  html += '  <div class="badges2"><span class="badge2">' + escAttr(l.book) + '</span><span class="badge2">' + escAttr(l.lessonTypeName) + '</span><span class="badge2">' + l.duration + '分钟</span></div>';
  html += '  <h1>' + escAttr(l.title) + '</h1>';
  html += '  <div class="hsub">' + escAttr(l.unitTitle) + '</div>';
  html += '  <div class="hstat">浏览 ' + (l.viewCount || 0) + ' · 下载 ' + (l.downloadCount || 0) + '</div>';
  html += '</div>';
  html += secHtml;
  html += '<div class="hint" style="margin-top:8px">— 以下为小程序下载栏，预览中点击会提示效果 —</div><div style="height:70px"></div>';

  $('content').innerHTML = html;

  let bar = document.querySelector('.dlbar');
  if (bar) bar.remove();
  bar = document.createElement('div');
  bar.className = 'dlbar';
  bar.innerHTML =
    '<span class="fav" data-fav-id="' + fid + '">' + (fav ? '★' : '☆') + '</span>' +
    '<div class="fmts">' +
      '<span class="fmt ' + (state.favFmt === 'word' ? 'on' : '') + '" data-fmt="word">Word</span>' +
      '<span class="fmt ' + (state.favFmt === 'pdf' ? 'on' : '') + '" data-fmt="pdf">PDF</span>' +
      '<span class="fmt ' + (state.favFmt === 'ppt' ? 'on' : '') + '" data-fmt="ppt">PPT</span>' +
    '</div>' +
    '<div class="btn" data-dl-id="' + fid + '">⬇ 下载 ' + state.favFmt.toUpperCase() + '</div>';
  $('content').appendChild(bar);
}

function setFmt(f) { state.favFmt = f; renderDetail(); }
function copySection(key) { toast('已复制本节（预览版）'); }

function doDownload(id) {
  const l = getLesson(id);
  if (l && state.downloads.indexOf(id) < 0) state.downloads.unshift(id);
  toast('已生成 ' + state.favFmt.toUpperCase() + '（预览：实际会在微信中打开文件）');
  renderDetail();
}

// ===== 清空操作 =====
function clearAll(kind) {
  if (kind === 'fav') { state.favorites = []; toast('已清空收藏'); }
  else if (kind === 'dl') { state.downloads = []; toast('已清空下载'); }
  else if (kind === 'rc') { state.recents = []; toast('已清空浏览'); }
  else if (kind === 'all') { state.favorites = []; state.downloads = []; state.recents = []; toast('已清空全部'); }
  render();
}

// ===== 初始化演示数据 & 首次渲染 =====
$('backBtn').addEventListener('click', goBack);
$('content').addEventListener('click', function(e) {
  var t = e.target.closest('[data-id]'); if (t) { openDetail(t.getAttribute('data-id')); return; }
  var f = e.target.closest('[data-fav-id]'); if (f) { toggleFav(f.getAttribute('data-fav-id')); return; }
  var c = e.target.closest('[data-copy-key]'); if (c) { copySection(c.getAttribute('data-copy-key')); return; }
  var b = e.target.closest('[data-book]'); if (b) { setBook(b.getAttribute('data-book')); return; }
  var h = e.target.closest('[data-hist]'); if (h) { onPrevHistory(h.getAttribute('data-hist')); return; }
  var x = e.target.closest('[data-clear]'); if (x) { onPrevClear(); return; }
  var m = e.target.closest('[data-fmt]'); if (m) { setFmt(m.getAttribute('data-fmt')); return; }
  var d = e.target.closest('[data-dl-id]'); if (d) { doDownload(d.getAttribute('data-dl-id')); return; }
});
$('content').addEventListener('change', function(e) {
  if (e.target.classList.contains('sin')) { onPrevSearch(e.target.value); }
});

state.downloads = ['l-cn-bs-u1-1', 'l-cn-bs-u1-2'];
state.recents = ['l-cn-bs-u1-1', 'l-cn-bs-u2-1', 'l-cn-bx-u1-1'];
state.favorites = ['l-cn-bs-u1-3'];
render();
</script>
</body>
</html>`;

const outPath = path.join(__dirname, '..', 'miniprogram-cn-preview.html');
fs.writeFileSync(outPath, html, 'utf8');

// 验证生成的JS是否合法
const outHtml = fs.readFileSync(outPath, 'utf8');
const scriptMatch = outHtml.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
  try {
    new Function(scriptMatch[1]);
    console.log('✅ JS syntax check: PASSED');
  } catch (e) {
    console.error('❌ JS syntax check: FAILED -', e.message);
  }
}

console.log('Written:', outPath, Math.round(html.length / 1024) + 'KB');
