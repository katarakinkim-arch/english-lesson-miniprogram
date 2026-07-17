#!/usr/bin/env python3
"""Download v2: precise real photos for 6 broken images.
   Strategy: multiple query candidates per image + keyword blacklist filtering.
   Must verify each downloaded image manually after this runs.
"""
import os, sys, time, json, urllib.request, urllib.error, ssl

IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'classroom_images_v2')
os.makedirs(IMG_DIR, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Blacklist: if ANY of these appear in the filename/title, SKIP
BLACKLIST_WORDS = [
    'kfc', 'kentucky', 'mcdonald', 'burger', 'restaurant',
    'salmon', 'chinook', 'trout', 'ocean', 'marine', 'seafood',
    'kayak', 'canoe', 'slalom', 'olympic', 'championship', 'athlete', 'sport',
    'bald eagle', 'haliaeetus',
]

# Each target: (output_filename, query_candidates)
TARGETS = [
    ('orange_isle.jpg', [
        ('橘子洲头', 'Mao Zedong sculpture Orange Isle'),
        ('Changsha Orange Isle youth statue', None),
        ('长沙 橘子洲 风光', None),
    ]),
    ('red_mountains.jpg', [
        ('香山红叶 北京', 'Fragrant Hills Beijing autumn red maple'),
        ('Yuelu Mountain autumn red leaves', None),
        ('Chinese mountain autumn forest red foliage', None),
    ]),
    ('green_river.jpg', [
        ('湘江 长沙 清澈', 'Xiang River Changsha clear'),
        ('Li River Guilin clear blue water', None),
        ('China river clear water landscape', None),
    ]),
    ('fish.jpg', [
        ('freshwater fish clear shallow water', None),
        ('carp koi clear water swimming', None),
        ('小鱼 浅底 游动', 'small fish clear river bottom'),
    ]),
    ('rapids.jpg', [
        ('river rapids waterfall fast flowing water', None),
        ('natural river white water current', None),
        ('激流 河流 瀑布', 'river rushing current'),
    ]),
    ('boats.jpg', [
        ('Li River bamboo raft cormorant', None),
        ('漓江 竹筏 渔翁', 'Guilin Li River fishing boat'),
        ('traditional chinese fishing boat river', None),
    ]),
]


def search_wikimedia(query_en, query_zh=None, limit=10):
    """Search Wikimedia Commons API, return list of (title, file_url_hint)."""
    results = []
    # Build query string
    qs_parts = []
    if query_en:
        qs_parts.append(query_en)
    if query_zh:
        qs_parts.append(query_zh)
    q_str = ' '.join(qs_parts)

    url = (
        'https://commons.wikimedia.org/w/api.php'
        '?action=query'
        '&list=search'
        f'&srsearch={urllib.parse.quote(q_str)}'
        '&srnamespace=6'
        '&srlimit={limit}'
        '&format=json'
    )
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'LessonPPTBuilder/1.0'})
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        data = json.loads(resp.read())
        for item in data.get('query', {}).get('search', []):
            title = item.get('title', '')
            results.append(title)
    except Exception as e:
        print(f'  Search error: {e}')
    return results


def get_image_info(title):
    """Get actual image URL and metadata for a given file title."""
    base = 'https://commons.wikimedia.org/w/api.php'
    params = (
        '?action=query'
        '&prop=imageinfo'
        '&iiprop=url|size|extmetadata'
        '&iiurlwidth=1600'
        '&format=json'
    )
    url = base + params + '&titles=' + urllib.parse.quote(title)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'LessonPPTBuilder/1.0'})
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        data = json.loads(resp.read())
        pages = data.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            for ii in pdata.get('imageinfo', []):
                thumb_url = ii.get('thumburl') or ii.get('url')
                orig_url = ii.get('url')
                width = ii.get('width', 0)
                height = ii.get('height', 0)
                size_bytes = ii.get('size', 0)
                desc = (ii.get('extmetadata', {}).get('ImageDescription', {}) or {}).get('value', '')
                return {
                    'thumb_url': thumb_url,
                    'orig_url': orig_url,
                    'width': width,
                    'height': height,
                    'size': size_bytes,
                    'desc': desc[:200],
                }
    except Exception as e:
        print(f'  Info error: {e}')
    return None


def download_image(url, dest_path, retries=3):
    """Download image to path, return bytes count or -1."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'LessonPPTBuilder/1.0 (Educational use)',
            })
            resp = urllib.request.urlopen(req, timeout=60, context=ctx)
            data = resp.read()
            with open(dest_path, 'wb') as f:
                f.write(data)
            return len(data)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(3)
            else:
                print(f'  Download failed after {retries} attempts: {e}')
    return -1


def is_blacklisted(title):
    t_lower = title.lower()
    return any(bw in t_lower for bw in BLACKLIST_WORDS)


def process_target(filename, query_list):
    """Try each query candidate until we get a good download."""
    out_path = os.path.join(IMG_DIR, filename)

    for qi, (q_en, q_zh) in enumerate(query_list):
        print(f'\n== {filename}  attempt {qi+1}/{len(query_list)}: {q_en or q_zh}')

        titles = search_wikimedia(q_en, q_zh, limit=15)

        if not titles:
            print(f'  No results for this query.')
            continue

        good_titles = [t for t in titles if not is_blacklisted(t)]
        if not good_titles:
            print(f'  All {len(titles)} results blacklisted. Sample: {titles[:3]}')
            continue

        print(f'  Found {len(good_titles)} non-blacklisted candidates')

        for ti, title in enumerate(good_titles[:5]):
            if ti >= 5:
                break
            print(f'  [{ti+1}] {title[:80]}')
            info = get_image_info(title)
            if not info:
                print(f'      -> no image info, skip')
                continue

            dl_url = info['thumb_url'] or info['orig_url']
            w, h, sz = info['width'], info['height'], info['size']

            # Basic quality filter
            if w < 400 or h < 300 or sz < 50000:
                print(f'      -> too small ({w}x{h}, {sz}b), skip')
                continue

            print(f'      -> downloading ({w}x{h}, {sz} bytes)...')
            nbytes = download_image(dl_url, out_path)
            if nbytes > 0:
                print(f'      -> OK! {nbytes} bytes saved to {filename}')
                return True
            else:
                print(f'      -> download failed, trying next...')

    print(f'\n  FAILED: all queries exhausted for {filename}')
    return False


# Main
import urllib.parse

print('='*60)
print('REAL PHOTO DOWNLOAD V2 - Precise queries + blacklist filter')
print('='*60)

ok_count = 0
fail_list = []

for fname, qlist in TARGETS:
    ok = process_target(fname, qlist)
    if ok:
        ok_count += 1
    else:
        fail_list.append(fname)

print('\n' + '='*60)
print(f'Done: {ok_count}/{len(TARGETS)} succeeded')
if fail_list:
    print(f'Failed: {fail_list}')
else:
    print('All images replaced successfully!')
