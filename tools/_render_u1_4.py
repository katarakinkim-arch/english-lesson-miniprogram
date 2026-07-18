# -*- coding: utf-8 -*-
# 《百合花》精读——细节描写与「百合花」意象（必修上 第一单元 第四课时）
# 课堂学生版 PPT（手写精排，9 页）
# 精细调研来源（已逐条 WebSearch 核实）：
#   ① 作者自述（一手来源）：茹志鹃谈《百合花》创作——"战争使人不能有长谈的机会，
#      但是战争却能使人深交……便能够肝胆相照，生死与共"；小说是"在匝匝忧虑之中，
#      缅怀追念时得来的产物"（茹志鹃《漫谈我的创作经历》）。
#   ② 权威评论（茅盾，1958）：在《谈最近的短篇小说》（《人民文学》1958）中以两个
#      "最"评价："结构谨严、没有闲笔"，"富于抒情诗的风味"，风格"清新、俊逸"。
#   小说三要素 / 细节描写 / 限知视角 / "两条线索"（"我"的视角 + 百合花被子物线）等
#   教学招式，综合统编教材教案与名师解读（茹志鹃、茅盾、陈思和等）整理。
# 照片决策：本课为小说，现有 _photos_u2_* 均为第二单元劳动主题照（稻田/麦收/柜台等），
#   与《百合花》意象（百合花被子·小通讯员·新媳妇）无关联；网络不可用、禁止新下载，
#   按规范 §2.3 / §5 以学科色块兜底，并在背景页明确标注「本课件未使用无关配图」。
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    # 左侧墨蓝焦点面板（视觉焦点，非照片，无需遮罩）
    panel = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(5.0), H)
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.line.fill.background(); panel.shadow.inherit = False
    rule(s, Inches(0.6), Inches(1.35), Inches(0.9), GOLD, 3)
    textbox(s, Inches(0.6), Inches(1.55), Inches(4.2), Inches(0.5),
            [{'text': '必修上 · 第一单元', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, Inches(0.55), Inches(2.15), Inches(4.3), Inches(1.6),
            [{'text': '百合花', 'size': 66, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, Inches(0.6), Inches(3.85), Inches(4.2), Inches(0.6),
            [{'text': '精读 · 小说', 'size': 22, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, Inches(0.6), Inches(4.55), Inches(4.2), Inches(2.0),
            [{'text': '茹志鹃 · 1958 年', 'size': 14, 'color': SOFT, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '一篇没有战场硝烟的', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5},
             {'text': '战争小说。', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    # 右侧纸面信息区
    kicker(s, '青春的价值 · 第四课时', Inches(5.4), M, FROST)
    textbox(s, Inches(5.4), Inches(1.9), Inches(7.4), Inches(1.2),
            [{'text': '细节描写与「百合花」意象', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, Inches(5.4), Inches(3.15), Inches(7.4), Inches(2.4),
            [{'text': '一条枣红底、洒满白色百合花的新被子，串起三个人物：文工团的"我"、', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8},
             {'text': '腼腆的小通讯员、刚过门三天的新媳妇。借被子、牺牲、盖被子——', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8},
             {'text': '看细节怎么把"纯洁"与"牺牲"写到一起。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.55}])
    tag = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.4), Inches(5.7), Inches(4.6), Inches(0.9))
    tag.fill.solid(); tag.fill.fore_color.rgb = XIANG; tag.line.fill.background(); tag.shadow.inherit = False
    textbox(s, Inches(5.6), Inches(5.82), Inches(4.3), Inches(0.7),
            [{'text': '读这篇小说，带三把钥匙：细节 · 意象 · 视角', 'size': 13, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ---------- P2 学习目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '梳理情节脉络（借被子→包扎所→牺牲→盖被子），找出3处以上关键细节并说清作用。', FROST),
        ('文化意识', '读懂战争中普通人的人性之美与青春之纯真，感受那个年代的人情温度。', XIANG),
        ('思维品质', '追踪「百合花被子」意象在情节中的变化，培养意象演变的阅读思维。', GOLD),
        ('学习能力', '掌握「细节→人物→主题」的小说细读路径，能迁移到其他小说。', MUTED),
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
                [{'text': b, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ---------- P3 背景与权威调研 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.2), col_w, Inches(0.6),
            [{'text': '一篇小说的来历', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
    textbox(s, lx, M + Inches(1.9), col_w, Inches(4.8),
            [{'text': '《百合花》写于 1958 年，首发于《延河》第3期，是茹志鹃的成名作。', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8},
             {'text': '故事背景设在 1946 年中秋的前线包扎所——不写战斗场面，只写三个人在战前的短暂交集。', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8},
             {'text': '叙事用第一人称限知视角（"我"是文工团女团员），语言清新克制。', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8},
             {'text': '小说三要素，这篇用"细节"而非"场面"取胜。', 'size': 14.5, 'color': MUTED, 'font': KAI, 'line': 1.55}])
    rx = M + col_w + Inches(0.5)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.2), col_w, Inches(4.5))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.38), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威调研 · 真实来源', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(1.95), col_w - Inches(0.6), Inches(0.4),
            [{'text': '① 作者自述（茹志鹃）', 'size': 13.5, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, rx + Inches(0.3), M + Inches(2.35), col_w - Inches(0.6), Inches(1.2),
            [{'text': '"战争使人不能有长谈的机会，但是战争却能使人深交……便能够肝胆相照，生死与共。"《百合花》是在"匝匝忧虑之中，缅怀追念时得来的产物"。', 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    textbox(s, rx + Inches(0.3), M + Inches(3.55), col_w - Inches(0.6), Inches(0.35),
            [{'text': '—— 茹志鹃《漫谈我的创作经历》', 'size': 11, 'color': GOLD, 'font': HEI}])
    textbox(s, rx + Inches(0.3), M + Inches(3.95), col_w - Inches(0.6), Inches(0.4),
            [{'text': '② 权威评论（茅盾，1958）', 'size': 13.5, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, rx + Inches(0.3), M + Inches(4.35), col_w - Inches(0.6), Inches(1.0),
            [{'text': '"结构谨严、没有闲笔"，"富于抒情诗的风味"；风格"清新、俊逸"——茅盾读过的几十个短篇里"最满意、最感动"的一篇。', 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    textbox(s, rx + Inches(0.3), M + Inches(5.35), col_w - Inches(0.6), Inches(0.4),
            [{'text': '—— 茅盾《谈最近的短篇小说》，《人民文学》1958', 'size': 11, 'color': GOLD, 'font': HEI}])
    textbox(s, lx, M + Inches(6.15), CW, Inches(0.4),
            [{'text': '本课件未使用无关配图（网络不可用；按规范 §2.3 以学科色块兜底，未套用无关图像）。', 'size': 11.5, 'color': MUTED, 'font': HEI, 'italic': True}])
    page_num(s)

# ---------- P4 重点 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三个抓手', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '情节 · 意象 · 细节', 'size': 24, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('① 情节脉络', '借被子（初遇）→ 包扎所帮忙（相处）→ 通讯员牺牲（高潮）→ 新媳妇盖被子（结局）。', ' 四幕一条线：从"不愿借"到"主动盖"。', FROST),
        ('② 核心意象', '「百合花被子」——初见（新媳妇不愿借）→ 相处（铺在包扎所）→ 高潮（盖在遗体上）。', ' 意象随情节演变，承载人的情感变化。', XIANG),
        ('③ 关键细节', '枪筒插树枝、衣服破洞、两个馒头——三个反复出现的细节，以小见大塑人物。', ' 找细节、看它出现几次、每次有何不同。', GOLD),
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
                [{'text': note, 'size': 12.5, 'color': col, 'bold': True, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- P5 方法 ----------
def s_methods(s):
    bg(s, PAPER)
    kicker(s, '方法 · 四步读法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '怎么读这篇小说', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('细读法', '聚焦关键段落（借被子 / 牺牲 / 盖被子），逐句品味细节。', FROST),
        ('意象追踪法', '画「百合花被子」的演变线索图，看意象怎么随情节走。', XIANG),
        ('角色分析法', '从言行细节推导人物性格（小通讯员的腼腆 / 新媳妇的转变）。', GOLD),
        ('比较法', '对比「限知视角」与「全知视角」的叙事差异与效果。', MUTED),
    ]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.7)
    for i, (t, body, col) in enumerate(steps):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.3), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.37), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(1.05), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 18, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.3), y + Inches(1.75), cw - Inches(0.6), Inches(2.2),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P6 难点 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三处容易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('「限知视角」的叙事效果', '叙述者"我"只看到一部分、听不到通讯员心里想什么。→ 体会这种"只知所见"带来的真实感与悬念。', FROST),
        ('细节的「反复」手法', '"衣服破洞"出现三次：生活细节（腼腆）→ 关切（要缝）→ 牺牲后（成永恒伤痕）。→ 追踪它的递进。', XIANG),
        ('结尾「盖被子」的情感分量', '从"不愿借"到"主动盖"，是新媳妇心理的转折。→ 读懂这条被子承载的崇敬与痛惜。', GOLD),
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
        textbox(s, x + Inches(1.0), y + Inches(0.26), cw - Inches(1.2), Inches(0.9),
                [{'text': t, 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.3}])
        textbox(s, x + Inches(0.3), y + Inches(1.15), cw - Inches(0.6), Inches(2.9),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P7 要点图谱（原"板书精华"，学生视角改中性名） ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '要点图谱 · 拿来复习', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.4), Inches(0.4),
            [{'text': '板块', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(4.0), M + Inches(1.28), Inches(8.4), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('意象内核', '百合花 ＝ 纯洁 ＋ 牺牲（枣红底上洒满白色百合花）', FROST),
        ('四幕脉络', '借被子 → 帮包扎 → 通讯员牺牲 → 新媳妇盖被子', XIANG),
        ('被子演变', '不愿借（私有）→ 铺在包扎所（共用）→ 献出盖遗体（牺牲）', GOLD),
        ('三个反复', '枪筒树枝 · 衣服破洞 · 两个馒头——以小见大塑人物', FROST),
        ('叙事视角', '限知视角：只知"我"所见 → 真实 ＋ 悬念', XIANG),
        ('细读四步', '追意象 → 读细节 → 析人物 → 推主题（可迁移）', GOLD),
    ]
    y = M + Inches(1.85)
    for i, (dim, a, col) in enumerate(rows):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.58))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
        card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.3), y + Inches(0.1), Inches(3.4), Inches(0.4),
                [{'text': dim, 'size': 14, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(4.0), y + Inches(0.1), Inches(8.4), Inches(0.4),
                [{'text': a, 'size': 13, 'color': INK, 'font': KAI}])
        y += Inches(0.64)
    page_num(s)

# ---------- P8 作业 ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '1. 梳理「百合花被子」在小说中的四次出现，各用一句话概括其状态与含义。\n2. 找出描写小通讯员腼腆的 3 处细节，各用一句话概括。', FROST),
        ('提升 · 选做', '写一段 200 字赏析，分析「衣服破洞」三次出现的递进意义：①引用原文；②分析每次的不同功能；③点明递进关系。', XIANG),
        ('拓展 · 衔接', '预习《哦，香雪》：同样第一人称限知视角，意象从「百合花」变为「铅笔盒」。试试用本课的追踪法，先猜它会怎么变。', GOLD),
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
            [{'text': '细读口诀', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '追意象 → 读细节 → 析人物 → 推主题。下一站——《哦，香雪》，看意象怎么换张脸。', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P9 单元小结 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '单元小结 · 青春的价值', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '从诗歌，走到小说', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    lbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.65), col_w, Inches(4.3))
    lbox.fill.solid(); lbox.fill.fore_color.rgb = WHITE; lbox.line.color.rgb = FROST; lbox.line.width = Pt(1.8); lbox.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.85), col_w - Inches(0.6), Inches(0.5),
            [{'text': '本篇一句话', 'size': 17, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.4), col_w - Inches(0.6), Inches(3.4),
            [{'text': '一条被子、一个腼腆的通讯员、一个新媳妇，', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8},
             {'text': '写出了战争里的人性之美与青春的纯真——', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8},
             {'text': '纯洁与牺牲，被同一朵百合花连在一起。', 'size': 14.5, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.55}])
    rx = M + col_w + Inches(0.5)
    rbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.65), col_w, Inches(4.3))
    rbox.fill.solid(); rbox.fill.fore_color.rgb = INK; rbox.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.85), col_w - Inches(0.6), Inches(0.5),
            [{'text': '一条能力线', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(2.4), col_w - Inches(0.6), Inches(3.4),
            [{'text': '· 读意象：找反复出现的物与画面', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '· 追细节：看它出现几次、如何变化', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '· 析人物：从言行推导性格', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '· 推主题：细节 → 人物 → 主题', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '单元主题：青春的价值，在于主动追求（担当·激情·纯真·觉醒）。', 'size': 13.5, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_methods,
           s_difficulties, s_blackboard, s_homework, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u1-4.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
