# -*- coding: utf-8 -*-
"""《峨日朵雪峰之侧 / 致云雀》群文 真实照片下载（Wikimedia Commons API + curl）。"""
import os, json, subprocess, time
from urllib.parse import urlencode
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'preview_v7', '_eduo_zhiyun_photos')
os.makedirs(OUT, exist_ok=True)
UA = 'WorkBuddyLessonBot/1.0 (educational use; python-requests)'
REFERER = 'https://commons.wikimedia.org/'

def api(params, tries=4):
    url = 'https://commons.wikimedia.org/w/api.php?' + urlencode(params)
    for i in range(tries):
        r = subprocess.run(['curl','-sL','-H',f'User-Agent: {UA}','-H',f'Referer: {REFERER}',url],
                           capture_output=True, text=True)
        try:
            d = json.loads(r.stdout)
            if 'error' not in d:
                return d
        except Exception:
            pass
        print('  [限速/重试] 稍候...'); time.sleep(6 + i*4)
    return {}

def search_files(term, limit=12):
    d = api({'action':'query','list':'search','srsearch':term,'srnamespace':6,'srlimit':limit,'format':'json'})
    return [h['title'] for h in d.get('query',{}).get('search',[])]
  # 取文件 title 列表

def get_thumb(title, width=1200):
    d = api({'action':'query','prop':'imageinfo','titles':title,'iiprop':'url|mime',
             'iiurlwidth':width,'format':'json'})
    for p in d.get('query',{}).get('pages',{}).values():
        ii = p.get('imageinfo', [])
        if ii:
            info = ii[0]
            if info.get('mime','').startswith('image/') and 'svg' not in info.get('mime',''):
                return info.get('thumburl') or info.get('url')
    return None

def download(url, dest):
    r = subprocess.run(['curl','-sL','-H',f'User-Agent: {UA}','-H',f'Referer: {REFERER}',
                        '-o',dest,url,'-w','%{http_code}'], capture_output=True, text=True)
    return r.stdout.strip() == '200' and os.path.getsize(dest) > 5000

def fit_crop(src, dest, tw, th):
    im = Image.open(src).convert('RGB')
    iw, ih = im.size
    if max(iw,ih) > 1600:
        r = 1600.0/max(iw,ih); im = im.resize((int(iw*r),int(ih*r)), Image.LANCZOS)
        iw, ih = im.size
    target_ratio = tw/th; img_ratio = iw/ih
    if img_ratio > target_ratio:
        new_w = int(ih*target_ratio); left = (iw-new_w)//2
        im = im.crop((left,0,left+new_w,ih))
    else:
        new_h = int(iw/target_ratio); top = (ih-new_h)//2
        im = im.crop((0,top,iw,top+new_h))
    im = im.resize((tw,th), Image.LANCZOS)
    im.save(dest,'JPEG',quality=86)

# 关键词 → 文件名 → 目标尺寸 → 用途说明
TARGETS = [
    ('snow covered mountain peak',   'real_snowpeak.jpg', 800, 800, '峨日朵雪峰'),
    ('spider on rock macro',         'real_spider.jpg',   800, 800, '蜘蛛·渺小征服者'),
    ('sunset behind mountain peak',  'real_sunset.jpg',  1200, 800, '落日·太阳意象'),
    ('mountain rock cliff face',     'real_cliff.jpg',   1200, 800, '石砾·岩壁·深渊'),
    ('Eurasian skylark bird',        'real_skylark.jpg',  800, 800, '云雀·欢乐精灵'),
]
for term, fname, tw, th, usage in TARGETS:
    dest = os.path.join(OUT, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f'[skip] {fname}'); continue
    print(f'[search] {term} ({usage}) ...')
    titles = search_files(term, limit=12)
    time.sleep(2)
    ok = False
    for title in titles:
        url = get_thumb(title, width=max(tw,th))
        if not url: continue
        raw = os.path.join(OUT, '_raw_'+fname)
        if download(url, raw):
            try:
                fit_crop(raw, dest, tw, th)
                os.remove(raw)
                print(f'  OK {title} -> {fname} ({tw}x{th})'); ok = True; break
            except Exception as e:
                print(f'  crop fail {title}: {e}')
    if not ok:
        print(f'  XX no image for: {term}')
print('\nDONE')
