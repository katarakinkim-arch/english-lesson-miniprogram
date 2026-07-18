# -*- coding: utf-8 -*-
"""共享渲染引擎 —— 语文精细课 9 页学生版 PPT（学科色块兜底，无无关配图）。

用法：每个 tools/_render_<id>.py 导入本模块，定义 PLAN / SOURCES / PHOTO，调用 build()。
设计系统全部复用 _classroom_lib 的 helper 与配色。所有文案以学生视角、中性口吻书写，
不含任何教师口吻禁用词（teacher / 大家 / 板书设计 / 教学过程 等）。
"""
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, textbox, rule, kicker, new_slide, page_num, step_card,
)

PHOTO_NOTE = '本课件未使用无关配图 · 学科色块设计'


def _rect(slide, x, y, w, h, color, line=None, line_w=1.4, radius=False):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(line_w)
    shp.shadow.inherit = False
    return shp


def build(prs, BLANK, PLAN):
    P = PLAN
    sources = P.get('sources', [])
    # ---------------- P1 封面 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    _rect(s, 0, 0, W, Inches(2.75), INK)
    rule(s, M, Inches(0.55), Inches(0.9), GOLD, 3)
    textbox(s, M, Inches(0.72), Inches(11.5), Inches(0.45),
            [{'text': f"{P['book']} · {P['unit']} · {P['period']}",
              'size': 14, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(1.25), Inches(12.3), Inches(1.3),
            [{'text': P['title'], 'size': 36, 'color': WHITE, 'bold': True,
              'font': KAI, 'line': 1.15}])
    textbox(s, M, Inches(3.05), CW, Inches(1.2),
            [{'text': P['lead'], 'size': 17, 'color': INK, 'font': KAI, 'line': 1.5}])
    textbox(s, M, Inches(6.55), CW, Inches(0.4),
            [{'text': PHOTO_NOTE, 'size': 11, 'color': MUTED, 'font': HEI}])
    page_num(s)

    # ---------------- P2 目标 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11), Inches(0.6),
            [{'text': '学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    objs = P['objectives']
    cols = 2
    rows = (len(objs) + 1) // 2
    cw = (CW - Inches(0.4)) / 2
    ch = Inches(2.25)
    gap = Inches(0.4)
    y0 = M + Inches(1.7)
    labels = ['语言能力', '文化意识', '思维品质', '学习能力']
    accents = [FROST, XIANG, GOLD, MUTED]
    for i, obj in enumerate(objs):
        r = i // cols
        c = i % cols
        x = M + c * (cw + gap)
        y = y0 + r * (ch + gap)
        card = _rect(s, x, y, cw, ch, WHITE, line=accents[i % 4], line_w=1.6, radius=True)
        _rect(s, x, y, cw, Inches(0.55), accents[i % 4])
        textbox(s, x, y + Inches(0.1), cw, Inches(0.4),
                [{'text': labels[i] if i < len(labels) else f'目标{i+1}',
                  'size': 15, 'color': WHITE, 'bold': True, 'font': HEI,
                  'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.72), cw - Inches(0.6), ch - Inches(0.85),
                [{'text': obj, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45}])
    page_num(s)

    # ---------------- P3 背景与权威调研 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '背景与权威调研', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.6),
            [{'text': '课文背景与权威来源', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    box = _rect(s, lx, M + Inches(1.55), col_w, Inches(4.6), WHITE, line=SOFT, line_w=1.2, radius=True)
    textbox(s, lx + Inches(0.3), M + Inches(1.75), col_w - Inches(0.6), Inches(0.45),
            [{'text': '课文定位', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI}])
    paras = []
    for ln in P['background'].split('\n'):
        paras.append({'text': ln, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8})
    textbox(s, lx + Inches(0.3), M + Inches(2.25), col_w - Inches(0.6), Inches(3.8), paras)
    rx = M + col_w + Inches(0.5)
    sbox = _rect(s, rx, M + Inches(1.55), col_w, Inches(4.6), INK)
    textbox(s, rx + Inches(0.3), M + Inches(1.75), col_w - Inches(0.6), Inches(0.45),
            [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    sparas = []
    for src in sources:
        sparas.append({'text': '· ' + src, 'size': 12.5, 'color': WHITE, 'font': HEI, 'line': 1.45, 'space_after': 7})
    sparas.append({'text': PHOTO_NOTE, 'size': 11, 'color': GOLD, 'font': HEI, 'line': 1.4, 'space_before': 10})
    textbox(s, rx + Inches(0.3), M + Inches(2.25), col_w - Inches(0.6), Inches(3.8), sparas)
    page_num(s)

    # ---------------- P4 重点 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '重点', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.6),
            [{'text': '本课重点', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    kps = P['keypoints']
    n = len(kps)
    cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7)
    ch = Inches(4.2)
    accents = [FROST, XIANG, GOLD]
    for i, kp in enumerate(kps):
        x = M + i * (cw + Inches(0.4))
        card = _rect(s, x, y, cw, ch, WHITE, line=accents[i % 3], line_w=1.6, radius=True)
        _rect(s, x, y, cw, Inches(0.6), accents[i % 3])
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': f'重点 {i+1}', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI,
                  'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), ch - Inches(1.0),
                [{'text': kp, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)

    # ---------------- P5 方法 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '方法', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.6),
            [{'text': '学习路径与方法', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    meths = P['methods']
    n = len(meths)
    # 2x2 for up to 4, single row beyond
    if n <= 4:
        cols = 2
    else:
        cols = n
    rows_n = (n + cols - 1) // cols
    cw = (CW - Inches(0.4) * (cols - 1)) / cols
    gap = Inches(0.4)
    y0 = M + Inches(1.7)
    ch = Inches(4.2) if rows_n == 1 else Inches(2.0)
    accents = [FROST, XIANG, GOLD, MUTED]
    for i, (t, b) in enumerate(meths):
        r = i // cols
        c = i % cols
        x = M + c * (cw + gap)
        y = y0 + r * (ch + gap)
        card = _rect(s, x, y, cw, ch, WHITE, line=accents[i % 4], line_w=1.6, radius=True)
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.22), y + Inches(0.22),
                                Inches(0.55), Inches(0.55))
        nb.fill.solid(); nb.fill.fore_color.rgb = accents[i % 4]; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.22), y + Inches(0.3), Inches(0.55), Inches(0.4),
                [{'text': str(i + 1), 'size': 18, 'color': WHITE, 'bold': True, 'font': HEI,
                  'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.95), y + Inches(0.24), cw - Inches(1.1), Inches(0.5),
                [{'text': t, 'size': 16.5, 'color': accents[i % 4], 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.3), y + Inches(0.95), cw - Inches(0.6), ch - Inches(1.1),
                [{'text': b, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)

    # ---------------- P6 难点 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '难点', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.6),
            [{'text': '难点突破', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    diffs = P['difficulties']
    n = len(diffs)
    cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7)
    ch = Inches(4.2)
    accents = [FROST, XIANG, GOLD]
    for i, (t, b) in enumerate(diffs):
        x = M + i * (cw + Inches(0.4))
        card = _rect(s, x, y, cw, ch, WHITE, line=accents[i % 3], line_w=1.6, radius=True)
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25),
                                Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = accents[i % 3]; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.33), Inches(0.6), Inches(0.45),
                [{'text': str(i + 1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI,
                  'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.05), y + Inches(0.27), cw - Inches(1.25), Inches(0.7),
                [{'text': t, 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.25}])
        textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), ch - Inches(1.25),
                [{'text': b, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

    # ---------------- P7 板书精华 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.6),
            [{'text': '板书精华', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    rows = P['blackboard']
    hdr = _rect(s, M, M + Inches(1.25), CW, Inches(0.55), INK)
    textbox(s, M + Inches(0.3), M + Inches(1.31), Inches(3.4), Inches(0.4),
            [{'text': '维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(4.0), M + Inches(1.31), Inches(8.4), Inches(0.4),
            [{'text': '内容', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    y = M + Inches(1.85)
    rh = Inches(0.62)
    for i, (dim, cont) in enumerate(rows):
        card = _rect(s, M, y, CW, rh, WHITE if i % 2 == 0 else SOFT, line=MUTED, line_w=0.8, radius=True)
        textbox(s, M + Inches(0.3), y + Inches(0.11), Inches(3.4), Inches(0.42),
                [{'text': dim, 'size': 14, 'color': FROST, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(4.0), y + Inches(0.11), Inches(8.4), Inches(0.42),
                [{'text': cont, 'size': 12.5, 'color': INK, 'font': KAI}])
        y += rh + Inches(0.06)
    page_num(s)

    # ---------------- P8 作业 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '作业', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.6),
            [{'text': '分层作业', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    ex = P['exercises']
    n = len(ex)
    cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7)
    ch = Inches(3.9)
    accents = [FROST, XIANG, GOLD]
    tiers = ['基础 · 必做', '提升 · 选做', '拓展 · 衔接']
    for i, e in enumerate(ex):
        x = M + i * (cw + Inches(0.4))
        card = _rect(s, x, y, cw, ch, WHITE, line=accents[i % 3], line_w=1.6, radius=True)
        _rect(s, x, y, cw, Inches(0.6), accents[i % 3])
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': tiers[i] if i < len(tiers) else f'作业{i+1}',
                  'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), ch - Inches(1.0),
                [{'text': e, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

    # ---------------- P9 单元小结 ----------------
    s = new_slide(prs, BLANK)
    bg(s, PAPER)
    kicker(s, '单元小结', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.6),
            [{'text': '单元小结与反思', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    panel = _rect(s, M, M + Inches(1.55), CW, Inches(4.7), INK)
    rule(s, M + Inches(0.35), M + Inches(1.85), Inches(0.06), GOLD, 30)
    textbox(s, M + Inches(0.6), M + Inches(1.8), CW - Inches(1.0), Inches(0.6),
            [{'text': P['unit'] + ' · 收束引导', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
    sparas = []
    for ln in P['summary'].split('\n'):
        sparas.append({'text': ln, 'size': 14, 'color': WHITE, 'font': KAI, 'line': 1.55, 'space_after': 9})
    sparas.append({'text': PHOTO_NOTE, 'size': 11, 'color': SOFT, 'font': HEI, 'space_before': 8})
    textbox(s, M + Inches(0.6), M + Inches(2.5), CW - Inches(1.2), Inches(3.6), sparas)
    page_num(s)
