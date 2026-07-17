# -*- coding: utf-8 -*-
"""生成语文课媒体（与英语 pilot 同构，纯手绘无 AI 水印）：
- 橘子洲秋景图 jpg（扁平编辑风插画）
- 占位朗诵音频 wav（方明版名家朗诵的占位，待替换真源）
输出到 subpackages/cn/images/lessons/<id>/ ，镜像英语结构。
"""
import os, struct, math, wave
from PIL import Image, ImageDraw, ImageFont

LESSON_ID = 'l-cn-bs-u1-1'
OUT_DIR = os.path.join('subpackages', 'cn', 'images', 'lessons', LESSON_ID)
os.makedirs(OUT_DIR, exist_ok=True)

# ---- 橘子洲秋景插画 ----
CW, CH = 960, 600
im = Image.new('RGB', (CW, CH), (245, 241, 233))
d = ImageDraw.Draw(im)

# 天空：暖色渐变（上浅下暖）
for y in range(CH):
    t = y / CH
    r = int(238 + (247 - 238) * 0 + 9 * t)
    g = int(236 + (235 - 236) * 0 + 6 * t)
    b = int(230 + (224 - 230) * 0 + 8 * t)
    # 简单两段渐变
    if y < CH * 0.62:
        r = int(242 - 14 * (y / (CH * 0.62)))
        g = int(240 - 12 * (y / (CH * 0.62)))
        b = int(234 - 8 * (y / (CH * 0.62)))
    else:
        r = int(228 + 10 * ((y - CH * 0.62) / (CH * 0.38)))
        g = int(228 + 6 * ((y - CH * 0.62) / (CH * 0.38)))
        b = int(226 + 4 * ((y - CH * 0.62) / (CH * 0.38)))
    d.line([(0, y), (CW, y)], fill=(max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))))

# 远山：三层秋色丘陵
def hill(base_y, amp, color, step=40):
    pts = [(0, CH)]
    x = 0
    phase = 0.0
    while x <= CW:
        y = base_y + math.sin((x / CW) * math.pi * 2 + phase) * amp + math.sin((x / CW) * math.pi * 6) * (amp * 0.25)
        pts.append((x, int(y)))
        x += step
    pts.append((CW, CH))
    d.polygon(pts, fill=color)

hill(int(CH * 0.40), 34, (196, 150, 120))   # 最远 暖褐
hill(int(CH * 0.50), 40, (183, 120, 86))    # 中 陶土
hill(int(CH * 0.60), 30, (168, 96, 66))     # 近 深陶土

# 湘江水面
water_top = int(CH * 0.66)
d.rectangle([0, water_top, CW, CH], fill=(120, 158, 168))
# 水面横向波纹
for i in range(7):
    yy = water_top + 18 + i * 22
    d.line([(0, yy), (CW, yy)], fill=(138, 174, 182), width=2)
# 水面倒影（山的暖色竖条）
for x in range(0, CW, 26):
    d.line([(x, water_top), (x, water_top + 26)], fill=(176, 132, 104), width=3)

# 飞雁（人字形）
def goose(cx, cy, s=1.0, col=(60, 70, 78)):
    d.line([(cx - int(14 * s), cy), (cx, cy - int(7 * s))], fill=col, width=3)
    d.line([(cx, cy - int(7 * s)), (cx + int(14 * s), cy)], fill=col, width=3)
goose(180, 120, 1.1)
goose(230, 138, 0.9)
goose(285, 126, 1.0)
goose(150, 160, 0.8)

# 一棵红枫剪影（右侧近岸）
def tree(cx, base_y):
    d.rectangle([cx - 6, base_y - 150, cx + 6, base_y], fill=(92, 64, 48))
    # 树冠：几团秋红
    crown = [(cx - 60, base_y - 150, 70, (196, 92, 60)),
             (cx + 10, base_y - 170, 60, (210, 110, 66)),
             (cx - 20, base_y - 190, 56, (186, 80, 54))]
    for (ex, ey, er, c) in crown:
        d.ellipse([ex, ey, ex + er * 2, ey + er * 2], fill=c)
tree(CW - 130, water_top + 4)

# 落款（右下小字，非水印，设计稿署名感）
d.text((CW - 180, CH - 34), '橘子洲 · 秋', font=ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 20), fill=(96, 110, 117))

jpg_path = os.path.join(OUT_DIR, 'juzizhou.jpg')
im.save(jpg_path, 'JPEG', quality=82, optimize=True)
print('橘子洲秋景图 ->', jpg_path, os.path.getsize(jpg_path) // 1024, 'KB')

# ---- 占位朗诵音频 wav（2 秒，双频叠加，可播放占位）----
def make_wav(path, seconds=2.0, sr=8000):
    n = int(seconds * sr)
    frames = bytearray()
    for i in range(n):
        t = i / sr
        # 440 + 660 Hz 轻叠加，模拟"有声音"
        v = int(0.25 * 32767 * (math.sin(2 * math.pi * 440 * t) + 0.6 * math.sin(2 * math.pi * 660 * t)))
        v = max(-32768, min(32767, v))
        frames += struct.pack('<h', v)
    with wave.open(path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(bytes(frames))
    print('占位朗诵音频 ->', path, os.path.getsize(path) // 1024, 'KB')

wav_path = os.path.join(OUT_DIR, 'recitation.wav')
make_wav(wav_path)
print('媒体目录:', OUT_DIR)
