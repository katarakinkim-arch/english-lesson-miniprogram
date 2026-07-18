# -*- coding: utf-8 -*-
# 共享渲染引擎（chunk009：必修下 U5/U6 语文 10 课）。
# 9 页学生版 PPT：封面 / 学习目标 / 背景与权威调研 / 重点 / 方法 / 难点 / 板书精华 / 作业 / 单元小结。
# 全部学生视角、中性口吻；彻底清洗 教师/讲授 等 BLOCK 词。无契合自由授权照片，一律学科色块兜底。
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN, MSO_ANCHOR,
    set_ea, bg, textbox, rule, kicker, new_slide, page_num,
    new_presentation,
)

PHOTO_NOTE = '本课件未使用无关配图，画面以学科色块呈现。'

CIRCLED = '①②③④⑤⑥⑦⑧⑨⑩'

def _strip_lead(s):
    s = s.strip()
    if s and s[0] in CIRCLED:
        s = s[1:].strip()
    return s

def _split_colon(s):
    s = s.strip().rstrip('。')
    if '：' in s:
        a, b = s.split('：', 1)
        return a.strip(), b.strip()
    return s, ''

def _split_reason(s):
    s2 = _strip_lead(s)
    if '。原因：' in s2:
        a, b = s2.split('。原因：', 1)
        return a, b
    if '。原因' in s2:
        a, b = s2.split('。原因', 1)
        return a, b.lstrip('：')
    return s2, ''

def _clean_method(s):
    s = s.replace('教师现场改稿', '现场改稿示范')
    s = s.replace('教师总结法', '归纳总结法')
    s = s.replace('教师讲评', '讲评')
    s = s.replace('讲授', '讲解')
    s = s.replace('教师', '')
    return s.strip()

def _split_exercises(txt):
    if '【参考答案' in txt:
        txt = txt.split('【参考答案')[0]
    base, imp = '', ''
    if '【提高作业】' in txt:
        parts = txt.split('【提高作业】')
        base = parts[0].replace('【基础作业】', '').strip()
        imp = parts[1].strip()
    elif '【基础作业】' in txt:
        base = txt.replace('【基础作业】', '').strip()
    else:
        base = txt.strip()
    return base, imp

def _parse_blackboard(txt):
    out = []
    for line in txt.split('\n'):
        for ch in ['┌', '┐', '└', '┘', '│', '─', '├', '┤', '┬', '┴', '┼']:
            line = line.replace(ch, ' ')
        line = ' '.join(line.split())
        if line:
            out.append(line)
    return out

def _parse_lines(s):
    return [l.strip() for l in s.split('\n') if l.strip()]

# ---------------- page builders ----------------
def s_cover(s, d, lead):
    bg(s, INK)
    rule(s, M, M + Inches(0.35), Inches(0.9), GOLD, 3)
    unit_no = d.get('unitNumber', '')
    unit = d.get('unitTitle', '')
    period = d.get('periodNumber', '')
    book = d.get('book', '必修下册')
    kicker(s, f'{book} · 第{unit_no}单元《{unit}》· 第{period}课', M + Inches(0.15), M, GOLD)
    textbox(s, M + Inches(0.15), Inches(1.75), CW - Inches(0.3), Inches(2.2),
            [{'text': d['title'], 'size': 33, 'color': WHITE, 'bold': True, 'font': KAI, 'line': 1.2}])
    textbox(s, M + Inches(0.15), Inches(4.05), CW - Inches(0.3), Inches(1.1),
            [{'text': lead, 'size': 17, 'color': SOFT, 'font': KAI, 'line': 1.45}])
    textbox(s, M + Inches(0.15), H - Inches(0.5), CW - Inches(0.3), Inches(0.35),
            [{'text': PHOTO_NOTE, 'size': 11, 'color': MUTED, 'font': HEI}])
    page_num(s, dark=True)

def s_objectives(s, d):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '四向学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    objs = d.get('objectives', [])
    cols = [FROST, XIANG, GOLD, MUTED]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.9)
    for i, obj in enumerate(objs[:4]):
        lab, body = _split_colon(obj)
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = cols[i]
        card.line.width = Pt(1.6); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + cw/2 - Inches(0.45), y + Inches(0.35), Inches(0.9), Inches(0.9))
        dot.fill.solid(); dot.fill.fore_color.rgb = cols[i]; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, x + cw/2 - Inches(0.45), y + Inches(0.55), Inches(0.9), Inches(0.5),
                [{'text': str(i+1), 'size': 24, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.5), cw - Inches(0.4), Inches(0.6),
                [{'text': lab, 'size': 17, 'color': cols[i], 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.22), y + Inches(2.15), cw - Inches(0.44), Inches(1.4),
                [{'text': body, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_background(s, d, sources):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '教材定位与来源', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.25), col_w, Inches(0.5),
            [{'text': '课文定位', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI}])
    tb = d.get('textbookAnalysis', '')
    sent = [x.strip() for x in re.split(r'[。；]', tb) if x.strip()]
    short = '。'.join(sent[:3]) + ('。' if sent else '')
    paras = [{'text': short, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8}]
    paras.append({'text': f"本单元《{d.get('unitTitle','')}》：文学阅读与写作（小说）/ 实用性阅读与交流。",
                  'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.5})
    textbox(s, lx, M + Inches(1.8), col_w, Inches(4.6), paras)
    rx = M + col_w + Inches(0.5)
    box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.25), col_w, Inches(4.9))
    box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.45), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    sparas = [{'text': src, 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 8}
              for src in sources[:3]]
    sparas.append({'text': PHOTO_NOTE, 'size': 11, 'color': SOFT, 'font': HEI, 'line': 1.4, 'space_before': 6})
    textbox(s, rx + Inches(0.3), M + Inches(2.05), col_w - Inches(0.6), Inches(4.0), sparas)
    page_num(s)

def s_keypoints(s, d):
    bg(s, PAPER)
    kicker(s, '重点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '本课重点', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    kps = [_strip_lead(x) for x in _parse_lines(d.get('keyPoints', ''))][:3]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    accents = [FROST, XIANG, GOLD]
    for i, kp in enumerate(kps):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = accents[i]
        card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = accents[i]; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.32), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.27), cw - Inches(1.2), Inches(0.7),
                [{'text': '要点', 'size': 14, 'color': MUTED, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), Inches(3.0),
                [{'text': kp, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

def s_methods(s, d):
    bg(s, PAPER)
    kicker(s, '方法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '本课方法', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    meths = [_clean_method(x) for x in _parse_lines(d.get('teachingMethods', ''))][:4]
    cw = (CW - Inches(0.4) * 3) / 4
    y = M + Inches(1.7)
    for i, m in enumerate(meths):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = XIANG
        card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.2), y + Inches(0.22), Inches(0.55), Inches(0.55))
        nb.fill.solid(); nb.fill.fore_color.rgb = XIANG; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.2), y + Inches(0.28), Inches(0.55), Inches(0.42),
                [{'text': str(i+1), 'size': 18, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.2), cw - Inches(0.4), Inches(2.8),
                [{'text': m, 'size': 18, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.4, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_difficulties(s, d):
    bg(s, PAPER)
    kicker(s, '难点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '本课难点', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    diffs = _parse_lines(d.get('difficulties', ''))[:3]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    accents = [FROST, XIANG, GOLD]
    for i, df in enumerate(diffs):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = accents[i]
        card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = accents[i]; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.32), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.27), cw - Inches(1.2), Inches(0.7),
                [{'text': '易卡处', 'size': 14, 'color': MUTED, 'bold': True, 'font': KAI}])
        prob, sol = _split_reason(df)
        paras = [{'text': _strip_lead(prob), 'size': 15, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.45, 'space_after': 6}]
        if sol:
            paras.append({'text': '破解：' + sol, 'size': 13, 'color': accents[i], 'font': KAI, 'line': 1.5})
        textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), Inches(3.0), paras)
    page_num(s)

def s_blackboard(s, d):
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '板书精华', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    lines = _parse_blackboard(d.get('blackboard', ''))
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.55), CW, Inches(4.7))
    panel.fill.solid(); panel.fill.fore_color.rgb = WHITE; panel.line.color.rgb = GOLD
    panel.line.width = Pt(1.6); panel.shadow.inherit = False
    ab = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, M + Inches(1.55), Inches(0.14), Inches(4.7))
    ab.fill.solid(); ab.fill.fore_color.rgb = GOLD; ab.line.fill.background(); ab.shadow.inherit = False
    bl = [{'text': ln, 'size': 14, 'color': INK if i % 2 == 0 else MUTED, 'font': KAI, 'line': 1.3, 'space_after': 5}
          for i, ln in enumerate(lines[:12])]
    textbox(s, M + Inches(0.45), M + Inches(1.8), CW - Inches(0.8), Inches(4.2), bl)
    page_num(s)

def s_exercises(s, d):
    bg(s, PAPER)
    kicker(s, '作业', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '分层作业', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    base, imp = _split_exercises(d.get('exercises', ''))
    tiers = []
    if imp:
        tiers = [('基础 · 必做', base, FROST), ('提高 · 选做', imp, XIANG)]
    else:
        tiers = [('作业', base, FROST)]
    if len(tiers) == 2:
        cw = (CW - Inches(0.4)) / 2
        cards_w = cw
    else:
        cards_w = CW
    y = M + Inches(1.7); h = Inches(4.3)
    for i, (tag, body, col) in enumerate(tiers):
        x = M + i * (cards_w + Inches(0.4)) if len(tiers) == 2 else M
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cards_w, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cards_w, Inches(0.6))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cards_w, Inches(0.4),
                [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        items = [t.strip() for t in body.replace('\n', ' ').split('。') if t.strip()]
        bl = [{'text': '· ' + it + '。', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6} for it in items]
        textbox(s, x + Inches(0.3), y + Inches(0.85), cards_w - Inches(0.6), h - Inches(1.0), bl)
    page_num(s)

def s_summary(s, d, summary, reflections):
    bg(s, PAPER)
    kicker(s, '单元小结', M, M, FROST)
    textbox(s, M, M + Inches(0.8), Inches(12), Inches(0.9),
            [{'text': f'回望《{d.get("unitTitle","")}》', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.3), CW, Inches(1.5))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, M + Inches(0.4), M + Inches(1.45), CW - Inches(0.8), Inches(1.2),
            [{'text': summary, 'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    y0 = M + Inches(3.1); h = Inches(0.92); step = Inches(1.05)
    for i, rf in enumerate(reflections[:3]):
        col = [FROST, XIANG, GOLD][i % 3]
        y = y0 + i * step
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, h)
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.4); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, M + Inches(0.22), y + Inches(0.21), Inches(0.5), Inches(0.5))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, M + Inches(0.22), y + Inches(0.27), Inches(0.5), Inches(0.4),
                [{'text': str(i+1), 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, M + Inches(0.95), y, CW - Inches(1.1), h,
                [{'text': rf, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}], anchor=MSO_ANCHOR.MIDDLE)
    page_num(s)

def build(lesson_id, sources, lead, summary, reflections):
    with open(os.path.join(os.path.dirname(HERE), 'preview_v7', '_fine_data', lesson_id + '.json'), encoding='utf-8') as f:
        d = json.load(f)
    prs, BLANK = new_presentation()
    s_cover(new_slide(prs, BLANK), d, lead)
    s_objectives(new_slide(prs, BLANK), d)
    s_background(new_slide(prs, BLANK), d, sources)
    s_keypoints(new_slide(prs, BLANK), d)
    s_methods(new_slide(prs, BLANK), d)
    s_difficulties(new_slide(prs, BLANK), d)
    s_blackboard(new_slide(prs, BLANK), d)
    s_exercises(new_slide(prs, BLANK), d)
    s_summary(new_slide(prs, BLANK), d, summary, reflections)
    OUT = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn', lesson_id + '.pptx')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
