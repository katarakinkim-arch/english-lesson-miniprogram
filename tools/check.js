// 通用教案质量校验（参数化，支持任意科目）
// 用法：node check.js [data文件路径，默认 lessons-cn.js]
const path = require('path');
const P = process.argv[2] ? path.resolve(process.argv[2]) : path.join(__dirname, '..', 'data', 'lessons-cn.js');
const L = require(P);
const subj = (L[0] && L[0].subject) || '?';
console.log('科目:', subj, '| 教案总数:', L.length);

let missing = [];
L.forEach(l => {
  (l.process || []).forEach((s, i) => {
    const c = s.content || '';
    const checks = [
      ['PPT', !c.includes('【PPT')],
      ['预设回答', !c.includes('预设回答')],
      ['板书', !c.includes('板书')],
      ['差异化', !c.includes('差异化')],
      ['易错点', !c.includes('易错点')]
    ];
    checks.forEach(([name, miss]) => { if (miss) missing.push(l.id + ' step' + (i + 1) + ' 缺' + name); });
  });
});

let objIssues = [];
L.forEach(l => { if (!l.objectives || l.objectives.length !== 4) objIssues.push(l.id + ' objectives=' + (l.objectives || []).length); });

let exIssues = [];
L.forEach(l => {
  const e = l.exercises || '';
  if (!e.includes('基础作业')) exIssues.push(l.id + ' 缺基础作业');
  if (!e.includes('参考答案')) exIssues.push(l.id + ' 缺参考答案');
});

console.log('\n=== 六要素检查 ===');
console.log('缺失总数:', missing.length);
if (missing.length > 0) missing.forEach(m => console.log('  ' + m));

console.log('\n=== objectives检查 ===');
console.log('非4条:', objIssues.length);
if (objIssues.length > 0) objIssues.forEach(m => console.log('  ' + m));

console.log('\n=== 作业检查 ===');
console.log('缺失:', exIssues.length);
if (exIssues.length > 0) exIssues.forEach(m => console.log('  ' + m));

console.log('\n=== ID唯一性 ===');
const ids = L.map(l => l.id);
console.log('唯一:', new Set(ids).size === ids.length, '(' + new Set(ids).size + '/' + ids.length + ')');

console.log('\n=== 按册/单元统计 ===');
const m = {};
L.forEach(l => { const k = (l.book || '?') + ' U' + (l.unitNumber || '?'); m[k] = (m[k] || 0) + 1; });
Object.keys(m).sort().forEach(k => console.log('  ' + k + ' ' + m[k]));
