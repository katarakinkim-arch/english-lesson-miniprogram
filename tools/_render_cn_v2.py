# -*- coding: utf-8 -*-
"""渲染语文课《沁园春·长沙》16 页 v2 设计稿 + 素材附录，合成 PDF。
设计语言（与英语 pilot 的 v2 方向一致）：暖纸白底 + 墨蓝主字 + 克制陶土橙，
细线页眉页脚 + 左侧大细体数字标识栏 + 白卡片浮层 + 大量留白。
"""
import os, sys, re, json
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
BG     = (247, 245, 240)
INK    = (28, 43, 51)
SUB    = (96, 110, 117)
ACCENT = (194, 112, 61)
LINE   = (216, 209, 197)
CARD   = (255, 255, 255)
CARDL  = (226, 220, 208)
SOFT   = (238, 234, 226)
MUT_G  = (120, 150, 110)   # 亮点 墨绿
MUT_R  = (176, 92, 74)     # 难点 砖红
MUT_T  = (92, 138, 148)    # 衔接 墨青

# 参数化：sys.argv[1]=JSON路径, sys.argv[2]=输出目录(默认cn_preview)
_JSON_PATH = sys.argv[1] if len(sys.argv) > 1 else 'lesson_cn.json'
OUT       = sys.argv[2] if len(sys.argv) > 2 else 'cn_preview'

F_LIGHT  = ImageFont.truetype(r'C:/Windows/Fonts/msyhl.ttc', 30)
F_REG    = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 20)
F_REG_S  = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 16)
F_BOLD   = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 24)
F_BOLD_L = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 34)
F_TITLE  = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 46)
F_BIG    = ImageFont.truetype(r'C:/Windows/Fonts/msyhl.ttc', 150)
F_EN     = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 14)
F_SEC    = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 28)
F_CT     = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 22)
F_BM     = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 21)
F_SM     = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 15)

os.makedirs(OUT, exist_ok=True)
LESSON = json.load(open(_JSON_PATH, encoding='utf8'))
MEDIA = os.path.join('subpackages', 'cn', 'images', 'lessons', LESSON['id'], 'juzizhou.jpg')

def new():
    im = Image.new('RGB', (W, H), BG)
    return im, ImageDraw.Draw(im)

def text(d, xy, s, font, fill, anchor=None):
    if anchor == 'mm':
        w = d.textlength(s, font=font); h = font.size
        d.text((xy[0]-w/2, xy[1]-h/2), s, font=font, fill=fill)
    else:
        d.text(xy, s, font=font, fill=fill)

def header(d, left, right):
    text(d, (70, 44), left, F_EN, SUB)
    rw = d.textlength(right, font=F_EN)
    d.text((W-70-rw, 44), right, font=F_EN, fill=SUB)
    d.line([(70, 70), (W-70, 70)], fill=LINE, width=1)

def footer(d, code, page, total):
    d.line([(70, H-58), (W-70, H-58)], fill=LINE, width=1)
    text(d, (70, H-46), code, F_EN, SUB)
    p = f'{page:02d}  /  {total:02d}'
    pw = d.textlength(p, font=F_EN)
    d.text((W-70-pw, H-46), p, font=F_EN, fill=SUB)

def card(d, x, y, w, h, radius=10):
    d.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=CARD, outline=CARDL, width=1)

def wrap(d, s, font, max_w):
    lines = []
    for para in str(s).split('\n'):
        cur = ''
        for ch in para:
            if d.textlength(cur + ch, font=font) <= max_w:
                cur += ch
            else:
                lines.append(cur); cur = ch
        lines.append(cur)
    return lines

def left_rail(d, num, sub=''):
    text(d, (96, 120), num, F_BIG, (220, 216, 208))
    d.line([(182, 112), (182, 596)], fill=LINE, width=1)
    if sub:
        text(d, (212, 200), sub, F_REG_S, SUB)

def block(d, x, y, w, title, body, color=ACCENT, body_font=F_BM,
          max_lines=3, bar_w=5, title_font=F_CT, pad_x=26, pad_y=18):
    lines = wrap(d, body, body_font, w - 2*pad_x - bar_w)
    lines = lines[:max_lines] if max_lines else lines
    th = title_font.size
    bh = len(lines) * (body_font.size + 9)
    h = pad_y + th + 12 + bh + pad_y
    h = max(h, 64)
    card(d, x, y, w, h)
    d.rectangle([x, y, x+bar_w, y+h], fill=color)
    text(d, (x+bar_w+pad_x, y+pad_y), title, title_font, color)
    yy = y + pad_y + th + 14
    for ln in lines:
        text(d, (x+bar_w+pad_x, yy), ln, body_font, INK)
        yy += body_font.size + 9
    return y + h

# ---------- 解析 ----------
def cjk(s):
    return ''.join(re.findall(r'[一-鿿——·]+', s))

def parse_step(content):
    res = {'ppt': '', 'teacher': '', 'student': '', 'blackboard': '', 'diff': '', 'warn': ''}
    m = re.search(r'【(PPT[^】]*)】', content)
    if m:
        res['ppt'] = m.group(1)
        body = content[m.end():]
    else:
        body = content
    markers = ['教师：', '预设回答：', '板书时机：', '差异化提示：', '易错点提醒：']
    positions = []
    for mk in markers:
        i = body.find(mk)
        if i != -1:
            positions.append((i, mk))
    positions.sort()
    segs = {}
    for idx, (pos, mk) in enumerate(positions):
        start = pos + len(mk)
        end = positions[idx+1][0] if idx+1 < len(positions) else len(body)
        segs[mk] = body[start:end].strip()
    res['teacher'] = segs.get('教师：', '')
    res['student'] = segs.get('预设回答：', '')
    res['blackboard'] = segs.get('板书时机：', '')
    res['diff'] = segs.get('差异化提示：', '')
    res['warn'] = segs.get('易错点提醒：', '')
    return res

def parse_ex(text):
    res = {'basic': [], 'adv': [], 'answer': ''}
    m1 = text.find('【基础作业】'); m2 = text.find('【提高作业】'); m3 = text.find('【参考答案')
    if m1 == -1:
        return res
    basic = text[m1+len('【基础作业】'): m2 if m2 != -1 else (m3 if m3 != -1 else len(text))]
    adv = text[m2+len('【提高作业】'): m3 if m3 != -1 else len(text)] if m2 != -1 else ''
    ans = text[m3+len('【参考答案——教师用】'):] if m3 != -1 else ''
    res['basic'] = [l.strip().lstrip('0123456789.、') for l in basic.split('\n') if l.strip()]
    res['adv'] = [l.strip().lstrip('0123456789.、') for l in adv.split('\n') if l.strip()]
    res['answer'] = ans.strip()
    return res

def parse_ref(text):
    res = {'highlight': '', 'improve': '', 'next': ''}
    pos = []
    for mk, key in [('✅', 'highlight'), ('⚠', 'improve'), ('📌', 'next')]:
        i = text.find(mk)
        if i != -1:
            pos.append((i, key))
    pos.sort()
    for idx, (i, key) in enumerate(pos):
        j = i
        while j < len(text) and text[j] in '✅⚠📌 ':
            j += 1
        end = pos[idx+1][0] if idx+1 < len(pos) else len(text)
        res[key] = text[j:end].strip()
    return res

def clean_bb(s):
    # 去掉 ASCII/Unicode 制表框线，保留文字
    return re.sub(r'[┌┐└┘├┤┬┴┼─│]', ' ', s)

# ================= 封面 =================
def slide_cover():
    im, d = new()
    header(d, 'CHINESE  ·  人教版 2019', f"{LESSON['book']}  UNIT {LESSON['unitNumber']}")
    text(d, (96, 220), LESSON['title'].split('——')[0].strip(), F_TITLE, INK)
    text(d, (98, 296), '课文精读 · 第一课时', F_LIGHT, SUB)
    d.rectangle([98, 342, 98+86, 342+4], fill=ACCENT)
    text(d, (98, 376), '授课教师：_________      班级：__________', F_REG, SUB)
    # 右侧橘子洲实景图（真实媒体，手绘无 watermark）
    if os.path.exists(MEDIA):
        ph = Image.open(MEDIA).convert('RGB')
        pw, phh = 460, 300
        ph.thumbnail((pw, phh))
        card(d, W-70-pw, 150, pw, ph.height + 0, radius=12)
        d.rounded_rectangle([W-70-pw, 150, W-70, 150+ph.height], radius=12, outline=CARDL, width=1)
        im.paste(ph, (W-70-pw+2, 152))
        text(d, (W-70-pw+14, 150+ph.height+14), '橘子洲秋景 · 课前导入素材', F_REG_S, SUB)
    # 右下角单元标识框
    bx, by, bw, bh = W-300, 500, 210, 150
    d.rounded_rectangle([bx, by, bx+bw, by+bh], radius=12, outline=LINE, width=1)
    text(d, (bx+bw/2, by+54), f"U{LESSON['unitNumber']}", ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 58), (210, 206, 198), anchor='mm')
    text(d, (bx+bw/2, by+118), LESSON['unitTitle'], F_REG_S, SUB, anchor='mm')
    footer(d, LESSON['id'], 1, 16)
    im.save(f'{OUT}/slide_01_cover.png', 'PNG', optimize=True)

# ================= 目录 =================
def slide_contents():
    im, d = new()
    header(d, 'CONTENTS', f"{LESSON['book']}  UNIT {LESSON['unitNumber']}")
    text(d, (96, 130), '目录', F_BOLD_L, INK)
    items = [('01', '课程概览', 'Overview'), ('02', '学习目标', 'Objectives'),
             ('03', '重点 · 难点', 'Key & Difficult'), ('04', '教学过程', '6 Steps'),
             ('05', '板书设计', 'Blackboard'), ('06', '作业 · 反思', 'Homework & Notes')]
    x0, y0, cw, ch = 96, 210, 520, 150
    gx, gy = 40, 26
    for i, (n, zh, en) in enumerate(items):
        col = i % 2; row = i // 2
        x = x0 + col*(cw+gx); y = y0 + row*(ch+gy)
        card(d, x, y, cw, ch)
        d.rectangle([x, y, x+6, y+ch], fill=ACCENT)
        text(d, (x+34, y+34), n, ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 40), (222, 217, 209))
        text(d, (x+110, y+40), zh, F_BOLD, INK)
        text(d, (x+110, y+82), en, F_REG_S, SUB)
    footer(d, LESSON['id'], 2, 16)
    im.save(f'{OUT}/slide_02_contents.png', 'PNG', optimize=True)

# ================= 课程概览 =================
def slide_overview():
    im, d = new()
    header(d, 'OVERVIEW', '课程概览')
    text(d, (96, 120), '一、课程概览', F_BOLD_L, INK)
    # 左：学情分析
    lx, ly, lw, lh = 96, 180, 520, 480
    card(d, lx, ly, lw, lh, radius=12)
    d.rectangle([lx, ly, lx+lw, ly+56], fill=INK)
    text(d, (lx+28, ly+16), '学情分析', F_CT, (233, 237, 234))
    ov = re.sub(r'^【学情分析】', '', LESSON.get('overview', ''))
    y = ly + 80
    for ln in wrap(d, ov, F_REG, lw-56)[:14]:
        text(d, (lx+28, y), ln, F_REG, INK); y += 28
    # 右：教材分析
    rx, ry, rw, rh = 656, 180, 528, 480
    card(d, rx, ry, rw, rh, radius=12)
    d.rectangle([rx, ry, rx+rw, ry+56], fill=ACCENT)
    text(d, (rx+28, ry+16), '教材分析', F_CT, (255, 255, 255))
    y = ry + 80
    for ln in wrap(d, LESSON.get('textbookAnalysis', ''), F_REG, rw-56)[:15]:
        text(d, (rx+28, y), ln, F_REG, INK); y += 28
    footer(d, LESSON['id'], 3, 16)
    im.save(f'{OUT}/slide_03_overview.png', 'PNG', optimize=True)

# ================= 学习目标 =================
def slide_objectives():
    im, d = new()
    header(d, 'OBJECTIVES', '学习目标')
    text(d, (96, 120), '二、学习目标', F_BOLD_L, INK)
    objs = LESSON.get('objectives', [])
    cw, ch = 530, 220
    for i, o in enumerate(objs):
        name, _, desc = o.partition('：')
        col = i % 2; row = i // 2
        x = 96 + col*(cw+48); y = 190 + row*(ch+30)
        card(d, x, y, cw, ch)
        d.rectangle([x, y, x+6, y+ch], fill=ACCENT)
        text(d, (x+34, y+26), f'0{i+1}', ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 30), (222, 217, 209))
        text(d, (x+110, y+30), name, F_BOLD, ACCENT)
        yy = y + 78
        for ln in wrap(d, desc, F_REG, cw-60)[:4]:
            text(d, (x+34, yy), ln, F_REG, INK); yy += 27
    footer(d, LESSON['id'], 4, 16)
    im.save(f'{OUT}/slide_04_objectives.png', 'PNG', optimize=True)

# ================= 重点·难点 =================
def slide_keypoints():
    im, d = new()
    header(d, 'KEY & DIFFICULT', '重点 · 难点')
    # 重点（左，墨绿）
    lx, ly, lw, lh = 96, 180, 520, 480
    card(d, lx, ly, lw, lh, radius=12)
    d.rectangle([lx, ly, lx+lw, ly+56], fill=MUT_G)
    text(d, (lx+28, ly+16), '教学重点', F_CT, (255, 255, 255))
    y = ly + 84
    for it in LESSON.get('keyPoints', '').split('\n'):
        it = it.strip()
        if not it:
            continue
        text(d, (lx+30, y), it[:1], F_BOLD, MUT_G)
        for k, ln in enumerate(wrap(d, it[1:].strip(), F_REG, lw-80)[:3]):
            text(d, (lx+72, y+k*27), ln, F_REG, INK)
        y += 27 * (min(3, len(wrap(d, it[1:].strip(), F_REG, lw-80))) or 1) + 14
    # 难点（右，砖红）
    rx, ry, rw, rh = 656, 180, 528, 480
    card(d, rx, ry, rw, rh, radius=12)
    d.rectangle([rx, ry, rx+rw, ry+56], fill=MUT_R)
    text(d, (rx+28, ry+16), '教学难点', F_CT, (255, 255, 255))
    y = ry + 84
    for it in LESSON.get('difficulties', '').split('\n'):
        it = it.strip()
        if not it:
            continue
        text(d, (rx+30, y), it[:1], F_BOLD, MUT_R)
        for k, ln in enumerate(wrap(d, it[1:].strip(), F_REG, rw-80)[:3]):
            text(d, (rx+72, y+k*27), ln, F_REG, INK)
        y += 27 * (min(3, len(wrap(d, it[1:].strip(), F_REG, rw-80))) or 1) + 14
    footer(d, LESSON['id'], 5, 16)
    im.save(f'{OUT}/slide_05_keypoints.png', 'PNG', optimize=True)

# ================= 教学过程 6 步 =================
def slide_step(num, total, step, content, page_id):
    im, d = new()
    header(d, f'STEP {num:02d} / {total:02d}', '教学过程')
    left_rail(d, f'{num:02d}')
    # 主标题
    text(d, (212, 150), step, F_BOLD_L, INK)
    p = parse_step(content)
    # ppt 标签 chip
    if p['ppt']:
        chip = f'PPT {p["ppt"].replace("PPT ", "")}'
        cw_chip = d.textlength(chip, font=F_REG_S) + 28
        d.rounded_rectangle([212, 200, 212+cw_chip, 232], radius=15, fill=SOFT, outline=LINE, width=1)
        text(d, (226, 209), chip, F_REG_S, SUB)
    # 2x2 网格：4 个块
    BW = 500
    GAP = 18
    y1 = 260
    y2 = y1 + 145 + GAP
    block(d, 212,        y1, BW, '教学指令', p.get('teacher') or p.get('activity',''), ACCENT, max_lines=3)
    block(d, 212+BW+20,  y1, BW, '学生预设', p['student'], MUT_T, max_lines=2)
    block(d, 212,        y2, BW, '分层指导', p['diff'], MUT_G, max_lines=2)
    block(d, 212+BW+20,  y2, BW, '易错提醒', p['warn'], MUT_R, max_lines=3)
    # 板书时机 一行
    by = H - 100
    d.line([(212, by-8), (1212, by-8)], fill=LINE, width=1)
    text(d, (212, by), '板书时机', F_REG_S, ACCENT)
    if p['blackboard']:
        for k, ln in enumerate(wrap(d, p['blackboard'], F_REG_S, 900)[:1]):
            text(d, (300, by), ln, F_REG_S, SUB)
    footer(d, LESSON['id'], page_id, 16)
    im.save(f'{OUT}/slide_{page_id:02d}_step{num}.png', 'PNG', optimize=True)

# ================= 板书设计 =================
def slide_blackboard():
    im, d = new()
    header(d, 'BLACKBOARD', '板书设计')
    bx, by, bw, bh = 96, 130, 1088, 520
    d.rounded_rectangle([bx, by, bx+bw, by+bh], radius=14, fill=INK)
    text(d, (bx+40, by+30), '沁园春 · 长沙  —  板书结构', ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 26), (233, 237, 234))
    d.line([(bx+40, by+74), (bx+bw-40, by+74)], fill=(70, 86, 94), width=1)
    bb = clean_bb(LESSON.get('blackboard', ''))
    yy = by + 92
    line_count = 0
    for ln in bb.split('\n'):
        ln = ln.rstrip()
        if not ln.strip():
            yy += 10; continue
        if yy > H - 80 or line_count > 13:   # 截断防溢出
            break
        color = (220, 226, 222)
        text(d, (bx+40, yy), ln, F_REG, color)
        yy += 30
        line_count += 1
    footer(d, LESSON['id'], 12, 16)
    im.save(f'{OUT}/slide_12_blackboard.png', 'PNG', optimize=True)

# ================= 作业·基础 =================
def slide_homework_basic():
    im, d = new()
    header(d, 'HOMEWORK', '作业布置 · 基础')
    text(d, (96, 120), '七、基础作业', F_BOLD_L, INK)
    ex = parse_ex(LESSON.get('exercises', ''))
    cw, ch = 1088, 470
    card(d, 96, 200, cw, ch, radius=12)
    d.rectangle([96, 200, 96+cw, 256], fill=MUT_G)
    text(d, (124, 216), '基础 · 必做', F_CT, (255, 255, 255))
    y = 290
    for it in ex['basic'][:4]:
        d.ellipse([124, y+6, 134, y+16], fill=MUT_G)
        for k, ln in enumerate(wrap(d, it, F_REG, cw-90)[:2]):
            text(d, (150, y), ln, F_REG, INK); y += 27
        y += 14
    footer(d, LESSON['id'], 13, 16)
    im.save(f'{OUT}/slide_13_homework_basic.png', 'PNG', optimize=True)

# ================= 作业·提高 + 答案 =================
def slide_homework_adv():
    im, d = new()
    header(d, 'HOMEWORK', '作业布置 · 提高')
    text(d, (96, 120), '八、提高作业 · 参考答案', F_BOLD_L, INK)
    ex = parse_ex(LESSON.get('exercises', ''))
    cw, ch = 1088, 470
    card(d, 96, 200, cw, ch, radius=12)
    d.rectangle([96, 200, 96+cw, 256], fill=ACCENT)
    text(d, (124, 216), '提高 · 选做 + 教师参考', F_CT, (255, 255, 255))
    y = 290
    for it in ex['adv'][:3]:
        d.ellipse([124, y+6, 134, y+16], fill=ACCENT)
        for k, ln in enumerate(wrap(d, it, F_REG, cw-90)[:2]):
            text(d, (150, y), ln, F_REG, INK); y += 27
        y += 10
    y += 6
    # 参考答案
    d.rounded_rectangle([124, y, 96+cw-28, y+34], radius=6, fill=SOFT, outline=LINE, width=1)
    text(d, (140, y+6), '参考答案（教师用）', F_REG_S, ACCENT)
    y += 44
    for ln in wrap(d, ex['answer'], F_REG_S, cw-120)[:5]:
        text(d, (140, y), ln, F_REG_S, SUB); y += 24
    footer(d, LESSON['id'], 14, 16)
    im.save(f'{OUT}/slide_14_homework_adv.png', 'PNG', optimize=True)

# ================= 教学反思 =================
def slide_reflection():
    im, d = new()
    header(d, 'REFLECTION', '教学反思')
    text(d, (96, 120), '九、教学反思', F_BOLD_L, INK)
    rf = parse_ref(LESSON.get('reflection', ''))
    blocks = [('亮点', rf['highlight'], MUT_G), ('需改进', rf['improve'], MUT_R), ('下节课衔接', rf['next'], MUT_T)]
    cw = 360
    for i, (title, body, color) in enumerate(blocks):
        x = 96 + i*(cw+24)
        card(d, x, 190, cw, 460, radius=12)
        d.rectangle([x, 190, x+cw, 246], fill=color)
        text(d, (x+28, 206), title, F_CT, (255, 255, 255))
        y = 280
        for ln in wrap(d, body, F_REG, cw-56)[:13]:
            text(d, (x+28, y), ln, F_REG, INK); y += 27
    footer(d, LESSON['id'], 15, 16)
    im.save(f'{OUT}/slide_15_reflection.png', 'PNG', optimize=True)

# ================= 课堂小结 =================
def slide_summary():
    im, d = new()
    header(d, 'SUMMARY', '课堂小结')
    text(d, (96, 150), '课堂小结', F_TITLE, INK)
    text(d, (98, 220), 'Summary · 读诗四步法与青春担当', F_LIGHT, SUB)
    objs = LESSON.get('objectives', [])
    y = 280
    for i, o in enumerate(objs):
        name, _, desc = o.partition('：')
        text(d, (120, y), f'0{i+1}', F_BOLD, ACCENT)
        text(d, (180, y), name, F_BOLD, INK)
        for k, ln in enumerate(wrap(d, desc, F_REG, 980)[:1]):
            text(d, (180, y+30), ln, F_REG, SUB)
        y += 68
    # 右下角读法（缩短高度，避免与 04 重叠）
    bx, by, bw, bh = 800, 600, 400, 56
    d.rounded_rectangle([bx, by, bx+bw, by+bh], radius=10, fill=INK)
    text(d, (bx+22, by+8), '读诗四步法', F_REG_S, (233, 237, 234))
    text(d, (bx+120, by+8), '圈意象→标特征→串联画面→推导情感', F_REG_S, (200, 210, 206))
    footer(d, LESSON['id'], 16, 16)
    im.save(f'{OUT}/slide_16_summary.png', 'PNG', optimize=True)

# ================= 素材附录 =================
def slide_appendix():
    im, d = new()
    header(d, 'APPENDIX', '素材图示')
    text(d, (96, 130), '素材图示（真实图片）', F_BOLD_L, INK)
    text(d, (98, 178), '课前导入 / 上阕精读 用 · 橘子洲秋景（手绘无水印）', F_REG_S, SUB)
    if os.path.exists(MEDIA):
        ph = Image.open(MEDIA).convert('RGB')
        ph.thumbnail((760, 470))
        x = (W - ph.width) // 2
        card(d, x-8, 220, ph.width+16, ph.height+16, radius=12)
        im.paste(ph, (x, 228))
    footer(d, LESSON['id'], 17, 17)
    im.save(f'{OUT}/slide_17_appendix.png', 'PNG', optimize=True)

# -------- 生成全部 --------
slide_cover()
slide_contents()
slide_overview()
slide_objectives()
slide_keypoints()
for i, st in enumerate(LESSON.get('process', [])[:6]):
    slide_step(i+1, 6, st['step'], st['content'], 6+i)
slide_blackboard()
slide_homework_basic()
slide_homework_adv()
slide_reflection()
slide_summary()
slide_appendix()

print('语文 v2 设计稿已生成:', sorted(os.listdir(OUT)))
print('共', len(os.listdir(OUT)), '页')
