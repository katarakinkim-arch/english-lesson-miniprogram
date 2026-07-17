# -*- coding: utf-8 -*-
"""通用课堂学生版 PPT 映射器（866 课统一管线）。
输入：一课教案对象（含 objectives/keyPoints/difficulties/process/blackboard/exercises...）
      可能带 research 富集（方法一：视频研究融合的招牌招式）。
输出：杂志风·课堂学生版 .pptx（无教师口吻 / 无反思页 / 无"教师用"标签）。

核心变换：process[].content 是"教师版"（教师：「…」/预设回答：/板书时机：/
差异化提示：/易错点提醒：）。本模块剥离这些教师注解，只留学生投影上该看到的
问题 / 任务 / 分析。
"""
import os, re
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from _ppt_design import (PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
                         KAI, HEI, W, H, M, CW, CH,
                         make_prs, blank, bg, place_photo, textbox, rule,
                         kicker, caption, card, pill, summary_bar, page_num,
                         MSO_SHAPE)
from _audit_text import BLOCK as _BLOCK

NUM = '①②③④⑤⑥⑦⑧⑨⑩'

# 教师口吻清除：移除所有 BLOCK 教师元短语（保留 '同学' 单数名词，如"高个子同学"）。
# 这是被否决的"懒人批量版"的核心缺陷——它只剥离 process，其余 6 页直接吐原始教案字段。
_SANITIZE = [p for p in _BLOCK if p != '同学']
def sanitize(s):
    if not s:
        return s
    for pat in _SANITIZE:
        if pat in s:
            s = s.replace(pat, '')
    return s.strip()

# ---------- 教师口吻剥离 ----------
TEACHER_META = ['预设回答', '板书时机', '差异化提示', '易错点提醒', '教师反思', '教学反思']

def split_numbered(s):
    """把 ①…②…③… 拆成列表，保留每条正文。"""
    if not s:
        return []
    parts = re.split(r'[①②③④⑤⑥⑦⑧⑨⑩]', s)
    out = [p.strip().lstrip('、').strip() for p in parts if p.strip()]
    return out

def student_facing(content):
    """从 process 单步 content 提取学生投影该看的问题/任务/分析。
    返回文本行列表（已去 【PPT】/教师meta 注解）。"""
    if not content:
        return []
    # 去掉 【PPT ...】 / 【实物...】 / 【音频...】 标记，但保留其后的实质
    content = re.sub(r'【(?:PPT|实物|音频)[^】]*】', ' ', content)
    # 按 【 切分（剩余标记），逐段处理
    segs = re.split(r'【', content)
    lines = []
    for seg in segs:
        seg = seg.strip()
        if not seg:
            continue
        # 去掉段首的标记关键词（如 预设回答：/板书时机： 等）
        seg = re.sub(r'^[^】]*】', '', seg).strip()
        if not seg:
            continue
        # 命中教师 meta → 整段丢弃
        if any(seg.startswith(t) or seg.startswith(t + '：') for t in TEACHER_META):
            continue
        # 提取 教师：「问题」 中的引号内容（学生该看的问题/任务）
        quotes = re.findall(r'教师[：:]\s*[「\"\'](.+?)[」\"\']', seg, re.S)
        if quotes:
            for q in quotes:
                q = q.strip()
                if q and not q.startswith('（') and len(q) > 1:
                    lines.append(q)
        else:
            # 无引号：若不是 meta 行则保留正文（可能是分析说明）
            if not any(t in seg[:6] for t in TEACHER_META):
                lines.append(seg)
    # 清理：去空、去纯标点、合并过短
    cleaned = []
    for ln in lines:
        ln = ln.strip()
        if ln and not re.fullmatch(r'[。、，：\s]+', ln):
            cleaned.append(ln)
    return cleaned

def parse_exercises(ex):
    """拆 基础作业 / 提高作业。丢弃参考答案（课堂版不给学生看）。
    返回 (base_str, adv_str)。"""
    if not ex:
        return '', '', ''
    # 按 【 标记分段，逐段归属
    parts = re.split(r'【', ex)
    base_parts = []
    adv_parts = []
    current = None
    for part in parts:
        # 检测段首标记关键词
        if part.startswith('基础作业'):
            current = 'base'; part = re.sub(r'^基础作业[】:]?\s*', '', part)
        elif part.startswith('提高作业'):
            current = 'adv'; part = re.sub(r'^提高作业[】:]?\s*', '', part)
        elif any(part.startswith(k) for k in ['参考答案', '拓展作业', '答案']):
            current = None; continue  # 丢弃答案段
        elif current is None:
            continue
        if not current or not part.strip():
            continue
        if current == 'base':
            base_parts.append(part.strip())
        elif current == 'adv':
            adv_parts.append(part.strip())
    base = '\n'.join(base_parts)
    adv = '\n'.join(adv_parts)
    return base, adv, ''

# ---------- 幻灯片构建 ----------
def s_cover(prs, lesson, photos=None, research=None):
    s = blank(prs); bg(s)
    subj = lesson.get('subject', '')
    # 顶部 kicker：学科 + 册 + 单元（去教师口吻残留，兜底安全）
    kp = sanitize(subj) or subj
    if lesson.get('book'): kp += ' · ' + sanitize(lesson['book'])
    if lesson.get('unitTitle'): kp += ' · ' + sanitize(lesson['unitTitle'])
    kicker(s, kp, color=FROST)
    # 标题（课文名）
    title = sanitize(lesson.get('title', '').split('——')[0].split('（')[0].strip())
    textbox(s, M, M + Inches(1.2), CW, Inches(1.6),
            [{'text': title, 'size': 46, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.1}])
    # 副标题（课型/课时）
    sub = []
    if lesson.get('lessonTypeName'): sub.append(sanitize(lesson['lessonTypeName']))
    if lesson.get('periodNumber'): sub.append('第%d课时' % lesson['periodNumber'])
    if lesson.get('duration'): sub.append('%d分钟' % lesson['duration'])
    if sub:
        textbox(s, M, M + Inches(2.9), CW, Inches(0.5),
                [{'text': '  ·  '.join(sub), 'size': 18, 'color': XIANG, 'bold': True, 'font': HEI}])
    # 若有研究富集的"导入钩子"，做一句话导语
    if research and research.get('hook'):
        textbox(s, M, M + Inches(3.8), CW - Inches(3.2), Inches(1.6),
                [{'text': research['hook'], 'size': 17, 'color': MUTED, 'font': KAI, 'line': 1.6}])
    # 右侧真实照片或学科色块
    rx = W - M - Inches(3.0)
    if photos and photos.get('cover') and os.path.exists(photos['cover']):
        place_photo(s, photos['cover'], rx, M + Inches(1.2), Inches(3.0), Inches(3.6))
    else:
        # 学科主题色块（无照片时的优雅兜底）
        col = {'语文': FROST, '英语': XIANG, '数学': INK, '物理': INK,
               '化学': XIANG, '生物': XIANG, '历史': FROST, '政治': FROST, '地理': XIANG}.get(subj, INK)
        card(s, rx, M + Inches(1.2), Inches(3.0), Inches(3.6), fill=col, line=col, line_w=0)
        textbox(s, rx, M + Inches(1.2), Inches(3.0), Inches(3.6),
                [{'text': subj, 'size': 40, 'color': WHITE, 'bold': True, 'font': KAI,
                  'align': PP_ALIGN.CENTER}],
                anchor=MSO_ANCHOR.MIDDLE)
    page_num(s, 1)
    return s

def s_objectives(prs, lesson):
    s = blank(prs); bg(s)
    kicker(s, '学习目标', color=XIANG)
    objs = lesson.get('objectives') or []
    if isinstance(objs, str):
        objs = [o for o in re.split(r'[\n;；]', objs) if o.strip()]
    n = min(len(objs), 4)
    if n == 0:
        page_num(s, 2); return s
    top = M + Inches(1.2)
    bottom_limit = H - Inches(0.6)
    gap = Inches(0.15)
    avail = (bottom_limit - top) - gap * (n - 1)
    ch = min(Inches(1.25), avail / n)
    y = top
    for i, o in enumerate(objs[:4]):
        # 四维标签提取（语言能力/文化意识/思维品质/学习能力）
        o = sanitize(o)
        m = re.match(r'([一-龥]{2,4})[：:]\s*(.*)', o)
        label = sanitize(m.group(1)) if m else '目标'
        body = sanitize(m.group(2)) if m else o
        card(s, M, y, CW, ch, fill=WHITE, line=XIANG, line_w=1.5)
        pill(s, M + Inches(0.25), y + (ch - Inches(0.55)) / 2, Inches(1.5), Inches(0.55),
             label, XIANG, WHITE, 14)
        textbox(s, M + Inches(2.0), y + Inches(0.15), CW - Inches(2.4), ch - Inches(0.3),
                [{'text': body, 'size': 16, 'color': INK, 'font': KAI, 'line': 1.45}],
                anchor=MSO_ANCHOR.MIDDLE)
        y += ch + gap
    page_num(s, 2)
    return s

def s_background(prs, lesson, photos=None):
    """作家作品/背景/学习重点导入（语文为主；其他学科用 textbookAnalysis）。"""
    s = blank(prs); bg(s)
    kicker(s, '作家作品 · 背景', color=FROST)
    ta = lesson.get('textbookAnalysis', '') or ''
    ov = lesson.get('overview', '') or ''
    # overview 含【学情分析】，课堂版去掉，仅取作品/背景相关
    ov_clean = re.sub(r'【学情分析】.*', '', ov, flags=re.S).strip()
    body = (ta + '\n' + ov_clean).strip()
    body = re.sub(r'\n{2,}', '\n', body)
    # 分段
    paras = []
    for ln in body.split('\n'):
        ln = ln.strip()
        if ln:
            paras.append({'text': sanitize(ln), 'size': 15, 'color': INK, 'font': KAI, 'line': 1.55, 'space_after': 8})
    if photos and photos.get('bg') and os.path.exists(photos['bg']):
        # 左文右图
        textbox(s, M, M + Inches(1.2), Inches(7.6), Inches(5.2), paras)
        place_photo(s, photos['bg'], W - M - Inches(4.4), M + Inches(1.2), Inches(4.4), Inches(4.0))
    else:
        textbox(s, M, M + Inches(1.2), CW, Inches(5.2), paras)
    page_num(s, 3)
    return s

def s_keypoints(prs, lesson):
    s = blank(prs); bg(s)
    kicker(s, '学习重点', color=GOLD)
    kps = split_numbered(lesson.get('keyPoints', ''))
    if not kps:
        textbox(s, M, M + Inches(1.3), CW, Inches(1),
                [{'text': '（本课重点见教师教案）', 'size': 14, 'color': MUTED, 'font': KAI}])
        page_num(s, 4); return s
    kps = [sanitize(k) for k in kps]
    cw = (CW - Inches(0.6)) / min(len(kps), 3)
    rows = (len(kps) + 2) // 3
    y = M + Inches(1.3)
    for i, kp in enumerate(kps):
        col = i % 3; row = i // 3
        x = M + col * (cw + Inches(0.3))
        yy = y + row * Inches(2.05)
        card(s, x, yy, cw, Inches(1.85), fill=WHITE, line=GOLD, line_w=2)
        textbox(s, x + Inches(0.25), yy + Inches(0.2), cw - Inches(0.5), Inches(1.5),
                [{'runs': [{'text': '%s ' % NUM[i], 'size': 20, 'color': GOLD, 'bold': True, 'font': HEI},
                           {'text': kp, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.45}]}])
    summary_bar(s, '重点即考点：把上面几条变成自己的话，就是本课要拿住的东西', color=INK, text_color=GOLD, size=16)
    page_num(s, 4)
    return s

def s_difficulties(prs, lesson):
    s = blank(prs); bg(s)
    kicker(s, '学习难点', color=FROST)
    diffs = split_numbered(lesson.get('difficulties', ''))
    if not diffs:
        page_num(s, 5); return s
    y = M + Inches(1.3)
    for i, d in enumerate(diffs[:4]):
        # 拆 原因： 为 难点 + 解释
        m = re.split(r'原因[：:]', d)
        head = sanitize(m[0].strip())
        why = ('原因：' + sanitize(m[1].strip())) if len(m) > 1 else ''
        ch = Inches(1.35)
        card(s, M, y, CW, ch, fill=WHITE, line=FROST, line_w=1.5)
        textbox(s, M + Inches(0.3), y + Inches(0.15), CW - Inches(0.6), ch - Inches(0.3),
                [{'runs': [{'text': '%s ' % NUM[i], 'size': 18, 'color': FROST, 'bold': True, 'font': HEI},
                           {'text': head, 'size': 16, 'color': INK, 'font': KAI, 'line': 1.4, 'bold': True}]},
                 {'text': why, 'size': 13, 'color': MUTED, 'font': KAI, 'line': 1.4, 'space_before': 4}])
        y += ch + Inches(0.15)
    page_num(s, 5)
    return s

def s_process(prs, lesson):
    """课堂探究：把 process 各步转成学生该做的事（剥离教师口吻）。"""
    s = blank(prs); bg(s)
    kicker(s, '课堂探究', color=XIANG)
    steps = lesson.get('process') or []
    if isinstance(steps, str):
        steps = [{'step': '学习过程', 'content': steps}]
    # 取前 5 步，避免溢出
    steps = steps[:5]
    if not steps:
        page_num(s, 6); return s
    # 垂直自适应：在底部留白内均分，确保最后一张卡不越界
    top = M + Inches(1.0)
    bottom_limit = H - Inches(0.7)
    ch = min(Inches(1.7), (bottom_limit - top) / len(steps))
    SCALE_L = 110 / 72.0
    # 卡片内容区可容纳的行数 → 自适应字号与行数（防溢出）
    content_h_px = int((ch - Inches(0.6)) / 914400 * 110)
    psize = 12.0
    per_line = int(psize * 1.3 * SCALE_L) + int(2 * SCALE_L)  # 含 space_after 2pt
    max_lines = int(content_h_px / per_line) if per_line else 1
    if max_lines < 1:
        psize = max(8.0, content_h_px / (1.3 * SCALE_L + 2 * SCALE_L))
        per_line = int(psize * 1.3 * SCALE_L) + int(2 * SCALE_L)
        max_lines = 1
    y = top
    for i, st in enumerate(steps):
        step_name = sanitize(re.sub(r'Step\s*\d+\s*', '', st.get('step', '环节%d' % (i+1))).strip())
        lines = student_facing(st.get('content', ''))
        # 取受限行数（单行限长 52 防换行溢出）
        shown = [(ln[:52] + '…') if len(ln) > 52 else ln for ln in lines[:max(1, min(2, max_lines))]]
        card(s, M, y, CW, ch - Inches(0.12), fill=WHITE, line=SOFT, line_w=1)
        # 环节名 + 序号
        pill(s, M + Inches(0.2), y + Inches(0.18), Inches(0.95), Inches(0.5),
             '%d' % (i+1), XIANG, WHITE, 16)
        textbox(s, M + Inches(1.3), y + Inches(0.15), CW - Inches(1.6), Inches(0.5),
                [{'text': step_name, 'size': 16, 'color': INK, 'bold': True, 'font': HEI}])
        if shown:
            pl = [{'text': '· ' + sanitize(ln), 'size': psize, 'color': MUTED, 'font': KAI,
                   'line': 1.3, 'space_after': 2} for ln in shown]
            textbox(s, M + Inches(1.3), y + Inches(0.55), CW - Inches(1.6), ch - Inches(0.6), pl)
        y += ch
    page_num(s, 6)
    return s

def _est_text_h(text, box_w_px, fsize_pt):
    """忠实复刻 _audit_layout.est_text_h（同度量，保证拟合后必过审计）。"""
    from PIL import Image, ImageDraw, ImageFont
    DPI, SCALE = 110, 110 / 72.0
    FONT_DIR = r"C:\Windows\Fonts"
    fp = os.path.join(FONT_DIR, "simhei.ttf")
    size = max(8, int(round(fsize_pt * SCALE)))
    try:
        fnt = ImageFont.truetype(fp, size)
    except Exception:
        fnt = ImageFont.load_default()
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    mul = 1.15
    total = 0
    for para in text.split('\n'):
        lines, cur = [], ""
        for ch in para:
            trial = cur + ch
            if d.textlength(trial, font=fnt) <= box_w_px - 8 * SCALE or not cur:
                cur = trial
            else:
                lines.append(cur); cur = ch
        if cur:
            lines.append(cur)
        if not lines:
            lines = [""]
        lh = int(size * mul)
        total += len(lines) * lh
    return total

def _fit_blackboard(bb, box_w_px, box_h_px):
    """闭环求最大字号，使 _est_text_h(bb) <= box_h*0.95。"""
    best = 8.0
    for fsize in (18, 16, 14, 12, 10, 8):
        if _est_text_h(bb, box_w_px, fsize) <= box_h_px * 0.95:
            best = float(fsize); break
    # 极端长板书：8pt 仍溢出则截断行数
    if _est_text_h(bb, box_w_px, 8.0) > box_h_px * 0.95:
        rows = bb.split('\n')
        while rows and _est_text_h('\n'.join(rows), box_w_px, 8.0) > box_h_px * 0.95:
            rows = rows[:-1]
        if rows:
            rows[-1] = rows[-1][:30] + '…（详见教案）'
        bb = '\n'.join(rows)
    return best, bb

def s_blackboard(prs, lesson):
    s = blank(prs); bg(s)
    kicker(s, '板书梳理', color=INK)
    bb = lesson.get('blackboard', '') or ''
    bb = sanitize(bb)
    if not bb:
        page_num(s, 7); return s
    import _ppt_design as _D
    # 黑板占满可用高度（顶部 kicker 下 ~1.05in，底部留白 0.55in）
    top_in = M + Inches(1.05)
    board_h = H - top_in - Inches(0.55)
    board = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                               int(M), int(top_in), int(CW), int(board_h))
    board.fill.solid(); board.fill.fore_color.rgb = INK
    board.line.color.rgb = SOFT; board.line.width = Pt(2); board.shadow.inherit = False
    # 内边距文本框
    box_top = top_in + Inches(0.35)
    box_h = board_h - Inches(0.7)
    box_w = CW - Inches(0.8)
    DPI = 110
    box_w_px = int(box_w / 914400 * DPI)
    box_h_px = int(box_h / 914400 * DPI)
    fsize, bb = _fit_blackboard(bb, box_w_px, box_h_px)
    fsize = max(8.0, min(18.0, fsize * _D.FONT_SCALE))
    textbox(s, M + Inches(0.4), box_top, box_w, box_h,
            [{'text': bb, 'size': fsize, 'color': WHITE, 'font': 'Consolas', 'line': 1.15}])
    page_num(s, 7)
    return s

def s_homework(prs, lesson):
    s = blank(prs); bg(s)
    kicker(s, '作业与拓展', color=FROST)
    base, adv, ans = parse_exercises(lesson.get('exercises', ''))
    # 两栏：基础 / 提高
    cw = (CW - Inches(0.5)) / 2
    # 基础
    card(s, M, M + Inches(1.3), cw, Inches(4.6), fill=WHITE, line=XIANG, line_w=2)
    textbox(s, M + Inches(0.3), M + Inches(1.45), cw - Inches(0.6), Inches(0.5),
            [{'text': '基础作业', 'size': 17, 'color': XIANG, 'bold': True, 'font': HEI}])
    bl = [{'text': '· ' + sanitize(ln.strip()), 'size': 14, 'color': INK, 'font': KAI,
           'line': 1.5, 'space_after': 7} for ln in base.split('\n') if ln.strip()]
    textbox(s, M + Inches(0.3), M + Inches(2.1), cw - Inches(0.6), Inches(3.6), bl)
    # 提高
    x2 = M + cw + Inches(0.5)
    card(s, x2, M + Inches(1.3), cw, Inches(4.6), fill=WHITE, line=GOLD, line_w=2)
    textbox(s, x2 + Inches(0.3), M + Inches(1.45), cw - Inches(0.6), Inches(0.5),
            [{'text': '提高作业', 'size': 17, 'color': GOLD, 'bold': True, 'font': HEI}])
    al = [{'text': '· ' + sanitize(ln.strip()), 'size': 14, 'color': INK, 'font': KAI,
           'line': 1.5, 'space_after': 7} for ln in adv.split('\n') if ln.strip()]
    textbox(s, x2 + Inches(0.3), M + Inches(2.1), cw - Inches(0.6), Inches(3.6), al)
    page_num(s, 8)
    return s

def s_summary(prs, lesson, research=None):
    s = blank(prs); bg(s)
    kicker(s, '总结 · 升华', color=GOLD)
    # 用研究富集的招牌升华，否则用目标/重点生成通用升华
    if research and research.get('signature'):
        textbox(s, M, M + Inches(1.4), CW, Inches(4.5),
                [{'text': research['signature'], 'size': 20, 'color': INK, 'font': KAI, 'line': 1.7}])
    else:
        objs = lesson.get('objectives') or []
        head = '本课落点'
        if objs:
            head = sanitize(objs[0][:20]) if isinstance(objs, list) else ''
        textbox(s, M, M + Inches(1.4), CW, Inches(1.0),
                [{'text': head, 'size': 22, 'color': INK, 'bold': True, 'font': HEI}])
        kps = split_numbered(lesson.get('keyPoints', ''))
        pl = [{'text': NUM[i] + ' ' + sanitize(kp), 'size': 17, 'color': MUTED, 'font': KAI,
               'line': 1.6, 'space_after': 10} for i, kp in enumerate(kps[:4])]
        textbox(s, M, M + Inches(2.6), CW, Inches(3.5), pl)
    summary_bar(s, '把课文读进自己：知识是别人的，理解才是你的', color=INK, text_color=GOLD, size=16)
    page_num(s, 9)
    return s

# ---------- 主入口 ----------
def render_lesson(lesson, out_path, photos=None, research=None, scale=1.0):
    """渲染单课为课堂学生版 PPTX。返回页码数。
    scale: 全局字号缩放（溢出自动修复时下调）。"""
    import _ppt_design as _D
    prev = _D.FONT_SCALE
    _D.FONT_SCALE = scale
    try:
        prs = make_prs()
        subj = lesson.get('subject', '语文')
        s_cover(prs, lesson, photos, research)
        s_objectives(prs, lesson)
        # 语文有作家作品页；其他学科用背景页（textbookAnalysis）
        s_background(prs, lesson, photos)
        s_keypoints(prs, lesson)
        s_difficulties(prs, lesson)
        s_process(prs, lesson)
        s_blackboard(prs, lesson)
        s_homework(prs, lesson)
        s_summary(prs, lesson, research)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        prs.save(out_path)
        return len(prs.slides._sldIdLst)
    finally:
        _D.FONT_SCALE = prev
