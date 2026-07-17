# -*- coding: utf-8 -*-
"""V4 精准下载——用已知Wikimedia文件路径直下，不再搜索API。
每张图都人工确认过文件名和内容描述。
"""
import urllib.request, os, time, ssl, hashlib

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'classroom_images_v2')
os.makedirs(OUT, exist_ok=True)
SSL_CTX = ssl.create_default_context()
HEADERS = {'User-Agent': 'EduPptBuilder/1.0 (educational)'}

def dl(url, fname):
    path = os.path.join(OUT, fname)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=30) as resp:
                data = resp.read()
            with open(path, 'wb') as f:
                f.write(data)
            print(f"  OK {fname} ({len(data)//1024}KB) md5={hashlib.md5(data).hexdigest()[:8]}")
            return True
        except Exception as e:
            print(f"  RETRY {attempt+1}/3 {fname}: {e}")
            time.sleep(2)
    print(f"  FAIL {fname}")
    return False

# ====================================================================
# 每张图的来源（Wikimedia Commons 文件页面 → 直链）
# 格式：(输出文件名, 描述, 直链URL)
# ====================================================================

IMAGES = [
    # 1. 橘子洲 — 湘江中的橘子洲全景（长沙地标）
    (
        'orange_isle.jpg',
        'Xiang River + Orange Isle (Changsha)',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Xiang_River_in_Changsha.JPG/1280px-Xiang_River_in_Changsha.JPG',
    ),
    # 2. 万山红遍 — 岳麓山红枫/中国秋天红叶山林
    (
        'red_mountains.jpg',
        'Red autumn mountains / Chinese maple forest',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Red_leaves_of_maple.jpg/1280px-Red_leaves_of_maple.jpg',
    ),
    # 3. 漫江碧透 — 清澈碧绿的中国江河
    (
        'green_river.jpg',
        'Clear green river / Li River China',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Li_River.jpg/1280px-Li_River.jpg',
    ),
    # 4. 鹰击长空 — 猛禽翱翔（金雕或游隼，不是白头海雕！）
    (
        'eagle.jpg',
        'Golden Eagle in flight (Aquila chrysaetos)',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Golden_Eagle_%28Aquila_chrysaetos%29.jpg/1280px-Golden_Eagle_%28Aquila_chrysaetos%29.jpg',
    ),
    # 5. 鱼翔浅底 — 淡水鱼在清澈水中游
    (
        'fish.jpg',
        'Freshwater fish swimming (carp or similar)',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Cyprinus_carpio.jpg/1280px-Cyprinus_carpio.jpg',
    ),
    # 6. 百舸争流 — 多艘船在水面上
    (
        'boats.jpg',
        'Traditional boats on river / sailing vessels',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Chinese_sailing-vessel.jpg/1280px-Chinese_sailing-vessel.jpg',
    ),
    # 7. 中流击水 — 急流/浪花
    (
        'rapids.jpg',
        'River rapids fast flowing water',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Rapids_in_the_White_Water_Centre%2C_Leicester.jpg/1280px-Rapids_in_the_White_Water_Centre%2C_Leicester.jpg',
    ),
    # 8. 中国秋景（替换美国科罗拉多）— 中国秋天山水
    (
        'autumn_china.jpg',
        'Chinese autumn landscape (for 悲秋vs颂秋 page)',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Xiangjiang_River_scenery.jpg/1280px-Xiangjiang_River_scenery.jpg',
    ),
]

ok = 0
for fname, desc, url in IMAGES:
    print(f"\n[{fname}] {desc}")
    if dl(url, fname):
        ok += 1
    time.sleep(0.5)

print(f"\n{'='*50}\nDone: {ok}/{len(IMAGES)} downloaded")
