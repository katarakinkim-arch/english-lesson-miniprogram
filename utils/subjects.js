// utils/subjects.js — 全学科配置（主包 + 子包共享）
// 用于：首页学科选择、收藏/记录按学科跳转对应子包详情页。
const SUBJECTS = [
  { key: 'eng', name: '英语', root: 'eng', emoji: '📘', color: '#2b6cb0', dataFile: 'lessons.js' },
  { key: 'cn', name: '语文', root: 'cn', emoji: '📗', color: '#2f855a', dataFile: 'lessons-cn.js' },
  { key: 'math', name: '数学', root: 'math', emoji: '📐', color: '#c05621', dataFile: 'lessons-math.js' },
  { key: 'physics', name: '物理', root: 'physics', emoji: '🔭', color: '#6b46c1', dataFile: 'lessons-physics.js' },
  { key: 'chem', name: '化学', root: 'chem', emoji: '⚗️', color: '#c53030', dataFile: 'lessons-chemistry.js' },
  { key: 'bio', name: '生物', root: 'bio', emoji: '🧬', color: '#25855a', dataFile: 'lessons-biology.js' },
  { key: 'his', name: '历史', root: 'his', emoji: '📜', color: '#975a16', dataFile: 'lessons-history.js' },
  { key: 'pol', name: '政治', root: 'pol', emoji: '⚖️', color: '#b7791f', dataFile: 'lessons-politics.js' },
  { key: 'geo', name: '地理', root: 'geo', emoji: '🌏', color: '#2c7a7b', dataFile: 'lessons-geography.js' }
];

// 数据里 subject 字段值 -> 子包根目录
const ROOT_BY_SUBJECT = {};
SUBJECTS.forEach((s) => { ROOT_BY_SUBJECT[s.name] = s.root; });

function rootOf(subject) {
  return ROOT_BY_SUBJECT[subject] || 'eng';
}

module.exports = { SUBJECTS, ROOT_BY_SUBJECT, rootOf };
