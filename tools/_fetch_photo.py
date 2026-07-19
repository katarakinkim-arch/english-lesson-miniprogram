# -*- coding: utf-8 -*-
"""Fetch a REAL, freely-licensed photo for a lesson (works in THIS sandbox).

Primary : Wikimedia Commons  (free-licensed, real, topic-relevant photos/diagrams)
          - list=search to find File: candidates (the generator= variant is blocked here)
          - imageinfo to get the ORIGINAL url + license + author
          - download original, PIL-resize (avoids Wikimedia's restricted-thumb-width 400)
Fallback : loremflickr.com     (real Flickr CC photos, matched by keyword)
Writes   : <out_path>  (resized JPEG)  +  <out_path>.attrib.json (license/author/source)

Prints the final saved path (or empty on total failure) so the driver can capture it.
Usage:  _fetch_photo.py "<zh_query>" "<en_query>" <out_path>
"""
import os, sys, json, re
import ssl
try:
    from urllib.request import Request, urlopen
    from urllib.parse import quote
except Exception:
    from urllib2 import Request, urlopen, quote
from io import BytesIO
from PIL import Image

UA = {'User-Agent': 'Mozilla/5.0 (compatible; edu-lesson-finetune/1.0)'}
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

IMG_MIME = ('image/jpeg', 'image/png')


def get_bytes(url, timeout=30):
    req = Request(url, headers=UA)
    return urlopen(req, timeout=timeout, context=CTX).read()


def commons_search(query, limit=8):
    q = quote(query.encode('utf-8'))
    url = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
           "&list=search&srsearch=%s&srnamespace=6&srlimit=%d" % (q, limit))
    try:
        data = json.loads(get_bytes(url).decode('utf-8', 'ignore'))
    except Exception:
        return []
    return [h['title'] for h in (data.get('query') or {}).get('search', [])]


def commons_imageinfo(title):
    q = quote(title.encode('utf-8'))
    url = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
           "&titles=%s&prop=imageinfo&iiprop=url%%7Csize%%7Cmime%%7Cextmetadata" % q)
    try:
        data = json.loads(get_bytes(url).decode('utf-8', 'ignore'))
    except Exception:
        return None
    pages = (data.get('query') or {}).get('pages') or {}
    for p in pages.values():
        ii = (p.get('imageinfo') or [{}])[0]
        if (ii.get('mime') or '') not in IMG_MIME:
            continue
        em = ii.get('extmetadata') or {}
        author = re.sub('<[^>]+>', '', (em.get('Artist') or {}).get('value', '') or '')
        return {
            'url': ii.get('url'),
            'license': (em.get('LicenseShortName') or {}).get('value', ''),
            'author': author[:80],
            'title': p.get('title', ''),
        }
    return None


def save_image(data, out_path, max_w=1200):
    im = Image.open(BytesIO(data)).convert('RGB')
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    im.save(out_path, 'JPEG', quality=85)
    return out_path


def loremflickr(keywords, out_path, lock):
    kw = quote(keywords.replace(' ', ',').encode('utf-8'))
    url = "https://loremflickr.com/%d/%d/%s?lock=%d" % (max_w, int(max_w * 0.66), kw, lock)
    try:
        data = get_bytes(url, timeout=25)
        if len(data) > 3000:
            save_image(data, out_path)
            return {'license': 'Flickr CC (via loremflickr)', 'author': '',
                    'source_url': 'https://loremflickr.com/', 'title': keywords}
    except Exception:
        pass
    return None


def main():
    if len(sys.argv) < 4:
        print(''); sys.exit(1)
    zh, en, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    d = os.path.dirname(out_path)
    os.makedirs(d, exist_ok=True)
    max_w = 1200
    lock = abs(hash(zh + '|' + en)) % 100000
    attrib = None

    # 1) Wikimedia Commons (zh then en)
    for q in [zh, en]:
        if not q or len(q) < 2:
            continue
        for t in commons_search(q):
            info = commons_imageinfo(t)
            if info and info.get('url'):
                try:
                    data = get_bytes(info['url'])
                    if len(data) > 3000:
                        save_image(data, out_path)
                        attrib = {
                            'license': info['license'], 'author': info['author'],
                            'source_url': 'https://commons.wikimedia.org/wiki/' + quote(t.encode('utf-8')),
                            'title': t,
                        }
                        break
                except Exception:
                    continue
            if attrib:
                break
        if attrib:
            break

    # 2) fallback: loremflickr (real Flickr CC photos by keyword)
    if not attrib:
        for q in [zh, en]:
            if q:
                attrib = loremflickr(q, out_path, lock)
                if attrib:
                    break

    if attrib:
        json.dump(attrib, open(out_path + '.attrib.json', 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        print(out_path)
    else:
        print('')


if __name__ == '__main__':
    main()
