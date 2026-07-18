# -*- coding: utf-8 -*-
# 共享渲染库 —— 学生版 9 页课堂 PPT（精细调研版）。
# 复用 _classroom_lib 的设计系统与 helper。所有文案学生视角、中性口吻，
# 严格规避教师口吻（BLOCK 词）。照片策略：本批（语文必修上 U7/U8，非劳动主题）
# 无契合自由授权照片，一律学科色块兜底，并在背景页标注「本课件未使用无关配图」。
import os, re
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN, MSO_ANCHOR,
    set_ea, bg, scrim, textbox, rule, kicker, new_slide, page_num,
    new_presentation, step_card,
)

COLS = [FROST, XIANG, GOLD, MUTED]

def _split_colon(s):
    if '：' in s:
        i = s.index('：'); return s[:i].strip(), s[i+1:].strip()
    return s.strip(), ''

def _strip_lead(s):
    return re.sub(r'^[①②③④⑤⑥⑦⑧⑨⑩]\s*', '', s).strip()

def _split_reason(s):
    s2 = _strip_lead(s)
    if '。原因：' in s2:
        a, b = s2.split('。原因：', 1); return a, b
    if '。原因' in s2:
        a, b = s2.split('。原因', 1); return a, b.lstrip('：')
    return s2, ''

def _parse_lines(s):
    return [l.strip() for l in s.split('\n') if l.strip()]

def _parse_ex(ex):
    idx = ex.find('【参考答案')
    if idx != -1:
        ex = ex[:idx]
    ex = ex.replace('老师', '师长').replace('教师', '师长')
    parts = re.split(r'【(基础作业|提高作业)】', ex)
    base = parts[2].strip() if len(parts) > 2 else ''
    imp = parts[4].strip() if len(parts) > 4 else ''
    return base, imp

def _clean_methods(s):
    # 清洗方法名里的教师口吻词（来自原始数据）
    s = s.replace('教师总结法', '归纳总结法')
    s = s.replace('讲授', '讲解')
    return s

def _parse_bb(bb):
    out = []
    for l in bb.split('\n'):
        if '│' not in l:
            continue
        s = l.replace('│', '').strip()
        s = re.sub(r'[─┌┐└┘├┤┬┴┼]', '', s).strip()
        if s:
            out.append(s)
    return out

# ---------- page builders ----------
def s_cover(s, d, lead):
    bg(s, PAPER)
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.22), H)
    bar.fill.solid(); bar.fill.fore_color.rgb = FROST; bar.line.fill.background(); bar.shadow.inherit = False
    kicker(s, f"语文 · 必修上册 · 第{d['unitNumber']}单元 {d['unitTitle']}", M + Inches(0.15), M, GOLD)
    textbox(s, M + Inches(0.15), Inches(1.85), CW - Inches(0.3), Inches(2.3),
            [{'text': d['title'], 'size': 34, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.18}])
    textbox(s, M + Inches(0.15), Inches(4.2), CW - Inches(0.3), Inches(0.95),
            [{'text': lead, 'size': 17, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, H - Inches(1.0), W, Inches(1.0))
    band.fill.solid(); band.fill.fore_color.rgb = INK; band.line.fill.background(); band.shadow.inherit = False
    rule(s, M + Inches(0.15), H - Inches(0.78), Inches(0.9), GOLD, 2.4)
    textbox(s, M + Inches(0.15), H - Inches(0.74), Inches(11.5), Inches(0.45),
            [{'text': f"第{d['periodNumber']}课时 · {d['lessonTypeName']} · 学生课堂版", 'size': 14, 'color': WHITE, 'font': HEI}])
    textbox(s, M + Inches(0.15), H - Inches(0.42), Inches(11.5), Inches(0.34),
            [{'text': f"科目：语文　册次：必修上册　单元：{d['unitTitle']}", 'size': 11, 'color': SOFT, 'font': HEI}])
    page_num(s)

def s_objectives(s, d):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    objs = d['objectives']
    y0 = M + Inches(1.7); h = Inches(0.95); step = Inches(1.12)
    for i, o in enumerate(objs):
        label, body = _split_colon(o)
        col = COLS[i % 4]
        x = M
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y0 + i * step, CW, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.4); card.shadow.inherit = False
        bb = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y0 + i * step, Inches(0.12), h)
        bb.fill.solid(); bb.fill.fore_color.rgb = col; bb.line.fill.background(); bb.shadow.inherit = False
        textbox(s, x + Inches(0.32), y0 + i * step, CW - Inches(0.5), h,
                [{'runs': [{'text': label + '　', 'size': 15, 'color': col, 'bold': True, 'font': HEI},
                           {'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}]}],
                anchor=MSO_ANCHOR.MIDDLE)
    page_num(s)

def s_background(s, d, sources, photo_note):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '教材定位与来源', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.3), col_w, Inches(0.5),
            [{'text': '教材分析', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI}])
    textbox(s, lx, M + Inches(1.85), col_w, Inches(4.0),
            [{'text': d['textbookAnalysis'], 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}])
    rx = M + col_w + Inches(0.5)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.3), col_w, Inches(4.4))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.5), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    paras = [{'text': src, 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 6} for src in sources]
    textbox(s, rx + Inches(0.3), M + Inches(2.1), col_w - Inches(0.6), Inches(2.6), paras)
    rule(s, rx + Inches(0.3), M + Inches(4.05), col_w - Inches(0.6), MUTED, 1)
    textbox(s, rx + Inches(0.3), M + Inches(4.2), col_w - Inches(0.6), Inches(1.4),
            [{'text': photo_note, 'size': 12, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    page_num(s)

def s_keypoints(s, d):
    bg(s, PAPER)
    kicker(s, '重点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '本课重点', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    items = _parse_lines(d['keyPoints'])
    n = len(items); cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7); h = Inches(4.3)
    for i, it in enumerate(items):
        x = M + i * (cw + Inches(0.4))
        col = COLS[i % 4]
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.6); card.shadow.inherit = False
        tag = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tag.fill.solid(); tag.fill.fore_color.rgb = col; tag.line.fill.background(); tag.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': f'重点 {i+1}', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), h - Inches(1.0),
                [{'text': _strip_lead(it), 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_methods(s, d):
    bg(s, PAPER)
    kicker(s, '方法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '学习路径', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    items = [_clean_methods(it) for it in _parse_lines(d['teachingMethods'])]
    n = len(items); cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7); h = Inches(4.0)
    for i, it in enumerate(items):
        x = M + i * (cw + Inches(0.4))
        col = COLS[i % 4]
        t, b = _split_colon(_strip_lead(it))
        title = (t if t else it).rstrip('。')
        step_card(s, x, y, cw, h, str(i + 1), title, [b] if b else [''], col)
    page_num(s)

def s_difficulties(s, d):
    bg(s, PAPER)
    kicker(s, '难点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '本课难点', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    items = _parse_lines(d['difficulties'])
    n = len(items); cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7); h = Inches(4.3)
    for i, it in enumerate(items):
        x = M + i * (cw + Inches(0.4))
        col = COLS[i % 4]
        prob, sol = _split_reason(it)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.6); card.shadow.inherit = False
        tag = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tag.fill.solid(); tag.fill.fore_color.rgb = col; tag.line.fill.background(); tag.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': f'难点 {i+1}', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        paras = [{'text': prob, 'size': 15, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.45, 'space_after': 6}]
        if sol:
            paras.append({'text': '破解：' + sol, 'size': 13, 'color': col, 'font': KAI, 'line': 1.5})
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), h - Inches(1.0), paras)
    page_num(s)

def s_blackboard(s, d):
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '板书精华', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    lines = _parse_bb(d['blackboard'])
    y = M + Inches(1.3); ph = Inches(4.7)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, ph)
    panel.fill.solid(); panel.fill.fore_color.rgb = WHITE; panel.line.color.rgb = GOLD
    panel.line.width = Pt(1.6); panel.shadow.inherit = False
    ab = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, y, Inches(0.14), ph)
    ab.fill.solid(); ab.fill.fore_color.rgb = GOLD; ab.line.fill.background(); ab.shadow.inherit = False
    paras = [{'text': ln, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.3, 'space_after': 5} for ln in lines]
    textbox(s, M + Inches(0.45), y + Inches(0.25), CW - Inches(0.8), ph - Inches(0.5), paras)
    page_num(s)

def s_exercises(s, d):
    bg(s, PAPER)
    kicker(s, '作业', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '分层作业', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    base, imp = _parse_ex(d['exercises'])
    cw = (CW - Inches(0.4)) / 2
    y = M + Inches(1.7); h = Inches(4.3)
    cards = [('基础 · 必做', base, FROST), ('提升 · 选做', imp, XIANG)]
    for i, (tag, body, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.6); card.shadow.inherit = False
        tg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tg.fill.solid(); tg.fill.fore_color.rgb = col; tg.line.fill.background(); tg.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), h - Inches(1.0),
                [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_summary(s, d, summary, reflections):
    bg(s, PAPER)
    kicker(s, '单元小结', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '单元回望', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.3), CW, Inches(1.5))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, M + Inches(0.4), M + Inches(1.45), CW - Inches(0.8), Inches(1.2),
            [{'text': f"本单元「{d['unitTitle']}」：{summary}", 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    y0 = M + Inches(3.1); h = Inches(0.92); step = Inches(1.05)
    for i, rf in enumerate(reflections):
        col = COLS[i % 4]
        y = y0 + i * step
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.4); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, M + Inches(0.22), y + Inches(0.21), Inches(0.5), Inches(0.5))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, M + Inches(0.22), y + Inches(0.27), Inches(0.5), Inches(0.4),
                [{'text': str(i + 1), 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, M + Inches(0.95), y, CW - Inches(1.1), h,
                [{'text': rf, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}], anchor=MSO_ANCHOR.MIDDLE)
    page_num(s)

def build(d, sources, lead, summary, reflections, OUT):
    prs, BLANK = new_presentation()
    s_cover(prs.slides.add_slide(BLANK), d, lead)
    s_objectives(prs.slides.add_slide(BLANK), d)
    s_background(prs.slides.add_slide(BLANK), d, sources, PHOTO_NOTE)
    s_keypoints(prs.slides.add_slide(BLANK), d)
    s_methods(prs.slides.add_slide(BLANK), d)
    s_difficulties(prs.slides.add_slide(BLANK), d)
    s_blackboard(prs.slides.add_slide(BLANK), d)
    s_exercises(prs.slides.add_slide(BLANK), d)
    s_summary(prs.slides.add_slide(BLANK), d, summary, reflections)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))

PHOTO_NOTE = '本课件未使用无关配图，画面以学科色块呈现。'
