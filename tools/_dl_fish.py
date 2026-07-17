# -*- coding: utf-8 -*-
"""Download better fish image from Wikipedia - swimming fish, not dead fish in hand"""
import urllib.request
import json
import os
import time

OUTDIR = r'C:\Users\1\WorkBuddy\2026-07-08-15-47-48\miniprogram\classroom_images_v2'

def get_pageimage(lang, title):
    """Get the main image for a Wikipedia page"""
    if lang == 'zh':
        base = 'https://zh.wikipedia.org/w/api.php'
    else:
        base = 'https://en.wikipedia.org/w/api.php'
    
    url = f"{base}?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&piprop=original&pilicense=any&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'EducationalPPT/1.0 (contact for issues)'})
    resp = urllib.request.urlopen(req, timeout=15)
    data = json.loads(resp.read())
    pages = data.get('query', {}).get('pages', {})
    for pid, pinfo in pages.items():
        orig = pinfo.get('original', {})
        src = orig.get('source', '')
        if src:
            return src
    return None

def download(url, filename):
    """Download an image file"""
    fpath = os.path.join(OUTDIR, filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'EducationalPPT/1.0'})
        resp = urllib.request.urlopen(req, timeout=30)
        with open(fpath, 'wb') as f:
            f.write(resp.read())
        size = os.path.getsize(fpath)
        print(f"  OK: {filename} ({size:,} bytes)")
        return True
    except Exception as e:
        print(f"  FAIL: {filename} -> {e}")
        return False

# Strategy: search for elegant swimming fish images
candidates = [
    # Koi/carp - elegant, artistic, swimming
    ('en', 'Koi', '_fish_koi.jpg'),
    ('zh', '锦鲤', '_fish_jinli.jpg'),
    # Goldfish - classic Chinese aesthetic
    ('en', 'Goldfish', '_fish_goldfish.jpg'),
    ('zh', '金鱼', '_fish_jinyu.jpg'),
    # Freshwater fish in habitat
    ('en', 'Freshwater_fish', '_fish_freshwater.jpg'),
    # Specific beautiful species
    ('en', 'Cyprinus_carpio', '_fish_carpio.jpg'),
]

print("=== Searching for better fish images ===")
for lang, title, fname in candidates:
    print(f"\nTrying {lang}:{title} ...")
    try:
        src = get_pageimage(lang, title)
        if src:
            print(f"  Found: {src[:100]}")
            download(src, fname)
        else:
            print("  No image found")
    except Exception as e:
        print(f"  Error: {e}")
    time.sleep(2)

print("\nDone! Check images and pick the best one.")
