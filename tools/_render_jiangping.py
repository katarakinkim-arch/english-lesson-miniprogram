# -*- coding: utf-8 -*-
# 《写作实践与讲评——新诗修改与提升》课堂学生版 PPT 渲染器（手写精排，import 共享库）
# 来源：lessons-cn.js u1-7 教案 + 高赞讲评/升格课共识招牌招式
#   · 核心：好诗三标准（意象鲜明·情感真挚·语言有张力）、三种典型习作讲评、修改三方向
#   · 研究补充：升格妙法（语序调整/炼字/成分省略/反常搭配·陌生化）、单元诗集编辑
#   · 注意：通篇不出现「教师/老师」字样（课堂学生版）
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 复用第6课已下载的真实照片（钢笔/星空/海浪/城市夜景）
PHOTO = {
    'pen':       os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_pen.jpg'),
    'star':      os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_star.jpg'),
    'ocean':     os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_ocean.jpg'),
    'citynight': os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_citynight.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['pen'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.52)
    rule(s, M, M + Inches(0.45), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.65), Inches(10), Inches(0.5),
            [{'text': '必修上 第一单元 · 写作讲评', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.3), Inches(12), Inches(1.6),
            [{'text': '新诗修改与提升', 'size': 46, 'color': WHITE, 'bold': True, 'font': KAI},
             {'text': '在别人的诗里，看见自己的诗', 'size': 22, 'color': SOFT, 'bold': True, 'font': KAI, 'space_before': 8}])
    textbox(s, M, Inches(5.2), Inches(12), Inches(1.2),
            [{'text': '删，有时比加更重要。', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4}])
    page_num(s)


# ---------- P2 导览 ----------
def s_contents(s):
    bg(s, PAPER)
    kicker(s, '本课导览', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(10), Inches(0.8),
            [{'text': '修改的十四步', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    items = [
        ('01', '好诗三标准：意象·情感·语言'),
        ('02', '典型 A：意象清，语言平'),
        ('03', '典型 B：情烈，意象模糊'),
        ('04', '典型 C：意象情感俱佳'),
        ('05', '修改三方向：换意象·调节奏·炼字'),
        ('06', '升格妙法：陌生化表达'),
        ('07', '修改示范：边改边说思路'),
        ('08', '同桌互签：写一句具体评语'),
        ('09', '诊断自检：读者读懂了吗'),
        ('10', '单元诗集：青春的吟唱'),
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


# ---------- P3 好诗三标准 ----------
def s_three_standards(s):
    bg(s, PAPER)
    kicker(s, '好诗三标准 · 内化', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '改诗之前，先记这三个标准', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    stds = [
        ('意象鲜明', '不是一个意象写很多，而是一个意象写透。', FROST),
        ('情感真挚', '热烈或迷茫都要真——为生活、为时代而歌。', XIANG),
        ('语言有张力', '不是华丽辞藻，是简单字词的组合产生力量。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(stds):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.8))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.7),
                [{'text': t, 'size': 21, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.2), cw - Inches(0.5), Inches(2.4),
                [{'text': b, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P4 典型 A ----------
def s_typicalA(s):
    bg(s, PAPER)
    kicker(s, '典型 A · 意象清，语言平', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '有牺牲感，但像记叙文', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    # 原稿
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), Inches(5.7), Inches(4.2))
    c1.fill.solid(); c1.fill.fore_color.rgb = SOFT; c1.line.color.rgb = MUTED; c1.line.width = Pt(1.3); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '原稿', 'size': 17, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '橡皮', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '在笔袋里', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '很安静', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '它擦掉了错字', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '自己变短了', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7}])
    # 诊断+改
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(6.1), M + Inches(1.7), Inches(5.7), Inches(4.2))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = FROST; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + Inches(6.4), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '诊断 → 改语言', 'size': 17, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(6.4), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '意象✓ 有牺牲感；语言△ 太平。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '「很安静」→「沉默」（人格化，更有力）', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '「错字」→「痕迹」（更宽泛、有余味）', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '改语言不是加形容词，是换更有张力的词。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P5 典型 B ----------
def s_typicalB(s):
    bg(s, PAPER)
    kicker(s, '典型 B · 情烈，意象模糊', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '情感强烈，却看不见画面', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), Inches(5.7), Inches(4.2))
    c1.fill.solid(); c1.fill.fore_color.rgb = SOFT; c1.line.color.rgb = MUTED; c1.line.width = Pt(1.3); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '原稿', 'size': 17, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '我要飞', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '飞过高山', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '飞过大海', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '飞向未来', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '青春的力量，不可阻挡', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(6.1), M + Inches(1.7), Inches(5.7), Inches(4.2))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + Inches(6.4), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '诊断 → 换意象', 'size': 17, 'color': XIANG, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(6.4), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '情感✓ 强烈；意象✗ 「飞」太抽象。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '「飞过高山大海」空泛——', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 6},
             {'text': '找一个具体的「物」承载情感。', 'size': 15, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '例：把「飞向未来」改成「把一只纸飞机／掷出教学楼的天台」。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P6 典型 C ----------
def s_typicalC(s):
    bg(s, PAPER)
    kicker(s, '典型 C · 意象情感俱佳', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '为什么这首「好」？', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), Inches(5.7), Inches(4.2))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = GOLD; c1.line.width = Pt(1.8); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '佳作', 'size': 17, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '台灯', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '在午夜', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '亮成一粒种子', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '我趴在桌上', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '是另一粒', 'size': 17, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(6.1), M + Inches(1.7), Inches(5.7), Inches(4.2))
    c2.fill.solid(); c2.fill.fore_color.rgb = SOFT; c2.line.color.rgb = GOLD; c2.line.width = Pt(1.6); c2.shadow.inherit = False
    textbox(s, M + Inches(6.4), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '赏析 · 好在哪里', 'size': 17, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(6.4), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '意象✓ 台灯=种子，我也=种子；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '情感✓ 都在「生长」，希望感；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '语言✓ 分行长短错落，有节奏。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '赏析要分析「为什么好」，有词句支撑。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P7 修改三方向 ----------
def s_revise_dirs(s):
    bg(s, PAPER)
    kicker(s, '修改三方向', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '朝这三个方向去改', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    dirs = [
        ('换意象', '意象不准或模糊，换一个更贴切、更新的物。', FROST),
        ('调节奏', '分行长短交错，在想让读者停顿处断行。', XIANG),
        ('炼　字', '用动词、用反常搭配，删去废话。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(dirs):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.6))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 22, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.2), cw - Inches(0.5), Inches(2.2),
                [{'text': b, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P8 升格妙法：陌生化 ----------
def s_shengge(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['ocean'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.56)
    kicker(s, '升格妙法 · 陌生化', M, M, GOLD)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '让语言「不像平时那样说」', 'size': 26, 'color': WHITE, 'bold': True, 'font': KAI}])
    methods = [
        ('语序调整', '故意倒装，制造停顿与重音。', FROST),
        ('炼　字', '一个动词顶一排形容词。', XIANG),
        ('成分省略', '留白，让读者自己补。', GOLD),
        ('反常搭配', '「咸味的歌」——打通感官。', MUTED),
    ]
    cw = (CW - Inches(0.3) * 3) / 4
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(methods):
        x = M + i * (cw + Inches(0.3))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.4))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.2), y + Inches(0.25), cw - Inches(0.4), Inches(0.6),
                [{'text': t, 'size': 17, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.05), cw - Inches(0.4), Inches(2.2),
                [{'text': b, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P9 修改示范 ----------
def s_demo(s):
    bg(s, PAPER)
    kicker(s, '修改示范 · 边改边说', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '同一首诗，可以有不同的改法', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.4)) / 2
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), cw, Inches(4.2))
    c1.fill.solid(); c1.fill.fore_color.rgb = SOFT; c1.line.color.rgb = MUTED; c1.line.width = Pt(1.3); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), cw - Inches(0.6), Inches(0.5),
            [{'text': '原稿', 'size': 17, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), cw - Inches(0.6), Inches(3.0),
            [{'text': '橡皮／在笔袋里／很安静／', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.7},
             {'text': '它擦掉了错字／自己变短了。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.7}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(1.7), cw, Inches(4.2))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = FROST; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(1.95), cw - Inches(0.6), Inches(0.5),
            [{'text': '改稿', 'size': 17, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(2.7), cw - Inches(0.6), Inches(3.0),
            [{'text': '橡皮／在笔袋角落／沉默／', 'size': 15, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '它擦去了痕迹／自己／', 'size': 15, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7},
             {'text': '一点一点／变短。', 'size': 15, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.7}])
    page_num(s)


# ---------- P10 同桌互签 ----------
def s_peer_sign(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['pen'], W - M - Inches(4.4), M, Inches(4.4), Inches(4.4))
    caption(s, '笔与稿纸 · 终稿', W - M - Inches(4.4), M + Inches(4.5), Inches(4.4))
    kicker(s, '同桌互签 · 具体评价', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.8), Inches(0.6),
            [{'text': '改完，请同桌写一句评语', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(6.9), Inches(4.8),
            [{'text': '互签不是互夸——要写具体：', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '「意象选得好，但第三行节奏断裂。」', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '「情感真挚，建议把『很』字都删掉。」', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '也给自己写自评：我改了什么、为什么改。', 'size': 16, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P11 诊断自检 ----------
def s_self_check(s):
    bg(s, PAPER)
    kicker(s, '诊断自检 · 读者视角', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '一个最简单的检测法', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.6), CW,
                '把诗读给一个没听过你想法的人——他读完，知道你想表达什么吗？', '修改的底线', FROST)
    textbox(s, M, M + Inches(3.8), CW, Inches(2.6),
            [{'text': '若对方一头雾水：多半是「意象模糊」或「情感没落地」——回去换意象、补具体。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '若对方被触动：说明意象与情感已打通，再打磨语言节奏即可。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '「删比加更重要」——敢大改，才改得出好诗。', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P12 单元诗集 ----------
def s_collection(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['citynight'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    kicker(s, '单元学习任务 · 诗集', M, M, GOLD)
    textbox(s, M, M + Inches(0.8), Inches(11), Inches(0.7),
            [{'text': '把全班诗作，编成一本集子', 'size': 30, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(2.0), Inches(11.5), Inches(4.0),
            [{'text': '主题：「青春的吟唱」。', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '你的终稿，就是其中的一页——为青春留一份诗意的纪念。', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '汇编、排版、写序与跋，让这一单元的学习有看得见的成果。', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P13 青春的价值 ----------
def s_youth(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['star'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.56)
    kicker(s, '青春的价值 · 为时代而歌', M, M, GOLD)
    textbox(s, M, M + Inches(0.8), Inches(11), Inches(0.7),
            [{'text': '写诗，也是思考青春', 'size': 30, 'color': WHITE, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.9), CW,
                '本单元读名家的青春之歌，现在写下你自己的——以意象，以真诚，以时代。',
                '第一单元 · 青春的价值', GOLD)
    textbox(s, M, M + Inches(4.6), CW, Inches(2.0),
            [{'text': '从《沁园春》的豪迈到《红烛》的赤诚，从《峨日朵》的坚守到《致云雀》的飞翔——', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '青春从不是单一模样。重要的是：心怀理想，勇于表达，为生活与时代写诗。', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P14 作业（分层） ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '提交新诗终稿（修改誊抄版），附同桌互签评语；写 50 字自评：意象、改了什么、为什么。', FROST),
        ('提升 · 选做', '从单元课文中选一首，仿其风格再写一首新诗，要求风格与课上明显不同。', XIANG),
        ('拓展 · 实践', '为班级诗集「青春的吟唱」投稿；尝试为你的诗配一句创作札记。', GOLD),
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
for fn in [s_cover, s_contents, s_three_standards, s_typicalA, s_typicalB, s_typicalC,
           s_revise_dirs, s_shengge, s_demo, s_peer_sign, s_self_check, s_collection,
           s_youth, s_homework]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(BASE, 'preview_v7', 'jiangping.pptx')
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
