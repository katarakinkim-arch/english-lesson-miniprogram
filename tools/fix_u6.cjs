const fs = require('fs');
const p = 'gen-cn-bs-u6.js';
let s = fs.readFileSync(p, 'utf8');
// Convert blackboard: '...' (multiline) into blackboard: `...` (template literal, multiline OK)
const out = s.replace(/blackboard: '([\s\S]*?)'/g, (m, body) => 'blackboard: `' + body + '`');
fs.writeFileSync(p, out, 'utf8');
const after = fs.readFileSync(p, 'utf8');
console.log('template-literal blackboards:', (after.match(/blackboard: `/g) || []).length);
console.log('old single-quote blackboards left:', (after.match(/blackboard: '/g) || []).length);
