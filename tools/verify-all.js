// 全9科教案质量汇总校验
// 用法：node tools/verify-all.js
// 判据与 check.js 保持一致：六要素(PPT/预设回答/板书/差异化/易错点)、objectives=4、作业(基础作业+参考答案)、ID唯一
const path = require('path');

const FILES = [
  ['英语', '../data/lessons.js'],
  ['语文', '../data/lessons-cn.js'],
  ['数学', '../data/lessons-math.js'],
  ['物理', '../data/lessons-physics.js'],
  ['化学', '../data/lessons-chemistry.js'],
  ['生物', '../data/lessons-biology.js'],
  ['历史', '../data/lessons-history.js'],
  ['政治', '../data/lessons-politics.js'],
  ['地理', '../data/lessons-geography.js'],
];

// 六要素关键词（与 check.js 一致）
const SIX = [
  ['PPT页号', '【PPT'],
  ['预设回答', '预设回答'],
  ['板书时机', '板书'],
  ['差异化提示', '差异化'],
  ['易错点提醒', '易错点'],
];

let grandTotal = 0, grandMiss = 0, grandObj = 0, grandEx = 0, grandDup = 0;
const rows = [];

for (const [name, rel] of FILES) {
  const L = require(path.join(__dirname, rel));
  let miss = 0;
  L.forEach((l) => (l.process || []).forEach((s) => {
    const c = s.content || '';
    SIX.forEach(([, kw]) => { if (!c.includes(kw)) miss++; });
  }));
  const obj = L.filter((l) => !l.objectives || l.objectives.length !== 4).length;
  const ex = L.filter((l) => {
    const e = l.exercises || '';
    return !e.includes('基础作业') || !e.includes('参考答案');
  }).length;
  const ids = L.map((l) => l.id);
  const dup = ids.length - new Set(ids).size;
  grandTotal += L.length; grandMiss += miss; grandObj += obj; grandEx += ex; grandDup += dup;
  rows.push({ name, total: L.length, miss, obj, ex, dup, unique: new Set(ids).size === ids.length });
}

console.log('科目   总数   六要素缺失  非4目标  作业缺失  重复ID');
console.log('------------------------------------------------------');
for (const r of rows) {
  console.log(
    r.name.padEnd(4, '　') + '  ' +
    String(r.total).padStart(4, ' ') + '   ' +
    String(r.miss).padStart(6, ' ') + '    ' +
    String(r.obj).padStart(4, ' ') + '   ' +
    String(r.ex).padStart(4, ' ') + '   ' +
    (r.unique ? '0 (OK)' : r.dup + ' (DUP!)')
  );
}
console.log('------------------------------------------------------');
console.log(
  '合计   ' + String(grandTotal).padStart(4, ' ') + '   ' +
  String(grandMiss).padStart(6, ' ') + '    ' +
  String(grandObj).padStart(4, ' ') + '   ' +
  String(grandEx).padStart(4, ' ') + '   ' +
  grandDup
);

const ok = grandMiss === 0 && grandObj === 0 && grandEx === 0 && grandDup === 0;
console.log('\n' + (ok ? '✅ 全9科质检全部通过' : '❌ 存在质检问题，需修复'));
process.exit(ok ? 0 : 1);
