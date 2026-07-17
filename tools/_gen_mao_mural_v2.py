# -*- coding: utf-8 -*-
"""生成「形象·同学少年」页左侧替换图 — 干净书法风格（替换原来杂乱的 mao_mural.jpg）
输出：classroom_images_v2/mao_mural_v2.jpg  (800x950 px, JPEG quality=88)
"""
from PIL import Image, ImageDraw, ImageFont
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, 'classroom_images_v2', 'mao_mural_v2.jpg')
FONT_DIR = r'C:\Windows\Fonts'

W, H = 800, 950

# --- colors ---
PAPER   = (0xF4, 0xEF, 0xE6)
INK     = (0x1C, 0x2A, 0x33)
FROST   = (0xB2, 0x3A, 0x2A)    # seal red
XIANG   = (0x2E, 0x7D, 0x6B)    # lake green
MUTED   = (0x6B, 0x62, 0x58)
GOLD    = (0xC8, 0xA8, 0x6B)
SOFT2    = (0xE7, 0xDF, 0xD2)

img = Image.new('RGB', (W, H), PAPER)
draw = ImageDraw.Draw(img)

# ---- 背景纹理：左上角淡淡斜线装饰（杂志风）----
for i in range(0, 300, 16):
    draw.line([(i, 0), (i + 120, 300)], fill=(0xDD, 0xD5, 0xCA), width=1)

# ---- 底部山/水形（极简）----
# 远山 — 两层淡绿
draw.polygon([
    (0, H - 180), (100, H - 320), (220, H - 240),
    (340, H - 350), (480, H - 260), (600, H - 330),
    (720, H - 250), (W, H - 200), (W, H), (0, H)
], fill=(0xC5, 0xDB, 0xD2))

# 近水 — 湘江感，底部横条
draw.rectangle([0, H - 90, W, H], fill=(0xA8, 0xCE, 0xC3))
# 波纹线
for row in range(3):
    y_base = H - 70 + row * 22
    pts = []
    for x in range(0, W + 20, 20):
        import math
        yy = y_base + int(4 * math.sin(x * 0.04 + row * 1.5))
        pts.append((x, yy))
    if len(pts) > 1:
        draw.line(pts, fill=(0x8B, 0xBC, 0xB1), width=1)

# ---- 竖排主标题「恰同学少年」----
try:
    font_big = ImageFont.truetype(os.path.join(FONT_DIR, 'simkai.ttf'), 86)
    font_mid = ImageFont.truetype(os.path.join(FONT_DIR, 'simkai.ttf'), 52)
    font_small = ImageFont.truetype(os.path.join(FONT_DIR, 'msyh.ttc'), 18)
except OSError:
    font_big = ImageFont.load_default()
    font_mid = font_big
    font_small = font_big

main_chars = '恰同学少年'
char_x = W // 2 - 30   # 稍偏右，给左边留红点空间
char_y_start = 100
line_spacing = 98

for i, ch in enumerate(main_chars):
    cy = char_y_start + i * line_spacing
    # 字阴影（微微偏右下）
    draw.text((char_x + 2, cy + 2), ch, fill=(0xCC, 0xC8, 0xC0), font=font_big)
    # 墨字
    draw.text((char_x, cy), ch, fill=INK, font=font_big)

# ---- 左侧竖排副标「风华正茂」----
sub_chars = '风华正茂'
sub_x = char_x - 90
sub_y_start = 160
sub_spacing = 64
for i, ch in enumerate(sub_chars):
    cy = sub_y_start + i * sub_spacing
    draw.text((sub_x, cy), ch, fill=XIANG, font=font_mid)

# ---- 右侧竖排小注「挥斥方遒」----
note_chars = '挥斥方遒'
note_x = char_x + 95
note_y_start = 200
note_spacing = 50
for i, ch in enumerate(note_chars):
    cy = note_y_start + i * note_spacing
    draw.text((note_x, cy), ch, fill=MUTED, font=font_mid)

# ---- 红色印章点缀（传统篆刻感，3-4个）----
seal_positions = [
    (55, 150, 28),   # 左上圆印
    (75, 520, 22),   # 中左小印
    (680, 420, 26),  # 右侧印
    (620, 650, 18),  # 右下小印
]
for sx, sy, sr in seal_positions:
    # 圆形印章底
    draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], outline=FROST, width=2)
    # 内部填充半透明红
    overlay = Image.new('RGBA', (sr*2+4, sr*2+4), (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([2, 2, sr*2+2, sr*2+2], fill=(*FROST, 40))
    img.paste(overlay.convert('RGB'), (sx-sr-2, sy-sr-2), overlay.convert('RGBA'))

# ---- 底部引文条（浅色横幅）----
banner_y = H - 140
draw.rectangle([40, banner_y, W - 40, banner_y + 38], fill=SOFT2)
try:
    font_quote = ImageFont.truetype(os.path.join(FONT_DIR, 'msyh.ttc'), 15)
except OSError:
    font_quote = font_small
quote_text = '书生意气  挥斥方遒  指点江山  激扬文字'
bbox = draw.textbbox((0, 0), quote_text, font=font_quote)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, banner_y + 10), quote_text, fill=MUTED, font=font_quote)

# ---- 保存 ----
img.save(OUT, 'JPEG', quality=88)
print(f'OK -> {OUT} ({img.size[0]}x{img.size[1]})')
