#!/usr/bin/env python3
# 把真实 listening.wav 嵌入 pilot PPTX 的 slide9（听力训练页），并做完整校验。
import io, os, re, zipfile, shutil
import xml.dom.minidom as M
from xml.parsers.expat import ExpatError
from PIL import Image, ImageDraw

SRC = 'pilot-l-eng-b1-u2-ls.pptx'
TMP = '_with_audio.pptx'
WAV = 'subpackages/eng/images/lessons/l-eng-b1-u2-ls/listening.wav'
MEDIA_DIR = 'subpackages/eng/images/lessons/l-eng-b1-u2-ls'
SLIDE = 9  # 听力训练页

# ---------- 1) 生成扬声器海报图（poster frame）----------
def make_poster(path):
    S = 240
    im = Image.new('RGBA', (S, S), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    # 蓝色圆底
    d.ellipse([20, 20, S-20, S-20], fill=(58, 122, 254, 255))
    # 白色扬声器
    d.polygon([(92, 100), (92, 140), (112, 140), (140, 165), (140, 75), (112, 100)], fill=(255, 255, 255, 255))
    d.rectangle([138, 78, 146, 162], fill=(255, 255, 255, 255))
    # 声波
    d.arc([150, 78, 184, 162], 200, 340, fill=(255, 255, 255, 255), width=7)
    im.convert('RGB').save(path, 'PNG')

poster = io.BytesIO()
p = Image.new('RGBA', (240, 240), (255, 255, 255, 0))
make_poster_pil = p
# 重新生成到内存
import tempfile
poster_path = '_poster_tmp.png'
make_poster(poster_path)
poster_bytes = open(poster_path, 'rb').read()
os.remove(poster_path)

wav_bytes = open(WAV, 'rb').read()

# ---------- 2) 读原包，注入部件 ----------
z = zipfile.ZipFile(SRC)
parts = {n: z.read(n) for n in z.namelist()}

# Content_Types
ct = parts['[Content_Types].xml'].decode('utf8')
if 'Extension="wav"' not in ct:
    ct = ct.replace('</Types>', '  <Default Extension="wav" ContentType="audio/wav"/>\n</Types>')
    parts['[Content_Types].xml'] = ct.encode('utf8')
if 'Extension="png"' not in ct:
    ct = ct.replace('</Types>', '  <Default Extension="png" ContentType="image/png"/>\n</Types>')
    parts['[Content_Types].xml'] = ct.encode('utf8')

# 媒体部件
parts['ppt/media/audio1.wav'] = wav_bytes
parts['ppt/media/poster_s9.png'] = poster_bytes

# slide9 rels：加 audio + poster image 两条关系
rels_name = f'ppt/slides/_rels/slide{SLIDE}.xml.rels'
rels = parts[rels_name].decode('utf8')
# 找最大 rId
ids = [int(x) for x in re.findall(r'Id="rId(\d+)"', rels)]
maxid = max(ids) if ids else 1
audio_rid = f'rId{maxid+1}'
poster_rid = f'rId{maxid+2}'
new_rels = (f'  <Relationship Id="{audio_rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/audio" Target="../media/audio1.wav"/>\n'
            f'  <Relationship Id="{poster_rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/poster_s9.png"/>\n')
rels = rels.replace('</Relationships>', new_rels + '</Relationships>')
parts[rels_name] = rels.encode('utf8')

# slide9 xml：插入 <p:audio> 形状（右下角，约 0.9x0.9 inch）
EMU = 914400
audio_xml = f'''<p:audio xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:nvPicPr><p:cNvPr id="999" name="Audio 1" descr=""/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr><a:audioFile r:link="{audio_rid}"/></p:nvPr></p:nvPicPr><p:blipFill><a:blip r:embed="{poster_rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="{int(11.9*EMU)}" y="{int(6.3*EMU)}"/><a:ext cx="{int(0.9*EMU)}" cy="{int(0.9*EMU)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr><p:timing><p:tnLst><p:par><p:cTn id="9998" fill="hold"><p:stCondLst><p:cond evt="onBegin" delay="0"/></p:stCondLst><p:childTnLst><p:audio><p:cMediaNode vol="100000" mute="0"><p:embed><a:audioFile r:link="{audio_rid}"/></p:embed></p:cMediaNode></p:audio></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing></p:audio>'''

slide_name = f'ppt/slides/slide{SLIDE}.xml'
slide = parts[slide_name].decode('utf8')
slide = slide.replace('</p:spTree>', audio_xml + '</p:spTree>')
parts[slide_name] = slide.encode('utf8')

# 写新包
with zipfile.ZipFile(TMP, 'w', zipfile.ZIP_DEFLATED) as zout:
    for n, b in parts.items():
        zout.writestr(n, b)

# ---------- 3) 校验 ----------
print('== 校验 ==')
z2 = zipfile.ZipFile(TMP)
print('zip 完整性:', 'OK' if z2.testzip() is None else 'BAD')
bad = []
for n in z2.namelist():
    if n.endswith('.xml') or n.endswith('.rels'):
        try:
            M.parseString(z2.read(n))
        except ExpatError as e:
            bad.append((n, str(e)))
print('XML 非法数:', len(bad))
for n, e in bad:
    print('  ✗', n, e)
print('  ✓ 全部良构' if not bad else '  ✗ 有错')
# slide9 关系闭环
sx = z2.read(f'ppt/slides/slide{SLIDE}.xml').decode('utf8')
rx = z2.read(f'ppt/slides/_rels/slide{SLIDE}.xml.rels').decode('utf8')
emb = set(re.findall(r'r:embed="([^"]+)"', sx)) | set(re.findall(r'r:link="([^"]+)"', sx))
relids = set(re.findall(r'Id="([^"]+)"', rx))
print('slide9 引用:', emb, '| 定义:', relids, '| 缺:', emb - relids)
print('slide9 含 <p:audio>:', '<p:audio>' in sx)
print('媒体部件:', [n for n in z2.namelist() if n.startswith('ppt/media/')])

# python-pptx 真机加载
from pptx import Presentation
prs = Presentation(TMP)
print('python-pptx 加载成功, 幻灯片数:', len(prs.slides))

# 覆盖原名
shutil.move(TMP, SRC)
print('已写回', SRC, os.path.getsize(SRC)//1024, 'KB')
