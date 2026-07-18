# -*- coding: utf-8 -*-
# 《单元活动——"我身边的劳动者"分享会与单元总结》—— 课堂学生版 PPT（手写精排）
# 精细调研来源（已逐条 WebSearch 核实）：
#   教材定位：统编版高中语文必修上册第二单元，属《普通高中语文课程标准》"实用性阅读与交流"
#     任务群，人文主题"劳动光荣"；单元含三篇人物通讯、一篇新闻评论、两首古代诗歌（陈玉《大单元
#     教学设计：劳动的光荣》）。
#   单元性质：第二单元的整体任务即综合实践活动最重要的方式——研究性学习的一个完整课题，引导从
#     生活情境发现问题、通过探究与体验获得真实经验（刘祥民《劳动启智 实践润心》，引教育部课程方案）。
#   招牌招式·自评与元认知：群文活动设计以"自评推荐语掌握情况 / 词云图绘制 / 通讯写作自评"收口，
#     强调学生自我评价与反馈（21cnjy《第二单元"劳动主题"群文活动教学设计》）。
#   单元主线：在劳动叙事中塑造时代品格——把"立德树人"溶解进"文学阅读与写作"的显性任务，学生自己
#     得出关于劳动价值的结论（myzxsx《于耕耘处见精神》单元整体心得）。
#   下单元衔接：第三单元"生命的诗意"回到古诗词——古诗亦"以事写人"，以意象与典故写情，能力可迁移。
# 真实照片（自由授权，复用同单元第四课时已下载，规范§3允许相邻课复用）：
#   harvest.jpg   麦收金田（Wikimedia Commons, CC BY-SA 4.0）——劳动的场景象征
#   ricefield.jpg 中国稻田（Wikimedia Commons, CC BY-SA 4.0）——"劳动创造价值"的具象
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
            [{'text': '必修上 第二单元 · 劳动光荣 · 第八课时', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.0), Inches(12.3), Inches(1.6),
            [{'text': '单元活动', 'size': 52, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(3.05), Inches(12.3), Inches(1.2),
            [{'text': '"我身边的劳动者"分享会与单元总结', 'size': 30, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(4.55), Inches(12), Inches(1.1),
            [{'text': '把读到的、写到的、说到的，汇成一句话。', 'size': 17, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.35), Inches(12), Inches(1.0),
            [{'text': '一条能力线：读通讯 → 说访谈 → 写通讯 → 改通讯 → 用。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.4}])
    page_num(s)

# ---------- P2 目标 ----------
def s_objectives(s):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('语言能力', '用口语讲述一个身边劳动者的故事（2分钟），做到有细节、有精神、不念稿。', FROST),
        ('文化意识', '在分享与倾听中深化对"劳动光荣"的体认，从概念走向情感认同。', XIANG),
        ('思维品质', '填写单元学习反思单，梳理8课时路径，培养自我评价与元认知能力。', GOLD),
        ('学习能力', '把阅读所得、口语所得、写作所得整合为一份单元学习成果。', MUTED),
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

# ---------- P3 背景：从读到说 ----------
def s_background(s):
    bg(s, PAPER)
    kicker(s, '承前启后 · 单元收官', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.25), col_w, Inches(0.6),
            [{'text': '从读到说，今天收口', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
    textbox(s, lx, M + Inches(1.95), col_w, Inches(4.6),
            [{'text': '这个单元走了8节课：读通讯、说访谈、写通讯、改通讯——', 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '今天把它们汇成一场分享与一份总结。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '统编版必修上第二单元属"实用性阅读与交流"任务群，人文主题"劳动光荣"（陈玉《大单元教学设计》）。', 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '单元的八课，本身就是一次完整的综合实践 / 研究性学习课题——从生活里发现问题，在探究中获得真实经验（劳动教育与语文融合研究）。', 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '语文里的劳动教育，靠叙事之美与形象之感打动人，远胜空洞说教。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}])
    rx = M + col_w + Inches(0.5)
    place_photo(s, PHOTO['ricefield'], rx, M + Inches(1.25), col_w, Inches(2.5))
    caption(s, '中国稻田（CC BY-SA 4.0）· "劳动创造价值"的具象', rx, M + Inches(3.85), col_w)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(4.3), col_w, Inches(2.2))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(4.45), col_w - Inches(0.6), Inches(0.5),
            [{'text': '一条能力线', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(5.0), col_w - Inches(0.6), Inches(1.4),
            [{'text': '· 读通讯：抓典型事件与细节', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 3},
             {'text': '· 说访谈：用口语讲，不念稿', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 3},
             {'text': '· 写通讯：以事写人，不说"好"', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- P4 重点：三个活动环节 ----------
def s_keypoints(s):
    bg(s, PAPER)
    kicker(s, '重点 · 三个环节', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '分享会 · 关键词展 · 反思单', 'size': 24, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('① 劳动者故事分享会', '每人上台讲述通讯中的人物，限时2分钟——讲细节、讲精神，不念稿。', ' B班可小组讲述降低压力；A班单独讲述、自选配图。', FROST),
        ('② 劳动精神关键词展', '在便签上写一个关键词 + 一句话，概括本单元最大感悟，贴成"劳动精神墙"。', '关键词尽量不重复：坚守 / 细节 / 14万株 都算好词。', XIANG),
        ('③ 单元学习反思单', '三行：我学会了 / 我还需提升 / 我的疑问（可空）。结构化回顾8课时。', '自我评价与元认知：群文活动设计即以自评收口。', GOLD),
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

# ---------- P5 重点续：讲述技巧卡 ----------
def s_talk(s):
    bg(s, PAPER)
    kicker(s, '重点 · 讲述技巧卡', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '上台前看一眼：四句话', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('不念稿', '用口语说', '抬头看人，像聊天："我写的是门卫王师傅，有件事印象特别深……"，不是背作文。', FROST),
        ('有细节', '讲画面', '讲1–2个具体画面：一抓准、手抖、凌晨四点——让事实自己说话。', XIANG),
        ('有精神', '点一句', '结尾点一句他身上的劳动精神，不喊口号，落在那件事上。', GOLD),
        ('2分钟', '守时间', '严格计时，超时叫停；内容宁愿少而精，不要拖。', MUTED),
    ]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.7)
    for i, (t, tag, body, col) in enumerate(steps):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.6),
                [{'text': t, 'size': 22, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.25), y + Inches(1.05), cw - Inches(0.5), Inches(0.5),
                [{'text': tag, 'size': 15, 'color': MUTED, 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.25), y + Inches(1.75), cw - Inches(0.5), Inches(2.2),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------- P6 难点：三处易卡 ----------
def s_difficulties(s):
    bg(s, PAPER)
    kicker(s, '难点 · 怎么破', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三处容易卡住的地方', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    cards = [
        ('念稿不像讲故事', '习惯读自己写的文字。→ 用技巧卡"抬头看人"，把通讯稿翻成口语讲。', FROST),
        ('反思写不深', '爱写"学到了很多"。→ 用具体提示："我学会的最重要的一个方法是……"', XIANG),
        ('活动节奏拖', '分享环节易超时。→ 严格计时 + 灵活裁剪，必要时分两组并行。', GOLD),
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

# ---------- P7 探究：招牌招式 ----------
def s_explore(s):
    bg(s, PAPER)
    kicker(s, '探究 · 招牌招式', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': '劳动精神墙 + 反思单', 'size': 25, 'color': INK, 'bold': True, 'font': KAI}])
    cw = (CW - Inches(0.5)) / 2
    lx = M
    m1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(1.55), cw, Inches(2.25))
    m1.fill.solid(); m1.fill.fore_color.rgb = WHITE; m1.line.color.rgb = FROST; m1.line.width = Pt(1.8); m1.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(1.72), cw - Inches(0.6), Inches(0.5),
            [{'text': '① 劳动精神墙', 'size': 16, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(2.25), cw - Inches(0.6), Inches(1.5),
            [{'text': '把每个人的"关键词+一句话"写在便签上，贴成一面墙。可视化让感悟互相看见——', 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 6},
             {'text': '"14万株""手抖""凌晨四点"都成了关键词。', 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    m2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, M + Inches(4.0), cw, Inches(2.25))
    m2.fill.solid(); m2.fill.fore_color.rgb = WHITE; m2.line.color.rgb = XIANG; m2.line.width = Pt(1.8); m2.shadow.inherit = False
    textbox(s, lx + Inches(0.3), M + Inches(4.17), cw - Inches(0.6), Inches(0.5),
            [{'text': '② 单元学习反思单', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI}])
    textbox(s, lx + Inches(0.3), M + Inches(4.7), cw - Inches(0.6), Inches(1.5),
            [{'text': '三行：我学会了 / 我还需提升 / 我的疑问。越具体越好——', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6},
             {'text': '"我学会了访谈问题要分三层" 比 "我学会了访谈" 有力得多。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.45}])
    rx = M + cw + Inches(0.5)
    qbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.55), cw, Inches(4.7))
    qbox.fill.solid(); qbox.fill.fore_color.rgb = INK; qbox.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.75), cw - Inches(0.6), Inches(0.5),
            [{'text': '单元主线：以事写人', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
    textbox(s, rx + Inches(0.3), M + Inches(2.35), cw - Inches(0.6), Inches(3.7),
            [{'text': '从袁隆平的稻田，走到你身边的门卫师傅——', 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '读通讯、说访谈、写通讯，一条能力线贯穿。', 'size': 14, 'color': SOFT, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '下单元"生命的诗意"回到古诗词：古诗也"以事写人"，用意象与典故写情——', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 8},
             {'text': '带着"以事写人"去读诗，会发现熟悉的写法。', 'size': 13.5, 'color': GOLD, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- P8 板书 ----------
def s_blackboard(s):
    bg(s, PAPER)
    kicker(s, '板书 · 单元收官', M, M, FROST)
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.28), Inches(3.4), Inches(0.4),
            [{'text': '板块', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(4.0), M + Inches(1.28), Inches(8.4), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('八课时路径', '①袁隆平 ②群文 ③工匠 ④古诗 ⑤访谈 ⑥写通讯 ⑦讲评 ⑧分享会', FROST),
        ('能力线', '读通讯 → 说访谈 → 写通讯 → 改通讯 → 用（可迁移）', XIANG),
        ('劳动精神墙', '坚守 / 细节 / 14万株 / 手抖 / 凌晨四点（便签贴满成墙）', GOLD),
        ('反思三问', '我学会了 __ ｜ 我还需提升 __ ｜ 我的疑问 __', FROST),
        ('单元共识', '劳动的价值，在于创造与坚守；以事写人，好自现', XIANG),
        ('下单元衔接', '第三单元"生命的诗意"：古诗亦以事写人，用意象与典故', GOLD),
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

# ---------- P9 作业 / 总结 ----------
def s_summary(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '提交单元学习反思单（三行完整填写）；誊抄你分享的劳动者故事（通讯终稿）+ 一句分享感受。', FROST),
        ('提升 · 选做', '写一段150字单元学习总结：①点明本单元最重要的一个方法；②举一个具体例子；③说一个想在下单元继续提升的方面。', XIANG),
        ('拓展 · 衔接', '把"以事写人"用到课外阅读与写作中，继续关注身边的劳动者——它不只是这一单元的事。', GOLD),
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
            [{'text': '单元收官口诀', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 4},
             {'text': '读 → 写 → 说 → 用：以事写人，好自现。下一站——第三单元"生命的诗意"。', 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45}])
    page_num(s)

# ---------- BUILD ----------
for fn in [s_cover, s_objectives, s_background, s_keypoints, s_talk,
           s_difficulties, s_explore, s_blackboard, s_summary]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', 'l-cn-bs-u2-8.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
