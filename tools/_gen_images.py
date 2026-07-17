# -*- coding: utf-8 -*-
"""V5 配图生成器——PIL手绘风格化配图，严格对应《沁园春·长沙》每个意象。
原则：
1. 每张图的内容必须让学生一眼看出对应词中哪个意象
2. 风格统一：中国风配色 + 扁平几何 + 柔和渐变
3. 1280x720（16:9 PPT标准），JPEG质量85
"""
import math, random, os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'classroom_images_v2')
os.makedirs(OUT, exist_ok=True)
W, H = 1280, 720

# 调色板——湘江秋日
C = {
    'sky_top':     (135, 180, 220),   # 秋空上
    'sky_bot':     (200, 220, 235),   # 秋空下
    'river':       (65, 145, 160),    # 湘江碧
    'river_deep':  (40, 100, 120),    # 碧水深
    'mount':       (140, 85, 55),     # 山褐
    'red_leaf':    (178, 58, 42),     # 霜红（枫叶）
    'orange_leaf': (194, 112, 61),    # 陶土橙
    'gold':        (200, 168, 107),   # 金黄
    'forest':      (60, 95, 55),      # 林绿
    'ink':         (28, 43, 51),      # 墨（文字/深色）
    'mist':        (220, 215, 205),   # 暮霭/霜
    'paper':       (244, 239, 230),   # 暖纸底
}

def _grad(draw, y0, y1, c0, c1, steps=80):
    """垂直线性渐变"""
    for i in range(steps):
        t = i / (steps - 1)
        c = tuple(int(c0[j] + (c1[j] - c0[j]) * t) for j in range(3))
        draw.line([(0, int(y0 + (y1 - y0) * t)), (W, int(y0 + (y1 - y0) * t))], fill=c)

def _save(img, name):
    path = os.path.join(OUT, name)
    img.convert('RGB').save(path, 'JPEG', quality=85)
    print(f"  OK {name} ({os.path.getsize(path)//1024}KB)")

# ====================================================================
# 1. 橘子洲 — 湘江中的长条沙洲，远桥近水
# ====================================================================
def gen_orange_isle():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    # 天空
    _grad(d, 0, H * 0.45, C['sky_top'], C['sky_bot'])
    # 远山（岳麓山轮廓）
    mt = [(0, 380), (80, 340), (180, 310), (300, 330), (420, 290), (550, 320),
          (680, 280), (800, 310), (920, 295), (1050, 330), (1150, 310), (1280, 350)]
    d.polygon(mt + [(1280, 400), (0, 400)], fill=C['mount'])
    # 山上的红叶点缀
    for _ in range(60):
        x = random.randint(0, W)
        y = random.randint(285, 370)
        r = random.randint(8, 22)
        c = random.choice([C['red_leaf'], C['orange_leaf'], C['gold']])
        d.ellipse([x-r, y-r*0.7, x+r, y+r*0.7], fill=c)
    # 湘江水面
    d.rectangle([0, 400, W, H], fill=C['river'])
    # 水面纹理线
    for i in range(12):
        y = 410 + i * 26
        alpha = 30 + i * 4
        c = (*C['river_deep'][:2], min(alpha, 255))
        d.line([(0, y), (W, y)], fill=C['river_deep'], width=1)
    # 橘子洲本体（长条形沙洲，横贯江心）
    isle_y = 480
    isle_pts = [(180, isle_y+30), (220, isle_y), (400, isle_y-10), (700, isle_y),
                (900, isle_y+5), (1050, isle_y+20), (1100, isle_y+50), (1050, isle_y+70),
                (850, isle_y+65), (500, isle_y+55), (250, isle_y+60)]
    d.polygon(isle_pts, fill=(194, 178, 155))  # 沙洲色
    # 洲上树木
    for _ in range(35):
        x = random.randint(210, 1080)
        y = random.randint(isle_y-5, isle_y+45)
        r = random.randint(6, 14)
        d.ellipse([x-r, y-r*0.8, x+r, y+r*0.8], fill=C['forest'])
    # 橘子洲大桥（远处）
    d.line([(0, 395), (1280, 395)], fill=(160, 150, 140), width=3)
    for bx in range(0, 1280, 80):
        d.line([(bx, 385), (bx, 405)], fill=(160, 150, 140), width=2)
    # 标题水印
    try:
        fnt = ImageFont.truetype('msyh.ttc', 28)
        d.text((W-220, H-45), "橘子洲 · 长沙", fill=(255,255,255,180), font=fnt)
    except: pass
    _save(img, 'orange_isle.jpg')

# ====================================================================
# 2. 万山红遍 — 层林尽染的红色山林
# ====================================================================
def gen_red_mountains():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    _grad(d, 0, H * 0.35, C['sky_top'], C['mist'])
    # 多层山峦，由远及近，颜色从淡到浓
    layers = [
        ([(0,280),(200,230),(450,260),(700,220),(950,250),(1150,235),(1280,270)], (180,160,145), 0.4),
        ([(0,330),(150,280),(380,300),(600,270),(850,295),(1100,275),(1280,320)], (160,130,110), 0.6),
        ([(0,390),(200,330),(450,360),(700,320),(950,350),(1200,335),(1280,380)], (140,90,60), 0.85),
    ]
    for pts, base_c, density in layers:
        d.polygon(pts + [(1280, H), (0, H)], fill=base_c)
        # 红叶覆盖
        for _ in range(int(80 * density)):
            x = random.randint(0, W)
            y = random.randint(int(pts[1][1])-20, int(pts[2][1])+60)
            r = random.randint(10, 30)
            rc = random.choice([C['red_leaf'], C['orange_leaf'], (200, 80, 50), (220, 120, 60)])
            d.ellipse([x-r, y-r*0.7, x+r, y+r*0.7], fill=rc)
    # 最近层：浓密红枫
    near = [(0,480),(100,420),(300,450),(500,410),(750,440),(950,420),(1150,460),(1280,430)]
    d.polygon(near + [(1280, H), (0, H)], fill=C['forest'])
    for _ in range(120):
        x = random.randint(0, W)
        y = random.randint(410, H)
        r = random.randint(12, 35)
        rc = random.choice([C['red_leaf'], (200, 60, 35), C['orange_leaf'], (220, 90, 45), C['gold']])
        d.ellipse([x-r, y-r*0.75, x+r, y+r*0.75], fill=rc)
    try:
        fnt = ImageFont.truetype('msyh.ttc', 28)
        d.text((20, H-45), "万山红遍 · 层林尽染", fill=(255,255,255,200), font=fnt)
    except: pass
    _save(img, 'red_mountains.jpg')

# ====================================================================
# 3. 漫江碧透 — 碧绿江水 + 倒影
# ====================================================================
def gen_green_river():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    # 天空
    _grad(d, 0, H * 0.38, (170, 200, 220), (210, 230, 240))
    # 远岸
    d.polygon([(0,280),(200,250),(500,270),(800,255),(1100,275),(1280,260),(1280,340),(0,340)],
              fill=(100, 120, 85))
    # 江水主体（碧绿色）
    _grad(d, 330, H, (80, 160, 150), (50, 125, 130))
    # 波光
    for _ in range(40):
        x = random.randint(0, W)
        y = random.randint(350, H-20)
        w = random.randint(30, 120)
        d.ellipse([x, y, x+w, y+3], fill=(140, 200, 195))
    # 几艘船的远景剪影
    boats_data = [(200, 400, 60, 18), (500, 450, 80, 22), (850, 380, 55, 15), (1050, 470, 70, 20)]
    for bx, by, bw, bh in boats_data:
        d.polygon([(bx, by), (bx+bw//2, by-bh), (bx+bw, by)], fill=(50, 70, 60))
    try:
        fnt = ImageFont.truetype('msyh.ttc', 28)
        d.text((W-220, H-45), "漫江碧透 · 百舸争流", fill=(255,255,255,180), font=fnt)
    except: pass
    _save(img, 'green_river.jpg')

# ====================================================================
# 4. 鹰击长空 — 雄鹰翱翔剪影
# ====================================================================
def gen_eagle():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    # 天空渐变
    _grad(d, 0, H, (100, 140, 180), (180, 200, 220))
    # 薄云
    for _ in range(8):
        cx = random.randint(100, W-100)
        cy = random.randint(50, 300)
        rx, ry = random.randint(80, 200), random.randint(25, 50)
        d.ellipse([cx-rx, cy-ry, cx+rx, cy+ry], fill=(255,255,255,40))
    # 雄鹰剪影（展翅俯冲姿态）
    ex, ey = 640, 300  # 鹰的中心位置
    # 身体
    d.polygon([(ex-15, ey-25), (ex+15, ey-25), (ex+20, ey+35), (ex-20, ey+35)], fill=C['ink'])
    # 头
    d.polygon([(ex-8, ey-30), (ex+8, ey-30), (ex+12, ey-18), (ex-12, ey-18)], fill=C['ink'])
    # 尾羽（展开）
    d.polygon([(ex-5, ey+35), (ex+5, ey+35), (ex+18, ey+60), (ex-18, ey+60)], fill=C['ink'])
    # 左翅（大翅膀展开向上）
    d.polygon([(ex-15, ey-20), (ex-180, ey-120), (ex-150, ey-100), (ex-12, ey-5)], fill=C['ink'])
    # 右翅
    d.polygon([(ex+15, ey-20), (ex+180, ey-120), (ex+150, ey-100), (ex+12, ey-5)], fill=C['ink'])
    # 翅膀羽毛纹理（高光线）
    for i in range(4):
        off = 20 + i * 35
        d.line([(ex-18-off*0.5, ey-18-off*0.6), (ex-160+off, ey-115+off*0.2)],
               fill=(80, 100, 120), width=2)
        d.line([(ex+18+off*0.5, ey-18-off*0.6), (ex+160-off, ey-115+off*0.2)],
               fill=(80, 100, 120), width=2)
    try:
        fnt = ImageFont.truetype('msyh.ttc', 32)
        d.text((W//2-100, H-60), "鹰击长空", fill=C['ink'], font=fnt)
    except: pass
    _save(img, 'eagle.jpg')

# ====================================================================
# 5. 鱼翔浅底 — 清澈水中游鱼
# ====================================================================
def gen_fish():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    # 水体渐变（浅→深）
    _grad(d, 0, H, (120, 180, 175), (40, 95, 100))
    # 光柱从水面射入
    for i in range(6):
        cx = 150 + i * 200
        pts = [(cx-30, 0), (cx+30, 0), (cx+80, H), (cx-80, H)]
        for j in range(len(pts)-1):
            d.line([pts[j], pts[j+1]], fill=(150, 200, 195, 30), width=2)
    # 水底（浅色沙石）
    d.ellipse([100, H-150, W-100, H+50], fill=(180, 170, 155))
    # 水草
    for _ in range(15):
        sx = random.randint(50, W-50)
        sy = H - random.randint(20, 120)
        sw = [sx]
        shs = [sy]
        for _ in range(5):
            sw.append(sw[-1] + random.randint(-15, 15))
            shs.append(shs[-1] - random.randint(15, 35))
        d.line(list(zip(sw, shs)), fill=(60, 110, 60), width=3)
    # 游鱼（多条，表现"翔"的自由姿态）
    fish_list = [
        (550, 350, 1, 1.0),   # 主鱼（大，朝右游）
        (300, 450, -1, 0.6),  # 小鱼左游
        (800, 500, 1, 0.5),   # 小鱼右游
        (180, 520, 1, 0.4),   # 更小
        (1000, 380, -1, 0.55),
    ]
    for fx, fy, fd, fscale in fish_list:
        fw, fh = int(140 * fscale), int(55 * fscale)
        if fd < 0:
            fx -= fw
        # 鱼身（椭圆）
        d.ellipse([fx, fy-fh//2, fx+fw, fy+fh//2], fill=(200, 160, 90))
        # 尾巴
        if fd > 0:
            d.polygon([(fx, fy), (fx-25*fscale, fy-20*fscale), (fx-25*fscale, fy+20*fscale)],
                      fill=(200, 160, 90))
        else:
            d.polygon([(fx+fw, fy), (fx+fw+25*fscale, fy-20*fscale), (fx+fw+25*fscale, fy+20*fscale)],
                      fill=(200, 160, 90))
        # 背鳍
        d.polygon([(fx+fw*0.3, fy-fh//2), (fx+fw*0.4, fy-fh*0.8), (fx+fw*0.55, fy-fh//2)],
                  fill=(170, 130, 70))
        # 眼睛
        ex = (fx + fw*0.7) if fd > 0 else (fx + fw*0.3)
        d.ellipse([ex-4*fscale, fy-5*fscale, ex+4*fscale, fy+5*fscale], fill=(40, 40, 40))
    # 气泡
    for _ in range(12):
        bx = random.randint(200, W-200)
        by = random.randint(200, H-100)
        br = random.randint(3, 8)
        d.ellipse([bx-br, by-br, bx+br, by+br], outline=(200, 230, 230))
    try:
        fnt = ImageFont.truetype('msyh.ttc', 32)
        d.text((W//2-100, H-60), "鱼翔浅底", fill=(255,255,255,200), font=fnt)
    except: pass
    _save(img, 'fish.jpg')

# ====================================================================
# 6. 百舸争流 — 多艘船竞渡
# ====================================================================
def gen_boats():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    _grad(d, 0, H * 0.3, C['sky_top'], C['sky_bot'])
    # 江面
    _grad(d, 220, H, (70, 140, 145), (45, 110, 120))
    # 多艘帆船/木船，不同大小位置表现"竞"
    vessels = [
        (150, 320, 100, 55, (140, 100, 60)),   # 左侧大帆船
        (380, 400, 75, 40, (120, 85, 50)),
        (600, 280, 120, 65, (150, 105, 65)),    # 中间最大
        (820, 420, 65, 35, (130, 90, 55)),
        (1000, 350, 90, 48, (145, 100, 58)),    # 右侧
        (1100, 460, 55, 28, (115, 80, 48)),
    ]
    for vx, vy, vw, vh, vc in vessels:
        # 船身
        d.polygon([(vx, vy), (vx+vw*0.1, vy+vh), (vx+vw*0.9, vy+vh), (vx+vw, vy)], fill=vc)
        # 帆（三角形）
        sail_h = vh * 1.8
        d.polygon([(vx+vw*0.25, vy), (vx+vw*0.25, vy-sail_h), (vx+vw*0.7, vy)], fill=(245, 240, 225))
        # 帆的阴影线
        d.line([(vx+vw*0.25, vy), (vx+vw*0.7, vy)], fill=(200, 190, 170), width=2)
    # 浪花/波纹
    for _ in range(25):
        wx = random.randint(0, W)
        wy = random.randint(280, H)
        ww = random.randint(20, 60)
        d.arc([wx, wy, wx+ww, wy+ww//3], 0, 180, fill=(180, 210, 210))
    try:
        fnt = ImageFont.truetype('msyh.ttc', 28)
        d.text((W-220, H-45), "百舸争流", fill=(255,255,255,180), font=fnt)
    except: pass
    _save(img, 'boats.jpg')

# ====================================================================
# 7. 中流击水 — 急流浪花
# ====================================================================
def gen_rapids():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    _grad(d, 0, H * 0.25, (100, 130, 160), (170, 185, 195))
    # 急流江水
    _grad(d, 180, H, (50, 105, 120), (30, 75, 90))
    # 激流线条（动感）
    for i in range(30):
        y = 200 + i * 18
        amp = 5 + (i % 3) * 4
        pts = []
        for x in range(0, W, 15):
            offset = amp * math.sin(x * 0.03 + i * 0.5)
            pts.append((x, y + offset))
        if len(pts) > 1:
            d.line(pts, fill=(90, 160, 165), width=2)
    # 大浪头
    wave_y = 380
    d.polygon([(0, wave_y+60), (200, wave_y), (500, wave_y+30), (800, wave_y-10),
               (1100, wave_y+20), (1280, wave_y+40), (1280, wave_y+80), (0, wave_y+80)],
              fill=(140, 195, 200))
    # 浪花白沫
    for _ in range(35):
        fx = random.randint(0, W)
        fy = random.randint(wave_y-10, wave_y+70)
        fr = random.randint(8, 25)
        d.ellipse([fx-fr, fy-fr*0.5, fx+fr, fy+fr*0.5], fill=(230, 242, 245))
    # 水花飞溅点
    for _ in range(20):
        sx = random.randint(100, W-100)
        sy = random.randint(wave_y-40, wave_y+10)
        sr = random.randint(3, 10)
        d.ellipse([sx-sr, sy-sr, sx+sr, sy+sr], fill=(255, 255, 255))
    try:
        fnt = ImageFont.truetype('msyh.ttc', 32)
        d.text((W//2-100, 30), "中流击水 · 浪遏飞舟", fill=(255,255,255,220), font=fnt)
    except: pass
    _save(img, 'rapids.jpg')

# ====================================================================
# 8. 中国秋景（替换美国科罗拉多）— 悲秋 vs 颂秋 对比页用
# ====================================================================
def gen_autumn_china():
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    # 秋日天空（偏暖色调）
    _grad(d, 0, H * 0.4, (180, 150, 130), (230, 210, 190))
    # 远山（水墨风格轮廓）
    mts = [(0, 260), (120, 220), (280, 245), (450, 210), (620, 235), (800, 200),
           (950, 225), (1120, 205), (1280, 240)]
    d.polygon(mts + [(1280, 360), (0, 360)], fill=(150, 130, 110))
    # 中景山坡（带红黄色秋叶）
    mids = [(0, 330), (200, 290), (450, 315), (700, 285), (950, 310), (1150, 295), (1280, 330)]
    d.polygon(mids + [(1280, H), (0, H)], fill=(130, 100, 70))
    for _ in range(100):
        x = random.randint(0, W)
        y = random.randint(285, H)
        r = random.randint(10, 30)
        rc = random.choice([C['red_leaf'], C['orange_leaf'], C['gold'], (190, 100, 50)])
        d.ellipse([x-r, y-r*0.7, x+r, y+r*0.7], fill=rc)
    # 近景：一株突出的大树（象征秋天）
    tx = 200
    # 树干
    d.polygon([(tx-15, H), (tx+15, H), (tx+8, H-200), (tx-10, H-200)], fill=(90, 65, 40))
    # 树冠（红色为主）
    for _ in range(80):
        angle = random.uniform(0, math.pi * 2)
        dist = random.uniform(0, 90)
        cx = tx + int(math.cos(angle) * dist)
        cy = int(H - 220 + math.sin(angle) * dist * 0.7)
        cr = random.randint(12, 28)
        crc = random.choice([C['red_leaf'], (210, 80, 40), C['orange_leaf'], (230, 140, 50), C['gold']])
        d.ellipse([cx-cr, cy-cr*0.7, cx+cr, cy+cr*0.7], fill=crc)
    # 地面落叶
    for _ in range(40):
        lx = random.randint(0, W)
        ly = random.randint(H-80, H+10)
        lr = random.randint(4, 12)
        lc = random.choice([C['red_leaf'], C['orangeleaf'] if False else C['gold'], C['orange_leaf']])
        d.ellipse([lx-lr, ly-lr//2, lx+lr, ly+lr//2], fill=lc)
    # 暮霭/雾气效果
    scrim = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    sd.rectangle([0, int(H*0.5), W, H], fill=(240, 235, 225, 80))
    img = img.convert('RGBA')
    img = Image.alpha_composite(img, scrim)
    try:
        fnt = ImageFont.truetype('msyh.ttc', 28)
        dd = ImageDraw.Draw(img)
        dd.text((W-250, H-45), "中国秋意 · 湘江之畔", fill=(80, 60, 50, 220), font=fnt)
    except: pass
    _save(img.convert('RGB'), 'autumn_china.jpg')


# ====================================================================
# RUN ALL
# ====================================================================
if __name__ == '__main__':
    print(f"Generating {W}x{H} images → {OUT}")
    gen_orange_isle()
    gen_red_mountains()
    gen_green_river()
    gen_eagle()
    gen_fish()
    gen_boats()
    gen_rapids()
    gen_autumn_china()
    print("\nAll done!")
