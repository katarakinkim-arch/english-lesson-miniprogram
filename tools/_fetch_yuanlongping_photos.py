# -*- coding: utf-8 -*-
"""《喜看稻菽千重浪——袁隆平》真实照片下载（Wikipedia pageimages + Commons 兜底 + curl）。"""
import os, json, subprocess, time
from urllib.parse import urlencode
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'preview_v7', '_yuanlongping_photos')
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

def wiki_thumb(lang, title, width):
    """维基百科条目人工精选主图（最可靠）。"""
    d = api({'action':'query','prop':'pageimages','piprop':'thumbnail',
             'pithumbsize':width,'titles':title,'format':'json'})
    for p in d.get('query',{}).get('pages',{}).values():
        th = p.get('thumbnail',{}).get('source')
        if th:
            return th
    return None

def commons_search_thumb(term, width=1200):
    d = api({'action':'query','list':'search','srsearch':term,'srnamespace':6,'srlimit':12,'format':'json'})
    for h in d.get('query',{}).get('search',[]):
        dd = api({'action':'query','prop':'imageinfo','titles':h['title'],
                  'iiprop':'url|mime','iiurlwidth':width,'format':'json'})
        for p in dd.get('query',{}).get('pages',{}).values():
            ii = p.get('imageinfo', [])
            if ii and ii[0].get('mime','').startswith('image/') and 'svg' not in ii[0].get('mime',''):
                return ii[0].get('thumburl') or ii[0].get('url')
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

# (method, id, fname, tw, th, usage)
# method: ('wiki', lang, title) 或 ('commons', search_term)
TARGETS = [
    (('wiki','zh','稻田'),       'real_rice_field.jpg', 1200, 800, '稻田·金色稻浪（封面/导入/背景）'),
    (('wiki','zh','水稻'),       'real_rice_plant.jpg',  800, 800, '稻穗特写（时间线/科学精神）'),
    (('wiki','zh','梯田'),       'real_terrace.jpg',    1200, 800, '梯田水田·试验田（挑战权威/知人论世）'),
    (('wiki','en','Yuan Longping'), 'real_yuanlongping.jpg', 900, 1100, '袁隆平田间照（科学精神/颁奖词）'),
    (('wiki','zh','麦田'),       'real_golden_field.jpg',1200, 800, '金色田野·丰收（颁奖词/余韵）'),
]

for spec, fname, tw, th, usage in TARGETS:
    dest = os.path.join(OUT, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f'[skip] {fname}'); continue
    print(f'[fetch] {usage} ...')
    url = None
    if spec[0] == 'wiki':
        url = wiki_thumb(spec[1], spec[2], width=max(tw,th))
    else:
        url = commons_search_thumb(spec[1], width=max(tw,th))
    time.sleep(2)
    if not url:
        # 兜底：Commons 搜索
        url = commons_search_thumb(fname.split('_')[1] if False else spec[2] if spec[0]=='wiki' else spec[1], width=max(tw,th))
    ok = False
    if url:
        raw = os.path.join(OUT, '_raw_'+fname)
        if download(url, raw):
            try:
                fit_crop(raw, dest, tw, th)
                os.remove(raw)
                print(f'  OK -> {fname} ({tw}x{th})'); ok = True
            except Exception as e:
                print(f'  crop fail: {e}')
    if not ok:
        print(f'  XX no image for: {usage}')
print('\nDONE')
