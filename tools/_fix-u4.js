const fs = require('fs');
let c = fs.readFileSync('./tools/gen-b2-u4.js', 'utf8');
// Replace double-backslash-quote with single-backslash-quote (only in content strings)
c = c.replace(/\\\\'/g, "\\'");
fs.writeFileSync('./tools/gen-b2-u4.js', c);
console.log('fixed');
