# -*- coding: utf-8 -*-
"""重新下载所有配图——严格按教案内容匹配，逐一人工确认搜索词。
目标：每张图必须能让学生一眼看出对应《沁园春·长沙》的哪个意象。
"""
import urllib.request, json, os, time, ssl

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'classroom_images_v2')
os.makedirs(OUT, exist_ok=True)

SSL_CTX = ssl.create_default_context()

def search_wikimedia(query, limit=8):
    """Search Wikimedia Commons, return list of (title, url, w, h)"""
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srlimit={limit}&srnamespace=6&format=json&origin=*"
    req = urllib.request.Request(url, headers={'User-Agent': 'EduPptBuilder/1.0'})
    try:
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  [SEARCH ERR] {query}: {e}")
        return []
    results = []
    for item in data.get('query', {}).get('search', []):
        title = item['title']  # File:xxx.jpg
        # Get image info to find real URL
        info_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=800&format=json&origin=*"
        try:
            req2 = urllib.request.Request(info_url, headers={'User-Agent': 'EduPptBuilder/1.0'})
            with urllib.request.urlopen(req2, context=SSL_CTX, timeout=15) as r2:
                info = json.loads(r2.read())
            pages = info.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                ii = pdata.get('imageinfo', [{}])[0]
                dl = ii.get('url', '')
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                desc = (ii.get('extmetadata', {}).get('ImageDescription', {}) or {}).get('value', '')[:120]
                if dl:
                    results.append((title, dl, w, h, desc))
        except Exception as e:
            print(f"  [INFO ERR] {title}: {e}")
    return results


def download(url, path, retries=3):
    """Download with retry"""
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'EduPptBuilder/1.0'})
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as resp:
                data = resp.read()
            with open(path, 'wb') as f:
                f.write(data)
            print(f"  OK {path} ({len(data)//1024}KB)")
            return True
        except Exception as e:
            print(f"  retry {i+1}/{retries}: {e}")
            time.sleep(2)
    return False


# ====================================================================
# 定义每张图的需求（中文搜索词 + 英文备选 + 人肉验证标准）
# ====================================================================
NEEDS = {
    # (输出文件名, 中文主搜, 英文备选, 验证标准, 是否需要横幅)
    'orange_isle':    ('orange_isle.jpg',     '橘子洲 长沙 湘江',         'Orange Isle Changsha Xiang River',       '必须是湘江中的橘子洲，有江水+远山或城市天际线', False),
    'red_mountains':  ('red_mountains.jpg',    '岳麓山 红叶 秋天 枫叶',   'Yuelu Mountain red maple autumn China',   '必须是成片的红枫林或红色山林，不是几片红叶', False),
    'green_river':    ('green_river.jpg',      '湘江 碧水 漓江 清澈',    'clear green river China Li Xiang',        '碧绿清澈的江河，能看到水面和岸', False),
    'eagle':          ('eagle.jpg',            '老鹰 飞翔 蓝天',          'eagle falcon hawk soaring sky',           '猛禽在天空中飞翔的剪影/清晰图，不能是白头海雕', False),
    'fish':           ('fish.jpg',             '鱼 清水 游泳 淡水鱼',     'fish swimming clear freshwater river',     '淡水鱼在清澈浅水中游动，能看到水底，不能是海水鱼/珊瑚礁', False),
    'boats':          ('boats.jpg',            '帆船 百舸 争流 江面',    'boats sailing river traditional China',    '多艘船在水面上航行/竞渡的场景', False),
    'rapids':         ('rapids.jpg',           '激流 浪花 急流 击水',     'river rapids waves fast water swimming',   '湍急的江水/浪花，表现"中流击水"的力量感', False),
    'autumn_forest':  ('autumn_china.jpg',      '中国 秋天 枫林 山水画',   'Chinese autumn forest painting landscape', '中国秋天景色（实景或国画），表现秋天氛围，不能是美国/欧洲风景', False),
}

import urllib.parse

log = []
for key, (fname, cn, en, criteria, _) in NEEDS.items():
    print(f"\n{'='*60}\n[{key}] → {fname}\n  搜: {cn} / {en}\n  验证: {criteria}\n")
    
    found = False
    # Try Chinese first, then English
    for q in [cn, en]:
        if found:
            break
        results = search_wikimedia(q, limit=10)
        print(f"  搜'{q}' → {len(results)}结果")
        for title, url, w, h, desc in results:
            # Basic filters
            if w < 600 or h < 400:
                continue
            # Skip obvious wrong types
            lower = (title + ' ' + desc).lower()
            if key == 'eagle' and ('bald eagle' in lower or 'haliaeetus' in lower):
                print(f"  SKIP bald eagle: {title}")
                continue
            if key == 'fish' and any(kw in lower for kw in ['coral', 'reef', 'aquarium', 'ocean', 'marine', 'saltwater', 'tropical fish']):
                print(f"  SKIP marine fish: {title}")
                continue
            if key in ('orange_isle', 'autumn_forest') and any(kw in lower for kw in ['colorado', 'maroon bells', 'aspen', 'rocky mountain']):
                print(f"  SKIP american landscape: {title}")
                continue
            
            path = os.path.join(OUT, fname)
            print(f"  TRY: {title} ({w}x{h})")
            if download(url, path):
                log.append(f"[{key}] {title} ({w}x{h}) from '{q}'")
                found = True
                break
        time.sleep(1)
    
    if not found:
        log.append(f"[{key}] !!! FAILED TO DOWNLOAD")

print("\n\n" + "="*60)
print("DOWNLOAD LOG:")
for l in log:
    print(l)
print(f"\nDone. {sum(1 for l in log if '!!!' not in l)}/{len(NEEDS)} succeeded.")
