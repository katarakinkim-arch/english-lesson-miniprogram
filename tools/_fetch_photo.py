# -*- coding: utf-8 -*-
"""Fetch a REAL, freely-licensed photo for a lesson (runs on an OPEN-NETWORK machine).

Primary: Wikimedia Commons API (free-licensed, real photos). Tries the zh query first,
then the english query if too few results. Downloads a 1200px thumbnail to <out_path>.
Fallback: if Commons yields nothing, tries a Bing image thumbnail (th.bing.com).
Prints the final saved path (or empty on total failure) so the driver can capture it.

Usage:  _fetch_photo.py "<zh_query>" "<en_query>" <out_path>
"""
import os, sys, re, json
try:
    from urllib.request import Request, urlopen
    from urllib.parse import quote
except Exception:
    from urllib2 import Request, urlopen, quote

UA = {'User-Agent': 'edu-lesson-finetune/1.0 (https://github.com; contact: teacher)'}

def get(url, timeout=25):
    req = Request(url, headers=UA)
    return urlopen(req, timeout=timeout).read()

def commons_search(query, limit=12):
    q = quote(query.encode('utf-8'))
    url = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
           "&generator=search&gsrsearch=%s&gsrnamespace=6&gsrlimit=%d"
           "&prop=imageinfo&iiprop=url%%7Csize%%7Cmime&iiurlwidth=1200" % (q, limit))
    try:
        data = json.loads(get(url))
    except Exception:
        return []
    pages = (data.get('query') or {}).get('pages') or {}
    out = []
    for p in pages.values():
        ii = (p.get('imageinfo') or [{}])[0]
        mime = ii.get('mime', '')
        if not mime.startswith('image'):
            continue
        w = ii.get('width', 0) or 0
        if w < 400:
            continue
        out.append({
            'thumb': ii.get('thumburl') or ii.get('url'),
            'url': ii.get('url'),
            'w': w, 'h': ii.get('height', 0) or 0,
            'title': p.get('title', ''),
        })
    # prefer reasonably-sized landscape-ish photos
    out.sort(key=lambda x: (x['w'] <= 1600, -x['w']))
    return out

def bing_thumb(query, out_path):
    q = quote(query.encode('utf-8'))
    url = "https://www.bing.com/images/search?q=" + q
    try:
        html = get(url).decode('utf-8', 'ignore')
    except Exception:
        return False
    urls = re.findall(r'https://th\.bing\.com/th/[^\"\\<> ]+', html)
    urls += re.findall(r'https://tse\d+\.mm\.bing\.net/th/[^\"\\<> ]+', html)
    for u in urls:
        try:
            data = get(u)
            if len(data) > 3000:
                open(out_path, 'wb').write(data)
                return True
        except Exception:
            continue
    return False

def main():
    if len(sys.argv) < 4:
        print(''); sys.exit(1)
    zh, en, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    for q in [zh, en]:
        if not q or len(q) < 2:
            continue
        hits = commons_search(q)
        if hits:
            try:
                data = get(hits[0]['thumb'])
                if len(data) > 3000:
                    open(out_path, 'wb').write(data)
                    print(out_path)
                    sys.exit(0)
            except Exception:
                pass
    # fallback to Bing thumbnail
    for q in [zh, en]:
        if q and bing_thumb(q, out_path):
            print(out_path)
            sys.exit(0)
    print('')  # no photo found

if __name__ == '__main__':
    main()
