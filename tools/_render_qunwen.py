# -*- coding: utf-8 -*-
# 《立在地球边上放号 / 红烛》群文 课堂学生版 PPT 渲染器（手写精排，import 共享库）
# 融合来源：温儒敏解读 + 多份高赞优质课/实录共识招牌招式
#   · 放号：地球边「巨人/大我」想象、宏大自然意象群、「力」排比与自由体、洪涛=五四象征
#   · 红烛：化用李商隐「蜡炬成灰」赋新意、烧/光/泪三层意象、「莫问收获但问耕耘」
#   · 群文：外放vs内敛 双维比较、意象≠比喻 概念辨析
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
    'candle':  os.path.join(BASE, 'preview_v7', '_qunwen_photos', 'real_candle.jpg'),
    'waves':   os.path.join(BASE, 'preview_v7', '_qunwen_photos', 'real_waves.jpg'),
    'pacific': os.path.join(BASE, 'preview_v7', '_qunwen_photos', 'real_pacific.jpg'),
    'iceberg': os.path.join(BASE, 'preview_v7', '_qunwen_photos', 'real_iceberg.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['waves'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.52)
    rule(s, M, M + Inches(0.45), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.65), Inches(10), Inches(0.5),
            [{'text': '必修上 第一单元 · 群文阅读', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.3), Inches(12), Inches(1.8),
            [{'text': '立在地球边上放号', 'size': 46, 'color': WHITE, 'bold': True, 'font': KAI},
             {'text': '红　烛', 'size': 46, 'color': WHITE, 'bold': True, 'font': KAI, 'space_before': 6}])
    textbox(s, M, Inches(4.5), Inches(12), Inches(0.7),
            [{'text': '郭沫若　·　闻一多　现代诗的意象与情感', 'size': 19, 'color': SOFT, 'font': HEI}])
    textbox(s, M, Inches(5.5), Inches(12), Inches(1.0),
            [{'text': '青春的两种声音：呐喊的爆发，与诉说的低语。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)


# ---------- P2 导览 ----------
def s_contents(s):
    bg(s, PAPER)
    kicker(s, '本课导览', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(10), Inches(0.8),
            [{'text': '九步读懂两首诗', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    items = [
        ('01', '导入：一支红烛，你想到什么？'),
        ('02', '知人论世：五四的洪流'),
        ('03', '《放号》意象：地球边的巨人'),
        ('04', '《放号》「力」的排比与自由体'),
        ('05', '《红烛》意象：烧 · 光 · 泪'),
        ('06', '《红烛》「莫问收获，但问耕耘」'),
        ('07', '群文比较：外放 vs 内敛'),
        ('08', '概念辨析：意象 ≠ 比喻'),
        ('09', '朗读、学法与青春价值'),
    ]
    paras = []
    for num, t in items:
        paras.append({'size': 16, 'color': INK, 'font': KAI, 'line': 1.3, 'space_after': 7,
                      'runs': [{'text': num + '  ', 'size': 16, 'color': FROST, 'bold': True, 'font': HEI},
                               {'text': t, 'size': 16, 'color': INK, 'font': KAI}]})
    textbox(s, M, M + Inches(1.75), CW, Inches(5.0), paras)
    page_num(s)


# ---------- P3 导入：红烛联想 ----------
def s_intro(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['candle'], W - M - Inches(4.6), M, Inches(4.6), Inches(4.6))
    caption(s, '红烛 · 赤诚与热烈', W - M - Inches(4.6), M + Inches(4.7), Inches(4.6))
    kicker(s, '导入 · 一支红烛', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.8), Inches(0.6),
            [{'text': '看到红烛，你想到什么？', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(6.8), Inches(4.6),
            [{'text': '奉献、光明、燃烧自己照亮别人——这是多数人的第一反应。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '注意「红」字：它不只是颜色，更带情感色彩——赤诚、热烈。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '闻一多化用李商隐「蜡炬成灰泪始干」，给这个古老意象注入新意：为理想而献身的痴情与执着。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P4 知人论世：五四的洪流 ----------
def s_background(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['waves'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '知人论世 · 1919 的洪流', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, M + Inches(1.3), Inches(11.5), Inches(0.8),
            [{'text': '五四，是一场青春的狂飙', 'size': 30, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(2.4), Inches(11.5), Inches(4.0),
            [{'text': '1919 年，五四运动席卷中国，旧道德、旧礼教受到猛烈冲击，自由与个性解放成为时代强音。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '郭沫若从日本回国，途经横滨海岸，面对浩渺大海，惊天激浪与时代洪流一起撞击胸怀。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '诗中滚滚洪涛，正是五四运动巨大声势的象征——向旧世界猛烈冲击的时代精神。', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P5 《放号》意象解码：巨人·大我 ----------
def s_fanghao_imagery(s):
    bg(s, PAPER)
    kicker(s, '《放号》意象解码 · 宏大的自然', M, M, FROST)
    place_photo(s, PHOTO['pacific'], M, M + Inches(1.4), Inches(4.4), Inches(2.4))
    caption(s, '太平洋 · 推倒地球', M, M + Inches(3.9), Inches(4.4))
    place_photo(s, PHOTO['iceberg'], M + Inches(4.7), M + Inches(1.4), Inches(4.4), Inches(2.4))
    caption(s, '北冰洋 · 壮丽晴景', M + Inches(4.7), M + Inches(3.9), Inches(4.4))
    textbox(s, M + Inches(9.2), M + Inches(1.4), Inches(2.7), Inches(4.4),
            [{'text': '意　象　群', 'size': 16, 'color': FROST, 'bold': True, 'font': HEI, 'space_after': 6},
             {'text': '白云 · 怒涌', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 5},
             {'text': '北冰洋 · 晴景', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 5},
             {'text': '太平洋 · 推倒地球', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 5},
             {'text': '洪涛 · 滚滚而来', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 12},
             {'text': '特　点', 'size': 16, 'color': XIANG, 'bold': True, 'font': HEI, 'space_after': 6},
             {'text': '宏大、阔远、雄奇，气势磅礴。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 12},
             {'text': '主体形象＝横跨两大洋的巨人——「大我」，五四个性解放后的自我意识。', 'size': 14, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P6 《放号》「力」的排比与自由体 ----------
def s_fanghao_li(s):
    bg(s, PAPER)
    kicker(s, '《放号》· 力的颂歌', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '「力」的排比：不是乱写，是青春的呐喊', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.6), CW, '力的绘画，力的舞蹈，力的音乐，力的诗歌，力的律吕哟！', '《放号》结句', FROST)
    cards = [
        ('动词的力量', '怒涌·提起·推倒·毁坏·创造·努力——毁坏与创造并存，正是变革的力。', FROST),
        ('自由体新诗', '长短句穿插、多用排比、几乎无节制——五四破壳而出的新形式。', XIANG),
        ('时代的摇滚', '一连七个「力」，不是乱写，是先驱者对旧世界的呐喊。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(4.5)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.0))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.2), cw - Inches(0.5), Inches(0.5),
                [{'text': t, 'size': 17, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.25), y + Inches(0.75), cw - Inches(0.5), Inches(1.1),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P7 《红烛》意象解码：烧·光·泪 ----------
def s_hongzhu_imagery(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['candle'], W - M - Inches(4.4), M, Inches(4.4), Inches(4.4))
    caption(s, '红烛 · 烧蜡成灰', W - M - Inches(4.4), M + Inches(4.5), Inches(4.4))
    kicker(s, '《红烛》意象解码', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.8), Inches(0.6),
            [{'text': '一支烛的三个动作', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    rows = [
        ('烧', '烧蜡成灰', '主动的牺牲——为创造光明而彻底燃烧自我', FROST),
        ('放', '放出光明', '传播光明，照破世人的梦、救出他们的灵魂', XIANG),
        ('流', '流下泪来', '赤诚与焦灼：为烧得不快而急，非伤心的泪', GOLD),
    ]
    y = M + Inches(1.7)
    for ch, act, mean, col in rows:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, Inches(6.8), Inches(1.35))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.5); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, M + Inches(0.2), y + Inches(0.32), Inches(0.7), Inches(0.7))
        dot.fill.solid(); dot.fill.fore_color.rgb = col; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, M + Inches(0.2), y + Inches(0.38), Inches(0.7), Inches(0.5),
                [{'text': ch, 'size': 22, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, M + Inches(1.1), y + Inches(0.18), Inches(5.5), Inches(0.5),
                [{'text': act, 'size': 17, 'color': INK, 'bold': True, 'font': KAI}])
        textbox(s, M + Inches(1.1), y + Inches(0.65), Inches(5.5), Inches(0.6),
                [{'text': mean, 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.4}])
        y += Inches(1.5)
    page_num(s)


# ---------- P8 《红烛》「莫问收获，但问耕耘」 ----------
def s_hongzhu_moyi(s):
    bg(s, PAPER)
    kicker(s, '《红烛》· 人生哲学', M, M, FROST)
    quote_block(s, M, M + Inches(1.2), CW, '莫问收获，但问耕耘。', '《红烛》结句', FROST)
    textbox(s, M, M + Inches(3.4), CW, Inches(3.2),
            [{'text': '红烛所有的付出，不求自身回报；只愿以一腔热血肥沃中华的土地。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '这是彻底奉献的人生哲学——在不合理的现实里，仍尽最大的力、发最强的光。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '红烛，就是诗人光辉人格的写照：悲而不伤，直面惨淡人生而坚毅前行（杜甫式的现实主义）。', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P9 群文比较：外放 vs 内敛 ----------
def s_compare(s):
    bg(s, PAPER)
    kicker(s, '群文比较 · 青春的两种表达', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '同写青春激情，气象各不同', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    # 表头
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.6), CW, Inches(0.6))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.25), M + Inches(1.68), Inches(3.0), Inches(0.45),
            [{'text': '比较维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(3.6), M + Inches(1.68), Inches(4.0), Inches(0.45),
            [{'text': '《放号》郭沫若', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(8.0), M + Inches(1.68), Inches(4.0), Inches(0.45),
            [{'text': '《红烛》闻一多', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('意象风格', '宏大（海洋·风暴）', '精微（一支烛）'),
        ('抒情方式', '外放（呐喊·爆发）', '内敛（诉说·低语）'),
        ('情感基调', '激越', '悲壮'),
        ('节奏形式', '排比短促', '反复低回'),
        ('精神气质', '浪漫（李白）', '现实（杜甫）'),
    ]
    y = M + Inches(2.35)
    for dim, a, b in rows:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.78))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if (int(y) // 10) % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.25), y + Inches(0.16), Inches(3.0), Inches(0.5),
                [{'text': dim, 'size': 15, 'color': INK, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(3.6), y + Inches(0.16), Inches(4.0), Inches(0.5),
                [{'text': a, 'size': 14, 'color': FROST, 'font': KAI}])
        textbox(s, M + Inches(8.0), y + Inches(0.16), Inches(4.0), Inches(0.5),
                [{'text': b, 'size': 14, 'color': XIANG, 'font': KAI}])
        y += Inches(0.86)
    page_num(s)


# ---------- P10 概念辨析：意象 ≠ 比喻 ----------
def s_concept(s):
    bg(s, PAPER)
    kicker(s, '概念辨析 · 读懂现代诗的关键', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '意象，不是比喻', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    # 左：比喻
    lc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), Inches(5.7), Inches(4.3))
    lc.fill.solid(); lc.fill.fore_color.rgb = WHITE; lc.line.color.rgb = MUTED; lc.line.width = Pt(1.2); lc.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '比喻：A 像 B', 'size': 18, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '「红烛像奉献的人」', 'size': 18, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '只是打比方，物仍是物，人仍人。', 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    # 右：意象
    rc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(6.1), M + Inches(1.7), Inches(5.7), Inches(4.3))
    rc.fill.solid(); rc.fill.fore_color.rgb = WHITE; rc.line.color.rgb = FROST; rc.line.width = Pt(1.6); rc.shadow.inherit = False
    textbox(s, M + Inches(6.4), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '意象：情志 + 物象 → 融合', 'size': 18, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(6.4), M + Inches(2.7), Inches(5.1), Inches(3.0),
            [{'text': '「红烛就是诗人自己」', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '物成了情感的载体，物我交融——这是意象。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '迁移：小说《百合花》「被子上的百合花」也是意象。', 'size': 14, 'color': XIANG, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P11 朗读：两种声音 ----------
def s_recite(s):
    bg(s, PAPER)
    kicker(s, '朗读 · 两种声音', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '一首呐喊，一首低语', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.4)) / 2
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.6), cw, Inches(4.5))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = FROST; c1.line.width = Pt(1.8); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.85), cw - Inches(0.6), Inches(0.6),
            [{'text': '《放号》：呐喊 · 爆发', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), cw - Inches(0.6), Inches(3.2),
            [{'text': '语速渐快，到排比处再加快；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '「怒涌」「推倒」「洪涛」等中心词做重音；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '「力的绘画，力的舞蹈……」一气呵成，不可断开。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(1.6), cw, Inches(4.5))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(1.85), cw - Inches(0.6), Inches(0.6),
            [{'text': '《红烛》：诉说 · 低语', 'size': 20, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(2.7), cw - Inches(0.6), Inches(3.2),
            [{'text': '深沉倾诉，与红烛「对话」的语气；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '感叹词「啊」「罢」回环，读出缠绵与赤诚；', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '末句「莫问收获，但问耕耘」放声赞颂，豪情收束。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P12 学法小结：意象→象征→情感 ----------
def s_method(s):
    bg(s, PAPER)
    kicker(s, '学法小结 · 现代诗研读路径', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三步读懂一首现代诗', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('找意象', '圈出诗中的物象：白云、洪涛、红烛……', FROST),
        ('明象征', '物象承载了什么情志：力、牺牲、光明……', XIANG),
        ('悟情感', '由象征抵达诗人心境与时代精神。', GOLD),
    ]
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(steps):
        step_card(s, M, y, CW, Inches(1.35), i + 1, t, [b], col)
        y += Inches(1.5)
    page_num(s)


# ---------- P13 作业（分层） ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '有感情朗读两首诗并录音（≥1分钟）；从每首找出 3 个意象，写出其象征义。', FROST),
        ('提升 · 选做', '写一首 8 行内现代诗，以「青春的____」为题，用≥2 个意象承载情感（非简单比喻）。', XIANG),
        ('拓展 · 实践', '对比李白与杜甫的青春书写，说说《放号》《红烛》分别像谁，为什么。', GOLD),
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


# ---------- P14 青春的价值（单元呼应） ----------
def s_youth(s):
    bg(s, PAPER)
    kicker(s, '青春的价值 · 单元呼应', M, M, FROST)
    textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
            [{'text': '两种声音，同一种青春', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.6), CW,
                '《放号》以浪漫张扬青春的力，《红烛》以现实承载青春的痛——外放与内敛，都是五四青年对家国的担当。',
                '第一单元 · 青春的价值', FROST)
    textbox(s, M, M + Inches(4.3), CW, Inches(2.0),
            [{'text': '本单元还读《沁园春·长沙》的豪迈、《百合花》《哦，香雪》的纯真——', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '青春从不是单一模样：它可以呐喊，可以低语，可以壮阔，也可以温柔。', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '重要的是——心怀家国，勇于担当。', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- BUILD ----------
for fn in [s_cover, s_contents, s_intro, s_background, s_fanghao_imagery, s_fanghao_li,
           s_hongzhu_imagery, s_hongzhu_moyi, s_compare, s_concept, s_recite, s_method,
           s_homework, s_youth]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(BASE, 'preview_v7', 'qunwen.pptx')
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
# === PART2 END ===
