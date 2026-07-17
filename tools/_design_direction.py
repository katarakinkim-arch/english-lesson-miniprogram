# -*- coding: utf-8 -*-
"""方向样张 v2：克制、有编辑设计感。输出 design_dir/ 5 张。"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
BG     = (247, 245, 240)   # 暖纸白 F7F5F0
INK    = (28, 43, 51)      # 墨蓝黑 1C2B33
SUB    = (96, 110, 117)    # 次级灰绿 606E75
ACCENT = (194, 112, 61)    # 陶土橙 C2703D（极度克制）
LINE   = (216, 209, 197)   # 细线 D8D1C5
CARD   = (255, 255, 255)
CARDL  = (226, 220, 208)   # 卡片边 E2DCD0
SOFT   = (238, 234, 226)   # 浅底 EEEAE2

F_LIGHT  = ImageFont.truetype(r'C:/Windows/Fonts/msyhl.ttc', 30)      # 雅黑 Light
F_REG    = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 20)       # 雅黑常规
F_REG_S  = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 16)
F_BOLD   = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 24)
F_BOLD_L = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 34)
F_TITLE  = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 46)
F_BIG    = ImageFont.truetype(r'C:/Windows/Fonts/msyhl.ttc', 150)      # 超大细体数字
F_EN     = ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 14)

OUT = 'design_dir'
os.makedirs(OUT, exist_ok=True)
M = ImageDraw.Draw  # placeholder

def new():
    return Image.new('RGB', (W, H), BG), ImageDraw.Draw(Image.new('RGB', (W, H)))

def txt(d, xy, s, font, fill, anchor=None):
    # 简易绘制（anchor 仅支持 None / 'mm'）
    if anchor == 'mm':
        w = d.textlength(s, font=font); h = font.size
        d.text((xy[0]-w/2, xy[1]-h/2), s, font=font, fill=fill)
    else:
        d.text(xy, s, font=font, fill=fill)

def header(d, left, right):
    txt(d, (70, 44), left, F_EN, SUB)
    rw = d.textlength(right, font=F_EN)
    d.text((W-70-rw, 44), right, font=F_EN, fill=SUB)
    d.line([(70, 70), (W-70, 70)], fill=LINE, width=1)

def footer(d, code, page, total):
    d.line([(70, H-58), (W-70, H-58)], fill=LINE, width=1)
    txt(d, (70, H-46), code, F_EN, SUB)
    p = f'{page:02d}  /  {total:02d}'
    pw = d.textlength(p, font=F_EN)
    d.text((W-70-pw, H-46), p, font=F_EN, fill=SUB)

def card(d, x, y, w, h, radius=10):
    d.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=CARD, outline=CARDL, width=1)

def left_rail(d, num, label, sub):
    # 左侧标识栏：超大细体数字 + 细竖线 + 小标签
    txt(d, (96, 130), num, F_BIG, (220, 216, 208))
    d.line([(180, 120), (180, 600)], fill=LINE, width=1)
    txt(d, (210, 150), label, F_BOLD_L, INK)
    if sub:
        txt(d, (210, 196), sub, F_REG_S, SUB)

# ---------------- 封面 ----------------
im, d = new()
header(d, 'ENGLISH  ·  人教版 2019', '必修一  UNIT 2')
txt(d, (96, 230), 'Travelling Around', F_TITLE, INK)
txt(d, (98, 300), '听说课  ·  Listening & Speaking', F_LIGHT, SUB)
d.rectangle([98, 346, 98+86, 346+4], fill=ACCENT)   # 细橙线
txt(d, (98, 380), '授课教师：_________      班级：__________', F_REG, SUB)
# 右下角细线标识框
bx, by, bw, bh = W-300, 470, 210, 170
d.rounded_rectangle([bx, by, bx+bw, by+bh], radius=12, outline=LINE, width=1)
txt(d, (bx+bw/2, by+58), 'U2', ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 60), (210,206,198), anchor='mm')
txt(d, (bx+bw/2, by+120), 'Travelling', F_REG_S, SUB, anchor='mm')
txt(d, (bx+bw/2, by+144), 'Around', F_REG_S, SUB, anchor='mm')
footer(d, 'l-eng-b1-u2-ls', 1, 16)
im.save(f'{OUT}/01_cover.png', 'PNG', optimize=True)

# ---------------- 目录 ----------------
im, d = new()
header(d, 'CONTENTS', '必修一  UNIT 2')
txt(d, (96, 130), '目录', F_BOLD_L, INK)
items = [('01', '课程概览', 'Overview'),
         ('02', '学习目标', 'Objectives'),
         ('03', '重点 · 难点', 'Key & Difficult'),
         ('04', '教学过程', '6 Steps'),
         ('05', '板书设计', 'Blackboard'),
         ('06', '作业 · 反思', 'Homework & Notes')]
x0, y0, cw, ch = 96, 210, 520, 150
gx, gy = 40, 26
for i, (n, zh, en) in enumerate(items):
    col = i % 2; row = i // 2
    x = x0 + col*(cw+gx); y = y0 + row*(ch+gy)
    card(d, x, y, cw, ch)
    d.rectangle([x, y, x+6, y+ch], fill=ACCENT)
    txt(d, (x+34, y+34), n, ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 40), (222,217,209))
    txt(d, (x+110, y+40), zh, F_BOLD, INK)
    txt(d, (x+110, y+82), en, F_REG_S, SUB)
footer(d, 'l-eng-b1-u2-ls', 2, 16)
im.save(f'{OUT}/02_contents.png', 'PNG', optimize=True)

# ---------------- 步骤页 (听前·激活) ----------------
im, d = new()
header(d, 'STEP 03 / 06', '教学过程')
left_rail(d, '03', '听前', 'Pre-listening')
txt(d, (210, 250), '激活背景知识，铺垫旅行词汇', F_BOLD_L, INK)
blocks = [
    ('教学活动', '展示目的地图片，引导学生用英语说出交通方式与必备物品'),
    ('教师台词', '“Look at the picture. How do you get there? What do you need to pack?”'),
    ('学生预期', '能说出 by train / by plane，并列举 suitcase, map, passport 等词汇'),
    ('时间安排', '约 6 分钟，小组接力发言，教师板书核心词汇'),
]
x, y, w = 210, 310, 1000
bh = 78; gap = 14
for title, body in blocks:
    card(d, x, y, w, bh)
    d.rectangle([x, y, x+5, y+bh], fill=ACCENT)
    txt(d, (x+26, y+12), title, F_BOLD, ACCENT)
    txt(d, (x+26, y+42), body, F_REG, INK)
    y += bh + gap
footer(d, 'l-eng-b1-u2-ls', 8, 16)
im.save(f'{OUT}/08_step3.png', 'PNG', optimize=True)

# ---------------- 板书页 ----------------
im, d = new()
header(d, 'BLACKBOARD', '板书设计')
bx, by, bw, bh = 96, 130, 1088, 520
d.rounded_rectangle([bx, by, bx+bw, by+bh], radius=14, fill=INK)
# 内部浅色板书
txt(d, (bx+40, by+34), 'Unit 2  Travelling Around', ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 26), (233, 237, 234))
d.line([(bx+40, by+78), (bx+bw-40, by+78)], fill=(70,86,94), width=1)
lines = [
    ('Key sentences', (198, 210, 166)),
    '  · — Where are you going?   — I\'m going to _______.',
    '  · — How are you getting there?   — By _______.',
    '  · — What are you doing there?   — I\'m _______.',
    '',
    ('Vocabulary', (198, 210, 166)),
    '  pack / suitcase / passport / boarding pass / map / visa',
    '  book / flight / hotel / camera / rent a car',
    '',
    ('Useful expression', (198, 210, 166)),
    '  make a travel plan   get around   places of interest',
]
yy = by + 96
for ln in lines:
    if isinstance(ln, tuple):
        txt(d, (bx+40, yy), ln[0], F_BOLD, ln[1]); yy += 38
    else:
        txt(d, (bx+40, yy), ln, F_REG, (220, 226, 222)); yy += 32
footer(d, 'l-eng-b1-u2-ls', 12, 16)
im.save(f'{OUT}/12_blackboard.png', 'PNG', optimize=True)

# ---------------- 作业页 ----------------
im, d = new()
header(d, 'HOMEWORK', '作业布置')
txt(d, (96, 130), '基础作业', F_BOLD_L, INK)
txt(d, (96, 176), '所有学生必做', F_REG_S, SUB)
# 左：基础  右：提高
cw, ch = 530, 470
card(d, 96, 220, cw, ch)
txt(d, (96+28, 248), '基础 · 巩固', F_BOLD, ACCENT)
base = ['1. 抄写本课 12 个核心词汇各 2 行',
        '2. 用 3 句话写“我的周末旅行计划”',
        '3. 完成练习册 P23 听力填空']
yy = 300
for t in base:
    d.ellipse([96+30, yy+6, 96+38, yy+14], fill=ACCENT)
    txt(d, (96+52, yy), t, F_REG, INK); yy += 40

card(d, 96+cw+44, 220, cw, ch)
txt(d, (96+cw+44+28, 248), '提高 · 拓展', F_BOLD, ACCENT)
adv = ['1. 录制一段 1 分钟“旅行 Vlog”英文旁白',
       '2. 用目标句型采访一位同学并写报告',
       '3. 查阅目的地文化习俗，做海报']
yy = 300
for t in adv:
    d.ellipse([96+cw+44+30, yy+6, 96+cw+44+38, yy+14], fill=ACCENT)
    txt(d, (96+cw+44+52, yy), t, F_REG, INK); yy += 40
footer(d, 'l-eng-b1-u2-ls', 13, 16)
im.save(f'{OUT}/13_homework.png', 'PNG', optimize=True)

print('方向样张已生成:', os.listdir(OUT))
