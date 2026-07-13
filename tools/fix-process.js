/**
 * fix-process.js — 修复必修一 process step 六要素缺失
 * 
 * 目标：每条 process step 的 content 必须同时包含
 *   【PPT页号】【教师台词】【预设回答】【板书时机】【差异化提示】【易错点提醒】
 * 
 * 逻辑：
 *   1. 读取 lessons.js
 *   2. 对每个已知缺失的 step 补全缺失要素
 *   3. 写回 lessons.js + 重新生成预览
 */

const fs = require('fs');
const path = require('path');

const LESSONS_PATH = path.join(__dirname, '..', 'data', 'lessons.js');
const lessons = require(LESSONS_PATH);

let fixCount = 0;
let fixes = [];

// ============================================================
// 辅助：检查并报告缺失
// ============================================================
function checkMissing(content, label) {
  const missing = [];
  if (!content.includes('【PPT')) missing.push('PPT');
  if (!content.includes('预设回答') && !content.includes('预设产出')) missing.push('预设回答');
  if (!content.includes('板书') && !content.includes('无')) missing.push('板书时机');
  if (!content.includes('差异化')) missing.push('差异化');
  if (!content.includes('易错点')) missing.push('易错点');
  return missing;
}

function getLesson(book, unit, suffix) {
  const id = 'l-eng-b1-u' + unit + '-' + suffix;
  return lessons.find(l => l.id === id);
}

function getStep(lesson, idx) {
  return lesson.process[idx];
}

function setContent(lesson, idx, content) {
  lesson.process[idx].content = content;
  fixCount++;
  fixes.push(lesson.id + ' step' + (idx+1));
}

// ============================================================
// U2-U5 系统性修复
// ============================================================

// LS step4（听中填表）：content 以【音频】开头，缺 PPT
function fixLS_step4(lesson) {
  const s = getStep(lesson, 3); // step 4 (0-indexed = 3)
  const c = s.content;
  const missing = checkMissing(c, lesson.id + ' LS step4');
  if (missing.includes('PPT')) {
    // 把【PPT P5 表格】插在【音频】前面
    s.content = c.replace(/^【音频/, '【PPT P5 表格】【音频');
  }
}

// LS step6 现在已经正确了（有【PPT P6】），跳过

// R1 step6（小结）：以【总结】开头，缺 PPT
function fixR1_step6(lesson, unitNum) {
  const s = getStep(lesson, 5); // step 6
  const c = s.content;
  if (!c.includes('【PPT')) {
    s.content = c.replace(/^【总结】/, '【PPT P7 总结回顾】');
  }
}

// R2 step4（语料库搭建）：缺预设回答
function fixR2_step4(lesson, subject) {
  const s = getStep(lesson, 3); // step 4
  const c = s.content;
  if (!c.includes('预设回答')) {
    // 在板书时机前插入预设回答
    s.content = c.replace(/板书时机：/, '预设回答：按' + subject + '模板分类填写词条。板书时机：');
  }
}

// G step4（归纳/产出）：缺预设回答
function fixG_step4(lesson, answers) {
  const s = getStep(lesson, 3); // step 4
  const c = s.content;
  if (!c.includes('预设回答')) {
    s.content = c.replace(/板书时机：/, '预设回答：' + answers + '板书时机：');
  }
}

// LT step3（听中记录）：以【音频】开头，缺 PPT
function fixLT_step3(lesson) {
  const s = getStep(lesson, 2); // step 3
  const c = s.content;
  if (!c.includes('【PPT')) {
    s.content = c.replace(/^【音频】/, '【PPT P4 听力任务卡】【音频】');
  }
}

// W1 step4（积语料）：缺预设回答
function fixW1_step4(lesson, subject) {
  const s = getStep(lesson, 3); // step 4
  const c = s.content;
  if (!c.includes('预设回答')) {
    s.content = c.replace(/板书时机：/, '预设回答：按' + subject + '分类卡填写词条。板书时机：');
  }
}

// W2 step2（起草）：以【写作】开头，缺 PPT + 预设回答
function fixW2_step2(lesson) {
  const s = getStep(lesson, 1); // step 2
  const c = s.content;
  if (!c.includes('【PPT')) {
    s.content = c.replace(/^【写作】/, '【PPT P6 写作提纲】');
  }
  if (!c.includes('预设回答') && !s.content.includes('预设回答')) {
    s.content = s.content.replace(/板书时机：/, '预设回答：（学生静写中，此处无口头回答）板书时机：');
  }
}

// W2 step4（修改）：以【修改】开头，缺 PPT + 预设回答
function fixW2_step4(lesson) {
  const s = getStep(lesson, 3); // step 4
  const c = s.content;
  if (!c.includes('【PPT')) {
    s.content = c.replace(/^【修改】/, '【PPT P9 修改清单】');
  }
  if (!c.includes('预设回答')) {
    s.content = s.content.replace(/板书时机：/, '预设回答：（学生自修中，教师口头提示共性错误）板书时机：');
  }
}

// P step3（制作海报/路线卡）：缺 PPT + 预设回答
function fixP_step3(lesson) {
  const s = getStep(lesson, 2); // step 3
  const c = s.content;
  if (!c.includes('【PPT')) {
    s.content = c.replace(/【实物/, '【PPT P7 范例参考】【实物');
  }
  if (!c.includes('预设回答')) {
    s.content = s.content.replace(/板书时机：/, '预设回答：（小组讨论制作中，教师巡视指导）板书时机：');
  }
}

// ============================================================
// U1 个别修复
// ============================================================

function fixU1() {
  // LS: l-eng-b1-u1-ls
  const ls = getLesson('必修第一册', 1, 'ls');
  
  // step2: 缺易错点 → 在差异化后添加
  let s2 = ls.process[1].content;
  if (!s2.includes('易错点')) {
    ls.process[1].content = s2.replace(/差异化提示：(.+)$/, '差异化提示：$1易错点提醒：join 与 attend 区别 — join club/attend class，板书对比标搭配。');
  }
  
  // step3: 缺PPT、板书时机
  let s3 = ls.process[2].content;
  if (!s3.includes('【PPT')) {
    ls.process[2].content = '【PPT P8 听力题】【音频1】' + s3.replace(/^【音频1】/, '');
  }
  if (!s3.includes('板书时机') && !ls.process[2].content.includes('板书时机')) {
    ls.process[2].content = ls.process[2].content.replace(/预设回答：/, '板书时机：答案填于黑板社团矩阵。预设回答：');
  }
  
  // step4: 缺PPT、差异化
  let s4 = ls.process[3].content;
  if (!s4.includes('【PPT')) {
    ls.process[3].content = '【PPT P9 听力题】' + s4;
  }
  if (!s4.includes('差异化') && !ls.process[3].content.includes('差异化')) {
    ls.process[3].content = ls.process[3].content.replace(/预设回答/, '差异化提示：B班只填社团名；A班补填招新要求。预设回答');
  }
  
  // step5: 缺板书时机
  let s5 = ls.process[4].content;
  if (!s5.includes('板书时机') && !s5.includes('无。')) {
    ls.process[4].content = s5.replace(/差异化/, '板书时机：补充新词至社团矩阵。差异化');
  }
  
  // step6: 缺PPT、预设回答、差异化 → 重写这句
  ls.process[5].content = '【PPT P10 总结】带学生回顾黑板社团矩阵，总结「表达意愿三句型」。教师：「Can you name the three patterns?」 预设回答：「I would like to / I am interested in / I recommend!」 板书时机：彩色笔圈出三句型。差异化提示：B班看黑板回答；A班闭眼回忆。易错点提醒：下节课 Reading 会用到这些社团词，提醒复习。';

  // R1: l-eng-b1-u1-r1
  const r1 = getLesson('必修第一册', 1, 'r1');
  
  // step3: 缺PPT → 加在开头
  if (!r1.process[2].content.includes('【PPT')) {
    r1.process[2].content = '【PPT P5 主旨选择】' + r1.process[2].content;
  }
  // step4: 缺PPT
  if (!r1.process[3].content.includes('【PPT')) {
    r1.process[3].content = '【PPT P6 时间轴】' + r1.process[3].content;
  }
  // step6: 缺PPT、预设回答、差异化
  r1.process[5].content = '【PPT P9 情感弧线】两人一组用时间轴复述 Adam 的一天。教师巡视纠音。教师：「Use past tense! He felt nervous, then...」 预设回答：「He felt nervous, but later he became confident.」 板书时机：留下情感弧线供复述参考。差异化提示：B班给关键词连句；A班脱稿复述。易错点提醒：复述用过去时，提醒动词变化。';

  // R2: l-eng-b1-u1-r2
  const r2 = getLesson('必修第一册', 1, 'r2');
  
  // step5: 缺PPT、预设回答、差异化
  r2.process[4].content = '【PPT P7 产出任务】用本课词写 3 句「介绍自己高中期待」。随后填「易混词清单」（confident/confidence, look forward to doing）。教师巡视。教师：「Write 3 sentences about your expectations.」 预设回答：「I am looking forward to making new friends.」 板书时机：留关键词供参考。差异化提示：B班照黑板词造句；A班独立写并用至少2个新词。易错点提醒：look forward to + doing，to 是介词不是不定式。';

  // G: l-eng-b1-u1-g
  const g = getLesson('必修第一册', 1, 'g');
  
  // step5: 缺PPT、预设回答、差异化
  g.process[4].content = '【PPT P6 产出任务】用至少2类短语写3句描述同学。教师：「Describe 3 classmates using what we learned.」 预设回答：「Li Hua plays the guitar very well. / Zhang Wei is the boy whose hair is curly.」 板书时机：留公式供写时参考。差异化提示：B班给填空式句型；A班自由造句。易错点提醒：写后自判中心词——圈出名词短语和定语从句连接点。';

  // LT: l-eng-b1-u1-lt
  const lt = getLesson('必修第一册', 1, 'lt');
  
  // step2: 缺PPT → 添加音频PPT号
  if (!lt.process[1].content.includes('【PPT')) {
    lt.process[1].content = '【PPT P3 听力任务】' + lt.process[1].content;
  }
  // step3: 缺PPT
  if (!lt.process[2].content.includes('【PPT')) {
    lt.process[2].content = '【PPT P4 听力任务】' + lt.process[2].content;
  }
  // step5: 缺PPT、预设回答、差异化
  lt.process[4].content = '【PPT P6 汇报框架】一组上台 1 分钟英文汇报计划。教师：「One minute per group. Be loud and clear.」 预设回答：「We are going to visit the museum and then eat lunch.」 板书时机：留 be going to 公式。差异化提示：B班看稿读；A班脱稿。易错点提醒：汇报用 are going to / will，注意主语复数一致。';

  // W1: l-eng-b1-u1-w1
  const w1 = getLesson('必修第一册', 1, 'w1');
  
  // step5: 缺PPT、预设回答、差异化
  w1.process[4].content = '【PPT P6 总结】总结结构+语库。教师：「Remember: 4 paragraphs, 3+ chunks.」 预设回答：「We know the structure now: interests, strengths, weakness, goal.」 板书时机：留结构树。差异化提示：B班再读一遍语库；A班自己说一遍结构。易错点提醒：下节课直接套用，别现编——课上写过的句子就是最好的素材。';

  // W2: l-eng-b1-u1-w2
  const w2 = getLesson('必修第一册', 1, 'w2');
  
  // step1-5: 缺PPT
  ['【PPT P5 计时写作】', '【PPT P6 互评量表】', '【PPT P7 修改指南】', '【PPT P8 讲评】', '【PPT P9 结课】'].forEach((ppt, i) => {
    if (!w2.process[i].content.includes('【PPT')) {
      w2.process[i].content = ppt + ' ' + w2.process[i].content;
    }
  });
  // step5: 缺PPT、预设回答、差异化
  w2.process[4].content = '【PPT P9 结课】总结「写—评—改」闭环。教师：「Great writers revise. Next time you will write even better.」 预设回答：「I will check my tenses next time!」 板书时机：留红线句。差异化提示：B班朗读红线句；A班自己找出自己稿子的红线亮点。易错点提醒：终稿用规范书写——卷面分在考试中真实存在。';

  // P: l-eng-b1-u1-p
  const p = getLesson('必修第一册', 1, 'p');
  
  // step2: 缺PPT
  if (!p.process[1].content.includes('【PPT')) {
    p.process[1].content = '【PPT P2 视频链接】' + p.process[1].content;
  }
  // step3: 缺PPT、预设回答
  if (!p.process[2].content.includes('【PPT')) {
    p.process[2].content = '【PPT P3 手册结构】' + p.process[2].content;
  }
  if (!p.process[2].content.includes('预设回答')) {
    p.process[2].content = p.process[2].content.replace(/板书时机：/, '教师：「Which part are you working on?」 预设回答：「The club recommendation!」 板书时机：');
  }
  // step4: 缺PPT
  if (!p.process[3].content.includes('【PPT')) {
    p.process[3].content = '【PPT P4 展示量规】' + p.process[3].content;
  }
  // step5: 缺PPT、预设回答、差异化
  p.process[4].content = '【PPT P4 自评表】学生勾选四维薄弱项并写1条补强计划。教师：「Be honest — this is for yourself.」 预设回答：「I need more speaking practice. I will talk in English for 5 minutes every day.」 板书时机：留自评维度。差异化提示：B班中文写计划、A班英文写。易错点提醒：自评要诚实，计划要具体（如「每天背5个单元词」而不是「多背单词」）。';
}

// ============================================================
// U2-U5 系统性修复
// ============================================================
function fixU2toU5() {
  const units = [
    { num: 2, r2subject: '旅行目的地', gAnswers: 'be doing已安排/will临时决定/be going to意图', w1subject: '旅行', pWhat: '路线卡' },
    { num: 3, r2subject: '体育传奇', gAnswers: '反意疑问句前肯后否/前否后肯', w1subject: '体育传奇', pWhat: '海报' },
    { num: 4, r2subject: '灾害报道', gAnswers: 'that/which指物/who指人/whom宾语/whose所有', w1subject: '灾害报道', pWhat: '海报' },
    { num: 5, r2subject: '语言文化', gAnswers: 'where地点/when时间/why原因/介词+which替换', w1subject: '语言学习', pWhat: '海报' },
  ];

  units.forEach(u => {
    const ls = getLesson('必修第一册', u.num, 'ls');
    const r1 = getLesson('必修第一册', u.num, 'r1');
    const r2 = getLesson('必修第一册', u.num, 'r2');
    const g = getLesson('必修第一册', u.num, 'g');
    const lt = getLesson('必修第一册', u.num, 'lt');
    const w1 = getLesson('必修第一册', u.num, 'w1');
    const w2 = getLesson('必修第一册', u.num, 'w2');
    const p = getLesson('必修第一册', u.num, 'p');

    fixLS_step4(ls);
    fixR1_step6(r1, u.num);
    fixR2_step4(r2, u.r2subject);
    fixG_step4(g, u.gAnswers);
    fixLT_step3(lt);
    fixW1_step4(w1, u.w1subject);
    fixW2_step2(w2);
    fixW2_step4(w2);
    fixP_step3(p);
  });
}

// ============================================================
// 执行
// ============================================================
console.log('=== 开始修复必修一 process step 六要素 ===');
console.log('  U1 个别修复中...');
fixU1();
console.log('  U2-U5 系统性修复中...');
fixU2toU5();
console.log('  完成 ' + fixCount + ' 处修复');
console.log('  涉及: ' + fixes.join(', '));

// 写回 lessons.js
const content = 'module.exports = ' + JSON.stringify(lessons, null, 2) + ';\n';
fs.writeFileSync(LESSONS_PATH, content, 'utf-8');
console.log('  已写回 ' + LESSONS_PATH);

// 验证
console.log('\n=== 验证 ===');
let verifyTotal = 0;
let verifyList = [];
const b1Check = lessons.filter(l => l.book === '必修第一册');
b1Check.forEach(l => {
  (l.process || []).forEach((s, i) => {
    const c = s.content || '';
    const missing = [];
    if (!c.includes('【PPT')) missing.push('PPT');
    if (!c.includes('预设回答') && !c.includes('预设产出')) missing.push('预设回答');
    if (!c.includes('板书')) missing.push('板书时机');
    if (!c.includes('差异化')) missing.push('差异化');
    if (!c.includes('易错点')) missing.push('易错点');
    if (missing.length > 0) {
      verifyTotal += missing.length;
      verifyList.push(l.id + ' step' + (i+1) + ': ' + missing.join(', '));
    }
  });
});
console.log('修复后剩余缺失: ' + verifyTotal);
if (verifyTotal > 0) {
  verifyList.forEach(v => console.log('  ' + v));
} else {
  console.log('  ✅ 全部通过！');
}
