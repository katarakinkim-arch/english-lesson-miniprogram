// tools/fix-eng-titles.js — 回填英语教案缺失的 title 字段（源数据修复，幂等）
const fs = require('fs');
const path = require('path');
const L = require('../data/lessons.js');

const ENG_TYPE = {
  'listening-speaking': 'Listening & Speaking',
  'listening-talking': 'Listening and Talking',
  'reading': 'Reading and Thinking',
  'grammar': 'Discovering Useful Structures',
  'writing': 'Writing',
  'project': 'Project',
  'viewing': 'Viewing',
  'speaking': 'Speaking',
  'talking': 'Talking'
};

let fixed = 0;
L.forEach((l) => {
  if (l.title) return;
  const t = ENG_TYPE[l.lessonType] || (l.lessonType ? (l.lessonType[0].toUpperCase() + l.lessonType.slice(1)) : 'Lesson');
  l.title = t + ' · ' + (l.unitTitle || '') + (l.periodNumber ? ' (P' + l.periodNumber + ')' : '');
  fixed++;
});

fs.writeFileSync(path.join(__dirname, '..', 'data', 'lessons.js'), 'module.exports = ' + JSON.stringify(L, null, 2) + ';\n', 'utf8');
console.log('English title backfilled:', fixed, '| total:', L.length);
