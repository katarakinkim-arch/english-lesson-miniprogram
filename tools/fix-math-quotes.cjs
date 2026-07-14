// 将 gen-math-b1*.js 中 content: '...' 字符串内的非法单引号(强调引号)转为转义双引号
// 仅处理 content 字段，不动 tags/title/objectives 等正常单引号字符串
const fs = require('fs');
const files = process.argv.slice(2);
files.forEach(f => {
  let s = fs.readFileSync(f, 'utf8');
  const re = /content: '([\s\S]*?)'(?=\s*\},?\s*$|\s*',)/gm;
  let n = 0;
  s = s.replace(re, (m, body) => {
    const fixed = body.replace(/'/g, '\\"');
    if (fixed !== body) n++;
    return "content: '" + fixed + "'";
  });
  fs.writeFileSync(f, s, 'utf8');
  console.log(f + ' : 修复 content 段落 ' + n + ' 处');
});
