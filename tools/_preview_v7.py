# -*- coding: utf-8 -*-
"""Faithful PIL preview of the redesigned magazine v7 pages.
Uses the SAME coordinate math as _render_qyc_mag_v3.py so the user can
judge the real layout without opening PowerPoint."""
import os
from PIL import Image, ImageDraw, ImageFont

SRC = r'C:\Users\1\WorkBuddy\2026-07-08-15-47-48\miniprogram\classroom_images_v2'
OUT = r'C:\Users\1\WorkBuddy\2026-07-08-15-47-48\miniprogram\preview_v7'
os.makedirs(OUT, exist_ok=True)

DPI = 120
IN = DPI / 1.0
def px(inch): return int(round(inch * IN))

W = px(13.333); H = px(7.5); M = px(0.8); CW = W - 2 * M

PAPER = (244, 239, 230)
INK   = (28, 42, 51)
FROST = (178, 58, 42)
XIANG = (46, 125, 107)
MUTED = (107, 98, 88)
WHITE = (255, 255, 255)
GOLD  = (200, 168, 107)
SOFT  = (231, 223, 210)
LINE  = (232, 226, 217)
LREDC = (255, 204, 204)

FONT_HEI = r'C:\Windows\Fonts\msyh.ttc'
FONT_KAI = r'C:\Windows\Fonts\simkai.ttf'
FONT_FANG = r'C:\Windows\Fonts\simfang.ttf'

def f(size_pt, path=FONT_HEI, idx=0):
    return ImageFont.truetype(path, int(size_pt * DPI / 72), index=idx)

def new_page():
    img = Image.new('RGB', (W, H), PAPER)
    return img, ImageDraw.Draw(img)

def rr(d, x, y, w, h, r, fill, outline=None, width=1):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill,
                         outline=outline, width=width)

def rect(d, x, y, w, h, fill):
    d.rectangle([x, y, x + w, y + h], fill=fill)

def circle(d, cx, cy, r, fill):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)

def text_c(d, s, cx, cy, font, fill):
    d.text((cx, cy), s, font=font, fill=fill, anchor='mm')

def text_l(d, s, x, y, font, fill):
    d.text((x, y), s, font=font, fill=fill)

def kicker(d, s, x=M, y=M, color=FROST):
    d.rectangle([x, y + px(0.05), x + px(0.35), y + px(0.16)], fill=color)
    d.text((x + px(0.45), y), s, font=f(12), fill=color)

def headline(d, s, x=M, y=M + px(0.65), size=26):
    d.text((x, y), s, font=f(size, FONT_HEI), fill=INK)

def paste_photo(d, path, x, y, w, h):
    im = Image.open(path).convert('RGB')
    im = im.resize((w, h))
    base = Image.new('RGB', (w + 4, h + 4), LINE)
    base.paste(im, (2, 2))
    return base

# ---------------------------------------------------------------- Slide 8
def slide_reading_guide():
    img, d = new_page()
    kicker(d, '朗读 · 指导')
    headline(d, '字音 · 节拍 · 情感')
    labels = ['字音', '节拍', '情感', '建议']
    colors = [FROST, XIANG, GOLD, INK]
    contents = [
        '舸 gě　寥 liáo　廓 kuò　怅 chàng　稠 chóu　遒 qiú　遏 è',
        '上阕“看”字领起，一气读到底；下阕“忆”字领起，渐入昂扬。',
        '上阕由景生情，由豪转怅；下阕由忆生志，愈读愈壮。',
        '先齐读把握节奏，再分角色读出“问”与“答”的气势。',
    ]
    card_y = M + px(1.25); card_h = px(1.05); gap = px(0.16)
    for idx in range(4):
        bar_w = px(0.1)
        rect(d, M, card_y, bar_w, card_h, colors[idx])
        rr(d, M + bar_w, card_y, CW - bar_w, card_h, 8, WHITE, LINE, 1)
        cx = M + bar_w + px(0.22) + px(0.19)
        cy = card_y + card_h / 2
        circle(d, cx, cy, px(0.19), colors[idx])
        text_c(d, '%02d' % (idx + 1), cx, cy, f(15), WHITE)
        lx = M + bar_w + px(0.38) + px(0.4)
        text_l(d, labels[idx], lx, card_y + px(0.18), f(17, FONT_HEI), colors[idx])
        text_l(d, contents[idx], lx, card_y + px(0.56), f(13.5, FONT_KAI), INK)
        card_y += card_h + gap
    img.save(os.path.join(OUT, 'p08_reading.png'))

# ---------------------------------------------------------------- Slide 26
def slide_exercise():
    img, d = new_page()
    kicker(d, '作业 · 分层')
    headline(d, '课后任务')
    cards = [
        ('01', '基础', FROST, '背诵全词，默写上阕；解释“击、翔、竞”的妙处。'),
        ('02', '提高', XIANG, '对比“悲秋”与“颂秋”的写法，写 200 字短评。'),
        ('03', '拓展', INK,  '以“我眼中的秋天”为题，用至少两个意象表达情感。'),
    ]
    card_y = M + px(1.4); card_h = px(1.25); gap = px(0.22)
    for num, label, color, content in cards:
        bar_w = px(0.12)
        rect(d, M, card_y, bar_w, card_h, color)
        rr(d, M + bar_w, card_y, CW - bar_w, card_h, 8, WHITE, LINE, 1)
        cx = M + bar_w + px(0.28) + px(0.18)
        cy = card_y + card_h / 2
        circle(d, cx, cy, px(0.18), color)
        text_c(d, num, cx, cy, f(16), WHITE)
        lx = M + bar_w + px(0.36) + px(0.45)
        text_l(d, label, lx, card_y + px(0.18), f(17, FONT_HEI), color)
        text_l(d, content, lx, card_y + px(0.58), f(14, FONT_KAI), INK)
        card_y += card_h + gap
    tip_y = H - px(0.95)
    rr(d, M, tip_y, CW, px(0.62), 8, SOFT)
    d.text((W / 2, tip_y + px(0.31)), '( 参考答案随教师版详案发放 )',
           font=f(13, FONT_KAI), fill=MUTED, anchor='mm')
    img.save(os.path.join(OUT, 'p26_exercise.png'))

# ---------------------------------------------------------------- Slide 25
def slide_board():
    img, d = new_page()
    kicker(d, '板书 · 结构')
    headline(d, '板书设计 · 词脉结构')
    col_labels = ['层面', '上阕（景）', '下阕（情）']
    col_x = [M, M + px(1.5), M + int(CW * 0.48)]
    col_w = [px(1.35), int(CW * 0.46), W - col_x[2] - M]
    label_y = M + px(1.35)
    for i, lbl in enumerate(col_labels):
        if i == 0:
            d.text((col_x[i] + col_w[i] / 2, label_y + px(0.19)), lbl,
                   font=f(12, FONT_HEI), fill=MUTED, anchor='mm')
        else:
            d.text((col_x[i], label_y + px(0.19)), lbl,
                   font=f(12, FONT_HEI), fill=MUTED, anchor='lm')
    rows = [
        ['起', '独立寒秋·橘子洲头', '携来百侣·曾游'],
        ['展', '万山·漫江·百舸·鹰鱼', '同学少年·风华正茂'],
        ['合', '怅寥廓·谁主沉浮', '到中流击水·浪遏飞舟'],
        ['法', '借景抒情', '叙议结合·用典'],
    ]
    rcolors = [FROST, XIANG, GOLD, INK]
    card_top = label_y + px(0.5); card_h = px(0.92); gap = px(0.14)
    for r_idx, (badge, c1, c2) in enumerate(rows):
        y = card_top + r_idx * (card_h + gap)
        acc_w = px(0.1)
        rect(d, M, y, acc_w, card_h, rcolors[r_idx])
        rr(d, M + acc_w, y, CW - acc_w, card_h, 8, WHITE, LINE, 1)
        csz = px(0.52)
        ccx = M + acc_w + (col_w[0] - csz) / 2 + csz / 2
        ccy = y + card_h / 2
        circle(d, ccx, ccy, csz / 2, rcolors[r_idx])
        text_c(d, badge, ccx, ccy, f(18, FONT_KAI), WHITE)
        text_l(d, c1, col_x[1] + px(0.08), y + px(0.22), f(14, FONT_KAI), INK)
        text_l(d, c2, col_x[2] + px(0.08), y + px(0.22), f(14, FONT_HEI), INK)
    img.save(os.path.join(OUT, 'p25_board.png'))

# ---------------------------------------------------------------- Slide 19
def slide_keyword():
    img, d = new_page()
    kicker(d, '炼字 · 竞')
    char_w = px(2.8)
    cy_box = M + px(1.0); ch_box = px(4.0)
    rr(d, M, cy_box, char_w, ch_box, 10, FROST)
    text_c(d, '竞', M + char_w / 2, cy_box + px(2.0), f(120, FONT_KAI), WHITE)
    d.text((M + char_w / 2, cy_box + px(3.4)), '“万类霜天竞自由”',
           font=f(13, FONT_KAI), fill=LREDC, anchor='mm')
    rx = M + char_w + px(0.5); rw = W - rx - M
    qb_h = px(0.85)
    rr(d, rx, M + px(1.0), rw, qb_h, 8, SOFT)
    rect(d, rx, M + px(1.0), px(0.08), qb_h, GOLD)
    d.text((rx + px(0.25), M + px(1.45)), '万类霜天竞自由',
           font=f(17, FONT_KAI), fill=INK, anchor='lm')
    analysis = [
        '“竞”者，竞相、争着也。',
        '红叶、碧水、百舸、雄鹰、游鱼——万物都在霜天里竞相生长。',
        '一个“竞”字，把静态的秋景写成了一部生命的交响。',
        '由“竞自由”自然过渡到“问苍茫大地，谁主沉浮”。',
    ]
    card_top = M + px(2.05); card_h = px(0.88); gap = px(0.12)
    for idx, line in enumerate(analysis):
        y = card_top + idx * (card_h + gap)
        col = XIANG if idx < len(analysis) - 1 else INK
        cr = px(0.21)
        circle(d, rx + px(0.05) + cr, y + card_h / 2, cr, col)
        text_c(d, str(idx + 1), rx + px(0.05) + cr, y + card_h / 2, f(14), WHITE)
        text_l(d, line, rx + px(0.58), y + px(0.2), f(14, FONT_KAI), INK)
    img.save(os.path.join(OUT, 'p19_keyword.png'))

# ---------------------------------------------------------------- Slide 5
def slide_timeline():
    img, d = new_page()
    kicker(d, '背景 · 1925')
    headline(d, '一首词里的时代')
    pw = px(4.8)
    ph = px(3.8)
    base = paste_photo(d, os.path.join(SRC, 'autumn_china.jpg'), M, M + px(1.4), pw, ph)
    img.paste(base, (M, M + px(1.4)))
    d.text((M, M + px(5.25)), '秋日的湘江畔，正是写词之地',
           font=f(11, FONT_HEI), fill=MUTED)
    events = [
        '1925 年，国共第一次合作展开，工农运动兴起。',
        '毛泽东回湖南考察农民运动，目睹民众觉醒的力量。',
        '同年秋，他重游橘子洲，写下这首《沁园春·长沙》。',
        '词中“问苍茫大地，谁主沉浮”，正是对时代之问的豪迈回应。',
    ]
    rx = M + pw + px(0.45); rw = W - rx - M
    tcolors = [FROST, XIANG, GOLD, INK]
    card_h = px(0.85); gap = px(0.12)
    for idx, ev in enumerate(events):
        y = M + px(1.4) + idx * (card_h + gap)
        circle(d, rx + px(0.15), y + card_h / 2, px(0.15), tcolors[idx])
        if idx < len(events) - 1:
            rect(d, rx + px(0.15) - px(0.02), y + card_h / 2 + px(0.15),
                 px(0.04), card_h + gap - px(0.3), SOFT)
        rr(d, rx + px(0.45), y, rw - px(0.45), card_h, 8, WHITE, LINE, 1)
        d.text((rx + px(0.58), y + px(0.18)), ev,
               font=f(13.5, FONT_KAI), fill=INK)
    img.save(os.path.join(OUT, 'p05_background.png'))

slide_reading_guide()
slide_exercise()
slide_board()
slide_keyword()
slide_timeline()
print('PREVIEW OK ->', OUT)
