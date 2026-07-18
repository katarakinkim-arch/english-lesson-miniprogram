# -*- coding: utf-8 -*-
# 《沁园春·长沙 精读（下）——忆青春与「谁主沉浮」之答》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条 WebSearch 核实，权威一手 / 学术来源）：
#   【来源 A · 学术权威解读】人民网/中国共产党新闻网《万类霜天竞自由——〈沁园春·长沙〉解析》
#     （theory.people.com.cn，2024-07-29；作者系中国井冈山干部学院教授、副院长，中国毛泽东诗词研究会副会长）：
#     下阕"以'忆'字为统领，以情为线，带情叙事"；"一个'恰'字打开记忆的闸口"，'同学少年'是'百侣'
#     的年龄特征、'风华正茂''书生意气'是素质特征；"粪土当年万户侯"典出《离骚》"苏粪壤以充帏兮"；
#     并引 1964 年毛泽东自解"问苍茫大地，谁主沉浮"指"北伐以前，军阀统治，中国命运究竟由哪一个阶级做主"。
#   【来源 B · 作者亲笔批注（一手史料）】毛泽东 1958 年 12 月 21 日于文物出版社大字本《毛主席诗词
#     十九首》书眉批注（人民网党史频道、中国作家网等转引）："击水：游泳。那时初学，盛夏水涨，几死者数，
#     一群人终于坚持，直到隆冬，犹在江中。当时有一篇诗，都忘记了，只记得两句：自信人生二百年，
#     会当水击三千里。"——证实"中流击水"是对湘江游泳经历的实写，兼喻"搏击时代大潮"。
# 真实照片：本词为毛泽东 1925 年橘子洲怀古之作，现有可复用照片均属第二单元劳动主题（西藏高原 /
#   王府井 / 张秉贵 / 麦收 / 稻田等），与词题无关联。按规范 §2.3「有真照才用真照，无则学科色块兜底
#   并明确标注，绝不糊弄」，本稿以学科色块呈现，不强行套用无关图像。
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
            [{'text': '必修上 第一单元 · 青春的价值 · 第二课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.0), Inches(8.2), Inches(1.6),
            [{'text': '沁园春·长沙', 'size': 56, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.15), Inches(8.6), Inches(1.0),
            [{'text': '精读（下）——忆青春与「谁主沉浮」之答', 'size': 27, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.55), Inches(8.0), Inches(1.0),
            [{'text': '上阕问沉浮，下阕作答——看少年词人的群像与担当。', 'size': 17, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.35), Inches(8.0), Inches(1.0),
            [{'text': '一条读词路径：抓领字 → 串意象 → 看结构 → 答沉浮。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.4}])
    # 右侧词摘面板（真实下阕诗句，中性装饰）
    px = Inches(9.1); pw = Inches(3.6)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, Inches(1.6), pw, Inches(4.9))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    rule(s, px + Inches(0.3), Inches(2.0), Inches(0.06), GOLD, 26)
    textbox(s, px + Inches(0.55), Inches(2.05), pw - Inches(0.8), Inches(0.5),
            [{'text': '词的下阕', 'size': 15, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, px + Inches(0.55), Inches(2.65), pw - Inches(0.85), Inches(3.6),
            [{'text': '恰同学少年，\n风华正茂；\n书生意气，\n挥斥方遒。\n\n到中流击水，\n浪遏飞舟？', 'size': 18, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 12},
             {'text': '—— 《沁园春·长沙》下阕（节选）', 'size': 11.5, 'color': SOFT, 'font': HEI}])
    page_num(s)

# ---------- P2 学习目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '准确背诵下阕，解释「粪土」「挥斥方遒」「中流击水」的含义与用法。', FROST),
        ('文化意识', '读懂「同学少年」群像里的革命青年精神，联系当代青年的使命。', XIANG),
        ('思维品质', '发现上下阕「问—答」的结构呼应，整体把握词的章法。', GOLD),
        ('学习能力', '用「对照阅读」法，把上阕「看景」与下阕「忆人」并排比较。', MUTED),
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
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '下阕写于 1925 · 橘子洲头', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    # 左：写作坐标（INK 面板）
    lx = M; lw = Inches(5.5)
    lbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.5), lw, Inches(4.1))
    lbox.fill.solid(); lbox.fill.fore_color.rgb = INK; lbox.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.7), lw - Inches(0.6), Inches(0.5),
            [{'text': '写作坐标', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.25), lw - Inches(0.6), Inches(3.2),
            [{'text': '1925 年秋，毛泽东离开韶山赴广州主办农民运动讲习所，途经长沙，重游橘子洲头。', 'size': 12.5, 'color': SOFT, 'font': KAI, 'line': 1.45, 'space_after': 8},
             {'text': '面对湘江秋景与蓬勃的革命形势，他写下全词。上阕"看"秋景，下阕"忆"青春，以"问苍茫大地，谁主沉浮"为枢纽衔接。', 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 8},
             {'text': '下阕是上阕一问的回答：用"同学少年"的群像，给出"谁主沉浮"的答案。', 'size': 12.5, 'color': GOLD, 'font': KAI, 'line': 1.45}])
    # 右：两条权威来源（白卡）
    rx = lx + lw + Inches(0.4); rw = Inches(5.83)
    def src_box(y, h, head, body, src, col):
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, y, rw, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, rx + Inches(0.3), y + Inches(0.16), rw - Inches(0.6), Inches(0.45),
                [{'text': head, 'size': 14.5, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, rx + Inches(0.3), y + Inches(0.62), rw - Inches(0.6), h - Inches(1.0),
                [{'text': body, 'size': 12, 'color': INK, 'font': KAI, 'line': 1.5}])
        textbox(s, rx + Inches(0.3), y + h - Inches(0.4), rw - Inches(0.6), Inches(0.35),
                [{'text': '来源：' + src, 'size': 10, 'color': MUTED, 'font': HEI}])
    src_box(M + Inches(1.5), Inches(2.0),
            '来源 A · 学术权威解读',
            "下阕“以'忆'字为统领，以情为线”；“一个'恰'字打开记忆的闸口”；“粪土当年万户侯”典出《离骚》“苏粪壤以充帏兮”。并引 1964 年毛泽东自解“谁主沉浮”指“北伐前军阀统治，中国命运由哪个阶级做主”。",
            '人民网《万类霜天竞自由——〈沁园春·长沙〉解析》（2024）', FROST)
    src_box(M + Inches(3.65), Inches(2.0),
            '来源 B · 作者亲笔批注（一手）',
            "“击水：游泳。那时初学，盛夏水涨，几死者数……自信人生二百年，会当水击三千里。”——证实“中流击水”写湘江游泳经历，兼喻“搏击时代大潮”。",
            '毛泽东 1958 年书眉批注；人民网党史频道、中国作家网转引', XIANG)
    textbox(s, M, Inches(6.4), Inches(11.9), Inches(0.45),
            [{'text': '（本词为橘子洲怀古之作，现有可复用照片均属第二单元劳动主题，与词题无关联；按规范 §2.3 以学科色块呈现，本课件未使用无关配图。）', 'size': 10.5, 'color': MUTED, 'font': HEI, 'line': 1.3}])
    page_num(s)

# ---------- P4 重点 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三个落点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '结构 · 词句 · 呼应', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('① 下阕结构', '「忆」领起 →「恰」字群像描写 →「到」字设问作答，一线贯通。', FROST),
        ('② 关键词句', '粪土（名词作动词，把……看作粪土）；挥斥方遒（奔放·正·强劲）。', XIANG),
        ('③ 上下阕呼应', '上阕"问苍茫大地，谁主沉浮" → 下阕"到中流击水，浪遏飞舟"即作答。', GOLD),
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
    kicker(s, '方法 · 四招读词', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '把方法握在手里', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('诵读体会', '听范读、练读四字句群（恰—同学少年……），"恰"后稍顿，读出气势与层次。', FROST),
        ('对照阅读', '上阕"看景" vs 下阕"忆人"，"问" vs "答"，双栏列表并排比较。', XIANG),
        ('比较迁移', '联系《沁园春·雪》"数风流人物，还看今朝"，体会同一词牌的"答"法。', GOLD),
        ('情境补白', '了解毛泽东在一师求学（冷水浴、游湘江），读懂"中流击水"的来历。', MUTED),
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
        ('「粪土」的词类活用', '容易当"粪便"讲。→ 名词作意动"以……为粪土"，用"异之""美我"等例句固化。', FROST),
        ('「浪遏飞舟」的象征义', '容易停在字面"浪大挡舟"。→ 推导为"青年搏击风浪、主宰命运"的豪情。', XIANG),
        ('四字句的朗读节奏', '容易读成 2-2 停顿。→ 示范"恰│同学少年│风华正茂"，语速渐快、力度渐强。', GOLD),
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
    kicker(s, '板书精华 · 下阕', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.4), Inches(0.4),
            [{'text': '板块', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(4.0), M + Inches(1.28), Inches(8.4), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('下阕结构', '忆 → 恰 → 到（领字 / 群像 / 设问作答）', FROST),
        ('同学少年群像', '风华正茂|才华横溢　书生意气|意气风发　指点江山|关心国事', XIANG),
        ('群像（续）', '激扬文字|敢于批判　粪土万户侯|蔑视权贵', GOLD),
        ('意动用法', '粪土→以…为粪土　异→以…为异　美→以…为美', FROST),
        ('上下阕对照', '上：看景→问沉浮　｜　下：忆人→答击水', XIANG),
        ('读词一得', '问—忆—答：上阕设问，下阕作答，结构浑然一体', GOLD),
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
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '基础 · 提升 · 衔接', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '① 背诵并默写全词（含下阕），书写规范、标点正确。② 解释词语在句中的含义与用法：粪土 / 挥斥方遒 / 中流击水。', FROST),
        ('提升 · 选做', '写一段 200 字赏析，主题"从上下阕的问与答看青年毛泽东的担当精神"：①引原文 ②点明结构呼应 ③联系当代青年。', XIANG),
        ('衔接 · 铺垫', '下节课转向现代诗群文（《立在地球边上放号》《红烛》）——从古典词到现代诗；"意象"概念可迁移，形式不同。', GOLD),
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
             {'text': '问—忆—答：上阕设问，下阕作答。下一站——现代诗群文，看意象如何迁移。', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
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
            [{'text': '本单元人文主题"青春的价值"，任务群"文学阅读与写作"。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '本课读下阕——以"忆"领起，用"同学少年"群像回答上阕"谁主沉浮"，结构"问—答"呼应。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 10},
             {'text': '读词路径可迁移：抓领字、串意象、看章法，把上下阕作为一个整体来读。', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5}])
    rx = M + col_w + Inches(0.5)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.7), col_w, Inches(4.6))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.35), M + Inches(1.9), col_w - Inches(0.7), Inches(0.5),
            [{'text': '一句话带走', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.35), M + Inches(2.5), col_w - Inches(0.7), Inches(3.5),
            [{'text': '问"谁主沉浮"，答"中流击水"——革命青年以行动主宰命运。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '下一站：现代诗群文，看意象如何承载情感。', 'size': 14.5, 'color': SOFT, 'font': KAI, 'line': 1.55, 'space_after': 10},
             {'text': '本课件未使用无关配图（学科色块兜底，按 §2.3）。', 'size': 11.5, 'color': MUTED, 'font': HEI, 'line': 1.4}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_methods,
           s_difficulties, s_blackboard, s_homework, s_unit]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u1-2.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
