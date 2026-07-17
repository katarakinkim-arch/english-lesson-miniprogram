# -*- coding: utf-8 -*-
"""《哦，香雪》课堂版 PPT — 手工精排（融合高赞课招牌招式）

融合来源：
  · 获奖课例"哦"字切入法（阶梯式品读人物精神变化，最受热捧的招牌钩子）
  · 省一等奖教学设计（诗化小说定位 + 物象象征链 + 香雪vs凤娇对比）
  · 何平旺课堂实录（细节描写品读人物心理 + 对比手法揭示主题）
  · 张伯存学术论文（铅笔盒三层符号系统 + 童话叙事结构 + 城乡二元对立超越）
  · 多课共识："一分钟"深层含义 + 夜归心理变化 + 铁凝不简单褒贬城乡

教材结构（本课专属）：哦字钩子 → 时代列车 → 诗化小说 → 一分钟停靠
→ 香雪凤娇对比 → 铅笔盒象征链 → 火车台儿沟 → 夜归心理
→ 诗化语言 → 提问链 → 板书 → 作业与升华

设计系统沿用杂志风（共享库 _classroom_lib）。
python-pptx 生成可编辑 .pptx。图片：Wikimedia Commons 真实照片。
"""
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PPTX = os.path.join(BASE, 'preview_v7', 'oxiangxue.pptx')

PHOTO_DIR = os.path.join(BASE, 'preview_v7', '_oxiangxue_photos')
PHOTO = {
    'cover':     os.path.join(PHOTO_DIR, 'real_cover.jpg'),
    'author':    os.path.join(PHOTO_DIR, 'real_background.jpg'),
    'pencilbox': os.path.join(PHOTO_DIR, 'real_pencilbox.jpg'),
    'night':     os.path.join(PHOTO_DIR, 'real_night.jpg'),
    'stream':    os.path.join(PHOTO_DIR, 'real_stream.jpg'),
    'train':     os.path.join(PHOTO_DIR, 'real_train.jpg'),
}

prs, BLANK = new_presentation()

# ===================================================================
# SLIDES — 《哦，香雪》课堂学生版 PPT（手工精排）
# ===================================================================
def s_cover():
    s = new_slide(prs, BLANK)
    place_photo(s, PHOTO['cover'], 0, 0, W, H)
    scrim(s, 0, H - Inches(3.8), W, Inches(3.8), INK, 0.62)
    scrim(s, 0, 0, W, Inches(1.2), INK, 0.35)
    kicker(s, '高中语文 · 必修上册 · 第一单元', M, M, GOLD)
    textbox(s, M, H - Inches(3.2), CW, Inches(1.7),
            [{'text': '哦，香雪', 'size': 64, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, H - Inches(1.6), CW, Inches(0.9),
            [{'runs': [
                {'text': '铁凝', 'size': 22, 'color': WHITE, 'bold': True, 'font': HEI},
                {'text': '    1982 年 · 一分钟的停靠，一个时代的回响', 'size': 16, 'color': SOFT, 'font': HEI}]}])
    textbox(s, M, H - Inches(0.62), CW, Inches(0.4),
            [{'text': '贯穿线索：以「物象」为抓手，读大山深处最纯真的青春', 'size': 13, 'color': GOLD, 'bold': True, 'font': HEI}])
    page_num(s, dark=True)

def s_contents():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, 'CONTENTS · 本课导览')
    textbox(s, M, M + Inches(0.7), CW, Inches(0.8),
            [{'text': '九个篇章，读懂一分钟里的整个世界', 'size': 30, 'color': INK, 'bold': True, 'font': HEI}])
    items = [
        ('壹', '导入·哦字钩子', '标题怎么读？两种读音，两种情感'),
        ('贰', '背景·时代列车', '铁凝与1982年改革开放初期的乡村书写'),
        ('叁', '文体·诗化小说', '淡化情节、聚焦心理、语言抒情——不一样的小说'),
        ('肆', '情节·一分钟的停靠', '火车来→姑娘迎→换铅笔盒→夜归三十里'),
        ('伍', '人物·香雪 vs 凤娇', '重精神 vs 重物质——因为她是全村唯一的初中生'),
        ('陆', '物象·铅笔盒', '三层符号系统：文具→知识→尊严→人生梦想'),
        ('柒', '物象·火车台儿沟', '现代文明与传统山村的碰撞与融合'),
        ('捌', '细读·夜归心理', '怕→不怕→犹豫→坚定，景物烘托内心成长'),
        ('玖', '提问与升华', '从小见大：纯真的代价与尊严的价值'),
    ]
    col_w = CW / 3
    for i, (num, t, d) in enumerate(items):
        col = i % 3
        row = i // 3
        x = M + col * col_w
        y = M + Inches(1.7) + row * Inches(1.7)
        textbox(s, x, y, Inches(0.7), Inches(0.7),
                [{'text': num, 'size': 30, 'color': FROST, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.75), y, col_w - Inches(0.9), Inches(0.5),
                [{'text': t, 'size': 16, 'color': INK, 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.75), y + Inches(0.5), col_w - Inches(0.9), Inches(0.9),
                [{'text': d, 'size': 12, 'color': MUTED, 'font': HEI, 'line': 1.4}])
    page_num(s)

def s_intro():
    """招牌钩子：「哦」字切入法（获奖课例核心招式）。"""
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '壹 · 导入——“哦”字钩子')
    textbox(s, M, M + Inches(0.7), CW, Inches(0.7),
            [{'text': '一个语气词，藏着两种情感', 'size': 26, 'color': INK, 'bold': True, 'font': HEI}])
    lc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.65), Inches(5.8), Inches(4.4))
    lc.fill.solid()
    lc.fill.fore_color.rgb = SOFT
    lc.line.color.rgb = FROST
    lc.line.width = Pt(1.5)
    lc.shadow.inherit = False
    textbox(s, M + Inches(0.25), M + Inches(1.82), Inches(5.3), Inches(0.45),
            [{'text': '这个标题该怎么读？', 'size': 16, 'color': FROST, 'bold': True, 'font': HEI}])
    reads = [
        ('ó（惊奇/疑问）', '哦？你居然用四十个鸡蛋换了一个铅笔盒！这是为什么？',
         '→ 读出的是好奇：一个山村女孩，为了什么值得如此冒险？'),
        ('ò（赞叹/醒悟）', '哦，香雪！你终于换回了心爱的铅笔盒，你太棒了。',
         '→ 读出的是赞叹：对纯真执着的敬意，对勇敢成长的肯定'),
    ]
    for i, (pron, quote, note) in enumerate(reads):
        y = M + Inches(2.35) + i * Inches(1.4)
        textbox(s, M + Inches(0.25), y, Inches(1.2), Inches(0.7),
                [{'text': pron, 'size': 22, 'color': GOLD, 'bold': True, 'font': KAI}])
        c = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(1.5), y, Inches(4.0), Inches(0.95))
        c.fill.solid()
        c.fill.fore_color.rgb = WHITE
        c.line.color.rgb = XIANG
        c.line.width = Pt(1)
        c.shadow.inherit = False
        textbox(s, M + Inches(1.6), y + Inches(0.08), Inches(3.8), Inches(0.8),
                [{'text': quote, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
        textbox(s, M + Inches(0.25), y + Inches(1.0), Inches(5.3), Inches(0.38),
                [{'text': note, 'size': 13, 'color': XIANG, 'font': KAI, 'bold': True}])
    rx = M + Inches(7.0)
    textbox(s, rx, M + Inches(1.65), Inches(5.3), Inches(0.5),
            [{'text': '本课读法', 'size': 17, 'color': INK, 'bold': True, 'font': HEI}])
    lock = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(2.2), Inches(5.3), Inches(0.55))
    lock.fill.solid()
    lock.fill.fore_color.rgb = GOLD
    lock.line.fill.background()
    lock.shadow.inherit = False
    textbox(s, rx, M + Inches(2.28), Inches(5.3), Inches(0.4),
            [{'text': 'ò —— 赞叹与醒悟', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    textbox(s, rx, M + Inches(2.9), Inches(5.3), Inches(3.0),
            [{'text': '我们选择 ò（赞叹），因为整篇小说就是一次对香雪的深情注视——从好奇她的执着，到理解她的自尊，到最终被她的纯真所感动。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 10},
             {'text': '读到最后，你会自然地发出一声：哦，香雪！', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5}])
    page_num(s)

def s_background():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '贰 · 背景——时代列车驶入深山')
    textbox(s, M, M + Inches(0.7), CW, Inches(0.7),
            [{'text': '1982 年，改革开放初期的中国乡村正在苏醒', 'size': 24, 'color': INK, 'bold': True, 'font': HEI}])
    place_photo(s, PHOTO['author'], W - M - Inches(2.0), M + Inches(0.55), Inches(2.0), Inches(2.0))
    lc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), Inches(5.8), Inches(4.4))
    lc.fill.solid()
    lc.fill.fore_color.rgb = SOFT
    lc.line.color.rgb = FROST
    lc.line.width = Pt(1.5)
    lc.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.9), Inches(5.0), Inches(0.4),
            [{'text': '作家 · 作品', 'size': 13, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.35), Inches(5.0), Inches(3.6),
            [{'text': '铁凝（1957— ）', 'size': 17, 'color': INK, 'bold': True, 'font': HEI, 'space_after': 8},
             {'text': '当代女作家。河北赵县人，曾任中国作家协会主席。《玫瑰门》《大浴女》《哦，香雪》等代表作。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 10},
             {'text': '《哦，香雪》1982年初刊《青年文学》，获全国优秀短篇小说奖。同名电影获第41届柏林国际电影节最佳儿童片水晶熊大奖。2019年起收入统编必修上册。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 10},
             {'text': '文体：散文化短篇小说。以舒缓节奏、细腻笔触，聚焦一群山村少女的日常与心事。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55}])
    rx = M + Inches(6.1)
    textbox(s, rx, M + Inches(1.7), Inches(6.2), Inches(0.45),
            [{'text': '【写作背景】', 'size': 12, 'color': FROST, 'bold': True, 'font': HEI, 'space_after': 8}])
    textbox(s, rx, M + Inches(2.2), Inches(6.2), Inches(2.0),
            [{'text': '1975—1979 年，铁凝在河北博野农村插队四年，与一群十八九岁的农村女孩结下深厚友谊。她们的善良质朴成为她创作的源泉。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 10},
             {'text': '20世纪70年代末，改革开放之风开始吹向封闭的中国乡村。铁凝敏锐地捕捉到现代文明与乡土社会的初次碰撞——以及这种碰撞在青年人心中激起的波澜。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55}])
    quote_block(s, rx, M + Inches(4.3), Inches(6.2),
                '"我想写出的是，即使在最平凡的生活里，人也可以有高贵的追求。"',
                '铁凝', GOLD)
    page_num(s)

def s_genre():
    """哦香雪特色页：诗化小说定位（区别于百合花的四幕情节）。"""
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '叁 · 文体——这是一部“不一样”的小说')
    textbox(s, M, M + Inches(0.7), CW, Inches(0.7),
            [{'text': '它像一首散文诗——淡化情节、聚焦细节、语言抒情', 'size': 26, 'color': INK, 'bold': True, 'font': HEI}])
    step_card(s, M, M + Inches(1.8), Inches(5.8), Inches(2.4), 'A', '传统小说',
              ['有激烈的矛盾冲突（如《范进中举》）', '起承转合，故事性强', '重情节推进，人物行动驱动'], MUTED)
    step_card(s, M + Inches(6.1), M + Inches(1.8), Inches(5.8), Inches(2.4), 'B', '《哦，香雪》（诗化小说）',
              ['没有坏人作梗，没有大悲大喜', '像散文诗一样舒缓、细腻、抒情', '重内心世界、环境意境、情感氛围'], FROST)
    features = [
        ('淡化情节', '故事简单到一句话就能概括：姑娘们看火车，香雪换铅笔盒，走夜路回家。作者故意“减法”，把笔墨集中在人的内心。'),
        ('聚焦细节心理', '香雪打开铅笔盒的动作（小心地打开、轻轻一拍、又打开……）、夜归时的景物感受——每一个细节都在说话。'),
        ('语言抒情化', '环境描写如诗：“一轮满月升起来了，照亮了寂静的山谷……”；结尾反复呼告：“哦，香雪！香雪！”'),
        ('意象与象征', '火车、铅笔盒、台儿沟、大山——每个物象都承载着超出自身的意义，是解读主题的关键。'),
    ]
    for i, (k, v) in enumerate(features):
        y = M + Inches(4.3) + i * Inches(0.55)
        tag = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, Inches(1.6), Inches(0.45))
        tag.fill.solid()
        tag.fill.fore_color.rgb = FROST if i % 2 == 0 else XIANG
        tag.line.fill.background()
        tag.shadow.inherit = False
        textbox(s, M + Inches(0.12), y + Inches(0.04), Inches(1.4), Inches(0.38),
                [{'text': k, 'size': 14, 'color': WHITE, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(1.8), y, CW - Inches(2.0), Inches(0.45),
                [{'text': v, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.3}])
    page_num(s)

def s_plot():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '肆 · 情节——一分钟的停靠')
    textbox(s, M, M + Inches(0.7), CW, Inches(0.7),
            [{'text': '物理时间短暂，心理意义漫长', 'size': 26, 'color': INK, 'bold': True, 'font': HEI}])
    acts = [
        ('开端', '火车进村', '台儿沟以往宁静被搅乱\n姑娘们梳妆打扮，盛装相迎', FROST),
        ('发展', '一分钟交易', '看乘客、和北京话搭讪\n凤娇聊天、做买卖、换发卡', XIANG),
        ('转折', '渴望铅笔盒', '香雪关注书包和铅笔盒\n公社同学让她意识到差距', GOLD),
        ('高潮', '跳车换盒', '误登火车，用40个鸡蛋\n换回自动铅笔盒', INK),
        ('结局', '深夜归来', '独自走完三十里夜路\n面对大山升起从未有过的骄傲', FROST),
    ]
    cw = (CW - Inches(0.4)) / 5
    for i, (act, title, desc, col) in enumerate(acts):
        x = M + i * (cw + Inches(0.1))
        y = M + Inches(1.65)
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.12))
        bar.fill.solid()
        bar.fill.fore_color.rgb = col
        bar.line.fill.background()
        bar.shadow.inherit = False
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y + Inches(0.12), cw, Inches(3.5))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = SOFT
        card.line.width = Pt(1)
        card.shadow.inherit = False
        textbox(s, x, y + Inches(0.28), cw, Inches(0.4),
                [{'text': act, 'size': 12, 'color': col, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x, y + Inches(0.72), cw, Inches(0.6),
                [{'text': title, 'size': 19, 'color': INK, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.15), y + Inches(1.4), cw - Inches(0.3), Inches(2.0),
                [{'text': desc, 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
        if i < 4:
            ar = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x + cw - Inches(0.04), y + Inches(1.8), Inches(0.25), Inches(0.25))
            ar.fill.solid()
            ar.fill.fore_color.rgb = GOLD
            ar.line.fill.background()
            ar.shadow.inherit = False
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, H - Inches(0.92), CW, Inches(0.62))
    band.fill.solid()
    band.fill.fore_color.rgb = INK
    band.line.fill.background()
    band.shadow.inherit = False
    textbox(s, M, H - Inches(0.83), CW, Inches(0.45),
            [{'text': '一分钟 = 台儿沟与外界连接的全部窗口 ｜ 情节链：火车来 → 一分钟 → 换铅笔盒 → 夜归', 'size': 18, 'color': GOLD, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_characters():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '伍 · 人物——香雪 vs 凤娇')
    textbox(s, M, M + Inches(0.7), CW, Inches(0.5),
            [{'text': '同样面对火车，她们看到的世界不同', 'size': 24, 'color': INK, 'bold': True, 'font': HEI}])
    textbox(s, M, M + Inches(1.2), CW, Inches(0.4),
            [{'text': '关键差异：香雪是台儿沟唯一考上初中的女孩——知识改变了她关注的焦点', 'size': 14, 'color': GOLD, 'bold': True, 'font': HEI}])
    lx = M
    lw = Inches(5.8)
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.8), lw, Inches(4.6))
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.line.color.rgb = FROST
    c1.line.width = Pt(2)
    c1.shadow.inherit = False
    hdr1 = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, lx, M + Inches(1.8), lw, Inches(0.7))
    hdr1.fill.solid()
    hdr1.fill.fore_color.rgb = FROST
    hdr1.line.fill.background()
    hdr1.shadow.inherit = False
    textbox(s, lx + Inches(0.2), M + Inches(1.92), lw, Inches(0.5),
            [{'text': '凤娇 · 追求物质之美', 'size': 18, 'color': WHITE, 'bold': True, 'font': HEI}])
    feng_items = [
        '关注金圈圈的发卡、指甲盖大的手表',
        '和列车员“北京话”聊天、做买卖',
        '大胆直率、活泼开朗、敢爱敢说',
        '代表台儿沟姑娘们对物质生活的向往',
        '——这是真实的、自然的、可理解的',
    ]
    fi = [{'text': '· ' + it, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8} for it in feng_items]
    textbox(s, lx + Inches(0.3), M + Inches(2.6), lw - Inches(2.4), Inches(3.6), fi)
    rx = M + Inches(6.3)
    rw = Inches(5.8)
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.8), rw, Inches(4.6))
    c2.fill.solid()
    c2.fill.fore_color.rgb = WHITE
    c2.line.color.rgb = XIANG
    c2.line.width = Pt(2)
    c2.shadow.inherit = False
    hdr2 = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, rx, M + Inches(1.8), rw, Inches(0.7))
    hdr2.fill.solid()
    hdr2.fill.fore_color.rgb = XIANG
    hdr2.line.fill.background()
    hdr2.shadow.inherit = False
    textbox(s, rx + Inches(0.2), M + Inches(1.92), rw, Inches(0.5),
            [{'text': '香雪 · 追求精神之光', 'size': 18, 'color': WHITE, 'bold': True, 'font': HEI}])
    xiang_items = [
        '注意车厢里的皮书包、自动铅笔盒',
        '打听北京的大学、什么叫配乐诗朗诵',
        '文静腼腆、少言寡语、内心丰富',
        '——她是台儿沟唯一的中学生',
        '代表对知识、文化、尊严的渴望',
        '用40个鸡蛋换铅笔盒，走30里夜路回家',
        '→ 不是傻，是比谁都清醒的追求者',
    ]
    xi = [{'text': '· ' + it, 'size': 14, 'color': INK if not it.startswith('→') else XIANG, 'font': KAI, 'line': 1.5, 'space_after': 8, 'bold': it.startswith('→')} for it in xiang_items]
    textbox(s, rx + Inches(0.3), M + Inches(2.6), rw - Inches(2.4), Inches(3.6), xi)
    page_num(s)

def s_pencilbox():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '陆 · 物象——铅笔盒的三层意义')
    textbox(s, M, M + Inches(0.7), Inches(9.0), Inches(0.7),
            [{'text': '一个小盒子，承载着三种价值', 'size': 26, 'color': INK, 'bold': True, 'font': HEI}])
    place_photo(s, PHOTO['pencilbox'], W - M - Inches(2.4), M + Inches(0.55), Inches(2.4), Inches(1.6))
    layers = [
        ('第一层', '实用文具', '一个能装铅笔、橡皮的盒子', '——但香雪为什么要用40个鸡蛋去换它？', FROST),
        ('第二层', '知识与尊严', '自动铅笔盒 = 现代文明的象征', '木盒 vs 塑料盒 = 台儿沟 vs 外面的世界；当女学生问“你们一天吃几顿饭”，香雪敏感地察觉到差距', XIANG),
        ('第三层', '梦想与平等', '“这是一个宝盒子”——童话中的魔法宝物', '谁用它就能上大学、坐火车到处跑、不再被人盘问；→ 铅笔盒 = 自尊、平等、走出大山的入场券', GOLD),
    ]
    cw = (CW - Inches(1.0)) / 3
    for i, (lvl, nature, desc, deep, col) in enumerate(layers):
        x = M + i * (cw + Inches(0.5))
        y = M + Inches(1.65)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(2)
        card.shadow.inherit = False
        textbox(s, x, y + Inches(0.28), cw, Inches(1.0),
                [{'text': lvl, 'size': 52, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x, y + Inches(1.35), cw, Inches(0.5),
                [{'text': nature, 'size': 18, 'color': INK, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        bl = [{'text': d, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6, 'align': PP_ALIGN.CENTER} for d in [desc, deep]]
        textbox(s, x + Inches(0.25), y + Inches(2.0), cw - Inches(0.5), Inches(2.0), bl)
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, H - Inches(0.92), CW, Inches(0.62))
    band.fill.solid()
    band.fill.fore_color.rgb = INK
    band.line.fill.background()
    band.shadow.inherit = False
    textbox(s, M, H - Inches(0.83), CW, Inches(0.45),
            [{'text': '铅笔盒 = 知识 · 尊严 · 平等 ｜ 一个山村少女的精神突围', 'size': 18, 'color': GOLD, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_symbolism():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '柒 · 物象——火车、台儿沟与大山')
    place_photo(s, PHOTO['train'], W - M - Inches(2.8), M + Inches(0.55), Inches(2.8), Inches(1.8))
    symbols = [
        ('火车', '现代文明 / 希望 / 改变', '每天只停一分钟，却带来了外面世界的所有新奇事物——发卡、手表、书包、铅笔盒。它是连接台儿沟与外界的纽带，象征着现代文明对传统山村的冲击。', FROST),
        ('台儿沟', '传统 / 纯真 / 封闭', '“一心一意掩藏在大山那深深的皱褶里”。贫穷、落后、与世隔绝，却保持着人性的纯朴善良。姑娘们天真无邪、真诚率直。', XIANG),
        ('大山', '封闭局限 / 温厚庇护', '既是阻隔台儿沟走向世界的屏障，也是赋予山民纯洁品质的摇篮。“面对严峻而又温厚的大山，她心中升起一种从未有过的骄傲。”', INK),
    ]
    for i, (icon, title, sym_mean, col) in enumerate(symbols):
        y = M + Inches(1.7) + i * Inches(1.5)
        ic = s.shapes.add_shape(MSO_SHAPE.OVAL, M, y, Inches(0.8), Inches(0.8))
        ic.fill.solid()
        ic.fill.fore_color.rgb = col
        ic.line.fill.background()
        ic.shadow.inherit = False
        textbox(s, M, y + Inches(0.2), Inches(0.8), Inches(0.45),
                [{'text': icon[0], 'size': 22, 'color': WHITE, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, M + Inches(1.0), y, Inches(2.9), Inches(0.5),
                [{'text': title, 'size': 16, 'color': INK, 'bold': True, 'font': KAI}])
        textbox(s, M + Inches(1.0), y + Inches(0.5), CW - Inches(1.2), Inches(0.9),
                [{'text': sym_mean, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.45}])
    band = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, H - Inches(0.72), CW, Inches(0.55))
    band.fill.solid()
    band.fill.fore_color.rgb = SOFT
    band.line.color.rgb = GOLD
    band.line.width = Pt(1.5)
    band.shadow.inherit = False
    textbox(s, M, H - Inches(0.64), CW, Inches(0.42),
            [{'text': '铁凝不简单褒贬城乡：台儿沟既有诗意也有苦涩，火车既带来希望也带来失落', 'size': 16, 'color': INK, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_nightwalk():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '捌 · 细读——夜归的心理成长')
    textbox(s, M, M + Inches(0.7), Inches(9.0), Inches(0.7),
            [{'text': '怕 → 不怕 → 犹豫 → 坚定，三十里山路也是三十里心路', 'size': 24, 'color': INK, 'bold': True, 'font': HEI}])
    place_photo(s, PHOTO['night'], W - M - Inches(3.0), M + Inches(0.55), Inches(3.0), Inches(2.2))
    stages = [
        ('怕', '刚下火车的西山口，四周漆黑陌生', '“她忽然觉得心里害怕” —— 第一次离开熟悉的环境', FROST),
        ('不怕', '想起铅笔盒，勇气涌上来', '“她定定神，打开了那个宝盒子” —— 梦想给了她力量', XIANG),
        ('犹豫', '想到台儿沟的贫穷，脚步慢下来', '“台儿沟再穷，她也从没白拿过别人的东西” —— 自尊与诚实', INK),
        ('坚定', '面对严峻而又温厚的大山', '“心中升起一种从未有过的骄傲” —— 接纳自己、接纳家乡、走向成熟', GOLD),
    ]
    cw = (CW - Inches(1.0)) / 4
    for i, (stage, mood, desc, col) in enumerate(stages):
        x = M + i * (cw + Inches(0.33))
        y = M + Inches(2.9)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.9))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(2)
        card.shadow.inherit = False
        textbox(s, x, y + Inches(0.22), cw, Inches(0.9),
                [{'text': stage, 'size': 44, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x, y + Inches(1.15), cw, Inches(0.45),
                [{'text': mood, 'size': 14, 'color': MUTED, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.7), cw - Inches(0.4), Inches(1.1),
                [{'text': desc, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.4, 'align': PP_ALIGN.CENTER}])
    qb = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(5.85), CW, Inches(0.9))
    qb.fill.solid()
    qb.fill.fore_color.rgb = SOFT
    qb.line.color.rgb = GOLD
    qb.line.width = Pt(1.5)
    qb.shadow.inherit = False
    textbox(s, M + Inches(0.25), M + Inches(5.92), CW - Inches(0.5), Inches(0.78),
            [{'text': '【景物烘托】', 'size': 12, 'color': GOLD, 'bold': True, 'font': HEI, 'space_after': 4},
             {'text': '“一轮满月升起来了，照亮了寂静的山谷、灰白的小路……还有漫山遍野那树的队伍。” —— 自然风景不是背景，而是香雪内心的投射：清澈、纯净、充满希望。', 'size': 12, 'color': INK, 'font': KAI, 'line': 1.35}])
    page_num(s)

def s_language():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '玖 · 语言——诗化的魅力')
    textbox(s, M, M + Inches(0.7), Inches(9.0), Inches(0.7),
            [{'text': '每一句话都像在吟咏', 'size': 26, 'color': INK, 'bold': True, 'font': HEI}])
    place_photo(s, PHOTO['stream'], W - M - Inches(3.0), M + Inches(0.55), Inches(3.0), Inches(1.5))
    examples = [
        ('环境描写', '“一轮满月升起来了，照亮了寂静的山谷、灰白的小路，照亮了秋日的败草、粗糙的树干，还有一丛丛荆棘、怪石，还有漫山遍野那树的队伍……”', '舒缓的节奏、密集的意象——为香雪夜行营造诗意背景，暗示少女内心的清澈。', FROST),
        ('动作细节', '“她小心地把它打开，又学着同桌的样子轻轻一拍盒盖，‘哒’的一声，它便合得严严实实。她又打开盒盖，觉得应该立刻装点东西进去……”', '一连串细微动作——把香雪对铅笔盒的珍视刻画入微，语言本身就是情感的放大镜。', XIANG),
        ('结尾呼告', '“哦，香雪！香雪！”', '反复呼告，像诗人对纯真心灵的赞叹。余韵悠长，让读者也被这份纯真打动——这就是诗化语言的感染力。', GOLD),
    ]
    for i, (kind, quote, analysis, col) in enumerate(examples):
        y = M + Inches(2.2) + i * Inches(1.5)
        kind_tag = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, Inches(1.5), Inches(0.5))
        kind_tag.fill.solid()
        kind_tag.fill.fore_color.rgb = col
        kind_tag.line.fill.background()
        kind_tag.shadow.inherit = False
        textbox(s, M + Inches(0.12), y + Inches(0.08), Inches(1.3), Inches(0.36),
                [{'text': kind, 'size': 14, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        qc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + Inches(1.65), y, CW - Inches(2.0), Inches(1.4))
        qc.fill.solid()
        qc.fill.fore_color.rgb = WHITE
        qc.line.color.rgb = SOFT
        qc.line.width = Pt(1)
        qc.shadow.inherit = False
        textbox(s, M + Inches(0.8), y + Inches(0.1), CW - Inches(2.7), Inches(0.65),
                [{'text': quote, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.4}])
        textbox(s, M + Inches(0.8), y + Inches(0.78), CW - Inches(2.7), Inches(0.55),
                [{'text': analysis, 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    page_num(s)

def s_questions():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '拾 · 提问链——从小见大')
    textbox(s, M, M + Inches(0.7), CW, Inches(0.5),
            [{'text': '好课，是把思考权交给读者自己', 'size': 24, 'color': INK, 'bold': True, 'font': HEI}])
    qs = [
        ('Q1', '用 40 个鸡蛋换一个铅笔盒，值吗？', ['表面看：一个塑料铅笔盒远不值 40 个鸡蛋', '但对香雪来说：铅笔盒 = 知识 = 尊严 = 走出大山的希望', '值不值得，取决于你用什么尺度衡量'], FROST),
        ('Q2', '铅笔盒真的只是一个文具吗？', ['它是实用工具（第一层）', '它是现代文明的象征，代表知识和文化（第二层）', '它是香雪维护自尊、争取平等的武器（第三层）'], XIANG),
        ('Q3', '香雪的“纯真”在今天还珍贵吗？', ['80年代：纯真是对抗物质诱惑的精神力量', '今天：在信息过载的时代，保持对知识的纯粹向往依然难得', '纯真不是幼稚，是一种清醒的价值选择'], GOLD),
    ]
    cw = (CW - Inches(1.0)) / 3
    for i, (q, title, ans, col) in enumerate(qs):
        x = M + i * (cw + Inches(0.5))
        y = M + Inches(1.3)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(2)
        card.shadow.inherit = False
        badge = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.fill.background()
        badge.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.34), Inches(0.6), Inches(0.45),
                [{'text': q, 'size': 14, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.6),
                [{'text': title, 'size': 15, 'color': INK, 'bold': True, 'font': HEI, 'line': 1.3}])
        al = [{'text': '· ' + a, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 8} for a in ans]
        textbox(s, x + Inches(0.3), y + Inches(0.95), cw - Inches(0.6), Inches(3.4), al)
    page_num(s)

def s_blackboard():
    s = new_slide(prs, BLANK)
    bg(s, INK)
    kicker(s, '板书 · 结构', color=GOLD)
    textbox(s, M, M + Inches(0.7), CW, Inches(0.7),
            [{'text': '哦，香雪 · 铁凝', 'size': 28, 'color': WHITE, 'bold': True, 'font': KAI}])
    board = (
        '┌── 哦，香雪 ＝ 一分钟里的整个世界 ──┐\n'
        '│                                      │\n'
        '│ 【文体】 诗化小说（散文化）           │\n'
        '│   淡化情节 · 聚焦心理 · 语言抒情      │\n'
        '│                                      │\n'
        '│ 【情节链】 火车来 → 一分钟 → 换笔   │\n'
        '│   盒 → 夜归 30 里                   │\n'
        '│                                      │\n'
        '│ 【物象象征】                          │\n'
        '│   火车 = 现代文明 / 希望               │\n'
        '│   铅笔盒 = 知识 · 尊严 · 梦想         │\n'
        '│   台儿沟 = 纯真 · 封闭               │\n'
        '│   大山 = 局限 · 庇护                 │\n'
        '│                                      │\n'
        '│ 【人物对比】                          │\n'
        '│   凤娇：重物质（发卡/手表/北京话）      │\n'
        '│   香雪：重精神（书包/铅笔盒/大学）      │\n'
        '└──────────────────────────────────────┘'
    )
    tb = s.shapes.add_textbox(M + Inches(0.5), M + Inches(1.6), Inches(7.5), Inches(5.2))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, line in enumerate(board.split('\n')):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        r = para.add_run()
        r.text = line
        r.font.size = Pt(13)
        r.font.name = 'Consolas'
        r.font.color.rgb = SOFT
        set_ea(r, 'Consolas')
    rx = M + Inches(8.5)
    textbox(s, rx, M + Inches(1.9), Inches(3.8), Inches(4.7),
            [{'text': '即使在最平凡的', 'size': 24, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '生活里，', 'size': 24, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '人也可以有', 'size': 24, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '高贵的追求', 'size': 28, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 10},
             {'text': '—— 铁凝', 'size': 14, 'color': SOFT, 'font': HEI, 'space_after': 12},
             {'text': '一分钟', 'size': 24, 'color': XIANG, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '的停靠', 'size': 24, 'color': XIANG, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '一个时代的', 'size': 24, 'color': XIANG, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '回响', 'size': 24, 'color': XIANG, 'bold': True, 'font': KAI}])
    page_num(s, dark=True)

def s_homework():
    s = new_slide(prs, BLANK)
    bg(s)
    kicker(s, '巩固 · 作业与升华')
    textbox(s, M, M + Inches(0.7), Inches(10.5), Inches(0.7),
            [{'text': '从阅读走向写作，从文本走向自我', 'size': 26, 'color': INK, 'bold': True, 'font': HEI}])
    cols = [
        ('基础作业', FROST, ['以“我眼中的香雪”为题，写300字短文', '要求：至少引用2处原文细节，体现你对人物形象的理解']),
        ('提高作业', XIANG, ['对比《百合花》中的小通讯员与《哦，香雪》中的香雪', '分析两位“青春形象”的异同，写200字赏析短评']),
        ('参考示例', GOLD, ['香雪：腼腆(少言)→纯真(唯一初中生)→执着(40蛋换盒)→勇敢(夜行30里)', '"有人情味的英雄"(百合花) vs "高贵追求的少女"(哦香雪) = 不同体裁，同样的青春温度']),
    ]
    cw = (CW - Inches(1.0)) / 3
    for i, (title, col, items) in enumerate(cols):
        x = M + i * (cw + Inches(0.5))
        y = M + Inches(1.5)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.5))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(2)
        card.shadow.inherit = False
        hdr = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.65))
        hdr.fill.solid()
        hdr.fill.fore_color.rgb = col
        hdr.line.fill.background()
        hdr.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.45),
                [{'text': title, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        il = [{'text': '· ' + it, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 10} for it in items]
        textbox(s, x + Inches(0.3), y + Inches(0.8), cw - Inches(0.6), Inches(2.5), il)
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, H - Inches(1.0), CW, Inches(0.72))
    band.fill.solid()
    band.fill.fore_color.rgb = INK
    band.line.fill.background()
    band.shadow.inherit = False
    textbox(s, M, H - Inches(0.88), CW, Inches(0.55),
            [{'text': '纯真之可贵，不在它的脆弱，而在于它在任何环境下都不愿放弃对美好的向往。｜ 这，就是香雪给我们的答案。', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ===================================================================
# BUILD
# ===================================================================
s_cover()
s_contents()
s_intro()
s_background()
s_genre()
s_plot()
s_characters()
s_pencilbox()
s_symbolism()
s_nightwalk()
s_language()
s_questions()
s_blackboard()
s_homework()

prs.save(OUT_PPTX)
print(f'OK 《哦，香雪》课堂版已生成：{OUT_PPTX}')
print(f'  共 {len(prs.slides)} 页')
