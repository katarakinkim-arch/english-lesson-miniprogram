// -*- coding: utf-8 -*-
// 把 9 科教案数据导出为单一 JSON，供 Python 渲染管线消费。
const fs = require('fs');
const path = require('path');
const BASE = path.dirname(path.dirname(__dirname)); // miniprogram/
const DATA = path.join(BASE, 'miniprogram', 'data');

const map = [
  ['英语', 'lessons.js'],
  ['语文', 'lessons-cn.js'],
  ['数学', 'lessons-math.js'],
  ['物理', 'lessons-physics.js'],
  ['化学', 'lessons-chemistry.js'],
  ['生物', 'lessons-biology.js'],
  ['历史', 'lessons-history.js'],
  ['政治', 'lessons-politics.js'],
  ['地理', 'lessons-geography.js'],
];

const out = {};
for (const [subj, file] of map) {
  const p = path.join(DATA, file);
  if (!fs.existsSync(p)) { console.error('MISSING', p); continue; }
  const mod = require(p);
  out[subj] = mod;
  console.log(subj, mod.length, 'lessons');
}
const target = path.join(BASE, 'miniprogram', 'preview_v7', '_lessons_all.json');
fs.mkdirSync(path.dirname(target), { recursive: true });
fs.writeFileSync(target, JSON.stringify(out, null, 0), 'utf8');
console.log('WROTE', target);
