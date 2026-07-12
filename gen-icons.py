# 生成精致描边风 tabBar 图标（矢量超采样抗锯齿）
from PIL import Image, ImageDraw

S = 4            # 超采样倍数
SIZE = 81        # 最终尺寸
B = SIZE * S     # 绘制尺寸
GRAY = (154, 161, 173, 255)     # #9aa1ad 未选中
BLUE = (26, 54, 93, 255)        # #1a365d 选中
LW = 11 * S      # 线宽（缩放后）

def canvas():
    return Image.new('RGBA', (B, B), (0, 0, 0, 0))

def save(img, path):
    img = img.resize((SIZE, SIZE), Image.LANCZOS)
    img.save(path)
    print('saved', path)

def home(color):
    img = canvas(); d = ImageDraw.Draw(img)
    cx = B // 2
    top = 46 * S
    eave = 120 * S
    left = 64 * S; right = B - 64 * S
    bottom = 250 * S
    # 屋顶
    d.line([(left, eave), (cx, top), (right, eave)], fill=color, width=LW, joint='curve')
    # 墙体
    d.line([(left, eave), (left, bottom), (right, bottom), (right, eave)],
           fill=color, width=LW, joint='curve')
    # 门
    dw = 34 * S
    dh = 64 * S
    d.rectangle([cx - dw, bottom - dh, cx + dw, bottom], outline=color, width=LW)
    return img

def star(color):
    img = canvas(); d = ImageDraw.Draw(img)
    cx = B // 2; cy = B // 2
    R = 100 * S; r = 42 * S
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = R if i % 2 == 0 else r
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.line(pts + [pts[0]], fill=color, width=LW, joint='curve')
    return img

def person(color):
    img = canvas(); d = ImageDraw.Draw(img)
    cx = B // 2
    head_r = 34 * S
    hy = 86 * S
    # 头
    d.ellipse([cx - head_r, hy - head_r, cx + head_r, hy + head_r], outline=color, width=LW)
    # 肩（下半椭圆弧）
    bx0 = cx - 78 * S; bx1 = cx + 78 * S
    by0 = hy + 36 * S; by1 = hy + 36 * S + 120 * S
    d.arc([bx0, by0, bx1, by1], 180, 360, fill=color, width=LW)
    return img

home(GRAY); save(home(GRAY), 'images/tabbar/home.png')
save(home(BLUE), 'images/tabbar/home-active.png')
save(star(GRAY), 'images/tabbar/star.png')
save(star(BLUE), 'images/tabbar/star-active.png')
save(person(GRAY), 'images/tabbar/person.png')
save(person(BLUE), 'images/tabbar/person-active.png')
print('done')
