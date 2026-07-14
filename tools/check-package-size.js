// tools/check-package-size.js — 模拟微信打包体积（主包=根目录-忽略项；各子包独立）
const fs = require('fs');
const path = require('path');
const BASE = path.join(__dirname, '..');

function walk(dir, out) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name === '.git' || e.name === 'node_modules') continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else out.push(p);
  }
  return out;
}
function rel(p) { return path.relative(BASE, p).replace(/\\/g, '/'); }

// 模拟 project.config.json 的 packOptions.ignore
function isIgnored(r) {
  if (r.startsWith('tools/')) return true;
  if (/^[^\/]+\.html$/.test(r)) return true;       // 根目录预览 html
  if (/^data\/lessons-.*\.js$/.test(r)) return true; // 根目录源数据
  if (r === 'data/lessons.js') return true;
  return false;
}

const all = walk(BASE, []);
const main = [];
const subs = {};
for (const f of all) {
  const r = rel(f);
  if (r.startsWith('subpackages/')) {
    const m = r.match(/^subpackages\/([^\/]+)\//);
    const root = m ? m[1] : '?';
    (subs[root] = subs[root] || []).push(f);
  } else {
    if (isIgnored(r)) continue;
    main.push(f);
  }
}
const size = (arr) => arr.reduce((s, f) => s + fs.statSync(f).size, 0);
const KB = 1024, LIMIT = 2048 * KB;

console.log('MAIN package :', (size(main) / KB).toFixed(1) + ' KB', size(main) <= LIMIT ? 'OK' : 'OVER LIMIT!');
for (const k of Object.keys(subs).sort()) {
  const s = size(subs[k]);
  console.log('SUB ' + k.padEnd(8) + ':', (s / KB).toFixed(1) + ' KB', s <= LIMIT ? 'OK' : 'OVER LIMIT!');
}
console.log('TOTAL (all subpackages):', (Object.keys(subs).reduce((t, k) => t + size(subs[k]), 0) / KB).toFixed(1) + ' KB (limit 20MB)');
