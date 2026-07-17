# -*- coding: utf-8 -*-
# 《单元学习活动——「青春的价值」综合活动与成果展示》课堂学生版 PPT 渲染器（手写精排）
# 来源：lessons-cn.js u1-8 教案 + 高赞单元活动设计共识招牌招式
#   · 核心：8课时路径回顾（意象 读→写）、青春诗朗诵会、青春意象展、反思三问
#   · 研究补充：青春意象图谱、小我与大我价值思辨、班级文集发布会、意象意识迁移实用文
#   · 注意：通篇不出现「教师/老师」字样（课堂学生版）
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO = {
    'star':      os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_star.jpg'),
    'citynight': os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_citynight.jpg'),
    'pen':       os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_pen.jpg'),
    'ocean':     os.path.join(BASE, 'preview_v7', '_xiezuo_photos', 'real_ocean.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['star'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.50)
    rule(s, M, M + Inches(0.45), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.65), Inches(10), Inches(0.5),
            [{'text': '必修上 第一单元 · 单元收官', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.3), Inches(12), Inches(1.6),
            [{'text': '青春诗会', 'size': 48, 'color': WHITE, 'bold': True, 'font': KAI},
             {'text': '「青春的价值」综合活动与成果展示', 'size': 22, 'color': SOFT, 'bold': True, 'font': KAI, 'space_before': 8}])
    textbox(s, M, Inches(5.2), Inches(12), Inches(1.2),
            [{'text': '从读诗，到写诗，到为青春赋形。', 'size': 18, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4}])
    page_num(s)


# ---------- P2 导览 ----------
def s_contents(s):
    bg(s, PAPER)
    kicker(s, '活动导览', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(10), Inches(0.8),
            [{'text': '今天做什么', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    items = [
        ('01', '回顾：8 课时的意象之路'),
        ('02', '青春诗朗诵会：建议卡四要素'),
        ('03', '朗诵小贴士：上台不慌'),
        ('04', '青春意象展：一个意象 + 一句话'),
        ('05', '单元学习反思单：三问'),
        ('06', '单元核心意象图谱'),
        ('07', '价值思辨：小我与大我'),
        ('08', '我的青春宣言'),
        ('09', '班级文集与发布会'),
        ('10', '意象意识，迁移到实用文'),
        ('11', '青春的价值 · 为青春赋形'),
        ('12', '分层作业'),
    ]
    paras = []
    for num, t in items:
        paras.append({'size': 15, 'color': INK, 'font': KAI, 'line': 1.25, 'space_after': 5,
                      'runs': [{'text': num + '  ', 'size': 15, 'color': FROST, 'bold': True, 'font': HEI},
                               {'text': t, 'size': 15, 'color': INK, 'font': KAI}]})
    textbox(s, M, M + Inches(1.7), CW, Inches(5.0), paras)
    page_num(s)


# ---------- P3 8课时路径回顾 ----------
def s_path(s):
    bg(s, PAPER)
    kicker(s, '回顾 · 8 课时的路', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '从读到写，一条意象之路', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('①', '长沙（上）', '意象品析'), ('②', '长沙（下）', '结构呼应'),
        ('③', '放号·红烛', '群文比较'), ('④', '百合花', '细节细读'),
        ('⑤', '香雪比较', '略读+单元'), ('⑥', '学写新诗', '从意象到情感'),
        ('⑦', '写作讲评', '修改升格'), ('⑧', '青春诗会', '展示成果'),
    ]
    cw = (CW - Inches(0.3) * 3) / 4
    y1 = M + Inches(1.7); y2 = M + Inches(4.2)
    for i, (num, t, sub) in enumerate(steps):
        x = M + (i % 4) * (cw + Inches(0.3))
        y = y1 if i < 4 else y2
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(1.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = FROST; card.line.width = Pt(1.5); card.shadow.inherit = False
        textbox(s, x + Inches(0.2), y + Inches(0.18), cw - Inches(0.4), Inches(0.5),
                [{'text': num, 'size': 20, 'color': FROST, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.2), y + Inches(0.7), cw - Inches(0.4), Inches(0.5),
                [{'text': t, 'size': 16, 'color': INK, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.2), y + Inches(1.15), cw - Inches(0.4), Inches(0.5),
                [{'text': sub, 'size': 13, 'color': MUTED, 'font': KAI}])
    banner = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(6.0), CW, Inches(0.45))
    banner.fill.solid(); banner.fill.fore_color.rgb = GOLD; banner.line.fill.background(); banner.shadow.inherit = False
    textbox(s, M, M + Inches(6.07), CW, Inches(0.35),
            [{'text': '核心只有一个词——意象：从「读」意象，到「写」意象。', 'size': 16, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
    page_num(s)


# ---------- P4 青春诗朗诵会 + 建议卡 ----------
def s_recital(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['citynight'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    kicker(s, '青春诗朗诵会', M, M, GOLD)
    textbox(s, M, M + Inches(0.8), Inches(11), Inches(0.7),
            [{'text': '上台，朗诵一首诗', 'size': 28, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(11.5), Inches(0.8),
            [{'text': '自创或单元课文，限时 2 分钟。先看清建议卡——', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.5}])
    cards = [
        ('节奏', '快慢搭配，别一个调到底。', FROST),
        ('停顿', '意象之后，微微一顿。', XIANG),
        ('重音', '动词、形容词，稍稍加重。', GOLD),
        ('情感', '不要喊，要真。', MUTED),
    ]
    cw = (CW - Inches(0.3) * 3) / 4
    y = M + Inches(2.7)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.3))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.6))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.2), y + Inches(0.25), cw - Inches(0.4), Inches(0.6),
                [{'text': t, 'size': 19, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.0), cw - Inches(0.4), Inches(1.5),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P5 朗诵小贴士 ----------
def s_tips(s):
    bg(s, PAPER)
    kicker(s, '朗诵小贴士 · 上台不慌', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三个让朗诵更稳的习惯', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tips = [
        ('抬头看人', '朗诵不是背书——眼神与观众交流，气场就立住了。', FROST),
        ('语速慢一半', '比平时说话慢，给意象和停顿留空间。', XIANG),
        ('忘词别重来', '停一下，接着往下；观众不会发现你跳了哪句。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(tips):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.4))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 20, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.1), cw - Inches(0.5), Inches(2.0),
                [{'text': b, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P6 青春意象展 ----------
def s_exhibition(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['pen'], W - M - Inches(4.4), M, Inches(4.4), Inches(4.4))
    caption(s, '便签与笔 · 意象墙', W - M - Inches(4.4), M + Inches(4.5), Inches(4.4))
    kicker(s, '青春意象展', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.8), Inches(0.6),
            [{'text': '一个意象 + 一句话', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(6.9), Inches(1.2),
            [{'text': '便签第一行写一个意象（一个词），第二行写一句话——它概括了你这个单元最大的感悟。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    chips = [
        ('种子', '从读到写，意象让我发芽。'),
        ('破洞', '细节里的情感，越读越深。'),
        ('铅笔盒', '原来不只是物，是渴望。'),
    ]
    y = M + Inches(3.2)
    for t, b in chips:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, Inches(6.9), Inches(1.0))
        card.fill.solid(); card.fill.fore_color.rgb = SOFT; card.line.color.rgb = FROST; card.line.width = Pt(1.3); card.shadow.inherit = False
        textbox(s, M + Inches(0.25), y + Inches(0.12), Inches(1.6), Inches(0.8),
                [{'text': t, 'size': 17, 'color': FROST, 'bold': True, 'font': KAI}])
        textbox(s, M + Inches(1.9), y + Inches(0.12), Inches(4.8), Inches(0.8),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
        y += Inches(1.15)
    page_num(s)


# ---------- P7 反思三问 ----------
def s_reflection(s):
    bg(s, PAPER)
    kicker(s, '单元学习反思单', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三问，越具体越好', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    q = [
        ('我学会了', '最重要的一个方法 / 知识（别说「学到了很多」）。', FROST),
        ('我需提升', '具体一项——朗读节奏？意象选择？', XIANG),
        ('我的疑问', '可以没有；有，就写一个有思考价值的问题。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(q):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.4))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 20, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.1), cw - Inches(0.5), Inches(2.0),
                [{'text': b, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P8 单元核心意象图谱 ----------
def s_imagery_map(s):
    bg(s, PAPER)
    kicker(s, '单元核心意象图谱', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '六个意象，读懂一个单元', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    imgs = [
        ('湘江秋景', '《沁园春》— 豪迈奋进', FROST),
        ('红　烛', '《红烛》— 赤诚奉献', XIANG),
        ('云　雀', '《致云雀》— 自由欢唱', GOLD),
        ('雪　峰', '《峨日朵》— 谦卑坚守', MUTED),
        ('百合花', '《百合花》— 纯真通讯', FROST),
        ('铅笔盒', '《哦香雪》— 渴望与向往', XIANG),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y1 = M + Inches(1.9); y2 = M + Inches(4.2)
    for i, (t, b, col) in enumerate(imgs):
        x = M + (i % 3) * (cw + Inches(0.4))
        y = y1 if i < 3 else y2
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.0))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 19, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.0), cw - Inches(0.5), Inches(0.8),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
    page_num(s)


# ---------- P9 价值思辨：小我与大我 ----------
def s_debate(s):
    bg(s, PAPER)
    kicker(s, '价值思辨 · 小我与大我', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '青春的「小我」与「大我」', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.4)) / 2
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), cw, Inches(4.0))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = FROST; c1.line.width = Pt(1.8); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.95), cw - Inches(0.6), Inches(0.6),
            [{'text': '小我 · 个人体验', 'size': 19, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, M + Inches(0.3), M + Inches(2.8), cw - Inches(0.6), Inches(2.6),
            [{'text': '《峨日朵》里「征服与敬畏并存」的生命体验——', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '青春的价值，也在于真实地活过自己的感受。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(1.7), cw, Inches(4.0))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(1.8); c2.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(1.95), cw - Inches(0.6), Inches(0.6),
            [{'text': '大我 · 时代担当', 'size': 19, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(2.8), cw - Inches(0.6), Inches(2.6),
            [{'text': '《沁园春》「中流击水」的社会使命感——', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '青春的价值，也在「无尽的远方，无数的人们，都与我有关」。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    textbox(s, M, M + Inches(5.85), CW, Inches(0.8),
            [{'text': '结论：不是取舍，而是交融——伟大的青春，是小我与大我深刻相连。', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    page_num(s)


# ---------- P10 我的青春宣言 ----------
def s_declaration(s):
    bg(s, PAPER)
    kicker(s, '我的青春宣言', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '把单元的精神，变成你的表达', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('诗歌仿写', '借托物言志（如《红烛》）或比喻铺陈（如《致云雀》），选自己的意象创作短诗。', FROST),
        ('主题演讲', '以「在____时代，我的青春何为」为题发言，须援引单元文本、观照现实。', XIANG),
        ('班级发布会', '诗歌朗诵 + 演讲 + 青春意象艺术展板，整合所有成果。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.9)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.4))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 18, 'color': col, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(1.1), cw - Inches(0.5), Inches(2.0),
                [{'text': b, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P11 班级文集与发布会 ----------
def s_anthology(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['ocean'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    kicker(s, '班级文集 · 发布会', M, M, GOLD)
    textbox(s, M, M + Inches(0.8), Inches(11), Inches(0.7),
            [{'text': '让零散的习作，长成一本书', 'size': 28, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(2.0), Inches(11.5), Inches(4.0),
            [{'text': '把单元里读与写的成果，汇编成班级第一本青春文集——', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '分专栏、拟栏目名、写序与跋，是真实的语言实践。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '一场「青春的诗与远方」发布会：朗诵、演讲、意象艺术展板。', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P12 迁移：意象意识 → 实用文 ----------
def s_transfer(s):
    bg(s, PAPER)
    kicker(s, '可迁移的能力', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '意象意识，不止于诗', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.6), CW,
                '读 → 写 → 用：意象意识，是可迁移的能力。', '单元核心方法', FROST)
    textbox(s, M, M + Inches(3.8), CW, Inches(2.6),
            [{'text': '下个单元读实用文（新闻、通讯、科普）——你会发现：', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '关键信息的「反复出现」，就是实用文的「意象」。', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '追踪它，你就抓住了作者真正想说的。课外阅读也试着用。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P13 青春的价值 · 为青春赋形 ----------
def s_youth(s):
    bg(s, PAPER)
    kicker(s, '青春的价值 · 为青春赋形', M, M, FROST)
    textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
            [{'text': '把抽象，写成具体的诗', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.6), CW,
                '青春是抽象的，文学用意象使它可感——从湘江秋景到铅笔盒，我们把青春赋了形。',
                '第一单元 · 青春的价值', FROST)
    textbox(s, M, M + Inches(4.3), CW, Inches(2.0),
            [{'text': '这个单元，我们从一首词走到一首自己写的诗。', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '重要的不是考了什么，而是你有了「意象的眼睛」——', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '看世界时，能看见物背后的情感与时代。', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P14 作业（分层） ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '提交单元学习反思单（三问完整）；誊抄你朗诵的诗 + 一句朗诵感受。', FROST),
        ('提升 · 选做', '写 150 字单元总结：点明最重要的方法 + 举一个你用它的例子 + 一项待提升。', XIANG),
        ('拓展 · 实践', '为班级文集「青春的吟唱」投稿；课外阅读一篇青春主题作品，用意象法写短评。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (tag, body, col) in enumerate(tiers):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.55))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.1), cw, Inches(0.4),
                [{'text': tag, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(0.75), cw - Inches(0.5), Inches(1.8),
                [{'text': body, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- BUILD ----------
for fn in [s_cover, s_contents, s_path, s_recital, s_tips, s_exhibition, s_reflection,
           s_imagery_map, s_debate, s_declaration, s_anthology, s_transfer, s_youth, s_homework]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(BASE, 'preview_v7', 'huodong.pptx')
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
