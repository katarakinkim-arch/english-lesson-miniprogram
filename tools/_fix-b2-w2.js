const fs = require('fs');
const path = require('path');
const LESSONS_PATH = path.join(__dirname, '..', 'data', 'lessons.js');
const L = require(LESSONS_PATH);

// Fix 必修二 W2 step3 (0-indexed = 2): add 预设回答
const targets = ['l-eng-b2-u1-w2', 'l-eng-b2-u2-w2', 'l-eng-b2-u3-w2', 'l-eng-b2-u4-w2', 'l-eng-b2-u5-w2'];
let fixCount = 0;

targets.forEach(id => {
  const l = L.find(x => x.id === id);
  if (!l) { console.log('NOT FOUND: ' + id); return; }
  const s = l.process[2]; // step3 = index 2
  if (!s.content.includes('预设回答')) {
    // Insert 预设回答 before 板书时机
    s.content = s.content.replace(/板书时机/, '预设回答：（学生修改中，此处无口头回答）板书时机');
    fixCount++;
    console.log('Fixed: ' + id + ' step3');
  }
});

fs.writeFileSync(LESSONS_PATH, 'module.exports = ' + JSON.stringify(L, null, 2) + ';\n', 'utf-8');
console.log('Done: ' + fixCount + ' fixes applied');
