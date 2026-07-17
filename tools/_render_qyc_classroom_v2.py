#!/usr/bin/env python3
"""
课堂版PPT渲染器 v2 —— 沁园春·长沙
基于真实公开课课件结构重写：白底+表格+教学动作+逐页分析
"""

from PIL import Image, ImageDraw, ImageFont
import os, sys

# ── 输出目录 ──
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cn_qyc_classroom_v2')
os.makedirs(OUT, exist_ok=True)

# ── 画布 ──
W, H = 1280, 720

# ── 字体 ──
FONT_DIR = 'C:/Windows/Fonts'
def load_font(name, size):
    path = os.path.join(FONT_DIR, name)
    return ImageFont.truetype(path, size)

F_TITLE   = load_font('msyhbd.ttc', 36)    # 页面主标题
F_SUB     = load_font('msyhbd.ttc', 24)    # 副标题
F_BODY    = load_font('msyh.ttc', 20)      # 正文
F_BODY_B  = load_font('msyhbd.ttc', 20)    # 正文加粗
F_SMALL   = load_font('msyh.ttc', 16)      # 小字/注释
F_BIG     = load_font('msyhbd.ttc', 48)    # 大字展示
F_POEM    = load_font('msyh.ttc', 22)      # 诗句
F_TABLE   = load_font('msyh.ttc', 18)      # 表格文字
F_TABLE_B = load_font('msyhbd.ttc', 18)    # 表格加粗

# ── 配色 ──
INK      = (28, 43, 51)       # 墨蓝 #1C2B33
WHITE    = (255, 255, 255)
FROST    = (178, 58, 42)      # 霜红 #B23A2A
XIANG    = (46, 125, 107)     # 湘碧 #2E7D6B
ACCENT   = (194, 112, 61)     # 陶土橙 #C2703D
LIGHT_BG = (245, 242, 237)    # 暖纸白
GRAY     = (128, 128, 128)
LIGHT_GRAY = (220, 220, 220)
TABLE_HDR = (28, 43, 51)      # 表头底色
TABLE_ALT = (240, 245, 250)   # 表格交替行
BORDER    = (180, 180, 180)
HIGHLIGHT = (255, 240, 220)   # 高亮底色

# ── 布局常量 ──
MARGIN = 80
HEADER_H = 80
CONTENT_TOP = HEADER_H + 20

# ── 辅助函数 ──
def new_slide():
    """创建空白幻灯片"""
    img = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(img)
    return img, d

def draw_header(d, title, subtitle=None, page_num=None):
    """绘制页面顶部标题栏"""
    # 顶部色条
    d.rectangle([(0, 0), (W, 5)], fill=INK)
    d.rectangle([(0, 5), (W, HEADER_H)], fill=INK)
    d.text((MARGIN, 18), title, fill=WHITE, font=F_TITLE)
    if subtitle:
        d.text((MARGIN + d.textlength(title, F_TITLE) + 30, 22), subtitle, fill=(180,190,200), font=F_SUB)
    if page_num:
        tw = d.textlength(str(page_num), F_SMALL)
        d.text((W - MARGIN - tw, 30), str(page_num), fill=(150,160,170), font=F_SMALL)

def draw_body_text(d, lines, y_start, font=None, fill=None, lh=32, x=MARGIN):
    """绘制正文文本行"""
    f = font or F_BODY
    c = fill or INK
    y = y_start
    for line in lines:
        d.text((x, y), line, fill=c, font=f)
        y += lh
    return y

def draw_bullet(d, items, y_start, font=None, fill=None, lh=30, x=MARGIN, bullet='•'):
    """绘制带要点的列表"""
    f = font or F_BODY
    c = fill or INK
    y = y_start
    for item in items:
        d.text((x, y), f'{bullet} ', fill=c, font=f)
        tw = d.textlength(f'{bullet} ', f)
        d.text((x + tw, y), item, fill=c, font=f)
        y += lh
    return y

def draw_section_title(d, title, y):
    """绘制小节标题——带左侧色条"""
    d.rectangle([(MARGIN - 10, y), (MARGIN - 4, y + 32)], fill=FROST)
    d.text((MARGIN + 8, y), title, fill=INK, font=F_SUB)
    return y + 42

def draw_table(d, headers, rows, x, y, col_widths=None, header_color=None, font_body=None, font_header=None):
    """绘制表格"""
    fh = font_header or F_TABLE_B
    fb = font_body or F_TABLE
    hc = header_color or TABLE_HDR
    row_h = 32
    
    if col_widths is None:
        col_widths = [150] * len(headers)
    
    total_w = sum(col_widths)
    
    # 表头
    cx = x
    d.rectangle([(x, y), (x + total_w, y + row_h)], fill=hc)
    for i, h in enumerate(headers):
        d.text((cx + 8, y + 6), h, fill=WHITE, font=fh)
        cx += col_widths[i]
    y += row_h
    
    # 数据行
    for ri, row in enumerate(rows):
        bg = TABLE_ALT if ri % 2 == 0 else WHITE
        d.rectangle([(x, y), (x + total_w, y + row_h)], fill=bg)
        cx = x
        for i, cell in enumerate(row):
            d.text((cx + 8, y + 6), str(cell), fill=INK, font=fb)
            cx += col_widths[i]
        y += row_h
    
    # 外框
    d.rectangle([(x, y - row_h * (len(rows)+1)), (x + total_w, y)], outline=BORDER, width=1)
    return y

def draw_card(d, x, y, w, h, title, content_lines, accent_color=None, font_title=None, font_body=None):
    """绘制带标题的卡片"""
    ac = accent_color or FROST
    ft = font_title or F_BODY_B
    fb = font_body or F_BODY
    
    # 卡片背景
    d.rectangle([(x, y), (x + w, y + h)], fill=LIGHT_BG, outline=LIGHT_GRAY, width=1)
    # 顶部色条
    d.rectangle([(x, y), (x + w, y + 4)], fill=ac)
    # 标题
    d.text((x + 16, y + 12), title, fill=ac, font=ft)
    # 内容
    cy = y + 40
    for line in content_lines:
        d.text((x + 16, cy), line, fill=INK, font=fb)
        cy += 26
    return y + h

def draw_emph_box(d, text, x, y, w, fill_color=None):
    """强调框"""
    fc = fill_color or HIGHLIGHT
    d.rectangle([(x, y), (x + w, y + 40)], fill=fc, outline=ACCENT, width=1)
    d.text((x + 16, y + 9), text, fill=INK, font=F_BODY_B)

def draw_poem_line(d, text, x, y, font=None, fill=None):
    """绘制诗句行"""
    f = font or F_POEM
    c = fill or INK
    d.text((x, y), text, fill=c, font=f)
    return y + 30

def save_slide(img, num, name):
    img.save(os.path.join(OUT, f'slide_{num:02d}_{name}.png'))

# ── 页数 ──
slide_num = [0]
def next_num():
    slide_num[0] += 1
    return slide_num[0]

# ═══════════════════════════════════════════════════
#  第一课时：走进《沁园春·长沙》
# ═══════════════════════════════════════════════════

def slide_cover():
    """1. 封面"""
    img, d = new_slide()
    # 背景：淡淡的暖纸色
    d.rectangle([(0, 0), (W, H)], fill=LIGHT_BG)
    # 顶部大色块
    d.rectangle([(0, 0), (W, 280)], fill=INK)
    # 装饰线
    d.rectangle([(0, 280), (W, 284)], fill=FROST)
    # 主标题
    d.text((MARGIN, 100), '沁园春·长沙', fill=WHITE, font=ImageFont.truetype(os.path.join(FONT_DIR, 'msyhbd.ttc'), 72))
    # 作者
    d.text((MARGIN + d.textlength('沁园春·长沙', ImageFont.truetype(os.path.join(FONT_DIR, 'msyhbd.ttc'), 72)) + 30, 120), '毛泽东', fill=(200,210,220), font=F_TITLE)
    # 课时标签
    d.rectangle([(MARGIN, 210), (MARGIN + 160, 248)], fill=FROST)
    d.text((MARGIN + 20, 218), '第一课时', fill=WHITE, font=F_BODY_B)
    # 底部信息
    d.text((MARGIN, 340), '统编版高中语文必修上册 · 第一单元', fill=GRAY, font=F_BODY)
    d.text((MARGIN, 380), '走进《沁园春·长沙》——知人论世·诵读感知·意象品析', fill=INK, font=F_SUB)
    # 装饰红叶
    for i in range(3):
        x = W - 120 - i*80
        y = 400 + i*60
        d.ellipse([(x-15, y-15), (x+15, y+15)], fill=FROST)
        d.ellipse([(x-8, y-12), (x+8, y+12)], fill=ACCENT)
        d.ellipse([(x-10, y-8), (x+10, y+8)], fill=FROST)
    
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
    """3. 导入：自古文人多悲秋"""
    img, d = new_slide()
    draw_header(d, '导入新课', '自古文人多悲秋', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '思考：古人笔下的秋天是什么样的？', fill=INK, font=F_SUB)
    y += 50
    
    # 悲秋组
    autumn_poems = [
        ('宋玉《九辨》', '"悲哉！秋之为气也，萧瑟兮草木摇落而变衰"', FROST),
        ('杜甫《登高》', '"万里悲秋常作客，百年多病独登台"', FROST),
        ('欧阳修《秋声赋》', '"噫嘻悲哉！此秋声也"', FROST),
    ]
    # 颂秋组
    autumn_poems2 = [
        ('刘禹锡《秋词》', '"自古逢秋悲寂寥，我言秋日胜春朝"', XIANG),
    ]
    
    w = 520
    d.rectangle([(MARGIN, y), (MARGIN + w, y + 20)], fill=FROST)
    d.text((MARGIN + 10, y + 2), '悲秋传统', fill=WHITE, font=F_SMALL)
    y += 30
    for author, poem, col in autumn_poems:
        d.text((MARGIN + 10, y), f'  {author}', fill=col, font=F_BODY_B)
        y += 24
        d.text((MARGIN + 10, y), f'  {poem}', fill=INK, font=F_BODY)
        y += 28
    y += 10
    
    d.rectangle([(MARGIN, y), (MARGIN + w, y + 20)], fill=XIANG)
    d.text((MARGIN + 10, y + 2), '例外：秋的赞歌', fill=WHITE, font=F_SMALL)
    y += 30
    for author, poem, col in autumn_poems2:
        d.text((MARGIN + 10, y), f'  {author}', fill=col, font=F_BODY_B)
        y += 24
        d.text((MARGIN + 10, y), f'  {poem}', fill=INK, font=F_BODY)
        y += 28
    
    y += 30
    draw_emph_box(d, '那么，毛泽东笔下的秋天，又是怎样的一番景象？', MARGIN, y, 700)
    
    save_slide(img, next_num(), 'leadin')

def slide_author():
    """4. 知人论世：毛泽东简介"""
    img, d = new_slide()
    draw_header(d, '知人论世', '毛泽东（1893—1976）', page_num=next_num())
    y = CONTENT_TOP
    
    # 左侧文字
    info = [
        ('字', '润之，笔名子任'),
        ('籍贯', '湖南湘潭韶山冲'),
        ('身份', '无产阶级革命家、战略家、理论家'),
        ('地位', '中国共产党、中国人民解放军和中华人民共和国的主要缔造者'),
        ('文学', '诗人、书法家——豪放派代表'),
    ]
    for label, val in info:
        d.text((MARGIN, y), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((MARGIN + tw, y), val, fill=INK, font=F_BODY)
        y += 34
    
    y += 20
    d.text((MARGIN, y), '名句选摘', fill=FROST, font=F_SUB)
    y += 30
    quotes = [
        '"雄关漫道真如铁，而今迈步从头越"',
        '"天若有情天亦老，人间正道是沧桑"',
        '"一万年太久，只争朝夕"',
        '"不到长城非好汉"',
    ]
    for q in quotes:
        d.text((MARGIN + 10, y), f'  {q}', fill=INK, font=F_BODY)
        y += 28
    
    # 右侧：手绘毛泽东轮廓框
    rx = 780
    d.rectangle([(rx, CONTENT_TOP), (W - MARGIN, CONTENT_TOP + 400)], fill=LIGHT_BG, outline=LIGHT_GRAY)
    d.text((rx + 30, CONTENT_TOP + 40), '[青年毛泽东像]', fill=GRAY, font=F_BODY)
    d.text((rx + 10, CONTENT_TOP + 100), '• 1925年，32岁', fill=INK, font=F_BODY)
    d.text((rx + 10, CONTENT_TOP + 130), '• 重游橘子洲', fill=INK, font=F_BODY)
    d.text((rx + 10, CONTENT_TOP + 160), '• 写下《沁园春·长沙》', fill=INK, font=F_BODY)
    
    # 手绘头像区域（简笔画占位）
    d.ellipse([(rx + 60, CONTENT_TOP + 210), (rx + 260, CONTENT_TOP + 390)], fill=(200, 190, 175))
    d.text((rx + 90, CONTENT_TOP + 320), '毛泽东', fill=(140,130,120), font=F_SUB)
    
    save_slide(img, next_num(), 'author')

def slide_background():
    """5. 写作背景"""
    img, d = new_slide()
    draw_header(d, '写作背景', '1925年·长沙', page_num=next_num())
    y = CONTENT_TOP
    
    # 时间线
    timeline = [
        ('1925年初', '毛泽东从上海回到韶山，开展农民运动', '▶'),
        ('1925年夏', '创建湖南第一个农村党支部——韶山支部', '▶'),
        ('1925年8月', '湖南省长赵恒惕下令逮捕毛泽东', '▶'),
        ('1925年10月', '离开韶山，途经长沙，重游橘子洲', '★'),
        ('1925年秋', '写下《沁园春·长沙》', '✦'),
    ]
    
    for date, event, mark in timeline:
        col = FROST if mark == '★' else ACCENT if mark == '✦' else INK
        d.text((MARGIN, y), f'{mark} {date}', fill=col, font=F_BODY_B)
        tw = d.textlength(f'{mark} {date}  ', F_BODY_B)
        d.text((MARGIN + tw, y), event, fill=INK, font=F_BODY)
        y += 34
    
    y += 20
    # 时代背景框
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 100)], fill=LIGHT_BG, outline=ACCENT, width=2)
    d.text((MARGIN + 16, y + 10), '时代背景', fill=ACCENT, font=F_BODY_B)
    d.text((MARGIN + 16, y + 38), '全国工农运动风起云涌 · 五卅运动爆发 · 北伐战争前夕', fill=INK, font=F_BODY)
    d.text((MARGIN + 16, y + 62), '革命由哪个阶级领导？——成为党内外斗争的焦点', fill=FROST, font=F_BODY)
    
    y += 120
    draw_emph_box(d, '面对如画的秋色和大好的革命形势，32岁的毛泽东心潮澎湃，写下此词', MARGIN, y, 750)
    
    save_slide(img, next_num(), 'background')

def slide_wenti():
    """6. 文体知识：词"""
    img, d = new_slide()
    draw_header(d, '文体知识', '词——"长短句"', page_num=next_num())
    y = CONTENT_TOP
    
    # 定义
    d.text((MARGIN, y), '什么是"词"？', fill=FROST, font=F_SUB)
    y += 30
    d.text((MARGIN + 10, y), '词，萌芽于南朝，形成于唐，盛行于宋。配合宴乐歌唱，又称"曲子词""长短句""诗余"。', fill=INK, font=F_BODY)
    y += 28
    d.text((MARGIN + 10, y), '特点：调有定格，句有定数，字有定声。作者按照词牌规定的格式去创作，称为"填词"。', fill=INK, font=F_BODY)
    y += 40
    
    # 三大分类表
    d.text((MARGIN, y), '词的分类', fill=FROST, font=F_SUB)
    y += 35
    draw_table(d,
        ['分类标准', '类别', '说明'],
        [
            ['按字数', '小令（≤58字）', '篇幅最短'],
            ['按字数', '中调（59-90字）', '中等篇幅'],
            ['按字数', '长调（≥91字）', '《沁园春·长沙》114字 ⊲ 属长调'],
            ['按段落', '单调', '一段'],
            ['按段落', '双调', '两段（两阕），最常见'],
            ['按段落', '三叠/四叠', '三段或四段'],
            ['按风格', '豪放派', '苏轼、辛弃疾——气势豪放、意境雄浑'],
            ['按风格', '婉约派', '柳永、李清照——清丽含蓄、婉转细腻'],
        ],
        MARGIN, y, [120, 200, 540]
    )
    
    save_slide(img, next_num(), 'wenti')

def slide_cipai():
    """7. 词牌·沁园春"""
    img, d = new_slide()
    draw_header(d, '词牌知识', '"沁园春"的来历', page_num=next_num())
    y = CONTENT_TOP
    
    # 词牌简介
    d.text((MARGIN, y), '词牌 vs 标题', fill=FROST, font=F_SUB)
    y += 35
    items = [
        '词牌 = 词的格式名称（决定字数、句数、平仄声韵），与内容无关',
        '标题 = 词的内容的集中体现（"长沙"表明描写对象与地点）',
        '"沁园春"：又名"洞庭春色""东仙""念离群"',
    ]
    y = draw_bullet(d, items, y, bullet='•')
    
    y += 25
    # 典故框
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 140)], fill=LIGHT_BG, outline=ACCENT, width=2)
    d.text((MARGIN + 16, y + 10), '典故："沁园"的由来', fill=ACCENT, font=F_BODY_B)
    d.text((MARGIN + 16, y + 38), '相传"沁园"为东汉明帝女儿沁水公主的园林。后外戚窦宪仗势强夺此园，', fill=INK, font=F_BODY)
    d.text((MARGIN + 16, y + 62), '有人作诗咏其事。后人以"沁园春"为词牌，寄寓世事变迁之感。', fill=INK, font=F_BODY)
    d.text((MARGIN + 16, y + 90), '《后汉书·窦宪传》记载此事。毛泽东以"沁园春"为词牌，暗含对旧世界的批判。', fill=FROST, font=F_SMALL)
    
    save_slide(img, next_num(), 'cipai')

def slide_zhengyin():
    """8. 正字音"""
    img, d = new_slide()
    draw_header(d, '朗读准备', '辨字正音', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '请正确读出下列红色字的读音', fill=INK, font=F_SUB)
    y += 40
    
    words = [
        ('沁（qìn）', '园春', '百舸（gě）', '争流'),
        ('寥廓（liáo kuò）', '', '方遒（qiú）', ''),
        ('峥嵘（zhēng róng）', '', '浪遏（è）', '飞舟'),
        ('惆怅（chóu chàng）', '', '橘子（jú）', '洲'),
    ]
    
    for a, b, c, d_text in words:
        d.text((MARGIN, y), a, fill=FROST, font=F_BODY_B)
        tw1 = d.textlength(a, F_BODY_B)
        if b:
            d.text((MARGIN + tw1, y), b, fill=INK, font=F_BODY)
            tw1 += d.textlength(b, F_BODY)
        
        d.text((MARGIN + 450, y), c, fill=FROST, font=F_BODY_B)
        tw2 = d.textlength(c, F_BODY_B)
        if d_text:
            d.text((MARGIN + 450 + tw2, y), d_text, fill=INK, font=F_BODY)
        y += 38
    
    y += 20
    d.text((MARGIN, y), '注意：多音字与易错字', fill=FROST, font=F_SUB)
    y += 32
    notes = [
        ('"看"（kàn）', '：领字，统领以下七句，读时稍作停顿'),
        ('"怅"（chàng）', '：惆怅感慨，非"怅惘"的轻飘'),
        ('"舸"（gě）', '：大船，非"可"音'),
        ('"遏"（è）', '：阻止，非"喝"音'),
    ]
    for word, note in notes:
        d.text((MARGIN + 10, y), word, fill=FROST, font=F_BODY_B)
        tw = d.textlength(word, F_BODY_B)
        d.text((MARGIN + 10 + tw, y), note, fill=INK, font=F_BODY)
        y += 28
    
    save_slide(img, next_num(), 'zhengyin')

def slide_dujiepai():
    """9. 朗读指导：节拍"""
    img, d = new_slide()
    draw_header(d, '朗读指导', '读出节拍韵律', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '节拍规则', fill=FROST, font=F_SUB)
    y += 35
    
    rules = [
        ('四字句 → 二二式', '独立 / 寒秋，湘江 / 北去'),
        ('  （例外）', '橘子洲 / 头（三一式）'),
        ('五字句 → 一四式', '恰 / 同学少年，问 / 苍茫大地'),
        ('七字句 → 二五式', '粪土 / 当年万户侯'),
        ('七字句 → 四三式', '万类霜天 / 竞自由'),
        ('八字句 → 三二三式', '忆往昔 / 峥嵘 / 岁月稠'),
    ]
    
    for rule, example in rules:
        if rule.startswith('  '):
            d.text((MARGIN + 30, y), rule.strip(), fill=GRAY, font=F_SMALL)
            tw = d.textlength(rule.strip(), F_SMALL)
            d.text((MARGIN + 30 + tw, y), f'  —— {example}', fill=INK, font=F_BODY)
        else:
            d.text((MARGIN + 10, y), rule, fill=FROST, font=F_BODY_B)
            tw = d.textlength(rule, F_BODY_B)
            d.text((MARGIN + 10 + tw, y), f'  —— {example}', fill=INK, font=F_BODY)
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
    """10. 全词展示与齐读"""
    img, d = new_slide()
    draw_header(d, '朗读课文', '齐读全词', page_num=next_num())
    y = CONTENT_TOP - 10
    
    # 上阕
    d.text((MARGIN, y), '上  阕', fill=FROST, font=F_SUB)
    y += 32
    shang_lines = [
        '独立寒秋，湘江北去，橘子洲头。',
        '看万山红遍，层林尽染；漫江碧透，百舸争流。',
        '鹰击长空，鱼翔浅底，万类霜天竞自由。',
        '怅寥廓，问苍茫大地，谁主沉浮？',
    ]
    for line in shang_lines:
        d.text((MARGIN + 20, y), line, fill=INK, font=F_POEM)
        y += 34
    
    y += 10
    # 分隔线
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=LIGHT_GRAY, width=1)
    y += 10
    
    # 下阕
    d.text((MARGIN, y), '下  阕', fill=XIANG, font=F_SUB)
    y += 32
    xia_lines = [
        '携来百侣曾游。忆往昔峥嵘岁月稠。',
        '恰同学少年，风华正茂；书生意气，挥斥方遒。',
        '指点江山，激扬文字，粪土当年万户侯。',
        '曾记否，到中流击水，浪遏飞舟？',
    ]
    for line in xia_lines:
        d.text((MARGIN + 20, y), line, fill=INK, font=F_POEM)
        y += 34
    
    save_slide(img, next_num(), 'full_poem')

def slide_four_pictures():
    """11. 整体感知：四幅图"""
    img, d = new_slide()
    draw_header(d, '整体感知', '全词四幅图画', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '思考：这首词按内容可划分为哪四幅图画？', fill=INK, font=F_SUB)
    y += 50
    
    # 四幅图卡片
    cards = [
        ('独立寒秋图', '独立寒秋\n湘江北去\n橘子洲头', FROST),
        ('湘江秋景图', '看万山红遍→鹰击长空\n→万类霜天竞自由', XIANG),
        ('峥嵘岁月图', '恰同学少年→\n粪土当年万户侯', ACCENT),
        ('中流击水图', '到中流击水\n浪遏飞舟', INK),
    ]
    
    cx = MARGIN
    cw = 260
    gap = 20
    for title, desc, col in cards:
        d.rectangle([(cx, y), (cx + cw, y + 180)], fill=LIGHT_BG, outline=col, width=2)
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
    draw_emph_box(d, '诗眼：上阕"看"字领起   |   下阕"忆"字领起   |   过片"怅寥廓，问苍茫大地，谁主沉浮？"', MARGIN, y, 750)
    
    save_slide(img, next_num(), 'four_pics')

def slide_duli():
    """12. 上阕分析：独立寒秋图"""
    img, d = new_slide()
    draw_header(d, '上阕品读', '独立寒秋图', page_num=next_num())
    y = CONTENT_TOP
    
    # 诗句展示
    d.text((MARGIN, y), '"独立寒秋，湘江北去，橘子洲头"', fill=FROST, font=F_POEM)
    y += 40
    
    # 分析
    d.text((MARGIN, y), '分析：这一句交代了哪些内容？', fill=INK, font=F_SUB)
    y += 38
    
    analysis = [
        ('时间', '寒秋（晚秋时节）'),
        ('地点', '橘子洲头（长沙湘江中的沙洲）'),
        ('环境', '湘江北去（江水滔滔向北流）'),
        ('人物', '"独立"（独自伫立，天地之间一尊伟岸身躯）'),
    ]
    
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 180)], fill=LIGHT_BG, outline=LIGHT_GRAY)
    ly = y + 10
    for label, val in analysis:
        d.text((MARGIN + 20, ly), f'{label}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{label}：', F_BODY_B)
        d.text((MARGIN + 20 + tw, ly), val, fill=INK, font=F_BODY)
        ly += 38
    
    y += 190
    d.text((MARGIN, y), '倒装句式：正常语序应为"寒秋，（我）独立橘子洲头，（望）湘江北去"', fill=GRAY, font=F_SMALL)
    y += 30
    draw_emph_box(d, '"独立"非孤独——是深思的形象、高瞻远瞩的姿态、思接千载视通万里的气度', MARGIN, y, 750)
    
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
    
    # 视角分析
    d.text((MARGIN, y), '诗人的观察视角变化', fill=INK, font=F_SUB)
    y += 35
    perspectives = [
        ('远眺', '万山红遍，层林尽染 —— 远景，色彩浓烈'),
        ('近观', '漫江碧透 —— 中景，江水清澈'),
        ('近视', '百舸争流 —— 近景，船只如梭'),
        ('仰视', '鹰击长空 —— 向上，矫健有力'),
        ('俯瞰', '鱼翔浅底 —— 向下，轻快自由'),
    ]
    for view, desc in perspectives:
        d.text((MARGIN + 10, y), f'{view}：', fill=FROST, font=F_BODY_B)
        tw = d.textlength(f'{view}：', F_BODY_B)
        d.text((MARGIN + 10 + tw, y), desc, fill=INK, font=F_BODY)
        y += 30
    
    y += 15
    draw_emph_box(d, '由远及近、由上到下、动静结合——如电影镜头般逐层推进', MARGIN, y, 750)
    
    save_slide(img, next_num(), 'kan')

def slide_imagery_table():
    """14. 意象分析表"""
    img, d = new_slide()
    draw_header(d, '湘江秋景图', '意象分析表', page_num=next_num())
    y = CONTENT_TOP - 10
    
    d.text((MARGIN, y), '思考：诗人选取了哪些意象？这些意象有什么特点？请完成表格。', fill=INK, font=F_SUB)
    y += 40
    
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
    """15. 意象美感：色彩+动态"""
    img, d = new_slide()
    draw_header(d, '意象品析', '色彩美与动态美', page_num=next_num())
    y = CONTENT_TOP
    
    # 色彩美
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
    
    # 动态美
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
    draw_emph_box(d, '康德："灌注了生气的形象"——这些意象不是客观白描，而是融入了诗人对自由解放的向往', MARGIN, y, 750)
    
    save_slide(img, next_num(), 'color_action')

def slide_lianzi_1():
    """16. 炼字品析（上）"""
    img, d = new_slide()
    draw_header(d, '炼字品析', '"击"与"翔"的精妙', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '思考：为什么用"击"不用"飞"？为什么用"翔"不用"游"？', fill=INK, font=F_SUB)
    y += 45
    
    # 对比分析
    draw_table(d,
        ['用字', '本义', '在词中的效果', '替换后的效果'],
        [
            ['击（鹰击长空）', '搏击、冲击', '写出鹰的矫健勇猛、迅猛有力、搏击风云的气势', '"飞"——只写动作，无力量感'],
            ['翔（鱼翔浅底）', '盘旋飞翔', '写鱼如鸟般轻快自由、欢快自在；浅底而有翔，更显水清', '"游"——平淡，无灵动之美'],
        ],
        MARGIN, y, [140, 150, 300, 170]
    )
    
    y += 110
    d.text((MARGIN, y), '结论：', fill=FROST, font=F_BODY_B)
    d.text((MARGIN + 80, y), '"击""翔"二字，赋予鹰和鱼以人的精神气质——勇敢、自由、奋进', fill=INK, font=F_BODY)
    y += 35
    d.text((MARGIN, y), '这就是毛泽东笔下的秋天：万物都充满了斗争精神和生命力！', fill=FROST, font=F_BODY_B)
    
    save_slide(img, next_num(), 'lianzi_1')

def slide_lianzi_2():
    """17. 炼字品析（下）"""
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
    d.text((MARGIN + 16, y + 10), '小结：上阕炼字精妙', fill=FROST, font=F_BODY_B)
    d.text((MARGIN + 16, y + 40), '"击""翔""竞"三个动词，从鹰的搏击→鱼的自由→万物的竞发，层层推进，渐入高潮', fill=INK, font=F_BODY)
    
    save_slide(img, next_num(), 'lianzi_2')

def slide_transition():
    """18. 过渡：谁主沉浮"""
    img, d = new_slide()
    draw_header(d, '承上启下', '"谁主沉浮"', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '"怅寥廓，问苍茫大地，谁主沉浮？"', fill=FROST, font=F_POEM)
    y += 45
    
    d.text((MARGIN, y), '思考：这三句在全词中起什么作用？', fill=INK, font=F_SUB)
    y += 38
    
    analysis_texts = [
        '"怅"——不是消沉，是面对壮阔秋景而生的深沉感慨',
        '"寥廓"——宇宙的广阔，反衬出思考的宏大',
        '"问苍茫大地，谁主沉浮"——从写景转入抒情，是全词的枢纽',
        '这一问，承上阕之景，启下阕之情，是"过片"之笔',
    ]
    y = draw_bullet(d, analysis_texts, y, bullet='  ')
    
    y += 20
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 80)], fill=LIGHT_BG, outline=INK, width=2)
    d.text((MARGIN + 16, y + 10), '深层理解', fill=INK, font=F_BODY_B)
    d.text((MARGIN + 16, y + 40), '"谁主沉浮"不仅是问自然——更是问：中国的命运由谁主宰？革命的前途谁来引领？', fill=FROST, font=F_BODY)
    
    save_slide(img, next_num(), 'transition')

def slide_summary_1():
    """19. 第一课时小结"""
    img, d = new_slide()
    draw_header(d, '第一课时小结', '', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '本课时我们学习了：', fill=INK, font=F_SUB)
    y += 40
    
    summary_items = [
        '词的文体知识（词牌、分类、特点）',
        '毛泽东的生平与《沁园春·长沙》的写作背景',
        '生字词读音与朗读节拍韵律',
        '全词四幅图画结构',
        '上阕意象分析——色彩美与动态美',
        '炼字品析——"击""翔""竞"的精妙',
    ]
    y = draw_bullet(d, summary_items, y, bullet='✓')
    
    y += 20
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 60)], fill=FROST)
    d.text((MARGIN + 20, y + 15), '下节课预告：品析下阕——同学少年的形象、典故运用、对比阅读、主题归纳', fill=WHITE, font=F_SUB)
    
    save_slide(img, next_num(), 'summary_1')

# ═══════════════════════════════════════════════════
#  第二课时：品析《沁园春·长沙》
# ═══════════════════════════════════════════════════

def slide_p2_cover():
    """20. 第二课时封面"""
    img, d = new_slide()
    d.rectangle([(0, 0), (W, H)], fill=LIGHT_BG)
    d.rectangle([(0, 0), (W, 280)], fill=INK)
    d.rectangle([(0, 280), (W, 284)], fill=XIANG)
    d.text((MARGIN, 100), '沁园春·长沙', fill=WHITE, font=ImageFont.truetype(os.path.join(FONT_DIR, 'msyhbd.ttc'), 72))
    d.text((MARGIN + d.textlength('沁园春·长沙', ImageFont.truetype(os.path.join(FONT_DIR, 'msyhbd.ttc'), 72)) + 30, 120), '毛泽东', fill=(200,210,220), font=F_TITLE)
    d.rectangle([(MARGIN, 210), (MARGIN + 160, 248)], fill=XIANG)
    d.text((MARGIN + 20, 218), '第二课时', fill=WHITE, font=F_BODY_B)
    d.text((MARGIN, 340), '品析下阕 · 情景交融 · 拓展对比', fill=INK, font=F_SUB)
    
    save_slide(img, next_num(), 'p2_cover')

def slide_review():
    """21. 回顾上阕"""
    img, d = new_slide()
    draw_header(d, '温故知新', '回顾上阕内容', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '上阕写了什么？使用什么手法？', fill=INK, font=F_SUB)
    y += 38
    
    d.text((MARGIN, y), '上阕：描绘绚丽多彩的湘江秋景', fill=FROST, font=F_BODY_B)
    y += 30
    d.text((MARGIN, y), '手法：远近相间、动静结合、视角转换（远眺→近观→仰视→俯瞰）', fill=INK, font=F_BODY)
    y += 30
    d.text((MARGIN, y), '诗眼："看"字领起七句', fill=INK, font=F_BODY)
    y += 30
    d.text((MARGIN, y), '过渡："怅寥廓，问苍茫大地，谁主沉浮？"', fill=INK, font=F_BODY)
    
    y += 40
    d.text((MARGIN, y), '今天我们将品读下阕——毛泽东和"同学少年"的故事', fill=FROST, font=F_SUB)
    
    save_slide(img, next_num(), 'review')

def slide_xiaque_intro():
    """22. 下阕引入"""
    img, d = new_slide()
    draw_header(d, '下阕品读', '"携来百侣曾游"', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '"携来百侣曾游。忆往昔峥嵘岁月稠。"', fill=XIANG, font=F_POEM)
    y += 40
    
    d.text((MARGIN, y), '分析：这两句在全词中起什么作用？', fill=INK, font=F_SUB)
    y += 35
    
    analysis_xia = [
        '"携来"——从上片的"独立"到"携来百侣"，由一人到群体',
        '"曾游"——旧地重游，自然引起对往昔的回忆',
        '"峥嵘岁月稠"——"峥嵘"形容岁月不平凡，如山峰般巍峨',
        '承上启下：从写景过渡到忆事抒情，衔接自然',
    ]
    y = draw_bullet(d, analysis_xia, y, bullet='  ')
    
    y += 15
    draw_emph_box(d, '上片独自凝望，下片携友回忆——词的脉络由"景"转"情"', MARGIN, y, 750)
    
    save_slide(img, next_num(), 'xiaque_intro')

def slide_tongxue_image():
    """23. 同学少年形象分析"""
    img, d = new_slide()
    draw_header(d, '峥嵘岁月图', '"同学少年"的形象', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '思考："同学少年"有着怎样的形象？请从词中找出依据。', fill=INK, font=F_SUB)
    y += 45
    
    # 形象分析表
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
    """24. 下阕炼字"""
    img, d = new_slide()
    draw_header(d, '下阕炼字', '动词与修辞的力量', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '品读：下阕哪些字词和修辞体现了诗人的青春激情？', fill=INK, font=F_SUB)
    y += 40
    
    words_analysis = [
        ('"指点"', '把评述褒贬变成可想象的画面——青年们积极关注国家大事'),
        ('"激扬"', '激浊扬清——抨击社会恶行，褒扬清明，爱憎分明'),
        ('"粪土"', '名词作动词，"视……如粪土"——志向高远，蔑视权贵'),
        ('"击"（中流击水）', '写游泳之奋力——青年人勇于挑战、奋力拼搏'),
        ('"遏"（浪遏飞舟）', '夸张手法——青年掀起的革命浪潮将改变旧世界'),
    ]
    
    for word, val in words_analysis:
        d.text((MARGIN + 10, y), word, fill=FROST, font=F_BODY_B)
        tw = d.textlength(word, F_BODY_B)
        d.text((MARGIN + 10 + tw, y), val, fill=INK, font=F_BODY)
        y += 32
    
    save_slide(img, next_num(), 'lianzi_xia')

def slide_diangu():
    """25. 典故解析"""
    img, d = new_slide()
    draw_header(d, '典故解析', '文化常识', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '"万户侯"与"中流击楫"', fill=INK, font=F_SUB)
    y += 40
    
    # 万户侯
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 30)], fill=FROST)
    d.text((MARGIN + 16, y + 4), '万户侯', fill=FROST, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '汉代侯爵最高一级，享万户赋税。卫青、霍去病为代表。', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '后泛指高官贵爵。词中"粪土当年万户侯"——视权贵如粪土，表达对旧秩序的蔑视。', fill=INK, font=F_BODY)
    y += 40
    
    # 中流击楫
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 30)], fill=XIANG)
    d.text((MARGIN + 16, y + 4), '中流击楫', fill=XIANG, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '东晋祖逖北伐，渡江于中流敲打船桨发誓："若不能平定中原，则如江水一去不返！"', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"中流击水"化用此典——表达诗人献身革命事业的雄心壮志。', fill=INK, font=F_BODY)
    
    save_slide(img, next_num(), 'diangu')

def slide_zhongliu():
    """26. 中流击水图分析"""
    img, d = new_slide()
    draw_header(d, '中流击水图', '"浪遏飞舟"的深意', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '"曾记否，到中流击水，浪遏飞舟？"', fill=XIANG, font=F_POEM)
    y += 45
    
    d.text((MARGIN, y), '思考：最后三句蕴含着怎样的感情？在全词中有什么作用？', fill=INK, font=F_SUB)
    y += 38
    
    answers = [
        '内容上：回忆当年在湘江游泳，不畏风浪的青春往事',
        '修辞上："浪遏飞舟"——夸张手法，写出劈波斩浪的气魄',
        '结构上：含蓄地回答了上片"谁主沉浮"——我们！',
        '主题上：一代革命青年胸怀壮志，勇担天下大任，矢志不渝追求中华复兴',
    ]
    y = draw_bullet(d, answers, y, bullet='  ')
    
    y += 20
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 80)], fill=LIGHT_BG, outline=XIANG, width=2)
    d.text((MARGIN + 16, y + 10), '首尾呼应', fill=XIANG, font=F_BODY_B)
    d.text((MARGIN + 16, y + 40), '开篇"独立寒秋"→ 结尾"中流击水"   |   开篇"谁主沉浮"→ 结尾"浪遏飞舟"（我辈来主！）', fill=INK, font=F_BODY)
    
    save_slide(img, next_num(), 'zhongliu')

def slide_qingjing():
    """27. 情景关系分析"""
    img, d = new_slide()
    draw_header(d, '艺术特色', '情景交融', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '本词如何做到情景交融？', fill=INK, font=F_SUB)
    y += 40
    
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 26)], fill=FROST)
    d.text((MARGIN + 16, y), '上阕：景中含情', fill=FROST, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '"万山红遍"——既是枫林如火的实写，又寄寓火热的革命情怀（星火燎原）', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"万类霜天竞自由"——是诗人对自由解放的向往与追求', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"怅寥廓"的感叹——由写景直接转入抒情（触景生情）', fill=INK, font=F_BODY)
    y += 30
    
    d.rectangle([(MARGIN, y), (MARGIN + 8, y + 26)], fill=XIANG)
    d.text((MARGIN + 16, y), '下阕：情中含景', fill=XIANG, font=F_BODY_B)
    y += 28
    d.text((MARGIN + 16, y), '"峥嵘岁月稠"——将不平凡岁月化为巍峨山峰（以景喻情）', fill=INK, font=F_BODY)
    y += 24
    d.text((MARGIN + 16, y), '"到中流击水，浪遏飞舟"——是一幅奋勇进击、劈波斩浪的宏伟画面', fill=INK, font=F_BODY)
    
    save_slide(img, next_num(), 'qingjing')

def slide_contrast():
    """28. 对比阅读：古人悲秋 vs 毛泽东颂秋"""
    img, d = new_slide()
    draw_header(d, '对比阅读', '悲秋 vs 颂秋', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '讨论：毛泽东笔下的秋天，和古代诗人有何不同？为什么？', fill=INK, font=F_SUB)
    y += 45
    
    draw_table(d,
        ['维度', '古代悲秋诗人', '毛泽东'],
        [
            ['典型意象', '黄花、枯草、寒蝉、暮鸦、落叶', '万山、层林、百舸、雄鹰、游鱼'],
            ['情感基调', '悲凉、凄清、生命短暂', '豪迈、热烈、生机勃勃'],
            ['典型名句', '"万里悲秋常作客"（杜甫）', '"万类霜天竞自由"'],
            ['根本原因', '个人遭际的感慨；人生苦短', '革命家的胸襟；以天下为己任'],
            ['哲学底色', '天人合一中的消极顺应', '斗争哲学——"与天奋斗，其乐无穷"'],
        ],
        MARGIN, y, [120, 280, 320]
    )
    
    save_slide(img, next_num(), 'contrast')

def slide_theme():
    """29. 主题归纳"""
    img, d = new_slide()
    draw_header(d, '主题归纳', '', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '本词的主题是什么？', fill=INK, font=F_SUB)
    y += 45
    
    d.rectangle([(MARGIN, y), (W - MARGIN, y + 120)], fill=LIGHT_BG, outline=FROST, width=2)
    d.text((MARGIN + 20, y + 20), '主题', fill=FROST, font=F_BODY_B)
    d.text((MARGIN + 20, y + 50), '这首词通过对长沙秋景的描绘和对青年时代革命斗争生活的回忆，', fill=INK, font=F_BODY)
    d.text((MARGIN + 20, y + 74), '抒写了革命青年对国家命运的关注和蔑视反动统治者、改造旧社会、以天下为己任的豪情壮志。', fill=INK, font=F_BODY)
    
    y += 140
    d.text((MARGIN, y), '结构归纳', fill=INK, font=F_SUB)
    y += 35
    structure = [
        '上阕（看）：写景——独立寒秋图 → 湘江秋景图 → 问谁主沉浮',
        '下阕（忆）：忆事抒情——峥嵘岁月图 → 中流击水图 → 答：同学少年',
        '手法：景中含情，情中显志',
        '风格：豪放雄浑，气势磅礴',
    ]
    y = draw_bullet(d, structure, y, bullet='  ')
    
    save_slide(img, next_num(), 'theme')

def slide_blackboard():
    """30. 板书设计"""
    img, d = new_slide()
    draw_header(d, '板书设计', '', page_num=next_num())
    y = CONTENT_TOP + 10
    
    d.text((MARGIN + 300, y), '沁园春·长沙', fill=FROST, font=F_TITLE)
    d.text((MARGIN + 300 + d.textlength('沁园春·长沙', F_TITLE) + 20, y + 10), '毛泽东', fill=INK, font=F_SUB)
    y += 50
    
    d.text((MARGIN + 180, y), '看（景）', fill=FROST, font=F_SUB)
    d.text((MARGIN + 520, y), '忆（情）', fill=XIANG, font=F_SUB)
    y += 30
    
    # 意象调色盘
    d.rectangle([(MARGIN + 120, y), (MARGIN + 380, y + 22)], fill=FROST)
    d.text((MARGIN + 130, y + 2), '【意象调色盘】', fill=WHITE, font=F_SMALL)
    y += 26
    imgs = ['万山红遍 → 热血', '鹰击长空 → 力量', '鱼翔浅底 → 突破']
    for img_line in imgs:
        d.text((MARGIN + 120, y), f'  {img_line}', fill=INK, font=F_SMALL)
        y += 22
    
    y = CONTENT_TOP + 80
    # 右侧
    d.rectangle([(MARGIN + 460, y), (MARGIN + 720, y + 22)], fill=XIANG)
    d.text((MARGIN + 470, y + 2), '【青春关键词】', fill=WHITE, font=F_SMALL)
    y += 26
    keywords = ['独立 → 清醒', '问 → 担当', '中流击水 → 行动']
    for kw in keywords:
        d.text((MARGIN + 460, y), f'  {kw}', fill=INK, font=F_SMALL)
        y += 22
    
    # 箭头连接
    y = CONTENT_TOP + 180
    d.text((MARGIN + 140, y), '问：谁主沉浮？  ━━━━━━━━▶  答：同学少年！', fill=INK, font=F_BODY_B)
    y += 35
    d.text((MARGIN + 140, y), '       景中含情  ━━━━━━━━▶  情中显志', fill=GRAY, font=F_BODY)
    
    y += 40
    d.text((MARGIN + 140, y), '"主宰沉浮，舍我其谁？！"', fill=FROST, font=F_BIG)
    
    save_slide(img, next_num(), 'blackboard')

def slide_exercises():
    """31. 课堂练习"""
    img, d = new_slide()
    draw_header(d, '课堂练习', '理解性默写', page_num=next_num())
    y = CONTENT_TOP
    
    d.text((MARGIN, y), '请根据提示，写出相应的词句：', fill=INK, font=F_SUB)
    y += 45
    
    exercises = [
        ('1. 面对大千世界，词人发出慨叹，表现雄心壮志：', ',    ？'),
        ('2. 起过渡作用，旧地重游引发对往昔的回忆：', ','),
        ('3. 同学少年评论国家大事，写出激浊扬清的文章：', '，，'),
        ('4. 夸张手法写出劈波斩浪气魄的两句：', '，'),
        ('5. 用动物表现生机勃勃秋景的两句：', '，'),
    ]
    
    for q, hint in exercises:
        d.text((MARGIN + 10, y), q, fill=INK, font=F_BODY)
        d.text((MARGIN + 10 + d.textlength(q, F_BODY), y), '____________', fill=GRAY, font=F_BODY)
        tw = d.textlength(q + '____________', F_BODY)
        d.text((MARGIN + 10 + tw, y), hint, fill=GRAY, font=F_SMALL)
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
    """32. 布置作业"""
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
    d.text((MARGIN + 16, y), '2. 以"我眼中的秋天"为题，写一篇300字短文，注意意象的选取和字词的锤炼', fill=INK, font=F_BODY)
    
    save_slide(img, next_num(), 'homework')

def slide_ending():
    """33. 结语"""
    img, d = new_slide()
    d.rectangle([(0, 0), (W, H)], fill=INK)
    
    # 大字结语
    d.text((MARGIN, 200), '青春永不落幕', fill=WHITE, font=ImageFont.truetype(os.path.join(FONT_DIR, 'msyhbd.ttc'), 56))
    
    y = 300
    quote = '"世界是你们的，也是我们的，但是归根结底是你们的。"'
    d.text((MARGIN, y), quote, fill=(200, 210, 220), font=F_BODY)
    y += 35
    d.text((MARGIN, y), '——毛泽东（1957年莫斯科大学讲话）', fill=GRAY, font=F_SMALL)
    
    save_slide(img, next_num(), 'ending')

# ═══════════════════════════════════════════════════
#  主流程
# ═══════════════════════════════════════════════════

def main():
    print('Rendering classroom PPT v2 (real teacher style)...')
    
    slides = [
        # 第一课时
        slide_cover,
        slide_objectives,
        slide_leadin_autumn,
        slide_author,
        slide_background,
        slide_wenti,
        slide_cipai,
        slide_zhengyin,
        slide_dujiepai,
        slide_full_poem,
        slide_four_pictures,
        slide_duli,
        slide_qiujing_kan,
        slide_imagery_table,
        slide_color_action,
        slide_lianzi_1,
        slide_lianzi_2,
        slide_transition,
        slide_summary_1,
        # 第二课时
        slide_p2_cover,
        slide_review,
        slide_xiaque_intro,
        slide_tongxue_image,
        slide_lianzi_xia,
        slide_diangu,
        slide_zhongliu,
        slide_qingjing,
        slide_contrast,
        slide_theme,
        slide_blackboard,
        slide_exercises,
        slide_homework,
        slide_ending,
    ]
    
    for fn in slides:
        fn()
        print(f'  ✓ {fn.__name__}')
    
    # 合成PDF
    from glob import glob
    pngs = sorted(glob(os.path.join(OUT, 'slide_*.png')))
    images = [Image.open(p).convert('RGB') for p in pngs]
    
    pdf_path = os.path.join(OUT, '沁园春长沙-课堂版PPT-v2.pdf')
    images[0].save(pdf_path, 'PDF', resolution=150, save_all=True, append_images=images[1:])
    
    desktop = os.path.expanduser('~/Desktop')
    import shutil
    shutil.copy(pdf_path, os.path.join(desktop, '沁园春长沙-课堂版PPT-v2.pdf'))
    
    size_kb = os.path.getsize(pdf_path) // 1024
    print(f'\nDone! {len(slides)} slides → {pdf_path} ({size_kb}KB)')
    print(f'Copied to desktop: 沁园春长沙-课堂版PPT-v2.pdf')

if __name__ == '__main__':
    main()
