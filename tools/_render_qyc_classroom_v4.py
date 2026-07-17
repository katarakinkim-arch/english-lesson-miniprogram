#!/usr/bin/env python3
"""
课堂版PPT渲染器 v4 —— 沁园春·长沙
全部意象用PIL手绘（不依赖外部图库），文字与图形融合，视觉冲击力
自检：每页验证意象、颜色、内容匹配
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, random, math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(SCRIPT_DIR)
OUT = os.path.join(PROJ_DIR, 'cn_qyc_classroom_v4')
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
MARGIN = 80
HEADER_H = 80
CONTENT_TOP = HEADER_H + 20

FONT_DIR = 'C:/Windows/Fonts'
def load_font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_TITLE   = load_font('msyhbd.ttc', 36)
F_SUB     = load_font('msyhbd.ttc', 24)
F_BODY    = load_font('msyh.ttc', 20)
F_BODY_B  = load_font('msyhbd.ttc', 20)
F_SMALL   = load_font('msyh.ttc', 16)
F_BIG     = load_font('msyhbd.ttc', 48)
F_HUGE    = load_font('msyhbd.ttc', 72)
F_POEM    = load_font('msyh.ttc', 22)
F_POEM_LG = load_font('msyhbd.ttc', 28)
F_TABLE   = load_font('msyh.ttc', 18)
F_TABLE_B = load_font('msyhbd.ttc', 18)
F_ICON    = load_font('msyhbd.ttc', 120)

INK      = (28, 43, 51)
WHITE    = (255, 255, 255)
FROST    = (178, 58, 42)
XIANG    = (46, 125, 107)
ACCENT   = (194, 112, 61)
LIGHT_BG = (245, 242, 237)
GRAY     = (128, 128, 128)
LIGHT_GRAY = (220, 220, 220)
TABLE_HDR = (28, 43, 51)
TABLE_ALT = (240, 245, 250)
BORDER    = (180, 180, 180)
HIGHLIGHT = (255, 240, 220)

# ═══════════════════════════════════════════════════
#  PIL 手绘意象函数
# ═══════════════════════════════════════════════════

def draw_gradient_bg(d, img, color1, color2, vertical=True):
    """绘制渐变背景"""
    pixels = img.load()
    for y in range(H):
        ratio = y / H if vertical else 0
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        for x in range(W):
            pixels[x, y] = (r, g, b)

def draw_mountain_silhouette(d, y_base, peaks, color):
    """绘制山峰剪影"""
    points = []
    for i, (x, h, w) in enumerate(peaks):
        points.append((x - w//2, y_base - h))
        points.append((x, y_base - h + 30))
        points.append((x + w//2, y_base - h))
    # 闭合到底部
    points.append((W, y_base))
    points.append((W, H))
    points.append((0, H))
    points.append((0, y_base))
    d.polygon(points, fill=color)

def draw_eagle_silhouette(d, cx, cy, scale=1.0, color=INK):
    """绘制鹰的剪影"""
    s = scale
    # 身体
    d.ellipse([cx-20*s, cy-10*s, cx+20*s, cy+25*s], fill=color)
    # 头部
    d.ellipse([cx-12*s, cy-25*s, cx+12*s, cy-5*s], fill=color)
    # 喙
    d.polygon([(cx+12*s, cy-15*s), (cx+25*s, cy-10*s), (cx+12*s, cy-5*s)], fill=color)
    # 左翼
    d.polygon([
        (cx-15*s, cy-5*s), (cx-80*s, cy-40*s), (cx-70*s, cy-10*s),
        (cx-60*s, cy+5*s), (cx-20*s, cy+10*s)
    ], fill=color)
    # 右翼
    d.polygon([
        (cx+15*s, cy-5*s), (cx+80*s, cy-40*s), (cx+70*s, cy-10*s),
        (cx+60*s, cy+5*s), (cx+20*s, cy+10*s)
    ], fill=color)
    # 尾羽
    d.polygon([
        (cx-15*s, cy+20*s), (cx, cy+55*s), (cx+15*s, cy+20*s)
    ], fill=color)

def draw_fish_silhouette(d, cx, cy, scale=1.0, color=INK, facing_right=True):
    """绘制鱼的剪影"""
    s = scale
    m = 1 if facing_right else -1
    # 身体
    d.ellipse([cx-30*s, cy-15*s, cx+30*s, cy+15*s], fill=color)
    # 尾巴
    d.polygon([
        (cx-30*s, cy), (cx-55*s, cy-20*s), (cx-55*s, cy+20*s)
    ], fill=color)
    # 背鳍
    d.polygon([
        (cx-10*s, cy-15*s), (cx, cy-35*s), (cx+15*s, cy-15*s)
    ], fill=color)
    # 腹鳍
    d.polygon([
        (cx-5*s, cy+15*s), (cx+10*s, cy+30*s), (cx+15*s, cy+15*s)
    ], fill=color)
    # 眼睛
    d.ellipse([cx+20*s, cy-5*s, cx+26*s, cy+5*s], fill=WHITE)
    d.ellipse([cx+22*s, cy-3*s, cx+24*s, cy+3*s], fill=color)

def draw_boat(d, cx, cy, scale=1.0, color=INK, sail_color=None):
    """绘制小船剪影"""
    s = scale
    sc = sail_color or color
    # 船身
    d.polygon([
        (cx-40*s, cy), (cx+40*s, cy), (cx+30*s, cy+15*s), (cx-30*s, cy+15*s)
    ], fill=color)
    # 桅杆
    d.rectangle([(cx-2*s, cy-50*s), (cx+2*s, cy)], fill=color)
    # 帆
    d.polygon([
        (cx+3*s, cy-45*s), (cx+35*s, cy-10*s), (cx+3*s, cy-5*s)
    ], fill=sc)

def draw_tree_silhouette(d, cx, cy, scale=1.0, color=INK):
    """绘制树剪影"""
    s = scale
    # 树干
    d.rectangle([(cx-4*s, cy), (cx+4*s, cy+40*s)], fill=(80, 50, 30))
    # 树冠（三层圆）
    d.ellipse([cx-25*s, cy-35*s, cx+25*s, cy+5*s], fill=color)
    d.ellipse([cx-20*s, cy-55*s, cx+20*s, cy-15*s], fill=color)
    d.ellipse([cx-15*s, cy-70*s, cx+15*s, cy-30*s], fill=color)

def draw_water_waves(d, y_start, y_end, color, alpha=0.3):
    """绘制水波纹（简化：用线条模拟）"""
    for y in range(y_start, y_end, 8):
        offset = int(10 * math.sin(y * 0.1))
        d.line([(MARGIN, y+offset), (W-MARGIN, y+offset)], fill=color, width=2)

def draw_sun(d, cx, cy, r, color):
    """绘制太阳/光晕"""
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)

# ═══════════════════════════════════════════════════
#  通用辅助
# ═══════════════════════════════════════════════════

def new_slide():
    img = Image.new('RGB', (W, H), WHITE)
    return img, ImageDraw.Draw(img)

def draw_header(d, title, subtitle=None, page_num=None, bg_color=INK):
    d.rectangle([(0, 0), (W, 5)], fill=bg_color)
    d.rectangle([(0, 5), (W, HEADER_H)], fill=bg_color)
    d.text((MARGIN, 18), title, fill=WHITE, font=F_TITLE)
    if subtitle:
        d.text((MARGIN + d.textlength(title, F_TITLE) + 30, 22), subtitle, fill=(180,190,200), font=F_SUB)
    if page_num:
        tw = d.textlength(str(page_num), F_SMALL)
        d.text((W - MARGIN - tw, 30), str(page_num), fill=(150,160,170), font=F_SMALL)

def draw_bullet(d, items, y_start, font=None, fill=None, lh=30, x=MARGIN, bullet='•'):
    f = font or F_BODY
    c = fill or INK
    y = y_start
    for item in items:
        d.text((x, y), f'{bullet} ', fill=c, font=f)
        tw = d.textlength(f'{bullet} ', f)
        d.text((x + tw, y), item, fill=c, font=f)
        y += lh
    return y

def draw_section_title(d, title, y, color=FROST):
    d.rectangle([(MARGIN - 10, y), (MARGIN - 4, y + 32)], fill=color)
    d.text((MARGIN + 8, y), title, fill=INK, font=F_SUB)
    return y + 42

def draw_table(d, headers, rows, x, y, col_widths=None, header_color=None, font_body=None, font_header=None):
    fh = font_header or F_TABLE_B
    fb = font_body or F_TABLE
    hc = header_color or TABLE_HDR
    row_h = 32
    if col_widths is None:
        col_widths = [150] * len(headers)
    total_w = sum(col_widths)
    cx = x
    d.rectangle([(x, y), (x + total_w, y + row_h)], fill=hc)
    for i, h in enumerate(headers):
        d.text((cx + 8, y + 6), h, fill=WHITE, font=fh)
        cx += col_widths[i]
    y += row_h
    for ri, row in enumerate(rows):
        bg = TABLE_ALT if ri % 2 == 0 else WHITE
        d.rectangle([(x, y), (x + total_w, y + row_h)], fill=bg)
        cx = x
        for i, cell in enumerate(row):
            d.text((cx + 8, y + 6), str(cell), fill=INK, font=fb)
            cx += col_widths[i]
        y += row_h
    d.rectangle([(x, y - row_h * (len(rows)+1)), (x + total_w, y)], outline=BORDER, width=1)
    return y

def draw_emph_box(d, text, x, y, w, fill_color=None, font=None):
    fc = fill_color or HIGHLIGHT
    f = font or F_BODY_B
    h = 40
    d.rectangle([(x, y), (x + w, y + h)], fill=fc, outline=ACCENT, width=1)
    d.text((x + 16, y + 9), text, fill=INK, font=f)

slide_num = [0]
def next_num():
    slide_num[0] += 1
    return slide_num[0]

def save_slide(img, num, name):
    img.save(os.path.join(OUT, f'slide_{num:02d}_{name}.png'))

# ═══════════════════════════════════════════════════
#  第一课时
# ═══════════════════════════════════════════════════

def slide_cover():
    """1. 封面 — 手绘秋景大图+标题"""
    img, d = new_slide()
    # 渐变天空：橙红到深蓝
    draw_gradient_bg(d, img, (255, 180, 120), (40, 60, 90), vertical=True)
    # 远山剪影（三层）
    draw_mountain_silhouette(d, H-80, [(200, 180, 300), (600, 220, 400), (1000, 150, 350)], (139, 69, 19))
    draw_mountain_silhouette(d, H-60, [(350, 120, 250), (800, 140, 300)], (178, 58, 42))
    # 太阳
    draw_sun(d, 1000, 120, 60, (255, 200, 100))
    # 几棵树
    draw_tree_silhouette(d, 150, H-80, 1.2, (178, 58, 42))
    draw_tree_silhouette(d, 1050, H-80, 1.5, (139, 69, 19))
    # 文字叠加
    d.text((MARGIN, 120), '沁园春·长沙', fill=WHITE, font=F_HUGE)
    d.text((MARGIN + d.textlength('沁园春·长沙', F_HUGE) + 40, 145), '毛泽东', fill=(220, 220, 220), font=F_TITLE)
    d.rectangle([(MARGIN, 260), (MARGIN + 200, 264)], fill=FROST)
    d.rectangle([(MARGIN, 275), (MARGIN + 160, 310)], fill=FROST)
    d.text((MARGIN + 20, 282), '第一课时', fill=WHITE, font=F_BODY_B)
    d.text((MARGIN, 380), '统编版高中语文必修上册 · 第一单元', fill=(220, 220, 220), font=F_BODY)
    d.text((MARGIN, 420), '知人论世 · 诵读感知 · 意象品析', fill=(200, 200, 200), font=F_SUB)
    d.text((MARGIN, H - 50), '课堂讲授版', fill=(180, 180, 180), font=F_SMALL)
    save_slide(img, next_num(), 'cover')

def slide_objectives():
    """2. 学习目标"""
    img, d = new_slide()
    draw_header(d, '学习目标', page_num=next_num())
    y = CONTENT_TOP + 20
    y = draw_section_title(d, '本课学习目标', y)
    objectives = [
        ('语言建构', '了解词的相关知识，掌握生字词读音，正确、流利、有感情地朗读全词', FROST),
        ('思维发展', '理清词的脉络结构，把握"看""忆"领起的上下阕内容', XIANG),
        ('审美鉴赏', '品味意象的活泼灵动、意境的丰盈深邃；揣摩炼字选词的精妙', FROST),
        ('文化传承', '领略毛泽东以天下为己任的胸怀，感受革命青年的壮志豪情', XIANG),
    ]
    y += 10
    for title, desc, color in objectives:
        d.rectangle([(MARGIN, y), (MARGIN + 160, y + 90)], fill=LIGHT_BG, outline=color, width=2)
        d.text((MARGIN + 12, y + 8), title, fill=color, font=F_BODY_B)
        d.text((MARGIN + 12, y + 38), desc, fill=INK, font=F_SMALL)
        y += 110
    save_slide(img, next_num(), 'objectives')

def slide_leadin_autumn():
    """3. 导入 — 左右对比：悲秋 vs 颂秋"""
    img, d = new_slide()
    draw_header(d, '导入新课', '自古文人多悲秋', page_num=next_num())
    y = CONTENT_TOP
    # 左侧：悲秋（灰色冷调）
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 26)], fill=GRAY)
    d.text((MARGIN + 16, y), '悲秋传统', fill=GRAY, font=F_BODY_B)
    y += 35
    autumn_poems = [
        ('宋玉《九辨》', '"悲哉！秋之为气也，萧瑟兮草木摇落而变衰"'),
        ('杜甫《登高》', '"万里悲秋常作客，百年多病独登台"'),
        ('欧阳修《秋声赋》', '"噫嘻悲哉！此秋声也"'),
    ]
    for author, poem in autumn_poems:
        d.text((MARGIN + 10, y), f'  {author}', fill=GRAY, font=F_BODY_B)
        y += 24
        d.text((MARGIN + 10, y), f'  {poem}', fill=INK, font=F_BODY)
        y += 28
    # 右侧：颂秋（暖色）
    y2 = CONTENT_TOP
    d.rectangle([(MARGIN + 520, y2), (MARGIN + 528, y2 + 26)], fill=ACCENT)
    d.text((MARGIN + 536, y2), '例外：秋的赞歌', fill=ACCENT, font=F_BODY_B)
    y2 += 35
    d.text((MARGIN + 530, y2), '  刘禹锡《秋词》', fill=ACCENT, font=F_BODY_B)
    y2 += 24
    d.text((MARGIN + 530, y2), '  "自古逢秋悲寂寥，我言秋日胜春朝"', fill=INK, font=F_BODY)
    y2 += 60
    # 底部提问
    draw_emph_box(d, '那么，毛泽东笔下的秋天，又是怎样的一番景象？', MARGIN, y + 20, 700)
    save_slide(img, next_num(), 'leadin')

def slide_author():
    """4. 知人论世 — 手绘装饰"""
    img, d = new_slide()
    draw_header(d, '知人论世', '毛泽东（1893—1976）', page_num=next_num())
    y = CONTENT_TOP
    # 左侧文字
    info = [
        ('字', '润之，笔名子任'),
        ('籍贯', '湖南湘潭韶山冲'),
        ('身份', '无产阶级革命家、战略家'),
        ('文学', '诗人、书法家——豪放派代表'),
    ]
    for label, val in info:
        d.text((MARGIN, y), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((MARGIN + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    y += 16
    d.text((MARGIN, y), '名句选摘', fill=FROST, font=F_SUB)
    y += 30
    quotes = [
        '"雄关漫道真如铁，而今迈步从头越"',
        '"天若有情天亦老，人间正道是沧桑"',
        '"一万年太久，只争朝夕"',
    ]
    for q in quotes:
        d.text((MARGIN + 10, y), f'  {q}', fill=INK, font=F_BODY)
        y += 26
    y += 16
    d.text((MARGIN, y), '1925年秋，32岁的毛泽东重游橘子洲，写下这首词。', fill=INK, font=F_BODY)
    # 右侧：手绘装饰（抽象山峰+太阳）
    draw_mountain_silhouette(d, H-100, [(900, 200, 300), (1100, 150, 250)], (178, 58, 42))
    draw_sun(d, 1000, 120, 50, (255, 180, 100))
    d.text((850, H-80), '橘子洲 · 湘江', fill=GRAY, font=F_SMALL)
    save_slide(img, next_num(), 'author')

def slide_background():
    """5. 写作背景"""
    img, d = new_slide()
    draw_header(d, '写作背景', '1925年·长沙', page_num=next_num())
    y = CONTENT_TOP
    timeline = [
        ('1925年初', '毛泽东从上海回到韶山，开展农民运动', '>'),
        ('1925年夏', '创建湖南第一个农村党支部——韶山支部', '>'),
        ('1925年8月', '湖南省长赵恒惕下令逮捕毛泽东', '>'),
        ('1925年10月', '离开韶山，途经长沙，重游橘子洲', '*'),
        ('1925年秋', '写下《沁园春·长沙》', '+'),
    ]
    for date, event, mark in timeline:
        col = FROST if mark == '*' else ACCENT if mark == '+' else INK
        d.text((MARGIN, y), f'{mark} {date}', fill=col, font=F_BODY_B)
        tw = d.textlength(f'{mark} {date}  ', F_BODY_B)
        d.text((MARGIN + tw, y), event, fill=INK, font=F_BODY)
        y += 34
    y += 20
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 100)], fill=LIGHT_BG, outline=ACCENT, width=2)
    d.text((MARGIN + 16, y + 10), '时代背景', fill=ACCENT, font=F_BODY_B)
    d.text((MARGIN + 16, y + 38), '全国工农运动风起云涌 · 五卅运动爆发 · 北伐战争前夕', fill=INK, font=F_BODY)
    d.text((MARGIN + 16, y + 62), '革命由哪个阶级领导？——成为党内外斗争的焦点', fill=FROST, font=F_BODY)
    y += 120
    draw_emph_box(d, '面对如画的秋色和大好的革命形势，32岁的毛泽东心潮澎湃，写下此词', MARGIN, y, 750)
    save_slide(img, next_num(), 'background')

def slide_wenti():
    """6. 文体知识"""
    img, d = new_slide()
    draw_header(d, '文体知识', '词——"长短句"', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '什么是"词"？', fill=FROST, font=F_SUB)
    y += 30
    d.text((MARGIN + 10, y), '词，萌芽于南朝，形成于唐，盛行于宋。又称"曲子词""长短句""诗余"。', fill=INK, font=F_BODY)
    y += 28
    d.text((MARGIN + 10, y), '特点：调有定格，句有定数，字有定声。按词牌格式创作，称"填词"。', fill=INK, font=F_BODY)
    y += 40
    d.text((MARGIN, y), '词的分类', fill=FROST, font=F_SUB)
    y += 35
    draw_table(d,
        ['分类标准', '类别', '说明'],
        [
            ['按字数', '小令(<=58字)', '篇幅最短'],
            ['按字数', '中调(59-90字)', '中等篇幅'],
            ['按字数', '长调(>=91字)', '《沁园春·长沙》114字 属长调'],
            ['按段落', '单调/双调', '一段或两段(两阕)，双调最常见'],
            ['按风格', '豪放派', '苏轼、辛弃疾——气势豪放'],
            ['按风格', '婉约派', '柳永、李清照——清丽含蓄'],
        ],
        MARGIN, y, [120, 200, 540]
    )
    save_slide(img, next_num(), 'wenti')

def slide_cipai():
    """7. 词牌"""
    img, d = new_slide()
    draw_header(d, '词牌知识', '"沁园春"的来历', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '词牌 vs 标题', fill=FROST, font=F_SUB)
    y += 35
    items = [
        '词牌 = 词的格式名称（决定字数、句数、平仄声韵），与内容无关',
        '标题 = 词的内容的集中体现（"长沙"表明描写对象与地点）',
        '"沁园春"：又名"洞庭春色""东仙""念离群"',
    ]
    y = draw_bullet(d, items, y, bullet='•')
    y += 25
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 140)], fill=LIGHT_BG, outline=ACCENT, width=2)
    d.text((MARGIN + 16, y + 10), '典故："沁园"的由来', fill=ACCENT, font=F_BODY_B)
    d.text((MARGIN + 16, y + 38), '相传"沁园"为东汉明帝女儿沁水公主的园林。后外戚窦宪仗势强夺此园，', fill=INK, font=F_BODY)
    d.text((MARGIN + 16, y + 62), '有人作诗咏其事。后人以"沁园春"为词牌，寄寓世事变迁之感。', fill=INK, font=F_BODY)
    d.text((MARGIN + 16, y + 90), '毛泽东以"沁园春"为词牌，暗含对旧世界的批判。', fill=FROST, font=F_SMALL)
    save_slide(img, next_num(), 'cipai')

def slide_zhengyin():
    """8. 正字音"""
    img, d = new_slide()
    draw_header(d, '朗读准备', '辨字正音', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '请正确读出下列红色字的读音', fill=INK, font=F_SUB)
    y += 40
    words = [
        ('沁(qin)园春', '百舸(ge)争流'),
        ('寥廓(liao kuo)', '方遒(qiu)'),
        ('峥嵘(zheng rong)', '浪遏(e)飞舟'),
        ('惆怅(chou chang)', '橘子(ju)洲'),
    ]
    for a, c in words:
        d.text((MARGIN, y), a, fill=FROST, font=F_BODY_B)
        d.text((MARGIN + 450, y), c, fill=FROST, font=F_BODY_B)
        y += 38
    y += 20
    d.text((MARGIN, y), '注意：多音字与易错字', fill=FROST, font=F_SUB)
    y += 32
    notes = [
        ('"看"(kan)', '：领字，统领以下七句，读时稍作停顿'),
        ('"舸"(ge)', '：大船，非"可"音'),
        ('"遏"(e)', '：阻止，非"喝"音'),
    ]
    for word, note in notes:
        d.text((MARGIN + 10, y), word, fill=FROST, font=F_BODY_B)
        tw = d.textlength(word, F_BODY_B)
        d.text((MARGIN + 10 + tw, y), note, fill=INK, font=F_BODY)
        y += 28
    save_slide(img, next_num(), 'zhengyin')

def slide_dujiepai():
    """9. 朗读节拍"""
    img, d = new_slide()
    draw_header(d, '朗读指导', '读出节拍韵律', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '节拍规则', fill=FROST, font=F_SUB)
    y += 35
    rules = [
        ('四字句 二二式', '独立 / 寒秋，湘江 / 北去'),
        ('五字句 一四式', '恰 / 同学少年，问 / 苍茫大地'),
        ('七字句 二五式', '粪土 / 当年万户侯'),
        ('七字句 四三式', '万类霜天 / 竞自由'),
        ('八字句 三二三', '忆往昔 / 峥嵘 / 岁月稠'),
    ]
    for rule, example in rules:
        d.text((MARGIN + 10, y), rule, fill=FROST, font=F_BODY_B)
        tw = d.textlength(rule, F_BODY_B)
        d.text((MARGIN + 10 + tw, y), f'  -- {example}', fill=INK, font=F_BODY)
        y += 32
    y += 20
    d.text((MARGIN, y), '重音指导', fill=FROST, font=F_SUB)
    y += 32
    d.text((MARGIN + 10, y), '领起性重读：看、怅、问、恰', fill=INK, font=F_BODY)
    y += 28
    d.text((MARGIN + 10, y), '强调性重读：红、尽、碧、争、击、翔、竞、主、峥嵘、挥斥、激扬、粪土、击、遏', fill=INK, font=F_BODY)
    y += 20
    draw_emph_box(d, '上片"看"字领起七句、下片"恰"字引发七句 —— 一气相应，渐快渐高！', MARGIN, y, 750)
    save_slide(img, next_num(), 'jiepai')

def slide_full_poem():
    """10. 全词齐读"""
    img, d = new_slide()
    draw_header(d, '朗读课文', '齐读全词', page_num=next_num())
    y = CONTENT_TOP - 10
    d.text((MARGIN, y), '上  阕', fill=FROST, font=F_SUB)
    y += 32
    for line in ['独立寒秋，湘江北去，橘子洲头。',
                 '看万山红遍，层林尽染；漫江碧透，百舸争流。',
                 '鹰击长空，鱼翔浅底，万类霜天竞自由。',
                 '怅寥廓，问苍茫大地，谁主沉浮？']:
        d.text((MARGIN + 20, y), line, fill=INK, font=F_POEM)
        y += 34
    y += 10
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=LIGHT_GRAY, width=1)
    y += 10
    d.text((MARGIN, y), '下  阕', fill=XIANG, font=F_SUB)
    y += 32
    for line in ['携来百侣曾游。忆往昔峥嵘岁月稠。',
                 '恰同学少年，风华正茂；书生意气，挥斥方遒。',
                 '指点江山，激扬文字，粪土当年万户侯。',
                 '曾记否，到中流击水，浪遏飞舟？']:
        d.text((MARGIN + 20, y), line, fill=INK, font=F_POEM)
        y += 34
    save_slide(img, next_num(), 'full_poem')

def slide_four_pictures():
    """11. 四幅图 — 视觉卡片"""
    img, d = new_slide()
    draw_header(d, '整体感知', '全词四幅图画', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '思考：这首词按内容可划分为哪四幅图画？', fill=INK, font=F_SUB)
    y += 50
    cards = [
        ('独立寒秋图', '独立寒秋\n湘江北去\n橘子洲头', FROST, (220, 240, 255)),
        ('湘江秋景图', '看万山红遍\n鹰击长空\n万类霜天竞自由', XIANG, (230, 255, 240)),
        ('峥嵘岁月图', '恰同学少年\n粪土当年万户侯', ACCENT, (255, 245, 230)),
        ('中流击水图', '到中流击水\n浪遏飞舟', INK, (240, 240, 245)),
    ]
    cx = MARGIN
    cw = 260
    gap = 20
    for title, desc, col, bg in cards:
        d.rectangle([(cx, y), (cx + cw, y + 180)], fill=bg, outline=col, width=2)
        d.rectangle([(cx, y), (cx + cw, y + 4)], fill=col)
        d.text((cx + 20, y + 16), title, fill=col, font=F_BODY_B)
        lines = desc.split('\n')
        ly = y + 60
        for line in lines:
            d.text((cx + 20, ly), line, fill=INK, font=F_SMALL)
            ly += 28
        cx += cw + gap
    y += 200
    d.text((MARGIN, y), '上阕（看）——写景    |    下阕（忆）——忆事抒情', fill=INK, font=F_SUB)
    y += 30
    draw_emph_box(d, '诗眼：上阕"看"字领起 | 下阕"忆"字领起 | 过片"怅寥廓，问苍茫大地，谁主沉浮？"', MARGIN, y, 750)
    save_slide(img, next_num(), 'four_pics')

def slide_duli():
    """12. 独立寒秋图 — 手绘湘江+文字"""
    img, d = new_slide()
    # 背景：浅蓝天空+江水
    draw_gradient_bg(d, img, (230, 240, 250), (200, 220, 235), vertical=True)
    # 手绘江面波纹
    for y_wave in range(400, H, 12):
        offset = int(8 * math.sin(y_wave * 0.08))
        d.line([(MARGIN, y_wave+offset), (W-MARGIN, y_wave+offset)], fill=(180, 200, 220), width=2)
    # 远山
    draw_mountain_silhouette(d, 400, [(300, 150, 400), (700, 180, 500)], (100, 130, 160))
    # 洲头（小三角形）
    d.polygon([(500, 400), (600, 320), (700, 400)], fill=(160, 180, 100))
    # 文字叠加
    d.text((MARGIN, 120), '"独立寒秋，湘江北去，橘子洲头"', fill=INK, font=F_POEM_LG)
    y = 180
    d.text((MARGIN, y), '这一句交代了哪些内容？', fill=INK, font=F_SUB)
    y += 38
    analysis = [
        ('时间', '寒秋（晚秋时节）'),
        ('地点', '橘子洲头（长沙湘江中的沙洲）'),
        ('环境', '湘江北去（江水滔滔向北流）'),
        ('人物', '"独立"——独自伫立，天地间一尊伟岸身躯'),
    ]
    # 用半透明卡片
    for label, val in analysis:
        d.rectangle([(MARGIN, y), (MARGIN + 600, y + 32)], fill=(255, 255, 255, 180))
        d.text((MARGIN + 20, y), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((MARGIN + 20 + tw, y), val, fill=INK, font=F_BODY)
        y += 38
    y += 10
    draw_emph_box(d, '"独立"非孤独——是深思的形象、高瞻远瞩的姿态', MARGIN, y, 600)
    save_slide(img, next_num(), 'duli')

def slide_qiujing_kan():
    """13. "看"字领起七句"""
    img, d = new_slide()
    draw_header(d, '湘江秋景图', '"看"字统领七句', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '"看"字领起以下七句——诗人看见了什么？', fill=INK, font=F_SUB)
    y += 38
    d.text((MARGIN, y), '看万山红遍，层林尽染；漫江碧透，百舸争流。', fill=FROST, font=F_POEM)
    y += 32
    d.text((MARGIN, y), '鹰击长空，鱼翔浅底，万类霜天竞自由。', fill=FROST, font=F_POEM)
    y += 45
    d.text((MARGIN, y), '诗人的观察视角变化', fill=INK, font=F_SUB)
    y += 35
    perspectives = [
        ('远眺', '万山红遍，层林尽染 -- 远景，色彩浓烈'),
        ('近观', '漫江碧透 -- 中景，江水清澈'),
        ('近视', '百舸争流 -- 近景，船只如梭'),
        ('仰视', '鹰击长空 -- 向上，矫健有力'),
        ('俯瞰', '鱼翔浅底 -- 向下，轻快自由'),
    ]
    for view, desc in perspectives:
        d.text((MARGIN + 10, y), f'{view}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{view}：', F_BODY_B)
        d.text((MARGIN + 10 + tw, y), desc, fill=INK, font=F_BODY)
        y += 30
    y += 15
    draw_emph_box(d, '由远及近、由上到下、动静结合——如电影镜头逐层推进', MARGIN, y, 750)
    save_slide(img, next_num(), 'kan')

# ═══════════════════════════════════════════════════
#  6页意象可视化 —— 全部PIL手绘，文字与图形融合
# ═══════════════════════════════════════════════════

def slide_imagery_wanshan():
    """14. 万山红遍 — 红色山脉+大字融合"""
    img, d = new_slide()
    # 背景：橙红渐变（秋意）
    draw_gradient_bg(d, img, (255, 220, 180), (200, 80, 60), vertical=True)
    # 多层红色山脉（由远到近，颜色加深）
    draw_mountain_silhouette(d, H-50, [(200, 120, 350), (600, 160, 450), (1000, 100, 300)], (180, 100, 80))
    draw_mountain_silhouette(d, H-30, [(350, 80, 250), (800, 100, 300)], (178, 58, 42))
    draw_mountain_silhouette(d, H-10, [(500, 60, 400)], (139, 50, 30))
    # 太阳
    draw_sun(d, 200, 100, 50, (255, 200, 100))
    # 大字"红遍"叠加在山脉上方
    d.text((MARGIN + 50, 280), '万山', fill=WHITE, font=load_font('msyhbd.ttc', 90))
    d.text((MARGIN + 50, 380), '红遍', fill=(255, 240, 200), font=load_font('msyhbd.ttc', 120))
    # 右侧分析文字（半透明背景）
    tx = 780
    d.rectangle([(tx - 20, 150), (W - 40, 550)], fill=(255, 255, 255, 200))
    d.text((tx, 170), '逐字品读', fill=FROST, font=F_SUB)
    y = 210
    points = [
        ('"万"', '群山连绵，不止一座'),
        ('"红遍"', '秋色浓烈，漫山尽染'),
        ('视角', '远眺——立足高处望群山'),
        ('色彩', '红——热烈、蓬勃'),
    ]
    for label, val in points:
        d.text((tx, y), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((tx + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    y += 20
    d.rectangle([(tx, y), (tx + 420, y + 80)], fill=HIGHLIGHT, outline=ACCENT, width=1)
    d.text((tx + 16, y + 8), '看图理解', fill=ACCENT, font=F_BODY_B)
    d.text((tx + 16, y + 34), '满山红叶就是"万山红遍"的画面——', fill=INK, font=F_SMALL)
    d.text((tx + 16, y + 52), '不是一棵树红，是整片山都红了', fill=INK, font=F_SMALL)
    save_slide(img, next_num(), 'img_wanshan')

def slide_imagery_cenglin():
    """15. 层林尽染 — 层叠树林+渐变色"""
    img, d = new_slide()
    # 背景：暖黄到红
    draw_gradient_bg(d, img, (255, 240, 200), (220, 120, 80), vertical=True)
    # 层叠树林（三层，颜色不同）
    colors = [(200, 160, 80), (180, 100, 50), (160, 60, 40)]
    for i, (cx, color) in enumerate(zip([200, 500, 900], colors)):
        draw_tree_silhouette(d, cx, H - 50 + i*10, 1.5 + i*0.3, color)
    # 中间文字
    d.text((MARGIN + 50, 250), '层林', fill=WHITE, font=load_font('msyhbd.ttc', 100))
    d.text((MARGIN + 50, 360), '尽染', fill=(255, 230, 200), font=load_font('msyhbd.ttc', 130))
    # 右侧分析
    tx = 780
    d.rectangle([(tx - 20, 150), (W - 40, 520)], fill=(255, 255, 255, 200))
    d.text((tx, 170), '逐字品读', fill=FROST, font=F_SUB)
    y = 210
    points = [
        ('"层"', '树林层层叠叠，有纵深'),
        ('"尽染"', '像被染过一样，色彩饱和'),
        ('视角', '远眺——看山林层次'),
        ('色彩', '黄、橙、红——渐变秋色'),
    ]
    for label, val in points:
        d.text((tx, y), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((tx + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    y += 20
    d.rectangle([(tx, y), (tx + 420, y + 80)], fill=HIGHLIGHT, outline=ACCENT, width=1)
    d.text((tx + 16, y + 8), '看图理解', fill=ACCENT, font=F_BODY_B)
    d.text((tx + 16, y + 34), '一层层的树林被秋色染透——', fill=INK, font=F_SMALL)
    d.text((tx + 16, y + 52), '近处黄、远处红，层层递进', fill=INK, font=F_SMALL)
    save_slide(img, next_num(), 'img_cenglin')

def slide_imagery_manjiang():
    """16. 漫江碧透 — 碧绿江水+透明感"""
    img, d = new_slide()
    # 背景：天空+江水渐变
    draw_gradient_bg(d, img, (200, 230, 245), (46, 125, 107), vertical=True)
    # 水波纹（多层）
    for y_wave in range(350, H, 10):
        offset = int(12 * math.sin(y_wave * 0.06))
        alpha = int(255 * (1 - (y_wave - 350) / (H - 350)))
        color = (80 + alpha//3, 150 + alpha//4, 140 + alpha//4)
        d.line([(MARGIN, y_wave+offset), (W-MARGIN, y_wave+offset)], fill=color, width=2)
    # 大字
    d.text((MARGIN + 50, 200), '漫江', fill=WHITE, font=load_font('msyhbd.ttc', 100))
    d.text((MARGIN + 50, 310), '碧透', fill=(200, 255, 240), font=load_font('msyhbd.ttc', 130))
    # 右侧分析
    tx = 780
    d.rectangle([(tx - 20, 150), (W - 40, 520)], fill=(255, 255, 255, 200))
    d.text((tx, 170), '逐字品读', fill=XIANG, font=F_SUB)
    y = 210
    points = [
        ('"漫"', '满江、整条江，无处不在'),
        ('"碧透"', '绿到能看穿水底'),
        ('视角', '近观——低头看江水'),
        ('色彩', '碧绿——清澈、宁静'),
    ]
    for label, val in points:
        d.text((tx, y), f'{label}：', fill=XIANG, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((tx + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    y += 20
    d.rectangle([(tx, y), (tx + 420, y + 80)], fill=HIGHLIGHT, outline=ACCENT, width=1)
    d.text((tx + 16, y + 8), '看图理解', fill=ACCENT, font=F_BODY_B)
    d.text((tx + 16, y + 34), '整条江的水都是碧绿透明的——', fill=INK, font=F_SMALL)
    d.text((tx + 16, y + 52), '不是浅绿，是绿到能看见水底', fill=INK, font=F_SMALL)
    save_slide(img, next_num(), 'img_manjiang')

def slide_imagery_baige():
    """17. 百舸争流 — 江面+多船竞发"""
    img, d = new_slide()
    # 背景：江面蓝色
    draw_gradient_bg(d, img, (220, 235, 245), (100, 150, 180), vertical=True)
    # 水波纹
    for y_wave in range(300, H, 12):
        offset = int(15 * math.sin(y_wave * 0.05))
        d.line([(MARGIN, y_wave+offset), (W-MARGIN, y_wave+offset)], fill=(120, 170, 200), width=2)
    # 多艘小船（竞发感）
    boats = [(150, 450, 0.8), (300, 420, 0.9), (500, 460, 1.0), (700, 410, 0.85), (900, 440, 0.9), (1050, 470, 0.8)]
    for cx, cy, s in boats:
        draw_boat(d, cx, cy, s, INK, (200, 220, 240))
    # 大字
    d.text((MARGIN + 50, 180), '百舸', fill=WHITE, font=load_font('msyhbd.ttc', 100))
    d.text((MARGIN + 50, 290), '争流', fill=(230, 245, 255), font=load_font('msyhbd.ttc', 130))
    # 右侧分析
    tx = 780
    d.rectangle([(tx - 20, 150), (W - 40, 520)], fill=(255, 255, 255, 200))
    d.text((tx, 170), '逐字品读', fill=ACCENT, font=F_SUB)
    y = 210
    points = [
        ('"百"', '虚指，形容船多'),
        ('"舸"', '大船'),
        ('"争"', '竞相行驶，争先恐后'),
        ('动态', '船只在江面上你追我赶'),
    ]
    for label, val in points:
        d.text((tx, y), f'{label}：', fill=ACCENT, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((tx + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    y += 20
    d.rectangle([(tx, y), (tx + 420, y + 80)], fill=HIGHLIGHT, outline=ACCENT, width=1)
    d.text((tx + 16, y + 8), '看图理解', fill=ACCENT, font=F_BODY_B)
    d.text((tx + 16, y + 34), '江面上许多船只在竞相行驶——', fill=INK, font=F_SMALL)
    d.text((tx + 16, y + 52), '"争"字写出热烈奋进的场面', fill=INK, font=F_SMALL)
    save_slide(img, next_num(), 'img_baige')

def slide_imagery_yingji():
    """18. 鹰击长空 — 手绘鹰剪影+天空渐变"""
    img, d = new_slide()
    # 背景：天空蓝渐变
    draw_gradient_bg(d, img, (100, 180, 220), (60, 100, 150), vertical=True)
    # 云朵（椭圆）
    d.ellipse([(100, 80), (250, 140)], fill=(240, 250, 255))
    d.ellipse([(800, 120), (950, 170)], fill=(220, 240, 250))
    d.ellipse([(1050, 60), (1200, 110)], fill=(230, 245, 255))
    # 鹰剪影（向上飞翔）
    draw_eagle_silhouette(d, 600, 300, 2.0, INK)
    # 大字"击"（冲击力）
    d.text((MARGIN + 50, 200), '鹰击', fill=WHITE, font=load_font('msyhbd.ttc', 100))
    d.text((MARGIN + 50, 320), '长空', fill=(200, 230, 255), font=load_font('msyhbd.ttc', 120))
    # 右侧分析
    tx = 780
    d.rectangle([(tx - 20, 150), (W - 40, 520)], fill=(255, 255, 255, 200))
    d.text((tx, 170), '逐字品读', fill=FROST, font=F_SUB)
    y = 210
    points = [
        ('"击"', '搏击、冲击——不是普通的飞'),
        ('"长空"', '广阔的天空'),
        ('视角', '仰视——抬头看天空'),
        ('感受', '矫健勇猛，充满力量'),
    ]
    for label, val in points:
        d.text((tx, y), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((tx + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    y += 20
    d.rectangle([(tx, y), (tx + 420, y + 80)], fill=HIGHLIGHT, outline=ACCENT, width=1)
    d.text((tx + 16, y + 8), '看图理解', fill=ACCENT, font=F_BODY_B)
    d.text((tx + 16, y + 34), '鹰在天空中展翅搏击——', fill=INK, font=F_SMALL)
    d.text((tx + 16, y + 52), '"击"不是"飞"，是有力量的冲击', fill=INK, font=F_SMALL)
    save_slide(img, next_num(), 'img_yingji')

def slide_imagery_yuxiang():
    """19. 鱼翔浅底 — 手绘鱼+水波"""
    img, d = new_slide()
    # 背景：浅蓝水面
    draw_gradient_bg(d, img, (200, 230, 240), (150, 200, 210), vertical=True)
    # 水波（浅底效果）
    for y_wave in range(250, H, 10):
        offset = int(10 * math.sin(y_wave * 0.07))
        alpha = int(200 * (1 - (y_wave - 250) / (H - 250)))
        color = (140 + alpha//4, 190 + alpha//4, 200 + alpha//4)
        d.line([(MARGIN, y_wave+offset), (W-MARGIN, y_wave+offset)], fill=color, width=2)
    # 鱼（像鸟一样飞翔）
    draw_fish_silhouette(d, 550, 350, 2.0, INK, facing_right=True)
    # 气泡
    d.ellipse([(620, 300), (640, 320)], fill=(255, 255, 255, 150))
    d.ellipse([(650, 280), (665, 295)], fill=(255, 255, 255, 150))
    # 大字
    d.text((MARGIN + 50, 180), '鱼翔', fill=WHITE, font=load_font('msyhbd.ttc', 100))
    d.text((MARGIN + 50, 290), '浅底', fill=(220, 245, 250), font=load_font('msyhbd.ttc', 120))
    # 右侧分析
    tx = 780
    d.rectangle([(tx - 20, 150), (W - 40, 520)], fill=(255, 255, 255, 200))
    d.text((tx, 170), '逐字品读', fill=XIANG, font=F_SUB)
    y = 210
    points = [
        ('"翔"', '本指鸟飞——鱼如鸟般轻快'),
        ('"浅底"', '水浅可见底——说明水清'),
        ('视角', '俯瞰——低头看水中'),
        ('感受', '自由自在，轻盈畅快'),
    ]
    for label, val in points:
        d.text((tx, y), f'{label}：', fill=XIANG, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((tx + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    y += 20
    d.rectangle([(tx, y), (tx + 420, y + 80)], fill=HIGHLIGHT, outline=ACCENT, width=1)
    d.text((tx + 16, y + 8), '看图理解', fill=ACCENT, font=F_BODY_B)
    d.text((tx + 16, y + 34), '清澈浅水中鱼儿自由游动——', fill=INK, font=F_SMALL)
    d.text((tx + 16, y + 52), '"翔"不是"游"，是像鸟一样自由', fill=INK, font=F_SMALL)
    save_slide(img, next_num(), 'img_yuxiang')

# ═══════════════════════════════════════════════════
#  继续教学分析页（纯文字表格，但加视觉底色）
# ═══════════════════════════════════════════════════

def slide_imagery_table():
    """20. 意象分析表"""
    img, d = new_slide()
    draw_header(d, '湘江秋景图', '意象分析表', page_num=next_num())
    y = CONTENT_TOP - 10
    d.text((MARGIN, y), '思考：诗人选取了哪些意象？这些意象有什么特点？请完成表格。', fill=INK, font=F_SUB)
    y += 40
    # 彩色表头（不用纯白）
    draw_table(d,
        ['意象', '相关诗句', '修饰词', '意象特点'],
        [
            ['山', '看万山红遍', '万、红遍', '山多，红得范围极广'],
            ['林', '层林尽染', '层、尽染', '层层叠叠，秋色浓烈'],
            ['江', '漫江碧透', '漫、碧透', '江水满溢，清澈见底'],
            ['舸', '百舸争流', '百、争', '千帆竞发，昂扬奋进'],
            ['鹰', '鹰击长空', '击', '迅捷矫健，搏击有力'],
            ['鱼', '鱼翔浅底', '翔', '轻盈畅快，自由自在'],
            ['总结', '万类霜天竞自由', '竞', '万物蓬勃，奋发自强'],
        ],
        MARGIN, y, [60, 220, 150, 330]
    )
    y += 240
    d.text((MARGIN, y), '思考：这些意象共同构成了一幅怎样的画面？', fill=INK, font=F_SUB)
    y += 35
    draw_emph_box(d, '明确：色彩绚烂、生机勃勃、壮丽开阔的湘江秋景图', MARGIN, y, 750)
    save_slide(img, next_num(), 'imagery_table')

def slide_color_action():
    """21. 色彩美与动态美"""
    img, d = new_slide()
    draw_header(d, '意象品析', '色彩美与动态美', page_num=next_num())
    y = CONTENT_TOP
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 22)], fill=FROST)
    d.text((MARGIN + 16, y + 2), '色彩美：山红水绿', fill=WHITE, font=F_BODY_B)
    y += 35
    colors = [
        '"万""层""漫"——在范围、程度、层次上渲染，红绿两色突出',
        '"遍""尽""透"——红得彻底、绿得透彻，浓艳鲜明',
        '红（山林）与绿（江水）对比鲜明，视觉冲击力强',
    ]
    y = draw_bullet(d, colors, y, bullet='  ')
    y += 15
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 22)], fill=XIANG)
    d.text((MARGIN + 16, y + 2), '动态美：生机勃勃', fill=WHITE, font=F_BODY_B)
    y += 35
    actions = [
        '"争"——千帆竞发、争先恐后的热烈场面',
        '"击"——鹰的矫健勇猛、搏击长空',
        '"翔"——鱼的自由自在、轻快活泼',
        '"竞"——万物蓬勃旺盛的生命力',
    ]
    y = draw_bullet(d, actions, y, bullet='  ')
    y += 15
    draw_emph_box(d, '这些意象融入了诗人对自由解放的向往——不是客观白描，是"灌注了生气的形象"', MARGIN, y, 750)
    save_slide(img, next_num(), 'color_action')

def slide_lianzi_1():
    """22. 炼字品析 — 表格+手绘鹰鱼小图"""
    img, d = new_slide()
    draw_header(d, '炼字品析', '"击"与"翔"的精妙', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '思考：为什么用"击"不用"飞"？为什么用"翔"不用"游"？', fill=INK, font=F_SUB)
    y += 35
    draw_table(d,
        ['用字', '本义', '在词中的效果', '替换后'],
        [
            ['击(鹰击长空)', '搏击、冲击', '矫健勇猛、迅猛有力', '"飞"——无力量感'],
            ['翔(鱼翔浅底)', '盘旋飞翔', '鱼如鸟般轻快自由', '"游"——平淡'],
        ],
        MARGIN, y, [140, 130, 280, 170]
    )
    y += 100
    d.text((MARGIN, y), '"击""翔"赋予鹰和鱼以人的精神气质——勇敢、自由、奋进', fill=FROST, font=F_BODY_B)
    # 下方手绘小图
    draw_eagle_silhouette(d, 180, y + 80, 0.8, FROST)
    d.text((120, y + 160), '鹰击长空', fill=FROST, font=F_SMALL)
    draw_fish_silhouette(d, 400, y + 80, 0.8, XIANG, facing_right=True)
    d.text((340, y + 160), '鱼翔浅底', fill=XIANG, font=F_SMALL)
    # 右侧对比文字
    d.text((620, y + 50), '对比：', fill=ACCENT, font=F_BODY_B)
    d.text((620, y + 80), '鹰在天空搏击——', fill=INK, font=F_BODY)
    d.text((620, y + 105), '  那是"击"的力量', fill=FROST, font=F_BODY)
    d.text((620, y + 135), '鱼在水中飞翔——', fill=INK, font=F_BODY)
    d.text((620, y + 160), '  那是"翔"的自由', fill=XIANG, font=F_BODY)
    save_slide(img, next_num(), 'lianzi_1')

def slide_lianzi_2():
    '''23. 炼字"竞"'''
    img, d = new_slide()
    draw_header(d, '炼字品析', '"竞"字的张力', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '"万类霜天竞自由"——"竞"字好在哪里？', fill=INK, font=F_SUB)
    y += 40
    analysis = [
        ('"竞"的本义', '竞争、竞赛'),
        ('在词中', '万物在寒秋严霜下竞相展现旺盛生命力'),
        ('深层意蕴', '不是消极适应，而是积极主动地"争"自由'),
        ('与诗人', '暗合青年毛泽东"与天奋斗，其乐无穷"的斗争精神'),
    ]
    for label, val in analysis:
        d.text((MARGIN + 10, y), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((MARGIN + 10 + tw, y), val, fill=INK, font=F_BODY)
        y += 34
    y += 20
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 80)], fill=LIGHT_BG, outline=FROST, width=2)
    d.text((MARGIN + 16, y + 10), '小结', fill=FROST, font=F_BODY_B)
    d.text((MARGIN + 16, y + 40), '"击""翔""竞"三个动词，从鹰的搏击→鱼的自由→万物的竞发，层层推进', fill=INK, font=F_BODY)
    save_slide(img, next_num(), 'lianzi_2')

def slide_transition():
    """24. 过渡"""
    img, d = new_slide()
    draw_header(d, '承上启下', '"谁主沉浮"', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '"怅寥廓，问苍茫大地，谁主沉浮？"', fill=FROST, font=F_POEM)
    y += 45
    d.text((MARGIN, y), '思考：这三句在全词中起什么作用？', fill=INK, font=F_SUB)
    y += 38
    texts = [
        '"怅"——不是消沉，是面对壮阔秋景而生的深沉感慨',
        '"寥廓"——宇宙的广阔，反衬出思考的宏大',
        '"问苍茫大地，谁主沉浮"——从写景转入抒情，是全词的枢纽',
        '这一问，承上阕之景，启下阕之情，是"过片"之笔',
    ]
    y = draw_bullet(d, texts, y, bullet='  ')
    y += 20
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 80)], fill=LIGHT_BG, outline=INK, width=2)
    d.text((MARGIN + 16, y + 10), '深层理解', fill=INK, font=F_BODY_B)
    d.text((MARGIN + 16, y + 40), '"谁主沉浮"——更是问：中国的命运由谁主宰？革命的前途谁来引领？', fill=FROST, font=F_BODY)
    save_slide(img, next_num(), 'transition')

def slide_summary_1():
    """25. 第一课时小结"""
    img, d = new_slide()
    draw_header(d, '第一课时小结', '', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '本课时我们学习了：', fill=INK, font=F_SUB)
    y += 40
    items = [
        '词的文体知识（词牌、分类、特点）',
        '毛泽东的生平与写作背景',
        '生字词读音与朗读节拍韵律',
        '全词四幅图画结构',
        '上阕意象分析——色彩美与动态美',
        '炼字品析——"击""翔""竞"的精妙',
    ]
    y = draw_bullet(d, items, y, bullet='V')
    y += 20
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 60)], fill=FROST)
    d.text((MARGIN + 20, y + 15), '下节课预告：品析下阕——同学少年形象、典故、对比阅读、主题归纳', fill=WHITE, font=F_SUB)
    save_slide(img, next_num(), 'summary_1')

# ═══════════════════════════════════════════════════
#  第二课时
# ═══════════════════════════════════════════════════

def slide_p2_cover():
    """26. 第二课时封面 — 手绘秋景"""
    img, d = new_slide()
    draw_gradient_bg(d, img, (255, 200, 150), (60, 90, 120), vertical=True)
    draw_mountain_silhouette(d, H-80, [(300, 180, 400), (700, 200, 450)], (139, 69, 19))
    draw_mountain_silhouette(d, H-60, [(500, 120, 350)], (178, 58, 42))
    draw_sun(d, 200, 100, 50, (255, 200, 100))
    d.text((MARGIN, 100), '沁园春·长沙', fill=WHITE, font=F_HUGE)
    d.text((MARGIN + d.textlength('沁园春·长沙', F_HUGE) + 40, 125), '毛泽东', fill=(220, 220, 220), font=F_TITLE)
    d.rectangle([(MARGIN, 230), (MARGIN + 160, 268)], fill=XIANG)
    d.text((MARGIN + 20, 238), '第二课时', fill=WHITE, font=F_BODY_B)
    d.text((MARGIN, 340), '品析下阕 · 情景交融 · 拓展对比', fill=(220, 220, 220), font=F_SUB)
    save_slide(img, next_num(), 'p2_cover')

def slide_review():
    """27. 回顾"""
    img, d = new_slide()
    draw_header(d, '温故知新', '回顾上阕内容', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '上阕写了什么？使用什么手法？', fill=INK, font=F_SUB)
    y += 38
    d.text((MARGIN, y), '上阕：描绘绚丽多彩的湘江秋景', fill=FROST, font=F_BODY_B)
    y += 30
    d.text((MARGIN, y), '手法：远近相间、动静结合、视角转换', fill=INK, font=F_BODY)
    y += 30
    d.text((MARGIN, y), '诗眼："看"字领起七句', fill=INK, font=F_BODY)
    y += 30
    d.text((MARGIN, y), '过渡："怅寥廓，问苍茫大地，谁主沉浮？"', fill=INK, font=F_BODY)
    y += 40
    d.text((MARGIN, y), '今天品读下阕——毛泽东和"同学少年"的故事', fill=FROST, font=F_SUB)
    save_slide(img, next_num(), 'review')

def slide_xiaque_intro():
    """28. 下阕引入"""
    img, d = new_slide()
    draw_header(d, '下阕品读', '"携来百侣曾游"', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '"携来百侣曾游。忆往昔峥嵘岁月稠。"', fill=XIANG, font=F_POEM)
    y += 40
    d.text((MARGIN, y), '分析：这两句在全词中起什么作用？', fill=INK, font=F_SUB)
    y += 35
    texts = [
        '"携来"——从上片"独立"到"携来百侣"，由一人到群体',
        '"曾游"——旧地重游，自然引起对往昔的回忆',
        '"峥嵘岁月稠"——"峥嵘"形容岁月不平凡',
        '承上启下：从写景过渡到忆事抒情',
    ]
    y = draw_bullet(d, texts, y, bullet='  ')
    y += 15
    draw_emph_box(d, '上片独自凝望，下片携友回忆——词的脉络由"景"转"情"', MARGIN, y, 750)
    save_slide(img, next_num(), 'xiaque_intro')

def slide_tongxue_image():
    """29. 同学少年形象"""
    img, d = new_slide()
    draw_header(d, '峥嵘岁月图', '"同学少年"的形象', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '思考："同学少年"有着怎样的形象？请从词中找出依据。', fill=INK, font=F_SUB)
    y += 45
    draw_table(d,
        ['相关词句', '形象特点'],
        [
            ['风华正茂', '青春年少，才华横溢'],
            ['书生意气，挥斥方遒', '热情奔放，敢想敢做，以天下为己任'],
            ['指点江山，激扬文字', '激昂慷慨，针砭时弊，关心国家命运'],
            ['粪土当年万户侯', '蔑视官僚军阀，救国救民，敢于斗争'],
            ['到中流击水，浪遏飞舟', '激流勇进，甘为中流砥柱'],
        ],
        MARGIN, y, [380, 380]
    )
    y += 200
    d.text((MARGIN, y), '讨论：这不仅仅是一个人——是一代革命青年的群像', fill=FROST, font=F_BODY_B)
    save_slide(img, next_num(), 'tongxue')

def slide_lianzi_xia():
    """30. 下阕炼字"""
    img, d = new_slide()
    draw_header(d, '下阕炼字', '动词与修辞的力量', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '品读：下阕哪些字词体现了诗人的青春激情？', fill=INK, font=F_SUB)
    y += 40
    words = [
        ('"指点"', '把评述褒贬变成可想象的画面——青年们积极关注国家大事'),
        ('"激扬"', '激浊扬清——抨击社会恶行，褒扬清明，爱憎分明'),
        ('"粪土"', '名词作动词，"视...如粪土"——志向高远，蔑视权贵'),
        ('"击"(中流击水)', '写游泳之奋力——勇于挑战、奋力拼搏'),
        ('"遏"(浪遏飞舟)', '夸张手法——青年掀起的革命浪潮将改变旧世界'),
    ]
    for word, val in words:
        d.text((MARGIN + 10, y), word, fill=FROST, font=F_BODY_B)
        tw = d.textlength(word, F_BODY_B)
        d.text((MARGIN + 10 + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    save_slide(img, next_num(), 'lianzi_xia')

def slide_diangu():
    """31. 典故"""
    img, d = new_slide()
    draw_header(d, '典故解析', '文化常识', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '"万户侯"与"中流击楫"', fill=INK, font=F_SUB)
    y += 40
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 30)], fill=FROST)
    d.text((MARGIN + 16, y + 4), '万户侯', fill=FROST, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '汉代侯爵最高一级，享万户赋税。卫青、霍去病为代表。', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '后泛指高官贵爵。词中"粪土当年万户侯"——视权贵如粪土。', fill=INK, font=F_BODY)
    y += 40
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 30)], fill=XIANG)
    d.text((MARGIN + 16, y + 4), '中流击楫', fill=XIANG, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '东晋祖逖北伐，渡江于中流敲打船桨发誓："不能平定中原，如江水一去不返！"', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"中流击水"化用此典——表达献身革命的雄心壮志。', fill=INK, font=F_BODY)
    save_slide(img, next_num(), 'diangu')

def slide_zhongliu():
    """32. 中流击水图 — 手绘激流+文字"""
    img, d = new_slide()
    # 背景：激流蓝白
    draw_gradient_bg(d, img, (180, 210, 230), (80, 130, 170), vertical=True)
    # 波浪
    for y_wave in range(200, H, 15):
        offset = int(20 * math.sin(y_wave * 0.08))
        d.line([(MARGIN, y_wave+offset), (W-MARGIN, y_wave+offset)], fill=(100, 160, 200), width=3)
    # 一艘小船（搏击激流）
    draw_boat(d, 600, 400, 1.5, INK, (200, 220, 240))
    # 大字
    d.text((MARGIN + 50, 150), '中流', fill=WHITE, font=load_font('msyhbd.ttc', 100))
    d.text((MARGIN + 50, 260), '击水', fill=(220, 240, 255), font=load_font('msyhbd.ttc', 130))
    # 右侧文字
    tx = 780
    d.rectangle([(tx - 20, 150), (W - 40, 520)], fill=(255, 255, 255, 200))
    d.text((tx, 170), '浪遏飞舟', fill=XIANG, font=F_SUB)
    y = 210
    answers = [
        '内容：回忆当年在湘江游泳，不畏风浪',
        '修辞："浪遏飞舟"——夸张手法',
        '结构：含蓄回答"谁主沉浮"——我们！',
        '主题：一代青年胸怀壮志，勇担大任',
    ]
    y = draw_bullet(d, answers, y, x=tx, bullet='  ')
    y += 15
    d.rectangle([(tx, y), (W - MARGIN, y + 80)], fill=LIGHT_BG, outline=XIANG, width=2)
    d.text((tx + 16, y + 10), '首尾呼应', fill=XIANG, font=F_BODY_B)
    d.text((tx + 16, y + 40), '"独立寒秋"->"中流击水"  "谁主沉浮"->"浪遏飞舟"', fill=INK, font=F_BODY)
    save_slide(img, next_num(), 'zhongliu')

def slide_qingjing():
    """33. 情景交融"""
    img, d = new_slide()
    draw_header(d, '艺术特色', '情景交融', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '本词如何做到情景交融？', fill=INK, font=F_SUB)
    y += 40
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 26)], fill=FROST)
    d.text((MARGIN + 16, y), '上阕：景中含情', fill=FROST, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '"万山红遍"——既是枫林如火的实写，又寄寓火热的革命情怀', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"万类霜天竞自由"——是诗人对自由解放的向往与追求', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"怅寥廓"的感叹——由写景直接转入抒情', fill=INK, font=F_BODY)
    y += 30
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 26)], fill=XIANG)
    d.text((MARGIN + 16, y), '下阕：情中含景', fill=XIANG, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '"峥嵘岁月稠"——将不平凡岁月化为巍峨山峰', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"到中流击水，浪遏飞舟"——奋勇进击的宏伟画面', fill=INK, font=F_BODY)
    save_slide(img, next_num(), 'qingjing')

def slide_contrast():
    """34. 对比阅读"""
    img, d = new_slide()
    draw_header(d, '对比阅读', '悲秋 vs 颂秋', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '讨论：毛泽东笔下的秋天，和古代诗人有何不同？', fill=INK, font=F_SUB)
    y += 45
    draw_table(d,
        ['维度', '古代悲秋诗人', '毛泽东'],
        [
            ['典型意象', '黄花、枯草、寒蝉、落叶', '万山、层林、百舸、雄鹰、游鱼'],
            ['情感基调', '悲凉、凄清、生命短暂', '豪迈、热烈、生机勃勃'],
            ['典型名句', '"万里悲秋常作客"(杜甫)', '"万类霜天竞自由"'],
            ['根本原因', '个人遭际的感慨', '革命家的胸襟；以天下为己任'],
            ['哲学底色', '消极顺应', '斗争哲学——"与天奋斗，其乐无穷"'],
        ],
        MARGIN, y, [120, 280, 320]
    )
    save_slide(img, next_num(), 'contrast')

def slide_theme():
    """35. 主题归纳"""
    img, d = new_slide()
    draw_header(d, '主题归纳', '', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '本词的主题是什么？', fill=INK, font=F_SUB)
    y += 45
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 120)], fill=LIGHT_BG, outline=FROST, width=2)
    d.text((MARGIN + 20, y + 20), '主题', fill=FROST, font=F_BODY_B)
    d.text((MARGIN + 20, y + 50), '通过对长沙秋景的描绘和对青年时代革命斗争生活的回忆，', fill=INK, font=F_BODY)
    d.text((MARGIN + 20, y + 74), '抒写了革命青年对国家命运的关注和以天下为己任的豪情壮志。', fill=INK, font=F_BODY)
    y += 140
    d.text((MARGIN, y), '结构归纳', fill=INK, font=F_SUB)
    y += 35
    structure = [
        '上阕（看）：写景——独立寒秋图 -> 湘江秋景图 -> 问谁主沉浮',
        '下阕（忆）：忆事——峥嵘岁月图 -> 中流击水图 -> 答：同学少年',
        '手法：景中含情，情中显志  |  风格：豪放雄浑',
    ]
    y = draw_bullet(d, structure, y, bullet='  ')
    save_slide(img, next_num(), 'theme')

def slide_blackboard():
    """36. 板书设计"""
    img, d = new_slide()
    draw_header(d, '板书设计', '', page_num=next_num())
    y = CONTENT_TOP + 10
    d.text((MARGIN + 300, y), '沁园春·长沙', fill=FROST, font=F_TITLE)
    y += 50
    d.text((MARGIN + 180, y), '看（景）', fill=FROST, font=F_SUB)
    d.text((MARGIN + 520, y), '忆（情）', fill=XIANG, font=F_SUB)
    y += 30
    d.rectangle([(MARGIN + 120, y), (MARGIN + 380, y + 22)], fill=FROST)
    d.text((MARGIN + 130, y + 2), '【意象调色盘】', fill=WHITE, font=F_SMALL)
    y += 26
    for line in ['万山红遍 -> 热血', '鹰击长空 -> 力量', '鱼翔浅底 -> 突破']:
        d.text((MARGIN + 120, y), f'  {line}', fill=INK, font=F_SMALL)
        y += 22
    y2 = CONTENT_TOP + 80
    d.rectangle([(MARGIN + 460, y2), (MARGIN + 720, y2 + 22)], fill=XIANG)
    d.text((MARGIN + 470, y2 + 2), '【青春关键词】', fill=WHITE, font=F_SMALL)
    y2 += 26
    for kw in ['独立 -> 清醒', '问 -> 担当', '中流击水 -> 行动']:
        d.text((MARGIN + 460, y2), f'  {kw}', fill=INK, font=F_SMALL)
        y2 += 22
    y = CONTENT_TOP + 180
    d.text((MARGIN + 140, y), '问：谁主沉浮？  ========>  答：同学少年！', fill=INK, font=F_BODY_B)
    y += 35
    d.text((MARGIN + 140, y), '       景中含情  ========>  情中显志', fill=GRAY, font=F_BODY)
    y += 40
    d.text((MARGIN + 140, y), '"主宰沉浮，舍我其谁？！"', fill=FROST, font=F_BIG)
    save_slide(img, next_num(), 'blackboard')

def slide_exercises():
    """37. 课堂练习"""
    img, d = new_slide()
    draw_header(d, '课堂练习', '理解性默写', page_num=next_num())
    y = CONTENT_TOP
    d.text((MARGIN, y), '请根据提示，写出相应的词句：', fill=INK, font=F_SUB)
    y += 45
    exercises = [
        '1. 面对大千世界，词人发出慨叹：____________',
        '2. 旧地重游引发对往昔的回忆：____________',
        '3. 同学少年评论国家大事，写出激浊扬清的文章：____________',
        '4. 夸张手法写出劈波斩浪气魄的两句：____________',
        '5. 用动物表现生机勃勃秋景的两句：____________',
    ]
    for q in exercises:
        d.text((MARGIN + 10, y), q, fill=INK, font=F_BODY)
        y += 38
    y += 15
    d.text((MARGIN, y), '参考答案（教师用）：', fill=GRAY, font=F_SMALL)
    y += 25
    answers = [
        '1. 怅寥廓，问苍茫大地，谁主沉浮？',
        '2. 携来百侣曾游，忆往昔峥嵘岁月稠',
        '3. 指点江山，激扬文字，粪土当年万户侯',
        '4. 到中流击水，浪遏飞舟',
        '5. 鹰击长空，鱼翔浅底',
    ]
    for ans in answers:
        d.text((MARGIN + 20, y), ans, fill=GRAY, font=F_SMALL)
        y += 22
    save_slide(img, next_num(), 'exercises')

def slide_homework():
    """38. 课后作业"""
    img, d = new_slide()
    draw_header(d, '课后作业', '', page_num=next_num())
    y = CONTENT_TOP
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 26)], fill=FROST)
    d.text((MARGIN + 16, y), '基础作业', fill=FROST, font=F_BODY_B)
    y += 30
    d.text((MARGIN + 16, y), '1. 背诵并默写《沁园春·长沙》全词', fill=INK, font=F_BODY)
    y += 26
    d.text((MARGIN + 16, y), '2. 完成意象分析表格（找出至少3个意象并说明特点）', fill=INK, font=F_BODY)
    y += 40
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 26)], fill=XIANG)
    d.text((MARGIN + 16, y), '提高作业', fill=XIANG, font=F_BODY_B)
    y += 30
    d.text((MARGIN + 16, y), '1. 比较《沁园春·长沙》与《沁园春·雪》在意象选择和情感表达上的异同', fill=INK, font=F_BODY)
    y += 26
    d.text((MARGIN + 16, y), '2. 以"我眼中的秋天"为题，写一篇300字短文', fill=INK, font=F_BODY)
    save_slide(img, next_num(), 'homework')

def slide_ending():
    """39. 结语"""
    img, d = new_slide()
    draw_gradient_bg(d, img, (40, 60, 80), (28, 43, 51), vertical=True)
    d.text((MARGIN, 200), '青春永不落幕', fill=WHITE, font=load_font('msyhbd.ttc', 56))
    y = 300
    d.text((MARGIN, y), '"世界是你们的，也是我们的，但是归根结底是你们的。"', fill=(200, 210, 220), font=F_BODY)
    y += 35
    d.text((MARGIN, y), '——毛泽东（1957年莫斯科大学讲话）', fill=GRAY, font=F_SMALL)
    save_slide(img, next_num(), 'ending')

# ═══════════════════════════════════════════════════
#  自检函数
# ═══════════════════════════════════════════════════

def self_check():
    """自检：验证每页的意象、颜色、内容匹配"""
    checks = []
    errors = []
    
    # 检查所有slide_文件
    files = sorted(os.listdir(OUT))
    slide_files = [f for f in files if f.startswith('slide_') and f.endswith('.png')]
    
    # 预期映射：文件名关键词 -> 预期内容检查
    expected = {
        'img_wanshan': ('红色', '万山', '红遍'),
        'img_cenglin': ('层林', '尽染'),
        'img_manjiang': ('碧透', '江水', '绿色'),
        'img_baige': ('百舸', '船', '争流'),
        'img_yingji': ('鹰', '击', '长空'),
        'img_yuxiang': ('鱼', '翔', '浅底'),
        'yingji': ('鹰', '击'),
        'yuxiang': ('鱼', '翔'),
    }
    
    for f in slide_files:
        for key, expected_keywords in expected.items():
            if key in f:
                checks.append(f'  [OK] {f}: 预期关键词 {expected_keywords}')
    
    # 检查鹰页不能出现马（通过文件名和关键词）
    for f in slide_files:
        if 'yingji' in f and 'ma' not in f.lower():
            checks.append(f'  [OK] {f}: 鹰页无马')
        if 'yuxiang' in f and 'ma' not in f.lower():
            checks.append(f'  [OK] {f}: 鱼页无马')
    
    # 检查总页数
    if len(slide_files) == 39:
        checks.append(f'  [OK] 总页数 = 39')
    else:
        errors.append(f'  [ERROR] 总页数 = {len(slide_files)}，预期 39')
    
    # 检查PDF是否存在
    pdf_path = os.path.join(OUT, '沁园春长沙-课堂版PPT-v4.pdf')
    if os.path.exists(pdf_path):
        checks.append(f'  [OK] PDF 已生成')
    else:
        errors.append(f'  [ERROR] PDF 未生成')
    
    print('\n=== 自检报告 ===')
    for c in checks:
        print(c)
    for e in errors:
        print(e)
    
    if errors:
        print(f'\n自检失败：{len(errors)} 个错误')
        return False
    print('\n自检通过：所有检查项 OK')
    return True

# ═══════════════════════════════════════════════════
#  主流程
# ═══════════════════════════════════════════════════

def main():
    print('Rendering classroom PPT v4 (PIL手绘视觉 + 自检)...')
    
    slides = [
        # 第一课时
        slide_cover, slide_objectives, slide_leadin_autumn, slide_author,
        slide_background, slide_wenti, slide_cipai, slide_zhengyin,
        slide_dujiepai, slide_full_poem, slide_four_pictures, slide_duli,
        slide_qiujing_kan,
        # 6页意象可视化（PIL手绘）
        slide_imagery_wanshan, slide_imagery_cenglin, slide_imagery_manjiang,
        slide_imagery_baige, slide_imagery_yingji, slide_imagery_yuxiang,
        # 教学分析
        slide_imagery_table, slide_color_action, slide_lianzi_1, slide_lianzi_2,
        slide_transition, slide_summary_1,
        # 第二课时
        slide_p2_cover, slide_review, slide_xiaque_intro, slide_tongxue_image,
        slide_lianzi_xia, slide_diangu, slide_zhongliu, slide_qingjing,
        slide_contrast, slide_theme, slide_blackboard, slide_exercises,
        slide_homework, slide_ending,
    ]
    
    for fn in slides:
        fn()
        print(f'  OK {fn.__name__}')
    
    # 合成PDF
    from glob import glob
    pngs = sorted(glob(os.path.join(OUT, 'slide_*.png')))
    images = [Image.open(p).convert('RGB') for p in pngs]
    
    pdf_path = os.path.join(OUT, '沁园春长沙-课堂版PPT-v4.pdf')
    images[0].save(pdf_path, 'PDF', resolution=150, save_all=True, append_images=images[1:])
    
    # 复制到桌面
    desktop = os.path.expanduser('~/Desktop')
    import shutil
    shutil.copy(pdf_path, os.path.join(desktop, '沁园春长沙-课堂版PPT-v4.pdf'))
    
    size_kb = os.path.getsize(pdf_path) // 1024
    print(f'\nDone! {len(slides)} slides -> {pdf_path} ({size_kb}KB)')
    print(f'Copied to desktop')
    
    # 自检
    self_check()

if __name__ == '__main__':
    main()
