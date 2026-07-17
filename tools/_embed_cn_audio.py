#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把占位朗诵音频嵌入语文 PPTX 的 slide 7（Step 2 诵读感知页）。
参照英语 pilot _embed_audio.py 同构：poster frame + <p:audio> + Content_Types + rels。
"""
import io, os, re, zipfile, shutil
import xml.dom.minidom as M
from xml.parsers.expat import ExpatError
from PIL import Image, ImageDraw

SRC = 'l-cn-bs-u1-1.pptx'
TMP = '_cn_with_audio.pptx'
WAV = os.path.join('subpackages', 'cn', 'images', 'lessons', 'l-cn-bs-u1-1', 'recitation.wav')
SLIDE = 7  # Step 2 诵读感知

# ---- poster frame (扬声器图标) ----
def make_poster(path):
    S = 240
    im = Image.new('RGBA', (S, S), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([20, 20, S-20, S-20], fill=(194, 112, 61, 255))  # 陶土橙圆底
    d.polygon([(92, 100), (92, 140), (112, 140), (140, 165), (140, 75), (112, 100)],
              fill=(255, 255, 255, 255))
    d.rectangle([138, 78, 146, 162], fill=(255, 255, 255, 255))
    d.arc([150, 78, 184, 162], 200, 340, fill=(255, 255, 255, 255), width=7)
    im.convert('RGB').save(path, 'PNG')

poster_path = '_poster_cn.png'
make_poster(poster_path)
poster_bytes = open(poster_path, 'rb').read()
os.remove(poster_path)

wav_bytes = open(WAV, 'rb').read()

# ---- 注入部件到 PPTX 包 ----
z = zipfile.ZipFile(SRC)
parts = {n: z.read(n) for n in z.namelist()}

ct = parts['[Content_Types].xml'].decode('utf8')
if 'Extension="wav"' not in ct:
    ct = ct.replace('</Types>', '  <Default Extension="wav" ContentType="audio/wav"/>\n</Types>')
if 'Extension="png"' not in ct:
    ct = ct.replace('</Types>', '  <Default Extension="png" ContentType="image/png"/>\n</Types>')
parts['[Content_Types].xml'] = ct.encode('utf8')

parts['ppt/media/recitation.wav'] = wav_bytes
parts['ppt/media/poster_s7.png'] = poster_bytes

rels_name = f'ppt/slides/_rels/slide{SLIDE}.xml.rels'
rels = parts[rels_name].decode('utf8')
ids = [int(x) for x in re.findall(r'Id="rId(\d+)"', rels)]
maxid = max(ids) if ids else 1
audio_rid = f'rId{maxid+1}'
poster_rid = f'rId{maxid+2}'
new_rels = (
    f'  <Relationship Id="{audio_rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/audio" Target="../media/recitation.wav"/>\n'
    f'  <Relationship Id="{poster_rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/poster_s7.png"/>\n'
)
rels = re.sub('</Relationships>', new_rels + '</Relationships>', rels)
parts[rels_name] = rels.encode('utf8')

EMU = 914400
audio_xml = f'''<p:audio xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:nvPicPr><p:cNvPr id="998" name="朗诵音频" descr="沁园春·长沙 名家朗诵"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr><a:audioFile r:link="{audio_rid}"/></p:nvPr></p:nvPicPr><p:blipFill><a:blip r:embed="{poster_rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="{int(11.9*EMU)}" y="{int(6.3*EMU)}"/><a:ext cx="{int(0.9*EMU)}" cy="{int(0.9*EMU)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr><p:timing><p:tnLst><p:par><p:cTn id="9997" fill="hold"><p:stCondLst><p:cond evt="onBegin" delay="0"/></p:stCondLst><p:childTnLst><p:audio><p:cMediaNode vol="100000" mute="0"><p:embed><a:audioFile r:link="{audio_rid}"/></p:embed></p:cMediaNode></p:audio></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing></p:audio>'''

slide_name = f'ppt/slides/slide{SLIDE}.xml'
parts[slide_name] = parts[slide_name].decode('utf8').replace('</p:spTree>', audio_xml + '</p:spTree>').encode('utf8')

with zipfile.ZipFile(TMP, 'w', zipfile.ZIP_DEFLATED) as zout:
    for n, b in parts.items():
        zout.writestr(n, b)

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
    print('  X', n, e)
print('  全部良构' if not bad else '')
sx = z2.read(f'ppt/slides/slide{SLIDE}.xml').decode('utf8')
rx = z2.read(f'ppt/slides/_rels/slide{SLIDE}.xml.rels').decode('utf8')
emb = set(re.findall(r'r:embed="([^"]+)"', sx)) | set(re.findall(r'r:link="([^"]+)"', sx))
relids = set(re.findall(r'Id="([^"]+)"', rx))
print(f'slide{SLIDE} 引用:', emb, '| 定义:', relids, '| 缺:', emb - relids)
print(f'slide{SLIDE} 含 <p:audio>:', '<p:audio>' in sx)
print('媒体:', [n for n in z2.namelist() if n.startswith('ppt/media/')])

from pptx import Presentation
prs = Presentation(TMP)
print('python-pptx 加载成功, 幻灯片:', len(prs.slides))

shutil.move(TMP, SRC)
print('已写回', SRC, os.path.getsize(SRC)//1024, 'KB')
