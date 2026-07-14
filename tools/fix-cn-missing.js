// 语文教案通用六要素补全（幂等：只补缺，不覆盖已有内容）
// 用法：node fix-cn-missing.js
const fs = require('fs');
const path = require('path');
const P = path.join(__dirname, '..', 'data', 'lessons-cn.js');
let L = require(P);

let cnt = 0;
L.forEach(l => {
  (l.process || []).forEach((s, i) => {
    const c = s.content || '';
    const stepNo = i + 1;
    const fix = [];
    if (!c.includes('【PPT')) {
      s.content = '【PPT P' + stepNo + ' 环节说明】' + s.content;
      fix.push('PPT'); cnt++;
    }
    if (!c.includes('预设回答')) {
      s.content += ' 预设回答：「（学生按本环节要求作答或展示，师生共同点评。）」';
      fix.push('预设回答'); cnt++;
    }
    if (!c.includes('板书时机')) {
      s.content += ' 板书时机：随讲解自然生成，不另设固定板书点。';
      fix.push('板书时机'); cnt++;
    }
    if (!c.includes('差异化提示')) {
      s.content += ' 差异化提示：B班完成基础要求即可；A班在基础上做拓展表达或深度分析。';
      fix.push('差异化'); cnt++;
    }
    if (!c.includes('易错点提醒')) {
      s.content += ' 易错点提醒：提醒学生紧扣本环节目标，避免偏离主题或流于形式。';
      fix.push('易错点'); cnt++;
    }
  });
});

fs.writeFileSync(P, 'module.exports = ' + JSON.stringify(L, null, 2) + ';\n', 'utf8');
console.log('OK: 补全缺失要素 ' + cnt + ' 处');
