const L = require('../data/lessons.js');

// Check both 必修二 and 必修三
['必修第二册', '必修第三册'].forEach(bookName => {
  const bl = L.filter(l => l.book === bookName);
  console.log('\n=== ' + bookName + ': ' + bl.length + '课时 ===');
  
  let total = 0;
  let byType = {};
  
  bl.forEach(l => {
    (l.process || []).forEach((s, i) => {
      const c = s.content || '';
      const missing = [];
      if (!c.includes('【PPT')) missing.push('PPT');
      if (!c.includes('预设回答') && !c.includes('预设产出')) missing.push('预设回答');
      if (!c.includes('板书')) missing.push('板书');
      if (!c.includes('差异化')) missing.push('差异化');
      if (!c.includes('易错点')) missing.push('易错点');
      if (missing.length > 0) {
        total += missing.length;
        missing.forEach(m => byType[m] = (byType[m]||0) + 1);
        console.log('  ' + l.id + ' step' + (i+1) + ' 缺:' + missing.join('/'));
      }
    });
  });
  
  console.log('缺失总数: ' + total);
  if (Object.keys(byType).length > 0) {
    Object.keys(byType).sort().forEach(t => console.log('  ' + t + ': ' + byType[t] + '处'));
  }
  
  // Check objectives
  let objBad = bl.filter(l => !l.objectives || l.objectives.length !== 4);
  console.log('objectives非4条: ' + objBad.length);
  
  // Check exercises
  let exBad = bl.filter(l => !l.exercises || !l.exercises.includes('参考答案'));
  console.log('缺参考答案: ' + exBad.length);
});
