// 通用六要素补全（幂等：只补缺，不覆盖已有内容）
// 用法：node fix-missing.js [data文件路径，默认 lessons-cn.js]
// 预设回答按环节类型给出"教师可即用"的语境化补语，而非一句万能占位。
const fs = require('fs');
const path = require('path');
const P = process.argv[2] ? path.resolve(process.argv[2]) : path.join(__dirname, '..', 'data', 'lessons-cn.js');
let L = require(P);

// 根据环节名称推断合适的预设回答（教师走进课堂即可用）
function replyFor(step) {
  const s = (step.step || '') + ' ' + (step.content || '');
  if (/导入|引入|情境|热身|实例/.test(s)) return '学生联系生活或已有知识举例、类比，说出直觉理解，教师顺势引出本课主题。';
  if (/小结|总结|作业|收口|回顾/.test(s)) return '学生自主归纳本课核心要点，同伴补充遗漏，教师用一句话收口并预告下节。';
  if (/练习|演练|巩固|训练/.test(s)) return '学生先独立完成后同桌互评，口述思路与结果，教师点错纠偏。';
  if (/例题|例[1-9]|板演|示范|解题/.test(s)) return '学生板演或口答，说明列式（或证明）依据与典型易错点，师生共评。';
  if (/应用|建模|实际|情境问题|迁移|解决/.test(s)) return '学生将新知迁移到真实情境，说出建模（或转化）步骤与结论。';
  if (/探究|活动|操作|实验|观察|讨论/.test(s)) return '学生分组探究或操作，汇报发现，教师追问关键节点。';
  if (/概念|定义|公式|定理|性质|原理|特性|关系|表示|理解|掌握|说明|分析|推导|含义|意义/.test(s)) return '学生复述本课关键概念（或公式）并指认前提条件，教师用反例辨析澄清。';
  return '学生按本环节要求作答或展示，师生共同点评，必要时教师示范。';
}

let cnt = 0;
L.forEach(l => {
  (l.process || []).forEach((s, i) => {
    const c = s.content || '';
    const stepNo = i + 1;
    if (!c.includes('【PPT')) {
      s.content = '【PPT P' + stepNo + ' 环节说明】' + s.content;
      cnt++;
    }
    if (!c.includes('预设回答')) {
      s.content += ' 预设回答：「' + replyFor(s) + '」';
      cnt++;
    }
    if (!c.includes('板书时机')) {
      s.content += ' 板书时机：随讲解自然生成，关键定义、公式、图形即时上板，不另设固定板书点。';
      cnt++;
    }
    if (!c.includes('差异化提示')) {
      s.content += ' 差异化提示：B班达成基础目标即可；A班在基础之上做拓展、变式或深度说理。';
      cnt++;
    }
    if (!c.includes('易错点提醒')) {
      s.content += ' 易错点提醒：紧扣本环节目标，提醒学生避开本节典型错误，避免流于形式。';
      cnt++;
    }
  });
});

fs.writeFileSync(P, 'module.exports = ' + JSON.stringify(L, null, 2) + ';\n', 'utf8');
console.log('OK: 补全缺失要素 ' + cnt + ' 处');
