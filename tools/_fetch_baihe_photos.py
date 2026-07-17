# -*- coding: utf-8 -*-
"""从 Wikimedia Commons 下载百合花 PPT 需要的真实照片。
流程：API search 找文件 → imageinfo 取 thumburl → curl 下载 → PIL 压缩裁剪。
"""
import os, json, subprocess, sys
from urllib.parse import urlencode
from PIL import Image

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'preview_v7', '_baihe_photos')
os.makedirs(OUT, exist_ok=True)
UA = 'WorkBuddyLessonBot/1.0 (educational use; python-requests)'
REFERER = 'https://commons.wikimedia.org/'

def api(params):
    url = 'https://commons.wikimedia.org/w/api.php?' + urlencode(params)
    r = subprocess.run(['curl', '-sL', '-H', f'User-Agent: {UA}', '-H', f'Referer: {REFERER}', url],
                       capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except Exception:
        print('  API 返回非JSON:', r.stdout[:200])
        return {}

def search_files(term, limit=10):
    d = api({'action':'query','list':'search','srsearch':term,'srnamespace':6,'srlimit':limit,'format':'json'})
    return [h['title'] for h in d.get('query', {}).get('search', [])]

def get_thumb(title, width=900):
    d = api({'action':'query','prop':'imageinfo','titles':title,'iiprop':'url|size|mime','iiurlwidth':width,'format':'json'})
    pages = d.get('query', {}).get('pages', {})
    for p in pages.values():
        ii = p.get('imageinfo', [])
        if ii:
            info = ii[0]
            if info.get('mime', '').startswith('image/'):
                return info.get('thumburl') or info.get('url')
    return None

def download(url, dest):
    r = subprocess.run(['curl', '-sL', '-H', f'User-Agent: {UA}', '-H', f'Referer: {REFERER}',
                        '-o', dest, url, '-w', '%{http_code}'], capture_output=True, text=True)
    code = r.stdout.strip()
    return code == '200' and os.path.getsize(dest) > 5000

def fit_crop(src, dest, tw, th):
    """裁剪到 tw×th 比例并缩放。"""
    im = Image.open(src).convert('RGB')
    iw, ih = im.size
    target_ratio = tw / th
    img_ratio = iw / ih
    if img_ratio > target_ratio:
        new_w = int(ih * target_ratio)
        left = (iw - new_w) // 2
        im = im.crop((left, 0, left + new_w, ih))
    else:
        new_h = int(iw / target_ratio)
        top = (ih - new_h) // 2
        im = im.crop((0, top, iw, top + new_h))
    im = im.resize((tw, th), Image.LANCZOS)
    im.save(dest, 'JPEG', quality=82)

# 需要的图：关键词 + 目标文件名 + 目标尺寸
TARGETS = [
    # (搜索词, 输出文件名, 目标宽, 目标高, 用途)
    ('Lilium candidum flower',  'real_lily.jpg',     1000, 1200, '封面/意象 百合花'),
    ('Lilium flower white',     'real_lily2.jpg',    800,  800,  '备用百合花'),
    ('full moon night sky',     'real_moon.jpg',     1400, 800,  'p11 风格 月光'),
    ('old newspaper vintage',   'real_newspaper.jpg', 800, 800,  'p4 背景 旧报纸'),
    ('handmade quilt floral',   'real_quilt.jpg',    1200, 700,  'p6 意象 被子纹理'),
    ('vintage fountain pen notebook', 'real_pen.jpg', 800, 800, 'p13 作业 钢笔本子'),
]

results = []
for term, fname, tw, th, usage in TARGETS:
    dest = os.path.join(OUT, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f'[skip] {fname} 已存在')
        results.append((fname, True, usage)); continue
    print(f'[search] {term} ...')
    titles = search_files(term, limit=10)
    ok = False
    for title in titles:
        url = get_thumb(title, width=max(tw, th))
        if not url: continue
        raw = os.path.join(OUT, '_raw_' + fname)
        if download(url, raw):
            try:
                fit_crop(raw, dest, tw, th)
                os.remove(raw)
                print(f'  ✓ {title} -> {fname} ({tw}x{th})')
                ok = True; break
            except Exception as e:
                print(f'  裁剪失败 {title}: {e}')
    if not ok:
        print(f'  ✗ 未找到可用图: {term}')
    results.append((fname, ok, usage))

print('\n=== 结果 ===')
for fname, ok, usage in results:
    print(f'  {"✓" if ok else "✗"} {fname}  ({usage})')
