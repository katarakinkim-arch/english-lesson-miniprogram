// 从 data/lessons-cn.js 提取单课为 JSON，供 Python 渲染器读取
const fs = require('fs');
const path = require('path');

const dataDir = path.join(__dirname, '..', 'data');
const outDir = path.join(__dirname, '..');

const id = process.argv[2] || 'l-cn-bs-u1-1';
const which = process.argv[3] || 'cn'; // cn | en

let file, L;
if (which === 'cn') {
  const data = require(path.join(dataDir, 'lessons-cn.js'));
  L = data.find((x) => x.id === id);
} else {
  const data = require(path.join(dataDir, 'lessons.js'));
  L = data.find((x) => x.id === id);
}

if (!L) {
  console.error('not found', id, 'in', which);
  process.exit(1);
}

const out = path.join(outDir, 'lesson_' + which + '.json');
fs.writeFileSync(out, JSON.stringify(L, null, 2), 'utf8');
console.log('extracted', id, '->', out, '(', fs.statSync(out).size, 'bytes )');
