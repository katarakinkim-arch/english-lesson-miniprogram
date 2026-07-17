# -*- coding: utf-8 -*-
# 《写作指导——学写人物通讯：从采访到成文》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条核实）：
#   教材：人教版必修上第二单元"单元学习任务"要求"学写人物通讯"；本课将阅读所得与第五课时访谈素材转化为写作。
#   课标：《普通高中语文课程标准》"实用性阅读与交流"任务群要求写作"真实·得体·清晰"。
#   通讯四大特点（写作教学共识）：严格的真实性 · 报道的客观性 · 较强的时间性 · 描写的形象性。
#   以事写人 / 典型细节：穆青（新华社原社长，《县委书记的榜样——焦裕禄》作者）——
#     "获得细节，处理好细节，是记者思想水平、新闻敏感、采访经验、写作技巧的综合反映。"
#   选材典型化："着力抓取人物身上最闪光的东西，有所取、有所舍"，典型与否在"能否体现人物精神"而非事件大小。
#   真实性红线：通讯切忌"编造显著性事迹""高大全假大空""合理想象"，须有采访支撑（写作教学文献）。
#   教材结构三选一：时间线（袁隆平式）/细节聚焦（张秉贵式）/时间跨度（钟扬式）。
# 真实照片（自由授权）：
#   ctype.jpg       中文打字机（Wikimedia Commons, CC BY-SA 4.0）——"写作"的实物象征，契合中文书写
#   typewriter.jpg  经典打字机（Wikimedia Commons, CC BY 4.0）——写作工具的见证
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PH = lambda n: os.path.join(HERE, '_photos_u2_6', n)
PHOTO = {
    'ctype': PH('ctype.jpg'),
    'typewriter': PH('typewriter.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['ctype'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.52)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第二单元 · 劳动光荣 · 第六课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.05), Inches(12.3), Inches(2.0),
            [{'text': '写作指导', 'size': 52, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.2), Inches(12.3), Inches(1.2),
            [{'text': '学写人物通讯：从采访到成文', 'size': 32, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.7), Inches(12), Inches(1.1),
            [{'text': '把读到的、问到的劳动故事，写成一篇真实的人物通讯。', 'size': 17, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.4), Inches(12), Inches(1.0),
            [{'text': '以事写人 —— 不说"好"，让事件自己说明"好"。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P2 目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '选取 2–3 个典型事件，写一篇 600 字以内的人物通讯，做到真实·典型·有新闻感。', FROST),
        ('文化意识', '写身边的劳动者，深化对"劳动光荣"的体认，培养关注普通人的人文情怀。', XIANG),
        ('思维品质', '在"选材→剪裁→成文"中，培养信息筛选与结构组织的实用写作思维。', GOLD),
        ('学习能力', '掌握"选典型事件→定结构线索→写新闻语言"的通讯写作三步法。', MUTED),
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

# ---------- P3 背景：通讯是什么 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '知人论世 · 从读到写', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.25), col_w, Inches(0.6),
            [{'text': '为什么写"人物通讯"', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
    textbox(s, lx, M + Inches(1.95), col_w, Inches(4.6),
            [{'text': '前三课读了三篇人物通讯，第五课做了访谈——', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '本课把"读到的、问到的"变成"写出的"。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '依据《普通高中语文课程标准》"实用性阅读与交流"：写作须真实·得体·清晰。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '通讯 ≠ 记叙文：不可虚构；', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 3},
             {'text': '通讯 ≠ 表扬稿：以事写人，不空喊评价。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['typewriter'], rx, M + Inches(1.25), col_w, Inches(2.5))
    caption(s, '经典打字机（CC BY 4.0）· 写作工具的见证', rx, M + Inches(3.85), col_w)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.3), col_w, Inches(2.2))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.45), col_w - Inches(0.6), Inches(0.5),
            [{'text': '通讯四大特点', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(5.0), col_w - Inches(0.6), Inches(1.4),
            [{'text': '· 严格的真实性（不可虚构）', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 3},
             {'text': '· 报道的客观性（让事实说话）', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 3},
             {'text': '· 较强的时间性（何时何地）', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 3},
             {'text': '· 描写的形象性（细节取胜）', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P4 重点：写作三步法 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 通讯写作三步法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '选材 → 结构 → 语言', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('① 选材', '选 2–3 个典型事件。', '检测：删掉它，人物形象会不会变？不变 = 不典型。', FROST),
        ('② 结构', '三选一：时间线 / 细节聚焦 / 时间跨度。', '先定线索，再动笔，不东拉西扯。', XIANG),
        ('③ 语言', '简洁客观：动词优先于形容词。', '有数据、有言行描写，用新闻句式。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, note, col) in enumerate(steps):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.3), y + Inches(0.3), cw - Inches(0.6), Inches(0.6),
                [{'text': t, 'size': 22, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), Inches(1.0),
                [{'text': b, 'size': 15, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.45}])
        textbox(s, x + Inches(0.3), y + Inches(2.3), cw - Inches(0.6), Inches(1.7),
                [{'text': note, 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- P5 重点：三种结构借鉴 ----------
def s_structure(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三种结构借鉴', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '向单元课文学"怎么搭骨架"', 'size': 24, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('时间线（袁隆平式）', '按研究历程展开：从发现天然杂交稻到三系配套，时间推进即精神推进。', '适合：有清晰经历脉络的人。', FROST),
        ('细节聚焦（张秉贵式）', '抓招牌细节："一抓准""一口清"，一个动作写活一个人。', '适合：有标志性言行的人。', XIANG),
        ('时间跨度（钟扬式）', '用多年坚守体现精神：16年西藏采种、4000万颗种子。', '适合：长期奉献、用数据震撼的人。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, fit, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': t, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(2.2),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
        textbox(s, x + Inches(0.3), y + Inches(3.15), cw - Inches(0.6), Inches(0.9),
                [{'text': fit, 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.45, 'space_after': 4},
                 {'text': '典型≠大事：小事能体现精神也是典型。', 'size': 12.5, 'color': col, 'bold': True, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P6 难点：三个易卡 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三个易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('表扬稿 → 通讯', '习惯写"他是个好人，因为……"。→ 改"以事写人"：不说好，让事件自己说明好。', FROST),
        ('典型事件难选', '分不清"日常事件"和"典型事件"。→ 用检测尺：删掉它，人物形象变不变？', XIANG),
        ('真实性守不住', '写不出细节就"编一个"。→ 通讯不可虚构；缺细节就回去补采访，不靠想象。', GOLD),
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

# ---------- P7 探究：对比示范 + 约束写作 + 穆青细节 ----------
def s_explore(s):
    bg(s, PAPER)
    kicker(s, '探究 · 招牌招式', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': '对比示范法 + 约束写作法', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.5)) / 2
    lx = M
    m1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.55), cw, Inches(2.25))
    m1.fill.solid(); m1.fill.fore_color.rgb = WHITE; m1.line.color.rgb = FROST; m1.line.width = Pt(1.8); m1.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.72), cw - Inches(0.6), Inches(0.5),
            [{'text': '① 对比示范法', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.25), cw - Inches(0.6), Inches(1.5),
            [{'text': '同写一人：A段(表扬稿)"伟大无私……"；B段(通讯)"凌晨四点扫完三条街，弯腰捡碎瓶包好——怕扎到早起的人"。', 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': 'B段以事写人，不说好而好自现。', 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    m2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(4.0), cw, Inches(2.25))
    m2.fill.solid(); m2.fill.fore_color.rgb = WHITE; m2.line.color.rgb = XIANG; m2.line.width = Pt(1.8); m2.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(4.17), cw - Inches(0.6), Inches(0.5),
            [{'text': '② 约束写作法', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(4.7), cw - Inches(0.6), Inches(1.5),
            [{'text': '整篇不许出现"伟大·无私·奉献"等评价词——用约束逼出"以事写人"。', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '写漏了就划掉，换成具体事件。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    rx = M + cw + Inches(0.5)
    place_photo(s, PHOTO['ctype'], rx, M + Inches(1.55), cw, Inches(2.3))
    caption(s, '中文打字机（CC BY-SA 4.0）· "写作"的实物象征', rx, M + Inches(3.95), cw)
    qbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.35), cw, Inches(1.9))
    qbox.fill.solid(); qbox.fill.fore_color.rgb = INK; qbox.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.5), cw - Inches(0.6), Inches(1.7),
            [{'text': '穆青（新华社原社长，《焦裕禄》作者）：', 'size': 13, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 6},
             {'text': '"获得细节，处理好细节，是记者思想水平与技巧的综合反映。"', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- P8 板书 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 学写人物通讯', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.0), Inches(0.4),
            [{'text': '维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(3.6), M + Inches(1.28), Inches(8.8), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('写作三步', '选材(2-3典型) → 结构(三选一) → 语言(简洁+数据+言行)', FROST),
        ('三种结构', '时间线(袁隆平) · 细节聚焦(张秉贵) · 时间跨度(钟扬)', XIANG),
        ('选材检测', '删掉它→形象变不变？不变 = 不典型（小事也能典型）', GOLD),
        ('以事写人', '不说"好"，让事件自己说明"好" ≠ 表扬稿', FROST),
        ('真实性', '不可虚构；缺细节就补采访，不"编"、不"合理想象"', XIANG),
        ('互评量表', '真实 | 典型 | 结构 | 语言（四维打分）', GOLD),
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

# ---------- P9 作业 / 总结 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '按互评意见修改初稿（600字内）誊抄；在文下标注：选了哪种结构、哪 2–3 个典型事件。', FROST),
        ('提升 · 选做', '为通讯拟新闻标题：主标题有文采 + 副标题说明人物身份（如"门房里的几百个名字——记校工王师傅"）。', XIANG),
        ('拓展 · 衔接', '写你认识的人（家长/校工/身边爱岗敬业的普通人），确保可采访可核实，不写离自己太远的人。', GOLD),
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
            [{'text': '通讯写作三步法口诀', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '选典型事件 → 定结构线索 → 写新闻语言。下节课：精选初稿公开讲评（评价词违规型 / 选材不准型 / 以事写人优秀型）。', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_structure,
           s_difficulties, s_explore, s_blackboard, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-6.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
