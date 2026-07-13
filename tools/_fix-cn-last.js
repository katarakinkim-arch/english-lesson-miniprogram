const fs = require('fs');
const path = require('path');
const LESSONS_PATH = path.join(__dirname, '..', 'data', 'lessons-cn.js');
const L = require(LESSONS_PATH);

const l = L.find(x => x.id === 'l-cn-bs-u1-7');
if (l && l.process[5]) {
  const s = l.process[5];
  if (!s.content.includes('\u3010PPT')) {
    s.content = '【PPT P7 展示要求】' + s.content;
    console.log('Fixed: l-cn-bs-u1-7 step6 补PPT标记');
  }
}

fs.writeFileSync(LESSONS_PATH, 'module.exports = ' + JSON.stringify(L, null, 2) + ';\n', 'utf8');
console.log('Done');
