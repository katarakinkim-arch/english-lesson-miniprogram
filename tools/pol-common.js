// 高中政治教案生成公共模块（人教版2019）
// 提供：makeLesson 工厂、C(content 组装，保证六要素标记齐全)、finalize(按册前缀幂等合并)
const fs = require('fs');
const path = require('path');

const LESSONS_PATH = path.join(__dirname, '..', 'data', 'lessons-politics.js');
const SUBJECT = '政治';

// 模块级册名，由各生成脚本通过 setBook 设置；makeLesson 未显式传 book 时回退到此值
let BOOK = '';
function setBook(b) { BOOK = b; }

// 组装教学过程每一步的 content，确保六要素标记齐全：
// 【PPT页号】【教师台词】【预设回答】【板书时机】【差异化提示】【易错点提醒】
// 用法：C({ppt:'P1 导入图', teacher:'……', preset:'……', board:'……', diff:'……', err:'……'})
function C(o) {
  const ppt = o.ppt || 'P? 环节';
  const teacher = (o.teacher || '').replace(/'/g, '"');
  const preset = (o.preset || '学生结合本课内容与生活经验思考作答，教师引导归纳要点。').replace(/'/g, '"');
  const board = (o.board || '随讲解自然生成，关键概念与结构即时上板。').replace(/'/g, '"');
  const diff = (o.diff || 'B班达成基础目标即可；A班在基础上做拓展、变式与深度说理。').replace(/'/g, '"');
  const err = (o.err || '紧扣本环节目标，提醒学生避开本节典型错误。').replace(/'/g, '"');
  return '【PPT ' + ppt + '】' + teacher + ' 预设回答：「' + preset + '」 板书时机：' + board + ' 差异化提示：' + diff + ' 易错点提醒：' + err;
}

function makeLesson(d) {
  return {
    id: d.id,
    lessonId: d.id,
    title: d.title,
    book: d.book || BOOK,
    unitNumber: d.unitNumber,
    unitTitle: d.unitTitle,
    lessonType: d.lessonType || 'new',
    lessonTypeName: d.lessonTypeName || '新授课',
    periodNumber: d.periodNumber,
    duration: 45,
    grade: d.grade || '高一',
    subject: SUBJECT,
    coreLiteracy: d.coreLiteracy,
    tags: d.tags,
    textbookAnalysis: d.textbookAnalysis,
    overview: d.overview,
    objectives: d.objectives,
    keyPoints: d.keyPoints,
    difficulties: d.difficulties,
    teachingMethods: d.teachingMethods,
    preparation: d.preparation,
    process: d.process,
    blackboard: d.blackboard,
    exercises: d.exercises,
    reflection: d.reflection,
    aiModel: 'claude-opus',
    viewCount: 0,
    downloadCount: 0,
    createdAt: d.createdAt || '2026-07-14T12:00:00Z'
  };
}

// 幂等合并：排除本册前缀后，与既有数据拼接写回
function finalize(PREFIX, periods) {
  let L = [];
  try { L = require(LESSONS_PATH); } catch (e) { L = []; }
  const rest = L.filter(l => !(l.id && l.id.startsWith(PREFIX)));
  const all = rest.concat(periods);
  fs.writeFileSync(LESSONS_PATH, 'module.exports = ' + JSON.stringify(all, null, 2) + ';\n', 'utf8');
  console.log('OK: ' + PREFIX + ' generated (' + periods.length + ' lessons)');
  periods.forEach(p => console.log('  ' + p.id + ' [' + p.lessonTypeName + '] ' + p.title));
}

module.exports = { C, makeLesson, finalize, setBook, LESSONS_PATH, SUBJECT };
