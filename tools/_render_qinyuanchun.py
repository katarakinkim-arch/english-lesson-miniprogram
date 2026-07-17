# -*- coding: utf-8 -*-
# 《沁园春·长沙》课堂学生版 PPT 渲染器（手写精排，import 共享库）
# 融合来源：多份高赞优质课/课堂实录共识招牌招式
#   · 悲秋vs赞秋 反差切入（杜甫/马致远 vs 毛泽东）
#   · 意象解码 + 炼字换字法（击/翔 vs 飞/游）
#   · 视角变换（远眺近观仰视俯瞰）+ 红碧色彩
#   · 诗眼「谁主沉浮」上阕问→下阕忆答 呼应
#   · 同学少年群像五维 / 对比《沁园春·雪》《秋词》《登高》/ 知人论世1925
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
    'statue': os.path.join(BASE, 'preview_v7', '_qinyuanchun_photos', 'real_statue.jpg'),
    'xiang':  os.path.join(BASE, 'preview_v7', '_qinyuanchun_photos', 'real_xiang.jpg'),
    'yuelu':  os.path.join(BASE, 'preview_v7', '_qinyuanchun_photos', 'real_yuelu.jpg'),
    'isle':   os.path.join(BASE, 'preview_v7', '_qinyuanchun_photos', 'real_isle.jpg'),
    'maple':  os.path.join(BASE, 'preview_v7', '_qinyuanchun_photos', 'real_maple.jpg'),
    'sail':   os.path.join(BASE, 'preview_v7', '_qinyuanchun_photos', 'real_sail.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['statue'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.5)
    rule(s, M, M + Inches(0.45), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.65), Inches(9), Inches(0.5),
            [{'text': '必修上 第一单元 · 现代诗歌', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.5), Inches(11), Inches(1.7),
            [{'text': '沁园春 · 长沙', 'size': 62, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.25), Inches(11), Inches(0.7),
            [{'text': '毛泽东　写于 1925 年秋', 'size': 20, 'color': SOFT, 'font': HEI}])
    textbox(s, M, Inches(5.35), Inches(11.5), Inches(1.3),
            [{'text': '独立寒秋，湘江北去，橘子洲头。', 'size': 19, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)


# ---------- P2 导览 ----------
def s_contents(s):
    bg(s, PAPER)
    kicker(s, '本课导览', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(10), Inches(0.8),
            [{'text': '九步读懂一首词', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    items = [
        ('01', '导入：古人悲秋，毛泽东为何赞秋？'),
        ('02', '知人论世：1925 年的橘子洲头'),
        ('03', '诵读：上下阕全词与领字脉络'),
        ('04', '上阕意象解码：四幅湘江秋景'),
        ('05', '炼字：把「击」「翔」换成别的字？'),
        ('06', '视角与色彩：远·近·仰·俯 + 红碧'),
        ('07', '诗眼：「问苍茫大地，谁主沉浮」'),
        ('08', '下阕：同学少年群像'),
        ('09', '问答呼应 · 对比思辨 · 写法小结'),
    ]
    paras = []
    for num, t in items:
        paras.append({'size': 16, 'color': INK, 'font': KAI, 'line': 1.3, 'space_after': 7,
                      'runs': [{'text': num + '  ', 'size': 16, 'color': FROST, 'bold': True, 'font': HEI},
                               {'text': t, 'size': 16, 'color': INK, 'font': KAI}]})
    textbox(s, M, M + Inches(1.75), CW, Inches(5.0), paras)
    page_num(s)


# ---------- P3 导入：悲秋 vs 赞秋 ----------
def s_intro(s):
    bg(s, PAPER)
    kicker(s, '导入 · 同写秋天，为何不同', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '古人悲秋，毛泽东却写出「壮秋」', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    # 左：古人悲秋
    lc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), Inches(5.7), Inches(4.6))
    lc.fill.solid(); lc.fill.fore_color.rgb = WHITE; lc.line.color.rgb = MUTED; lc.line.width = Pt(1.2); lc.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '古人的秋天 · 萧瑟悲凉', 'size': 17, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.6), Inches(5.1), Inches(3.5),
            [{'text': '万里悲秋常作客，百年多病独登台。', 'size': 17, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '—— 杜甫《登高》', 'size': 12, 'color': MUTED, 'font': HEI, 'space_after': 14},
             {'text': '枯藤老树昏鸦，小桥流水人家，古道西风瘦马。', 'size': 17, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '—— 马致远《天净沙·秋思》', 'size': 12, 'color': MUTED, 'font': HEI}])
    # 右：毛泽东赞秋
    rc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(6.1), M + Inches(1.7), Inches(5.7), Inches(4.6))
    rc.fill.solid(); rc.fill.fore_color.rgb = INK; rc.line.fill.background(); rc.shadow.inherit = False
    textbox(s, M + Inches(6.4), M + Inches(1.95), Inches(5.1), Inches(0.5),
            [{'text': '毛泽东的秋天 · 生机磅礴', 'size': 17, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(6.4), M + Inches(2.6), Inches(5.1), Inches(3.5),
            [{'text': '万山红遍，层林尽染；漫江碧透，百舸争流。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '鹰击长空，鱼翔浅底，万类霜天竞自由。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 14},
             {'text': '同是写秋，毛泽东不附和悲凉，反以秋写力量与自由。', 'size': 14, 'color': SOFT, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P4 知人论世 1925 ----------
def s_background(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['xiang'], W - M - Inches(5.0), M, Inches(5.0), Inches(5.8))
    scrim(s, W - M - Inches(5.0), M + Inches(4.5), Inches(5.0), Inches(1.3), INK, 0.45)
    caption(s, '湘江与橘子洲 · 长沙', W - M - Inches(5.0), M + Inches(5.85), Inches(5.0))
    kicker(s, '知人论世 · 1925', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.6), Inches(0.7),
            [{'text': '风雨飘摇中的追问', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(6.6), Inches(4.8),
            [{'text': '1925 年，军阀赵恒惕统治湖南。毛泽东回湘领导农民运动，遭通缉追捕，脱险后辗转来到长沙。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '他独立橘子洲头，面对寒秋湘江，抚今追昔——当年风华正茂的师范生，如今已在时代洪流中搏击。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '「问苍茫大地，谁主沉浮」不是闲情，而是革命低潮、个人险境里，对民族命运的深沉诘问。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P5 诵读：全词 ----------
def s_recite(s):
    bg(s, PAPER)
    kicker(s, '诵读 · 上下阕全词', M, M, FROST)
    paras = [
        {'text': '上　阕', 'size': 16, 'color': FROST, 'bold': True, 'font': HEI, 'space_after': 6},
        {'text': '独立寒秋，湘江北去，橘子洲头。', 'size': 21, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 7},
        {'text': '看万山红遍，层林尽染；漫江碧透，百舸争流。', 'size': 21, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 7},
        {'text': '鹰击长空，鱼翔浅底，万类霜天竞自由。', 'size': 21, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 7},
        {'text': '怅寥廓，问苍茫大地，谁主沉浮？', 'size': 21, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 12},
        {'text': '下　阕', 'size': 16, 'color': XIANG, 'bold': True, 'font': HEI, 'space_after': 6},
        {'text': '携来百侣曾游。忆往昔峥嵘岁月稠。', 'size': 21, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 7},
        {'text': '恰同学少年，风华正茂；书生意气，挥斥方遒。', 'size': 21, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 7},
        {'text': '指点江山，激扬文字，粪土当年万户侯。', 'size': 21, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 7},
        {'text': '曾记否，到中流击水，浪遏飞舟？', 'size': 21, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.5},
    ]
    textbox(s, M, M + Inches(1.15), CW, Inches(5.3), paras)
    # 领字 chips
    chips = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, H - Inches(0.92), CW, Inches(0.6))
    chips.fill.solid(); chips.fill.fore_color.rgb = SOFT; chips.line.color.rgb = GOLD; chips.line.width = Pt(1.2); chips.shadow.inherit = False
    textbox(s, M + Inches(0.2), H - Inches(0.82), CW - Inches(0.4), Inches(0.45),
            [{'text': '领字脉络：看（写景）· 怅/问（发问）· 忆（回忆）· 恰（铺展）· 记（收束）', 'size': 14, 'color': INK, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)


# ---------- P6 上阕意象解码：四幅画面 ----------
def s_imagery(s):
    bg(s, PAPER)
    kicker(s, '上阕意象解码 · 一个「看」字领七句', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '四幅秋景，拼成壮阔湘江图', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    place_photo(s, PHOTO['yuelu'], M, M + Inches(1.5), Inches(3.4), Inches(2.7))
    caption(s, '岳麓山 · 万山红遍', M, M + Inches(4.35), Inches(3.4))
    cards = [
        ('远眺', '万山红遍，层林尽染', '群峰如染，红透天际'),
        ('近观', '漫江碧透，百舸争流', '秋水澄碧，千帆竞发'),
        ('仰视', '鹰击长空', '「击」字写尽雄健进取'),
        ('俯瞰', '鱼翔浅底', '「翔」字写尽自由轻快'),
    ]
    cw = (CW - Inches(3.4) - Inches(0.4) - Inches(0.3) * 1) / 2
    x0 = M + Inches(3.9)
    ys = [M + Inches(1.5), M + Inches(3.0)]
    for i, (tag, line, feat) in enumerate(cards):
        col = i % 2; row = i // 2
        x = x0 + col * (cw + Inches(0.3))
        y = ys[row]
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(1.4))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = FROST if i % 2 == 0 else XIANG; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.2), y + Inches(0.12), Inches(1.3), Inches(0.4),
                [{'text': tag, 'size': 13, 'color': card.line.color.rgb, 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.2), y + Inches(0.5), cw - Inches(0.4), Inches(0.5),
                [{'text': line, 'size': 15, 'color': INK, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.2), y + Inches(0.98), cw - Inches(0.4), Inches(0.4),
                [{'text': feat, 'size': 12, 'color': MUTED, 'font': KAI}])
    band = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, H - Inches(0.92), CW, Inches(0.62))
    band.fill.solid(); band.fill.fore_color.rgb = INK; band.shadow.inherit = False
    textbox(s, M, H - Inches(0.83), CW, Inches(0.45),
            [{'text': '由远及近、由天到水——空间层层展开，秋景生机盎然，绝无半点萧瑟', 'size': 16, 'color': GOLD, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)


# ---------- P7 炼字：击与翔 ----------
def s_refine(s):
    bg(s, PAPER)
    kicker(s, '炼字 · 换一个字，味道全变', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '「击」「翔」二字，力透纸背', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.4)) / 2
    # 击
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.55), cw, Inches(4.4))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = FROST; c1.line.width = Pt(1.8); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.8), cw - Inches(0.6), Inches(0.6),
            [{'text': '鹰 击 长 空', 'size': 26, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M + Inches(0.3), M + Inches(2.7), cw - Inches(0.6), Inches(3.0),
            [{'text': '若作「鹰飞长空」——只说会飞，平淡无力。', 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '「击」——如利爪搏击苍穹，写尽雄健与进取。', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '一上一下：鹰击长空、鱼翔浅底，一天一地，尽显词人胸襟之阔。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    # 翔
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(1.55), cw, Inches(4.4))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(1.8), cw - Inches(0.6), Inches(0.6),
            [{'text': '鱼 翔 浅 底', 'size': 26, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(2.7), cw - Inches(0.6), Inches(3.0),
            [{'text': '若作「鱼游浅底」——只说游动，失了灵气。', 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '「翔」——如鸟翔于云霄，写尽自由轻快。', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '江水映天，鱼在清澈江面游走，仿佛游于蓝天白云之间。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P8 视角与色彩 ----------
def s_color(s):
    bg(s, PAPER)
    kicker(s, '视角与色彩 · 画面为何壮阔', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '红碧交织，远近视俯', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    place_photo(s, PHOTO['maple'], M, M + Inches(1.5), Inches(3.0), Inches(2.3))
    caption(s, '层林尽染 · 红', M, M + Inches(3.95), Inches(3.0))
    place_photo(s, PHOTO['isle'], M + Inches(3.4), M + Inches(1.5), Inches(3.0), Inches(2.3))
    caption(s, '橘子洲头 · 俯瞰', M + Inches(3.4), M + Inches(3.95), Inches(3.0))
    textbox(s, M + Inches(6.9), M + Inches(1.5), Inches(5.4), Inches(4.4),
            [{'text': '色　彩', 'size': 17, 'color': FROST, 'bold': True, 'font': HEI, 'space_after': 5},
             {'text': '「万山红遍」与「漫江碧透」——红与碧强烈对比，视觉冲击力拉满。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '视　角', 'size': 17, 'color': XIANG, 'bold': True, 'font': HEI, 'space_after': 5},
             {'text': '远眺万山、近观漫江、仰视飞鹰、俯瞰游鱼——四重空间层层展开。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '由「特写」到「万类霜天竞自由」的全景，视野越来越开阔。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P9 诗眼：谁主沉浮 ----------
def s_eye(s):
    bg(s, PAPER)
    kicker(s, '诗眼 · 全词落点', M, M, FROST)
    quote_block(s, M, M + Inches(1.2), CW, '问苍茫大地，谁主沉浮？', '上阕结句 · 千古绝唱', FROST)
    textbox(s, M, M + Inches(4.0), CW, Inches(2.6),
            [{'text': '面对生机勃勃的宇宙，词人「怅寥廓」——不是悲伤，而是由壮景生出的深沉思虑：万物竞自由，而现实中的国家民族却身不自由。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '于是发出惊天一问：中国的命运，究竟由谁来主宰？这一问，是上阕写景的落点，也是下阕回忆的引子。', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P10 下阕：同学少年群像 ----------
def s_youth(s):
    bg(s, PAPER)
    kicker(s, '下阕 · 同学少年群像', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '能「主沉浮」的，是这样一群人', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    dims = [
        ('年龄', '同学少年', '正值青春年华'),
        ('精神', '风华正茂', '风采才华旺盛勃发'),
        ('才干', '挥斥方遒', '意气风发强劲有力'),
        ('行动', '指点江山\n激扬文字', '评点时局宣扬真理'),
        ('抱负', '粪土当年\n万户侯', '蔑视权贵改天换地'),
    ]
    cw = (CW - Inches(0.25) * 4) / 5
    y = M + Inches(1.7)
    for i, (dim, word, mean) in enumerate(dims):
        x = M + i * (cw + Inches(0.25))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.6))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = FROST if i % 2 == 0 else XIANG; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x, y + Inches(0.22), cw, Inches(0.4),
                [{'text': dim, 'size': 14, 'color': card.line.color.rgb, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x, y + Inches(0.75), cw, Inches(1.1),
                [{'text': word, 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER, 'line': 1.1}])
        textbox(s, x, y + Inches(1.95), cw, Inches(1.5),
                [{'text': mean, 'size': 13, 'color': MUTED, 'font': KAI, 'align': PP_ALIGN.CENTER, 'line': 1.4}])
    band = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, H - Inches(0.92), CW, Inches(0.62))
    band.fill.solid(); band.fill.fore_color.rgb = INK; band.shadow.inherit = False
    textbox(s, M, H - Inches(0.83), CW, Inches(0.45),
            [{'text': '胸怀天下、才华超群、敢于批判、蔑视权贵——这正是词人心中能主沉浮的力量', 'size': 16, 'color': GOLD, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)


# ---------- P11 问答呼应 + 中流击水 ----------
def s_answer(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['sail'], W - M - Inches(5.0), M, Inches(5.0), Inches(4.4))
    caption(s, '百舸争流 · 击水意象', W - M - Inches(5.0), M + Inches(4.5), Inches(5.0))
    kicker(s, '上阕问 · 下阕答', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.6), Inches(0.6),
            [{'text': '一问一答，浑然一体', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(6.6), Inches(4.6),
            [{'text': '上阕「谁主沉浮」一出，下阕便以回忆作答。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '「忆往昔峥嵘岁月稠」——当年同学少年，正是能主沉浮的力量。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '「到中流击水，浪遏飞舟」：在时代洪流中奋勇拼搏的象征。', 'size': 15, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '这正是对「谁主沉浮」的响亮回答：敢搏风浪的新青年！', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P12 对比思辨 ----------
def s_compare(s):
    bg(s, PAPER)
    kicker(s, '对比思辨 · 格局何在', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '同写秋与青年，气象各不相同', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    rows = [
        ('《沁园春·雪》', '「数风流人物，还看今朝」', '与本文互文：主沉浮者，正在今朝青年', FROST),
        ('刘禹锡《秋词》', '「我言秋日胜春朝」', '亦赞秋，却偏个人情志，格局稍窄', XIANG),
        ('杜甫《登高》', '「万里悲秋常作客」', '个人身世悲慨，未及家国之问', MUTED),
    ]
    y = M + Inches(1.7)
    for title, quote, note, col in rows:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(1.35))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.4); card.shadow.inherit = False
        textbox(s, M + Inches(0.25), y + Inches(0.18), Inches(3.2), Inches(1.0),
                [{'text': title, 'size': 17, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(3.6), y + Inches(0.2), Inches(4.2), Inches(1.0),
                [{'text': quote, 'size': 16, 'color': INK, 'font': KAI, 'line': 1.3}])
        textbox(s, M + Inches(8.0), y + Inches(0.2), CW - Inches(8.2), Inches(1.0),
                [{'text': note, 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.4}])
        y += Inches(1.5)
    band = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, H - Inches(0.92), CW, Inches(0.62))
    band.fill.solid(); band.fill.fore_color.rgb = INK; band.shadow.inherit = False
    textbox(s, M, H - Inches(0.83), CW, Inches(0.45),
            [{'text': '本词融个人理想与国家命运，格局宏大——这是红色诗词独有的气魄', 'size': 16, 'color': GOLD, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)


# ---------- P13 写法小结 ----------
def s_craft(s):
    bg(s, PAPER)
    kicker(s, '写法小结 · 三把钥匙', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '读懂诗词的鉴赏路径', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    crafts = [
        ('情景交融', '上阕句句写景，却处处是词人开阔胸襟的外现——秋景愈生机，愈见其豪情。', FROST),
        ('虚实结合', '上阕「看」为实写眼前秋景；下阕「忆」为虚写往昔岁月，虚实相生。', XIANG),
        ('炼字造境', '遍·染·透·争·击·翔——六个动词撑起立体秋景与昂扬生命力。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (title, body, col) in enumerate(crafts):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.6))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + cw/2 - Inches(0.35), y + Inches(0.3), Inches(0.7), Inches(0.7))
        dot.fill.solid(); dot.fill.fore_color.rgb = col; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, x, y + Inches(1.2), cw, Inches(0.5),
                [{'text': title, 'size': 20, 'color': col, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(1.8), cw - Inches(0.6), Inches(1.6),
                [{'text': body, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P14 作业与升华 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业与升华', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '分层作业 · 青春的价值', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '背诵并工整默写全词；摘抄文中精彩炼字，每处写 20 字赏析。', FROST),
        ('提升 · 选做', '对比杜甫《登高》与本词的「秋」，写 150 字短评。', XIANG),
        ('拓展 · 实践', '拍摄身边秋日壮阔景致，仿「万类霜天竞自由」写一段写景短句。', GOLD),
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
    band = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, H - Inches(0.95), CW, Inches(0.7))
    band.fill.solid(); band.fill.fore_color.rgb = INK; band.shadow.inherit = False
    textbox(s, M, H - Inches(0.86), CW, Inches(0.5),
            [{'text': '百年前青年以救国为责；新时代青年亦当心怀家国，勇担使命。', 'size': 17, 'color': GOLD, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)


# ---------- BUILD ----------
for fn in [s_cover, s_contents, s_intro, s_background, s_recite, s_imagery,
           s_refine, s_color, s_eye, s_youth, s_answer, s_compare, s_craft, s_homework]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(BASE, 'preview_v7', 'qinyuanchun.pptx')
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
# === PART2 END ===
