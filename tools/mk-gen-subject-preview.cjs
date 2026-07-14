// 由 generate-preview.js 改造出通用的「单科目预览生成器」
// 运行：node mk-gen-subject-preview.cjs  -> 生成 gen-subject-preview.js
const fs = require('fs');
const p = 'generate-preview.js';
let s = fs.readFileSync(p, 'utf8');

// 1. 数据文件可由 argv[2] 指定
s = s.replace(
  "const lessons = require(path.join(miniDir, 'data', 'lessons.js'));",
  "const dataArg = process.argv[2] ? path.resolve(process.argv[2]) : path.join(miniDir, 'data', 'lessons.js');\nconst lessons = require(dataArg);\nconst SUBJECT = (lessons[0] && lessons[0].subject) || '教案';"
);

// 2. 标题动态化
s = s.replace('<title>英语教案小程序 · 预览</title>', '<title>${SUBJECT}教案小程序 · 预览</title>');
s = s.replace('<span id="navTitle">英语教案库</span>', '<span id="navTitle">${SUBJECT}教案库</span>');

// 3. 册序动态化（支持 必修一/二/三、选择性必修一/二/三、选修）
const bookFn = `
function bookNum(b){ const m=b.match(/第([一二三四五六\\d])册/); if(m){ const c=m[1]; const mp={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6}; return mp[c]!==undefined?mp[c]:(parseInt(c)||0);} const d=b.match(/(\\d+)/); return d?parseInt(d[1]):0; }
function bookRank(b){ if(b.indexOf('选择性必修')>=0||b.indexOf('选修')>=0) return 100+bookNum(b); if(b.indexOf('必修')>=0) return bookNum(b); return 300; }
const BOOK_ORDER = {}; BOOKS.forEach(function(b){ BOOK_ORDER[b] = bookRank(b); });
const BOOK_SHORT = {}; BOOKS.forEach(function(b){ BOOK_SHORT[b] = b.replace('选择性必修','选必').replace(/必修第([一二三四五六])册/,'必修$1'); });
`;
s = s.replace("const BOOK_ORDER = { '必修第一册':1, '必修第二册':2, '必修第三册':3 };", bookFn);
s = s.replace("const BOOK_SHORT = { '必修第一册':'必修一', '必修第二册':'必修二', '必修第三册':'必修三' };", '');

// 4. 类型图标/底色通用化
s = s.replace(
  "const TYPE_ICON = { 'listening-speaking':'🎧', 'reading':'📖', 'grammar':'✏️', 'listening-talking':'💬', 'writing':'✍️', 'project':'🎯' };",
  "const TYPE_ICON = { jingdu:'📖', qunwen:'🔗', xiezuo:'✍️', huodong:'🎯', fangfa:'🛠', new:'🆕', exercise:'✏️', review:'🔁', comprehensive:'🌟', reading:'📖', grammar:'✏️', listening:'🎧', speaking:'💬', writing:'✍️', project:'🎯' };"
);
s = s.replace(
  "const TYPE_BG = { 'listening-speaking':'#6b46c1', 'reading':'#1a365d', 'grammar':'#1a6840', 'listening-talking':'#b7791f', 'writing':'#7b341e', 'project':'#2c5282' };",
  "const TYPE_BG = { jingdu:'#1a365d', qunwen:'#6b46c1', xiezuo:'#7b341e', huodong:'#2c5282', fangfa:'#1a6840', new:'#b7791f', exercise:'#2a4a7d', review:'#553c9a', comprehensive:'#0f766e', reading:'#1a365d', grammar:'#1a6840', listening:'#6b46c1', speaking:'#b7791f', writing:'#7b341e', project:'#2c5282' };"
);

// 5. 导航标题动态化
s = s.split("setNav('英语教案库', false);").join("setNav(SUBJECT + '教案库', false);");

// 6. 演示数据改用本科目前几条
s = s.replace(
  "state.downloads = ['l-eng-b1-u1-reading', 'l-eng-b1-u1-grammar'];",
  "state.downloads = LESSONS.slice(0, 2).map(function(l){ return l.id; });"
);
s = s.replace(
  "state.recents = ['l-eng-b1-u1-reading', 'l-eng-b1-u2-writing', 'l-eng-b2-u1-reading'];",
  "state.recents = LESSONS.slice(0, 3).map(function(l){ return l.id; });"
);
s = s.replace(
  "state.favorites = ['l-eng-b1-u1-grammar'];",
  "state.favorites = LESSONS.slice(0, 1).map(function(l){ return l.id; });"
);

// 7. 输出文件名可配置 argv[3]，默认 miniprogram-{科目}-preview.html
s = s.replace(
  "const outPath = path.join(__dirname, '..', 'miniprogram-preview.html');",
  "const outPath = path.join(__dirname, '..', process.argv[3] || ('miniprogram-' + SUBJECT + '-preview.html'));"
);

fs.writeFileSync('gen-subject-preview.js', s, 'utf8');
console.log('gen-subject-preview.js written (' + s.length + ' bytes)');
