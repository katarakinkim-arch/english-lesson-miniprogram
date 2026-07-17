# -*- coding: utf-8 -*-
# 《写作指导——学写新诗：从意象到情感》课堂学生版 PPT 渲染器（手写精排，import 共享库）
# 来源：lessons-cn.js u1-6 教案 + 高赞写作课共识招牌招式
#   · 核心：写作四步法（选意象→定情感→写初稿→改语言）
#   · 招牌：约束练习「禁止说青春」逼出意象、仿写二选一（排比体/咏物体）、互评量表、炼字
#   · 研究补充：诗歌四要素（意象·情感·节奏·语言）、用动词替形容词/通感/分行控节奏
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO = {
    'pen':        os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_pen.jpg'),
    'star':       os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_star.jpg'),
    'ocean':      os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_ocean.jpg'),
    'citynight':  os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_citynight.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['pen'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.52)
    rule(s, M, M + Inches(0.45), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.65), Inches(10), Inches(0.5),
            [{'text': '必修上 第一单元 · 写作指导', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.3), Inches(12), Inches(1.6),
            [{'text': '学写新诗', 'size': 48, 'color': WHITE, 'bold': True, 'font': KAI},
             {'text': '从意象到情感', 'size': 30, 'color': SOFT, 'bold': True, 'font': KAI, 'space_before': 6}])
    textbox(s, M, Inches(4.7), Inches(12), Inches(0.7),
            [{'text': '不追求格律，重在以意象承载青春', 'size': 19, 'color': WHITE, 'font': HEI}])
    textbox(s, M, Inches(5.6), Inches(12), Inches(1.2),
            [{'text': '少年是天生的诗人——', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '把所思所感，写成属于你的青春的诗。', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)


# ---------- P2 导览 ----------
def s_contents(s):
    bg(s, PAPER)
    kicker(s, '本课导览', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(10), Inches(0.8),
            [{'text': '写诗的十二步', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    items = [
        ('01', '为什么写诗：青春是专属诗歌的时光'),
        ('02', '写作四步法：选意象→定情感→写初稿→改语言'),
        ('03', '关键一式：禁止说「青春」'),
        ('04', '选意象，不是比喻'),
        ('05', '仿写二选一：排比体 / 咏物体'),
        ('06', '学生佳作示例'),
        ('07', '互评量表：意象·情感·语言·节奏'),
        ('08', '炼字：改一个字，感觉不同'),
        ('09', '写作小锦囊：动词·通感·分行'),
        ('10', '诗歌四要素小结'),
        ('11', '青春的价值 · 为时代而歌'),
        ('12', '分层作业'),
    ]
    paras = []
    for num, t in items:
        paras.append({'size': 15, 'color': INK, 'font': KAI, 'line': 1.25, 'space_after': 5,
                      'runs': [{'text': num + '  ', 'size': 15, 'color': FROST, 'bold': True, 'font': HEI},
                               {'text': t, 'size': 15, 'color': INK, 'font': KAI}]})
    textbox(s, M, M + Inches(1.7), CW, Inches(5.0), paras)
    page_num(s)


# ---------- P3 为什么写诗 ----------
def s_why(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['star'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '为什么写诗', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, M + Inches(1.3), Inches(11.5), Inches(0.8),
            [{'text': '青春，是专属诗歌的时光', 'size': 30, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(2.5), Inches(11.5), Inches(4.0),
            [{'text': '诗言志，诗缘情——诗是强烈情感的自然流露。', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '少年是天生的诗人：你路遇的不平、亲人的关爱、自然的春华秋实，都能化作诗。', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '本单元读了《沁园春》《放号》《红烛》——现在，把读到的「意象思维」变成你自己的笔。', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P4 写作四步法 ----------
def s_method(s):
    bg(s, PAPER)
    kicker(s, '写作四步法 · 核心', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '四步，写出一首小诗', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('①', '选意象', '找一个能承载你情感的物——不是漂亮的东西，是「能寄托」的物。', FROST),
        ('②', '定情感', '你想表达什么：热烈、迷茫、坚定，还是不舍？先想清。', XIANG),
        ('③', '写初稿', '8 行以内，先写出来，别急着改——让情感流出来。', GOLD),
        ('④', '改语言', '调分行、控节奏、炼字——让语言有诗感。', MUTED),
    ]
    cw = (CW - Inches(0.3) * 3) / 4
    y = M + Inches(1.9)
    for i, (num, t, b, col) in enumerate(steps):
        x = M + i * (cw + Inches(0.3))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.0))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.3), Inches(0.7), Inches(0.7))
        dot.fill.solid(); dot.fill.fore_color.rgb = col; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.42), Inches(0.7), Inches(0.5),
                [{'text': num, 'size': 22, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.1), y + Inches(0.35), cw - Inches(1.3), Inches(0.6),
                [{'text': t, 'size': 19, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.25), y + Inches(1.4), cw - Inches(0.5), Inches(2.4),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)


# ---------- P5 关键一式：禁止说「青春」 ----------
def s_constraint(s):
    bg(s, PAPER)
    kicker(s, '关键一式 · 逼出意象', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '不许说「青春」，却要让人感到青春', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), CW, Inches(1.0),
            [{'text': '直抒胸臆（「青春真好」）太浅。给自己一个约束——用具体的物去说，意象就出来了。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6}])
    chips = [
        ('像刚开的窗，风灌进来。', '——新鲜、涌动'),
        ('跑道上的起跑线。', '——蓄势、出发'),
        ('还没干透的水彩画。', '——未定、可能'),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(3.0)
    for i, (poem, note) in enumerate(chips):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.0))
        card.fill.solid(); card.fill.fore_color.rgb = SOFT; card.line.color.rgb = FROST; card.line.width = Pt(1.4); card.shadow.inherit = False
        textbox(s, x + Inches(0.3), y + Inches(0.3), cw - Inches(0.6), Inches(1.0),
                [{'text': poem, 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.5}])
        textbox(s, x + Inches(0.3), y + Inches(1.35), cw - Inches(0.6), Inches(0.5),
                [{'text': note, 'size': 13, 'color': FROST, 'font': KAI}])
    page_num(s)


# ---------- P6 选意象，不是比喻 ----------
def s_imagery_not_metaphor(s):
    bg(s, PAPER)
    kicker(s, '概念辨析 · 意象 ≠ 比喻', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '「寄托」，不是「打比方」', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    lc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), Inches(5.7), Inches(4.3))
    lc.fill.solid(); lc.fill.fore_color.rgb = WHITE; lc.line.color.rgb = MUTED; lc.line.width = Pt(1.2); lc.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '比喻：A 像 B', 'size': 18, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '「黑板擦像奉献的人」', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '只是打比方——物仍是物，人仍人。', 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    rc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(6.1), M + Inches(1.7), Inches(5.7), Inches(4.3))
    rc.fill.solid(); rc.fill.fore_color.rgb = WHITE; rc.line.color.rgb = FROST; rc.line.width = Pt(1.6); rc.shadow.inherit = False
    textbox(s, M + Inches(6.4), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '意象：物我交融', 'size': 18, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(6.4), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '黑板擦在讲台上，', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.5},
             {'text': '没有人看它；', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.5},
             {'text': '它擦掉了字，自己变白了。', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '物自己「说话」——这就是意象。', 'size': 15, 'color': FROST, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P7 仿写二选一 ----------
def s_imitation(s):
    bg(s, PAPER)
    kicker(s, '动手写 · 仿写二选一', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '站在名家的肩上起步', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.4)) / 2
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), cw, Inches(4.2))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = FROST; c1.line.width = Pt(1.8); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), cw - Inches(0.6), Inches(0.6),
            [{'text': 'A · 排比体（仿《放号》）', 'size': 19, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M + Inches(0.3), M + Inches(2.8), cw - Inches(0.6), Inches(3.0),
            [{'text': '用「力的____」句式写 4 行；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '换掉意象与情感，别只改字；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '例：力的画笔，力的鼓点，力的星火……', 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(1.7), cw, Inches(4.2))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(1.95), cw - Inches(0.6), Inches(0.6),
            [{'text': 'B · 咏物体（仿《红烛》）', 'size': 19, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(2.8), cw - Inches(0.6), Inches(3.0),
            [{'text': '选一个物，写它的动作与变化；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '让物承载一种精神或情感；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '例：写「闹钟」——叫醒梦，也叫醒不想醒来的我。', 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P8 学生佳作示例 ----------
def s_examples(s):
    bg(s, PAPER)
    kicker(s, '学生佳作 · 借镜', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '同龄人的诗，什么样？', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    poems = [
        ('闹钟', '在凌晨五点／叫醒了梦／也叫醒了／不想醒来的我。', FROST),
        ('流云', '流云，流云，你是天际的少年；／少年，少年，你是地上的流云。', XIANG),
        ('春茧体育馆', '钢架编织成网的经纬，／坐满三万颗跳动的心脏；／篮球撞击地板的声响，／是青春在混凝土里发芽的回响。', GOLD),
    ]
    y = M + Inches(1.7)
    for title, body, col in poems:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(1.5))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.4); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.18), Inches(2.2), Inches(1.1),
                [{'text': '《' + title + '》', 'size': 18, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, M + Inches(2.6), y + Inches(0.22), CW - Inches(2.9), Inches(1.1),
                [{'text': body, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
        y += Inches(1.65)
    page_num(s)


# ---------- P9 互评量表 ----------
def s_peer_review(s):
    bg(s, PAPER)
    kicker(s, '互评量表 · 四维', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '读别人的诗，评这四个维度', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    dims = [
        ('意象', '有没有具体的物？是否新颖？', FROST),
        ('情感', '物是否承载了情感？真挚吗？', XIANG),
        ('语言', '有没有诗感？是否精炼？', GOLD),
        ('节奏', '分行是否控制了停顿与快慢？', MUTED),
    ]
    cw = (CW - Inches(0.3) * 3) / 4
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(dims):
        x = M + i * (cw + Inches(0.3))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.6))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 22, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.2), cw - Inches(0.5), Inches(2.2),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    textbox(s, M, y + Inches(3.8), CW, Inches(0.5),
            [{'text': '评价要说具体：好在哪里、不好在哪里，别只说「写得不错」。', 'size': 14, 'color': MUTED, 'font': KAI, 'italic': True}])
    page_num(s)


# ---------- P10 炼字 ----------
def s_revise(s):
    bg(s, PAPER)
    kicker(s, '炼字 · 改一个字，感觉不同', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '原稿 vs 改稿', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.4)) / 2
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), cw, Inches(4.2))
    c1.fill.solid(); c1.fill.fore_color.rgb = SOFT; c1.line.color.rgb = MUTED; c1.line.width = Pt(1.3); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), cw - Inches(0.6), Inches(0.5),
            [{'text': '原稿', 'size': 17, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), cw - Inches(0.6), Inches(3.0),
            [{'text': '海浪拍打在礁石上，', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.7, 'space_after': 8},
             {'text': '很好听。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.7}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(1.7), cw, Inches(4.2))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = FROST; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(1.95), cw - Inches(0.6), Inches(0.5),
            [{'text': '改稿', 'size': 17, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(2.7), cw - Inches(0.6), Inches(3.0),
            [{'text': '海浪咀嚼着礁石，', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7, 'space_after': 8},
             {'text': '把咸味的歌，吐还给月亮。', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7}])
    page_num(s)


# ---------- P11 写作小锦囊 ----------
def s_tips(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['ocean'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.56)
    kicker(s, '写作小锦囊', M, M, GOLD)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三个让诗「立」起来的办法', 'size': 26, 'color': WHITE, 'bold': True, 'font': KAI}])
    tips = [
        ('用动词替形容词', '「咀嚼」替代「拍打」——物活了，画面动了。', FROST),
        ('用通感破感官', '「咸味的歌」——味觉与听觉打通，新奇空灵。', XIANG),
        ('分行控制节奏', '长短句交错，在你想让读者停顿处断行。', GOLD),
    ]
    y = M + Inches(1.9)
    for t, b, col in tips:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(1.35))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.18), Inches(3.8), Inches(1.0),
                [{'text': t, 'size': 18, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, M + Inches(4.3), y + Inches(0.2), CW - Inches(4.6), Inches(1.0),
                [{'text': b, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.5}])
        y += Inches(1.5)
    page_num(s)


# ---------- P12 诗歌四要素 ----------
def s_four_elements(s):
    bg(s, PAPER)
    kicker(s, '小结 · 好诗的四个要素', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '一首好诗，长这样', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    elems = [
        ('新颖意象', '从生活里挑「能承载情感」的物，越具体越好。', FROST),
        ('真挚情感', '热烈或迷茫，都要真——为时代、为生活而歌。', XIANG),
        ('自然节奏', '长短句交错，分行制造停顿，读来上口。', GOLD),
        ('精炼语言', '一字千钧，用动词、用通感，删去废话。', MUTED),
    ]
    cw = (CW - Inches(0.3) * 3) / 4
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(elems):
        x = M + i * (cw + Inches(0.3))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.8))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.7),
                [{'text': t, 'size': 19, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.2), cw - Inches(0.5), Inches(2.4),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)


# ---------- P13 青春的价值 · 为时代而歌 ----------
def s_youth(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['citynight'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    kicker(s, '青春的价值 · 为时代而歌', M, M, GOLD)
    textbox(s, M, M + Inches(0.8), Inches(11), Inches(0.7),
            [{'text': '把青春，写成诗', 'size': 30, 'color': WHITE, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.9), CW,
                '文章合为时而著，歌诗合为事而作。——白居易',
                '写诗，也要把握时代脉搏', GOLD)
    textbox(s, M, M + Inches(4.6), CW, Inches(2.0),
            [{'text': '本单元读《沁园春》的豪迈、《放号》《红雀》的浪漫、《红烛》的赤诚、《百合花》《哦，香雪》的纯真——', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '现在轮到你：用意象说出你的青春，为生活、为时代，写一首小小的诗。', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P14 作业（分层） ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '依互评意见修改新诗终稿（8 行内），誊抄；诗下用一句话写明意象与情感。', FROST),
        ('提升 · 选做', '再写一首不同风格的新诗（首首排比体则写咏物体），对比两首意象选择的差异。', XIANG),
        ('拓展 · 实践', '以「我的____青春」为题写诗，融入一个真实的生活意象，为单元诗集投稿。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (tag, body, col) in enumerate(tiers):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.55))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.1), cw, Inches(0.4),
                [{'text': tag, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(0.75), cw - Inches(0.5), Inches(1.8),
                [{'text': body, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- BUILD ----------
for fn in [s_cover, s_contents, s_why, s_method, s_constraint, s_imagery_not_metaphor,
           s_imitation, s_examples, s_peer_review, s_revise, s_tips, s_four_elements,
           s_youth, s_homework]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(BASE, 'preview_v7', 'xiezuo.pptx')
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
