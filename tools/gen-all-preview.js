// 生成"全学科统一"预览 HTML：顶部学科选择栏，选哪科显示哪科，共用同一套渲染。
// 复用 gen-subject-preview.js 已验证的模板，仅改造数据层 + 增加学科切换，渲染逻辑完全一致。
const fs = require('fs');
const path = require('path');

const miniDir = path.join(__dirname, '..');
const srcPath = path.join(__dirname, 'gen-subject-preview.js');
let src = fs.readFileSync(srcPath, 'utf8');

const dataFiles = {
  cn: 'lessons-cn.js', eng: 'lessons.js', math: 'lessons-math.js', physics: 'lessons-physics.js',
  chemistry: 'lessons-chemistry.js', biology: 'lessons-biology.js', history: 'lessons-history.js',
  politics: 'lessons-politics.js', geography: 'lessons-geography.js'
};
const ALL_SUBJECTS = {};
Object.keys(dataFiles).forEach(function(k){ ALL_SUBJECTS[k] = require(path.join(miniDir, 'data', dataFiles[k])); });

function safeJsonStr(obj) { return JSON.stringify(obj).replace(/</g, '\\x3c'); }

// ---- T1: 数据加载段（原 4 行 -> 加载全部 9 科 + 元信息）----
const T1_old = "const miniDir = path.join(__dirname, '..');\nconst dataArg = process.argv[2] ? path.resolve(process.argv[2]) : path.join(miniDir, 'data', 'lessons.js');\nconst lessons = require(dataArg);\nconst SUBJECT = (lessons[0] && lessons[0].subject) || '教案';";
const T1_new = "const miniDir = path.join(__dirname, '..');\nconst dataFiles = {\n  cn: 'lessons-cn.js', eng: 'lessons.js', math: 'lessons-math.js', physics: 'lessons-physics.js',\n  chemistry: 'lessons-chemistry.js', biology: 'lessons-biology.js', history: 'lessons-history.js',\n  politics: 'lessons-politics.js', geography: 'lessons-geography.js'\n};\nconst ALL_SUBJECTS = {};\nObject.keys(dataFiles).forEach(function(k){ ALL_SUBJECTS[k] = require(path.join(miniDir, 'data', dataFiles[k])); });\nlet SUBJECT = '语文';\nlet CURRENT_KEY = 'cn';";
if (src.indexOf(T1_old) < 0) throw new Error('T1 anchor not found');
src = src.replace(T1_old, T1_new);

// ---- T0: 标题 ----
src = src.replace('<title>${SUBJECT}教案小程序 · 预览</title>', '<title>高中全学科教案 · 预览</title>');

// ---- T2: 内联全部 9 科数据（替代单科 LESSONS 嵌入）----
// 关键：仍用 ${safeJsonStr(...)} 模板插值（保留为字面文本，生成器运行时再求值），
// 不能把 JSON 字面量直接拼进外层模板，否则数据里的 ` 或 ${ 或换行会破坏模板。
const T2_old = "const LESSONS = ${safeJsonStr(lessons)};";
const T2_new =
"const ALL_SUBJECTS = {\n" +
"  cn: ${safeJsonStr(ALL_SUBJECTS.cn)},\n" +
"  eng: ${safeJsonStr(ALL_SUBJECTS.eng)},\n" +
"  math: ${safeJsonStr(ALL_SUBJECTS.math)},\n" +
"  physics: ${safeJsonStr(ALL_SUBJECTS.physics)},\n" +
"  chemistry: ${safeJsonStr(ALL_SUBJECTS.chemistry)},\n" +
"  biology: ${safeJsonStr(ALL_SUBJECTS.biology)},\n" +
"  history: ${safeJsonStr(ALL_SUBJECTS.history)},\n" +
"  politics: ${safeJsonStr(ALL_SUBJECTS.politics)},\n" +
"  geography: ${safeJsonStr(ALL_SUBJECTS.geography)}\n" +
"};\n" +
"const SUBJECTS_META = {\n" +
"  cn: { name: '语文', color: '#b91c1c', short: '语' },\n" +
"  eng: { name: '英语', color: '#1d4ed8', short: '英' },\n" +
"  math: { name: '数学', color: '#7c3aed', short: '数' },\n" +
"  physics: { name: '物理', color: '#0891b2', short: '物' },\n" +
"  chemistry: { name: '化学', color: '#059669', short: '化' },\n" +
"  biology: { name: '生物', color: '#16a34a', short: '生' },\n" +
"  history: { name: '历史', color: '#ca8a04', short: '史' },\n" +
"  politics: { name: '政治', color: '#dc2626', short: '政' },\n" +
"  geography: { name: '地理', color: '#0d9488', short: '地' }\n" +
"};\n" +
"let SUBJECT = '语文';\n" +
"let CURRENT_KEY = 'cn';\n" +
"let LESSONS = ALL_SUBJECTS[CURRENT_KEY];";
if (src.indexOf(T2_old) < 0) throw new Error('T2 anchor not found');
src = src.replace(T2_old, T2_new);

// ---- T3: BOOKS/BOOK_ORDER/BOOK_SHORT 改 let + 新增 recomputeBooks ----
src = src.replace("const BOOKS = [...new Set(LESSONS.map(function(l){ return l.book; }))];",
  "let BOOKS = [...new Set(LESSONS.map(function(l){ return l.book; }))];");
src = src.replace("const BOOK_ORDER = {}; BOOKS.forEach(function(b){ BOOK_ORDER[b] = bookRank(b); });",
  "let BOOK_ORDER = {};");
src = src.replace("const BOOK_SHORT = {}; BOOKS.forEach(function(b){ BOOK_SHORT[b] = b.replace('选择性必修','选必').replace(/必修第([一二三四五六])册/,'必修$1'); });",
  "let BOOK_SHORT = {};\nfunction recomputeBooks(){\n  BOOKS = [...new Set(LESSONS.map(function(l){ return l.book; }))];\n  BOOK_ORDER = {}; BOOKS.forEach(function(b){ BOOK_ORDER[b] = bookRank(b); });\n  BOOK_SHORT = {}; BOOKS.forEach(function(b){ BOOK_SHORT[b] = b.replace('选择性必修','选必').replace(/必修第([一二三四五六])册/,'必修$1'); });\n}\nrecomputeBooks();");

// ---- T4: getLesson 跨科查找 ----
src = src.replace("function getLesson(id) { return LESSONS.find(function(l){ return l.id === id; }); }",
  "function getLesson(id) { for (var k in ALL_SUBJECTS) { var f = ALL_SUBJECTS[k].find(function(l){ return l.id === id; }); if (f) return f; } return null; }");

// ---- T5: 新增 selectSubject（在 switchTab 之后插入）----
const T5_anchor = "function goBack() {";
const T5_new = "function selectSubject(key) {\n" +
"  if (!ALL_SUBJECTS[key] || key === CURRENT_KEY) return;\n" +
"  CURRENT_KEY = key;\n" +
"  LESSONS = ALL_SUBJECTS[key];\n" +
"  SUBJECT = SUBJECTS_META[key].name;\n" +
"  state.filterBook = '';\n" +
"  state.keyword = '';\n" +
"  state.detailId = null;\n" +
"  state.privacy = false;\n" +
"  document.querySelectorAll('.tab').forEach(function(t){ t.classList.toggle('on', t.dataset.tab === 'index'); });\n" +
"  recomputeBooks();\n" +
"  renderIndex();\n" +
"}\n\n" + T5_anchor;
if (src.indexOf(T5_anchor) < 0) throw new Error('T5 anchor not found');
src = src.replace(T5_anchor, T5_new);

// ---- T6: renderIndex 顶部插入学科选择栏 ----
src = src.replace("function renderIndex() {\n  setNav(SUBJECT + '教案库', false);",
  "function renderIndex() {\n  setNav(SUBJECT + '教案库', false);\n" +
  "  const subjectBar = '<div class=\"subjbar\">' + Object.keys(SUBJECTS_META).map(function(k){\n" +
  "    const on = k === CURRENT_KEY;\n" +
  "    const style = on ? ('background:' + SUBJECTS_META[k].color + ';color:#fff;border-color:' + SUBJECTS_META[k].color + ';') : '';\n" +
  "    return '<div class=\"subj' + (on ? ' on' : '') + '\" data-subj=\"' + k + '\" style=\"' + style + '\">' + SUBJECTS_META[k].short + '</div>';\n" +
  "  }).join('') + '</div>';");

// 把 subjectBar 插入到 search 之后、histHtml 之前
src = src.replace("    histHtml +\n    '<div class=\"chips\">' + bookChips + '</div>' +",
  "    subjectBar +\n    histHtml +\n    '<div class=\"chips\">' + bookChips + '</div>' +");

// ---- T7: 事件委托增加 [data-subj] ----
src = src.replace("  var b = e.target.closest('[data-book]'); if (b) { setBook(b.getAttribute('data-book')); return; }",
  "  var sj = e.target.closest('[data-subj]'); if (sj) { selectSubject(sj.getAttribute('data-subj')); return; }\n  var b = e.target.closest('[data-book]'); if (b) { setBook(b.getAttribute('data-book')); return; }");

// ---- T8: 输出路径固定为 miniprogram-all-preview.html ----
src = src.replace("const outPath = path.join(__dirname, '..', process.argv[3] || ('miniprogram-' + SUBJECT + '-preview.html'));",
  "const outPath = path.join(__dirname, '..', 'miniprogram-all-preview.html');");

// ---- T9: CSS 增加 .subjbar / .subj ----
src = src.replace("  .tip{ font-size:11px; color:#aab; text-align:center; margin-top:14px; line-height:1.6; }\n</style>",
  "  .tip{ font-size:11px; color:#aab; text-align:center; margin-top:14px; line-height:1.6; }\n" +
  "  .subjbar{ display:flex; gap:6px; margin:6px 0 10px; overflow-x:auto; -webkit-overflow-scrolling:touch; padding-bottom:2px; }\n" +
  "  .subjbar::-webkit-scrollbar{ height:0; }\n" +
  "  .subj{ flex-shrink:0; font-size:13px; padding:7px 14px; border-radius:20px; background:var(--chip); color:var(--sub); cursor:pointer; white-space:nowrap; border:1.5px solid transparent; }\n" +
  "  .subj.on{ font-weight:700; }\n</style>");

// 语法检查（生成器自身）
try { new Function(src); } catch (e) { fs.writeFileSync(path.join(__dirname, '_mod_src.js'), src); throw new Error('generator syntax error: ' + e.message); }

// 执行生成器得到 HTML
const moduleWrap = '(function(){ var module={exports:{}}; var exports=module.exports; ' + src + '\n; return module.exports; })';
try {
  // gen-subject-preview.js 直接写文件，不导出；用 eval 在当前作用域执行
  eval(src);
} catch (e) {
  console.error('❌ 生成失败:', e.message);
  process.exit(1);
}

console.log('✅ 聚合预览生成完成');
