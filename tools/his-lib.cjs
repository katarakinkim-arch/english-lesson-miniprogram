// his-lib.cjs —— 高中历史教案生成公共库（人教版2019）
// 用法：在各 gen-his-*.js 中 const { build, emit } = require('./his-lib.cjs');
// 每课用一个紧凑 spec 数组描述，build() 展开为完整 lesson 对象；
// 教学环节的 6 个【】标记由 makeStep() 自动生成（含情境化默认值，关键步可覆盖）。

const fs = require('fs');

// 册码 -> 书名 / 年级
const BOOK = {
  b1: '必修《中外历史纲要》上册',
  b2: '必修《中外历史纲要》下册',
  sx1: '选择性必修1 国家制度与社会治理',
  sx2: '选择性必修2 经济与社会生活',
  sx3: '选择性必修3 文化交流与传播'
};
const GRADE = { b1: '高一', b2: '高一', sx1: '高二', sx2: '高二', sx3: '高二' };

// 历史核心素养（5）：唯物史观/时空观念/史料实证/历史解释/家国情怀
const CORE = ['唯物史观', '时空观念', '史料实证', '历史解释', '家国情怀'];

// 根据环节名推断合适的“预设回答”（教师走进课堂即可用）
function defaultPreset(name) {
  const s = name || '';
  if (/导入|情境|引入|热身|实例|溯源|激趣/.test(s)) return '学生联系已有知识或生活经验举例、类比，说出直觉认识，教师顺势引出本课主题。';
  if (/史料|材料|实证|文献|地图|文物|图片|表格/.test(s)) return '学生阅读史料/地图，提取关键信息(时间、主体、态度、数据)，指出史料类型与价值，教师点拨实证方法。';
  if (/探究|分析|讨论|归纳|比较|思辨|梳理/.test(s)) return '学生分组或同桌讨论，提取信息、归纳要点，教师追问关键因果与历史解释的角度。';
  if (/概念|定义|制度|背景|原因|内涵|特点|措施|政策|法律/.test(s)) return '学生复述本课核心概念(或制度)并指认其背景与前提条件，教师用对比/反例澄清易混点。';
  if (/练习|演练|巩固|训练|应用|迁移|解题/.test(s)) return '学生先独立完成后同桌互评，口述思路与结果，教师点错纠偏并小结方法。';
  if (/小结|总结|作业|收口|回顾|升华/.test(s)) return '学生自主归纳本课主线(背景—内容—影响/意义)，同伴补充遗漏，教师一句话收口并预告下节。';
  return '学生按本环节要求作答或展示，师生共同点评，必要时教师示范。';
}

// 根据环节名推断合适的“易错点提醒”
function defaultPitfall(name) {
  const s = name || '';
  if (/背景|原因|根源|条件|动机/.test(s)) return '区分\"根本原因\"与\"直接原因/导火索\"，避免把触发事件等同于深层根源。';
  if (/时间|年代|朝代|时序|纪年|世纪/.test(s)) return '时序易混，建议边讲边画\"时间轴\"，先记朝代/阶段先后再填事件与人物。';
  if (/影响|意义|评价|作用|地位/.test(s)) return '评价要分\"积极/消极\"\"短期/长远\"\"对谁而言\"，避免单一化、绝对化。';
  if (/制度|政策|法律|措施|政体|体制/.test(s)) return '制度须放回其时代背景与适用对象中理解，避免脱离条件空谈\"优劣\"。';
  if (/概念|名词|内涵|术语|含义/.test(s)) return '核心概念易望文生义，先下准确定义再运用，避免张冠李戴。';
  if (/比较|异同|对比|区别|联系/.test(s)) return '比较先定标准(政治/经济/文化/阶段)，逐项对照，避免只罗列事实而无对比。';
  return '紧扣本课目标，提醒学生避开\"时序错乱\"\"张冠李戴\"\"评价单一\"\"因果倒置\"等典型错误。';
}

// 由紧凑参数生成单步 content（自动补全 6 个【】标记）
function makeStep(name, time, teacher, o) {
  o = o || {};
  const ppt = o.ppt || 'P?';
  const preset = o.preset || defaultPreset(name);
  const blackboard = o.blackboard || '随讲随写：关键时间轴、因果链、制度要点即时上板，不另设固定板书点。';
  const diff = o.diff || 'B班达成识记(时间、人物、事件、制度)即可；A班在基础上做史料辨析、因果论证与开放探究。';
  const pitfall = o.pitfall || defaultPitfall(name);
  return {
    step: name,
    time: time,
    content: '【PPT ' + ppt + '】' + teacher
      + ' 预设回答：「' + preset + '」'
      + ' 板书时机：' + blackboard
      + ' 差异化提示：' + diff
      + ' 易错点提醒：' + pitfall
  };
}

// spec 顺序：
// [0]idSuffix [1]unitNumber [2]unitTitle [3]periodNumber [4]tags
// [5]textbookAnalysis [6]overview(含【学情分析】) [7]objectives(4)
// [8]keyPoints [9]difficulties [10]teachingMethods [11]preparation
// [12]steps:[[name,time,teacher,opts?],...] [13]blackboard(反引号) [14]exercises [15]reflection
// [16]coreLiteracy?(可选)
function build(prefix, sp) {
  const code = prefix.replace('l-his-', '');
  const id = 'l-his-' + code + '-' + sp[0];
  const unitNumber = sp[1];
  const unitTitle = sp[2];
  const title = '第' + unitNumber + '课 ' + unitTitle;
  const process = (sp[12] || []).map(function (s) { return makeStep(s[0], s[1], s[2], s[3]); });
  return {
    id: id, lessonId: id, title: title,
    book: BOOK[code], unitNumber: unitNumber, unitTitle: unitTitle,
    lessonType: 'new', lessonTypeName: '新授课',
    periodNumber: sp[3], duration: 45,
    grade: GRADE[code], subject: '历史',
    coreLiteracy: sp[16] || CORE,
    tags: sp[4], textbookAnalysis: sp[5], overview: sp[6],
    objectives: sp[7], keyPoints: sp[8], difficulties: sp[9],
    teachingMethods: sp[10], preparation: sp[11],
    process: process, blackboard: sp[13], exercises: sp[14], reflection: sp[15],
    aiModel: 'claude-opus', viewCount: 0, downloadCount: 0,
    createdAt: '2026-07-14T12:00:00Z'
  };
}

// 合并写入：排除本前缀已有记录后追加本脚本生成的课时（幂等）
function emit(prefix, periods, outPath) {
  let prev = [];
  try { prev = require(outPath); } catch (e) { prev = []; }
  const rest = prev.filter(function (l) { return !(l.id && l.id.indexOf(prefix + '-') === 0); });
  const merged = rest.concat(periods);
  fs.writeFileSync(outPath, 'module.exports = ' + JSON.stringify(merged, null, 2) + ';\n', 'utf8');
  console.log('OK: ' + prefix + ' generated (' + periods.length + ' lessons, total ' + merged.length + ')');
  periods.forEach(function (p) { console.log('  ' + p.id + ' ' + p.title); });
}

module.exports = { BOOK, GRADE, CORE, defaultPreset, defaultPitfall, makeStep, build, emit };
