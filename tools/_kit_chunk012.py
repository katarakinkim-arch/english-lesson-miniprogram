# -*- coding: utf-8 -*-
"""chunk012 共享渲染套件 —— 生物（bio）学生版 9 页课堂 PPT 构建器。

仅依赖 _classroom_lib（设计系统）+ _audit_text（BLOCK/WARN 词表）。
本批为生物（必修1 分子与细胞），可用真实照仅限农业/植物类，与本批「细胞/物质运输」
课题不契合 → 统一采用学科色块兜底（§2.3），并在背景页标注「本课件未使用无关配图」。
所有文字经 sanitize 清洗并 assert 无 BLOCK 词，确保四层审计文本门禁可 PASS。
"""
import re
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)
from _audit_text import BLOCK

# 生物主色：湘碧（绿）契合生命科学
ACCENT = XIANG
ACCENTS = [XIANG, FROST, GOLD, MUTED]

# ---- 教师口吻清洗：防御式替换 ----
REPL = [
    ('教学重点', '重点'), ('教学难点', '难点'), ('教学目标', '目标'), ('教学过程', '学习过程'),
    ('教学设想', '设想'), ('板书设计', '板书'), ('课堂小结', '小结'), ('学法指导', '学习方法'),
    ('教法', '方法'), ('授课', '讲解'), ('讲授', '讲解'), ('教学反思', '回顾'), ('备课', '准备'),
    ('易错点提醒', '注意'), ('易错点', '易混点'), ('板书时机', ''), ('预设回答', ''),
    ('教师讲解', '讲解'), ('教师导语', ''), ('教师讲', '讲解'), ('老师讲', '讲解'),
    ('教师', ''), ('老师', ''), ('同学们', '大家'), ('各位同学', '大家'),
    ('请大家', '大家'), ('请同学', '同学'), ('下面请', ''), ('我们说', ''), ('跟我读', '读'),
    ('一起读', '读'), ('齐读', '读'), ('跟读', '读'),
    ('请翻开', '翻开'), ('请打开', '打开'),
    ('这节课', '本课'), ('本课时', '本课'),
    ('我们一起来', '一起'), ('下面我们', ''), ('我们学习', '学习'), ('我们来', ''),
    ('注意看', '看'), ('想一想', '想一想'), ('思考', '分析'),
]

def sanitize(t):
    if t is None:
        return ''
    t = str(t)
    for a, b in REPL:
        t = t.replace(a, b)
    return t

def assert_clean(t, where=''):
    t = t or ''
    for pat in BLOCK:
        if pat and pat in t:
            raise RuntimeError("BLOCK word '%s' in %s: ...%s..." % (pat, where, t[:50]))

def T(slide, x, y, w, h, paras, **kw):
    """textbox 包装：清洗每个 run 文本并断言无 BLOCK 词。"""
    for p in paras:
        if 'runs' in p:
            for r in p['runs']:
                r['text'] = sanitize(r['text'])
                assert_clean(r['text'], 'run')
        else:
            p['text'] = sanitize(p['text'])
            assert_clean(p['text'], 'para')
    return textbox(slide, x, y, w, h, paras, **kw)

# ---------- 数据解析 ----------
def _strip_num(s):
    s = s.strip()
    s = re.sub(r'^[①-⑳0-9]+[.、)）]?\s*', '', s)
    return s.strip()

def parse_kv(s):
    out = []
    for line in (s or '').split('\n'):
        line = line.strip()
        if not line:
            continue
        line = _strip_num(line)
        if '：' in line:
            t, b = line.split('：', 1)
        elif ':' in line:
            t, b = line.split(':', 1)
        elif '，' in line:
            t, b = line.split('，', 1)
        elif ',' in line:
            t, b = line.split(',', 1)
        else:
            t, b = line, ''
        t = t.strip()
        b = b.strip()
        if not t and b:
            t = b[:8]
        if t or b:
            out.append((t, b))
    return out

def parse_method(s):
    out = []
    for line in (s or '').split('\n'):
        line = line.strip()
        if not line:
            continue
        line = _strip_num(line).rstrip('。')
        m = re.match(r'^(.*?)[（(](.*?)[）)]\s*$', line)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
        else:
            out.append((line, ''))
    return out

def parse_exercises(s):
    s = (s or '').split('【参考答案')[0]
    s = s.split('参考答案')[0]
    tiers = []
    for key in ['基础作业', '提高作业', '拓展作业']:
        idx = s.find('【' + key + '】')
        if idx >= 0:
            rest = s[idx + len('【' + key + '】'):]
            nxt = rest.find('【')
            seg = rest[:nxt] if nxt >= 0 else rest
            seg = seg.replace('\n', ' ').strip().strip('。')
            if seg:
                tiers.append((key, seg))
    # 至少保证 2 档；缺拓展则补一句探究性作业
    if len(tiers) == 2:
        tiers.append(('拓展作业', '把本课要点讲给家人听，或找一处生活中的例子印证。'))
    return tiers[:3]

# ---------- 9 页构建 ----------
def build_bio_pptx(data, sources, out, mnemonic=None, next_link=None, accent=ACCENT):
    title = sanitize(data.get('title', ''))
    unit = sanitize(data.get('unitTitle', ''))
    book = sanitize(data.get('book', ''))
    unit_no = data.get('unitNumber', '')
    period = data.get('periodNumber', '')
    tags = data.get('tags', []) or []
    tag_str = ' · '.join([sanitize(t) for t in tags if t and '课时' not in str(t) and 'Ch' not in str(t)][:5])
    objectives = [sanitize(o) for o in data.get('objectives', [])]
    keypts = parse_kv(data.get('keyPoints', ''))
    diffs = parse_kv(data.get('difficulties', ''))
    methods = parse_method(data.get('teachingMethods', ''))
    ex_tiers = parse_exercises(data.get('exercises', ''))
    textbook = sanitize(data.get('textbookAnalysis', ''))
    assert_clean(title, 'title'); assert_clean(unit, 'unit')

    prs, BLANK = new_presentation()

    # ===== P1 封面 =====
    def s_cover(s):
        bg(s, PAPER)
        band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.28), H)
        band.fill.solid(); band.fill.fore_color.rgb = accent; band.line.fill.background(); band.shadow.inherit = False
        rule(s, M, M + Inches(0.45), Inches(0.9), GOLD, 3)
        head = '%s · 第%s单元 · 第%s课时' % (book, unit_no, period)
        T(s, M, M + Inches(0.65), Inches(11), Inches(0.5),
          [{'text': head, 'size': 15, 'color': accent, 'bold': True, 'font': HEI}])
        T(s, M, Inches(1.95), Inches(12.2), Inches(1.5),
          [{'text': title, 'size': 46, 'color': INK, 'bold': True, 'font': KAI}])
        T(s, M, Inches(3.25), Inches(12), Inches(0.7),
          [{'text': '单元：' + unit, 'size': 20, 'color': accent, 'bold': True, 'font': KAI}])
        lead = textbook[:46] + ('…' if len(textbook) > 46 else '')
        T(s, M, Inches(4.15), Inches(12.0), Inches(1.3),
          [{'text': lead, 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.5}])
        # 底部标签带
        tb_band = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, Inches(6.05), CW, Inches(0.95))
        tb_band.fill.solid(); tb_band.fill.fore_color.rgb = INK; tb_band.shadow.inherit = False
        T(s, M + Inches(0.3), Inches(6.18), CW - Inches(0.6), Inches(0.7),
          [{'text': tag_str, 'size': 13, 'color': WHITE, 'font': HEI}])
        page_num(s)

    # ===== P2 学习目标 =====
    def s_objectives(s):
        bg(s, PAPER)
        kicker(s, '学习目标', M, M, accent)
        T(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
          [{'text': '四向核心素养目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
        cards = []
        for o in objectives[:4]:
            if '：' in o:
                lab, body = o.split('：', 1)
            elif ':' in o:
                lab, body = o.split(':', 1)
            else:
                lab, body = '目标', o
            cards.append((lab.strip(), body.strip()))
        while len(cards) < 4:
            cards.append(('目标', '结合本课内容达成相应素养要求。'))
        cw = (CW - Inches(0.4) * 3) / 4
        y = M + Inches(1.9)
        for i, (lab, body) in enumerate(cards):
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.7))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE
            card.line.color.rgb = ACCENTS[i % 4]; card.line.width = Pt(1.6); card.shadow.inherit = False
            dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + cw/2 - Inches(0.45), y + Inches(0.35), Inches(0.9), Inches(0.9))
            dot.fill.solid(); dot.fill.fore_color.rgb = ACCENTS[i % 4]; dot.line.fill.background(); dot.shadow.inherit = False
            T(s, x + cw/2 - Inches(0.45), y + Inches(0.55), Inches(0.9), Inches(0.5),
              [{'text': str(i+1), 'size': 24, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
            T(s, x + Inches(0.2), y + Inches(1.5), cw - Inches(0.4), Inches(0.6),
              [{'text': lab, 'size': 17, 'color': ACCENTS[i % 4], 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            T(s, x + Inches(0.22), y + Inches(2.15), cw - Inches(0.44), Inches(1.4),
              [{'text': body, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
        page_num(s)

    # ===== P3 背景与权威调研 =====
    def s_background(s):
        bg(s, PAPER)
        kicker(s, '背景 · 权威调研', M, M, accent)
        col_w = (CW - Inches(0.5)) / 2
        lx = M
        T(s, lx, M + Inches(1.25), col_w, Inches(0.6),
          [{'text': '课题背景', 'size': 20, 'color': accent, 'bold': True, 'font': KAI, 'space_after': 6}])
        bg_paras = []
        bg_paras.append({'text': textbook, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 10})
        bg_paras.append({'text': '本课属%s，承接本单元前序知识，为后续内容打基础。' % unit,
                         'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5})
        T(s, lx, M + Inches(1.95), col_w, Inches(4.6), bg_paras)
        rx = M + col_w + Inches(0.5)
        # 调研来源面板
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.25), col_w, Inches(4.3))
        box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
        T(s, rx + Inches(0.3), M + Inches(1.45), col_w - Inches(0.6), Inches(0.5),
          [{'text': '权威调研来源', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
        sp = []
        if sources:
            for k, src in enumerate(sources[:3]):
                sp.append({'text': '· ' + sanitize(src), 'size': 13, 'color': WHITE, 'font': KAI, 'line': 1.5, 'space_after': 8})
        else:
            sp.append({'text': '· 未联网核实（按教材分析兜底）', 'size': 13, 'color': WHITE, 'font': KAI, 'line': 1.5})
        sp.append({'text': '配图说明：本课件未使用无关配图，采用学科色块呈现。',
                   'size': 11.5, 'color': SOFT, 'font': HEI, 'line': 1.4, 'space_before': 6})
        T(s, rx + Inches(0.3), M + Inches(2.05), col_w - Inches(0.6), Inches(3.3), sp)
        page_num(s)

    # ===== P4 重点 =====
    def s_keypoints(s):
        bg(s, PAPER)
        kicker(s, '重点', M, M, accent)
        T(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
          [{'text': '本课需要掌握的重点', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        items = keypts[:4]
        if not items:
            items = [('重点', textbook)]
        n = len(items)
        cols = n if n <= 4 else 4
        cw = (CW - Inches(0.4) * (cols - 1)) / cols
        y = M + Inches(1.7)
        for i, (t, b) in enumerate(items):
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE
            card.line.color.rgb = ACCENTS[i % 4]; card.line.width = Pt(1.6); card.shadow.inherit = False
            tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.7))
            tagbar.fill.solid(); tagbar.fill.fore_color.rgb = ACCENTS[i % 4]; tagbar.line.fill.background(); tagbar.shadow.inherit = False
            T(s, x + Inches(0.1), y + Inches(0.14), cw - Inches(0.2), Inches(0.5),
              [{'text': t, 'size': 14, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            body = b if b else t
            T(s, x + Inches(0.3), y + Inches(0.9), cw - Inches(0.6), Inches(3.3),
              [{'text': body, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'align': PP_ALIGN.CENTER}])
        page_num(s)

    # ===== P5 方法 =====
    def s_methods(s):
        bg(s, PAPER)
        kicker(s, '方法', M, M, accent)
        T(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
          [{'text': '本课采用的学习方法', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        items = methods[:4]
        if not items:
            items = [('方法', '结合图文与模型理解。')]
        n = len(items)
        cols = n if n <= 4 else 4
        cw = (CW - Inches(0.4) * (cols - 1)) / cols
        y = M + Inches(1.7)
        for i, (t, b) in enumerate(items):
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE
            card.line.color.rgb = ACCENTS[i % 4]; card.line.width = Pt(1.8); card.shadow.inherit = False
            T(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.7),
              [{'text': t, 'size': 18, 'color': ACCENTS[i % 4], 'bold': True, 'font': KAI}])
            T(s, x + Inches(0.25), y + Inches(1.15), cw - Inches(0.5), Inches(3.0),
              [{'text': (b if b else '结合本课内容运用该方法。'), 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
        page_num(s)

    # ===== P6 难点 =====
    def s_difficulties(s):
        bg(s, PAPER)
        kicker(s, '难点', M, M, accent)
        T(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
          [{'text': '容易卡住的地方与突破', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        items = diffs[:3]
        if not items:
            items = [('难点', '结合对比与实例厘清。')]
        cols = len(items)
        cw = (CW - Inches(0.4) * (cols - 1)) / cols
        y = M + Inches(1.7)
        for i, (t, b) in enumerate(items):
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE
            card.line.color.rgb = ACCENTS[i % 4]; card.line.width = Pt(1.6); card.shadow.inherit = False
            nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
            nb.fill.solid(); nb.fill.fore_color.rgb = ACCENTS[i % 4]; nb.line.fill.background(); nb.shadow.inherit = False
            T(s, x + Inches(0.25), y + Inches(0.33), Inches(0.6), Inches(0.45),
              [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            T(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.8),
              [{'text': t, 'size': 16.5, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.3}])
            body = b if b else '结合实例与对比，逐步弄清。'
            T(s, x + Inches(0.3), y + Inches(1.15), cw - Inches(0.6), Inches(3.0),
              [{'text': '突破：' + body, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
        page_num(s)

    # ===== P7 板书精华 =====
    def s_blackboard(s):
        bg(s, PAPER)
        kicker(s, '板书精华', M, M, accent)
        hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), CW, Inches(0.55))
        hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
        T(s, M + Inches(0.3), M + Inches(1.28), Inches(3.4), Inches(0.4),
          [{'text': '板块', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
        T(s, M + Inches(4.0), M + Inches(1.28), Inches(8.4), Inches(0.4),
          [{'text': '要点', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
        rows = [('课题', title)]
        for t, b in keypts[:5]:
            if b:
                rows.append((t, t + '：' + b))
            else:
                # 无冒号陈述型要点：标签放窄列，整句放宽列，避免窄列溢出
                rows.append(('要点', t))
        y = M + Inches(1.85)
        for i, (dim, a) in enumerate(rows):
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.58))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE if i % 2 == 0 else SOFT
            card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
            T(s, M + Inches(0.3), y + Inches(0.1), Inches(3.4), Inches(0.4),
              [{'text': dim, 'size': 14, 'color': ACCENTS[i % 4], 'bold': True, 'font': HEI}])
            T(s, M + Inches(4.0), y + Inches(0.1), Inches(8.4), Inches(0.4),
              [{'text': a, 'size': 12.5, 'color': INK, 'font': KAI}])
            y += Inches(0.64)
        page_num(s)

    # ===== P8 作业 =====
    def s_exercises(s):
        bg(s, PAPER)
        kicker(s, '作业', M, M, accent)
        T(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
          [{'text': '基础 · 提高 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        labels = {'基础作业': '基础 · 必做', '提高作业': '提高 · 选做', '拓展作业': '拓展 · 探究'}
        tiers = [(labels.get(k, '作业'), seg) for k, seg in ex_tiers]
        while len(tiers) < 3:
            tiers.append(('拓展 · 探究', '把本课要点讲给家人听，或找一处生活中的例子印证。'))
        cw = (CW - Inches(0.4) * 2) / 3
        y = M + Inches(1.7)
        for i, (tag, body) in enumerate(tiers):
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.7))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE
            card.line.color.rgb = ACCENTS[i % 4]; card.line.width = Pt(1.6); card.shadow.inherit = False
            tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
            tagbar.fill.solid(); tagbar.fill.fore_color.rgb = ACCENTS[i % 4]; tagbar.line.fill.background(); tagbar.shadow.inherit = False
            T(s, x, y + Inches(0.12), cw, Inches(0.4),
              [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            T(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(2.7),
              [{'text': body, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.55}])
        page_num(s)

    # ===== P9 单元小结 =====
    def s_summary(s):
        bg(s, PAPER)
        kicker(s, '单元小结', M, M, accent)
        T(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
          [{'text': '本课小结与单元定位', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
        col_w = (CW - Inches(0.5)) / 2
        lx = M
        T(s, lx, M + Inches(1.3), col_w, Inches(0.5),
          [{'text': '本课小结', 'size': 18, 'color': accent, 'bold': True, 'font': KAI, 'space_after': 6}])
        sp = []
        for t, b in keypts[:4]:
            line = (t + ('：' + b if b else ''))
            sp.append({'text': '· ' + line, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.45, 'space_after': 7})
        T(s, lx, M + Inches(1.85), col_w, Inches(4.0), sp)
        rx = M + col_w + Inches(0.5)
        panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.3), col_w, Inches(4.0))
        panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
        T(s, rx + Inches(0.3), M + Inches(1.5), col_w - Inches(0.6), Inches(0.5),
          [{'text': '单元坐标', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
        coord = []
        coord.append({'text': '教材：' + book, 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 6})
        coord.append({'text': '单元：' + unit, 'size': 13.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 6})
        if next_link:
            coord.append({'text': '衔接：' + sanitize(next_link), 'size': 13, 'color': SOFT, 'font': KAI, 'line': 1.45, 'space_after': 6})
        else:
            coord.append({'text': '衔接：承接本单元前序，铺垫后续内容。', 'size': 13, 'color': SOFT, 'font': KAI, 'line': 1.45, 'space_after': 6})
        if mnemonic:
            coord.append({'text': '口诀：' + sanitize(mnemonic), 'size': 13.5, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.45, 'space_before': 6})
        T(s, rx + Inches(0.3), M + Inches(2.05), col_w - Inches(0.6), Inches(3.0), coord)
        page_num(s)

    for fn in [s_cover, s_objectives, s_background, s_keypoints, s_methods,
               s_difficulties, s_blackboard, s_exercises, s_summary]:
        fn(new_slide(prs, BLANK))

    import os
    os.makedirs(os.path.dirname(out), exist_ok=True)
    prs.save(out)
    return out
