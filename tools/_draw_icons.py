"""PIL 手绘 4 个扁平教学图标（800x800，无水印、风格统一、教育主题色）。"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = r'C:\Users\1\WorkBuddy\2026-07-08-15-47-48\miniprogram\subpackages\eng\images\lessons\l-eng-b1-u2-ls'
os.makedirs(OUT, exist_ok=True)

# 统一配色（教育蓝主题）
BG = (245, 247, 250)         # 浅灰蓝背景
PRIM = (37, 99, 235)         # 主色：教育蓝
ACCENT = (251, 146, 60)      # 强调：暖橙
DARK = (30, 41, 59)          # 文字：深蓝灰
WHITE = (255, 255, 255)
LIGHT = (219, 234, 254)      # 浅蓝
GOLD = (234, 179, 8)         # 金色（护照国徽用）
RED = (220, 38, 38)          # 红色（护照用）

def setup(w=800, h=800):
    im = Image.new('RGB', (w, h), BG)
    d = ImageDraw.Draw(im)
    # 圆角背景框
    d.rounded_rectangle([40, 40, w-40, h-40], radius=48, fill=WHITE, outline=LIGHT, width=3)
    return im, d

def draw_passport():
    im, d = setup()
    # 护照本体（暗红圆角）
    d.rounded_rectangle([240, 160, 560, 660], radius=24, fill=RED, outline=DARK, width=3)
    # 顶部装饰条
    d.rectangle([240, 160, 560, 200], fill=GOLD)
    # 国徽简化：大五角星 + 4 小五角星 + 天安门 + 齿轮 + 麦穗轮廓
    cx, cy = 400, 410
    # 大五角星
    import math
    def star(cx, cy, r, points=5, fill=GOLD):
        pts = []
        for i in range(points*2):
            ang = -math.pi/2 + i*math.pi/points
            rr = r if i%2==0 else r*0.4
            pts.append((cx + rr*math.cos(ang), cy + rr*math.sin(ang)))
        d.polygon(pts, fill=fill)
    star(cx, cy-20, 50)
    # 4 个小五角星（弧形分布）
    for i, ang in enumerate([-50, -20, 20, 50]):
        sx = cx + 60*math.cos(math.radians(ang-90))
        sy = cy-20 + 60*math.sin(math.radians(ang-90))
        star(sx, sy, 14)
    # 天安门简化
    d.rectangle([cx-50, cy+50, cx+50, cy+90], fill=GOLD)
    d.rectangle([cx-60, cy+90, cx+60, cy+110], fill=GOLD)
    # 底部"中国"文字标识
    f1 = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 36)
    d.text((350, 600), 'CHINA', font=f1, fill=GOLD)
    im.save(os.path.join(OUT, 'passport.jpg'), 'JPEG', quality=85)
    return im.size

def draw_boardingpass():
    im, d = setup()
    # 登机牌主体（白纸+阴影+撕角）
    # 阴影
    d.rounded_rectangle([126, 186, 686, 624], radius=18, fill=(220,220,228))
    # 主体
    d.rounded_rectangle([120, 180, 680, 620], radius=18, fill=WHITE, outline=DARK, width=2)
    # 顶部蓝色 banner
    d.rectangle([120, 180, 680, 230], fill=PRIM)
    d.text((150, 188), 'BOARDING PASS', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 28), fill=WHITE)
    # 虚线分隔线
    for x in range(140, 670, 12):
        d.line([(x, 320), (x+6, 320)], fill=(180,180,190), width=2)
    # 信息网格
    f_label = ImageFont.truetype(r'C:/Windows/Fonts/arial.ttf', 18)
    f_value = ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 32)
    info = [
        (160, 260, 'PASSENGER', 'WANG / MR'),
        (160, 350, 'FLIGHT', 'FL 0123'),
        (380, 350, 'GATE', 'B12'),
        (160, 430, 'SEAT', '12A'),
        (380, 430, 'CLASS', 'ECON'),
    ]
    for x, y, lab, val in info:
        d.text((x, y), lab, font=f_label, fill=(120,120,135))
        d.text((x, y+22), val, font=f_value, fill=DARK)
    # 底部条形码（黑白条）
    bx, by = 160, 540
    for i, w in enumerate([3,2,1,2,3,1,2,1,3,2,1,2,3,1,2,3,2,1,2,1,3,2,1,2,3,1,2,3,2,1,2,3,1,2,1,2,3]):
        color = DARK if i%2==0 else WHITE
        d.rectangle([bx, by, bx+w, by+50], fill=color)
        bx += w + 2
    im.save(os.path.join(OUT, 'boardingpass.jpg'), 'JPEG', quality=85)
    return im.size

def draw_suitcase():
    im, d = setup()
    # 拉杆
    d.rectangle([388, 180, 412, 280], fill=DARK)
    d.rounded_rectangle([358, 160, 442, 200], radius=10, fill=DARK)
    # 主体（圆角矩形）
    d.rounded_rectangle([200, 280, 600, 660], radius=30, fill=PRIM, outline=DARK, width=3)
    # 中央分缝线
    d.line([(400, 290), (400, 650)], fill=DARK, width=3)
    # 提手
    d.rounded_rectangle([360, 270, 440, 295], radius=8, fill=DARK)
    # 行李牌（橙色，斜挂）
    d.polygon([(480, 380), (560, 360), (570, 430), (490, 450)], fill=ACCENT, outline=DARK)
    d.text((490, 395), 'PARIS', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 22), fill=WHITE)
    # 轮子
    d.ellipse([220, 660, 260, 700], fill=DARK)
    d.ellipse([540, 660, 580, 700], fill=DARK)
    im.save(os.path.join(OUT, 'suitcase.jpg'), 'JPEG', quality=85)
    return im.size

def draw_map():
    im, d = setup()
    # 折纸地图（米黄底）
    d.polygon([(160, 200), (640, 180), (660, 600), (180, 620)], fill=(253, 230, 196), outline=DARK, width=2)
    # 折痕
    d.line([(400, 190), (400, 610)], fill=(220, 200, 170), width=2)
    d.line([(170, 410), (650, 395)], fill=(220, 200, 170), width=2)
    # 陆地色块
    d.ellipse([220, 280, 380, 360], fill=(186, 230, 200), outline=(140, 200, 160))
    d.polygon([(420, 260), (580, 270), (560, 380), (440, 360)], fill=(186, 230, 200), outline=(140, 200, 160))
    d.polygon([(200, 440), (340, 430), (320, 560), (220, 560)], fill=(186, 230, 200), outline=(140, 200, 160))
    # 蓝色水域
    d.polygon([(180, 380), (300, 350), (280, 440), (190, 430)], fill=(180, 220, 240))
    d.polygon([(450, 400), (620, 400), (600, 540), (470, 540)], fill=(180, 220, 240))
    # 红色路线（折线）
    pts = [(240, 320), (320, 380), (380, 340), (450, 400), (520, 460), (560, 510)]
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=RED, width=6)
    for p in pts:
        d.ellipse([p[0]-8, p[1]-8, p[0]+8, p[1]+8], fill=RED, outline=WHITE, width=2)
    # 指南针
    cx, cy, r = 580, 240, 36
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=WHITE, outline=DARK, width=2)
    d.polygon([(cx, cy-r+6), (cx-8, cy), (cx, cy+r-6), (cx+8, cy)], fill=RED, outline=DARK)
    d.polygon([(cx, cy-r+6), (cx+8, cy), (cx, cy), (cx-8, cy)], fill=WHITE, outline=DARK)
    d.text((cx-6, cy-12), 'N', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 14), fill=DARK)
    im.save(os.path.join(OUT, 'map.jpg'), 'JPEG', quality=85)
    return im.size

# 全部生成
for fn, name in [(draw_passport, 'passport'),
                 (draw_boardingpass, 'boardingpass'),
                 (draw_suitcase, 'suitcase'),
                 (draw_map, 'map')]:
    sz = fn()
    p = os.path.join(OUT, name + '.jpg')
    print(f'{name}.jpg  {sz}  {os.path.getsize(p)//1024} KB')

# 清理 PNG 残留
for f in os.listdir(OUT):
    if f.endswith('.png'):
        os.remove(os.path.join(OUT, f))
print('PNG 残留已清理')

# 总大小
total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
print(f'子包媒体总大小: {total//1024} KB')
