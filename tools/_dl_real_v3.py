#!/usr/bin/env python3
"""Download v3: Get main images from Wikipedia article pages.
   Each target maps to a specific Wiki article whose featured image IS the correct photo.
   This bypasses the broken search API entirely.
"""
import os, sys, json, time, urllib.request, urllib.error, ssl

IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'classroom_images_v2')
os.makedirs(IMG_DIR, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Target -> list of (wiki_api_url, description) to try in order
# Using both zh-wiki and en-wiki for better coverage
TARGETS = [
    ('orange_isle.jpg', [
        ('https://zh.wikipedia.org/w/api.php', '橘子洲'),
        ('https://en.wikipedia.org/w/api.php', 'Orange Isle'),
        ('https://commons.wikimedia.org/w/api.php', 'File:Mao_Zedong_Youth_Sculpture.jpg'),
    ]),
    ('red_mountains.jpg', [
        ('https://zh.wikipedia.org/w/api.php', '香山公园'),
        ('https://en.wikipedia.org/w/api.php', 'Fragrant_Hills'),
        ('https://zh.wikipedia.org/w/api.php', '岳麓山'),
    ]),
    ('green_river.jpg', [
        ('https://zh.wikipedia.org/w/api.php', '湘江'),
        ('https://en.wikipedia.org/w/api.php', 'Xiang_River'),
        ('https://zh.wikipedia.org/w/api.php', '漓江'),
    ]),
    ('fish.jpg', [
        # For "fish swimming in clear water", use a specific Commons file
        ('https://commons.wikimedia.org/w/api.php', 'File:Fish_in_clear_water.jpg'),
        ('https://commons.wikimedia.org/w/api.php', 'File:Cyprinus_carpio_(Koi).jpg'),
        ('https://commons.wikimedia.org/w/api.php', 'File:Freshwater_fish.jpg'),
    ]),
    ('rapids.jpg', [
        ('https://commons.wikimedia.org/w/api.php', 'File:River_rapids.jpg'),
        ('https://zh.wikipedia.org/w/api.php', '虎跳峡'),
        ('https://en.wikipedia.org/w/api.php', 'Tiger_Leaping_Gorge'),
    ]),
    ('boats.jpg', [
        ('https://zh.wikipedia.org/w/api.php', '漓江'),
        ('https://commons.wikimedia.org/w/api.php', 'File:Li_River_fishing_boats.jpg'),
        ('https://commons.wikimedia.org/w/api.php', 'File:Cormorant_fishing.jpg'),
    ]),
]


def get_page_image(api_base, title):
    """Get the main image for a wiki article or commons file."""
    is_file = title.startswith('File:') or title.startswith('file:')
    q_title = urllib.parse.quote(title)

    if is_file:
        url = f'{api_base}?action=query&titles={q_title}&prop=imageinfo&iiprop=url|size&iiurlwidth=1600&format=json'
    else:
        url = f'{api_base}?action=query&titles={q_title}&prop=pageimages&piprop=original&pithumbsize=1600&format=json'

    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'LessonPPTBuilder/1.0 (Educational use)'
        })
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        data = json.loads(resp.read())
        pages = data.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            if is_file:
                for ii in pdata.get('imageinfo', []):
                    thumb = ii.get('thumburl') or ii.get('url')
                    return {
                        'url': thumb,
                        'orig': ii.get('url'),
                        'width': ii.get('width', 0),
                        'size': ii.get('size', 0),
                    }
            else:
                orig = pdata.get('original', {})
                if orig and orig.get('source'):
                    return {
                        'url': orig['source'],
                        'width': orig.get('width', 0),
                        'height': orig.get('height', 0),
                    }
                # Try thumbnail as fallback
                thumb = pdata.get('thumbnail', {})
                if thumb and thumb.get('source'):
                    return {
                        'url': thumb['source'],
                        'width': thumb.get('width', 0),
                        'height': thumb.get('height', 0),
                    }
    except Exception as e:
        print(f'  Error: {e}')
    return None


def download(url, dest_path, retries=3):
    """Download with retries."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'LessonPPTBuilder/1.0 (Educational use)'
            })
            resp = urllib.request.urlopen(req, timeout=60, context=ctx)
            data = resp.read()
            if len(data) < 10000:  # too small, probably an error page
                print(f'      -> too small ({len(data)} bytes), skip')
                return -1
            with open(dest_path, 'wb') as f:
                f.write(data)
            return len(data)
        except Exception as e:
            if attempt < retries - 1:
                print(f'      -> retry ({attempt+1}/{retries}): {e}')
                time.sleep(5)
            else:
                print(f'      -> failed: {e}')
    return -1


import urllib.parse

print('=' * 60)
print('WIKIPEDIA MAIN IMAGE DOWNLOADER V3')
print('=' * 60)

ok = 0
fails = []

for fname, sources in TARGETS:
    out = os.path.join(IMG_DIR, fname)
    print(f'\n== {fname} ==')

    found = False
    for api_base, title in sources:
        label = title.split(':')[0] if ':' in title else title
        print(f'  trying {label} @ {api_base.split("/")[2]} ...')

        info = get_page_image(api_base, title)
        if not info:
            print(f'    no image found')
            continue

        dl_url = info['url']
        w = info.get('width', '?')
        sz = info.get('size', '?')
        print(f'    image found ({w}px, ~{sz}b)')

        nbytes = download(dl_url, out)
        if nbytes > 0:
            print(f'    OK! {nbytes} bytes -> {fname}')
            found = True
            ok += 1
            break
        else:
            print(f'    download failed')

    if not found:
        fails.append(fname)
        print(f'  FAILED')

print('\n' + '=' * 60)
print(f'Result: {ok}/{len(TARGETS)} succeeded')
if fails:
    print(f'Failed: {fails}')
else:
    print('ALL DONE!')
