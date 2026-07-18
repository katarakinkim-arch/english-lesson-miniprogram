// tools/_dump_lessons.js
// Combine every subject's module.exports array into one JSON keyed by id.
const fs = require('fs');
const path = require('path');
const files = {
  cn: 'lessons-cn.js',
  bio: 'lessons-biology.js',
  che: 'lessons-chemistry.js',
  geo: 'lessons-geography.js',
  his: 'lessons-history.js',
  math: 'lessons-math.js',
  phy: 'lessons-physics.js',
  pol: 'lessons-politics.js',
  eng: 'lessons.js',
};
const all = {};
const order = [];
for (const [subj, fn] of Object.entries(files)) {
  const mod = require(path.join(__dirname, '..', 'data', fn));
  for (const les of mod) {
    const id = les.id;
    if (!id) continue;
    les._subj = subj;
    all[id] = les;
    order.push(id);
  }
}
const out = path.join(__dirname, '..', 'data', '_all_lessons.json');
fs.writeFileSync(out, JSON.stringify({ ids: order, byId: all }, null, 0));
console.log('dumped', order.length, 'lessons ->', out);
