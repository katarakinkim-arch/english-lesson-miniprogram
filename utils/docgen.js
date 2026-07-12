// utils/docgen.js
// 端上文件生成：Word(.doc) / PPT(.pptx) / PDF —— 无需服务器
// 依赖：wx.* 小程序 API；FileSystemManager 写入临时目录后用 wx.openDocument 打开

/* ============ 工具 ============ */
function utf8Encode(str) {
  const out = [];
  for (let i = 0; i < str.length; i++) {
    let c = str.charCodeAt(i);
    if (c < 0x80) out.push(c);
    else if (c < 0x800) out.push(0xc0 | (c >> 6), 0x80 | (c & 0x3f));
    else if (c >= 0xd800 && c <= 0xdbff) {
      const c2 = str.charCodeAt(++i);
      c = 0x10000 + ((c & 0x3ff) << 10) + (c2 & 0x3ff);
      out.push(0xf0 | (c >> 18), 0x80 | ((c >> 12) & 0x3f), 0x80 | ((c >> 6) & 0x3f), 0x80 | (c & 0x3f));
    } else out.push(0xe0 | (c >> 12), 0x80 | ((c >> 6) & 0x3f), 0x80 | (c & 0x3f));
  }
  return new Uint8Array(out);
}

function esc(s) {
  if (!s) return '';
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function safeName(id) {
  return String(id || 'lesson').replace(/[\\/:*?"<>|]/g, '_');
}

/* ============ Word (.doc HTML) ============ */
function buildWordHtml(plan) {
  let h = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">';
  h += '<head><meta charset="utf-8"><title>' + esc(plan.title) + '</title>';
  h += '<style>body{font-family:"Microsoft YaHei","PingFang SC",sans-serif;color:#1a1a2e;line-height:1.8;}';
  h += 'h1{color:#1a365d;font-size:22pt;} h2{color:#1a365d;border-bottom:2px solid #1a365d;font-size:15pt;margin-top:18pt;}';
  h += 'h3{color:#2c5282;font-size:13pt;} .meta{color:#666;font-size:11pt;margin-bottom:10pt;}';
  h += '.section{margin:8pt 0;} pre{font-family:Consolas,monospace;background:#f0f7eb;padding:8pt;white-space:pre-wrap;}</style></head><body>';
  h += '<h1>' + esc(plan.title) + '</h1>';
  h += '<div class="meta">' + esc(plan.grade) + ' · ' + esc(plan.subject) + ' · ' + esc(plan.textbook || '') +
       ' · 第' + (plan.unitNumber || 1) + '单元 · ' + esc(plan.lessonTypeName || '') + ' · ' + (plan.duration || 45) + '分钟</div>';
  if (plan.overview) h += '<h2>【教案概述】</h2><div class="section">' + esc(plan.overview) + '</div>';
  if (plan.objectives && plan.objectives.length) {
    h += '<h2>【教学目标】</h2>';
    plan.objectives.forEach((o, i) => { h += '<div>' + (i + 1) + '. ' + esc(o) + '</div>'; });
  }
  if (plan.keyPoints) h += '<h2>【教学重点】</h2><div class="section">' + esc(plan.keyPoints) + '</div>';
  if (plan.difficulties) h += '<h2>【教学难点】</h2><div class="section">' + esc(plan.difficulties) + '</div>';
  if (plan.preparation) h += '<h2>【课前准备】</h2><div class="section">' + esc(plan.preparation) + '</div>';
  if (plan.process && plan.process.length) {
    h += '<h2>【教学过程】</h2>';
    plan.process.forEach((s, i) => {
      h += '<h3>步骤' + (i + 1) + '：' + esc(s.step) + '（' + s.time + '分钟）</h3>';
      h += '<div class="section">' + esc(s.content) + '</div>';
    });
  }
  if (plan.blackboard) h += '<h2>【板书设计】</h2><pre>' + esc(plan.blackboard) + '</pre>';
  if (plan.exercises) h += '<h2>【课后练习】</h2><div class="section">' + esc(plan.exercises) + '</div>';
  if (plan.reflection) h += '<h2>【教学反思】</h2><div class="section">' + esc(plan.reflection) + '</div>';
  h += '</body></html>';
  return h;
}

/* ============ PPT (.pptx) ============ */
function crc32Table() {
  const t = new Uint32Array(256);
  for (let i = 0; i < 256; i++) { let c = i; for (let j = 0; j < 8; j++) { c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1); } t[i] = c >>> 0; }
  return t;
}
const CRC = crc32Table();
function crc32(data) { let crc = 0xFFFFFFFF; for (let k = 0; k < data.length; k++) { crc = (CRC[(crc ^ data[k]) & 0xFF] ^ (crc >>> 8)) >>> 0; } return (crc ^ 0xFFFFFFFF) >>> 0; }

function createZip(files) {
  function dos(d) { const time = (d.getSeconds() >> 1) | (d.getMinutes() << 5) | (d.getHours() << 11); const date = d.getDate() | ((d.getMonth() + 1) << 5) | ((d.getFullYear() - 1980) << 9); return { time, date }; }
  const now = dos(new Date());
  const chunks = [], central = []; let offset = 0;
  for (const file of files) {
    const nameBytes = utf8Encode(file.name);
    const data = file.data;
    const c = crc32(data);
    const lh = new Uint8Array(30 + nameBytes.length);
    const dv = new DataView(lh.buffer);
    dv.setUint32(0, 0x04034b50, true); dv.setUint16(4, 20, true); dv.setUint16(6, 0, true); dv.setUint16(8, 0, true);
    dv.setUint16(10, now.time, true); dv.setUint16(12, now.date, true);
    dv.setUint32(14, c, true); dv.setUint32(18, data.length, true); dv.setUint32(22, data.length, true);
    dv.setUint16(26, nameBytes.length, true); dv.setUint16(28, 0, true);
    lh.set(nameBytes, 30);
    chunks.push(lh); chunks.push(data);
    const cd = new Uint8Array(46 + nameBytes.length);
    const cdv = new DataView(cd.buffer);
    cdv.setUint32(0, 0x02014b50, true); cdv.setUint16(4, 20, true); cdv.setUint16(6, 20, true); cdv.setUint16(8, 0, true); cdv.setUint16(10, 0, true);
    cdv.setUint16(12, now.time, true); cdv.setUint16(14, now.date, true); cdv.setUint32(16, c, true);
    cdv.setUint32(20, data.length, true); cdv.setUint32(24, data.length, true);
    cdv.setUint16(28, nameBytes.length, true); cdv.setUint16(30, 0, true); cdv.setUint16(32, 0, true); cdv.setUint16(34, 0, true); cdv.setUint16(36, 0, true); cdv.setUint32(38, 0, true); cdv.setUint32(42, offset, true);
    cd.set(nameBytes, 46);
    central.push(cd);
    offset += lh.length + data.length;
  }
  let cdSize = 0; for (const cd of central) cdSize += cd.length;
  const eocd = new Uint8Array(22);
  const edv = new DataView(eocd.buffer);
  edv.setUint32(0, 0x06054b50, true); edv.setUint16(4, 0, true); edv.setUint16(6, 0, true); edv.setUint16(8, files.length, true); edv.setUint16(10, files.length, true); edv.setUint32(12, cdSize, true); edv.setUint32(16, offset, true); edv.setUint16(20, 0, true);
  let total = 0; for (const c of chunks) total += c.length; total += cdSize + 22;
  const result = new Uint8Array(total); let pos = 0;
  for (const c of chunks) { result.set(c, pos); pos += c.length; }
  for (const c of central) { result.set(c, pos); pos += c.length; }
  result.set(eocd, pos);
  return result;
}

function splitParas(text) { return String(text || '').split(/\r\n|\n|\r/).filter(l => l.trim() !== ''); }
function buildParas(text, sz) {
  let xml = '';
  for (const line of splitParas(text)) xml += '<a:p><a:r><a:rPr lang="zh-CN" sz="' + sz + '"/><a:t>' + esc(line) + '</a:t></a:r><a:endParaRPr lang="zh-CN"/></a:p>';
  return xml;
}

function buildPPTX(plan) {
  const slides = [];
  slides.push({ title: plan.title, content: (plan.grade || '') + ' · ' + (plan.subject || '') + ' · ' + (plan.textbook || '') + '\n第' + (plan.unitNumber || 1) + '单元 ' + (plan.unitTitle || '') + '\n' + (plan.lessonTypeName || '') + ' · ' + (plan.duration || 45) + '分钟', isTitle: true });
  if (plan.overview) slides.push({ title: '教案概述', content: plan.overview });
  if (plan.objectives && plan.objectives.length) { let t = ''; plan.objectives.forEach((o, i) => { t += (i + 1) + '. ' + o + '\n'; }); slides.push({ title: '教学目标', content: t }); }
  if (plan.keyPoints) slides.push({ title: '教学重点', content: plan.keyPoints });
  if (plan.difficulties) slides.push({ title: '教学难点', content: plan.difficulties });
  if (plan.preparation) slides.push({ title: '课前准备', content: plan.preparation });
  if (plan.process && plan.process.length) plan.process.forEach((s, i) => slides.push({ title: '步骤' + (i + 1) + '：' + s.step + '（' + s.time + '分钟）', content: s.content }));
  if (plan.blackboard) slides.push({ title: '板书设计', content: plan.blackboard });
  if (plan.exercises) slides.push({ title: '课后练习', content: plan.exercises });
  if (plan.reflection) slides.push({ title: '教学反思', content: plan.reflection });

  const files = [];
  const nowDate = new Date().toISOString().replace(/\.\d+Z$/, 'Z');
  const title = plan.title || '教案';

  let ct = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">';
  ct += '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>';
  ct += '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>';
  ct += '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>';
  ct += '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>';
  ct += '<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>';
  ct += '<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>';
  ct += '<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>';
  ct += '<Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presProps+xml"/>';
  ct += '<Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.viewProps+xml"/>';
  ct += '<Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>';
  for (let i = 0; i < slides.length; i++) ct += '<Override PartName="/ppt/slides/slide' + (i + 1) + '.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>';
  ct += '</Types>';
  files.push({ name: '[Content_Types].xml', data: utf8Encode(ct) });

  files.push({ name: '_rels/.rels', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>') });

  files.push({ name: 'docProps/app.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Lesson Plan Generator</Application><Slides>' + slides.length + '</Slides><AppVersion>16.0000</AppVersion></Properties>') });
  files.push({ name: 'docProps/core.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>' + esc(title) + '</dc:title><dc:creator>LessonPlan</dc:creator><dcterms:created xsi:type="dcterms:W3CDTF">' + nowDate + '</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">' + nowDate + '</dcterms:modified></cp:coreProperties>') });

  let pres = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentation xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><p:sldIdLst>';
  for (let i = 0; i < slides.length; i++) pres += '<p:sldId id="' + (256 + i) + '" r:id="rId' + (i + 2) + '"/>';
  pres += '</p:sldIdLst><p:sldSz cx="9144000" cy="6858000" type="screen4x3"/><p:notesSz cx="6858000" cy="9144000"/></p:presentation>';
  files.push({ name: 'ppt/presentation.xml', data: utf8Encode(pres) });

  let presRels = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>';
  for (let i = 0; i < slides.length; i++) presRels += '<Relationship Id="rId' + (i + 2) + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide' + (i + 1) + '.xml"/>';
  let nr = slides.length + 2;
  presRels += '<Relationship Id="rId' + nr + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>'; nr++;
  presRels += '<Relationship Id="rId' + nr + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/presProps" Target="presProps.xml"/>'; nr++;
  presRels += '<Relationship Id="rId' + nr + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps" Target="viewProps.xml"/>'; nr++;
  presRels += '<Relationship Id="rId' + nr + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableStyles" Target="tableStyles.xml"/>';
  presRels += '</Relationships>';
  files.push({ name: 'ppt/_rels/presentation.xml.rels', data: utf8Encode(presRels) });

  files.push({ name: 'ppt/slideMasters/slideMaster1.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldMaster xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><p:cSld><p:bg><p:bgRef idx="1001"><a:schemeClr val="bg1"/></p:bgRef></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/><p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst><p:txStyles><p:titleStyle><a:lvl1pPr algn="l"><a:defRPr sz="4400" kern="1200"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="+mj-lt"/><a:ea typeface="+mj-ea"/></a:defRPr></a:lvl1pPr></p:titleStyle><p:bodyStyle><a:lvl1pPr marL="342900" indent="-342900"><a:defRPr sz="2800" kern="1200"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="+mn-lt"/><a:ea typeface="+mn-ea"/></a:defRPr></a:lvl1pPr></p:bodyStyle><p:otherStyle><a:lvl1pPr marL="342900" indent="-342900"><a:defRPr sz="2400" kern="1200"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="+mn-lt"/><a:ea typeface="+mn-ea"/></a:defRPr></a:lvl1pPr></p:otherStyle></p:txStyles></p:sldMaster>') });
  files.push({ name: 'ppt/slideMasters/_rels/slideMaster1.xml.rels', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/></Relationships>') });
  files.push({ name: 'ppt/slideLayouts/slideLayout1.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldLayout xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>') });
  files.push({ name: 'ppt/slideLayouts/_rels/slideLayout1.xml.rels', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>') });
  files.push({ name: 'ppt/theme/theme1.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme"><a:themeElements><a:clrScheme name="Office"><a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1><a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="44546A"/></a:dk2><a:lt2><a:srgbClr val="E7E6E6"/></a:lt2><a:accent1><a:srgbClr val="4472C4"/></a:accent1><a:accent2><a:srgbClr val="ED7D31"/></a:accent2><a:accent3><a:srgbClr val="A5A5A5"/></a:accent3><a:accent4><a:srgbClr val="FFC000"/></a:accent4><a:accent5><a:srgbClr val="5B9BD5"/></a:accent5><a:accent6><a:srgbClr val="70AD47"/></a:accent6><a:hlink><a:srgbClr val="0563C1"/></a:hlink><a:folHlink><a:srgbClr val="954F72"/></a:folHlink></a:clrScheme><a:fontScheme name="Office"><a:majorFont><a:latin typeface="Calibri Light"/><a:ea typeface=""/></a:majorFont><a:minorFont><a:latin typeface="Calibri"/><a:ea typeface=""/></a:minorFont></a:fontScheme><a:fmtScheme name="Office"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:gradFill rotWithShape="1"><a:gsLst><a:gs pos="0"><a:schemeClr val="phClr"><a:lumMod val="110000"/><a:satMod val="105000"/><a:tint val="67000"/></a:schemeClr></a:gs><a:gs pos="50000"><a:schemeClr val="phClr"><a:lumMod val="105000"/><a:satMod val="103000"/><a:tint val="73000"/></a:schemeClr></a:gs><a:gs pos="100000"><a:schemeClr val="phClr"><a:lumMod val="105000"/><a:satMod val="109000"/><a:tint val="81000"/></a:schemeClr></a:gs></a:gsLst><a:lin ang="5400000" scaled="0"/></a:gradFill><a:gradFill rotWithShape="1"><a:gsLst><a:gs pos="0"><a:schemeClr val="phClr"><a:satMod val="103000"/><a:lumMod val="102000"/><a:tint val="94000"/></a:schemeClr></a:gs><a:gs pos="50000"><a:schemeClr val="phClr"><a:satMod val="110000"/><a:lumMod val="100000"/><a:shade val="100000"/></a:schemeClr></a:gs><a:gs pos="100000"><a:schemeClr val="phClr"><a:lumMod val="99000"/><a:satMod val="120000"/><a:shade val="78000"/></a:schemeClr></a:gs></a:gsLst><a:lin ang="5400000" scaled="0"/></a:gradFill></a:fillStyleLst><a:lnStyleLst><a:ln w="6350" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/><a:miter lim="800000"/></a:ln><a:ln w="12700" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/><a:miter lim="800000"/></a:ln><a:ln w="19050" cap="flat" cmpd="sng" algn="ctr"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:prstDash val="solid"/><a:miter lim="800000"/></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"><a:tint val="95000"/><a:satMod val="170000"/></a:schemeClr></a:solidFill><a:gradFill rotWithShape="1"><a:gsLst><a:gs pos="0"><a:schemeClr val="phClr"><a:tint val="93000"/><a:satMod val="150000"/><a:shade val="98000"/><a:lumMod val="102000"/></a:schemeClr></a:gs><a:gs pos="50000"><a:schemeClr val="phClr"><a:tint val="98000"/><a:satMod val="130000"/><a:shade val="90000"/><a:lumMod val="103000"/></a:schemeClr></a:gs><a:gs pos="100000"><a:schemeClr val="phClr"><a:shade val="63000"/><a:satMod val="120000"/></a:schemeClr></a:gs></a:gsLst><a:lin ang="5400000" scaled="0"/></a:gradFill></a:bgFillStyleLst></a:fmtScheme></a:themeElements><a:objectDefaults/><a:extraClrSchemeLst/></a:theme>') });
  files.push({ name: 'ppt/presProps.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentationPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>') });
  files.push({ name: 'ppt/viewProps.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:viewPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:normalViewPr><p:restoredLeft sz="15620"/><p:restoredTop sz="94660" autoAdjust="0"/></p:normalViewPr><p:slideViewPr><p:cSldViewPr><p:cViewPr varScale="1"><p:scale><a:sx n="64" d="100"/><a:sy n="64" d="100"/></p:scale><p:origin x="-1392" y="-96"/></p:cViewPr><p:guideLst/></p:cSldViewPr></p:slideViewPr></p:viewPr>') });
  files.push({ name: 'ppt/tableStyles.xml', data: utf8Encode('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:tblStyleLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"/>') });

  const slideLayoutRel = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>';
  for (let i = 0; i < slides.length; i++) {
    const s = slides[i];
    const titleSize = s.isTitle ? '4400' : '3600';
    const titleXml = buildParas(s.title, titleSize);
    const contentXml = buildParas(s.content, '1800');
    const slideXml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr><p:sp><p:nvSpPr><p:cNvPr id="2" name="Title"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="457200" y="274638"/><a:ext cx="8230125" cy="1143000"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" rtlCol="0"><a:spAutoFit/></a:bodyPr><a:lstStyle/>' + titleXml + '</p:txBody></p:sp><p:sp><p:nvSpPr><p:cNvPr id="3" name="Content"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="457200" y="1600200"/><a:ext cx="8230125" cy="4658375"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" rtlCol="0"><a:spAutoFit/></a:bodyPr><a:lstStyle/>' + contentXml + '</p:txBody></p:sp></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>';
    files.push({ name: 'ppt/slides/slide' + (i + 1) + '.xml', data: utf8Encode(slideXml) });
    files.push({ name: 'ppt/slides/_rels/slide' + (i + 1) + '.xml.rels', data: utf8Encode(slideLayoutRel) });
  }

  return createZip(files);
}

/* ============ PDF（canvas 绘制图片后嵌入，真 PDF 支持中文） ============ */
function buildPDF(plan) {
  return new Promise((resolve, reject) => {
    wx.createSelectorQuery().select('#pdfCanvas').fields({ node: true }).exec((res) => {
      if (!res || !res[0] || !res[0].node) { reject(new Error('pdfCanvas not found')); return; }
      const canvas = res[0].node;
      const ctx = canvas.getContext('2d');
      const W = 595, H = 842;
      canvas.width = W; canvas.height = H;

      // 收集绘制行
      const lines = [];
      const pushHead = (t) => lines.push({ type: 'head', text: t });
      const pushBody = (t) => {
        const maxW = W - 80;
        ctx.font = '13px sans-serif';
        let cur = '';
        const chars = String(t).split('');
        for (const ch of chars) {
          if (ctx.measureText(cur + ch).width > maxW && cur) { lines.push({ type: 'body', text: cur }); cur = ch; }
          else cur += ch;
        }
        if (cur) lines.push({ type: 'body', text: cur });
      };
      lines.push({ type: 'title', text: plan.title });
      if (plan.overview) { pushHead('教案概述'); pushBody(plan.overview); }
      if (plan.objectives && plan.objectives.length) { pushHead('教学目标'); plan.objectives.forEach((o, i) => pushBody((i + 1) + '. ' + o)); }
      if (plan.keyPoints) { pushHead('教学重点'); pushBody(plan.keyPoints); }
      if (plan.difficulties) { pushHead('教学难点'); pushBody(plan.difficulties); }
      if (plan.preparation) { pushHead('课前准备'); pushBody(plan.preparation); }
      if (plan.process && plan.process.length) { pushHead('教学过程'); plan.process.forEach((s, i) => { pushHead('步骤' + (i + 1) + '：' + s.step + '（' + s.time + '分钟）'); pushBody(s.content); }); }
      if (plan.blackboard) { pushHead('板书设计'); pushBody(plan.blackboard); }
      if (plan.exercises) { pushHead('课后练习'); pushBody(plan.exercises); }
      if (plan.reflection) { pushHead('教学反思'); pushBody(plan.reflection); }

      const lineH = { title: 32, head: 26, body: 19 };
      const MARGIN = 44;
      const pages = []; let cur = []; let y = 0;
      for (const ln of lines) {
        const lh = lineH[ln.type] || 19;
        if (y + lh > H - MARGIN && cur.length) { pages.push(cur); cur = []; y = 0; }
        cur.push(ln); y += lh;
      }
      if (cur.length) pages.push(cur);

      const drawPage = (pageLines) => new Promise((res2, rej2) => {
        ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, W, H);
        let yy = MARGIN; ctx.textBaseline = 'top';
        for (const ln of pageLines) {
          if (ln.type === 'title') { ctx.fillStyle = '#1a365d'; ctx.font = 'bold 20px sans-serif'; ctx.fillText(ln.text, MARGIN, yy); yy += 32; }
          else if (ln.type === 'head') { ctx.fillStyle = '#1a365d'; ctx.font = 'bold 15px sans-serif'; ctx.fillText(ln.text, MARGIN, yy); yy += 26; }
          else { ctx.fillStyle = '#333333'; ctx.font = '13px sans-serif'; ctx.fillText(ln.text, MARGIN, yy); yy += 19; }
        }
        wx.canvasToTempFilePath({ canvas, fileType: 'jpg', quality: 0.92, success: (r) => res2(r.tempFilePath), fail: rej2 });
      });

      Promise.all(pages.map(drawPage)).then((paths) => {
        const reads = paths.map((p) => new Promise((r, j) => {
          wx.getFileSystemManager().readFile({ filePath: p, success: (d) => r(new Uint8Array(d.data)), fail: j });
        }));
        Promise.all(reads).then((jpegs) => {
          try { resolve(buildPdfFromJpegs(W, H, jpegs)); }
          catch (e) { reject(e); }
        }).catch(reject);
      }).catch(reject);
    });
  });
}

function pad10(n) { let s = String(n); while (s.length < 10) s = '0' + s; return s; }
function concatBytes(a, b) {
  const out = new Uint8Array(a.length + b.length);
  out.set(a, 0); out.set(b, a.length);
  return out;
}

function buildPdfFromJpegs(W, H, jpegs) {
  const enc = (s) => utf8Encode(s);
  const N = jpegs.length;
  const totalObjs = 2 + N * 3;
  const stringObjs = {};
  stringObjs[1] = '<< /Type /Catalog /Pages 2 0 R >>';
  const kids = [];
  for (let i = 0; i < N; i++) kids.push((3 + i * 3) + ' 0 R');
  stringObjs[2] = '<< /Type /Pages /Kids [' + kids.join(' ') + '] /Count ' + N + ' >>';
  for (let i = 0; i < N; i++) {
    const pn = 3 + i * 3, cn = pn + 1, im = pn + 2;
    stringObjs[pn] = '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ' + W + ' ' + H + '] /Resources << /XObject << /Im0 ' + im + ' 0 R >> >> /Contents ' + cn + ' 0 R >>';
    stringObjs[cn] = 'q ' + W + ' 0 0 ' + H + ' 0 0 cm /Im0 Do Q';
  }
  const offsets = new Array(totalObjs + 1).fill(0);
  const parts = [];
  let pos = 0;
  const push = (bytes) => { parts.push(bytes); pos += bytes.length; };
  push(enc('%PDF-1.4\n%\xE2\xE3\xCF\xD3\n'));
  for (let o = 1; o <= totalObjs; o++) {
    offsets[o] = pos;
    if (o >= 3 && (o - 3) % 3 === 2) {
      const i = Math.floor((o - 3) / 3);
      const jpg = jpegs[i];
      const head = enc(o + ' 0 obj\n<< /Type /XObject /Subtype /Image /Width ' + W + ' /Height ' + H + ' /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ' + jpg.length + ' >>\nstream\n');
      push(head); push(jpg); push(enc('\nendstream\nendobj\n'));
    } else {
      push(enc(o + ' 0 obj\n' + stringObjs[o] + '\nendobj\n'));
    }
  }
  const xrefStart = pos;
  let xref = enc('xref\n0 ' + (totalObjs + 1) + '\n0000000000 65535 f \n');
  for (let o = 1; o <= totalObjs; o++) xref = concatBytes(xref, enc(pad10(offsets[o]) + ' 00000 n \n'));
  push(xref);
  push(enc('trailer\n<< /Size ' + (totalObjs + 1) + ' /Root 1 0 R >>\nstartxref\n' + xrefStart + '\n%%EOF'));

  let total = 0; for (const p of parts) total += p.length;
  const result = new Uint8Array(total); let pp = 0;
  for (const p of parts) { result.set(p, pp); pp += p.length; }
  return result;
}

/* ============ 统一入口 ============ */
function writeAndOpen(data, name) {
  return new Promise((resolve, reject) => {
    const filePath = wx.env.USER_DATA_PATH + '/' + name;
    wx.getFileSystemManager().writeFile({
      filePath: filePath,
      data: data,
      success: () => resolve(filePath),
      fail: (e) => reject(e)
    });
  });
}

function generateDoc(plan, fmt) {
  if (fmt === 'word') {
    return writeAndOpen(buildWordHtml(plan), safeName(plan.id) + '.doc');
  }
  if (fmt === 'ppt') {
    const ab = buildPPTX(plan);
    return writeAndOpen(ab.buffer, safeName(plan.id) + '.pptx');
  }
  if (fmt === 'pdf') {
    return buildPDF(plan).then((ab) => writeAndOpen(ab.buffer, safeName(plan.id) + '.pdf'));
  }
  return Promise.reject(new Error('unknown format: ' + fmt));
}

module.exports = { generateDoc };
