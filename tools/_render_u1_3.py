# -*- coding: utf-8 -*-
# 《立在地球边上放号 / 红烛 群文阅读——现代诗的意象与情感》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条 WebSearch 核实）：
#   统编教材定位：高中语文必修上册第一单元「青春的价值」，任务群「文学阅读与写作」，
#     第三课时群文阅读（郭沫若《立在地球边上放号》+ 闻一多《红烛》）。
#   权威招式·温儒敏（统编高中语文教材总主编）《中学现代文教学直播实录》：
#     闻一多把李商隐「蜡炬成灰泪始干」的旧意象，重写为「心火发光、泪流」的「红烛」，
#     赋予牺牲自我、创造光明的新内涵；《红烛》末句「莫问收获，但问耕耘」即此痴情与唯美。
#     郭沫若「立在地球边上」的「大我」俯瞰全球，正是五四个性解放、自我发现的崭新精神
#     （腾讯新闻《温儒敏教授直播中学现代文教学文字实录》，2021）。
#   权威招式·闻一多《诗的格律》（1926 年 5 月 13 日北平《晨报副刊》）：
#     新诗应具「三美」——音乐的美（音节）、绘画的美（辞藻）、建筑的美（章法均齐）；
#     《红烛》反复低回、前后呼应的章法即「建筑的美」的体现（中国作家网）。
#   事实坐标（《立在地球边上放号》写于 1919 年 9—10 月，收入诗集《女神》1921；
#     《红烛》为闻一多同名诗集 1923 的序诗；创作契机为五四运动的时代冲击）——经 21cnjy / 百度百科等核对。
# 真实照片：本诗题为现代诗（五四 / 红烛 / 海洋意象），现有可复用照片均为第二单元劳动主题
#   （麦收、张秉贵、稻田等），与诗题无关联。按规范 §2.3「有真照才用真照，无则学科色块兜底
#   并明确标注，绝不糊弄」，本稿以学科色块呈现，不强行套用无关照片。
import os
HERE = os.path.dirname(os.path.abspath(__file__))
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, textbox, rule, kicker,
    new_slide, page_num, new_presentation,
)

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第一单元 · 青春的价值 · 第三课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(1.75), Inches(8.0), Inches(1.7),
            [{'text': '立在地球边上放号', 'size': 46, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.0), Inches(8.0), Inches(1.1),
            [{'text': '红烛', 'size': 46, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.15), Inches(8.0), Inches(0.7),
            [{'text': '群文阅读 · 现代诗的意象与情感', 'size': 22, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(5.0), Inches(8.0), Inches(1.0),
            [{'text': '外放与内敛，青春激情的两种声音。', 'size': 17, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    # 右侧诗摘面板（真实诗句，中性装饰）
    px = Inches(9.1); pw = Inches(3.6)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.6), pw, Inches(4.9))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, px + Inches(0.3), Inches(2.0), Inches(0.06), GOLD, 26)
    textbox(s, px + Inches(0.55), Inches(2.05), pw - Inches(0.8), Inches(0.5),
            [{'text': '诗里的话', 'size': 15, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, px + Inches(0.55), Inches(2.65), pw - Inches(0.85), Inches(3.6),
            [{'text': '不断的毁坏，\n不断的创造，\n不断的努力。', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 14},
             {'text': '—— 《立在地球边上放号》', 'size': 12, 'color': SOFT, 'font': HEI, 'space_after': 18},
             {'text': '莫问收获，\n但问耕耘。', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 14},
             {'text': '—— 《红烛》', 'size': 12, 'color': SOFT, 'font': HEI}])
    page_num(s)

# ---------- P2 学习目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '有感情地朗读两首诗，说出「白云」「洪涛」「红烛」等核心意象的象征义。', FROST),
        ('文化意识', '理解五四时期青年「破旧立新」的时代精神，体会诗人的社会责任感。', XIANG),
        ('思维品质', '比较两首诗「外放—内敛」的不同抒情方式，培养对比分析的思维能力。', GOLD),
        ('学习能力', '掌握「意象→象征→情感」的现代诗研读路径，能迁移到其他现代诗阅读。', MUTED),
    ]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + cw/2 - Inches(0.45), y + Inches(0.35), Inches(0.9), Inches(0.9))
        dot.fill.solid(); dot.fill.fore_color.rgb = col; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, x + cw/2 - Inches(0.45), y + Inches(0.55), Inches(0.9), Inches(0.5),
                [{'text': str(i+1), 'size': 24, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.5), cw - Inches(0.4), Inches(0.6),
                [{'text': t, 'size': 18, 'color': col, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.22), y + Inches(2.15), cw - Inches(0.44), Inches(1.4),
                [{'text': b, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ---------- P3 背景与权威调研 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '两首诗，一个时代', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    # 左：写作坐标（INK 面板）
    lx = M; lw = Inches(5.5)
    lbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.5), lw, Inches(4.35))
    lbox.fill.solid(); lbox.fill.fore_color.rgb = INK; lbox.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.7), lw - Inches(0.6), Inches(0.5),
            [{'text': '写作坐标', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.25), lw - Inches(0.6), Inches(3.4),
            [{'text': '《立在地球边上放号》', 'size': 14, 'color': WHITE, 'bold': True, 'font': HEI, 'line': 1.4, 'space_after': 3},
             {'text': '写于 1919 年 9—10 月，收入诗集《女神》（1921）。时郭沫若留日，于横滨海岸面对大洋，感五四浪潮而作。', 'size': 12.5, 'color': SOFT, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '《红烛》', 'size': 14, 'color': WHITE, 'bold': True, 'font': HEI, 'line': 1.4, 'space_after': 3},
             {'text': '闻一多同名诗集（1923）的序诗，以一支红烛写青春抉择与赤子之心。', 'size': 12.5, 'color': SOFT, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '共同的背景：五四运动——青年破旧立新、张扬个性的时代强音。', 'size': 12.5, 'color': GOLD, 'font': KAI, 'line': 1.45}])
    # 右：两条权威来源（白卡）
    rx = lx + lw + Inches(0.4); rw = Inches(5.83)
    def src_box(y, h, head, body, src, col):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, y, rw, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, rx + Inches(0.3), y + Inches(0.18), rw - Inches(0.6), Inches(0.45),
                [{'text': head, 'size': 15, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, rx + Inches(0.3), y + Inches(0.68), rw - Inches(0.6), h - Inches(1.0),
                [{'text': body, 'size': 12.5, 'color': INK, 'font': KAI, 'line': 1.5}])
        textbox(s, rx + Inches(0.3), y + h - Inches(0.42), rw - Inches(0.6), Inches(0.35),
                [{'text': '来源：' + src, 'size': 10.5, 'color': MUTED, 'font': HEI}])
    src_box(M + Inches(1.5), Inches(2.05),
            '统编教材总主编 · 温儒敏',
            '闻一多把李商隐「蜡炬成灰泪始干」的旧意象，重写为「心火发光、泪流」的红烛，赋予牺牲与光明的新内涵；郭沫若「立在地球边上」的「大我」俯瞰，正是五四个性解放、自我发现的崭新精神。',
            '《中学现代文教学直播实录》（腾讯新闻，2021）', FROST)
    src_box(M + Inches(3.7), Inches(2.05),
            '闻一多《诗的格律》（1926）',
            '新诗应具「三美」——音乐的美（音节）、绘画的美（辞藻）、建筑的美（章法均齐）。《红烛》反复低回、前后呼应的章法，正是「建筑的美」的体现。',
            '《晨报副刊》；中国作家网', XIANG)
    textbox(s, M, Inches(6.25), Inches(11.9), Inches(0.5),
            [{'text': '（本诗题为现代诗，现有可复用照片均属第二单元劳动主题，与诗题无关联；按规范 §2.3 以学科色块呈现，不强行套用无关图像。）', 'size': 10.5, 'color': MUTED, 'font': HEI, 'line': 1.3}])
    page_num(s)

# ---------- P4 重点 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三个抓手', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '意象 · 象征 · 比较', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('① 《放号》意象群', '白云 · 北冰洋 · 太平洋 · 洪涛——宏大意象叠加「力」的排比，表现毁灭与创造的力量。', FROST),
        ('② 《红烛》核心意象', '红烛——「烧蜡成灰」象征自我牺牲，「放光」象征传播光明，「泪」象征痛苦与赤诚。', XIANG),
        ('③ 比较阅读维度', '抒情方式（外放 / 内敛）、意象风格（宏大 / 精微）、情感基调（激越 / 悲壮）。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': t, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.9), cw - Inches(0.6), Inches(3.1),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)

# ---------- P5 方法 ----------
def s_methods(s):
    bg(s, PAPER)
    kicker(s, '方法 · 四招读懂', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '朗读 · 比较 · 支架 · 标注', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('朗读体验', '听名家朗诵，体会《放号》的激越上扬与《红烛》的深沉倾诉，读出节奏差异。', FROST),
        ('群文比较', '用双栏对照表，从意象 / 象征 / 情感 / 节奏四个维度并排比较两首诗。', XIANG),
        ('背景支架', '了解五四运动与闻一多留美经历，为「破旧立新」「赤子之心」提供理解背景。', GOLD),
        ('意象标注', '在诗上圈出意象、旁批象征义、末尾写一句话写清自己的感受。', MUTED),
    ]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.35), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 19, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.25), y + Inches(1.15), cw - Inches(0.5), Inches(2.8),
                [{'text': b, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P6 难点 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '三处容易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('「力的律动」读不出', '不熟悉自由诗节奏，看不见排比句式本身就是「力」的形式。→ 把「力的绘画，力的舞蹈……」当作一串快节奏鼓点，排比本身就在发力。', FROST),
        ('红烛的「泪」想简单了', '容易只当作「伤心的泪」。→ 区分物理的蜡油与情感的焦灼——「烧得不稳时着急得流泪」，是怕理想来得太慢。', XIANG),
        ('把意象当成了比喻', '习惯「A 像 B」。→ 「红烛像奉献的人」是比喻；「红烛就是诗人自己」是意象——物本身就是情感的载体。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.33), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.8),
                [{'text': t, 'size': 15.5, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.3}])
        textbox(s, x + Inches(0.3), y + Inches(1.15), cw - Inches(0.6), Inches(3.0),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- P7 板书精华 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书精华 · 双表对照', M, M, FROST)
    cw = (CW - Inches(0.4)) / 2
    lx = M
    # 左：放号意象表
    lc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.4), cw, Inches(3.4))
    lc.fill.solid(); lc.fill.fore_color.rgb = WHITE; lc.line.color.rgb = FROST; lc.line.width = Pt(1.8); lc.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.55), cw - Inches(0.6), Inches(0.5),
            [{'text': '《放号》意象表', 'size': 17, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.15), cw - Inches(0.6), Inches(2.5),
            [{'text': '意象 | 特征 | 象征', 'size': 13, 'color': MUTED, 'bold': True, 'font': HEI, 'space_after': 5},
             {'text': '白云 — 自由 — 宏大', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 4},
             {'text': '洪涛 — 力量 — 毁灭+创造', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 4},
             {'text': '力 — 律动 — 排比即形式', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    # 右：红烛意象表
    rx = lx + cw + Inches(0.4)
    rc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.4), cw, Inches(3.4))
    rc.fill.solid(); rc.fill.fore_color.rgb = WHITE; rc.line.color.rgb = XIANG; rc.line.width = Pt(1.8); rc.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.55), cw - Inches(0.6), Inches(0.5),
            [{'text': '《红烛》意象表', 'size': 17, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(2.15), cw - Inches(0.6), Inches(2.5),
            [{'text': '意象 | 动作 | 象征', 'size': 13, 'color': MUTED, 'bold': True, 'font': HEI, 'space_after': 5},
             {'text': '红烛 — 烧 — 牺牲', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 4},
             {'text': '光 — 放 — 光明', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 4},
             {'text': '泪 — 流 — 赤诚·焦灼', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    # 底部：比较表 + 意象定义
    pb = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(5.0), CW, Inches(1.5))
    pb.fill.solid(); pb.fill.fore_color.rgb = INK; pb.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(5.12), Inches(3.4), Inches(0.5),
            [{'text': '比较表', 'size': 15, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, M + Inches(0.3), M + Inches(5.55), CW - Inches(0.6), Inches(0.9),
            [{'text': '意象：放号宏大 | 红烛精微      情感：放号激越 | 红烛悲壮      节奏：放号排比 | 红烛反复', 'size': 13, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 4},
             {'text': '意象 ＝ 主观情志 ＋ 客观物象 → 融合体（≠ 比喻）', 'size': 14, 'color': GOLD, 'bold': True, 'font': KAI}])
    page_num(s)

# ---------- P8 作业 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '基础 · 提升 · 衔接', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '有感情地朗读两首诗，录制音频（不少于 1 分钟）；从每首诗中找出 3 个意象，写出其象征义。', FROST),
        ('提升 · 选做', '写一首 8 行以内的现代诗，以「青春的____」为题（填一个意象）：至少用 2 个意象，且意象承载情感而非简单比喻。', XIANG),
        ('衔接 · 铺垫', '本单元后续将读小说《百合花》，意象从诗歌（红烛）迁移到小说（百合花被子）——可带着「借物寄情」的眼光去读。', GOLD),
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
            [{'text': '读法口诀', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '意象 → 象征 → 情感：读诗先找「物」，再问「它寄托了什么情」。下一站——小说《百合花》。', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P9 单元小结 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '单元小结 · 青春的价值', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '两种声音，一样青春', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('意象读法', '描摹景象特点 → 分析技法 → 挖掘象征 → 关联情感与背景。把「意象→象征→情感」走通。', FROST),
        ('两种青春表达', '《放号》如洪涛奔涌，《红烛》如烛火低语；一崇高一悲壮，都是五四青年的心声。', XIANG),
        ('向小说迁移', '意象不止在诗里——下读《百合花》，看「百合花被子」如何借情节与细节承载情感。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.5))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.3), y + Inches(0.3), cw - Inches(0.6), Inches(0.6),
                [{'text': t, 'size': 17, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.3), y + Inches(1.0), cw - Inches(0.6), Inches(2.3),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(5.6), CW, Inches(1.5))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, M + Inches(0.3), Inches(5.87), Inches(0.06), GOLD, 24)
    textbox(s, M + Inches(0.55), Inches(5.78), CW - Inches(0.8), Inches(1.25),
            [{'text': '青春收束', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '「莫问收获，但问耕耘。」（闻一多《红烛》）——把青春交给行动，让意象自己说话。', 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_methods,
           s_difficulties, s_blackboard, s_homework, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u1-3.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
