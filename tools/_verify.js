const L = require('../data/lessons.js');

// Spot check specific fixes
const checks = [
  // U1 LS step3: should now have PPT + 板书时机
  {id:'l-eng-b1-u1-ls', step:3, checks:['【PPT','板书']},
  // U1 LS step4: should have PPT + 差异化
  {id:'l-eng-b1-u1-ls', step:4, checks:['【PPT','差异化']},
  // U1 LS step5: should have 板书时机
  {id:'l-eng-b1-u1-ls', step:5, checks:['板书时机']},
  // U1 LS step6: should have all 5
  {id:'l-eng-b1-u1-ls', step:6, checks:['【PPT','预设回答','板书','差异化','易错点']},
  // U1 R1 step3: should have PPT
  {id:'l-eng-b1-u1-r1', step:3, checks:['【PPT']},
  // U2 LS step4: should have PPT
  {id:'l-eng-b1-u2-ls', step:4, checks:['【PPT']},
  // U2 R1 step6: should have PPT
  {id:'l-eng-b1-u2-r1', step:6, checks:['【PPT']},
  // U2 R2 step4: should have 预设回答
  {id:'l-eng-b1-u2-r2', step:4, checks:['预设回答']},
  // U2 G step4: should have 预设回答
  {id:'l-eng-b1-u2-g', step:4, checks:['预设回答']},
  // U2 W2 step2: should have PPT + 预设回答
  {id:'l-eng-b1-u2-w2', step:2, checks:['【PPT','预设回答']},
  // U2 P step3: should have PPT + 预设回答
  {id:'l-eng-b1-u2-p', step:3, checks:['【PPT','预设回答']},
  // U1 W2 step1-5: all should have PPT
  {id:'l-eng-b1-u1-w2', step:1, checks:['【PPT']},
  {id:'l-eng-b1-u1-w2', step:5, checks:['预设回答','差异化']},
];

let allOk = true;
checks.forEach(chk => {
  const l = L.find(x => x.id === chk.id);
  if (!l) { console.log('NOT FOUND: ' + chk.id); allOk = false; return; }
  const s = l.process[chk.step - 1];
  const c = s.content || '';
  const fails = chk.checks.filter(ck => !c.includes(ck));
  if (fails.length > 0) {
    console.log('FAIL ' + chk.id + ' step' + chk.step + ': missing ' + fails.join(', '));
    console.log('  content[:150]: ' + c.substring(0, 150));
    allOk = false;
  }
});

if (allOk) {
  console.log('ALL CHECKS PASSED ✅');
  
  // Show a few complete step contents
  console.log('\n=== Spot samples ===');
  [['l-eng-b1-u1-ls', 6], ['l-eng-b1-u2-ls', 4], ['l-eng-b1-u2-w2', 2]].forEach(([id, step]) => {
    const l = L.find(x => x.id === id);
    const s = l.process[step - 1];
    console.log('\n--- ' + id + ' step' + step + ' [' + s.step + '] ---');
    console.log(s.content);
  });
}
