# -*- coding: utf-8 -*-
# 《芣苢》×《文氏外孙入村收麦》古诗群文 — 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条核实）：
#   芣苢：诗经·周南第八篇，方玉润《诗经原始》"群歌互答"；毛传/朱熹=车前草(Plantago major)，闻一多=薏苡(Coix)。
#   苏辙(1039-1112)，北宋，晚年退居颍川，《文氏外孙入村收麦》写外孙帮忙收麦的乡村生活。
#   教学招式：动作演示法（演示6动词）+ 朗读体验法（四言二二节拍）+ 对比分析法（三章变与不变）
# 真实照片（自由授权）：
#   plantago.jpg   车前草/芣苢真身（Wikimedia Commons, CC BY 4.0）——诗中被采摘的真实植物
#   harvest.jpg    麦收金田（Wikimedia Commons, CC BY-SA 4.0）——苏辙收麦场景
#   ricefield.jpg  中国稻田（Wikimedia Commons, Public domain）——古代劳动背景
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PH = lambda n: os.path.join(HERE, '_photos_u2_4', n)
PHOTO = {
    'plantago': PH('plantago.jpg'),
    'harvest':  PH('harvest.jpg'),
    'ricefield': PH('ricefield.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['plantago'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.48)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第二单元 · 劳动光荣', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.15), Inches(12.3), Inches(2.4),
            [{'text': '芣苢 · 文氏外孙入村收麦', 'size': 48, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.55), Inches(12), Inches(0.65),
            [{'text': '《诗经·周南》× 北宋·苏辙 —— 古诗中的劳动节拍与诗意', 'size': 17, 'color': SOFT, 'font': KAI}])
    textbox(s, M, Inches(5.45), Inches(12), Inches(1.1),
            [{'text': '从通讯到评论再到古诗——劳动的主题穿越两千年。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P2 目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '准确朗读两首诗，解释六动词含义，说出重章叠句的表达效果。', FROST),
        ('文化意识', '感受古人对劳动的朴素赞美，理解"劳动光荣"是中华文化的悠久传统。', XIANG),
        ('思维品质', '追踪六动词变化，发现"劳动进程→情感递进"的内在逻辑。', GOLD),
        ('学习能力', '掌握"辨字义→理结构→品节奏→悟情感"古诗劳动阅读四步法。', MUTED),
    ]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.6))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + cw/2 - Inches(0.45), y + Inches(0.35), Inches(0.9), Inches(0.9))
        dot.fill.solid(); dot.fill.fore_color.rgb = col; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, x + cw/2 - Inches(0.45), y + Inches(0.55), Inches(0.9), Inches(0.5),
                [{'text': str(i+1), 'size': 24, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.5), cw - Inches(0.4), Inches(0.6),
                [{'text': t, 'size': 18, 'color': col, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.22), y + Inches(2.15), cw - Inches(0.44), Inches(1.3),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ---------- P3 背景：知人论世 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '知人论世 · 两首诗两个时代', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    # 左：芣苢
    lx = M
    place_photo(s, PHOTO['plantago'], lx, M + Inches(1.25), col_w, Inches(2.3))
    caption(s, '车前草（Plantago major）· 即"芣苢"（毛传/朱熹说）', lx, M + Inches(3.65), col_w)
    textbox(s, lx, M + Inches(4.05), col_w, Inches(2.45),
            [{'text': '《诗经·周南·芣苢》（先秦）', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '· 周代采集歌谣，三章十二句，仅换六动词', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 植物身份：毛传=车前草；闻一多=薏苡', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 方玉润："田家妇女三三五五，群歌互答"', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}])
    # 右：苏辙
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['harvest'], rx, M + Inches(1.25), col_w, Inches(2.3))
    caption(s, '麦收金田 · 苏辙"收麦"场景（环境照）', rx, M + Inches(3.65), col_w)
    textbox(s, rx, M + Inches(4.05), col_w, Inches(2.45),
            [{'text': '《文氏外孙入村收麦》苏辙（北宋）', 'size': 18, 'color': XIANG, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '· 苏辙(1039–1112)，晚年退居颍川（今河南许昌一带）', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 写外孙入村帮忙收麦：劳动辛劳 + 天伦温情交织', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 与《芣苢》同写劳动：群体欢欣 vs 个体温情', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P4 重点：六动词递进 + 重章叠句 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 六动词递进', M, M, FROST)
    # 六动词递进图
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.4), CW, Inches(2.8))
    box.fill.solid(); box.fill.fore_color.rgb = WHITE; box.line.color.rgb = FROST; box.line.width = Pt(2); box.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.6), CW - Inches(0.6), Inches(0.55),
            [{'text': '六动词递进：从开始摘到满载而归', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI}])
    verbs = [
        ('采', '开始摘取', FROST),
        ('有', '摘到了（动手取得）', FROST),
        ('掇 duō', '一片片拾起掉落', XIANG),
        ('捋 luō', '顺着茎滑下成把', XIANG),
        ('袺 jié', '提衣襟兜着', GOLD),
        ('襭 xié', '扎紧衣襟装满带走', GOLD),
    ]
    cw_v = (CW - Inches(0.6)) / 3
    vx = [M + Inches(0.3)]
    for i in range(1, 3): vx.append(vx[-1] + cw_v + Inches(0.15))
    vy = M + Inches(2.3)
    for i, (v, d, col) in enumerate(verbs):
        cx = vx[i % 3]
        cy = vy if i < 3 else vy + Inches(1.1)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, cw_v, Inches(0.95))
        card.fill.solid(); card.fill.fore_color.rgb = SOFT if i < 3 else SOFT; card.line.color.rgb = col; card.line.width = Pt(1.4); card.shadow.inherit = False
        textbox(s, cx + Inches(0.1), cy + Inches(0.08), Inches(1.4), Inches(0.42),
                [{'text': v, 'size': 20, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, cx + Inches(1.5), cy + Inches(0.12), cw_v - Inches(1.6), Inches(0.38),
                [{'text': d, 'size': 11.5, 'color': INK, 'font': KAI, 'line': 1.3}])
    # 箭头提示
    textbox(s, M, Inches(5.0), CW, Inches(0.4),
            [{'text': '▶ 劳动进程完整呈现：开始 → 得到 → 细致 → 高效 → 兜装 → 满载', 'size': 14, 'color': MUTED, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    # 重章叠句说明
    box2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(5.45), CW, Inches(1.75))
    box2.fill.solid(); box2.fill.fore_color.rgb = INK; box2.shadow.inherit = False
    textbox(s, M + Inches(0.3), Inches(5.6), CW - Inches(0.6), Inches(1.5),
            [{'text': '重章叠句的艺术智慧', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '不变 = 结构重复（劳动的节拍感、往复回环的音乐性）', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '变 = 动词推进（每次重复都有新动作，劳动在向前走）', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P5 难点：三个易卡住的地方 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三个易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('六动词细微区别', '"掇"(拾掉落的) vs "捋"(从茎上抹下)方向不同。→ 动作演示法：现场做一遍，人人能看懂。', FROST),
        ('重章叠句≠偷懒重复', '学生觉得"三章一样"。→ 对比分析标红变动字：不变=节拍，变=推进。不是技术缺陷，是艺术智慧。', XIANG),
        ('劳动=辛苦？不！还有欢欣', '思维定式：劳动就是累。→ 方玉润意境还原："平原旷野、风和日丽中群歌互答"——古人写的是劳动之美。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.33), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.8),
                [{'text': t, 'size': 16.5, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.3}])
        textbox(s, x + Inches(0.3), y + Inches(1.15), cw - Inches(0.6), Inches(2.9),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- P6 探究：招牌招式（方玉润意境 + 动作演示） ----------
def s_explore(s):
    bg(s, PAPER)
    kicker(s, '探究 · 从真实问题出发', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': '招牌招式：方玉润"意境还原" + 动作演示法', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    lx = M
    cw = (CW - Inches(0.5)) / 2
    # 左：方玉润意境还原
    box1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.55), cw, Inches(4.7))
    box1.fill.solid(); box1.fill.fore_color.rgb = WHITE; box1.line.color.rgb = FROST; box1.line.width = Pt(1.8); box1.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.75), cw - Inches(0.6), Inches(0.5),
            [{'text': '① 方玉润《诗经原始》意境还原', 'size': 17, 'color': FROST, 'bold': True, 'font': KAI}])
    quote_box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx + Inches(0.2), M + Inches(2.4), cw - Inches(0.4), Inches(2.0))
    quote_box.fill.solid(); quote_box.fill.fore_color.rgb = SOFT; quote_box.line.color.rgb = MUTED; quote_box.line.width = Pt(1); quote_box.shadow.inherit = False
    textbox(s, lx + Inches(0.35), M + Inches(2.55), cw - Inches(0.7), Inches(1.8),
            [{'text': '"读者试平心静气涵咏此诗,\n恍听田家妇女,三三五五,\n于平原旷野、风和日丽中,\n群歌互答,\n余音袅袅,若远若近……"\n\n—— 清·方玉润《诗经原始》', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    textbox(s, lx + Inches(0.3), M + Inches(4.55), cw - Inches(0.6), Inches(1.6),
            [{'text': '· 用这段话让学生闭眼想象画面——不是"读一首诗"，而是"走进一个场景"', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '· 再联系现代：南方妇女登山采茶结伴讴歌，犹有此风', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45}])
    # 右：稻田照 + 动作演示法
    rx = M + cw + Inches(0.5)
    place_photo(s, PHOTO['ricefield'], rx, M + Inches(1.55), cw, Inches(2.2))
    caption(s, '中国稻田 · 古代劳动背景（PD）', rx, M + Inches(3.85), cw)
    box2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.25), cw, Inches(2.0))
    box2.fill.solid(); box2.fill.fore_color.rgb = INK; box2.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.4), cw - Inches(0.6), Inches(1.8),
            [{'text': '② 动作演示法', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 5},
             {'text': '现场演示：掇（蹲拾）、捋（顺抹）、袺（提兜）、襭（扎腰塞入）', 'size': 13, 'color': WHITE, 'font': KAI, 'line': 1.4, 'space_after': 5},
             {'text': '跟做一遍 → 六动词不再是抽象字词，而是身体记忆', 'size': 13, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P7 板书：六动词 + 重章叠句 + 古今对比 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 古诗中的劳动', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.0), Inches(0.4),
            [{'text': '维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(3.6), M + Inches(1.28), Inches(8.8), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('六动词递进', '采→有→掇→捋→袺→襭 （开始→得→细→效→兜→满载）', FROST),
        ('重章叠句', '不变=结构（节拍）｜变=动词（推进）＝劳动韵律', XIANG),
        ('《芣苢》基调', '群体劳动的欢欣与热情——"劳动的节拍"', GOLD),
        ('苏辙诗基调', '个体劳动的辛劳与天伦温情交织——"劳动+人情"', GOLD),
        ('古今对比', '古诗：节拍·欢欣｜通讯：过程·精神｜共通：劳动光荣', FROST),
        ('古诗四步法', '辨字义 → 理结构 → 品节奏 → 悟情感', MUTED),
    ]
    y = M + Inches(1.85)
    for i, (dim, a, col) in enumerate(rows):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.58))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.1), Inches(3.0), Inches(0.4),
                [{'text': dim, 'size': 14, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(3.6), y + Inches(0.1), Inches(8.8), Inches(0.4),
                [{'text': a, 'size': 13.5, 'color': INK, 'font': KAI}])
        y += Inches(0.64)
    page_num(s)

# ---------- P8 作业：分层 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '① 背诵《芣苢》全诗；② 准确默写六个动词（采·有·掇·捋·袺·襭）；③ 各用一句话描述每个动词的动作。', FROST),
        ('提升 · 选做', '写150字赏析《从六个动词看〈芣苢〉的劳动节拍》：按序解释六动词，分析递进逻辑，点明重章叠句效果。', XIANG),
        ('拓展 · 实践', '比较古今写劳动：《芣苢》vs 袁隆平通讯 vs 张秉贵通讯——形式不同但精神相通，各举一例。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (tag, body, col) in enumerate(tiers):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(3.2),
                [{'text': body, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)

# ---------- P9 总结：古诗四步法 + 单元衔接 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '总结 · 读古诗的四步', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '辨字义 → 理结构 → 品节奏 → 悟情感', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    pillars = [
        ('辨字义', '六动词各有其动作——掇≠捋，袺≠襭，动作演示帮记忆。', FROST),
        ('理结构', '重章叠句：不变是节拍，变是推进——《诗经》的艺术智慧。', XIANG),
        ('品节奏', '四言"二二"停顿：采采/芣苢，薄言/采之——像劳动号子。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(pillars):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.25), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 21, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.95), cw - Inches(0.6), Inches(1.2),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(5.0), CW, Inches(2.1))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, M + Inches(0.3), Inches(5.25), Inches(0.06), GOLD, 30)
    textbox(s, M + Inches(0.55), Inches(5.15), CW - Inches(0.8), Inches(1.9),
            [{'text': '劳动光荣，穿越千年', 'size': 19, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 8},
             {'text': '《芣苢》：两千年前妇女的采摘欢歌。\n苏辙：千年前文人笔下的收麦温情。\n袁隆平/张秉贵/钟扬：今天的劳动精神。\n形式不同，精神相通——劳动光荣是中华民族的文化基因。', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_difficulties,
           s_explore, s_blackboard, s_homework, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-4.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
