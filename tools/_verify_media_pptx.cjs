// 验证：用试点课 + 真实图片/音频字节跑 buildPPTX，产出 .pptx 并校验媒体部件
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const docgen = require(path.join(root, 'utils', 'docgen.js'));
const data = require(path.join(root, 'data', 'lessons.js'));
const media = require(path.join(root, 'data', 'media.js'));

const LID = 'l-eng-b1-u2-ls';
const lesson = data.find((l) => l.id === LID);
if (!lesson) throw new Error('lesson not found');
const m = media[LID];
const attach = (arr) => (arr || []).map((x) => ({ ...x, data: new Uint8Array(fs.readFileSync(path.join(root, x.file))) }));
lesson.media = { images: attach(m.images), audios: attach(m.audios) };

const bytes = docgen.buildPPTX(lesson);
const out = path.join(root, '_pilot_sample.pptx');
fs.writeFileSync(out, Buffer.from(bytes));
console.log('PPTX written:', out, (bytes.length / 1024).toFixed(0) + 'KB');

// ---- 校验 ----
const bufStr = Buffer.from(bytes).toString('latin1');
const bufUtf8 = Buffer.from(bytes).toString('utf8');
let ok = true;
const checks = [
  ['EOCD 签名', bufStr.includes('PK\x05\x06')],
  ['[Content_Types].xml', bufStr.includes('[Content_Types].xml')],
  ['类型 image/jpeg', bufStr.includes('image/jpeg')],
  ['类型 audio/wav', bufStr.includes('audio/wav')],
  ['媒体 image1.jpeg 部件', bufStr.includes('ppt/media/image1.jpeg')],
  ['媒体 audio1.wav 部件', bufStr.includes('ppt/media/audio1.wav')],
  ['图片关系(relType image)', bufStr.includes('relationships/image" Target="../media/image1.jpeg"')],
  ['音频关系(relType audio)', bufStr.includes('relationships/audio" Target="../media/audio1.wav"')],
  ['图片形状 <p:pic>', bufStr.includes('<p:pic>')],
  ['音频形状 <p:audio>', bufStr.includes('<p:audio>')],
  ['素材图示页标题', bufUtf8.includes('课前准备 · 素材图示')]
];
for (const [name, pass] of checks) { console.log((pass ? '  ✓ ' : '  ✗ ') + name); if (!pass) ok = false; }
console.log(ok ? '\nALL MEDIA CHECKS PASSED' : '\nSOME CHECKS FAILED');
process.exit(ok ? 0 : 1);
