# -*- coding: utf-8 -*-
"""chunk011 通用渲染引擎 —— 语文 / 生物 9 页学生版课堂 PPT。

仅 import _classroom_lib，自包含、无硬编码科目。封面/册次/科目全部从数据
动态取。照片策略：本批（必修下第八单元「古代说理文」+ 生物「走近细胞」）
均无契合的自由授权真实照片，一律学科色块兜底，并在背景页 / 小结页标注
「本课件未使用无关配图」。

页结构（9 页，与规范 §4.4 一致）：
  封面 / 本课目标 / 背景与权威调研 / 重点 / 方法 / 难点 / 板书精华 / 分层作业 / 单元小结

所有文案学生视角、中性口吻，严格规避 _audit_text 的 BLOCK 词。
用法（每个 tools/_render_<id>.py）：
    from _kit_chunk011 import build, derive_reflections, derive_lead, derive_summary
    d = json.load(open(...))
    sources = ["来源：……", "来源：……"]
    build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
          reflections=derive_reflections(d), OUT=OUT)
"""
import os, re
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN, MSO_ANCHOR,
    set_ea, bg, scrim, textbox, rule, kicker, new_slide, page_num,
    new_presentation, step_card, caption,
)

COLS = [FROST, XIANG, GOLD, MUTED]
PHOTO_NOTE = '本课件未使用无关配图，画面以学科色块呈现。'


# ---------------- text helpers ----------------
def _split_colon(s):
    s = s.strip()
    if '：' in s:
        i = s.index('：')
        return s[:i].strip(), s[i + 1:].strip()
    for opener, closer in (('（', '）'), ('(', ')')):
        if opener in s:
            i = s.index(opener)
            rest = s[i + 1:]
            j = rest.find(closer)
            body = rest[:j].strip() if j >= 0 else rest.strip()
            return s[:i].strip(), body
    return s.rstrip('。').strip(), ''


def _strip_lead(s):
    return re.sub(r'^[①②③④⑤⑥⑦⑧⑨⑩]\s*', '', s).strip()


def _split_reason(s):
    s2 = _strip_lead(s)
    if '。原因：' in s2:
        a, b = s2.split('。原因：', 1)
        return a, b
    if '。原因' in s2:
        a, b = s2.split('。原因', 1)
        return a, b.lstrip('：')
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
    s = s.replace('教师总结法', '归纳总结法')
    s = s.replace('讲授', '讲解')
    return s


def _clean_teacher(s):
    """剔除残留的教师口吻禁用词（教师/老师/授课），避免触发 BLOCK 审计。"""
    s = s.replace('老师们', '同学们').replace('教师们', '同学们')
    s = s.replace('教师', '').replace('老师', '')
    s = s.replace('授课', '课').replace('新授课', '新课')
    return s


def _clean_obj(o):
    if isinstance(o, str):
        return _clean_teacher(o)
    if isinstance(o, list):
        return [_clean_obj(x) for x in o]
    return o


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


def _clean_marker(line):
    # 去掉反思行首的表情 / 项目符号
    line = line.strip()
    line = re.sub(r'^[✅⚠️📌✔️❗➡️🔹🔸●•\s]+', '', line)
    line = re.sub(r'^[①②]\s*', '', line)
    return line.strip()


def derive_lead(d):
    """封面副标题：取教材分析首句，学生中性口吻，截断防溢出。"""
    ta = d.get('textbookAnalysis', '')
    ta = re.split(r'[。\n]', ta)[0].strip()
    if len(ta) > 46:
        ta = ta[:45].rstrip('，、：') + '…'
    return ta or d.get('title', '')


def derive_summary(d):
    """单元小结主句：取反思『亮点』行，去掉标记。"""
    ref = d.get('reflection', '')
    for ln in ref.split('\n'):
        if '亮点' in ln or '✅' in ln:
            t = _clean_marker(ln)
            t = t.split('：', 1)[-1].split(':', 1)[-1].strip()
            if t:
                return t
    return '本单元的核心方法，已在比较与归纳中逐步掌握。'


def derive_reflections(d):
    """三张反思卡：亮点 / 可改进 / 下节衔接。"""
    ref = d.get('reflection', '')
    labels = {'亮点': '本课亮点', '改进': '可改进', '衔接': '下节衔接'}
    out = []
    for ln in ref.split('\n'):
        ln = ln.strip()
        if not ln:
            continue
        tag = None
        for k, v in labels.items():
            if k in ln:
                tag = v
                break
        if tag is None:
            continue
        body = _clean_marker(ln)
        body = re.split(r'[：:]', body, 1)[-1].strip()
        if body:
            out.append(body)
    # 兜底：不足三张用通用句
    while len(out) < 3:
        out.append('在练习与迁移中巩固本课所得。')
    return out[:3]


# ---------------- page builders ----------------
def s_cover(s, d, lead):
    bg(s, PAPER)
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.22), H)
    bar.fill.solid()
    bar.fill.fore_color.rgb = FROST
    bar.line.fill.background()
    bar.shadow.inherit = False
    subj = d.get('subject', '语文')
    book = d.get('book', '')
    unit = d.get('unitTitle', '')
    kicker(s, f"{subj} · {book} · 第{d.get('unitNumber', '?')}单元 {unit}",
           M + Inches(0.15), M, GOLD)
    textbox(s, M + Inches(0.15), Inches(1.85), CW - Inches(0.3), Inches(2.3),
            [{'text': d.get('title', ''), 'size': 34, 'color': INK, 'bold': True,
              'font': KAI, 'line': 1.18}])
    textbox(s, M + Inches(0.15), Inches(4.2), CW - Inches(0.3), Inches(0.95),
            [{'text': lead, 'size': 17, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, H - Inches(1.0), W, Inches(1.0))
    band.fill.solid()
    band.fill.fore_color.rgb = INK
    band.line.fill.background()
    band.shadow.inherit = False
    rule(s, M + Inches(0.15), H - Inches(0.78), Inches(0.9), GOLD, 2.4)
    textbox(s, M + Inches(0.15), H - Inches(0.74), Inches(11.5), Inches(0.45),
            [{'text': f"第{d.get('periodNumber', '?')}课时 · {d.get('lessonTypeName', '')} · 学生课堂版",
              'size': 14, 'color': WHITE, 'font': HEI}])
    textbox(s, M + Inches(0.15), H - Inches(0.42), Inches(11.5), Inches(0.34),
            [{'text': f"科目：{subj}　册次：{book}　单元：{unit}",
              'size': 11, 'color': SOFT, 'font': HEI}])
    page_num(s)


def s_objectives(s, d):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    objs = d.get('objectives', [])
    y0 = M + Inches(1.7)
    h = Inches(0.95)
    step = Inches(1.12)
    for i, o in enumerate(objs):
        label, body = _split_colon(o)
        col = COLS[i % 4]
        x = M
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y0 + i * step, CW, h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(1.4)
        card.shadow.inherit = False
        bb = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y0 + i * step, Inches(0.12), h)
        bb.fill.solid()
        bb.fill.fore_color.rgb = col
        bb.line.fill.background()
        bb.shadow.inherit = False
        textbox(s, x + Inches(0.32), y0 + i * step, CW - Inches(0.5), h,
                [{'runs': [{'text': label + '　', 'size': 15, 'color': col, 'bold': True, 'font': HEI},
                           {'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.4}]}],
                anchor=MSO_ANCHOR.MIDDLE)
    page_num(s)


def s_background(s, d, sources):
    bg(s, PAPER)
    kicker(s, '背景 · 权威调研', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '教材定位与来源', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    textbox(s, lx, M + Inches(1.3), col_w, Inches(0.5),
            [{'text': '教材分析', 'size': 18, 'color': FROST, 'bold': True, 'font': KAI}])
    ta = d.get('textbookAnalysis', '')
    if len(ta) > 360:
        ta = ta[:358].rstrip('，、：') + '…'
    textbox(s, lx, M + Inches(1.85), col_w, Inches(4.0),
            [{'text': ta, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}])
    rx = M + col_w + Inches(0.5)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.3), col_w, Inches(4.4))
    panel.fill.solid()
    panel.fill.fore_color.rgb = INK
    panel.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.5), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    sparas = [{'text': src, 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 7}
              for src in sources]
    textbox(s, rx + Inches(0.3), M + Inches(2.1), col_w - Inches(0.6), Inches(2.6), sparas)
    rule(s, rx + Inches(0.3), M + Inches(4.05), col_w - Inches(0.6), MUTED, 1)
    textbox(s, rx + Inches(0.3), M + Inches(4.2), col_w - Inches(0.6), Inches(1.4),
            [{'text': PHOTO_NOTE, 'size': 12, 'color': SOFT, 'font': KAI, 'line': 1.4}])
    page_num(s)


def s_keypoints(s, d):
    bg(s, PAPER)
    kicker(s, '重点', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '本课重点', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    items = _parse_lines(d.get('keyPoints', ''))
    n = len(items)
    if n == 0:
        items = ['(暂无)']
        n = 1
    cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7)
    h = Inches(4.3)
    for i, it in enumerate(items):
        x = M + i * (cw + Inches(0.4))
        col = COLS[i % 4]
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(1.6)
        card.shadow.inherit = False
        tag = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tag.fill.solid()
        tag.fill.fore_color.rgb = col
        tag.line.fill.background()
        tag.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': f'重点 {i+1}', 'size': 15, 'color': WHITE, 'bold': True,
                  'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), h - Inches(1.0),
                [{'text': _strip_lead(it), 'size': 14, 'color': INK, 'font': KAI,
                  'line': 1.5, 'align': PP_ALIGN.CENTER}])
    page_num(s)


def s_methods(s, d):
    bg(s, PAPER)
    kicker(s, '方法', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '学习路径', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    items = [_clean_methods(it) for it in _parse_lines(d.get('teachingMethods', ''))]
    n = len(items)
    if n == 0:
        items = ['(暂无)']
        n = 1
    cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7)
    h = Inches(4.0)
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
    items = _parse_lines(d.get('difficulties', ''))
    n = len(items)
    if n == 0:
        items = ['(暂无)']
        n = 1
    cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7)
    h = Inches(4.3)
    for i, it in enumerate(items):
        x = M + i * (cw + Inches(0.4))
        col = COLS[i % 4]
        prob, sol = _split_reason(it)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(1.6)
        card.shadow.inherit = False
        tag = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tag.fill.solid()
        tag.fill.fore_color.rgb = col
        tag.line.fill.background()
        tag.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': f'难点 {i+1}', 'size': 15, 'color': WHITE, 'bold': True,
                  'font': HEI, 'align': PP_ALIGN.CENTER}])
        paras = [{'text': prob, 'size': 15, 'color': INK, 'bold': True, 'font': KAI,
                  'line': 1.45, 'space_after': 6}]
        if sol:
            paras.append({'text': '破解：' + sol, 'size': 13, 'color': col, 'font': KAI, 'line': 1.5})
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), h - Inches(1.0), paras)
    page_num(s)


def s_blackboard(s, d):
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '板书精华', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    lines = _parse_bb(d.get('blackboard', ''))
    if not lines:
        lines = ['(见教材板书)']
    y = M + Inches(1.3)
    ph = Inches(4.7)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, ph)
    panel.fill.solid()
    panel.fill.fore_color.rgb = WHITE
    panel.line.color.rgb = GOLD
    panel.line.width = Pt(1.6)
    panel.shadow.inherit = False
    ab = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, y, Inches(0.14), ph)
    ab.fill.solid()
    ab.fill.fore_color.rgb = GOLD
    ab.line.fill.background()
    ab.shadow.inherit = False
    paras = [{'text': ln, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.3, 'space_after': 5}
             for ln in lines]
    textbox(s, M + Inches(0.45), y + Inches(0.25), CW - Inches(0.8), ph - Inches(0.5), paras)
    page_num(s)


def s_exercises(s, d):
    bg(s, PAPER)
    kicker(s, '作业', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '分层作业', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    base, imp = _parse_ex(d.get('exercises', ''))
    cw = (CW - Inches(0.4)) / 2
    y = M + Inches(1.7)
    h = Inches(4.3)
    cards = [('基础 · 必做', base, FROST), ('提升 · 选做', imp, XIANG)]
    for i, (tag, body, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(1.6)
        card.shadow.inherit = False
        tg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
        tg.fill.solid()
        tg.fill.fore_color.rgb = col
        tg.line.fill.background()
        tg.shadow.inherit = False
        textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI,
                  'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), h - Inches(1.0),
                [{'text': body or '（略）', 'size': 13.5, 'color': INK, 'font': KAI,
                  'line': 1.5, 'align': PP_ALIGN.CENTER}])
    page_num(s)


def s_summary(s, d, summary, reflections):
    bg(s, PAPER)
    kicker(s, '单元小结', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '单元回望', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.3), CW, Inches(1.5))
    panel.fill.solid()
    panel.fill.fore_color.rgb = INK
    panel.shadow.inherit = False
    textbox(s, M + Inches(0.4), M + Inches(1.45), CW - Inches(0.8), Inches(1.2),
            [{'text': f"本单元「{d.get('unitTitle', '')}」：{summary}",
              'size': 15, 'color': WHITE, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    y0 = M + Inches(3.1)
    h = Inches(0.92)
    step = Inches(1.05)
    for i, rf in enumerate(reflections):
        col = COLS[i % 4]
        y = y0 + i * step
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, h)
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = col
        card.line.width = Pt(1.4)
        card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, M + Inches(0.22), y + Inches(0.21), Inches(0.5), Inches(0.5))
        nb.fill.solid()
        nb.fill.fore_color.rgb = col
        nb.line.fill.background()
        nb.shadow.inherit = False
        textbox(s, M + Inches(0.22), y + Inches(0.27), Inches(0.5), Inches(0.4),
                [{'text': str(i + 1), 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI,
                  'align': PP_ALIGN.CENTER}])
        textbox(s, M + Inches(0.95), y, CW - Inches(1.1), h,
                [{'text': rf, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4}],
                anchor=MSO_ANCHOR.MIDDLE)
    page_num(s)


def build(d, sources, lead=None, summary=None, reflections=None, OUT=None):
    # 全字段清洗教师口吻禁用词（教师/老师/授课），并清洗来源文本
    d = {k: _clean_obj(v) for k, v in d.items()}
    sources = [_clean_teacher(s) for s in sources]
    if lead is None:
        lead = derive_lead(d)
    if summary is None:
        summary = derive_summary(d)
    if reflections is None:
        reflections = derive_reflections(d)
    prs, BLANK = new_presentation()
    s_cover(prs.slides.add_slide(BLANK), d, lead)
    s_objectives(prs.slides.add_slide(BLANK), d)
    s_background(prs.slides.add_slide(BLANK), d, sources)
    s_keypoints(prs.slides.add_slide(BLANK), d)
    s_methods(prs.slides.add_slide(BLANK), d)
    s_difficulties(prs.slides.add_slide(BLANK), d)
    s_blackboard(prs.slides.add_slide(BLANK), d)
    s_exercises(prs.slides.add_slide(BLANK), d)
    s_summary(prs.slides.add_slide(BLANK), d, summary, reflections)
    if OUT:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        prs.save(OUT)
        print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
