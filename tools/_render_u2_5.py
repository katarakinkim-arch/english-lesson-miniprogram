# -*- coding: utf-8 -*-
# 《口语交流——人物访谈与新闻播报训练》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条核实）：
#   教材：人教版必修上第二单元"单元学习任务"要求开展"人物访谈"与"新闻播报"实践。
#   课标：《普通高中语文课程标准》"实用性阅读与交流"任务群要求口语交际"清楚、连贯、得体"。
#   播报语态权威：张颂（中国传媒大学播音主持艺术学科奠基人）定义"播报"语言样态为
#     "字正腔圆·呼吸无声·感而不入·语尾不坠·语势稳健·讲究分寸·节奏明快·语流晓畅"
#     （《文艺报》/中国作家网，2010）——"感而不入·讲究分寸"对应客观，"节奏明快·语流晓畅"对应有节奏。
#   播报≠朗诵（朗诵有情感渲染，播报客观冷静）≠说新闻/日常说话（日常随意，播报规范简洁）；
#     规范播报以《新闻联播》为代表，特征"准确清晰·醇厚朴实·简洁明快·舒展流畅·态度客观"（新闻播报词条综合文献）。
#   新闻播音语速：央视《新闻联播》约 280–300 字/分（浙江日报相关述评）——比日常说话略快但须字字清楚。
#   访谈三层次（事实→感受→价值）即教材给出的访谈支架，符合深度访谈"由事及理"通用逻辑（如央视《面对面》追问式访谈）。
# 真实照片（自由授权）：
#   mic.jpg          手持话筒（Wikimedia Commons, CC0）——访谈/播报的标志性器物
#   vintagemic.jpg   早期广播话筒（Wikimedia Commons, Public domain）——播报传统的实物见证
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PH = lambda n: os.path.join(HERE, '_photos_u2_5', n)
PHOTO = {
    'mic': PH('mic.jpg'),
    'vintagemic': PH('vintagemic.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['mic'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.50)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第二单元 · 劳动光荣 · 第五课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.1), Inches(12.3), Inches(2.4),
            [{'text': '口语交流', 'size': 52, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.25), Inches(12.3), Inches(1.2),
            [{'text': '人物访谈 与 新闻播报训练', 'size': 34, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.7), Inches(12), Inches(1.1),
            [{'text': '把前四课读到的劳动人物，用口语"说出来"——', 'size': 17, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.35), Inches(12), Inches(1.0),
            [{'text': '访谈练"问与答"，播报练"说与听"。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P2 目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '设计 3–5 个有层次的访谈问题；用新闻播报语态播报一段劳动人物事迹（约1分钟）。', FROST),
        ('文化意识', '在访谈与播报中深化对劳动精神的理解，感受口语传播劳动故事的文化价值。', XIANG),
        ('思维品质', '借"由浅入深·由事及理"的提问层次，培养提问的逻辑性与层次感。', GOLD),
        ('学习能力', '掌握"设计问题→模拟访谈→整理记录"访谈三步法与"选材→组稿→播报"播报三步法。', MUTED),
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

# ---------- P3 背景：从阅读到表达 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '知人论世 · 从读到说', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    # 左：价值说明
    lx = M
    textbox(s, lx, M + Inches(1.25), col_w, Inches(0.6),
            [{'text': '为什么练"口语交流"', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
    textbox(s, lx, M + Inches(1.95), col_w, Inches(4.6),
            [{'text': '本单元前四课，我们读了袁隆平、张秉贵、钟扬的劳动故事——', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '"读到了"不等于"说得出"。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '本课两种口语能力互为补充：', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '· 访谈——"问与答"的互动交流', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 4},
             {'text': '· 播报——"说与听"的单向传递', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 10},
             {'text': '依据《普通高中语文课程标准》"实用性阅读与交流"任务群：口语交际须"清楚·连贯·得体"。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5}])
    # 右：早期话筒照
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['vintagemic'], rx, M + Inches(1.25), col_w, Inches(2.7))
    caption(s, '早期广播话筒（Public domain）· 播报传统的实物见证', rx, M + Inches(4.05), col_w)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.5), col_w, Inches(2.0))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.65), col_w - Inches(0.6), Inches(1.8),
            [{'text': '口语三原则（本课总纲）', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '目的性 —— 为什么说（传递信息）', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '条理性 —— 怎么说清楚（有框架）', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '得体性 —— 对谁说（看对象）', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P4 重点：三层次金字塔 + 三原则 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 访谈问题三层次', M, M, FROST)
    cw = (CW - Inches(0.5)) / 2
    # 左：金字塔（由浅入深）
    lx = M
    textbox(s, lx, M + Inches(1.2), cw, Inches(0.5),
            [{'text': '访谈问题三层次（金字塔）', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI}])
    center = lx + cw / 2
    levels = [
        ('价值层', '为什么重要？', '他的种子对未来有何意义？', GOLD, 0.58),
        ('感受层', '怎么想的？', '他想过放弃吗？', XIANG, 0.78),
        ('事实层', '做了什么？', '在西藏每天怎么采种？', FROST, 0.96),
    ]
    y0 = M + Inches(1.8)
    bh = Inches(1.18)
    gap = Inches(0.12)
    for i, (name, q, ex, col, wf) in enumerate(levels):
        w = cw * wf
        x = center - w / 2
        y = y0 + i * (bh + gap)
        bar = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, bh)
        bar.fill.solid(); bar.fill.fore_color.rgb = WHITE; bar.line.color.rgb = col; bar.line.width = Pt(1.8); bar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), w, Inches(0.45),
                [{'text': name, 'size': 17, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x, y + Inches(0.55), w, Inches(0.38),
                [{'text': q, 'size': 14, 'color': INK, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.15), y + Inches(0.9), w - Inches(0.3), Inches(0.3),
                [{'text': '例：' + ex, 'size': 11.5, 'color': MUTED, 'font': KAI, 'align': PP_ALIGN.CENTER}])
    textbox(s, lx, y0 + 3 * (bh + gap) + Inches(0.05), cw, Inches(0.4),
            [{'text': '▲ 由浅入深·由事及理：先问"做了什么"，再追问"为何重要"', 'size': 12.5, 'color': MUTED, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    # 右：口语三原则卡片
    rx = M + cw + Inches(0.5)
    textbox(s, rx, M + Inches(1.2), cw, Inches(0.5),
            [{'text': '口语三原则', 'size': 18, 'color': XIANG, 'bold': True, 'font': KAI}])
    prins = [
        ('目的性', '先想"为什么开口"——传递信息，不是随便闲聊。', FROST),
        ('条理性', '按框架说：访谈有层次，播报有结构，不东拉西扯。', XIANG),
        ('得体性', '看对象调整：对同学、对长辈、对镜头，语气不一样。', GOLD),
    ]
    py = M + Inches(1.8)
    for i, (t, b, col) in enumerate(prins):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, py, cw, Inches(1.5))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = col; card.line.width = Pt(1.4); card.shadow.inherit = False
        textbox(s, rx + Inches(0.25), py + Inches(0.18), Inches(1.6), Inches(0.5),
                [{'text': t, 'size': 17, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, rx + Inches(1.9), py + Inches(0.2), cw - Inches(2.1), Inches(1.1),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}])
        py += Inches(1.62)
    page_num(s)

# ---------- P5 难点：三处易卡住的地方 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三个易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('问题缺层次', '只会问"你觉得怎么样"这种空问题。→ 用三层次框架填空：事实→感受→价值，每个问题都要"具体可答"。', FROST),
        ('找不到"新闻语态"', '要么太随意（像聊天），要么太夸张（像朗诵）。→ 中间态：客观·简洁·有节奏，看主播示范对比。', XIANG),
        ('当众开口紧张', '不敢说、低头念稿、忘词。→ 4人小组分工（记者/受访者/记录员/观察员），降低个体压力。', GOLD),
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

# ---------- P6 探究：角色扮演法 + 示范模仿法 + 张颂语态 ----------
def s_explore(s):
    bg(s, PAPER)
    kicker(s, '探究 · 招牌招式', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': '角色扮演法 + 示范模仿法', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.5)) / 2
    lx = M
    # 左：两招式卡
    m1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.55), cw, Inches(2.25))
    m1.fill.solid(); m1.fill.fore_color.rgb = WHITE; m1.line.color.rgb = FROST; m1.line.width = Pt(1.8); m1.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.72), cw - Inches(0.6), Inches(0.5),
            [{'text': '① 角色扮演法（4人小组）', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.25), cw - Inches(0.6), Inches(1.5),
            [{'text': '记者 / 受访者（扮演劳动者同事）/ 记录员 / 观察员，用设计好的问题做 3 分钟模拟访谈。', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '受访者须"基于课文回答"，不确定的就说"这点我不确定"——守住真实性。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    m2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(4.0), cw, Inches(2.25))
    m2.fill.solid(); m2.fill.fore_color.rgb = WHITE; m2.line.color.rgb = XIANG; m2.line.width = Pt(1.8); m2.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(4.17), cw - Inches(0.6), Inches(0.5),
            [{'text': '② 示范模仿法（播报语态）', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(4.7), cw - Inches(0.6), Inches(1.5),
            [{'text': '先听央视新闻片段，再跟读示范稿："据本台消息，被誉为杂交水稻之父的袁隆平院士……"', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '同一内容用三种语态说——讲故事 / 朗诵 / 新闻，自己对比差异最直观。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    # 右：早期话筒照 + 张颂语态定义
    rx = M + cw + Inches(0.5)
    place_photo(s, PHOTO['vintagemic'], rx, M + Inches(1.55), cw, Inches(2.1))
    caption(s, '广播话筒 · 播报传统的实物见证（PD）', rx, M + Inches(3.75), cw)
    qbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.15), cw, Inches(2.1))
    qbox.fill.solid(); qbox.fill.fore_color.rgb = INK; qbox.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.3), cw - Inches(0.6), Inches(1.9),
            [{'text': '张颂（播音学奠基人）定义"播报"语言样态：', 'size': 13.5, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 6},
             {'text': '感而不入·讲究分寸 → 客观\n节奏明快·语流晓畅 → 有节奏', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '（字正腔圆·语尾不坠 → 简洁清晰）', 'size': 12, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P7 板书：完整结构 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 访谈与播报', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.0), Inches(0.4),
            [{'text': '维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(3.6), M + Inches(1.28), Inches(8.8), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('口语三原则', '目的性(为何说) · 条理性(说清楚) · 得体性(对谁说)', FROST),
        ('访谈三层次', '事实层(做了什么) → 感受层(怎么想) → 价值层(为何重要)', XIANG),
        ('播报语态', '客观(不评价) · 简洁(一句一事) · 节奏(句间微顿) ≠朗诵 ≠日常', GOLD),
        ('评价量表', '内容(准不准) · 语态(像不像) · 节奏(停不好) · 表达(清不清)', FROST),
        ('访谈三步', '设计问题 → 模拟访谈 → 整理记录', XIANG),
        ('播报三步', '选材 → 组稿 → 播报', GOLD),
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

# ---------- P8 作业：分层 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '① 完善访谈问题：三层次各 2 个，且"具体可答"；② 整理模拟访谈记录 3 条关键信息；③ 修改播报稿（5句内），标停顿"/"，录1分钟音频。', FROST),
        ('提升 · 选做', '采访一位身边的劳动者（家长 / 校工 / 身边爱岗敬业的普通人）：写访谈目的 + 5个三层次问题 + 预设回答 + 播报稿。', XIANG),
        ('拓展 · 衔接', '访谈记录与播报稿，直接作为下节课"学写人物通讯"的素材——口语素材转化为书面写作。', GOLD),
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
                [{'text': body, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)

# ---------- P9 总结：两步法口诀 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '总结 · 两种口语方法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '访谈三步 · 播报三步', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    pillars = [
        ('访谈三步法', '设计问题 → 模拟访谈 → 整理记录。问题要"具体可答"，由事实到价值层层追问。', FROST),
        ('播报三步法', '选材 → 组稿 → 播报。语态要客观·简洁·有节奏，抬头看"观众"像主播。', XIANG),
        ('核心一句', '读到的劳动故事，用口语"说出来"——这就是实用性表达。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(pillars):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.25), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 21, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.95), cw - Inches(0.6), Inches(1.2),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(5.0), CW, Inches(2.1))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, M + Inches(0.3), Inches(5.25), Inches(0.06), GOLD, 30)
    textbox(s, M + Inches(0.55), Inches(5.15), CW - Inches(0.8), Inches(1.9),
            [{'text': '口语交流，贵在"得体"', 'size': 19, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4, 'space_after': 8},
             {'text': '访谈练"会问"——问题有层次，才挖得出真故事。\n播报练"会说"——语态客观简洁，信息才传得准。\n下节课：把口语素材写成人物通讯，口头表达落地为书面写作。', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_difficulties,
           s_explore, s_blackboard, s_homework, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-5.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
