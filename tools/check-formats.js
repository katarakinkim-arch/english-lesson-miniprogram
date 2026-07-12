// 兼容性测试：全部 30 课 × Word/PPT/PDF 三种格式
const fs = require('fs');

// ---- 模拟 wx 环境 ----
const captured = {};
function makeCtx() {
  return {
    fillStyle: '', font: '', textBaseline: '',
    fillRect() {},
    createLinearGradient() { return { addColorStop() {} }; },
    fillText() {},
    measureText(s) { return { width: String(s).length * 7 }; }
  };
}
const mockCanvas = { getContext: () => makeCtx(), width: 0, height: 0 };
global.wx = {
  env: { USER_DATA_PATH: '/tmp/wxdata' },
  createSelectorQuery() {
    return { select() { return { fields() { return { exec(cb) { cb([{ node: mockCanvas }]); } }; } }; } };
  },
  canvasToTempFilePath(opts) {
    if (opts && opts.success) opts.success({ tempFilePath: 'mock_' + Math.random() + '.jpg' });
    else if (opts && opts.fail) opts.fail(new Error('no success'));
  },
  getFileSystemManager() {
    return {
      writeFile(opts) {
        captured[opts.filePath] = opts.data;
        if (opts.success) opts.success({});
      },
      readFile(opts) {
        // 返回一个小而合法的 JPEG 占位字节（仅用于 PDF 字节组装测试）
        const jpg = new Uint8Array([0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01, 0xFF, 0xD9]);
        if (opts.success) opts.success({ data: jpg });
        else if (opts.fail) opts.fail(new Error('read fail'));
      }
    };
  }
};

const lessons = require('../data/lessons.js');
const docgen = require('../utils/docgen.js');

function decodeBytes(b) {
  if (b instanceof Uint8Array) return Buffer.from(b);
  if (b instanceof ArrayBuffer) return Buffer.from(new Uint8Array(b));
  return Buffer.from(b);
}

let pass = 0, fail = 0;
const failures = [];

async function run() {
  console.log('总课程数:', lessons.length);
  for (const plan of lessons) {
    for (const fmt of ['word', 'ppt', 'pdf']) {
      try {
        const filePath = await docgen.generateDoc(plan, fmt);
        const bytes = captured[filePath];
        if (!bytes) throw new Error('未捕获到写入数据');
        const buf = decodeBytes(bytes);

        if (fmt === 'word') {
          const html = buf.toString('utf8');
          if (!html.includes('一、教材分析与学情')) throw new Error('Word 缺少精美分节标题');
          // 标题中的 & 等会被 esc() 转义，需用转义后的形式比对
          const escTitle = String(plan.title).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
          if (!html.includes(escTitle)) throw new Error('Word 缺标题(转义后)');
        } else if (fmt === 'ppt') {
          if (buf[0] !== 0x50 || buf[1] !== 0x4B || buf[2] !== 0x03 || buf[3] !== 0x04) throw new Error('PPTX 魔数错误(非合法ZIP)');
          if (!buf.toString('utf8').includes('[Content_Types].xml')) throw new Error('PPTX 缺少内容类型');
        } else if (fmt === 'pdf') {
          const s = buf.toString('latin1');
          if (!s.startsWith('%PDF')) throw new Error('PDF 头错误');
          if (!s.trim().endsWith('%%EOF')) throw new Error('PDF 尾错误');
        }
        pass++;
      } catch (e) {
        fail++;
        failures.push(`[${fmt}] ${plan.id}: ${e.message}`);
      }
    }
  }

  console.log(`\n=== 兼容性测试结果 ===`);
  console.log('通过:', pass, ' 失败:', fail, ' 总计:', pass + fail);
  if (failures.length) {
    console.log('\n失败明细:');
    failures.forEach((f) => console.log('  -', f));
  } else {
    console.log('✅ 全部 30 课 × 3 种格式均生成成功且产物合法！');
  }
}

run().then(() => process.exit(fail ? 1 : 0)).catch((e) => { console.error('FATAL', e); process.exit(2); });
