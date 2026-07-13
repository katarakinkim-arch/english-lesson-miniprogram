const L = require('../data/lessons.js');
const b1 = L.filter(l => l.book === '必修第一册');
console.log('必修一课时:', b1.length);

let total = 0;
let byLesson = {};

b1.forEach(l => {
  (l.process || []).forEach((s, i) => {
    const c = s.content || '';
    const missing = [];
    if (!c.includes('【PPT')) missing.push('PPT');
    if (!c.includes('预设回答')) missing.push('预设回答');
    if (!c.includes('板书')) missing.push('板书时机');
    if (!c.includes('差异化')) missing.push('差异化');
    if (!c.includes('易错点')) missing.push('易错点');

    if (missing.length > 0) {
      total += missing.length;
      if (!byLesson[l.id]) byLesson[l.id] = [];
      byLesson[l.id].push({ step: i + 1, stepName: s.step, missing, contentPreview: c.substring(0, 80) });
    }
  });
});

console.log('真正缺失要素总数:', total);
console.log('');

// Print by lesson
const keys = Object.keys(byLesson).sort();
keys.forEach(k => {
  const items = byLesson[k];
  const unit = k.replace(/^l-eng-b1-u/, '').replace(/-.*/, '');
  console.log('--- ' + k + ' (U' + unit + ') ' + items.length + '个step有问题 ---');
  items.forEach(it => {
    console.log('  step' + it.step + ' [' + it.stepName + '] 缺:' + it.missing.join('/'));
    console.log('    content: ' + it.contentPreview);
  });
  console.log('');
});

// Count by type
console.log('=== 按缺失类型统计 ===');
let byType = {};
keys.forEach(k => {
  byLesson[k].forEach(it => {
    it.missing.forEach(m => {
      byType[m] = (byType[m] || 0) + 1;
    });
  });
});
Object.keys(byType).sort().forEach(t => {
  console.log(t + ': ' + byType[t] + '处');
});
