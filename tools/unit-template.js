// tools/unit-template.js
// 按 U1 金标准结构，把一个单元（8 课时）构建为 lessons.js 数组元素。
// 使用：见 gen-u2.js / gen-u3.js ...

const BOOK_CODE = { '必修第一册': 'b1', '必修第二册': 'b2', '必修第三册': 'b3' };
const TYPE_NAME = {
  'listening-speaking': '听与说',
  'reading': '阅读',
  'grammar': '语法',
  'listening-talking': '听与谈',
  'writing': '写作',
  'project': '项目复习',
};
// id 后缀：reading 用 r1/r2、writing 用 w1/w2，其余单字母
const TYPE_SUFFIX = {
  'listening-speaking': 'ls',
  'reading': 'r',
  'grammar': 'g',
  'listening-talking': 'lt',
  'writing': 'w',
  'project': 'p',
};

// 给一个单元的 8 课时 spec，补全公共字段并返回 lesson 对象数组
function buildUnit({ book, unitNumber, unitTitle, bookLabel, periods }) {
  const bc = BOOK_CODE[book] || 'bx';
  let rIdx = 0, wIdx = 0;
  return periods.map(p => {
    const base = TYPE_SUFFIX[p.lessonType] || 'x';
    let suffix = base;
    if (p.lessonType === 'reading') { rIdx++; suffix = 'r' + rIdx; }
    else if (p.lessonType === 'writing') { wIdx++; suffix = 'w' + wIdx; }
    const id = 'l-eng-' + bc + '-u' + unitNumber + '-' + suffix;
    const lessonTypeName = p.lessonTypeName || TYPE_NAME[p.lessonType] || '课时';
    return {
      id,
      lessonId: id,
      title: p.title,
      book,
      unitNumber,
      unitTitle,
      lessonType: p.lessonType,
      lessonTypeName,
      lessonNumber: p.periodNumber,
      periodNumber: p.periodNumber,
      duration: p.duration,
      grade: '高一',
      subject: '英语',
      tags: p.tags || [lessonTypeName, 'Unit ' + unitNumber, unitTitle, '人教版' + (bookLabel || book) + ' U' + unitNumber, '第' + p.periodNumber + '节课'],
      textbookAnalysis: p.textbookAnalysis,
      overview: p.overview,
      objectives: p.objectives,
      keyPoints: p.keyPoints,
      difficulties: p.difficulties,
      teachingMethods: p.teachingMethods,
      preparation: p.preparation,
      process: p.process,
      blackboard: p.blackboard,
      exercises: p.exercises,
      reflection: p.reflection,
      aiModel: 'claude-opus',
      viewCount: 0,
      downloadCount: 0,
      createdAt: p.createdAt || '2026-07-13T18:00:00Z',
    };
  });
}

// 在已有 lessons 中，用新 spec 替换指定单元（先删旧课后追加新课），保持其余不变
function replaceUnit(lessons, spec) {
  const rest = lessons.filter(l => !(l.book === spec.book && l.unitNumber === spec.unitNumber));
  return rest.concat(buildUnit(spec));
}

module.exports = { buildUnit, replaceUnit, BOOK_CODE, TYPE_NAME, TYPE_SUFFIX };
