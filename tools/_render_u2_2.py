# -*- coding: utf-8 -*-
# 《心有一团火，温暖众人心》×《"探界者"钟扬》群文比较 — 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条核实）：
#   张秉贵：光明日报 2016-06-26《张秉贵:心中"一团火",温暖万人心》；中新网/经济日报《最美奋斗者》
#   钟扬：新华社/人民日报 2018-03-25《一粒种子造福万千苍生》；2018"感动中国"；中宣部"时代楷模"
#   教学招式：名师论文《任务·问题·情境——以人物通讯群文阅读教学为例》(sohu 394096162)
#             —— "以疑定教"：用学生真实疑问推进"选材典型性"探究；课内外文段比对
# 真实照片（自由授权）：
#   zhang_binggui.jpg  1963年北京张秉贵（Wikimedia Commons, Public domain）
#   wangfujing.jpg     王府井百货大楼（Wikimedia Commons, CC BY-SA 3.0）
#   tibet.jpg          西藏高原（钟扬16年采种环境, Wikimedia Commons, CC BY-SA 3.0 de）
#   说明：钟扬本人肖像为新华社版权照片，依规未使用；以采种环境照替代并明确标注。
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PH = lambda n: os.path.join(HERE, '_photos_u2_2', n)
PHOTO = {
    'zhang':  PH('zhang_binggui.jpg'),
    'wang':   PH('wangfujing.jpg'),
    'tibet':  PH('tibet.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['zhang'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.5)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第二单元 · 劳动光荣', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.2), Inches(12), Inches(2.2),
            [{'text': '心有一团火', 'size': 50, 'color': WHITE, 'bold': True, 'font': KAI},
             {'text': '「探界者」钟扬', 'size': 50, 'color': WHITE, 'bold': True, 'font': KAI, 'space_before': 8}])
    textbox(s, M, Inches(4.7), Inches(12), Inches(0.7),
            [{'text': '两篇人物通讯 · 群文比较阅读', 'size': 19, 'color': SOFT, 'font': HEI}])
    textbox(s, M, Inches(5.6), Inches(12), Inches(1.2),
            [{'text': '平凡柜台的坚守，与高原上的追寻——劳动光荣，不分工种。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P2 目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '概括两篇通讯的核心事件与人物精神，说出选材的典型性差异。', FROST),
        ('文化意识', '理解「平凡岗位坚守」与「科学探索执着」都是劳动精神的不同呈现。', XIANG),
        ('思维品质', '比较两篇通讯的选材角度、描写手法与情感基调，培养归纳能力。', GOLD),
        ('学习能力', '掌握「同主题·异选材·比手法」的群文路径，能迁移到其他实用文。', MUTED),
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

# ---------- P3 背景：两双劳动的手 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '知人论世 · 两双劳动的手', M, M, FROST)
    col_w = Inches(5.75)
    # 左：张秉贵
    lx = M
    place_photo(s, PHOTO['zhang'], lx, M + Inches(1.3), col_w, Inches(2.5))
    caption(s, '张秉贵（1963年，北京）· 新华社资料', lx, M + Inches(4.0), col_w)
    textbox(s, lx, M + Inches(4.45), col_w, Inches(2.1),
            [{'text': '张秉贵（1918—1987）', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '· 1955年36岁入王府井百货糖果柜台，一站32年', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 练就「一抓准」「一口清」，待客近400万人次', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 发明「接一问二联三」，柜台被誉为「燕京第九景」', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 1979年全国劳模，著有《张秉贵柜台服务艺术》', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}])
    # 右：钟扬
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['tibet'], rx, M + Inches(1.3), col_w, Inches(2.5))
    caption(s, '西藏高原 · 钟扬16年采种之地（环境照）', rx, M + Inches(4.0), col_w)
    textbox(s, rx, M + Inches(4.45), col_w, Inches(2.1),
            [{'text': '钟扬（1964—2017）', 'size': 18, 'color': XIANG, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '· 中科大少年班→复旦教授，2001年起援藏16年', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 采得4000余万颗种子（近西藏植物1/5）', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 海拔6200米采到鼠曲雪兔子（人类采样最高点）', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '· 2017.9.25赴鄂尔多斯讲课途中车祸殉职，「时代楷模」', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P4 重点：两篇通讯的核心 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 两篇通讯的核心', M, M, FROST)
    cw = (CW - Inches(0.5)) / 2
    # 张秉贵
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.4), cw, Inches(4.4))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = FROST; c1.line.width = Pt(2); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.65), cw - Inches(0.6), Inches(0.6),
            [{'text': '《心有一团火》· 张秉贵', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M + Inches(0.3), M + Inches(2.45), cw - Inches(0.6), Inches(3.1),
            [{'text': '一抓准', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'space_after': 2},
             {'text': '要几斤几两，一把抓来分毫不差——缩短排队时间。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '一口清', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'space_after': 2},
             {'text': '称包同时心算报价，分毫不差。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '一团火', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'space_after': 2},
             {'text': '32年温暖每一位顾客，把售货做成服务艺术。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '→ 平凡岗位的精益求精', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI}])
    # 钟扬
    rx = M + cw + Inches(0.5)
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.4), cw, Inches(4.4))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(2); c2.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.65), cw - Inches(0.6), Inches(0.6),
            [{'text': '《"探界者"钟扬》· 钟扬', 'size': 20, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(2.45), cw - Inches(0.6), Inches(3.1),
            [{'text': '16年', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'space_after': 2},
             {'text': '扎根西藏，跋涉50多万公里盘点植物「家底」。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '4000万颗种子', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'space_after': 2},
             {'text': '为未来建一艘种子的「诺亚方舟」。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '探界者', 'size': 18, 'color': INK, 'bold': True, 'font': KAI, 'space_after': 2},
             {'text': '跨界（平原→高原·植物学→教育）的执着奉献。', 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '→ 知识分子的跨界奉献', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI}])
    page_num(s)

# ---------- P5 难点：三个拦路虎 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三个易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('「一团火」的时代隔阂', '电商时代难体会柜台服务的分量。→ 用1960年代百货长队场景与老顾客回忆，搭背景支架。', FROST),
        ('钟扬「探界」的三重义', '不止地理跨界，还有学科跨界（植物学+教育）与生命境界的超越。→ 画「探界层次图」。', XIANG),
        ('比较易「并列」难「归纳」', '习惯逐篇罗列，不善跨文本提炼共性。→ 用四维框架（人物/场景/精神/手法）收口。', GOLD),
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

# ---------- P6 探究：以疑定教（真实教学招式） ----------
def s_explore(s):
    bg(s, PAPER)
    kicker(s, '探究 · 从真问题出发', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': '同学常问的两个「为什么」', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    # 两个真实疑问
    q1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.55), CW, Inches(1.15))
    q1.fill.solid(); q1.fill.fore_color.rgb = SOFT; q1.line.color.rgb = MUTED; q1.line.width = Pt(1); q1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.7), CW - Inches(0.6), Inches(0.9),
            [{'text': '问：钟扬「胁迫」领结婚证这种生活小事，为什么也写进课文？', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.4}])
    q2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(2.85), CW, Inches(1.15))
    q2.fill.solid(); q2.fill.fore_color.rgb = SOFT; q2.line.color.rgb = MUTED; q2.line.width = Pt(1); q2.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(3.0), CW - Inches(0.6), Inches(0.9),
            [{'text': '问：张秉贵的「接一问二联三」那么绝，课文为何一笔带过？', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.4}])
    # 探究结论
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(4.2), CW, Inches(2.4))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, M + Inches(0.35), M + Inches(4.4), CW - Inches(0.7), Inches(2.1),
            [{'text': '通讯选材的窍门：不贪多，只选最能凸显人物精神的典型事件。', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '· 写钟扬领结婚证——见出他「把科普当逗乐」的赤子性情；', 'size': 14.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 5},
             {'text': '· 略写售货法——因为通讯要突出的是「一团火」的服务心，不是技术手册；', 'size': 14.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 5},
             {'text': '· 课内外比对：课外写科考艰苦（吃苦耐劳），课文写高原反应仍坚持（责任与拼命）——同一人，不同侧面，皆为真。', 'size': 14.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P7 板书：双栏比较表 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 群文比较表', M, M, FROST)
    # 表头
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.3), CW, Inches(0.62))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.4), Inches(3.0), Inches(0.45),
            [{'text': '比较维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(3.6), M + Inches(1.4), Inches(4.2), Inches(0.45),
            [{'text': '《心有一团火》张秉贵', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(8.2), M + Inches(1.4), Inches(4.2), Inches(0.45),
            [{'text': '《探界者》钟扬', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('人物身份', '售货员', '大学教授'),
        ('劳动场景', '王府井糖果柜台', '西藏高原采种'),
        ('精神品质', '精益求精·坚守', '跨界奉献'),
        ('选材手法', '细节反复（一抓准）', '数据跨度（16年/4000万颗）'),
    ]
    y = M + Inches(2.05)
    for i, (dim, a, b) in enumerate(rows):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.72))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.15), Inches(3.0), Inches(0.45),
                [{'text': dim, 'size': 15, 'color': INK, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(3.6), y + Inches(0.15), Inches(4.2), Inches(0.45),
                [{'text': a, 'size': 14, 'color': FROST, 'font': KAI}])
        textbox(s, M + Inches(8.2), y + Inches(0.15), Inches(4.2), Inches(0.45),
                [{'text': b, 'size': 14, 'color': XIANG, 'font': KAI}])
        y += Inches(0.8)
    # 归纳
    textbox(s, M, y + Inches(0.15), CW, Inches(0.9),
            [{'text': '劳动光荣 ＝ 坚守（张秉贵）＋ 创新（袁隆平）＋ 奉献（钟扬）', 'size': 19, 'color': INK, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ---------- P8 作业：分层 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '完成两篇通讯比较表（人物｜场景｜精神｜选材手法），各维度用一句话概括；并从每篇找1个最打动你的细节写50字赏析。', FROST),
        ('提升 · 选做', '写200字短评「劳动光荣不分工种——从三篇通讯看劳动精神的多元呈现」，要求引用≥2篇细节、点明共性、联系当代职业观。', XIANG),
        ('拓展 · 实践', '用「同主题·异选材·比手法」，假设三篇通讯的选材手法互换会怎样？体会典型选材的力量。', GOLD),
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
                [{'text': body, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)

# ---------- P9 总结：劳动光荣不分工种 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '总结 · 劳动光荣不分工种', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '三双手，同一种光荣', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    pillars = [
        ('坚守', '张秉贵', '柜台前的一抓准，是把平凡做到极致的执着。', FROST),
        ('创新', '袁隆平', '稻田里的14万株筛选，是用实践质疑权威的勇气。', XIANG),
        ('奉献', '钟扬', '高原上的4000万颗种子，是把生命写进未来的胸怀。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.8)
    for i, (t, who, b, col) in enumerate(pillars):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.5))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.25), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 24, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(0.95), cw - Inches(0.5), Inches(0.5),
                [{'text': who, 'size': 16, 'color': INK, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(1.5), cw - Inches(0.6), Inches(0.9),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
    # 收束面板
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(5.2), CW, Inches(1.9))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, M + Inches(0.3), Inches(5.45), Inches(0.06), GOLD, 30)
    textbox(s, M + Inches(0.55), Inches(5.4), CW - Inches(0.8), Inches(1.6),
            [{'text': '群文比较口诀：同主题 · 异选材 · 比手法。', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 8},
             {'text': '下节课从「记人」（通讯）转向「说理」（评论）——《以工匠精神雕琢时代品质》。', 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_difficulties,
           s_explore, s_blackboard, s_homework, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-2.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
