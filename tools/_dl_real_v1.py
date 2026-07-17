# -*- coding: utf-8 -*-
"""下载真实照片替换手绘风景图。每张先搜到候选，下载后人工查看确认。"""
import os, time, json, urllib.request, urllib.parse

OUT = 'C:/Users/1/WorkBuddy/2026-07-08-15-47-48/miniprogram/classroom_images_v2'
API = 'https://commons.wikimedia.org/w/api.php'

# 用词尽量精确，避免错配（如 eagle 别搜成 bald eagle）
QUERIES = {
    'orange_isle':   'Orange Isle Changsha Hunan',
    'red_mountains': 'autumn red maple forest mountain',
    'green_river':   'Li River Guilin clear water',
    'eagle':         'Aquila chrysaetos flying',
    'fish':          'fish clear shallow water',
    'boats':         'Li River Guilin fishing boats',
    'rapids':        'river rapids whitewater',
    'autumn_china':  'Jiuzhaigou autumn',
}

IMG_EXT = ('.jpg', '.jpeg', '.png')

def api_search(q):
    params = {
        'action': 'query', 'format': 'json',
        'generator': 'search', 'gsrsearch': q, 'gsrnamespace': '6',
        'gsrlimit': '8', 'prop': 'imageinfo', 'iiprop': 'url',
        'iiurlwidth': '1600',
    }
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': 'EduPPT/1.0 (edu@example.com)'})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.load(r)
    pages = data.get('query', {}).get('pages', {})
    out = []
    for p in pages.values():
        title = p.get('title', '')
        if not title.lower().endswith(IMG_EXT):
            continue
        ii = p.get('imageinfo', [{}])[0]
        u = ii.get('thumburl') or ii.get('url')
        if u:
            out.append((title, u))
    return out

def download(url, path, retries=6):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'EduPPT/1.0'})
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
            with open(path, 'wb') as f:
                f.write(data)
            return len(data)
        except Exception as e:
            last = e
            time.sleep(2 + i * 2)
    print(f'  FAIL {os.path.basename(path)}: {last}')
    return 0

for key, q in QUERIES.items():
    print(f'\n== {key}  query: {q}')
    try:
        cands = api_search(q)
    except Exception as e:
        print(f'  search error: {e}')
        continue
    if not cands:
        print('  no candidates')
        continue
    for t, u in cands[:5]:
        print(f'   - {t}')
    title, url = cands[0]
    print(f'  -> downloading: {title}')
    n = download(url, os.path.join(OUT, key + '.jpg'))
    print(f'     bytes={n}')
