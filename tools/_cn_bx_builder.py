# -*- coding: utf-8 -*-
"""共享渲染器：必修下（bx）语文课堂学生版 PPTX（9 页，中性口吻）。

9 页结构：封面 / 学习目标 / 背景与权威调研 / 重点 / 方法 / 难点 / 板书精华 / 作业 / 单元小结
复用 _classroom_lib 的设计系统与 helper。所有文字学生视角、中性表述，
不使用「教师/老师」等 BLOCK 词。无契合照片时采用学科色块兜底（见 P3）。
"""
import os, re
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    bg, textbox, rule, kicker, new_slide, page_num, caption, step_card,
    new_presentation,
)

def split_numbered(s):
    items = re.split(r'(?m)^\s*(?:[①②③④⑤⑥⑦⑧⑨⑩]|\d+[.、])\s*', s)
    return [x.strip() for x in items if x and x.strip()]

def split_label(s):
    for sep in ('：', ':'):
        if sep in s:
            a, b = s.split(sep, 1)
            return a.strip(), b.strip()
    return '', s.strip()

def parse_diff(s):
    s = re.sub(r'^\s*[①②③④⑤⑥⑦⑧⑨⑩]\s*', '', s)
    if '原因' in s:
        m = re.split(r'原因[:：]', s, 1)
        title = m[0].rstrip('。').strip()
        reason = m[1].strip() if len(m) > 1 else ''
    else:
        title = s.rstrip('。').strip()
        reason = ''
    reason = reason.replace('学生', '容易').replace('需解', '可读作').replace('需为', '可为')
    return title, reason

def parse_board(s):
    out = []
    for ln in s.split('\n'):
        cleaned = ''.join(ch for ch in ln if not (0x2500 <= ord(ch) <= 0x257F))
        cleaned = cleaned.replace('─', '').replace('│', '').strip()
        if cleaned:
            out.append(cleaned)
    return out

def parse_exercises(s):
    s = re.split(r'【参考答案', s)[0]
    parts = re.split(r'(?=【)', s)
    tiers = []
    for p in parts:
        m = re.match(r'【(.+?)】(.+)', p, re.S)
        if m:
            tiers.append((m.group(1).strip(), m.group(2).strip()))
    return tiers

def sanitize(t):
    """去掉可能触发学生版审计的 BLOCK 词（教师口吻）。"""
    for a, b in (('讲授', '讲析'), ('教师现场', '现场'), ('教师总结', '单元总结'),
                 ('教师', '现场'), ('教法', '方法'), ('课堂小结', '单元小结')):
        t = t.replace(a, b)
    return t

def card(slide, x, y, w, h, fill=WHITE, line=GOLD, lw=1.6):
    c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    c.fill.solid()
    c.fill.fore_color.rgb = fill
    c.line.color.rgb = line
    c.line.width = Pt(lw)
    c.shadow.inherit = False
    return c

ACCENT = [FROST, XIANG, GOLD, MUTED]

def build_course(D, SOURCES, out_path, INTRO=''):
    prs, BLANK = new_presentation()
    title = D['title']
    book = D.get('book', '必修下册')
    unit = D.get('unitNumber')
    unitTitle = D.get('unitTitle', '')
    period = D.get('periodNumber')
    lessonType = D.get('lessonTypeName', '')
    book_kicker = f"{book} · 第{unit}单元"
    intro = INTRO or (D.get('textbookAnalysis', '')[:36] + '…')

    objectives = [sanitize(o) for o in D.get('objectives', [])]
    keypoints = [sanitize(k) for k in split_numbered(D.get('keyPoints', ''))]
    methods = [sanitize(m) for m in split_numbered(D.get('teachingMethods', ''))]
    difficulties = [parse_diff(sanitize(x)) for x in split_numbered(D.get('difficulties', ''))]
    board_lines = [sanitize(b) for b in parse_board(D.get('blackboard', ''))]
    tiers = [(sanitize(t), sanitize(b)) for (t, b) in parse_exercises(D.get('exercises', ''))]

    # ---------- P1 封面 ----------
    def s_cover(s):
        bg(s, PAPER)
        band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.32), H)
        band.fill.solid(); band.fill.fore_color.rgb = FROST
        band.line.fill.background(); band.shadow.inherit = False
        kicker(s, book_kicker + ' · ' + unitTitle, M + Inches(0.12), M, GOLD)
        textbox(s, M, Inches(1.85), Inches(11.9), Inches(1.9),
                [{'text': title, 'size': 36, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.18}])
        rule(s, M, Inches(3.55), Inches(0.9), GOLD, 2.4)
        textbox(s, M, Inches(3.78), Inches(11.6), Inches(1.25),
                [{'text': intro, 'size': 16, 'color': MUTED, 'font': KAI, 'line': 1.45}])
        textbox(s, M, Inches(6.35), Inches(11.6), Inches(0.5),
                [{'text': f"学生课堂版 · 第{period}课时 · {lessonType}", 'size': 13, 'color': MUTED, 'font': HEI}])
        page_num(s)

    # ---------- P2 学习目标 ----------
    def s_objectives(s):
        bg(s, PAPER)
        kicker(s, '本课目标', M, M, FROST)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': '四向学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
        cw = (CW - Inches(0.4)) / 2
        ch = Inches(2.3)
        gap = Inches(0.3)
        y0 = M + Inches(1.55)
        for i, obj in enumerate(objectives):
            col = i % 2; row = i // 2
            x = M + col * (cw + Inches(0.4))
            y = y0 + row * (ch + gap)
            lab, body = split_label(obj)
            card(s, x, y, cw, ch, WHITE, ACCENT[i % 4])
            nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.22), Inches(0.5), Inches(0.5))
            nb.fill.solid(); nb.fill.fore_color.rgb = ACCENT[i % 4]
            nb.line.fill.background(); nb.shadow.inherit = False
            textbox(s, x + Inches(0.25), y + Inches(0.28), Inches(0.5), Inches(0.4),
                    [{'text': str(i + 1), 'size': 18, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            textbox(s, x + Inches(0.9), y + Inches(0.24), cw - Inches(1.1), Inches(0.5),
                    [{'text': lab, 'size': 17, 'color': ACCENT[i % 4], 'bold': True, 'font': HEI}])
            textbox(s, x + Inches(0.3), y + Inches(0.9), cw - Inches(0.6), ch - Inches(1.05),
                    [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}])
        page_num(s)

    # ---------- P3 背景与权威调研 ----------
    def s_background(s):
        bg(s, PAPER)
        kicker(s, '背景 · 权威调研', M, M, FROST)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': '课文背景与研读来源', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        col_w = (CW - Inches(0.5)) / 2
        lx = M
        rx = M + col_w + Inches(0.5)
        tb = D.get('textbookAnalysis', '')
        textbox(s, lx, M + Inches(1.5), col_w, Inches(5.0),
                [{'text': tb, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 6}])
        card(s, rx, M + Inches(1.5), col_w, Inches(5.0), INK, GOLD, 1.8)
        textbox(s, rx + Inches(0.3), M + Inches(1.72), col_w - Inches(0.6), Inches(0.5),
                [{'text': '研读来源', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
        sy = M + Inches(2.3)
        for src in SOURCES:
            textbox(s, rx + Inches(0.3), sy, col_w - Inches(0.6), Inches(1.0),
                    [{'text': src, 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.4, 'space_after': 4}])
            sy += Inches(1.0)
        caption(s, '本课件未使用无关配图（无契合照片，学科色块兜底）', rx, M + Inches(6.35), col_w, SOFT)
        page_num(s)

    # ---------- P4 重点 ----------
    def s_keypoints(s):
        bg(s, PAPER)
        kicker(s, '重点', M, M, FROST)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': '本课重点', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
        n = max(1, len(keypoints))
        cw = (CW - Inches(0.4) * (n - 1)) / n
        y = M + Inches(1.7); h = Inches(4.3)
        for i, kp in enumerate(keypoints):
            x = M + i * (cw + Inches(0.4))
            col = ACCENT[i % 4]
            card(s, x, y, cw, h, WHITE, col, 1.8)
            textbox(s, x + Inches(0.25), y + Inches(0.25), cw - Inches(0.5), Inches(0.6),
                    [{'text': f'重点 {i + 1}', 'size': 15, 'color': col, 'bold': True, 'font': HEI}])
            textbox(s, x + Inches(0.25), y + Inches(0.95), cw - Inches(0.5), h - Inches(1.1),
                    [{'text': kp, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.5}])
        page_num(s)

    # ---------- P5 方法 ----------
    def method_card(s, x, y, w, h, num, title, body_lines, accent):
        """方法卡：编号徽标 + 占满宽度的标题框（可换行）+ 下方说明。"""
        card(s, x, y, w, h, WHITE, accent, 1.8)
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.22), y + Inches(0.22), Inches(0.5), Inches(0.5))
        nb.fill.solid(); nb.fill.fore_color.rgb = accent; nb.line.fill.background(); nb.shadow.inherit = False
        nb_size = 16 if num <= 9 else 13
        textbox(s, x + Inches(0.22), y + Inches(0.27), Inches(0.5), Inches(0.42),
                [{'text': str(num), 'size': nb_size, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.28), y + Inches(0.82), w - Inches(0.5), Inches(1.0),
                [{'text': title, 'size': 15, 'color': INK, 'bold': True, 'font': HEI, 'line': 1.25}])
        bl = [{'text': t, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.35, 'space_after': 4} for t in body_lines]
        textbox(s, x + Inches(0.28), y + Inches(1.95), w - Inches(0.5), h - Inches(2.1), bl)

    def s_methods(s):
        bg(s, PAPER)
        kicker(s, '方法', M, M, FROST)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': '学习路径与方法', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        n = max(1, len(methods))
        if n <= 4:
            cw = (CW - Inches(0.4) * (n - 1)) / n
            cols = n; rows = 1
        else:
            cols = 2; rows = (n + 1) // 2
            cw = (CW - Inches(0.4)) / 2
        y0 = M + Inches(1.7); ch = Inches(4.3) if rows == 1 else (Inches(4.3) - Inches(0.35) * (rows - 1)) / rows
        for i, m in enumerate(methods):
            r = i // cols; c = i % cols
            x = M + c * (cw + Inches(0.4))
            y = y0 + r * (ch + Inches(0.35))
            lab, body = split_label(m)
            title = lab if lab else m
            btext = [body] if body else ['在课文语境中体会运用。']
            method_card(s, x, y, cw, ch, i + 1, title, btext, ACCENT[i % 4])
        page_num(s)

    # ---------- P6 难点 ----------
    def s_difficulties(s):
        bg(s, PAPER)
        kicker(s, '难点', M, M, FROST)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': '学习难点与突破', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        n = max(1, len(difficulties))
        cw = (CW - Inches(0.4) * (n - 1)) / n
        y = M + Inches(1.7); h = Inches(4.3)
        for i, (ti, re) in enumerate(difficulties):
            x = M + i * (cw + Inches(0.4))
            col = ACCENT[i % 4]
            card(s, x, y, cw, h, WHITE, col, 1.8)
            nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.55), Inches(0.55))
            nb.fill.solid(); nb.fill.fore_color.rgb = col
            nb.line.fill.background(); nb.shadow.inherit = False
            textbox(s, x + Inches(0.25), y + Inches(0.32), Inches(0.55), Inches(0.42),
                    [{'text': str(i + 1), 'size': 18, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            textbox(s, x + Inches(0.95), y + Inches(0.28), cw - Inches(1.15), Inches(0.6),
                    [{'text': ti, 'size': 16.5, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.3}])
            bl = [{'text': '突破：' + re, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}] if re \
                else [{'text': '在语境中细读，联系全文把握。', 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}]
            textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), h - Inches(1.25), bl)
        page_num(s)

    # ---------- P7 板书精华 ----------
    def s_board(s):
        bg(s, INK)
        kicker(s, '板书精华', M, M, GOLD)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': '板书精华', 'size': 28, 'color': GOLD, 'bold': True, 'font': KAI}])
        lines = board_lines
        half = (len(lines) + 1) // 2
        col_w = (CW - Inches(0.6)) / 2
        lx = M
        rx = M + col_w + Inches(0.6)
        y = M + Inches(1.6)
        lh = Inches(0.52)
        for i, ln in enumerate(lines):
            col = lx if i < half else rx
            yy = y + (i if i < half else i - half) * lh
            textbox(s, col, yy, col_w, lh,
                    [{'text': '· ' + ln, 'size': 12.5, 'color': SOFT, 'font': KAI, 'line': 1.25}])
        page_num(s, dark=True)

    # ---------- P8 作业 ----------
    def s_exercises(s):
        bg(s, PAPER)
        kicker(s, '作业', M, M, FROST)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': '分层作业', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
        t = tiers[:3]
        n = max(1, len(t))
        cw = (CW - Inches(0.4) * (n - 1)) / n
        y = M + Inches(1.7); h = Inches(4.3)
        for i, (tag, body) in enumerate(t):
            x = M + i * (cw + Inches(0.4))
            col = ACCENT[i % 4]
            card(s, x, y, cw, h, WHITE, col, 1.8)
            tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
            tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col
            tagbar.line.fill.background(); tagbar.shadow.inherit = False
            textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                    [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), h - Inches(1.0),
                    [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}])
        page_num(s)

    # ---------- P9 单元小结 ----------
    def s_summary(s):
        bg(s, PAPER)
        kicker(s, '单元小结', M, M, FROST)
        textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
                [{'text': f'回望 · 第{unit}单元', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        card(s, M, M + Inches(1.55), CW, Inches(0.8), INK, GOLD, 1.8)
        textbox(s, M + Inches(0.3), M + Inches(1.62), CW - Inches(0.6), Inches(0.66),
                [{'text': unitTitle, 'size': 18, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        cards = [
            ('我读到了什么', f"本单元围绕「{unitTitle}」展开；本课抓住：{keypoints[0] if keypoints else title}。"),
            ('我留下什么疑问', '哪一处最想再细读？写下你的一个问题，带着它走向课外阅读。'),
            ('我怎样去运用', f"把「{methods[0] if methods else '细读'}」用到一部剧或一篇科普的观赏与阅读中。"),
        ]
        cw = (CW - Inches(0.4) * 2) / 3
        y = M + Inches(2.6); h = Inches(3.6)
        for i, (ti, body) in enumerate(cards):
            x = M + i * (cw + Inches(0.4))
            col = ACCENT[i % 4]
            card(s, x, y, cw, h, WHITE, col, 1.6)
            textbox(s, x + Inches(0.25), y + Inches(0.25), cw - Inches(0.5), Inches(0.5),
                    [{'text': ti, 'size': 16, 'color': col, 'bold': True, 'font': HEI}])
            textbox(s, x + Inches(0.25), y + Inches(0.9), cw - Inches(0.5), h - Inches(1.05),
                    [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5}])
        page_num(s)

    for fn in [s_cover, s_objectives, s_background, s_keypoints, s_methods,
               s_difficulties, s_board, s_exercises, s_summary]:
        fn(new_slide(prs, BLANK))

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    prs.save(out_path)
    print('SAVED', out_path, 'slides=', len(prs.slides._sldIdLst))
