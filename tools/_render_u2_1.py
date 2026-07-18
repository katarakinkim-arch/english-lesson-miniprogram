# -*- coding: utf-8 -*-
# 《实用文本阅读（上）——喜看稻菽千重浪：袁隆平的科学人生》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条 WebSearch 核实）：
#   ① 中国工程院官网《袁隆平：稻田逐梦，用一粒种子改变世界》（cae.cn/cae/html/main/col2263/
#      2024-06/13/...）：1964年袁隆平在观察了14万多个稻穗后，发现第一株来自洞庭早籼的雄性不育株；
#      1973年10月在苏州全国水稻科研会议上作《利用"野败"选育"三系"的进展》报告，标志中国籼型
#      杂交水稻三系（不育系·保持系·恢复系）配套成功。
#   ② 21世纪教育网·2024高考语文人物通讯学案（zy.21cnjy.com/19161788）：通讯五大特点——严格的
#      真实性、报道的客观性、较强的时间性、描写的形象性、议论色彩较浓；人物通讯阅读方法（理清新闻
#      事实→不虚构前提下叙述描写并重→分析作者立场态度）；消息与通讯在时效性/内容/篇幅/表达上的区别。
# 真实照片（自由授权，复用同单元第四课时已下载，规范§3允许相邻课复用）：
#   harvest.jpg   麦收金田（Wikimedia Commons, CC BY-SA 4.0）——"稻菽千重浪"的具象
#   ricefield.jpg 中国稻田  （Wikimedia Commons, 自由授权）——"劳动创造价值"的具象
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
PHOTO = {
    'harvest': PH('harvest.jpg'),
    'ricefield': PH('ricefield.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['harvest'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    rule(s, M, M + Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '必修上 第二单元 · 劳动光荣 · 第一课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(1.95), Inches(12.3), Inches(1.5),
            [{'text': '实用文本阅读（上）', 'size': 50, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.0), Inches(12.3), Inches(1.2),
            [{'text': '喜看稻菽千重浪 · 袁隆平的科学人生', 'size': 30, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.5), Inches(12), Inches(1.1),
            [{'text': '一篇人物通讯，写一段把饭碗端在自己手里的科学人生。', 'size': 17, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.3), Inches(12), Inches(1.0),
            [{'text': '从1960到1973：14万株稻穗里，长出一株改变世界的不育株。', 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P2 学习目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '本课学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '说出通讯的文体特征（真实·及时·典型），梳理袁隆平科研历程的三个关键节点。', FROST),
        ('文化意识', '理解袁隆平「尊重事实、勇于创新、心系苍生」的科学精神，感受劳动者的时代担当。', XIANG),
        ('思维品质', '通过筛选关键信息、概括事件要点，培养实用文阅读中的信息提取与整合能力。', GOLD),
        ('学习能力', '掌握「圈关键信息→理事件脉络→析人物精神」的实用文阅读三步法，能迁移运用。', MUTED),
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
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.2), col_w, Inches(0.6),
            [{'text': '读什么 · 为什么读', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
    textbox(s, lx, M + Inches(1.9), col_w, Inches(4.7),
            [{'text': '本课属统编版必修上第二单元，学习任务群为「实用性阅读与交流」，人文主题「劳动光荣」。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '课文是沈英甲撰写的人物通讯《喜看稻菽千重浪——记首届国家最高科技奖获得者袁隆平》，记录其发现天然雄性不育株、培育三系杂交水稻的科学历程。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '通讯以「实践出真知」统领，选取质疑权威学说、田间发现不育株、挑战「自花授粉作物无杂种优势」定论等关键事件，兼具新闻真实与文学感染。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '它是实用文阅读的典型范本：既要抓故事情节，也要看文体特征与信息筛选的方法。', 'size': 14, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.4}])
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['ricefield'], rx, M + Inches(1.2), col_w, Inches(2.3))
    caption(s, '图：中国稻田（自由授权，Wikimedia Commons）', rx, M + Inches(3.55), col_w)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.05), col_w, Inches(2.55))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.2), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(4.75), col_w - Inches(0.6), Inches(1.8),
            [{'text': '① 中国工程院官网 cae.cn：1964年观察14万余稻穗发现首株雄性不育株；1973年籼型杂交水稻三系配套成功。', 'size': 12, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 7},
             {'text': '② 21世纪教育网 人物通讯学案：通讯五大特点（真实·客观·时效·形象·议论）；消息与通讯在时效、篇幅、表达上的区别。', 'size': 12, 'color': SOFT, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P4 重点：通讯特征·科研三节点·科学精神 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三个支点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '通讯特征 · 科研三节点 · 科学精神', 'size': 24, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('① 通讯文体特征', '真实性（基于事实不可虚构）·及时性（新闻时效）·典型性（选取代表事件）·文学性（生动描写）。', FROST),
        ('② 科研三节点', '1960 发现天然杂交稻 → 1964 找到雄性不育株 → 1973 三系杂交稻成功（14万株寻1株）。', XIANG),
        ('③ 科学精神内涵', '尊重事实（用实践检验理论）·勇于创新（挑战权威定论）·坚韧不拔（数十年田间坚守）。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.62))
        bar.fill.solid(); bar.fill.fore_color.rgb = col; bar.line.fill.background(); bar.shadow.inherit = False
        textbox(s, x, y + Inches(0.13), cw, Inches(0.4),
                [{'text': t, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.95), cw - Inches(0.6), Inches(3.2),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P5 方法：任务驱动·文体比较·圈点批注·背景支架 ----------
def s_method(s):
    bg(s, PAPER)
    kicker(s, '方法 · 四种读法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '任务驱动 · 文体比较 · 圈点批注 · 背景支架', 'size': 23, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('任务驱动法', '用「袁隆平科研时间线」任务单驱动信息筛选，从长文中精准取点。', FROST),
        ('文体比较法', '对比一则消息与本文通讯，在比较中看清通讯的文体特征。', XIANG),
        ('圈点批注法', '文中圈关键信息、旁批事件要点、末尾概括人物精神。', GOLD),
        ('背景支架法', '补充1960年代背景，理解「让所有人吃饱」的研究初心。', MUTED),
    ]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.7)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.35), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 17, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.25), y + Inches(1.2), cw - Inches(0.5), Inches(2.9),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P6 难点 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三处容易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('通讯与消息的区分', '容易把两者混淆。→ 对比篇幅、描写、人物刻画，明确通讯「长·细·有人物」。', FROST),
        ('「挑战权威」的理解', '习惯接受结论，缺「质疑—验证」思维。→ 结合袁隆平事例，体会质疑的价值。', XIANG),
        ('信息的筛选与整合', '易「全部划线」或「什么也不划」。→ 用任务驱动，给出明确的筛选标准。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.32), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.8),
                [{'text': t, 'size': 16.5, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.3}])
        textbox(s, x + Inches(0.3), y + Inches(1.15), cw - Inches(0.6), Inches(3.0),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- P7 板书精华 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.15), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.23), CW - Inches(0.6), Inches(0.4),
            [{'text': '《喜看稻菽千重浪》· 阅读主干', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    rows = [
        ('通讯 vs 消息', '消息——短·简·快；通讯——长·细·有人物（仍须真实）', FROST),
        ('科研时间线', '1960 发现天然杂交稻 → 1964 找到雄性不育株 → 1973 三系成功（14万株→1株）', XIANG),
        ('科学精神', '尊重事实 → 质疑权威 → 实践检验（← 初心：让所有人吃饱饭）', GOLD),
        ('实用文三步法', '圈关键信息 → 理事件脉络 → 析人物精神（可迁移）', MUTED),
    ]
    y = M + Inches(1.85)
    for i, (dim, a, col) in enumerate(rows):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(1.0))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        rule(s, M + Inches(0.25), y + Inches(0.18), Inches(0.06), col, 0.64)
        textbox(s, M + Inches(0.5), y + Inches(0.16), Inches(3.0), Inches(0.7),
                [{'text': dim, 'size': 15, 'color': col, 'bold': True, 'font': HEI, 'anchor': None}])
        textbox(s, M + Inches(3.7), y + Inches(0.16), CW - Inches(4.0), Inches(0.7),
                [{'text': a, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.35}])
        y += Inches(1.08)
    page_num(s)

# ---------- P8 作业 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '完成袁隆平科研时间线（时间|事件|困难|突破），至少3个节点；解释「通讯」文体特征，至少3点。', FROST),
        ('提升 · 选做', '写150字分析「从14万株到1株看袁隆平的科学精神」：①引原文数据 ②析劳动量 ③点科学精神。', XIANG),
        ('拓展 · 衔接', '用三步法试读下篇通讯《心有一团火》，关注「科学家」与「普通劳动者」的异同（预习）。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (tag, body, col) in enumerate(tiers):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.9))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        bar.fill.solid(); bar.fill.fore_color.rgb = col; bar.line.fill.background(); bar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.9), cw - Inches(0.6), Inches(2.9),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P9 单元小结 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '单元小结', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '第一课时 · 收得住', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    m1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.6), col_w, Inches(2.3))
    m1.fill.solid(); m1.fill.fore_color.rgb = WHITE; m1.line.color.rgb = FROST; m1.line.width = Pt(1.8); m1.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.77), col_w - Inches(0.6), Inches(0.5),
            [{'text': '读通讯的三步法', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.3), col_w - Inches(0.6), Inches(1.5),
            [{'text': '圈关键信息 → 理事件脉络 → 析人物精神。', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '这套读法可迁移到本单元后续的每一篇通讯。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    m2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(4.1), col_w, Inches(2.3))
    m2.fill.solid(); m2.fill.fore_color.rgb = WHITE; m2.line.color.rgb = XIANG; m2.line.width = Pt(1.8); m2.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(4.27), col_w - Inches(0.6), Inches(0.5),
            [{'text': '单元主线', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(4.8), col_w - Inches(0.6), Inches(1.5),
            [{'text': '劳动光荣，写在稻田、柜台与高原。袁隆平以科学劳动让中国人把饭碗端在自己手里。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '下节课：群文比较《心有一团火》《探界者钟扬》。', 'size': 13.5, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.45}])
    rx = M + col_w + Inches(0.5)
    qbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.6), col_w, Inches(4.8))
    qbox.fill.solid(); qbox.fill.fore_color.rgb = INK; qbox.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.8), col_w - Inches(0.6), Inches(0.5),
            [{'text': '一句话记住', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(2.45), col_w - Inches(0.6), Inches(3.8),
            [{'text': '14万株稻穗里，长出1株不育株——', 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '科学精神不在灵感，在田间一棵一棵的查验；', 'size': 14, 'color': SOFT, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '通讯之美不在虚构，在真实事件的生动书写；', 'size': 14, 'color': SOFT, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '劳动光荣不在口号，在把一件事做到底。', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_method,
           s_difficulties, s_blackboard, s_homework, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-1.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
