# -*- coding: utf-8 -*-
# 共享渲染库 · chunk013 批次（生物 l-bio）
# 由 preview_v7/_fine_data/<id>.json 字段驱动生成 9 页学生版 PPTX。
# 设计系统复用 _classroom_lib；本批生物课无契合自由授权照片，统一学科色块兜底。
import os, re
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

def _split_numbered(s):
    if isinstance(s, list):
        lines = [x.strip() for x in s if isinstance(x, str) and x.strip()]
    else:
        lines = [x.strip() for x in s.split('\n') if x.strip()]
    out = []
    for l in lines:
        l = re.sub(r'^[①②③④⑤⑥⑦⑧⑨⑩]\s*', '', l)
        out.append(l)
    return out

def _parse_obj(obj):
    # obj: list of "类别：内容" or string
    items = obj if isinstance(obj, list) else [x for x in obj.split('\n') if x.strip()]
    res = []
    for it in items:
        it = it.strip()
        if '：' in it:
            lab, body = it.split('：', 1)
        elif ':' in it:
            lab, body = it.split(':', 1)
        else:
            lab, body = '', it
        res.append((lab.strip(), body.strip()))
    return res

def _parse_exercises(s):
    # 取参考答案之前的部分，按 【标记】 拆分
    if '【参考答案' in s:
        s = s[:s.index('【参考答案')]
    segs = {}
    for chunk in re.split(r'【', s):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.match(r'([^】]+)】\s*(.*)', chunk, re.S)
        if m:
            lab, body = m.group(1).strip(), m.group(2).strip()
        else:
            lab, body = '', chunk
        segs[lab] = body
    return segs

PAL = [FROST, XIANG, GOLD, MUTED]

# ---------------- P1 封面 ----------------
def s_cover(s, d):
    bg(s, PAPER)
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, Inches(2.7))
    band.fill.solid(); band.fill.fore_color.rgb = INK; band.line.fill.background(); band.shadow.inherit = False
    rule(s, M, Inches(0.5), Inches(0.9), GOLD, 3)
    ltn = (d.get('lessonTypeName','') or '').replace('授课', '课')
    meta = ' · '.join([d.get('book',''), d.get('grade',''), ltn])
    textbox(s, M, Inches(0.62), Inches(12), Inches(0.4),
            [{'text': meta, 'size': 14, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(1.15), Inches(12.3), Inches(1.2),
            [{'text': d.get('title',''), 'size': 44, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, Inches(2.18), Inches(12), Inches(0.5),
            [{'text': '单元：' + d.get('unitTitle',''), 'size': 18, 'color': SOFT, 'font': KAI}])
    rule(s, M, Inches(3.05), Inches(0.9), FROST, 2.4)
    textbox(s, M, Inches(3.25), Inches(12), Inches(0.5),
            [{'text': '学生课堂版 · 权威调研核实', 'size': 15, 'color': MUTED, 'font': KAI}])
    tags = '  '.join('#'+t for t in d.get('tags', []) if t)
    textbox(s, M, Inches(3.95), Inches(12), Inches(0.5),
            [{'text': tags, 'size': 13, 'color': XIANG, 'font': HEI}])
    cap = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, H - Inches(0.55), W, Inches(0.55))
    cap.fill.solid(); cap.fill.fore_color.rgb = XIANG; cap.line.fill.background(); cap.shadow.inherit = False
    textbox(s, M, H - Inches(0.5), Inches(12), Inches(0.4),
            [{'text': '本课件未使用无关配图 · 学科色块兜底', 'size': 12, 'color': WHITE, 'font': HEI}])
    page_num(s)

# ---------------- P2 学习目标 ----------------
def s_objectives(s, d):
    bg(s, PAPER)
    kicker(s, '学习目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '四向学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    cards = _parse_obj(d.get('objectives', []))
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.9)
    for i, (lab, body) in enumerate(cards):
        col = PAL[i % 4]
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + i*(cw+Inches(0.4)), y, cw, Inches(3.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, M + i*(cw+Inches(0.4)) + cw/2 - Inches(0.45), y + Inches(0.3), Inches(0.9), Inches(0.9))
        dot.fill.solid(); dot.fill.fore_color.rgb = col; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, M + i*(cw+Inches(0.4)) + cw/2 - Inches(0.45), y + Inches(0.5), Inches(0.9), Inches(0.5),
                [{'text': str(i+1), 'size': 24, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, M + i*(cw+Inches(0.4)) + Inches(0.2), y + Inches(1.45), cw - Inches(0.4), Inches(0.5),
                [{'text': lab, 'size': 17, 'color': col, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, M + i*(cw+Inches(0.4)) + Inches(0.22), y + Inches(2.05), cw - Inches(0.44), Inches(1.5),
                [{'text': body, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    page_num(s)

# ---------------- P3 背景与权威调研 ----------------
def s_background(s, d, sources):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.2), col_w, Inches(0.5),
            [{'text': '教材定位与背景', 'size': 19, 'color': FROST, 'bold': True, 'font': KAI}])
    ta = d.get('textbookAnalysis', '')
    paras = [{'text': ta, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8}]
    paras.insert(0, {'text': '本单元主题：' + d.get('unitTitle',''), 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.5, 'space_after': 8})
    textbox(s, lx, M + Inches(1.75), col_w, Inches(4.6), paras)
    rx = M + col_w + Inches(0.5)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.2), col_w, Inches(5.0))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.35), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威来源（联网核实）', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    src_paras = []
    for src in sources:
        src_paras.append({'text': '· ' + src, 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.4, 'space_after': 7})
    src_paras.append({'text': '本课件未使用无关配图', 'size': 11.5, 'color': SOFT, 'font': HEI, 'line': 1.3, 'space_after': 0})
    textbox(s, rx + Inches(0.3), M + Inches(1.95), col_w - Inches(0.6), Inches(4.1), src_paras)
    page_num(s)

# ---------------- P4 重点 ----------------
def s_keypoints(s, d):
    bg(s, PAPER)
    kicker(s, '重点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '本课重点', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    items = _split_numbered(d.get('keyPoints', ''))
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.7)
    for i, body in enumerate(items):
        col = PAL[i % 4]
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tag = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tag.fill.solid(); tag.fill.fore_color.rgb = col; tag.line.fill.background(); tag.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': '重点 ' + str(i+1), 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(0.85), cw - Inches(0.5), Inches(3.1),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------------- P5 方法 ----------------
def s_methods(s, d):
    bg(s, PAPER)
    kicker(s, '方法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': '学习路径与方法', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    items = _split_numbered(d.get('teachingMethods', ''))
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.7)
    for i, body in enumerate(items):
        col = PAL[i % 4]
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.8); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.22), y + Inches(0.25), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.22), y + Inches(0.32), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.6),
                [{'text': '方法', 'size': 16, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.25), y + Inches(1.1), cw - Inches(0.5), Inches(2.9),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------------- P6 难点 ----------------
def s_difficulties(s, d):
    bg(s, PAPER)
    kicker(s, '难点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '易卡之处与突破', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    items = _split_numbered(d.get('difficulties', ''))
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, body in enumerate(items):
        col = PAL[i % 4]
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.32), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.8),
                [{'text': '难点 ' + str(i+1), 'size': 16.5, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.3}])
        textbox(s, x + Inches(0.3), y + Inches(1.15), cw - Inches(0.6), Inches(2.9),
                [{'text': body, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------------- P7 板书精华 ----------------
def s_blackboard(s, d):
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    board = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.25), CW, Inches(5.05))
    board.fill.solid(); board.fill.fore_color.rgb = INK; board.shadow.inherit = False
    rule(s, M + Inches(0.3), M + Inches(1.5), Inches(0.06), GOLD, 34)
    textbox(s, M + Inches(0.55), M + Inches(1.5), Inches(11), Inches(0.5),
            [{'text': '课题：' + d.get('title',''), 'size': 19, 'color': GOLD, 'bold': True, 'font': KAI}])
    items = _split_numbered(d.get('keyPoints', ''))
    paras = []
    for i, body in enumerate(items):
        paras.append({'text': ('①②③④⑤⑥⑦⑧⑨⑩'[i]) + ' ' + body, 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 10})
    textbox(s, M + Inches(0.55), M + Inches(2.25), CW - Inches(1.1), Inches(3.9), paras)
    page_num(s)

# ---------------- P8 作业 ----------------
def s_exercises(s, d):
    bg(s, PAPER)
    kicker(s, '作业', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '分层作业', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    segs = _parse_exercises(d.get('exercises', ''))
    # 按固定顺序取：基础作业 / 提高作业 / 拓展作业
    order = ['基础作业', '提高作业', '拓展作业']
    present = [(k, segs[k]) for k in order if k in segs]
    if not present:
        # 兜底：直接展示全部段落
        present = [(k, v) for k, v in segs.items() if k]
    # 若不足 3 个，补一个“巩固提示”
    fillers = [
        ('巩固提示', '回看本课板书精华，用一句话概括核心过程，写在笔记本上。'),
        ('巩固提示', '结合单元主题，举一例说明本课知识在生活中的应用。'),
    ]
    fi = 0
    while len(present) < 3 and fi < len(fillers):
        present.append(fillers[fi]); fi += 1
    present = present[:3]
    cols = len(present)
    cw = (CW - Inches(0.4) * (cols - 1)) / cols
    y = M + Inches(1.7)
    tier_color = [FROST, XIANG, GOLD]
    for i, (lab, body) in enumerate(present):
        col = tier_color[i % 3]
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.9))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tag = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tag.fill.solid(); tag.fill.fore_color.rgb = col; tag.line.fill.background(); tag.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': lab, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(2.9),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

# ---------------- P9 单元小结 ----------------
def s_summary(s, d):
    bg(s, PAPER)
    kicker(s, '单元小结', M, M, FROST)
    textbox(s, M, M + Inches(0.7), Inches(11.5), Inches(0.7),
            [{'text': d.get('unitTitle',''), 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    paras = [{'text': d.get('textbookAnalysis',''), 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 10}]
    paras.append({'text': '本单元线索：' + d.get('unitTitle','') + '，本课为其中一环，承上启下。',
                  'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5})
    textbox(s, lx, M + Inches(1.55), col_w, Inches(4.6), paras)
    rx = M + col_w + Inches(0.5)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.55), col_w, Inches(4.6))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.7), col_w - Inches(0.6), Inches(0.5),
            [{'text': '本课要点回顾', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    items = _split_numbered(d.get('keyPoints', ''))
    src_paras = []
    for i, body in enumerate(items):
        src_paras.append({'text': ('①②③④⑤⑥⑦⑧⑨⑩'[i]) + ' ' + body, 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 7})
    textbox(s, rx + Inches(0.3), M + Inches(2.3), col_w - Inches(0.6), Inches(3.7), src_paras)
    page_num(s)

def render(lesson, sources, out_path):
    prs, BLANK = new_presentation()
    fns = [s_cover, s_objectives, s_background, s_keypoints, s_methods,
           s_difficulties, s_blackboard, s_exercises, s_summary]
    for fn in fns:
        if fn.__name__ == 's_background':
            fn(new_slide(prs, BLANK), lesson, sources)
        else:
            fn(new_slide(prs, BLANK), lesson)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    prs.save(out_path)
    return out_path
