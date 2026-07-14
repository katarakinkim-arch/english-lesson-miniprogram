// 修复必修上册U2（劳动光荣）8处六要素缺失
const fs = require('fs');
const path = require('path');
const P = path.join(__dirname, '..', 'data', 'lessons-cn.js');
let L = require(P);

function patch(id, stepIdx, append, prepend) {
  const l = L.find(x => x.id === id);
  if (!l) { console.log('MISS', id); return; }
  const s = l.process[stepIdx - 1];
  if (prepend) s.content = prepend + s.content;
  if (append) s.content = s.content + append;
}

// u2-5 step4 缺预设回答
patch('l-cn-bs-u2-5', 4, ' 预设回答：「（学生分组模拟访谈与播报，访谈对象谈岗位感受；播报组播报本组新闻稿，师生共同点评。）」');
// u2-6 step2 缺预设回答
patch('l-cn-bs-u2-6', 2, ' 预设回答：「（学生回忆单元课文人物，说出袁隆平/张秉贵/钟扬最打动自己的一个细节。）」');
// u2-6 step4 缺预设回答
patch('l-cn-bs-u2-6', 4, ' 预设回答：「（小组代表朗读采访片段或展示采访提纲，其他组补充提问。）」');
// u2-7 step5 缺预设回答
patch('l-cn-bs-u2-7', 5, ' 预设回答：「（学生对照量表互评，指出通讯的优点与可改处，如导语是否抓人、细节是否具体。）」');
// u2-7 step6 缺PPT + 缺预设回答
patch('l-cn-bs-u2-7', 6, ' 预设回答：「（学生提交终稿并互签，教师收齐存档。）」', '【PPT P7 终稿提交说明】');
// u2-8 step2 缺预设回答
patch('l-cn-bs-u2-8', 2, ' 预设回答：「（各小组依次展示分享，讲述身边劳动者的故事或采访见闻，听众提问交流。）」');
// u2-8 step5 缺预设回答
patch('l-cn-bs-u2-8', 5, ' 预设回答：「（学生用一句话概括本单元最大的收获，如『劳动的价值在于创造与坚守』。）」');

fs.writeFileSync(P, 'module.exports = ' + JSON.stringify(L, null, 2) + ';\n', 'utf8');
console.log('OK: U2 六要素已补齐');
