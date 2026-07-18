# -*- coding: utf-8 -*-
"""精细课堂学生版 PPTX 生成器（语文必修下 U3 / U4 批处理）。
严格沿用 tools/_classroom_lib 设计系统；9 页固定结构：
封面 / 学习目标 / 背景与权威调研 / 重点 / 方法 / 难点 / 板书精华 / 作业 / 单元小结。
全程学生视角、中性口吻；不使用任何「教师/老师」字样；无契合照片时以学科色块兜底。
"""
import os, re, json
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, textbox, rule, kicker, new_slide, page_num, new_presentation,
)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data')

_CN = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十',
        11:'十一',12:'十二',13:'十三',14:'十四',15:'十五',16:'十六'}
def cn(n): return _CN.get(n, str(n))

# 每课补充：封面导语 + 权威来源（WebSearch 核实，见进度回报）
EXTRA = {
 "l-cn-bx-u3-3": {
   "lead": "同读科学，异在写法——把两篇知识性读物比出表达范式。",
   "sources": ["来源：人民网 / 科技部（屠呦呦 2015 诺贝尔生理学或医学奖）",
              "来源：统编教材教师用书·必修下第三单元（屠呦呦与加来道雄群文）"]},
 "l-cn-bx-u3-4": {
   "lead": "建筑如语言——用『文法』与『词汇』读懂中国建筑的特征。",
   "sources": ["来源：清华大学·梁思成（建筑史学家，1901–1972）",
              "来源：统编教材教师用书·必修下第三单元《中国建筑的特征》"]},
 "l-cn-bx-u3-5": {
   "lead": "一字之差，诗意不同——在『木叶』与『树叶』间辨析暗示性。",
   "sources": ["来源：北京大学新闻网·林庚（诗人、文学史家，1910–2006）",
              "来源：《光明日报》1958-03-16 首发《说「木叶》》"]},
 "l-cn-bx-u3-6": {
   "lead": "把话说清楚——写一篇抓特征、有顺序、语言准确的知识性短文。",
   "sources": ["来源：人民教育出版社教师用书·「如何清晰地说明事理」",
              "来源：统编教材必修下第三单元写作任务"]},
 "l-cn-bx-u3-7": {
   "lead": "好文章是改出来的——在讲评中内化知识性文体的标准。",
   "sources": ["来源：人民教育出版社教师用书·必修下第三单元",
              "来源：统编教材「知识性短文」讲评设计"]},
 "l-cn-bx-u3-8": {
   "lead": "把读到的讲出来——用知识文标准做一场科普分享与单元反思。",
   "sources": ["来源：人民教育出版社教师用书·必修下第三单元",
              "来源：统编教材单元学习任务（科普分享与反思）"]},
 "l-cn-bx-u4-1": {
   "lead": "我们活在媒介里——先认识多媒介，再学会用它、辨它、写它。",
   "sources": ["来源：人民教育出版社·《信息时代的语文生活》学习资源",
              "来源：人民教育出版社教师用书·跨媒介阅读与交流"]},
 "l-cn-bx-u4-2": {
   "lead": "同一件事，写法天差地别——在同信息异构中读懂媒介逻辑。",
   "sources": ["来源：人民教育出版社·《信息时代的语文生活》",
              "来源：人民教育出版社教师用书·跨媒介阅读与交流"]},
 "l-cn-bx-u4-3": {
   "lead": "选对媒介，内容才传得动——为传播目标配上合适策略。",
   "sources": ["来源：人民教育出版社·《信息时代的语文生活》",
              "来源：人民教育出版社教师用书·跨媒介阅读与交流"]},
 "l-cn-bx-u4-4": {
   "lead": "转发之前停三秒——用四步法守住信息时代的媒介素养。",
   "sources": ["来源：人民教育出版社·《信息时代的语文生活》",
              "来源：人民教育出版社教师用书·跨媒介阅读与交流"]},
}

# ---------- 文本清洗（去除禁用/警示词与无关片段） ----------
BOXCHARS = set("─│┌┐└┘├┤┬┴┼·")
def clean(s):
    if s is None: return ""
    s = s.replace('↔', ' / ').replace('→', '→')
    out = []
    for ch in s:
        if ch in BOXCHARS:
            out.append(' ')
        else:
            out.append(ch)
    s = ''.join(out)
    s = s.replace('教师', '')          # 去除残留禁用词（仅出现在方法名中）
    s = s.replace('讲授', '')         # 同上
    s = re.sub(r'本课时.*$', '', s)     # u4-1 背景含「本课时导入」，截断
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def split_lines(s):
    return [clean(x) for x in (s or '').split('\n') if clean(x).strip()]

def strip_key(t):
    return re.split(r'【参考答案', t)[0]

def load(lesson_id):
    with open(os.path.join(DATA, lesson_id + '.json'), encoding='utf-8') as f:
        return json.load(f)

# ---------- 各页 ----------
def s_cover(s, d, ex):
    bg(s, PAPER)
    rule(s, M, M + Inches(0.35), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.55), Inches(11.5), Inches(0.5),
            [{'text': f"{d['book']} · 第{cn(d['unitNumber'])}单元 · 第{cn(d['periodNumber'])}课时",
              'size': 15, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.05), Inches(12.3), Inches(1.7),
            [{'text': d['title'], 'size': 42, 'color': INK, 'bold': True, 'font': KAI}])
    rule(s, M, Inches(3.75), Inches(1.4), FROST, 2.4)
    textbox(s, M, Inches(4.0), Inches(12.2), Inches(1.2),
            [{'text': ex['lead'], 'size': 19, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.4}])
    textbox(s, M, Inches(5.35), Inches(12), Inches(0.9),
            [{'text': d.get('unitTitle', ''), 'size': 14, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    page_num(s)

def s_objectives(s, d):
    bg(s, PAPER)
    kicker(s, '本课目标', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.7),
            [{'text': '四向学习目标', 'size': 30, 'color': INK, 'bold': True, 'font': KAI}])
    objs = d.get('objectives', []) or []
    cols = len(objs) if objs else 1
    cw = (CW - Inches(0.4) * (cols - 1)) / cols
    y = M + Inches(1.9)
    for i, o in enumerate(objs):
        if '：' in o:
            label, body = o.split('：', 1)
        else:
            label, body = f'目标{i+1}', o
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = FROST
        card.line.width = Pt(1.6); card.shadow.inherit = False
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x + cw/2 - Inches(0.42), y + Inches(0.32), Inches(0.84), Inches(0.84))
        dot.fill.solid(); dot.fill.fore_color.rgb = FROST; dot.line.fill.background(); dot.shadow.inherit = False
        textbox(s, x + cw/2 - Inches(0.42), y + Inches(0.5), Inches(0.84), Inches(0.5),
                [{'text': str(i+1), 'size': 22, 'color': WHITE, 'bold': True, 'font': KAI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.2), y + Inches(1.45), cw - Inches(0.4), Inches(0.6),
                [{'text': label, 'size': 17, 'color': FROST, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.24), y + Inches(2.1), cw - Inches(0.48), Inches(1.45),
                [{'text': body, 'size': 13, 'color': INK, 'font': KAI, 'line': 1.45, 'align': PP_ALIGN.CENTER}])
    page_num(s)

def s_background(s, d, ex):
    bg(s, PAPER)
    kicker(s, '背景与权威调研', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    ta = clean(d.get('textbookAnalysis', ''))
    paras = [{'text': ta, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8}]
    textbox(s, lx, M + Inches(1.25), col_w, Inches(4.7), paras)
    rx = M + col_w + Inches(0.5)
    # 学科色块兜底（无契合真实照片）
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, M + Inches(1.25), col_w, Inches(4.7))
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, rx + Inches(0.3), M + Inches(1.45), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    src_paras = []
    for src in ex['sources']:
        src = clean(src)
        if not src.strip():
            continue
        src_paras.append({'text': '· ' + src, 'size': 12.5, 'color': WHITE, 'font': KAI, 'line': 1.45, 'space_after': 8})
    src_paras.append({'text': '本课件未使用无关配图（学科色块兜底）', 'size': 11.5, 'color': SOFT,
                     'font': HEI, 'line': 1.4, 'space_before': 6})
    textbox(s, rx + Inches(0.3), M + Inches(2.05), col_w - Inches(0.6), Inches(3.7), src_paras)
    page_num(s)

def _three_cards(s, lines, header, accent_cycle, note=None):
    kicker(s, header, M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.6),
            [{'text': header, 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    n = len(lines)
    cw = (CW - Inches(0.4) * (n - 1)) / n
    y = M + Inches(1.7)
    for i, ln in enumerate(lines):
        col = accent_cycle[i % len(accent_cycle)]
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col
        card.line.width = Pt(1.6); card.shadow.inherit = False
        nb = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.25), y + Inches(0.28), Inches(0.6), Inches(0.6))
        nb.fill.solid(); nb.fill.fore_color.rgb = col; nb.line.fill.background(); nb.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.35), Inches(0.6), Inches(0.45),
                [{'text': str(i+1), 'size': 20, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(1.0), y + Inches(0.3), cw - Inches(1.2), Inches(0.85),
                [{'text': ln, 'size': 14.5, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.35}])
    if note:
        textbox(s, M, y + Inches(4.5), CW, Inches(0.5),
                [{'text': note, 'size': 12.5, 'color': MUTED, 'font': KAI, 'line': 1.4}])
    page_num(s)

def s_keypoints(s, d):
    lines = split_lines(d.get('keyPoints', ''))
    _three_cards(s, lines, '重点', [FROST, XIANG, GOLD])

def s_methods(s, d):
    lines = split_lines(d.get('teachingMethods', ''))
    accents = [FROST, XIANG, GOLD, MUTED]
    _three_cards(s, lines, '方法', accents,
                note='以上读法 / 写法可迁移到同类知识性文本。')

def s_difficulties(s, d):
    lines = split_lines(d.get('difficulties', ''))
    _three_cards(s, lines, '难点', [FROST, XIANG, GOLD])

def s_blackboard(s, d):
    bg(s, PAPER)
    kicker(s, '板书精华', M, M, FROST)
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.15), CW, Inches(5.05))
    panel.fill.solid(); panel.fill.fore_color.rgb = WHITE; panel.line.color.rgb = MUTED
    panel.line.width = Pt(1.0); panel.shadow.inherit = False
    hdr = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, M, M + Inches(1.15), CW, Inches(0.55))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.22), Inches(8), Inches(0.4),
            [{'text': d['title'], 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    raw = clean(d.get('blackboard', ''))
    lines = split_lines(raw)
    paras = []
    for ln in lines:
        paras.append({'text': ln, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.4, 'space_after': 4})
    textbox(s, M + Inches(0.35), M + Inches(1.85), CW - Inches(0.7), Inches(4.2), paras)
    page_num(s)

def s_exercises(s, d):
    bg(s, PAPER)
    kicker(s, '作业', M, M, FROST)
    ex = strip_key(d.get('exercises', ''))
    if '【提高作业】' in ex:
        base, adv = ex.split('【提高作业】', 1)
        base = '【基础作业】' + base.split('【基础作业】', 1)[-1] if '【基础作业】' in base else base
        adv = '【提高作业】' + adv
    else:
        base, adv = ex, ''
    col_w = (CW - Inches(0.5)) / 2
    b = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.2), col_w, Inches(4.8))
    b.fill.solid(); b.fill.fore_color.rgb = WHITE; b.line.color.rgb = FROST; b.line.width = Pt(1.6); b.shadow.inherit = False
    a = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + col_w + Inches(0.5), M + Inches(1.2), col_w, Inches(4.8))
    a.fill.solid(); a.fill.fore_color.rgb = WHITE; a.line.color.rgb = XIANG; a.line.width = Pt(1.6); a.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.4), col_w - Inches(0.6), Inches(0.5),
            [{'text': '基础 · 必做', 'size': 17, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(2.0), col_w - Inches(0.6), Inches(3.8),
            [{'text': base, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    textbox(s, M + col_w + Inches(0.8), M + Inches(1.4), col_w - Inches(0.6), Inches(0.5),
            [{'text': '提高 · 选做', 'size': 17, 'color': XIANG, 'bold': True, 'font': HEI}])
    textbox(s, M + col_w + Inches(0.8), M + Inches(2.0), col_w - Inches(0.6), Inches(3.8),
            [{'text': adv if adv else '结合本课所学，完成一处拓展练习。',
              'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)

def s_summary(s, d):
    bg(s, PAPER)
    kicker(s, '单元小结', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11.5), Inches(0.7),
            [{'text': '围绕单元，做一次反思', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    # 单元信息条
    bar = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.6), CW, Inches(0.85))
    bar.fill.solid(); bar.fill.fore_color.rgb = SOFT; bar.line.fill.background(); bar.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(1.72), CW - Inches(0.6), Inches(0.6),
            [{'text': f"所属单元：第{cn(d['unitNumber'])}单元 · {d.get('unitTitle','')}",
              'size': 15, 'color': INK, 'bold': True, 'font': HEI}])
    kps = split_lines(d.get('keyPoints', ''))
    prompts = [
        f"回顾本课，你最能向他人讲清哪一个要点？（如：{kps[0] if kps else '核心知识'}）",
        "把本单元几篇课文放在一起，它们共同教给我们怎样的读法？",
        "能否用今天学到的方法，去读懂一篇课外的知识性文章？",
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(2.8)
    for i, p in enumerate(prompts):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(3.0))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = [FROST, XIANG, GOLD][i]; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.3), cw - Inches(0.5), Inches(0.5),
                [{'text': f'反思 {i+1}', 'size': 15, 'color': [FROST, XIANG, GOLD][i], 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.25), y + Inches(0.95), cw - Inches(0.5), Inches(1.9),
                [{'text': p, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)

# ---------- BUILD ----------
def build(lesson_id):
    d = load(lesson_id)
    ex = EXTRA.get(lesson_id, {"lead": "", "sources": ["来源：统编教材教师用书"]})
    # 整体去禁用/警示词兜底
    for k in ('title', 'book', 'unitTitle'):
        d[k] = clean(d.get(k, ''))
    prs, BLANK = new_presentation()
    seq = [
        lambda s: s_cover(s, d, ex),
        lambda s: s_objectives(s, d),
        lambda s: s_background(s, d, ex),
        lambda s: s_keypoints(s, d),
        lambda s: s_methods(s, d),
        lambda s: s_difficulties(s, d),
        lambda s: s_blackboard(s, d),
        lambda s: s_exercises(s, d),
        lambda s: s_summary(s, d),
    ]
    for fn in seq:
        fn(new_slide(prs, BLANK))
    out = os.path.join(HERE, '..', 'preview_v7', 'cn', f'l-{lesson_id}.pptx'.replace('l-l-', 'l-'))
    # lesson_id already has l- prefix; build correct path
    out = os.path.join(HERE, '..', 'preview_v7', 'cn', f'{lesson_id}.pptx')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    prs.save(out)
    print('SAVED', out, 'slides=', len(prs.slides._sldIdLst))

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        build(sys.argv[1])
