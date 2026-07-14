const fs = require('fs');
const p = 'gen-cn-bs-u6.js';
let s = fs.readFileSync(p, 'utf8');
let n = 0;
s = s.replace(/(blackboard: ')([\s\S]*?)(')/g, (m, pre, body, post) => {
  // Replace real newline chars inside the blackboard body with escaped \n
  const fixed = body.replace(/\r?\n/g, '\n');
  n++;
  return pre + fixed + post;
});
fs.writeFileSync(p, s, 'utf8');
console.log('Fixed blackboard blocks:', n);
