// 生成一段真实可播放的占位音频（WAV，440Hz 正弦音 2 秒，16bit/8kHz）
// 用途：试点验证 PPT 音频嵌入管线；真实教材听力音频待用户提供后替换。
const fs = require('fs');
const path = require('path');
const outDir = path.join(__dirname, '..', 'images', 'lessons', 'l-eng-b1-u2-ls');
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
const sampleRate = 8000, duration = 2, amp = 12000;
const n = sampleRate * duration;
const dataBytes = n * 2;
const buf = Buffer.alloc(44 + dataBytes);
// RIFF header
buf.write('RIFF', 0); buf.writeUInt32LE(36 + dataBytes, 4); buf.write('WAVE', 8);
buf.write('fmt ', 12); buf.writeUInt32LE(16, 16); buf.writeUInt16LE(1, 20); // PCM
buf.writeUInt16LE(1, 22); // mono
buf.writeUInt32LE(sampleRate, 24); buf.writeUInt32LE(sampleRate * 2, 28);
buf.writeUInt16LE(2, 32); buf.writeUInt16LE(16, 34);
buf.write('data', 36); buf.writeUInt32LE(dataBytes, 40);
for (let i = 0; i < n; i++) {
  const t = i / sampleRate;
  // 440Hz 主音 + 轻微 660Hz 泛音，首尾 50ms 淡入淡出，避免爆音
  let s = Math.sin(2 * Math.PI * 440 * t) * 0.7 + Math.sin(2 * Math.PI * 660 * t) * 0.3;
  const fade = Math.min(t, duration - t, 0.05) / 0.05;
  s *= fade;
  buf.writeInt16LE(Math.round(s * amp), 44 + i * 2);
}
const out = path.join(outDir, 'listening.wav');
fs.writeFileSync(out, buf);
console.log('WAV written:', out, (buf.length / 1024).toFixed(0) + 'KB');
