# -*- coding: utf-8 -*-
# 《以工匠精神雕琢时代品质》新闻评论精读 — 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条核实）：
#   出处：李斌，《人民日报》2016年4月30日第4版"人民论坛"；"工匠精神"首次写入2016年政府工作报告（十二届全国人大四次会议，李克强）。
#   结构：引论(1段引出话题)→本论(2-4段：概念/作用/内涵)→结论(5段倡导践行)，总分总。
#   分论点：敬业(态度)→精益求精(标准)→创新(动力)，并列中有递进（名师论文指出第4段内涵由浅入深9层）。
#   论证方法：引用(《说文》"匠，木工也")、举例(瑞士手表/德国制造)、对比(有精神vs急功近利)、假设排比("没有一流的心性，就没有一流的技术")。
#   教学招式（从7331字课堂实录 jiaoxueshilu.com/865 提炼）：
#     · 思维导图对比法——两版学生思维导图比较异同，发现"开头1段→正文2-4段→结尾5段"总分总；
#     · "三问法"解剖文本（观点？证据？推理？）对应"找论点→析论据→理逻辑"（郑洁/黄碧俊教学设计）。
# 真实照片（自由授权）：
#   craft.jpg   制琴师精修提琴（Wikimedia Commons, CC BY 2.5）——工匠精神·精益求精的视觉象征
#   renmin.jpg  人民日报社（Wikimedia Commons, CC BY-SA 3.0）——新闻评论文体背景
#   watch.jpg   机械表机芯（Wikimedia Commons, CC BY-SA 2.0）——文中"瑞士手表"举例论证的真实参照
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PH = lambda n: os.path.join(HERE, '_photos_u2_3', n)
PHOTO = {
    'craft':  PH('craft.jpg'),
    'renmin': PH('renmin.jpg'),
    'watch':  PH('watch.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['craft'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.52)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第二单元 · 劳动光荣', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.15), Inches(12.3), Inches(2.4),
            [{'text': '以工匠精神', 'size': 50, 'color': WHITE, 'bold': True, 'font': KAI},
             {'text': '雕琢时代品质', 'size': 50, 'color': WHITE, 'bold': True, 'font': KAI, 'space_before': 6}])
    textbox(s, M, Inches(4.7), Inches(12), Inches(0.7),
            [{'text': '李斌 · 人民日报2016 · 一篇说理的新闻评论', 'size': 18, 'color': SOFT, 'font': HEI}])
    textbox(s, M, Inches(5.55), Inches(12), Inches(1.2),
            [{'text': '从「写人」（通讯）转向「说理」（评论）——读懂论点、论据与论证的力量。', 'size': 16.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P2 目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '准确找出中心论点与分论点，说出≥3种论证方法及其作用。', FROST),
        ('文化意识', '理解工匠精神（敬业·精益求精·创新）的时代价值，反思"速成"心态。', XIANG),
        ('思维品质', '梳理"论点→论据→论证"逻辑链，培养逻辑分析与批判思维。', GOLD),
        ('学习能力', '掌握"找论点→析论据→理逻辑"评论三步法，能迁移其他评论。', MUTED),
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

# ---------- P3 背景：写作背景 + 新闻评论文体 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '知人论世 · 因事立论', M, M, FROST)
    col_w = Inches(5.75)
    # 左：人民日报 + 写作背景
    lx = M
    place_photo(s, PHOTO['renmin'], lx, M + Inches(1.3), col_w, Inches(2.4))
    caption(s, '人民日报社（新闻评论发表地）· 自由授权', lx, M + Inches(3.85), col_w)
    textbox(s, lx, M + Inches(4.3), col_w, Inches(2.2),
            [{'text': '写作背景', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '· 2016年政府工作报告首提"培育精益求精的工匠精神"', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 李斌据此因事立论，2016.4.30刊于《人民日报》"人民论坛"', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 新闻性：回应社会热词，释"什么是工匠精神、为何倡导"', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 倾向性：提倡工匠精神，批评浮躁风气与短视心态', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}])
    # 右：新闻评论三要素
    rx = M + col_w + Inches(0.5)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.3), col_w, Inches(5.2))
    box.fill.solid(); box.fill.fore_color.rgb = WHITE; box.line.color.rgb = XIANG; box.line.width = Pt(2); box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.55), col_w - Inches(0.6), Inches(0.6),
            [{'text': '新闻评论 · 三要素', 'size': 20, 'color': XIANG, 'bold': True, 'font': KAI}])
    rows = [
        ('论点', '作者的观点、主张——文章要"立"什么。', FROST),
        ('论据', '支撑观点的材料：引权威、举实例、作对比。', XIANG),
        ('论证', '用推理把论据与论点连起来的"桥"（归纳/演绎/对比）。', GOLD),
    ]
    y = M + Inches(2.35)
    for i, (t, b, col) in enumerate(rows):
        textbox(s, rx + Inches(0.3), y, Inches(1.4), Inches(0.9),
                [{'text': t, 'size': 22, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, rx + Inches(1.8), y + Inches(0.05), col_w - Inches(2.1), Inches(0.9),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
        y += Inches(1.0)
    rule(s, rx + Inches(0.3), y + Inches(0.0), col_w - Inches(0.6), MUTED, 1)
    textbox(s, rx + Inches(0.3), y + Inches(0.15), col_w - Inches(0.6), Inches(0.9),
            [{'text': '特点：政策性 · 针对性 · 时效性；篇幅有限，靠独到见解取胜。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P4 重点：中心论点 + 分论点树（递进） ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 论点与结构', M, M, FROST)
    cw = (CW - Inches(0.5)) / 2
    # 左：结构与中心论点
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.4), cw, Inches(4.5))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = FROST; c1.line.width = Pt(2); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.65), cw - Inches(0.6), Inches(0.6),
            [{'text': '中心论点', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M + Inches(0.3), M + Inches(2.35), cw - Inches(0.6), Inches(1.0),
            [{'text': '时代需要工匠精神\n来雕琢时代品质', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.4}])
    textbox(s, M + Inches(0.3), M + Inches(3.55), cw - Inches(0.6), Inches(2.2),
            [{'text': '结构（总分总）', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '· 引论（第1段）：时代重精细品质，引出工匠精神', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 5},
             {'text': '· 本论（2-4段）：概念→作用→内涵，层层深入', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 5},
             {'text': '· 结论（第5段）：倡导人人成为践行者', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}])
    # 右：分论点递进
    rx = M + cw + Inches(0.5)
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.4), cw, Inches(4.5))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(2); c2.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.65), cw - Inches(0.6), Inches(0.6),
            [{'text': '分论点 · 递进', 'size': 20, 'color': XIANG, 'bold': True, 'font': KAI}])
    chain = [
        ('① 敬业', '态度：爱岗敬业、劳动光荣的价值原色', FROST),
        ('② 精益求精', '标准：将产品当艺术、质量当生命', XIANG),
        ('③ 创新', '动力：改变现实的力量，而非雕虫小技', GOLD),
    ]
    y = M + Inches(2.4)
    for i, (t, b, col) in enumerate(chain):
        bar = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx + Inches(0.3), y, cw - Inches(0.6), Inches(0.95))
        bar.fill.solid(); bar.fill.fore_color.rgb = SOFT if i else SOFT; bar.line.color.rgb = col; bar.line.width = Pt(1.4); bar.shadow.inherit = False
        textbox(s, rx + Inches(0.5), y + Inches(0.1), cw - Inches(1.0), Inches(0.45),
                [{'text': t, 'size': 18, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, rx + Inches(0.5), y + Inches(0.5), cw - Inches(1.0), Inches(0.45),
                [{'text': b, 'size': 13, 'color': INK, 'font': KAI}])
        if i < 2:
            textbox(s, rx + cw/2 - Inches(0.3), y + Inches(0.95), Inches(0.6), Inches(0.3),
                    [{'text': '▼', 'size': 13, 'color': MUTED, 'align': PP_ALIGN.CENTER}])
        y += Inches(1.25)
    page_num(s)

# ---------- P5 难点：三个易错点 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三个易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('论点与论据分不清', '学生常把"举例"当论点。→ 明确：论点是观点，论据是支撑观点的材料；中心论点不在第1段第1句。', FROST),
        ('"创新"维度被忽略', '以为工匠精神只是"重复做好"。→ 引导发现文中"将产品做到极致也是一种创造"。', XIANG),
        ('评论语言"说理之美"', '习惯通讯的生动描写，难体会评论的简洁有力。→ 对比"写得生动"与"说得在理"。', GOLD),
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

# ---------- P6 探究：思维导图对比法 + 三问法（真实教学招式） ----------
def s_explore(s):
    bg(s, PAPER)
    kicker(s, '探究 · 从真问题出发', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': '招牌招式：思维导图对比 + 三问法', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    # 左：思维导图对比法
    lx = M
    cw = (CW - Inches(0.5)) / 2
    box1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.55), cw, Inches(4.7))
    box1.fill.solid(); box1.fill.fore_color.rgb = WHITE; box1.line.color.rgb = FROST; box1.line.width = Pt(1.8); box1.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.75), cw - Inches(0.6), Inches(0.5),
            [{'text': '① 思维导图对比法', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.35), cw - Inches(0.6), Inches(3.7),
            [{'text': '让学生画两版本文思路图并比较异同——', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '· 两版都指向：开头(1段)→正文(2-4段)→结尾(5段)', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '· 差异在"正文"：有人写概念，有人写作用与内涵', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '· 由此自然归纳出"总分总"结构，B班也能跟上', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '（招式取自7331字课堂实录：两图并置、异同互见）', 'size': 12.5, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    # 右：三问法 + 瑞士机芯图
    rx = M + cw + Inches(0.5)
    place_photo(s, PHOTO['watch'], rx, M + Inches(1.55), cw, Inches(2.1))
    caption(s, '瑞士机芯 · 文中"瑞士手表"举例论证的真实参照', rx, M + Inches(3.75), cw)
    box2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.0), cw, Inches(2.25))
    box2.fill.solid(); box2.fill.fore_color.rgb = INK; box2.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.15), cw - Inches(0.6), Inches(2.0),
            [{'text': '② "三问法"解剖文本', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 5},
             {'text': '观点是什么？→ 找论点', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.4},
             {'text': '证据怎么摆？→ 析论据', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.4},
             {'text': '推理严密吗？→ 理逻辑', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P7 板书：论点树 + 论据分类 + 逻辑链 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 论证结构表', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.1), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.2), Inches(3.0), Inches(0.4),
            [{'text': '维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(3.6), M + Inches(1.2), Inches(8.8), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('中心论点', '时代需要工匠精神来雕琢时代品质（第5段收束点明）', FROST),
        ('分论点①', '敬业——态度：爱岗敬业、劳动光荣的价值原色', FROST),
        ('分论点②', '精益求精——标准：将产品当艺术、质量当生命', XIANG),
        ('分论点③', '创新——动力：改变现实的力量，而非雕虫小技', GOLD),
        ('论据·引用', '《说文》"匠，木工也"——以权威字书释"工"，增强说服力', XIANG),
        ('论据·举例', '瑞士手表、德国制造——精益求精的典范，论证具体真实', GOLD),
        ('论据·对比', '有工匠精神的企业 vs 急功近利的企业——正反对举', FROST),
        ('逻辑链', '论点 → 论据 → 论证（推理） → 结论', MUTED),
    ]
    y = M + Inches(1.8)
    for i, (dim, a, col) in enumerate(rows):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.55))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.09), Inches(3.0), Inches(0.38),
                [{'text': dim, 'size': 14, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(3.6), y + Inches(0.09), Inches(8.8), Inches(0.38),
                [{'text': a, 'size': 13.5, 'color': INK, 'font': KAI}])
        y += Inches(0.6)
    page_num(s)

# ---------- P8 作业：分层 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '① 画出本文论点树（中心论点+3分论点+各分论点论据）；② 解释引用/举例/对比三种论证方法，各举文中一例。', FROST),
        ('提升 · 选做', '写200字小评论《工匠精神与速成文化之我见》：有明确论点，至少用2种论证方法，联系生活实际。', XIANG),
        ('拓展 · 实践', '比较"通讯三步法"与"评论三步法"的异同——前者读故事，后者读道理。', GOLD),
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

# ---------- P9 总结：评论三步法 + 单元衔接 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '总结 · 读评论的三步', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '找论点 → 析论据 → 理逻辑', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    pillars = [
        ('找论点', '通读后判断中心与分论点，不在首句死等。', FROST),
        ('析论据', '按引用/举例/对比分类，看它支撑哪条分论点。', XIANG),
        ('理逻辑', '画出"论点→论据→论证→结论"链条，辨关系。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(pillars):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.4))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.25), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 22, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(1.0), cw - Inches(0.6), Inches(1.2),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(5.15), CW, Inches(1.95))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, M + Inches(0.3), Inches(5.4), Inches(0.06), GOLD, 30)
    textbox(s, M + Inches(0.55), Inches(5.35), CW - Inches(0.8), Inches(1.7),
            [{'text': '工匠精神 ＝ 敬业 ＋ 精益求精 ＋ 创新', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 8},
             {'text': '下节课从「说理」（评论）回到「审美」（古诗）——《芣苢》《文氏外孙入村收麦》，主题仍是"劳动"。', 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_difficulties,
           s_explore, s_blackboard, s_homework, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-3.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
