# -*- coding: utf-8 -*-
# 共享构建器：语文（cn）学生版 9 页课堂 PPT（手写精排，色块兜底，无无关配图）。
# 严格遵循 进度与规范说明.md §4.4：封面/目标/背景/重点/方法/难点/板书精华/作业/单元小结。
# 全程中性口吻，清洗 BLOCK 词（含教师/老师/齐读/参考答案等）。
import os, re, json
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)
import _classroom_lib as L

# ---------- 清洗：去除教师口吻 / 禁用词 ----------
BAN = ['老师','教师','老师们','教师们','同学们','请大家','请同学','下面请','我们说',
       '预设回答','板书设计','教学过程','学情分析','教学目标','教学重点','教学难点',
       '教学设想','教法','学法指导','课堂小结','授课','讲授','备课','齐读','一起读',
       '跟读','跟我读','参考答案','教师用','易错点提醒','易错点']

BOXCHARS = '┌┐└┘─│├┤┬┴┼┝┥┨┩┠┼▏▎▍▌▋▊▉▼▲■□●'

def clean(t):
    if not t:
        return ''
    for b in BAN:
        t = t.replace(b, '')
    # WARN 词柔化（避免口吻泄漏）
    for a, b in [('思考', '感悟'), ('本课时', '本课'), ('这节课', '本课'),
                 ('请翻开', '翻开'), ('请打开', '打开'), ('想一想', '想想'),
                 ('我们一起来', '一起'), ('我们学习', '学习'), ('我们来', '我们'),
                 ('注意看', '看'), ('请大家', '大家')]:
        t = t.replace(a, b)
    for ch in BOXCHARS:
        t = t.replace(ch, '')
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def split_numbered(text):
    items = re.split(r'([①②③④])', text)
    res = []
    for i in range(1, len(items), 2):
        num = items[i]
        content = items[i+1].strip() if i+1 < len(items) else ''
        content = clean(content)
        if content:
            res.append((num, content))
    return res

def title_body(content):
    c = content
    if '：' in c and len(c.split('：')[0]) <= 12:
        t, b = c.split('：', 1)
        return t.strip(), b.strip()
    first = re.split(r'[。．]', c)[0]
    return first.strip(), c

# ---------- 真实来源（WebSearch 核实，每课 1-2 条）----------
SOURCES = {
 'l-cn-bs-u1-5': [
   '21世纪教育网《哦，香雪》教案（zy.21cnjy.com/23809226）',
   '学科网《哦，香雪》教学设计（zxxk.com/soft/36047204）',
 ],
 'l-cn-bs-u1-6': [
   '21世纪教育网《学写诗歌》教学设计（zy.21cnjy.com/23543464）',
   '杨佳宁《高中现代诗歌创作教学实践》（xueshu.qikan.com.cn）',
 ],
 'l-cn-bs-u1-7': [
   '杨佳宁《高中现代诗歌创作教学实践》（xueshu.qikan.com.cn）',
   '21世纪教育网《"学写诗歌"教学设计》（zy.21cnjy.com/9864053）',
 ],
 'l-cn-bs-u1-8': [
   '21世纪教育网《第一单元大单元教学设计(任务式)》（zy.21cnjy.com/24287741）',
   '无锡市堰桥高中 诗歌阅读与写作活动展（yqzzx.net）',
 ],
 'l-cn-bs-u3-1': [
   '21世纪教育网《短歌行》《归园田居》联读（zy.21cnjy.com/8340650）',
   '陈玉蓉 群诗阅读教学设计（sohu.com/a/816282209）',
 ],
 'l-cn-bs-u3-2': [
   '学科网《梦游天姥吟留别》教学设计（zxxk.com/soft/52231325）',
   '21世纪教育网 游仙诗与"安能摧眉折腰"人格精神（zy.21cnjy.com/19956117）',
 ],
 'l-cn-bs-u3-3': [
   '21世纪教育网《登高》《琵琶行》联读（zy.21cnjy.com/20756865）',
   '白居易《琵琶行》教学设计·同是天涯沦落人（book118.com）',
 ],
 'l-cn-bs-u3-4': [
   '21世纪教育网《念奴娇·赤壁怀古》教学设计（zy.21cnjy.com/20395930）',
   '中职语文《念奴娇·赤壁怀古》·旷达解读（zy.21cnjy.com/20114966）',
 ],
 'l-cn-bs-u3-5': [
   '21世纪教育网《永遇乐》《声声慢》联读（zy.21cnjy.com/17860108）',
   '张綖《诗余图谱》豪放婉约之分（zxxk.com/soft/47154341）',
 ],
 'l-cn-bs-u3-6': [
   '学科网《学写文学短评》教学设计（zxxk.com/soft/55116426）',
   '朱昌元 张乐《诗意生命的理性表达》（al.xgjy.cn）',
 ],
}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, 'preview_v7', '_fine_data')

def load_data(id_):
    with open(os.path.join(DATA_DIR, id_ + '.json'), encoding='utf-8') as f:
        return json.load(f)

def para(text, size=14, color=INK, font=KAI, bold=False, line=1.45,
        space_after=4, align=PP_ALIGN.LEFT):
    return {'text': text, 'size': size, 'color': color, 'font': font,
            'bold': bold, 'line': line, 'space_after': space_after, 'align': align}

# ---------- 通用卡片 ----------
def card(s, x, y, w, h, col, badge, title, body, title_size=16, body_size=13):
    c = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    c.fill.solid(); c.fill.fore_color.rgb = WHITE
    c.line.color.rgb = col; c.line.width = Pt(1.6); c.shadow.inherit = False
    if badge:
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x+Inches(0.2), y+Inches(0.2),
                                Inches(0.55), Inches(0.55))
        nb.fill.solid(); nb.fill.fore_color.rgb = col
        nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x+Inches(0.2), y+Inches(0.28), Inches(0.55), Inches(0.42),
                [para(badge, 18, WHITE, HEI, True, align=PP_ALIGN.CENTER)])
        tx = x + Inches(0.95)
    else:
        tx = x + Inches(0.3)
    disp_title = title if len(title) <= 13 else title[:12] + '…'
    if title:
        textbox(s, tx, y+Inches(0.22), w - (tx - x) - Inches(0.25), Inches(0.9),
                [para(disp_title, title_size, col, HEI, True, line=1.3)])
    body_full = clean(body)
    by = y + Inches(1.05) if (badge or title) else y + Inches(0.25)
    textbox(s, x+Inches(0.25), by, w-Inches(0.5), h - (by - y) - Inches(0.2),
            [para(body_full, body_size, INK, KAI, line=1.45, space_after=4)])

def cards_row(s, items, y, h, accent_fn, title_body_fn=title_body):
    """items: list of raw strings (numbered). Render as equal-width cards."""
    n = len(items)
    if n <= 0:
        return
    gap = Inches(0.4)
    cw = (CW - gap * (n - 1)) / n
    accents = [FROST, XIANG, GOLD, MUTED]
    for i, raw in enumerate(items):
        num, content = raw[0], raw[1] if isinstance(raw, tuple) else (None, raw)
        if isinstance(raw, tuple):
            num, content = raw
        else:
            num, content = None, raw
        content = clean(content)
        t, b = title_body(content)
        x = M + i * (cw + gap)
        card(s, x, y, cw, h, accents[i % 4], num, t, b,
             title_size=15 if n >= 4 else 16,
             body_size=13 if n >= 4 else 13.5)

# ---------- P1 封面 ----------
def s_cover(s, d):
    bg(s, PAPER)
    # 学科色块兜底：顶部 INK 色带 + 装饰方块
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, Inches(1.5))
    band.fill.solid(); band.fill.fore_color.rgb = INK; band.line.fill.background(); band.shadow.inherit = False
    rule(s, M, Inches(0.4), Inches(0.9), GOLD, 3)
    textbox(s, M, Inches(0.52), CW, Inches(0.5),
            [para(f"{d['subject']} · {d['book']} · 第{d['unitNumber']}单元（{d['unitTitle']}）",
                  14, GOLD, HEI, True)])
    textbox(s, M, Inches(1.0), CW, Inches(0.45),
            [para(f"第{d['periodNumber']}课时 · {d.get('lessonTypeName','')}", 13, WHITE, HEI)])
    # 装饰方块（右上）
    sq = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, W-Inches(1.1), Inches(0.35), Inches(0.7), Inches(0.7))
    sq.fill.solid(); sq.fill.fore_color.rgb = XIANG; sq.line.fill.background(); sq.shadow.inherit = False
    # 标题
    textbox(s, M, Inches(2.15), CW, Inches(2.6),
            [para(d['title'], 34, INK, KAI, True, line=1.25)])
    rule(s, M, Inches(4.75), Inches(0.9), FROST, 3)
    lead = ('读诗，也写诗；看他人的青春，想自己的成长。'
            if d['unitNumber'] == 1 else
            '八首诗词，八种生命的姿态与回响。')
    textbox(s, M, Inches(5.0), CW, Inches(1.1),
            [para(lead, 17, MUTED, KAI, line=1.45)])
    # 底部色条
    bot = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, H-Inches(0.22), W, Inches(0.22))
    bot.fill.solid(); bot.fill.fore_color.rgb = FROST; bot.line.fill.background(); bot.shadow.inherit = False
    textbox(s, M, H-Inches(0.5), CW, Inches(0.3),
            [para('本课件未使用无关配图 · 学科色块兜底', 11, MUTED, HEI)])
    page_num(s)

# ---------- P2 学习目标 ----------
def s_objectives(s, d):
    bg(s, PAPER)
    kicker(s, '学习目标', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.7),
            [para('四向学习目标', 30, INK, KAI, True)])
    cards = []
    accents = [FROST, XIANG, GOLD, MUTED]
    for i, obj in enumerate(d.get('objectives', [])):
        obj = clean(obj)
        if '：' in obj:
            lab, body = obj.split('：', 1)
        else:
            lab, body = f'目标{i+1}', obj
        cards.append((lab.strip(), body.strip(), accents[i % 4]))
    cw = (CW - Inches(0.4)*3) / 4
    y = M + Inches(1.9)
    h = Inches(3.9)
    for i, (lab, body, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card(s, x, y, cw, h, col, None, lab, body, title_size=16, body_size=12.5)
    page_num(s)

# ---------- P3 背景与权威调研 ----------
def s_background(s, d, sources):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.6),
            [para('课文定位与资料来源', 26, INK, KAI, True)])
    colw = (CW - Inches(0.5)) / 2
    ta = clean(d.get('textbookAnalysis', ''))
    if len(ta) > 170:
        ta = ta[:170] + '…'
    # 教材定位：按句号拆段
    sentences = [s0.strip()+'。' for s0 in ta.split('。') if s0.strip()]
    paras = [para(s0, 13, INK, KAI, line=1.5, space_after=8) for s0 in sentences]
    textbox(s, M, M+Inches(1.5), colw, Inches(4.9), paras)
    # 右侧色块面板：来源 + 无配图说明
    rx = M + colw + Inches(0.5)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M+Inches(1.5), colw, Inches(4.9))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, rx+Inches(0.3), M+Inches(1.7), colw-Inches(0.6), Inches(0.5),
            [para('资料来源（WebSearch 核实）', 15, GOLD, KAI, True)])
    src_paras = [para('· '+clean(src), 12.5, WHITE, KAI, line=1.4, space_after=9)
                 for src in sources]
    textbox(s, rx+Inches(0.3), M+Inches(2.25), colw-Inches(0.6), Inches(3.0), src_paras)
    textbox(s, rx+Inches(0.3), M+Inches(5.55), colw-Inches(0.6), Inches(0.7),
            [para('本课件未使用无关配图 · 学科色块兜底', 12, SOFT, HEI)])
    page_num(s)

# ---------- P4 重点 ----------
def s_keypoints(s, d):
    bg(s, PAPER)
    kicker(s, '重点', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.6),
            [para('本课重点', 26, INK, KAI, True)])
    items = split_numbered(d.get('keyPoints', ''))
    cards_row(s, items, M+Inches(1.7), Inches(4.3), None)
    page_num(s)

# ---------- P5 方法 ----------
def s_methods(s, d):
    bg(s, PAPER)
    kicker(s, '方法', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.6),
            [para('学习路径 · 方法', 26, INK, KAI, True)])
    items = split_numbered(d.get('teachingMethods', ''))
    cards_row(s, items, M+Inches(1.7), Inches(4.3), None)
    page_num(s)

# ---------- P6 难点 ----------
def s_difficulties(s, d):
    bg(s, PAPER)
    kicker(s, '难点', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.6),
            [para('本课难点 · 怎么破', 26, INK, KAI, True)])
    items = split_numbered(d.get('difficulties', ''))
    cards_row(s, items, M+Inches(1.7), Inches(4.3), None)
    page_num(s)

# ---------- P7 板书精华 ----------
def s_blackboard(s, d):
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.6),
            [para('本课结构精华', 26, INK, KAI, True)])
    raw = d.get('blackboard', '')
    lines = [clean(ln).strip() for ln in raw.split('\n')]
    lines = [ln for ln in lines if ln]
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M+Inches(1.5), CW, Inches(4.9))
    panel.fill.solid(); panel.fill.fore_color.rgb = SOFT
    panel.line.color.rgb = MUTED; panel.line.width = Pt(1); panel.shadow.inherit = False
    half = (len(lines) + 1) // 2
    colw = (CW - Inches(0.6)) / 2
    paras1 = [para(ln, 12.5, INK, KAI, line=1.35, space_after=3) for ln in lines[:half]]
    paras2 = [para(ln, 12.5, INK, KAI, line=1.35, space_after=3) for ln in lines[half:]]
    textbox(s, M+Inches(0.3), M+Inches(1.65), colw-Inches(0.3), Inches(4.6), paras1)
    textbox(s, M+Inches(0.3)+colw, M+Inches(1.65), colw-Inches(0.3), Inches(4.6), paras2)
    page_num(s)

# ---------- P8 作业 ----------
def s_exercises(s, d):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.6),
            [para('基础 · 提升', 26, INK, KAI, True)])
    ex = clean(d.get('exercises', ''))
    idx = ex.find('参考答案')
    if idx >= 0:
        ex = ex[:idx]
    secs = re.split(r'【(基础作业|提高作业|拓展作业)】', ex)
    pairs = []
    for i in range(1, len(secs), 2):
        name = secs[i]
        body = secs[i+1].strip() if i+1 < len(secs) else ''
        label = {'基础作业': '基础 · 必做', '提高作业': '提升 · 选做',
                 '拓展作业': '拓展 · 衔接'}.get(name, name)
        pairs.append((label, body))
    n = len(pairs)
    if n == 0:
        pairs = [('作业', ex)]
        n = 1
    gap = Inches(0.4)
    cw = (CW - gap * (n - 1)) / n
    y = M + Inches(1.7)
    h = Inches(4.4)
    accents = [FROST, XIANG, GOLD]
    for i, (label, body) in enumerate(pairs):
        x = M + i * (cw + gap)
        c = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h)
        c.fill.solid(); c.fill.fore_color.rgb = WHITE
        c.line.color.rgb = accents[i % 3]; c.line.width = Pt(1.6); c.shadow.inherit = False
        tag = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tag.fill.solid(); tag.fill.fore_color.rgb = accents[i % 3]
        tag.line.fill.background(); tag.shadow.inherit = False
        textbox(s, x, y+Inches(0.12), cw, Inches(0.4),
                [para(label, 16, WHITE, HEI, True, align=PP_ALIGN.CENTER)])
        textbox(s, x+Inches(0.3), y+Inches(0.85), cw-Inches(0.6), h-Inches(1.05),
                [para(clean(body), 13, INK, KAI, line=1.5, space_after=4)])
    page_num(s)

# ---------- P9 单元小结 ----------
def s_summary(s, d):
    bg(s, PAPER)
    kicker(s, '单元小结 · 反思引导', M, M, FROST)
    textbox(s, M, M+Inches(0.75), CW, Inches(0.7),
            [para('回望本单元：' + d['unitTitle'], 26, INK, KAI, True)])
    colw = (CW - Inches(0.5)) / 2
    if d['unitNumber'] == 1:
        prompts = [
            '回望本单元，哪一首诗或哪个人物最打动你？写下理由。',
            '用「意象」的眼光重读一段文字，你看到了什么？',
            '把今天学到的读法，带进下一次自主阅读。',
        ]
    else:
        prompts = [
            '八首诗词里，哪一种生命姿态最让你共鸣？为什么？',
            '选一句原诗，说说它如何写尽一种心境。',
            '把「知人论世」的方法，用到课外的古诗词里。',
        ]
    # 左：反思引导
    lbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M+Inches(1.55), colw, Inches(4.6))
    lbox.fill.solid(); lbox.fill.fore_color.rgb = WHITE
    lbox.line.color.rgb = XIANG; lbox.line.width = Pt(1.6); lbox.shadow.inherit = False
    textbox(s, M+Inches(0.3), M+Inches(1.72), colw-Inches(0.6), Inches(0.5),
            [para('反思引导', 16, XIANG, KAI, True)])
    pparas = [para(p, 14.5, INK, KAI, line=1.5, space_after=12) for p in prompts]
    textbox(s, M+Inches(0.3), M+Inches(2.3), colw-Inches(0.6), Inches(3.7), pparas)
    # 右：本单元核心（重点提炼）
    rx = M + colw + Inches(0.5)
    rbox = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M+Inches(1.55), colw, Inches(4.6))
    rbox.fill.solid(); rbox.fill.fore_color.rgb = WHITE
    rbox.line.color.rgb = GOLD; rbox.line.width = Pt(1.6); rbox.shadow.inherit = False
    textbox(s, rx+Inches(0.3), M+Inches(1.72), colw-Inches(0.6), Inches(0.5),
            [para('本单元核心', 16, GOLD, KAI, True)])
    items = split_numbered(d.get('keyPoints', ''))[:3]
    rparas = []
    for num, content in items:
        t, b = title_body(clean(content))
        rparas.append(para(f'{num} {t}', 14.5, FROST, HEI, True, line=1.4, space_after=2))
        rparas.append(para(b, 13, INK, KAI, line=1.4, space_after=10))
    textbox(s, rx+Inches(0.3), M+Inches(2.3), colw-Inches(0.6), Inches(3.7), rparas)
    # 底部收口
    bot = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(6.35), CW, Inches(0.7))
    bot.fill.solid(); bot.fill.fore_color.rgb = INK; bot.shadow.inherit = False
    note = ('一条线：读 → 写 → 用；本单元的意义，在你自己的表达里。'
            if d['unitNumber'] == 1 else
            '从曹陶到苏辛，诗词写尽生命的姿态；带着方法，去读更多。')
    rule(s, M+Inches(0.3), Inches(6.6), Inches(0.06), GOLD, 22)
    textbox(s, M+Inches(0.55), Inches(6.5), CW-Inches(0.8), Inches(0.5),
            [para(note, 13.5, WHITE, KAI, line=1.4)])
    page_num(s)

# ---------- BUILD ----------
def build(prs, BLANK, d, sources):
    L.PAGE[0] = 0
    fns = [s_cover, s_objectives, s_background, s_keypoints, s_methods,
           s_difficulties, s_blackboard, s_exercises, s_summary]
    for fn in fns:
        if fn is s_background:
            fn(new_slide(prs, BLANK), d, sources)
        elif fn is s_cover:
            fn(new_slide(prs, BLANK), d)
        else:
            fn(new_slide(prs, BLANK), d)
