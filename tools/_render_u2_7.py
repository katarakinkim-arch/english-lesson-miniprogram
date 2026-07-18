# -*- coding: utf-8 -*-
# 《写作讲评——人物通讯的修改与提升》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条 WebSearch 核实）：
#   教材：人教版必修上第二单元"单元学习任务"，承接第六课时"学写人物通讯"初稿与互评，进入修改讲评。
#   课标：《普通高中语文课程标准》"实用性阅读与交流"任务群——写作须真实·得体·清晰。
#   以事实细节作主体发言（人民日报客户端《5招教你写好人物通讯稿》）：
#     "人物通讯必须以事实的细节为支撑"；"2千字以上的通讯应有3个以上的细节描写"（成组的典型细节）。
#   少评价·多描述（《学习写人物通讯稿》topnews）：把"他无私奉献"换成"总把工资三分之一捐出、
#     自己常年穿洗得发白的衬衫"；核心标签≠空洞形容词（"用10年走坏20双鞋的孩子摆渡人"≠"优秀乡村教师"）。
#   真实是通讯的生命（搜狐《浅谈怎样写好人物通讯》）：不能添枝加叶、随意拔高。
#   场景/细节论（穆青，新华社原社长，《县委书记的榜样——焦裕禄》作者）：
#     "获得细节，处理好细节，是记者思想水平与技巧的综合反映"；《焦裕禄》"倚门望雪"以场景烘托人物。
#   写作评价标准（《高中语文人物通讯写作评价标准探析》）：真实书写·形象饱满·结构清晰·语言平实。
# 真实照片（自由授权，复用同单元第六课时已下载，规范§3允许相邻课复用）：
#   typewriter.jpg  经典打字机（Wikimedia Commons, CC BY 4.0）——写作与修改工具的见证
#   ctype.jpg       中文打字机（Wikimedia Commons, CC BY-SA 4.0）——"写作"的实物象征
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PH = lambda n: os.path.join(HERE, '_photos_u2_7', n)
PHOTO = {
    'ctype': PH('ctype.jpg'),
    'typewriter': PH('typewriter.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['typewriter'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第二单元 · 劳动光荣 · 第七课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.05), Inches(12.3), Inches(2.0),
            [{'text': '写作讲评', 'size': 52, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.2), Inches(12.3), Inches(1.2),
            [{'text': '人物通讯的修改与提升', 'size': 32, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.7), Inches(12), Inches(1.1),
            [{'text': '把"评价"改成"画面"——让事件自己说明"好"。', 'size': 17, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.4), Inches(12), Inches(1.0),
            [{'text': '好通讯三标准：真实 · 典型 · 以事写人。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P2 目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '依据讲评反馈修改通讯终稿，做到选材典型、结构清晰、语言简洁、无评价词违规。', FROST),
        ('文化意识', '在公开讲评中欣赏他人笔下的劳动者形象，涵养尊重普通劳动者的表达态度。', XIANG),
        ('思维品质', '诊断三种典型习作的优缺点，发展评价意识与自我修订能力。', GOLD),
        ('学习能力', '内化"好通讯三标准"（真实·典型·以事写人），能独立评价并修改通讯。', MUTED),
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

# ---------- P3 背景：从"写出来"到"改得好" ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '承前启后 · 从写到改', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.25), col_w, Inches(0.6),
            [{'text': '从"写出来"到"改得好"', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
    textbox(s, lx, M + Inches(1.95), col_w, Inches(4.6),
            [{'text': '上一课完成了人物通讯初稿，并做了一轮互评——', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '本课进入修改提升与公开讲评。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '依据课标"实用性阅读与交流"：写作须真实·得体·清晰。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '通讯的生命是真实：不添枝加叶、不随意拔高；', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 3},
             {'text': '改稿不是改对错，而是把"评价"改成"画面"。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['typewriter'], rx, M + Inches(1.25), col_w, Inches(2.5))
    caption(s, '经典打字机（CC BY 4.0）· 写作与修改工具的见证', rx, M + Inches(3.85), col_w)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.3), col_w, Inches(2.2))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.45), col_w - Inches(0.6), Inches(0.5),
            [{'text': '好通讯三标准', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(5.0), col_w - Inches(0.6), Inches(1.4),
            [{'text': '· 真实：实事求是，不虚构、不拔高', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 3},
             {'text': '· 典型：事件精当，删掉它形象会变', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 3},
             {'text': '· 以事写人：不说"好"，让事实说话', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P4 重点：三种典型习作诊断 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三种典型诊断', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '在"别人的通讯"里看见自己的问题', 'size': 24, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('A｜评价词违规', '通篇"伟大·无私·默默奉献"，只有评价、没有事实。', '诊断：全是空话标签，读完记不住这个人。', FROST),
        ('B｜选材不准', '门卫的一天写成流水账：穿制服、看学生、传达室吃饭——都是"这一类"的共性。', '诊断：删掉任一句形象都不变 = 不典型。', XIANG),
        ('C｜以事写人 ✓', '打饭时张阿姨的手总在抖——一勺红烧肉抖掉两块，又偷偷补上三块。"勺子替她说了。"', '赏析：不说"善良"，借物代言，好自现。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, note, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': t, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(2.3),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
        textbox(s, x + Inches(0.3), y + Inches(3.2), cw - Inches(0.6), Inches(0.9),
                [{'text': note, 'size': 12.5, 'color': col, 'bold': True, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P5 重点：修改三方向 ----------
def s_revise(s):
    bg(s, PAPER)
    kicker(s, '重点 · 修改三方向', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '换素材 → 调结构 → 改语言', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('① 换素材', '更典型', '删掉流水账与共性事件，选 1–2 个体现精神的独有细节。检测尺：删掉它，形象变不变？', FROST),
        ('② 调结构', '更清晰', '三选一定线索：时间线 / 细节聚焦 / 时间跨度，先搭骨架再落笔。', XIANG),
        ('③ 改语言', '评价→画面', '全文检索评价词，逐句换成具体事件。"伟大"→"亮着灯"，"无私"→"感冒药"。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, tag, body, col) in enumerate(steps):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.3), y + Inches(0.3), cw - Inches(0.6), Inches(0.6),
                [{'text': t, 'size': 22, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.3), y + Inches(1.05), cw - Inches(0.6), Inches(0.5),
                [{'text': tag, 'size': 15, 'color': MUTED, 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.3), y + Inches(1.75), cw - Inches(0.6), Inches(2.2),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P6 难点：三处易卡 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三处容易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('评价词自检难', '不自觉写出"伟大·无私"。→ 用"全文检索法"逐句排查，圈出所有形容词式评价。', FROST),
        ('舍不得删素材', '"写了就舍不得删"。→ 用检测尺追问：删掉它形象变不变？不变就删。', XIANG),
        ('赏析只会"夸"', '评点只说"写得好"。→ 赏析要落到具体词句：好在哪、为什么好。', GOLD),
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

# ---------- P7 探究：对比修改法 + 约束修改法 + 细节论 ----------
def s_explore(s):
    bg(s, PAPER)
    kicker(s, '探究 · 招牌招式', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': '对比修改法 + 约束修改法', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.5)) / 2
    lx = M
    m1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.55), cw, Inches(2.25))
    m1.fill.solid(); m1.fill.fore_color.rgb = WHITE; m1.line.color.rgb = FROST; m1.line.width = Pt(1.8); m1.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.72), cw - Inches(0.6), Inches(0.5),
            [{'text': '① 对比修改法', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.25), cw - Inches(0.6), Inches(1.5),
            [{'text': '同一句两版对照：原句"她待人特别好，是大家眼里的热心人"；改句"办公室的灯总亮到很晚，抽屉里备着感冒药，谁嗓子哑了就递一盒"。', 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '评价变成了画面，好自现。', 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    m2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(4.0), cw, Inches(2.25))
    m2.fill.solid(); m2.fill.fore_color.rgb = WHITE; m2.line.color.rgb = XIANG; m2.line.width = Pt(1.8); m2.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(4.17), cw - Inches(0.6), Inches(0.5),
            [{'text': '② 约束修改法', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(4.7), cw - Inches(0.6), Inches(1.5),
            [{'text': '终稿通篇不许出现"伟大·无私·奉献"等评价词——用约束逼出以事写人。', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '写漏了就划掉，换成具体事件。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    rx = M + cw + Inches(0.5)
    place_photo(s, PHOTO['ctype'], rx, M + Inches(1.55), cw, Inches(2.3))
    caption(s, '中文打字机（CC BY-SA 4.0）· "写作"的实物象征', rx, M + Inches(3.95), cw)
    qbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.35), cw, Inches(1.9))
    qbox.fill.solid(); qbox.fill.fore_color.rgb = INK; qbox.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.5), cw - Inches(0.6), Inches(1.7),
            [{'text': '穆青（新华社原社长，《焦裕禄》作者）：', 'size': 13, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 5},
             {'text': '"获得细节、处理好细节，是记者综合水平的反映。"', 'size': 13, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 5},
             {'text': '《焦裕禄》以"倚门望雪"的场景烘托人——细节比评价更有力量。', 'size': 12, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P8 板书 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 通讯修改', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.4), Inches(0.4),
            [{'text': '维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(4.0), M + Inches(1.28), Inches(8.4), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('好通讯三标准', '真实(不虚构) · 典型(事件精当) · 以事写人', FROST),
        ('习作A 评价词违规', '删评价加事实：伟大→亮着灯，无私→感冒药', XIANG),
        ('习作B 选材不准', '删流水账选典型：穿制服→记住每个名字', GOLD),
        ('习作C 以事写人 ✓', '借物代言：手抖→"勺子替她说了"', FROST),
        ('修改三方向', '换素材 · 调结构 · 改语言（评价→画面）', XIANG),
        ('互签量表', '真实 | 典型 | 结构 | 语言（四维互评）', GOLD),
    ]
    y = M + Inches(1.85)
    for i, (dim, a, col) in enumerate(rows):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.58))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.1), Inches(3.4), Inches(0.4),
                [{'text': dim, 'size': 14, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(4.0), y + Inches(0.1), Inches(8.4), Inches(0.4),
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
        ('基础 · 必做', '依据讲评修改通讯终稿并誊抄：先全文检索评价词，再核对选材是否典型；文下附 50 字自评（改了什么·为什么改）。', FROST),
        ('提升 · 选做', '为通讯拟正副标题（主标题有文采 + 副标题点明身份），并注明所选结构：时间线 / 细节聚焦 / 时间跨度。', XIANG),
        ('拓展 · 衔接', '与同桌互签：写一句具体评语（一处优点 + 一处可改），为下一课单元活动"我身边的劳动者"分享做准备。', GOLD),
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
            [{'text': '通讯修改口诀', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '检索评价词 → 换典型素材 → 改成画面语言。下一课：单元活动"我身边的劳动者"分享与单元总结。', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_revise,
           s_difficulties, s_explore, s_blackboard, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-7.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
