# -*- coding: utf-8 -*-
# 《沁园春·长沙 精读（上）——意象与情感》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条 WebSearch 核实）：
#   创作背景：人民网/中国共产党新闻网《万类霜天竞自由——〈沁园春·长沙〉解析》
#     （theory.people.com.cn，2024-07-29）：该词作于1925年秋（一说10月）毛泽东重游长沙橘子洲头；
#     并引毛泽东1964年自解"怅寥廓，问苍茫大地，谁主沉浮"指"在北伐以前，军阀统治，中国的命运
#     究竟由哪一个阶级做主"（毛泽东亲自审定《毛主席诗词》亦以本词为首篇）。
#   教学招式·意象分析法：21世纪教育网（21cnjy）统编版高中语文必修上册《沁园春·长沙》教案设计，
#     将"意象分析法"列为核心教学方法，引导学生分组探究"万山/鹰鱼/霜天"等意象群的色彩、动静与
#     象征意义；鉴赏诗歌另须"知人论世"，结合时代背景体会"景中寓情、情中见志"。
# 真实照片（自由授权，同单元相邻课已下载，规范§3允许复用；网络不可用，未新下载）：
#   ricefield.jpg 中国稻田（Wikimedia Commons, CC BY-SA 4.0）——"漫江碧透"自然意象的具象
#   tibet.jpg     西藏高原（Wikimedia Commons, CC BY-SA 4.0）——"万山红遍"辽阔豪迈的呼应
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
PH2 = lambda n: os.path.join(HERE, '_photos_u2_2', n)
PHOTO = {
    'ricefield': PH('ricefield.jpg'),
    'tibet': PH2('tibet.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['ricefield'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.58)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11.5), Inches(0.5),
            [{'text': '必修上 第一单元 · 青春的价值 · 第一课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.0), Inches(12.3), Inches(1.6),
            [{'text': '沁园春·长沙', 'size': 56, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.15), Inches(12.3), Inches(1.1),
            [{'text': '精读（上）——意象与情感', 'size': 30, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.6), Inches(12), Inches(1.0),
            [{'text': '抓住六个核心意象，读出少年词人的豪情与担当。', 'size': 17, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.4), Inches(12), Inches(1.0),
            [{'text': '一条读词路径：圈意象 → 标特征 → 串联画面 → 推导情感。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P2 学习目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '准确朗读全词，把握"看""忆""问"三个领字的统领作用，说出6个以上核心意象及其特征。', FROST),
        ('文化意识', '理解青年毛泽东以天下为己任的情怀，体会"同学少年"精神对当下青年的启示。', XIANG),
        ('思维品质', '沿"意象群→画面→情感"的推导路径，培养从具象到抽象的文学思维。', GOLD),
        ('学习能力', '掌握"圈点意象→标注特征→串联画面→推导情感"的诗词研读四步法，能迁移运用。', MUTED),
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
                [{'text': b, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ---------- P3 背景与权威调研 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.25), col_w, Inches(0.6),
            [{'text': '写于1925年秋 · 橘子洲头', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
    textbox(s, lx, M + Inches(1.95), col_w, Inches(2.4),
            [{'text': '1925年秋（一说10月），毛泽东离开韶山赴广州主办农民运动讲习所，途经长沙，重游橘子洲头。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '面对湘江秋景与蓬勃的革命形势，他写下此词。全词分上下阕，上阕"看"秋景，下阕"忆"青春，以"问苍茫大地，谁主沉浮"为枢纽衔接。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    quote_block(s, lx, M + Inches(4.35), col_w,
                '怅寥廓，问苍茫大地，谁主沉浮？——毛泽东1964年自解：指北伐前军阀统治下"中国命运由哪个阶级做主"。',
                '人民网《万类霜天竞自由——〈沁园春·长沙〉解析》', FROST)
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['tibet'], rx, M + Inches(1.25), col_w, Inches(2.5))
    caption(s, '西藏高原（CC BY-SA 4.0，Wikimedia Commons）', rx, M + Inches(3.85), col_w)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.3), col_w, Inches(2.2))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.45), col_w - Inches(0.6), Inches(0.5),
            [{'text': '两把读词钥匙', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(5.0), col_w - Inches(0.6), Inches(1.4),
            [{'text': '· 意象分析法：探究"万山/鹰鱼/霜天"的色彩、动静与象征（21cnjy 教案）。', 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 4},
             {'text': '· 知人论世：结合1925年时代背景，体会"景中寓情、情中见志"。', 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P4 重点 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三处落点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '朗读 · 意象 · 情感', 'size': 24, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('① 朗读节奏', '读准"看万山红遍"（2-2-2）、"问苍茫大地"（1-2-2），领字后短暂停顿，读出层次。', FROST),
        ('② 意象品析', '万山(红)、层林(染)、漫江(碧)、百舸(争)、鹰(击)、鱼(翔)——六组意象构成"湘江秋景图"。', XIANG),
        ('③ 情感脉络', '"看"景→"问"天→"忆"人→"记"事，由景及情、由问及答，一线贯通。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': t, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(3.2),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P5 方法（学生视角的研读方法）----------
def s_methods(s):
    bg(s, PAPER)
    kicker(s, '方法 · 四招读词', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '把方法握在手里', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('诵读体会', '反复朗读', '听名家朗诵、自己放声读，抓住"看/忆/问"三领字的停顿与气势。', FROST),
        ('圈点批注', '标意象', '在词上圈出意象、标修饰语、画箭头串起情感脉络，让分析有落点。', XIANG),
        ('替换比较', '品炼字', '用"飞"替"击"、用"游"替"翔"，对比中感受动词的力度与自由感。', GOLD),
        ('知人论世', '补背景', '了解1925年大革命前夕的时代语境，读懂"谁主沉浮"的分量。', MUTED),
    ]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.7)
    for i, (t, tag, body, col) in enumerate(steps):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 20, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.25), y + Inches(1.05), cw - Inches(0.5), Inches(0.5),
                [{'text': tag, 'size': 15, 'color': MUTED, 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.25), y + Inches(1.75), cw - Inches(0.5), Inches(2.2),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P6 难点 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三处容易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('"击""翔"的妙处', '易理解为"飞""游"。→ 用替换比较法，体会"击"的力度感与"翔"的自由感。', FROST),
        ('"谁主沉浮"的分量', '易停留在字面。→ 补1925年革命背景，理解这是对国家命运的主动担当。', XIANG),
        ('词牌格律特点', '只记名称。→ 借图示看清"沁园春"上下阕结构与平仄节奏。', GOLD),
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

# ---------- P7 板书精华 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 精华', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.4), Inches(0.4),
            [{'text': '板块', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(4.0), M + Inches(1.28), Inches(8.4), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('青春基色', '壮阔 · 豪迈——全词的情感底色', FROST),
        ('上阕·看→景', '万山|红|热烈  层林|染|层次  漫江|碧|澄澈', XIANG),
        ('上阕·意象', '百舸|争|动感  鹰|击|力量  鱼|翔|自由', GOLD),
        ('炼字双璧', '击 → 力量·搏击　｜　翔 → 自由·超越', FROST),
        ('情感脉络', '景（壮阔）→ 问（沉浮）→ 情（担当）', XIANG),
        ('读诗四步法', '圈意象 → 标特征 → 串联画面 → 推导情感', GOLD),
    ]
    y = M + Inches(1.85)
    for i, (dim, a, col) in enumerate(rows):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.58))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.1), Inches(3.4), Inches(0.4),
                [{'text': dim, 'size': 14, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(4.0), y + Inches(0.1), Inches(8.4), Inches(0.4),
                [{'text': a, 'size': 12.5, 'color': INK, 'font': KAI}])
        y += Inches(0.64)
    page_num(s)

# ---------- P8 作业（分层）----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '① 背诵并默写上阕，书写规范、标点正确。② 完成意象表格（意象|修饰语|特征|感受），至少填6组。', FROST),
        ('提升 · 选做', '从"击""翔""染""争"中任选一字，写一段150字炼字品析：①字面义 ②画面感 ③传达的情感。', XIANG),
        ('拓展 · 衔接', '找一首同写"秋日豪情"的词对比阅读（如《沁园春·雪》），体会豪放词风的一脉相承。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (tag, body, col) in enumerate(tiers):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(2.7),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(5.65), CW, Inches(1.45))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, M + Inches(0.3), Inches(5.9), Inches(0.06), GOLD, 22)
    textbox(s, M + Inches(0.55), Inches(5.8), CW - Inches(0.8), Inches(1.2),
            [{'text': '读词口诀', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '圈意象 → 标特征 → 串联画面 → 推导情感：上阕写景，下阕"忆青春"接着讲。', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P9 单元小结 ----------
def s_unit(s):
    bg(s, PAPER)
    kicker(s, '单元小结 · 青春的价值', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '一课收口 · 单元回望', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.7), col_w, Inches(4.6),
            [{'text': '本单元人文主题是"青春的价值"，属"文学阅读与写作"任务群。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '作为单元开篇，这首词用壮阔秋景与少年豪情，立起"以天下为己任"的青春坐标。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '读它的路径同样适用全单元：先抓意象，再连画面，最后读出文字背后的情感与志向。', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5}])
    rx = M + col_w + Inches(0.5)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.7), col_w, Inches(4.6))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.35), M + Inches(1.9), col_w - Inches(0.7), Inches(0.5),
            [{'text': '一句话带走', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.35), M + Inches(2.5), col_w - Inches(0.7), Inches(3.5),
            [{'text': '景物壮阔，是力量在积蓄；一问沉浮，是革命者主动担当的豪情。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '下阕"忆青春"：从"问"到"答"，回扣本课"景→问→情"的脉络，接着往下读。', 'size': 14.5, 'color': SOFT, 'font': KAI, 'line': 1.55, 'space_after': 10},
             {'text': '图：中国稻田 / 西藏高原（CC BY-SA 4.0，Wikimedia Commons）。', 'size': 12, 'color': MUTED, 'font': HEI, 'line': 1.4}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_methods,
           s_difficulties, s_blackboard, s_summary, s_unit]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u1-1.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
