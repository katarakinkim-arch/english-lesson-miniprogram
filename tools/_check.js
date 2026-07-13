const L = require('../data/lessons.js');
const tests = [
  {id:'l-eng-b1-u2-ls', step:6, check:'【PPT'},
  {id:'l-eng-b1-u3-ls', step:6, check:'【PPT'},
  {id:'l-eng-b1-u2-g', step:3, check:'【PPT'},
  {id:'l-eng-b1-u2-lt', step:2, check:'【PPT'},
  {id:'l-eng-b1-u2-r1', step:4, check:'预设回答'},
  {id:'l-eng-b1-u2-g', step:4, check:'预设回答'},
];
tests.forEach(t=>{
  const l = L.find(x => x.id === t.id);
  if (!l) { console.log(t.id + ' NOT FOUND'); return; }
  const s = l.process[t.step - 1];
  const c = s.content || '';
  const ok = c.includes(t.check);
  console.log(t.id + ' step' + t.step + ' has [' + t.check + ']: ' + ok);
  if (!ok) console.log('  content[:120]: ' + c.substring(0, 120));
});
