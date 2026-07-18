// 幂等同步：把 preview_v7/_fine_progress/*.json（audit=PASS）追加进
// preview_v7/_RESEARCH_TRACK.md 的「已完成（精细调研）」表格，并重新编号。
// 已存在的行（按 ID 判断）保留，不重复；新行按 id 顺序追加。
const fs = require("fs");
const path = require("path");
const ROOT = path.resolve(__dirname, "..");
const MD = path.join(ROOT, "preview_v7/_RESEARCH_TRACK.md");
const PROG = path.join(ROOT, "preview_v7/_fine_progress");

function esc(s) { return String(s == null ? "" : s).replace(/\|/g, "\\|").replace(/\n/g, " "); }

const md = fs.readFileSync(MD, "utf8").split("\n");
// 定位表格块
let hi = -1;
for (let i = 0; i < md.length; i++) {
  if (md[i].includes("| # |") || md[i].includes("| # |")) { hi = i; break; }
  if (md[i].trim().startsWith("| #") && md[i].includes("ID")) { hi = i; break; }
}
if (hi < 0) { console.error("找不到表格头"); process.exit(1); }
let end = hi + 1;
while (end < md.length && md[end].trim().startsWith("|")) end++;
const header = md[hi];            // 表头
const sep = md[hi + 1];           // 分隔行
// 解析已有数据行
const existing = [];
for (let i = hi + 2; i < end; i++) {
  const line = md[i].trim();
  if (!line.startsWith("|")) continue;
  const cells = line.split("|").map(c => c.trim()).filter((_, idx, arr) => idx > 0 && idx < arr.length - 1);
  if (cells.length >= 2) existing.push({ id: cells[1], title: cells[2], sources: cells[3], photo: cells[4], audit: cells[5], renderer: cells[6] });
}
const existingIds = new Set(existing.map(r => r.id));

// 读所有进度 JSON
let added = 0;
const files = fs.readdirSync(PROG).filter(f => f.endsWith(".json"));
for (const f of files) {
  let j; try { j = JSON.parse(fs.readFileSync(path.join(PROG, f), "utf8")); } catch (e) { continue; }
  if (j.audit !== "PASS") continue;
  if (existingIds.has(j.id)) continue;
  const sources = Array.isArray(j.sources) ? j.sources.join("；") : (j.sources || "");
  existing.push({
    id: j.id, title: j.title || "", sources: sources,
    photo: j.photo || "色块兜底", audit: "PASS×4", renderer: j.renderer || `tools/_render_${j.id}.py`
  });
  existingIds.add(j.id); added++;
}
// 重新编号
const rows = existing.map((r, i) =>
  `| ${i + 1} | ${esc(r.id)} | ${esc(r.title)} | ${esc(r.sources).slice(0, 80)} | ${esc(r.photo)} | ${esc(r.audit)} | ${esc(r.renderer)} |`
);
const block = [header, sep, ...rows].join("\n");
const newMd = [...md.slice(0, hi), block, ...md.slice(end)].join("\n");
fs.writeFileSync(MD, newMd);
console.log(`OK: 表格共 ${rows.length} 行，本次新增 ${added} 行（进度 JSON 中 PASS 数=${files.length}）`);
