# -*- coding: utf-8 -*-
"""《沁园春·长沙》真实照片下载（Wikimedia Commons API + curl）。"""
import os, json, subprocess, time
from urllib.parse import urlencode
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'preview_v7', '_qinyuanchun_photos')
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

TARGETS = [
    ('Mao Zedong statue Changsha',   'real_statue.jpg', 1200, 750, '封面 橘子洲青年毛泽东雕像'),
    ('Xiang River Changsha',         'real_xiang.jpg',  1400, 800, '湘江秋景'),
    ('Yuelu Mountain',               'real_yuelu.jpg',  1200, 800, '万山红遍 岳麓山'),
    ('Orange Isle Changsha',         'real_isle.jpg',   1200, 800, '橘子洲头'),
    ('autumn maple leaves',          'real_maple.jpg',   800, 800, '层林尽染'),
    ('sailboats river regatta',      'real_sail.jpg',   1200, 750, '百舸争流'),
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
