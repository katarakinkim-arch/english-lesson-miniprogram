// 生成浏览器可预览的小程序模拟版 HTML
// 核心修复：生成的 JS 使用模板字符串（backtick）拼接 HTML，彻底避免嵌套引号问题
const fs = require('fs');
const path = require('path');

const miniDir = path.join(__dirname, '..');
const lessons = require(path.join(miniDir, 'data', 'lessons.js'));

// 安全嵌入 JSON 到 JS：转义 </ 防止闭合 script 标签，转义反引号和 ${ 防止破坏模板字符串
function safeJsonStr(obj) {
  return JSON.stringify(obj)
    .replace(/</g, '\\x3c')
    .replace(/`/g, '\\`')
    .replace(/\$\{/g, '\\${');
}

const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<title>英语教案小程序 · 预览</title>
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
  .tabbar{ height:60px; background:#fff; border-top:1px solid var(--line); display:flex; flex-shrink:0; }
  .tab{ flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#9aa1ad; font-size:11px; gap:3px; cursor:pointer; -webkit-user-select:none; user-select:none; }
  .tab .ico{ font-size:21px; }
  .tab.on{ color:var(--brand); }
  .search{ background:#fff; border-radius:14px; padding:11px 14px; display:flex; align-items:center; gap:8px; color:var(--sub); font-size:14px; box-shadow:0 2px 10px rgba(20,40,80,.05); }
  .chips{ display:flex; gap:8px; margin:12px 0; flex-wrap:wrap; }
  .chip{ background:var(--chip); color:var(--sub); font-size:13px; padding:7px 14px; border-radius:20px; cursor:pointer; white-space:nowrap; }
  .chip.on{ background:var(--brand); color:#fff; }
  .card{ background:#fff; border-radius:16px; padding:15px; margin-bottom:12px; box-shadow:0 2px 10px rgba(20,40,80,.05); cursor:pointer; transition:transform .15s; }
  .card:active{ transform:scale(.98); }
  .card .row1{ display:flex; gap:12px; }
  .card .docico{ width:44px; height:44px; border-radius:12px; background:linear-gradient(135deg,var(--brand),var(--brand2)); color:#fff; display:flex; align-items:center; justify-content:center; font-size:22px; flex-shrink:0; }
  .card .ttl{ font-size:15px; font-weight:600; line-height:1.35; }
  .card .sub{ font-size:12px; color:var(--sub); margin-top:5px; }
  .card .desc{ font-size:12px; color:#8a90a0; margin-top:9px; line-height:1.5; }
  .card .foot{ display:flex; align-items:center; justify-content:space-between; margin-top:11px; }
  .badges{ display:flex; gap:6px; }
  .badge{ font-size:11px; padding:3px 9px; border-radius:8px; background:#eef2f8; color:var(--brand); }
  .stats{ font-size:11px; color:#aab; }
  .empty{ text-align:center; color:var(--sub); padding:60px 20px; }
  .empty .e{ font-size:54px; }
  .empty .t{ margin-top:12px; font-size:15px; }
  .empty .p{ margin-top:6px; font-size:12px; color:#b3b8c4; }
  .hero{ margin:-14px -14px 14px; padding:26px 18px 20px; background:linear-gradient(160deg,var(--brand),var(--brand2)); color:#fff; border-radius:0 0 22px 22px; }
  .hero .badges2{ display:flex; gap:8px; margin-bottom:14px; }
  .hero .badge2{ font-size:12px; padding:4px 11px; border-radius:9px; background:rgba(255,255,255,.18); }
  .hero h1{ font-size:20px; margin:0 0 8px; line-height:1.35; }
  .hero .hsub{ font-size:13px; opacity:.85; }
  .hero .hstat{ font-size:12px; opacity:.8; margin-top:12px; }
  .sec{ background:#fff; border-radius:16px; padding:16px; margin-bottom:12px; box-shadow:0 2px 10px rgba(20,40,80,.05); }
  .sec h3{ margin:0 0 12px; font-size:15px; display:flex; align-items:center; gap:8px; color:var(--brand); }
  .sno{ flex-shrink:0; width:24px; height:24px; line-height:24px; text-align:center; background:linear-gradient(135deg,var(--brand),var(--brand2)); color:#fff; border-radius:50%; font-size:13px; font-weight:700; }
  .sno.sm{ width:20px; height:20px; line-height:20px; font-size:12px; }
  .sec p{ margin:0; font-size:13px; line-height:1.7; color:#3a4150; white-space:pre-wrap; word-break:break-word; }
  .sec ul{ margin:0; padding-left:18px; }
  .sec li{ font-size:13px; line-height:1.7; color:#3a4150; margin-bottom:4px; }
  .step{ background:#f7f9fc; border-left:4px solid var(--brand2); border-radius:12px; padding:10px 12px; margin-bottom:12px; }
  .step .sn{ font-size:13px; font-weight:600; color:var(--brand); display:flex; align-items:center; gap:7px; flex-wrap:wrap; }
  .step .st{ font-size:11px; color:#fff; background:var(--brand2); border-radius:7px; padding:1px 8px; margin-left:4px; }
  .step p{ margin:6px 0 0; font-size:12.5px; line-height:1.6; color:#444; white-space:pre-wrap; word-break:break-word; }
  .dlbar{ position:sticky; bottom:0; background:#fff; border-top:1px solid var(--line); padding:10px 12px; display:flex; align-items:center; gap:8px; z-index:10; }
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
</style>
</head>
<body>
<div class="phone">
  <div class="statusbar"><span>9:41</span><span class="icons">&#128246;&#128267;</span></div>
  <div class="navbar"><span class="back" id="backBtn" style="display:none">&#8249;</span><span id="navTitle">英语教案库</span></div>
  <div class="content" id="content"></div>
  <div class="tabbar" id="tabbar">
    <div class="tab on" data-tab="index" onclick="switchTab('index')"><div class="ico">&#128218;</div>教案库</div>
    <div class="tab" data-tab="favorites" onclick="switchTab('favorites')"><div class="ico">&#11088;</div>收藏</div>
    <div class="tab" data-tab="profile" onclick="switchTab('profile')"><div class="ico">&#128100;</div>我的</div>
  </div>
</div>
<div class="toast" id="toast"></div>
<script>
// ===== 数据（JSON安全嵌入）=====
const LESSONS = ${safeJsonStr(lessons)};

const BOOKS = [...new Set(LESSONS.map(l => l.book))];
const TYPES = [...new Set(LESSONS.map(l => l.lessonType))];

// ===== 状态管理 =====
let state = {
  tab: 'index',
  filterBook: '',
  filterType: '',
  detailId: null,
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
  setTimeout(() => t.classList.remove('show'), 1400);
}

function getLesson(id) { return LESSONS.find(l => l.id === id); }

function clip(s, n) {
  s = String(s || '').replace(/\\s+/g, ' ').trim();
  return s.length > n ? s.slice(0, n) + '\u2026' : s;
}

function escAttr(s) {
  // 转义HTML属性值中的特殊字符，防止XSS和属性断裂
  return String(s || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function setNav(title, showBack) {
  $('navTitle').textContent = title;
  $('backBtn').style.display = showBack ? 'block' : 'none';
}

// ===== 导航 =====
function switchTab(tab) {
  state.tab = tab;
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('on', t.dataset.tab === tab));
  render();
}

function goBack() {
  state.detailId = null;
  render();
}

function openDetail(id) {
  state.detailId = id;
  if (!state.recents.includes(id)) {
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
    toast('\u2605 已收藏');
  }
  render();
}

// ===== 渲染入口 =====
function render() {
  const tab = state.tab;
  if (state.detailId) { renderDetail(); return; }
  if (tab === 'index') renderIndex();
  else if (tab === 'favorites') renderFavorites();
  else if (tab === 'profile') renderProfile();
}

// ===== 教案库页面 =====
function renderIndex() {
  setNav('英语教案库', false);
  let list = LESSONS.slice();
  if (state.filterBook) list = list.filter(l => l.book === state.filterBook);
  if (state.filterType) list = list.filter(l => l.lessonType === state.filterType);

  // 筛选标签
  const bookChips = [\`<div class="chip \${!state.filterBook ? 'on' : ''}" onclick="setBook('')">全部</div>\`]
    .concat(BOOKS.map(b => \`<div class="chip \${state.filterBook === b ? 'on' : ''}" onclick="setBook(\\\`\${escAttr(b)}\\\`)">\${escAttr(b)}</div>\`))
    .join('');
  const typeChips = [\`<div class="chip \${!state.filterType ? 'on' : ''}" onclick="setType('')">全部</div>\`]
    .concat(TYPES.map(t => \`<div class="chip \${state.filterType === t ? 'on' : ''}" onclick="setType(\\\`\${escAttr(t)}\\\`)">\${escAttr(t)}</div>\`))
    .join('');

  // 卡片列表（使用模板字符串避免引号地狱）
  const cards = list.map(l => {
    const fav = state.favorites.includes(l.id);
    return \`
    <div class="card" onclick="openDetail(\\\`\${escAttr(l.id)}\\\`)">
      <div class="row1">
        <div class="docico">&#128196;</div>
        <div style="flex:1">
          <div class="ttl">\${escAttr(l.title)}</div>
          <div class="sub">\${escAttr(l.book)} \u00B7 \${escAttr(l.unitTitle)} \u00B7 \${escAttr(l.lessonTypeName)} \u00B7 \${l.duration}\u5206\u949F</div>
        </div>
        \${fav ? '<div style="color:#e6a23c;font-size:20px">\u2605</div>' : ''}
      </div>
      <div class="desc">\${escAttr(clip(l.overview, 70))}</div>
      <div class="foot">
        <div class="badges">
          <span class="badge">Word</span><span class="badge">PDF</span><span class="badge">PPT</span>
        </div>
        <div class="stats">\uD83D\uDCC1 \${l.viewCount||0} \u00B7 \u2B07 \${l.downloadCount||0}</div>
      </div>
    </div>\`;
  }).join('');

  $('content').innerHTML = \`
    <div class="search">&#128269; 搜索教案（预览版无实际搜索）</div>
    <div class="chips">\${bookChips}</div>
    <div class="chips">\${typeChips}</div>
    \${cards || '<div class="empty"><div class="e">&#128420;</div><div class="t">没有匹配的教案</div></div>'}
  \`;
}

function setBook(b) { state.filterBook = b; renderIndex(); }
function setType(t) { state.filterType = t; renderIndex(); }

// ===== 收藏页面 =====
function renderFavorites() {
  setNav('我的收藏', false);
  const cards = state.favorites.map(id => {
    const l = getLesson(id);
    if (!l) return '';
    return \`
    <div class="card" onclick="openDetail(\\\`\${escAttr(l.id)}\\\`)">
      <div class="row1">
        <div class="docico">&#128196;</div>
        <div style="flex:1">
          <div class="ttl">\${escAttr(l.title)}</div>
          <div class="sub">\${escAttr(l.book)} \u00B7 \${escAttr(l.unitTitle)} \u00B7 \${escAttr(l.lessonTypeName)}</div>
        </div>
        <div style="color:#c0392b;font-size:22px;cursor:pointer"
             onclick="event.stopPropagation();toggleFav(\\\`\${escAttr(l.id)}\\\`)">\u2715</div>
      </div>
    </div>\`;
  }).join('');

  $('content').innerHTML = \`
    <div class="glabel"><span>已收藏 \${state.favorites.length} \u7BC7</span>\${state.favorites.length ? '<span class="clr" onclick="clearAll(\\'fav\\')">清空</span>' : ''}</div>
    \${cards || '<div class="empty"><div class="e">&#11088;</div><div class="t">还没有收藏</div><div class="p">在教案详情页点 \u2606 即可收藏</div></div>'}
  \`;
}

// ===== 我的页面 =====
function renderProfile() {
  setNav('我的', false);
  const p = state.profile;

  const dl = state.downloads.map(id => {
    const l = getLesson(id);
    if (!l) return '';
    return \`<div class="favitem" onclick="openDetail(\\\`\${escAttr(l.id)}\\\`)"><div class="fi">&#128196;</div><div class="ft">\${escAttr(l.title)}</div></div>\`;
  }).join('');

  const rl = state.recents.map(id => {
    const l = getLesson(id);
    if (!l) return '';
    return \`<div class="favitem" onclick="openDetail(\\\`\${escAttr(l.id)}\\\`)"><div class="fi">&#128196;</div><div class="ft">\${escAttr(l.title)}</div></div>\`;
  }).join('');

  $('content').innerHTML = \`
    <div class="phead">
      <div class="pavatar">\${p.avatarUrl ? '<img src="' + escAttr(p.avatarUrl) + '">' : '&#128100;'}</div>
      <div>
        <div class="pname">\${escAttr(p.nickName)}</div>
        <div class="psub">微信用户 \u00B7 云端已同步</div>
      </div>
    </div>
    <div class="stats3">
      <div class="stat"><div class="num">\${state.favorites.length}</div><div class="lbl">收藏</div></div>
      <div class="stat"><div class="num">\${state.downloads.length}</div><div class="lbl">下载</div></div>
      <div class="stat"><div class="num">\${state.recents.length}</div><div class="lbl">最近</div></div>
    </div>
    <div class="block">
      <h3>&#128229; 下载记录 <span class="clear" onclick="clearAll(\\'dl\\')">清空</span></h3>
      \${dl || '<div class="hint">暂无下载记录</div>'}
    </div>
    <div class="block">
      <h3>&#128340; 浏览历史 <span class="clear" onclick="clearAll(\\'rc\\')">清空</span></h3>
      \${rl || '<div class="hint">暂无浏览记录</div>'}
    </div>
    <div class="block">
      <h3>&#9881; 数据管理</h3>
      <div class="favitem" onclick="clearAll(\\'all\\')"><div class="fi">&#128465;</div><div class="ft">清空全部本地数据</div></div>
    </div>
    <div class="hint">此预览版数据仅存于当前页面，刷新即丢失。真机数据存储于微信云开发。</div>
  \`;
}

// ===== 详情页 =====
function renderDetail() {
  const l = getLesson(state.detailId);
  if (!l) { state.detailId = null; render(); return; }
  setNav(l.lessonTypeName || '教案详情', true);

  // 构建各板块（中文序号，与小程序精美版一致）
  const CN = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'];
  const secs = [];
  let si = 0;
  const add = (name, payload) => { if (payload) { si++; secs.push(Object.assign({ no: CN[si - 1], name: name }, payload)); } };
  add('教材分析与学情', l.overview && { body: l.overview });
  add('教学目标', l.objectives && l.objectives.length && { list: l.objectives });
  add('教学重点', l.keyPoints && { body: l.keyPoints });
  add('教学难点', l.difficulties && { body: l.difficulties });
  add('课前准备', l.preparation && { body: l.preparation });
  add('教学过程', l.process && l.process.length && { steps: l.process.map((s, i) => ({ n: i + 1, name: s.step || s.name || ('步骤' + (i + 1)), time: s.time || '', content: s.content || '' })) });
  add('板书设计', l.blackboard && { body: l.blackboard });
  add('课后练习', l.exercises && { body: l.exercises });
  add('教学反思', l.reflection && { body: l.reflection });

  const secHtml = secs.map(sec => {
    if (sec.list) {
      return \`<div class="sec"><h3><span class="sno">\${sec.no}</span>\${sec.name}</h3><ul>\${sec.list.map(x => '<li>' + escAttr(x) + '</li>').join('')}</ul></div>\`;
    }
    if (sec.steps) {
      return \`<div class="sec"><h3><span class="sno">\${sec.no}</span>\${sec.name}</h3>\${
        sec.steps.map(s =>
          \`<div class="step"><div class="sn"><span class="sno sm">\${s.n}</span>\${escAttr(s.name)}<span class="st">\${escAttr(s.time)}</span></div><p>\${escAttr(s.content)}</p></div>\`
        ).join('')
      }</div>\`;
    }
    return \`<div class="sec"><h3><span class="sno">\${sec.no}</span>\${sec.name}</h3><p>\${escAttr(sec.body)}</p></div>\`;
  }).join('');

  const fav = state.favorites.includes(l.id);
  const fid = escAttr(l.id);

  \$('content').innerHTML = \`
    <div class="hero">
      <div class="badges2">
        <span class="badge2">\${escAttr(l.book)}</span>
        <span class="badge2">\${escAttr(l.lessonTypeName)}</span>
        <span class="badge2">\${l.duration}\u5206\u949F</span>
      </div>
      <h1>\${escAttr(l.title)}</h1>
      <div class="hsub">\${escAttr(l.unitTitle)}</div>
      <div class="hstat">\uD83D\uDCC1 \${l.viewCount||0} 浏览 \u00B7 \u2B07 \${l.downloadCount||0} 下载</div>
    </div>
    \${secHtml}
    <div class="hint" style="margin-top:8px">\u2014 以下为小程序下载栏，预览中点击会提示效果 \u2014</div>
  \`;

  // 底部操作栏
  let bar = document.querySelector('.dlbar');
  if (bar) bar.remove();
  bar = document.createElement('div');
  bar.className = 'dlbar';
  bar.innerHTML =
    '<span class="fav ' + (fav ? '' : '') + '" onclick="toggleFav(\\'' + fid + '\\')">' + (fav ? '\\u2605' : '\\u2606') + '</span>' +
    '<div class="fmts">' +
      '<span class="fmt ' + (state.favFmt === 'word' ? 'on' : '') + '" onclick="setFmt(\\'word\\')">Word</span>' +
      '<span class="fmt ' + (state.favFmt === 'pdf' ? 'on' : '') + '" onclick="setFmt(\\'pdf\\')">PDF</span>' +
      '<span class="fmt ' + (state.favFmt === 'ppt' ? 'on' : '') + '" onclick="setFmt(\\'ppt\\')">PPT</span>' +
    '</div>' +
    '<div class="btn" onclick="doDownload(\\'' + fid + '\\')">\\uD83D\\uDCE5 下载 ' + state.favFmt.toUpperCase() + '</div>';
  \$('content').appendChild(bar);
}

function setFmt(f) { state.favFmt = f; renderDetail(); }

function doDownload(id) {
  const l = getLesson(id);
  if (l && !state.downloads.includes(id)) state.downloads.unshift(id);
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
state.downloads = ['l-eng-b1-u1-reading', 'l-eng-b1-u1-grammar'];
state.recents = ['l-eng-b1-u1-reading', 'l-eng-b1-u2-writing', 'l-eng-b2-u1-reading'];
state.favorites = ['l-eng-b1-u1-grammar'];
render();
</script>
</body>
</html>`;

const outPath = path.join(__dirname, '..', 'miniprogram-preview.html');
fs.writeFileSync(outPath, html, 'utf8');

// 验证生成的JS是否合法
const outHtml = fs.readFileSync(outPath, 'utf8');
const scriptMatch = outHtml.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
  try {
    new Function(scriptMatch[1]);
    console.log('\u2705 JS syntax check: PASSED');
  } catch(e) {
    console.error('\u274C JS syntax check: FAILED -', e.message);
  }
}

console.log('Written:', outPath, Math.round(html.length / 1024) + 'KB');
