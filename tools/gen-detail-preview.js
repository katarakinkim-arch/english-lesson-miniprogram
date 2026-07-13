const fs = require('fs');
const path = require('path');
const L = require('../data/lessons.js');

// 取必修一 U1 阅读第1课时作为详情页演示
const lesson = L.find(l => l.id === 'l-eng-b1-u1-r1') || L[0];

const esc = (s) => String(s == null ? '' : s)
  .replace(/&/g, '&amp;')
  .replace(/</g, '&lt;')
  .replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;');

/* ===== 智能解析函数 ===== */

function parseOverview(raw) {
  // 【学情分析】A班...B班... → 结构化显示
  const s = raw || '';
  if (s.includes('【学情分析】')) {
    const body = s.replace(/【学情分析】/, '').trim();
    // 按 A班 / B班 / 共同问题 拆分
    const aMatch = body.match(/A[班班]?\s*[：:]\s*([^B共]*)/);
    const bMatch = body.match(/B[班班]?\s*[：:]\s*([^共]*)/);
    const cMatch = body.match(/共同问题\s*[：:]\s*(.*)/);
    let html = '<div class="ov-row"><span class="ov-label ov-a">A 班</span><span class="ov-text">' + esc(aMatch ? aMatch[1].trim() : '') + '</span></div>';
    html += '<div class="ov-row"><span class="ov-label ov-b">B 班</span><span class="ov-text">' + esc(bMatch ? bMatch[1].trim() : '') + '</span></div>';
    if (cMatch) html += '<div class="ov-row"><span class="ov-label ov-c">共同问题</span><span class="ov-text">' + esc(cMatch[1].trim()) + '</span></div>';
    return html;
  }
  // fallback
  return esc(s).replace(/\n/g, '<br>');
}

function parseKeyPoints(raw) {
  const s = raw || '';
  // 按 ① ② ③ 拆分行
  const parts = s.split(/(?=①|②|③|④|⑤)/).filter(Boolean);
  if (parts.length > 1) {
    return parts.map(p => '<div class="kp-item">' + esc(p.trim()) + '</div>').join('');
  }
  return esc(s).replace(/\n/g, '<br>');
}

function parseDifficulties(raw) {
  return parseKeyPoints(raw); // same format
}

function parsePrep(raw) {
  const s = raw || '';
  const pptMatch = s.match(/【PPT课件】([\s\S]*?)(?=【实物教具】|$)/);
  const realiaMatch = s.match(/【实物教具】([\s\S]*?)(?=【音频】|$)/);
  const audioMatch = s.match(/【音频】([\s\S]*?)$/);

  let html = '';
  if (pptMatch) html += section('PPT课件', pptMatch[1].trim().replace(/[;；]/g, '<br>').replace(/P\d+/g, '<span class="tag tag-ppt">$&</span>'));
  if (realiaMatch) html += section('实物教具', esc(realiaMatch[1].trim()));
  if (audioMatch) html += section('音频', esc(audioMatch[1].trim()));
  return html || esc(s);
}

function parseExercises(raw) {
  const s = raw || '';
  const basicMatch = s.match(/【基础作业】([\s\S]*?)(?=【提高作业】|$)/);
  const advMatch = s.match(/【提高作业】([\s\S]*?)(?=【参考答案]|$)/);
  const ansMatch = s.match(/【参考答案[^】]*】([\s\S]*?)$/);

  let html = '';
  if (basicMatch) html += section('基础作业', esc(basicMatch[1].trim()).replace(/\d+\./g, '<b>$&</b>'));
  if (advMatch) html += section('提高作业', esc(advMatch[1].trim()));
  if (ansMatch) html += section('参考答案——教师用', '<div class="ans-box">' + esc(ansMatch[1].trim()) + '</div>');
  return html || esc(s);
}

function parseReflection(raw) {
  const s = raw || '';
  const hi = s.match(/✅\s*(亮点)[^：:]*[:：]?\s*([^⚠️\n]+)/);
  const im = s.match(/⚠️\s*(需改进)[^：:]*[:：]?\s*([^📌\n]+)/);
  const nl = s.match(/📌\s*(下节课衔接)[^：:]*[:：]?\s*(.+)/);

  let html = '';
  if (hi) html += section('✅ 亮点', esc(hi[2].trim()));
  if (im) html += section('⚠️ 需改进', esc(im[2].trim()));
  if (nl) html += section('📌 下节课衔接', esc(nl[2].trim()));
  return html || esc(s);
}

// process step 高亮
function highlightContent(c) {
  return esc(c)
    .replace(/【PPT[^】]*】/g, '<span class="tag tag-ppt">$&</span>')
    .replace(/【音频\d*[^】]*】/g, '<span class="tag tag-audio">$&</span>')
    .replace(/预设回答[:：][^。]*/g, '<span class="tag tag-ans">$&</span>')
    .replace(/板书时机[:：][^。]*/g, '<span class="tag tag-board">$&</span>')
    .replace(/差异化提示[:：][^。]*/g, '<span class="tag tag-diff">$&</span>')
    .replace(/易错点提醒[:：][^。]*/g, '<span class="tag tag-warn">$&</span>')
    .replace(/教师[:：][^。]*/g, '<span class="tag tag-teacher">$&</span>')
    .replace(/\n/g, '<br>');
}

/* ===== 辅助 ===== */
function section(title, body) {
  if (!body) return '';
  return '<div class="sub-card"><div class="sub-h">' + esc(title) + '</div><div class="sub-b">' + body + '</div></div>';
}

let processHtml = (lesson.process || []).map((s, i) => {
  return '<div class="step">'
    + '<div class="step-head"><span class="step-no">' + (i + 1) + '</span>'
    + '<span class="step-name">' + esc(s.step || '').replace(/^Step \d+\s*/, '') + '</span>'
    + '<span class="step-time">' + esc((s.time || '')) + '</span></div>'
    + '<div class="step-body">' + highlightContent(s.content || '') + '</div></div>';
}).join('');

let objHtml = (lesson.objectives || []).map((o, i) => {
  const labels = ['语言能力', '文化意识', '思维品质', '学习能力'];
  return '<div class="obj"><span class="obj-tag">' + (labels[i] || ('维度' + (i+1))) + '</span>' + esc(o) + '</div>';
}).join('');

/* ===== HTML 输出 ===== */
const html = `<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(lesson.title)}</title>
<style>
<style>
/* 手机模拟器外壳 */
html { background:#e5e7eb; }
body {
  max-width: 375px;
  margin: 20px auto;
  min-height:100vh;
  box-shadow:0 0 40px rgba(0,0,0,.15);
  border-radius:36px;
  overflow:hidden;
  position:relative;
  background:#f0f2f5;
}

* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif; background:#f0f2f5; color:#1a1a2e; line-height:1.75; -webkit-font-smoothing:antialiased; }

/* ===== 微信小程序外壳模拟 ===== */
/* 状态栏 + 微信胶囊 */
.phone { width:375px; max-width:100%; margin:0 auto; position:relative; min-height:100vh; display:flex; flex-direction:column; background:#f0f2f5; }

/* 状态栏 */
.statusbar { height:44px; background:#1a365d; display:flex; align-items:center; justify-content:space-between; padding:0 20px; color:#fff; font-size:14px; font-weight:600; flex-shrink:0; }
.statusbar .time { letter-spacing:.5px; }
.statusbar .icons { display:flex; gap:5px; align-items:center; }
.statusbar .icons svg { display:block; }

/* 微信导航栏（替代原生胶囊的模拟） */
.wxnav { height:44px; background:#1a365d; display:flex; align-items:center; padding:0 12px; color:#fff; position:relative; flex-shrink:0; }
.wxnav .back { font-size:22px; line-height:1; margin-right:6px; }
.wxnav .title { font-size:17px; font-weight:600; position:absolute; left:50%; transform:translateX(-50%); max-width:60%; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.wxnav .capsule { position:absolute; right:10px; top:50%; transform:translateY(-50%); width:87px; height:32px; background:rgba(255,255,255,.25); border:1px solid rgba(255,255,255,.4); border-radius:16px; display:flex; align-items:center; justify-content:space-around; }
.wxnav .capsule .dot { width:4px; height:4px; border-radius:50%; background:#fff; }
.wxnav .capsule .oval { width:16px; height:16px; position:relative; }
.wxnav .capsule .oval:before, .wxnav .capsule .oval:after { content:''; position:absolute; background:#fff; }
.wxnav .capsule .oval:before { width:7px; height:7px; border:1.5px solid #fff; border-radius:50%; top:2px; left:0; background:transparent; }
.wxnav .capsule .oval:after { width:1.5px; height:11px; background:#fff; top:3px; left:13px; }

/* 内容滚动区 */
.screen { flex:1; overflow-y:auto; -webkit-overflow-scrolling:touch; }

/* 底部 tabBar */
.tabbar { height:52px; background:#fff; border-top:1px solid #e5e7eb; display:flex; flex-shrink:0; padding-bottom:env(safe-area-inset-bottom); }
.tabbar .tab { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:2px; font-size:10px; color:#888; }
.tabbar .tab.active { color:#1a365d; font-weight:600; }
.tabbar .tab svg { width:24px; height:24px; }

/* Hero — 紧接导航栏下方 */
.hero { background:linear-gradient(135deg,#0f172a,#1e3a8a); color:#fff; padding:16px 16px 18px; margin-bottom:12px; border-radius:0 0 16px 16px; }
.hero-badge { display:inline-block; font-size:12px; opacity:.8; margin-bottom:6px; letter-spacing:.3px; }
.hero h1 { font-size:21px; font-weight:800; line-height:1.35; margin-bottom:8px; }
.hero-meta { font-size:13px; opacity:.75; display:flex; flex-wrap:wrap; gap:10px; }
.hero-meta span { background:rgba(255,255,255,.15); padding:2px 8px; border-radius:6px; }

.wrap { padding:0 12px 20px; }

/* Cards */
.card { background:#fff; border-radius:16px; overflow:hidden; margin-bottom:13px; box-shadow:0 1px 4px rgba(0,0,0,.05); }
.card-h { padding:11px 15px; font-size:15px; font-weight:700; color:#1e3a8a; background:#eff4ff; border-left:4px solid #2563eb; }
.card-b { padding:14px 15px; font-size:14px; line-height:1.85; }

/* Overview — 学情分析结构化 */
.overview-box { background:#fff; border-radius:16px; overflow:hidden; margin-bottom:13px; box-shadow:0 1px 4px rgba(0,0,0,.05); }
.ov-header { padding:11px 15px; font-size:15px; font-weight:700; color:#166534; background:#f0fdf4; border-left:4px solid #22c55e; }
.ov-body { padding:14px 15px; }
.ov-row { display:flex; gap:10px; align-items:flex-start; margin-bottom:9px; }
.ov-label { flex:none; width:52px; text-align:center; font-size:12px; font-weight:700; padding:3px 0; border-radius:7px; }
.ov-a { background:#dbeafe; color:#1e40af; }
.ov-b { background:#fef3c7; color:#92400e; }
.ov-c { background:#fce7f3; color:#be185d; }
.ov-text { font-size:14px; color:#374151; flex:1; }

/* Objectives 4维 */
.obj { background:#f8fafc; border-radius:12px; padding:11px 13px; margin-bottom:9px; display:flex; gap:10px; align-items:flex-start; border-left:3px solid #cbd5e1; }
.obj-tag { flex:none; min-width:56px; text-align:center; font-size:12px; font-weight:700; color:#fff; padding:3px 8px; border-radius:7px; background:linear-gradient(135deg,#2563eb,#1e3a8a); }
.obj:nth-child(1) .obj-tag { background:linear-gradient(135deg,#2563eb,#1d4ed8); } /* 语言能力 */
.obj:nth-child(2) .obj-tag { background:linear-gradient(135deg,#7c3aed,#6d28d9); } /* 文化意识 */
.obj:nth-child(3) .obj-tag { background:linear-gradient(135deg,#0891b2,#0e7490); } /* 思维品质 */
.obj:nth-child(4) .obj-tag { background:linear-gradient(135deg,#dc2626,#b91c1c); } /* 学习能力 */

/* Sub cards (inside card) */
.sub-card { margin-bottom:10px; border-radius:10px; overflow:hidden; border:1px solid #eef2f7; }
.sub-h { font-size:13px; font-weight:600; color:#475569; background:#f8fafc; padding:7px 12px; border-left:3px solid #94a3b8; }
.sub-b { padding:9px 12px; font-size:14px; line-height:1.85; }

/* Key Points / Difficulties */
.kp-item { position:relative; padding-left:22px; margin-bottom:9px; font-size:14px; }
.kp-item:before { content:''; position:absolute; left:4px; top:8px; width:8px; height:8px; border-radius:50%; background:#2563eb; }
.kp-item:last-child { margin-bottom:0; }

/* Process Steps */
.step { background:#fff; border-radius:14px; margin-bottom:12px; box-shadow:0 1px 4px rgba(0,0,0,.06); overflow:hidden; }
.step-head { display:flex; align-items:center; gap:10px; padding:10px 14px; background:#fafbfd; border-bottom:1px solid #f0f1f3; }
.step-no { width:28px; height:28px; border-radius:50%; background:#2563eb; color:#fff; font-size:14px; font-weight:800; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.step-name { font-weight:700; font-size:14px; color:#1e293b; flex:1; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.step-time { font-size:12px; color:#64748b; background:#f1f5f9; padding:2px 9px; border-radius:7px; flex-shrink:0; }
.step-body { padding:13px 14px; font-size:14px; line-height:1.95; color:#334155; word-break:break-word; }

/* Tags */
.tag { display:inline-block; padding:1px 6px; border-radius:5px; font-size:12.5px; font-weight:500; margin:1px 1px; vertical-align:middle; }
.tag-ppt { background:#dbeafe; color:#1e40af; border:1px solid #bfdbfe; }
.tag-teacher { background:#fee2e2; color:#991b1b; border:1px solid #fecaca; }
.tag-ans { background:#dcfce7; color:#166534; border:1px solid #bbf7d0; }
.tag-board { background:#fef9c3; color:#854d0e; border:1px solid #fde047; }
.tag-diff { background:#ede9fe; color:#5b21b6; border:1px solid #ddd6fe; }
.tag-warn { background:#ffedd5; color:#9a3412; border:1px solid #fed7aa; }
.tag-audio { background:#e0f2fe; color:#0369a1; border:1px solid #bae6fd; }

/* Blackboard */
.board-wrap { background:#fff; border-radius:14px; overflow:hidden; margin-bottom:13px; box-shadow:0 1px 4px rgba(0,0,0,.05); }
.board { font-family:"Cascadia Code","Fira Code",Consolas,monospace; white-space:pre; background:#0f172a; color:#e2e8f0; padding:16px; font-size:12.5px; line-height:1.65; border-radius:0; overflow-x:auto; }

/* Answers */
.ans-box { background:#fefce8; border:1px solid #fde68a; border-radius:8px; padding:10px 12px; font-size:13.5px; color:#854d0e; }

/* 详情页导出按钮（嵌在内容底部，不占 tabBar 位置） */
.actions { display:flex; gap:8px; padding:14px 0 8px; }
.btn { flex:1; text-align:center; background:linear-gradient(135deg,#2563eb,#1d4ed8); color:#fff; padding:12px 8px; border-radius:10px; font-size:13px; font-weight:700; }
.btn-ppt { background:linear-gradient(135deg,#7c3aed,#6d28d9); }
.btn-pdf { background:linear-gradient(135deg,#dc2626,#b91c1c); }
</style></head>
<body>

<div class="phone">

  <!-- iOS 状态栏 -->
  <div class="statusbar">
    <span class="time">9:41</span>
    <span class="icons">
      <svg width="17" height="11" viewBox="0 0 17 11" fill="none"><path d="M1 4h2v6H1zM5 3h2v7H5zM9 2h2v8H9zM13 0h2v10h-2z" fill="#fff" opacity=".4"/><path d="M1 4h2v6H1zM5 3h2v7H5zM9 2h2v8H9zM13 0h2v10h-2z" fill="#fff"/></svg>
      <svg width="16" height="11" viewBox="0 0 16 11" fill="none"><path d="M8 2C4.5 2 1.8 4 .5 5.5l1 1C2.7 5.2 5 3.5 8 3.5s5.3 1.7 6.5 3l1-1C14.2 4 11.5 2 8 2z" fill="#fff" opacity=".5"/><path d="M8 5.5c-1.8 0-3.3 1-4 1.8l1 1c.6-.6 1.7-1.3 3-1.3s2.4.7 3 1.3l1-1c-.7-.8-2.2-1.8-4-1.8z" fill="#fff"/><circle cx="8" cy="9.5" r="1" fill="#fff"/></svg>
      <svg width="27" height="12" viewBox="0 0 27 12" fill="none"><rect x=".5" y=".5" width="22" height="11" rx="2.5" stroke="#fff" opacity=".5" fill="none"/><rect x="2" y="2" width="19" height="8" rx="1" fill="#fff"/><rect x="23.5" y="3.5" width="1.5" height="5" rx=".5" fill="#fff" opacity=".5"/></svg>
    </span>
  </div>

  <!-- 微信导航栏（含胶囊） -->
  <div class="wxnav">
    <span class="back">‹</span>
    <span class="title">教案详情</span>
    <div class="capsule">
      <div style="display:flex;gap:2px;align-items:center;"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
      <div class="oval"></div>
    </div>
  </div>

  <!-- 内容滚动区 -->
  <div class="screen">

<div class="hero">
  <div class="hero-badge">${esc(lesson.book)} · 单元${esc(lesson.unitNumber)} ${esc(lesson.unitTitle || '')}</div>
  <h1>${esc(lesson.title)}</h1>
  <div class="hero-meta">
    ${[lesson.lessonTypeName, '第'+lesson.periodNumber+'课时', lesson.duration+'分钟'].concat((lesson.tags||[]).slice(0,4)).map(t=>'<span>'+esc(t)+'</span>').join('')}
  </div>
</div>

<div class="wrap">

  <!-- 学情分析 -->
  <div class="overview-box">
    <div class="ov-header">📊 学情分析</div>
    <div class="ov-body">${parseOverview(lesson.overview)}</div>
  </div>

  <!-- 教学目标 -->
  <div class="card">
    <div class="card-h">🎯 教学目标（4 维）</div>
    <div class="card-b" style="padding:10px;">${objHtml}</div>
  </div>

  <!-- 教材分析 -->
  ${(lesson.textbookAnalysis ? '<div class="card"><div class="card-h">📖 教材分析</div><div class="card-b">' + esc(lesson.textbookAnalysis) + '</div></div>' : '')}

  <!-- 教学重点 -->
  ${(lesson.keyPoints ? '<div class="card"><div class="card-h">💡 教学重点</div><div class="card-b">' + parseKeyPoints(lesson.keyPoints) + '</div></div>' : '')}

  <!-- 教学难点 -->
  ${(lesson.difficulties ? '<div class="card"><div class="card-h">⚠️ 教学难点</div><div class="card-b">' + parseDifficulties(lesson.difficulties) + '</div></div>' : '')}

  <!-- 教学方法 -->
  ${(lesson.teachingMethods ? '<div class="card"><div class="card-h">🔧 教学方法</div><div class="card-b">' + esc(lesson.teachingMethods).replace(/[\n①②③④⑤]/g, m=>m==='\n'?'<br>':'<br>'+m) + '</div></div>' : '')}

  <!-- 教学准备 -->
  ${parsePrep(lesson.preparation) ? '<div class="card"><div class="card-h">🛠 教学准备</div><div class="card-b" style="padding:10px;">' + parsePrep(lesson.preparation) + '</div></div>' : ''}

  <!-- 教学过程 -->
  <div class="card">
    <div class="card-h">📝 教学过程</div>
    <div style="padding:8px 0">${processHtml}</div>
  </div>

  <!-- 板书设计 -->
  ${(lesson.blackboard ? '<div class="board-wrap"><div class="card-h" style="background:#1e293b;color:#e2e8f0;border-color:#475569;">📐 板书设计</div><div class="board">' + esc(lesson.blackboard) + '</div></div>' : '')}

  <!-- 课后作业 -->
  ${parseExercises(lesson.exercises) ? '<div class="card"><div class="card-h">📚 课后作业</div><div class="card-b" style="padding:10px;">' + parseExercises(lesson.exercises) + '</div></div>' : ''}

  <!-- 教学反思 -->
  ${parseReflection(lesson.reflection) ? '<div class="card"><div class="card-h">💭 教学反思</div><div class="card-b" style="padding:10px;">' + parseReflection(lesson.reflection) + '</div></div>' : ''}

</div>

  <!-- 导出按钮 -->
  <div class="actions">
    <div class="btn">📄 Word</div>
    <div class="btn btn-ppt">📊 PPT</div>
    <div class="btn btn-pdf">📑 PDF</div>
  </div>

  </div><!-- /screen -->

  <!-- 底部 tabBar -->
  <div class="tabbar">
    <div class="tab active">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
      <span>教案库</span>
    </div>
    <div class="tab">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      <span>收藏</span>
    </div>
    <div class="tab">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      <span>我的</span>
    </div>
  </div>

</div><!-- /phone -->

</body></html>`;

const out = path.join(__dirname, '..', 'preview-detail.html');
fs.writeFileSync(out, html, 'utf8');
console.log('OK: preview-detail.html (' + Buffer.byteLength(html) + ' bytes)');
