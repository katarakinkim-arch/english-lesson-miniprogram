# -*- coding: utf-8 -*-
# 共享渲染器：语文古典/文化经典 9 页学生版 PPT（手写精排，学科色块兜底，中性口吻）。
# 用法： from _render_cn_classic import build ; build('l-cn-...')
import os, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)
DATA = os.path.join(os.path.dirname(HERE), 'preview_v7', '_fine_data')
OUTDIR = os.path.join(os.path.dirname(HERE), 'preview_v7', 'cn')

# 每课权威来源（已逐条 WebSearch 核实，落到各自课题）
SOURCES = {
 'l-cn-bs-u5-7': [
    '中国教育报：读《乡土中国》的「三把钥匙」（生命经验解概念、写读书笔记）',
    '费孝通《乡土中国》（1948）：差序格局 / 乡土本色等核心概念'],
 'l-cn-bs-u5-8': [
    '中国教育报：读《乡土中国》的「三把钥匙」（概念卡墙、单元反思）',
    '费孝通《乡土中国》：十四篇构成整本书阅读脉络'],
 'l-cn-bx-u1-1': [
    '百度百科《子路、曾皙、冉有、公西华侍坐》——《论语·先进》篇',
    '21世纪教育网：必修下《侍坐》教材深度解读'],
 'l-cn-bx-u1-2': [
    '南京国学研究会：保民为王，实施仁政——孟子政治主张（下）',
    '语文迷：《齐桓晋文之事》原文翻译与赏析'],
 'l-cn-bx-u1-3': [
    '人民号（人民日报客户端）：《庄子》庖丁解牛的故事中隐藏着养生秘笈',
    '重庆社科联：《庖丁解牛》——〈庄子·养生主〉的人生智慧'],
 'l-cn-bx-u1-4': [
    '黄陂教育云：文约而意丰 辞婉而理骋——《烛之武退秦师》辞令赏析',
    '瑞文网：《烛之武退秦师》原文译文及赏析'],
 'l-cn-bx-u1-5': [
    '丁新闻：于微言处观风云——《鸿门宴》文本细读',
    '亦诗网：鸿门宴——楚汉之争的开端（司马迁的悲剧英雄写人）'],
 'l-cn-bx-u1-6': [
    '21世纪教育网：必修下第一单元单元学习任务（人文主题「中华文明之光」）',
    '大连文谷高中试卷：诸子散文与史传散文比较（说理 / 叙事）'],
 'l-cn-bx-u1-7': [
    '中国教育报：参透教材，提升思辨能力（议论文框架与论证表达）',
    '中国教育新闻网：高中语文议论文写作教学策略优化实践'],
 'l-cn-bx-u1-8': [
    '21世纪教育网：必修下第一单元单元学习任务（人文主题「中华文明之光」）',
    '中国教育报：参透教材，提升思辨能力'],
}

def clean_method(s):
    return s.replace('讲授', '讲解')

def split_pair(s, sep='：'):
    s = s.strip().rstrip('。')
    if sep in s:
        a, b = s.split(sep, 1)
        return a.strip(), b.strip()
    return s, ''

def split_exercises(txt):
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

def parse_blackboard(txt):
    lines = []
    for line in txt.split('\n'):
        for ch in ['┌', '┐', '└', '┘', '│', '─', '├', '┤', '┬', '┴', '┼']:
            line = line.replace(ch, ' ')
        line = ' '.join(line.split())
        if line:
            lines.append(line)
    return lines

def build(lesson_id):
    with open(os.path.join(DATA, lesson_id + '.json'), encoding='utf-8') as f:
        d = json.load(f)
    sources = SOURCES.get(lesson_id, ['未联网核实（以教材与 textbookAnalysis 兜底）'])
    title = d['title']
    book = d.get('book', '必修上册')
    unit = d.get('unitTitle', '')
    period = d.get('periodNumber', 0)
    unit_no = d.get('unitNumber', 0)
    kicker_txt = f'{book} · 第{unit_no}单元《{unit}》· 第{period}课时'
    objectives = d.get('objectives', [])
    keypts = [x for x in d.get('keyPoints', '').split('\n') if x.strip()]
    methods = [clean_method(x) for x in d.get('teachingMethods', '').split('\n') if x.strip()]
    diffs = [x for x in d.get('difficulties', '').split('\n') if x.strip()]
    tb = d.get('textbookAnalysis', '')
    ex = d.get('exercises', '')
    bb = parse_blackboard(d.get('blackboard', ''))

    prs, BLANK = new_presentation()

    # ---------- P1 封面 ----------
    def s_cover(s):
        bg(s, INK)
        rule(s, M, M + Inches(0.35), Inches(0.9), GOLD, 3)
        textbox(s, M, M + Inches(0.55), Inches(11.5), Inches(0.5),
                [{'text': kicker_txt, 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
        textbox(s, M, Inches(1.75), Inches(12.3), Inches(2.0),
                [{'text': title, 'size': 32, 'color': WHITE, 'bold': True, 'font': KAI, 'line': 1.3}])
        textbox(s, M, Inches(3.95), Inches(12), Inches(1.4),
                [{'text': '把读到的经典，变成自己的眼光与方法。', 'size': 18, 'color': SOFT, 'font': KAI, 'line': 1.5},
                 {'text': '本课件未使用无关配图，以学科色块呈现。', 'size': 12, 'color': MUTED, 'font': HEI}])
        page_num(s, dark=True)
    # alias for dark page numbers consistency

    # ---------- P2 目标 ----------
    def s_objectives(s):
        bg(s, PAPER)
        kicker(s, '本课目标', M, M, FROST)
        textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
                [{'text': '四向学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
        cols = [FROST, XIANG, GOLD, MUTED]
        cw = (CW - Inches(0.4) * 3) / 4
        y = M + Inches(1.85)
        for i, obj in enumerate(objectives[:4]):
            lab, body = split_pair(obj)
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.8))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = cols[i]; card.line.width = Pt(1.6); card.shadow.inherit = False
            dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + cw/2 - Inches(0.45), y + Inches(0.35), Inches(0.9), Inches(0.9))
            dot.fill.solid(); dot.fill.fore_color.rgb = cols[i]; dot.line.fill.background(); dot.shadow.inherit = False
            textbox(s, x + cw/2 - Inches(0.45), y + Inches(0.55), Inches(0.9), Inches(0.5),
                    [{'text': str(i+1), 'size': 24, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
            textbox(s, x + Inches(0.2), y + Inches(1.5), cw - Inches(0.4), Inches(0.6),
                    [{'text': lab, 'size': 17, 'color': cols[i], 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            textbox(s, x + Inches(0.22), y + Inches(2.15), cw - Inches(0.44), Inches(1.5),
                    [{'text': body, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
        page_num(s)

    # ---------- P3 背景与权威调研 ----------
    def s_background(s):
        bg(s, PAPER)
        kicker(s, '背景 · 权威调研', M, M, FROST)
        col_w = (CW - Inches(0.5)) / 2
        lx = M
        textbox(s, lx, M + Inches(1.2), col_w, Inches(0.6),
                [{'text': '课文定位', 'size': 20, 'color': FROST, 'bold': True, 'font': KAI, 'space_after': 6}])
        tb_lines = []
        # 精简 textbookAnalysis 到 2~3 句
        import re
        sent = re.split(r'[。；]', tb)
        sent = [x.strip() for x in sent if x.strip()]
        short = '。'.join(sent[:3]) + '。'
        tb_lines.append({'text': short, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8})
        tb_lines.append({'text': f'本单元《{unit}》：整本书阅读与研讨 / 中华传统文化经典。', 'size': 13.5, 'color': MUTED, 'font': KAI, 'line': 1.5})
        textbox(s, lx, M + Inches(1.85), col_w, Inches(4.6), tb_lines)
        rx = M + col_w + Inches(0.5)
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.2), col_w, Inches(4.9))
        box.fill.solid(); box.fill.fore_color.rgb = INK; box.shadow.inherit = False
        textbox(s, rx + Inches(0.3), M + Inches(1.4), col_w - Inches(0.6), Inches(0.5),
                [{'text': '权威来源', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI}])
        src_lines = []
        for i, src in enumerate(sources[:2]):
            src_lines.append({'text': f'{i+1}. {src}', 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 8})
        src_lines.append({'text': '本课件未使用无关配图，以学科色块呈现。', 'size': 11.5, 'color': SOFT, 'font': HEI, 'line': 1.4, 'space_after': 4})
        textbox(s, rx + Inches(0.3), M + Inches(2.0), col_w - Inches(0.6), Inches(4.0), src_lines)
        page_num(s)

    # ---------- P4 重点 ----------
    def s_keypoints(s):
        bg(s, PAPER)
        kicker(s, '重点', M, M, FROST)
        textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
                [{'text': '本课重点', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
        cw = (CW - Inches(0.4) * 2) / 3
        y = M + Inches(1.7)
        for i, kp in enumerate(keypts[:3]):
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = FROST; card.line.width = Pt(1.6); card.shadow.inherit = False
            nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
            nb.fill.solid(); nb.fill.fore_color.rgb = FROST; nb.line.fill.background(); nb.shadow.inherit = False
            textbox(s, x + Inches(0.25), y + Inches(0.32), Inches(0.6), Inches(0.45),
                    [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            body = kp
            if '.' in kp and len(kp) > 2 and kp[1] in '、. ':
                body = kp[2:].strip()
            textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.8),
                    [{'text': '要点', 'size': 14, 'color': MUTED, 'bold': True, 'font': KAI}])
            textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), Inches(3.0),
                    [{'text': body, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5}])
        page_num(s)

    # ---------- P5 方法 ----------
    def s_methods(s):
        bg(s, PAPER)
        kicker(s, '方法', M, M, FROST)
        textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
                [{'text': '本课方法', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
        cw = (CW - Inches(0.4) * 3) / 4
        y = M + Inches(1.7)
        for i, m in enumerate(methods[:4]):
            t, b = split_pair(m)
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = XIANG; card.line.width = Pt(1.6); card.shadow.inherit = False
            nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.2), y + Inches(0.22), Inches(0.55), Inches(0.55))
            nb.fill.solid(); nb.fill.fore_color.rgb = XIANG; nb.line.fill.background(); nb.shadow.inherit = False
            textbox(s, x + Inches(0.2), y + Inches(0.28), Inches(0.55), Inches(0.42),
                    [{'text': str(i+1), 'size': 18, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            textbox(s, x + Inches(0.9), y + Inches(0.24), cw - Inches(1.1), Inches(0.6),
                    [{'text': t, 'size': 15, 'color': XIANG, 'bold': True, 'font': HEI, 'line': 1.2}])
            bl = [b] if b else ['—']
            textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), Inches(3.0),
                    [{'text': ln, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.5} for ln in bl])
        page_num(s)

    # ---------- P6 难点 ----------
    def s_difficulties(s):
        bg(s, PAPER)
        kicker(s, '难点', M, M, FROST)
        textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
                [{'text': '本课难点', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
        cw = (CW - Inches(0.4) * 2) / 3
        y = M + Inches(1.7)
        for i, df in enumerate(diffs[:3]):
            x = M + i * (cw + Inches(0.4))
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = GOLD; card.line.width = Pt(1.6); card.shadow.inherit = False
            nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.25), Inches(0.6), Inches(0.6))
            nb.fill.solid(); nb.fill.fore_color.rgb = GOLD; nb.line.fill.background(); nb.shadow.inherit = False
            textbox(s, x + Inches(0.25), y + Inches(0.32), Inches(0.6), Inches(0.45),
                    [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            body = df[2:].strip() if ('.' in df and len(df) > 2 and df[1] in '、. ') else df
            textbox(s, x + Inches(1.0), y + Inches(0.28), cw - Inches(1.2), Inches(0.8),
                    [{'text': '易卡处', 'size': 14, 'color': MUTED, 'bold': True, 'font': KAI}])
            textbox(s, x + Inches(0.3), y + Inches(1.1), cw - Inches(0.6), Inches(3.0),
                    [{'text': body, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
        page_num(s)

    # ---------- P7 板书精华 ----------
    def s_blackboard(s):
        bg(s, PAPER)
        kicker(s, '板书精华', M, M, FROST)
        textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
                [{'text': '板书精华', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
        panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.55), CW, Inches(4.7))
        panel.fill.solid(); panel.fill.fore_color.rgb = WHITE; panel.line.color.rgb = MUTED; panel.line.width = Pt(1.0); panel.shadow.inherit = False
        lines = []
        for i, ln in enumerate(bb[:12]):
            col = INK if i % 2 == 0 else MUTED
            lines.append({'text': ln, 'size': 14, 'color': col, 'font': KAI, 'line': 1.3, 'space_after': 6})
        textbox(s, M + Inches(0.4), M + Inches(1.8), CW - Inches(0.8), Inches(4.2), lines)
        page_num(s)

    # ---------- P8 作业 ----------
    def s_exercises(s):
        bg(s, PAPER)
        kicker(s, '作业', M, M, FROST)
        textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
                [{'text': '分层作业', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
        base, imp = split_exercises(ex)
        if imp:
            cw = (CW - Inches(0.4)) / 2
            cards = [(base, '基础 · 必做', FROST), (imp, '提高 · 选做', XIANG)]
            for i, (txt, tag, col) in enumerate(cards):
                x = M + i * (cw + Inches(0.4))
                y = M + Inches(1.7)
                card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
                card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
                tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
                tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
                textbox(s, x, y + Inches(0.12), cw, Inches(0.4),
                        [{'text': tag, 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
                # 拆成句
                items = [t.strip() for t in txt.replace('\n', ' ').split('。') if t.strip()]
                bl = [{'text': '· ' + it, 'size': 13.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 6} for it in items]
                textbox(s, x + Inches(0.3), y + Inches(0.85), cw - Inches(0.6), Inches(3.3), bl)
        else:
            card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.7), CW, Inches(4.3))
            card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = FROST; card.line.width = Pt(1.6); card.shadow.inherit = False
            items = [t.strip() for t in base.replace('\n', ' ').split('。') if t.strip()]
            bl = [{'text': '· ' + it, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8} for it in items]
            textbox(s, M + Inches(0.4), M + Inches(2.0), CW - Inches(0.8), Inches(3.8), bl)
        page_num(s)

    # ---------- P9 单元小结 ----------
    def s_summary(s):
        bg(s, PAPER)
        kicker(s, '单元小结', M, M, FROST)
        textbox(s, M, M + Inches(0.8), Inches(12), Inches(0.9),
                [{'text': f'回望《{unit}》', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
        # 关键提炼
        kp_short = '；'.join(x[2:].strip() if ('.' in x and len(x) > 2 and x[1] in '、. ') else x for x in keypts[:3])
        textbox(s, M, M + Inches(1.85), CW, Inches(1.4),
                [{'text': '本课要点回顾', 'size': 16, 'color': FROST, 'bold': True, 'font': HEI, 'space_after': 4},
                 {'text': kp_short, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
        # 反思引导（中性、无「思考/这节课/本课时」）
        prompts = [
            '哪一个概念或人物最触动你？用一句话写下来。',
            '把本课学到的方法，套用到下一篇阅读或写作里，会怎样？',
            '用三个词概括你对本单元的新认识。',
        ]
        y = M + Inches(3.5)
        for i, p in enumerate(prompts):
            nb = s.shapes.add_shape(MSO_SHAPE.OVAL, M, y + Inches(0.05), Inches(0.5), Inches(0.5))
            nb.fill.solid(); nb.fill.fore_color.rgb = XIANG; nb.line.fill.background(); nb.shadow.inherit = False
            textbox(s, M, y + Inches(0.12), Inches(0.5), Inches(0.4),
                    [{'text': str(i+1), 'size': 16, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
            textbox(s, M + Inches(0.7), y, CW - Inches(0.7), Inches(0.7),
                    [{'text': p, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.4}])
            y += Inches(0.85)
        page_num(s)

    for fn in [s_cover, s_objectives, s_background, s_keypoints, s_methods,
               s_difficulties, s_blackboard, s_exercises, s_summary]:
        fn(new_slide(prs, BLANK))

    OUT = os.path.join(OUTDIR, lesson_id + '.pptx')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    prs.save(OUT)
    print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
