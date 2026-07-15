"""
用 PIL 直接渲染 16 页 1280×720 高质量 PNG 排版设计稿。
排版原则：
- 教育蓝主色 (#2563EB) + 暖橙强调 (#FB923C) + 浅蓝辅助 (#DBEAFE) + 深蓝灰文字 (#1E293B)
- 大量留白、大字号、卡片化、图标化
- 真实上课 PPT 质感（不是单调标题+正文）
"""
import os, math, re
from PIL import Image, ImageDraw, ImageFont

OUT = r'C:\Users\1\WorkBuddy\2026-07-08-15-47-48\miniprogram\design_preview'
os.makedirs(OUT, exist_ok=True)

# 调色板
PRIM = (37, 99, 235)        # 教育蓝
PRIM_DK = (29, 78, 216)
ACCENT = (251, 146, 60)     # 暖橙
ACCENT_DK = (234, 88, 12)
LIGHT = (219, 234, 254)     # 浅蓝
PALE = (239, 246, 255)      # 更浅蓝
GREEN = (34, 197, 94)       # 绿（重点）
GREEN_LT = (220, 252, 231)
RED = (220, 38, 38)         # 红（难点）
RED_LT = (254, 226, 226)
DARK = (30, 41, 59)         # 文字主色
GRAY = (100, 116, 139)      # 次要文字
GRAY_LT = (148, 163, 184)
BG = (248, 250, 252)        # 页面底色
WHITE = (255, 255, 255)
BORDER = (226, 232, 240)

W, H = 1280, 720

# 字体
F_TITLE = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 48)
F_SUBTITLE = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 24)
F_BODY = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 20)
F_BODY_S = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 18)
F_BIG_NUM = ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 72)
F_NUM = ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 36)
F_CARD_TITLE = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 26)
F_LABEL = ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 18)
F_SMALL = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 16)
F_ICON = ImageFont.truetype(r'C:/Windows/Fonts/seguisb.ttf', 32)

# emoji 替换表（系统字体无 emoji 渲染，全部改为纯文本前缀）
EMOJI_REPLACE = {
    '🎯': '01',
    '🌏': '02',
    '🌍': '02',
    '💡': '03',
    '📘': '04',
    '✅': '+',
    '⚠️': '!',
    '⚠': '!',
    '📌': '★',
    '⚡': '★',
    '📖': '01',
    '📚': '02',
    '🎧': '03',
    '🗣': '04',
    '📝': '05',
    '✏️': '06',
    '🔑': '★',
    '🔖': '★',
    '📍': '★',
    '⏱': '时间',
    '💬': '台词',
    '🎒': '学情',
    '✓': '+',
    '☑': '+',
    '◆': '+',
    '▶': '>',
    '▍': '|',
    '◆': '+',
    '●': '.',
    '→': '->',
    '←': '<-',
    '↑': '^',
    '↓': 'v',
    '─': '-',
    '━': '-',
    '│': '|',
    '┌': '+',
    '┐': '+',
    '└': '+',
    '┘': '+',
    '├': '+',
    '┤': '+',
    '┬': '+',
    '┴': '+',
    '┼': '+',
}
import re
def deemoji(s):
    out = []
    for ch in s:
        out.append(EMOJI_REPLACE.get(ch, ch))
    return ''.join(out)

# monkey-patch：让所有 d.text() 第一个字符串参数自动 deemoji
_orig_text = ImageDraw.ImageDraw.text
def _patched_text(self, xy, text, *a, **kw):
    if isinstance(text, str):
        text = deemoji(text)
    return _orig_text(self, xy, text, *a, **kw)
ImageDraw.ImageDraw.text = _patched_text

def new_page():
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    # 顶部品牌条
    d.rectangle([0, 0, W, 8], fill=PRIM)
    # 底部页脚
    d.rectangle([0, H-32, W, H], fill=WHITE)
    d.line([(0, H-32), (W, H-32)], fill=BORDER, width=1)
    return im, d

def footer(d, page_num, total, lesson_id):
    d.text((40, H-26), f'人教版 2019 · 高中英语必修一 · Travelling Around', font=F_SMALL, fill=GRAY)
    d.text((W-180, H-26), f'{page_num:02d} / {total:02d}  ·  {lesson_id}', font=F_SMALL, fill=GRAY)

def title_bar(d, title, kicker=None):
    """页面顶部标题区：左侧色块 + 主标题 + 副标题"""
    # 左侧大色块
    d.rectangle([0, 8, 16, H-32], fill=PRIM)
    # 主标题
    d.text((60, 38), title, font=F_TITLE, fill=DARK)
    if kicker:
        d.text((60, 100), kicker, font=F_SUBTITLE, fill=GRAY)

def wrap_text(d, text, font, max_w):
    """文本按像素宽度换行"""
    lines = []
    for para in text.split('\n'):
        cur = ''
        for ch in para:
            if d.textlength(cur + ch, font=font) <= max_w:
                cur += ch
            else:
                lines.append(cur)
                cur = ch
        if cur:
            lines.append(cur)
    return lines

def bullet(d, x, y, text, font, color=DARK, w=400, gap=4):
    """带圆点项目符号的列表"""
    # 圆点
    d.ellipse([x, y+8, x+10, y+18], fill=PRIM)
    text_x = x + 22
    for line in wrap_text(d, text, font, w - 22):
        d.text((text_x, y), line, font=font, fill=color)
        y += font.size + gap
    return y

# ============================================================
# Slide 1: 封面
# ============================================================
def slide1():
    im, d = new_page()
    # 左侧大色块（占 45% 宽）
    d.rectangle([0, 8, 580, H-32], fill=PRIM)
    # 色块内的几何装饰
    d.ellipse([40, 80, 220, 260], fill=(255,255,255,30) if False else PRIM_DK)
    d.ellipse([400, 480, 580, 660], fill=PRIM_DK)
    d.polygon([(440, 120), (520, 120), (480, 60)], fill=ACCENT)
    # 学科徽标
    d.rounded_rectangle([40, 60, 180, 100], radius=8, fill=WHITE)
    d.text((62, 67), '高中英语', font=F_LABEL, fill=PRIM)
    # 教材版本
    d.text((40, 200), '人教版 2019 统编版', font=F_SUBTITLE, fill=WHITE)
    d.text((40, 240), '必修第一册', font=F_SUBTITLE, fill=WHITE)
    # 单元标签
    d.rounded_rectangle([40, 320, 220, 360], radius=20, fill=ACCENT)
    d.text((68, 330), 'UNIT 2', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 22), fill=WHITE)
    # 主标题（白色）
    d.text((40, 400), 'Travelling Around', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 56), fill=WHITE)
    d.text((40, 470), '旅  行  随  笔', font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 40), fill=WHITE)
    # 课时类型
    d.rounded_rectangle([40, 540, 240, 580], radius=18, fill=WHITE)
    d.text((72, 548), '听说课 · 第 1 课时', font=F_LABEL, fill=PRIM)
    # 右侧白色区域：核心信息
    d.text((640, 120), 'TEACHER', font=F_LABEL, fill=GRAY)
    d.text((640, 148), '备课教师：高二英语组', font=F_BODY, fill=DARK)
    d.text((640, 200), 'CLASS', font=F_LABEL, fill=GRAY)
    d.text((640, 228), '授课对象：高一 (5) 班', font=F_BODY, fill=DARK)
    d.text((640, 280), 'DURATION', font=F_LABEL, fill=GRAY)
    d.text((640, 308), '课时长度：45 分钟', font=F_BODY, fill=DARK)
    # 信息卡片
    d.rounded_rectangle([620, 360, 1200, 480], radius=12, fill=PALE, outline=BORDER, width=1)
    d.text((640, 380), '🔖 单元主题', font=F_LABEL, fill=PRIM)
    d.text((640, 410), '探索世界 · 介绍旅行经历', font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 22), fill=DARK)
    # 底部 logo / 标识
    d.text((640, 520), '教案系统 · Mini Lesson', font=F_LABEL, fill=GRAY)
    d.text((640, 560), '微信小程序端生成', font=F_SMALL, fill=GRAY_LT)
    # footer
    footer(d, 1, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_01_cover.png'), 'PNG', optimize=True)

# ============================================================
# Slide 2: 目录
# ============================================================
def slide2():
    im, d = new_page()
    title_bar(d, '目  录  CONTENTS', kicker='六大环节 · 完整教学流程')
    items = [
        ('01', '课程概览', '学情 · 教材 · 目标', PRIM, PALE),
        ('02', '学习目标', '四项核心能力', ACCENT, (254, 243, 199)),
        ('03', '教学重点 / 难点', '关键知识 · 易错提示', GREEN, GREEN_LT),
        ('04', '教学准备', 'PPT · 教具 · 音频素材', (168, 85, 247), (243, 232, 255)),
        ('05', '教学过程', '6 步教学法 · 完整剧本', (236, 72, 153), (252, 231, 243)),
        ('06', '板书 · 作业 · 反思', '课堂成果 + 课后延伸', (14, 165, 233), (224, 242, 254)),
    ]
    # 3x2 网格
    cw, ch = 380, 240
    gap = 24
    x0, y0 = 60, 170
    for i, (num, name, desc, color, bg) in enumerate(items):
        col, row = i % 3, i // 3
        x = x0 + col * (cw + gap)
        y = y0 + row * (ch + gap)
        d.rounded_rectangle([x, y, x+cw, y+ch], radius=14, fill=WHITE, outline=BORDER, width=1)
        # 左侧色条
        d.rectangle([x, y, x+8, y+ch], fill=color)
        # 大数字
        d.ellipse([x+30, y+30, x+130, y+130], fill=bg, outline=color, width=2)
        d.text((x+45, y+50), num, font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 50), fill=color)
        # 名称+描述
        d.text((x+30, y+150), name, font=F_CARD_TITLE, fill=DARK)
        d.text((x+30, y+190), desc, font=F_BODY_S, fill=GRAY)
    footer(d, 2, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_02_contents.png'), 'PNG', optimize=True)

# ============================================================
# Slide 3: 课程概览 + 学情
# ============================================================
def slide3():
    im, d = new_page()
    title_bar(d, '一、课程概览', kicker='Course Overview · 学情 + 教材分析')
    # 左卡：学情分析
    d.rounded_rectangle([60, 170, 620, 670], radius=14, fill=WHITE, outline=BORDER, width=1)
    d.rounded_rectangle([60, 170, 620, 220], radius=14, fill=PRIM)
    d.rectangle([60, 200, 620, 220], fill=PRIM)
    d.text((90, 183), '学  情  分  析', font=F_CARD_TITLE, fill=WHITE)
    y = 250
    d.text((90, y), '▍A 班（创新班）', font=F_LABEL, fill=PRIM); y += 30
    y = bullet(d, 90, y, '英语基础扎实，听说读写均衡发展', F_BODY_S, DARK, w=480)
    y = bullet(d, 90, y, '已掌握一般现在时、现在进行时', F_BODY_S, DARK, w=480)
    y += 20
    d.text((90, y), '▍B 班（平行班）', font=F_LABEL, fill=ACCENT); y += 30
    y = bullet(d, 90, y, '约 60% 学生词汇量偏少', F_BODY_S, DARK, w=480)
    y = bullet(d, 90, y, '听力材料需慢速 + 文字稿辅助', F_BODY_S, DARK, w=480)
    y += 20
    d.text((90, y), '▍共性问题', font=F_LABEL, fill=GREEN); y += 30
    y = bullet(d, 90, y, '机场/旅行场景词汇与表达陌生', F_BODY_S, DARK, w=480)
    # 右卡：教材分析
    d.rounded_rectangle([660, 170, 1220, 670], radius=14, fill=WHITE, outline=BORDER, width=1)
    d.rounded_rectangle([660, 170, 1220, 220], radius=14, fill=ACCENT)
    d.rectangle([660, 200, 1220, 220], fill=ACCENT)
    d.text((690, 183), '教  材  分  析', font=F_CARD_TITLE, fill=WHITE)
    y = 250
    d.text((690, y), '📖 语篇类型', font=F_LABEL, fill=ACCENT); y += 30
    y = bullet(d, 690, y, 'Listening & Speaking 听说课', F_BODY_S, DARK, w=480)
    y += 10
    d.text((690, y), '🎯 核心话题', font=F_LABEL, fill=ACCENT); y += 30
    y = bullet(d, 690, y, 'Travelling Around 旅行相关', F_BODY_S, DARK, w=480)
    y += 10
    d.text((690, y, ), '📚 语料来源', font=F_LABEL, fill=ACCENT); y += 30
    y = bullet(d, 690, y, '课本 P5 表格 + P6 对话 + 听力音频', F_BODY_S, DARK, w=480)
    y += 10
    d.text((690, y), '⏱ 课时安排', font=F_LABEL, fill=ACCENT); y += 30
    y = bullet(d, 690, y, '1 课时 = 45 分钟', F_BODY_S, DARK, w=480)
    footer(d, 3, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_03_overview.png'), 'PNG', optimize=True)

# ============================================================
# Slide 4: 学习目标（4 卡片）
# ============================================================
def slide4():
    im, d = new_page()
    title_bar(d, '二、学习目标', kicker='四项核心素养 · 高中英语学科能力')
    # 4 个角分布
    targets = [
        ('🎯', '语言能力', '听懂旅行场景对话，准确提取 5 个关键信息', PRIM, PALE),
        ('🌏', '文化意识', '了解英语国家旅行礼仪与表达习惯', ACCENT, (254, 243, 199)),
        ('💡', '思维品质', '通过比较中外旅行方式，培养批判性思维', GREEN, GREEN_LT),
        ('📘', '学习能力', '掌握"预测—听中—听后"三段听力策略', (168, 85, 247), (243, 232, 255)),
    ]
    cw, ch = 580, 230
    coords = [(60, 170), (640, 170), (60, 420), (640, 420)]
    for (emoji, name, desc, color, bg), (x, y) in zip(targets, coords):
        d.rounded_rectangle([x, y, x+cw, y+ch], radius=14, fill=WHITE, outline=BORDER, width=1)
        # 左侧图标圆
        d.ellipse([x+24, y+24, x+108, y+108], fill=bg, outline=color, width=2)
        d.text((x+42, y+38), emoji, font=ImageFont.truetype(r'C:/Windows/Fonts/seguisb.ttf', 44), fill=DARK)
        # 名称
        d.text((x+140, y+34), name, font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 30), fill=color)
        # 描述
        for i, line in enumerate(wrap_text(d, desc, F_BODY, cw-160)):
            d.text((x+140, y+90+i*(F_BODY.size+6)), line, font=F_BODY, fill=DARK)
    footer(d, 4, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_04_objectives.png'), 'PNG', optimize=True)

# ============================================================
# Slide 5: 教学重点 / 难点
# ============================================================
def slide5():
    im, d = new_page()
    title_bar(d, '三、教学重点 / 难点', kicker='Key Points & Difficulties')
    # 重点（左，绿色）
    d.rounded_rectangle([60, 170, 620, 670], radius=14, fill=WHITE, outline=GREEN, width=2)
    d.rounded_rectangle([60, 170, 620, 230], radius=14, fill=GREEN)
    d.rectangle([60, 210, 620, 230], fill=GREEN)
    d.text((90, 185), '✓  教  学  重  点', font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 32), fill=WHITE)
    y = 270
    items_zd = [
        ('①', '掌握机场/旅行场景核心词汇 12 个'),
        ('②', '听懂两段听力材料的关键信息'),
        ('③', '能用 5 句话介绍旅行计划'),
    ]
    for num, txt in items_zd:
        d.ellipse([90, y, 132, y+42], fill=GREEN_LT, outline=GREEN, width=2)
        d.text((100, y+5), num, font=F_NUM, fill=GREEN)
        for i, line in enumerate(wrap_text(d, txt, F_BODY, 420)):
            d.text((155, y+8+i*(F_BODY.size+4)), line, font=F_BODY, fill=DARK)
        y += 90
    # 难点（右，红色）
    d.rounded_rectangle([660, 170, 1220, 670], radius=14, fill=WHITE, outline=RED, width=2)
    d.rounded_rectangle([660, 170, 1220, 230], radius=14, fill=RED)
    d.rectangle([660, 210, 1220, 230], fill=RED)
    d.text((690, 185), '⚠  教  学  难  点', font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 32), fill=WHITE)
    y = 270
    items_nd = [
        ('①', 'flight / flat / fright 同音区分'),
        ('②', '快速听力中数字、时间、地点的捕捉'),
        ('③', '一般将来时在口语中的自然运用'),
    ]
    for num, txt in items_nd:
        d.ellipse([690, y, 732, y+42], fill=RED_LT, outline=RED, width=2)
        d.text((700, y+5), num, font=F_NUM, fill=RED)
        for i, line in enumerate(wrap_text(d, txt, F_BODY, 420)):
            d.text((755, y+8+i*(F_BODY.size+4)), line, font=F_BODY, fill=DARK)
        y += 90
    # 底部易错点提醒
    d.rounded_rectangle([60, 640, 1220, 680], radius=8, fill=(255, 247, 224), outline=(251, 191, 36), width=1)
    d.text((90, 650), '⚡ 易错点提醒：', font=F_LABEL, fill=(180, 83, 9))
    d.text((230, 652), 'flight（航班） ≠ flat（公寓） ≠ fright（害怕），听写时务必根据语境判断', font=F_BODY_S, fill=DARK)
    footer(d, 5, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_05_keypoints.png'), 'PNG', optimize=True)

# ============================================================
# Slide 6-11: 教学过程（6 步）
# ============================================================
def step_page(num, total, title, content_blocks, color, page_id):
    assert total == 6, 'step_page 固定 total=6'
    im, d = new_page()
    # 顶部左侧大数字（圆形）
    d.ellipse([40, 50, 180, 190], fill=color)
    d.text((78, 70), f'{num:02d}', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 76), fill=WHITE)
    # 标题
    d.text((220, 70), title, font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 36), fill=DARK)
    d.text((220, 122), f'教学过程 · 步骤 {num}/{total}', font=F_SUBTITLE, fill=GRAY)
    # 右侧进度条
    bar_w = 380
    d.rounded_rectangle([860, 90, 860+bar_w, 110], radius=10, fill=BORDER)
    d.rounded_rectangle([860, 90, 860+int(bar_w*num/total), 110], radius=10, fill=color)
    d.text((860+bar_w+10, 86), f'{num}/{total}', font=F_LABEL, fill=GRAY)
    # 内容区
    y = 210
    for block in content_blocks:
        btype, btitle, bbody, bcolor = block
        # 块标题
        d.rounded_rectangle([60, y, 1220, y+34], radius=8, fill=bcolor)
        d.text((78, y+5), btitle, font=F_LABEL, fill=WHITE)
        y += 50
        # 块内容
        for line in wrap_text(d, bbody, F_BODY, 1140):
            d.text((80, y), line, font=F_BODY, fill=DARK)
            y += F_BODY.size + 6
        y += 16
    footer(d, page_id, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, f'slide_{page_id:02d}_step{num}.png'), 'PNG', optimize=True)

# ============================================================
# Slide 12: 板书
# ============================================================
def slide12():
    im, d = new_page()
    title_bar(d, '六、板书设计', kicker='Blackboard Layout · 课堂实时书写')
    # 左侧：板书框（黑底白字模拟）
    d.rounded_rectangle([60, 170, 760, 670], radius=8, fill=(28, 36, 52))
    # 板书标题条
    d.rectangle([60, 170, 760, 220], fill=(40, 52, 78))
    d.text((90, 180), 'BLACKBOARD  ·  Travelling Around', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 20), fill=WHITE)
    # 板书内容（黄色粉笔字）
    chalk = (255, 235, 130)
    chalk2 = (200, 220, 255)
    f_chalk = ImageFont.truetype(r'C:/Windows/Fonts/consolab.ttf', 22)
    f_chalk_lg = ImageFont.truetype(r'C:/Windows/Fonts/consolab.ttf', 28)
    y = 240
    d.text((90, y), '◆ Topic: Travelling Around', font=f_chalk_lg, fill=chalk); y += 38
    d.text((90, y), '◆ Key Vocabulary (12):', font=f_chalk_lg, fill=chalk); y += 34
    vocab = ['passport / visa / boarding pass', 'suitcase / map / camera', 'flight / gate / seat', 'check in / take off / land']
    for v in vocab:
        d.text((120, y), f'· {v}', font=f_chalk, fill=chalk2); y += 28
    y += 8
    d.text((90, y), '◆ Sentence Pattern:', font=f_chalk_lg, fill=chalk); y += 34
    d.text((120, y), '"I am travelling to ___ next ___."', font=f_chalk, fill=chalk2); y += 28
    d.text((120, y), '"Have you ever ___?"', font=f_chalk, fill=chalk2); y += 28
    # 右侧：板书要点说明
    d.rounded_rectangle([800, 170, 1220, 670], radius=14, fill=WHITE, outline=BORDER, width=1)
    d.rounded_rectangle([800, 170, 1220, 220], radius=14, fill=PRIM)
    d.rectangle([800, 200, 1220, 220], fill=PRIM)
    d.text((830, 183), '板 书 要 点', font=F_CARD_TITLE, fill=WHITE)
    y = 250
    descs = [
        '① 板书时机：讲完词汇、引入对话时书写',
        '② 粉笔颜色：主标题用黄色、解释用白色',
        '③ 留白原则：右下角 1/3 留作学生补充',
        '④ 板书时长：贯穿全程，不一次性写完',
    ]
    for desc in descs:
        d.text((830, y), desc, font=F_BODY, fill=DARK); y += 50
    # 提示
    d.rounded_rectangle([830, 540, 1190, 640], radius=10, fill=(255, 247, 224), outline=(251, 191, 36), width=1)
    d.text((850, 555), '⚡ 课堂提示', font=F_LABEL, fill=(180, 83, 9))
    for i, line in enumerate(wrap_text(d, '板书分三次完成：导入时写主题、词汇时写词块、对话时写句型', F_BODY_S, 340)):
        d.text((850, 585+i*(F_BODY_S.size+4)), line, font=F_BODY_S, fill=DARK)
    footer(d, 12, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_12_blackboard.png'), 'PNG', optimize=True)

# ============================================================
# Slide 13: 基础作业
# ============================================================
def slide13():
    im, d = new_page()
    title_bar(d, '七、作业布置 · 基础层', kicker='Homework · 必做 · 巩固词汇 + 句型')
    # 作业卡片
    d.rounded_rectangle([60, 170, 1220, 670], radius=14, fill=WHITE, outline=BORDER, width=1)
    d.rounded_rectangle([60, 170, 1220, 220], radius=14, fill=GREEN)
    d.rectangle([60, 200, 1220, 220], fill=GREEN)
    d.text((90, 183), '📝  基础作业  (必做 · 15 分钟)', font=F_CARD_TITLE, fill=WHITE)
    d.text((900, 185), 'A 班 + B 班', font=F_LABEL, fill=WHITE)
    # 三道题
    qs = [
        ('一、', '单词拼写', '根据中文写出英文，每空一词。\n1. 护照 ________  2. 登机牌 ________  3. 行李箱 ________\n4. 航班 ________  5. 起飞 ________  6. 降落 ________'),
        ('二、', '句型转换', '根据提示完成句子。\n1. I will travel to Paris. (改为一般疑问句)\n2. He has never been to Tokyo. (对 Tokyo 提问)\n3. They are going to take a flight. (对 a flight 提问)'),
        ('三、', '听力复述', '重听 P6 听力材料，用自己的话复述对话大意（不少于 50 词）。'),
    ]
    y = 250
    for num, title, body in qs:
        d.rounded_rectangle([90, y, 1190, y+34], radius=6, fill=PALE)
        d.text((110, y+5), f'{num} {title}', font=F_LABEL, fill=PRIM)
        y += 44
        for line in body.split('\n'):
            for sub in wrap_text(d, line, F_BODY, 1080):
                d.text((110, y), sub, font=F_BODY, fill=DARK); y += F_BODY.size + 4
        y += 16
    # 提交方式
    d.rounded_rectangle([60, 640, 1220, 680], radius=8, fill=(239, 246, 255), outline=PRIM, width=1)
    d.text((90, 650), '📌 提交方式：', font=F_LABEL, fill=PRIM)
    d.text((230, 652), '拍照上传至班级小管家，截止时间：明日 08:00', font=F_BODY_S, fill=DARK)
    footer(d, 13, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_13_homework_basic.png'), 'PNG', optimize=True)

# ============================================================
# Slide 14: 提高作业 + 参考答案
# ============================================================
def slide14():
    im, d = new_page()
    title_bar(d, '八、作业布置 · 提高层', kicker='Homework · 选做 · 情境写作 + 拓展')
    # 作业卡片
    d.rounded_rectangle([60, 170, 1220, 670], radius=14, fill=WHITE, outline=BORDER, width=1)
    d.rounded_rectangle([60, 170, 1220, 220], radius=14, fill=ACCENT)
    d.rectangle([60, 200, 1220, 220], fill=ACCENT)
    d.text((90, 183), '✏️  提高作业  (选做 · 10 分钟)', font=F_CARD_TITLE, fill=WHITE)
    d.text((900, 185), 'A 班必做 · B 班选做', font=F_LABEL, fill=WHITE)
    # 任务说明
    y = 250
    d.text((90, y), '四、情境写作', font=F_LABEL, fill=ACCENT); y += 30
    for line in wrap_text(d, '假设你下个月要去北京旅行，请写一段 80 词左右的英语短文介绍你的旅行计划。要求：', F_BODY, 1080):
        d.text((90, y), line, font=F_BODY, fill=DARK); y += F_BODY.size + 4
    y += 10
    items = [
        '① 说明出行方式（航班/火车）',
        '② 至少使用 5 个本课新词汇',
        '③ 至少使用 2 个一般将来时句型',
    ]
    for it in items:
        d.text((110, y), it, font=F_BODY, fill=DARK); y += F_BODY.size + 6
    y += 20
    # 参考答案（折叠区）
    d.rounded_rectangle([90, y, 1190, y+34], radius=6, fill=(255, 247, 224), outline=(251, 191, 36), width=1)
    d.text((110, y+5), '🔑 参考答案（教师用）', font=F_LABEL, fill=(180, 83, 9))
    y += 44
    sample = ('Next month, I am going to Beijing by flight. I will take my passport, suitcase and camera. '
              'I am visiting the Great Wall and the Forbidden City. I have never been to Beijing before, '
              'so I am very excited. The flight takes off at 8:00 AM and lands at 11:00 AM. I am looking forward to the trip!')
    for line in wrap_text(d, sample, F_BODY_S, 1080):
        d.text((110, y), line, font=F_BODY_S, fill=(82, 50, 5)); y += F_BODY_S.size + 4
    footer(d, 14, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_14_homework_advanced.png'), 'PNG', optimize=True)

# ============================================================
# Slide 15: 教学反思
# ============================================================
def slide15():
    im, d = new_page()
    title_bar(d, '九、教学反思', kicker='Reflection · 课后复盘 · 持续改进')
    blocks = [
        ('OK', '亮  点', GREEN, GREEN_LT, [
            '·  词汇分块教学 + 实物图标，视觉锚点强',
            '·  听力分三步走：预测—听中—听后，策略清晰',
            '·  A/B 班分层指令，B 班跟读速度降 30%',
            '·  学生角色扮演参与度 95%，超预期',
        ]),
        ('!', '需 改 进', RED, RED_LT, [
            '·  flight / flat 同音辨析时间不够，需增加 2 分钟',
            '·  板书书写时学生注意力分散，应配合提问',
            '·  课末复述环节超时 3 分钟，需精简',
            '·  后排 4 名学生参与度低，座位待调整',
        ]),
        ('*', '下 节 衔 接', PRIM, PALE, [
            '·  下节课讲 Reading：Travel Plans（课本 P7-9）',
            '·  课前听写 12 词，巩固本节词汇',
            '·  继续训练"预测—听中—听后"策略',
            '·  引入语篇：介绍你最喜欢的旅行目的地',
        ]),
    ]
    cw = 380
    for i, (emoji, title, color, bg, items) in enumerate(blocks):
        x = 60 + i * (cw + 24)
        d.rounded_rectangle([x, 170, x+cw, 670], radius=14, fill=WHITE, outline=color, width=2)
        d.rounded_rectangle([x, 170, x+cw, 230], radius=14, fill=color)
        d.rectangle([x, 210, x+cw, 230], fill=color)
        d.text((x+24, 188), emoji, font=ImageFont.truetype(r'C:/Windows/Fonts/seguisb.ttf', 36), fill=WHITE)
        d.text((x+90, 188), title, font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 28), fill=WHITE)
        y = 260
        for it in items:
            d.rounded_rectangle([x+20, y, x+24, y+24], fill=color)
            d.text((x+34, y), it, font=F_BODY_S, fill=DARK); y += 50
    footer(d, 15, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_15_reflection.png'), 'PNG', optimize=True)

# ============================================================
# Slide 16: 总结 + 结束
# ============================================================
def slide16():
    im, d = new_page()
    # 大色块背景
    d.rounded_rectangle([60, 80, 1220, 640], radius=24, fill=PRIM)
    # 装饰圆
    d.ellipse([900, 100, 1220, 420], fill=PRIM_DK)
    d.ellipse([40, 400, 240, 600], fill=PRIM_DK)
    d.polygon([(1080, 540), (1140, 540), (1110, 490)], fill=ACCENT)
    # 主标题
    d.text((140, 200), '课 堂 小 结', font=ImageFont.truetype(r'C:/Windows/Fonts/msyhbd.ttc', 56), fill=WHITE)
    d.text((140, 280), 'Summary of Today\'s Lesson', font=ImageFont.truetype(r'C:/Windows/Fonts/arial.ttf', 24), fill=(199, 220, 254))
    # 关键收获
    y = 360
    pts = [
        '+  12 个旅行场景核心词汇',
        '✓  flight / flat 同音辨析策略',
        '✓  "预测—听中—听后"三段听力法',
        '✓  一般将来时在旅行语境的运用',
    ]
    for p in pts:
        d.text((140, y), p, font=ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', 22), fill=WHITE); y += 40
    # 结束语
    d.text((140, 580), 'THANKS  ·  See You Next Class!', font=ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', 26), fill=ACCENT)
    # 右下角单元信息
    d.rounded_rectangle([840, 540, 1180, 600], radius=10, fill=WHITE)
    d.text((860, 550), '人教版 2019 · 必修一 · U2', font=F_LABEL, fill=PRIM)
    d.text((860, 575), 'Travelling Around · Listening & Speaking', font=F_BODY_S, fill=DARK)
    footer(d, 16, 16, 'l-eng-b1-u2-ls')
    im.save(os.path.join(OUT, 'slide_16_summary.png'), 'PNG', optimize=True)

# 教学过程 6 步的 page_id 序列
step_pages = [
    # (num, title, content_blocks, color, page_id)
    (1, 'Step 1  课前导入 · Warm-up', [
        ('🎯', '教学活动', '教师展示三张旅行图片（护照 / 机票 / 行李箱），询问学生：\n· "What do you see in these pictures?"\n· "Have you ever travelled by plane?"', PRIM),
        ('💬', '教师台词', '"Today we are going to learn about travelling. Look at these pictures. Can you guess what they are?"', ACCENT),
        ('🎒', '学生预期回答', 'Passport!  /  A boarding pass.  /  A suitcase.', GREEN),
        ('⏱', '时间安排', '5 分钟', GRAY),
    ], PRIM, 6),
    (2, 'Step 2  词汇呈现 · New Words', [
        ('📚', '教学活动', '教师分四组呈现 12 个核心词汇（分场景）：\n· 证件类：passport / visa / ID card\n· 行李类：suitcase / carry-on / backpack\n· 登机类：gate / seat / boarding pass\n· 飞行类：take off / land / flight', PRIM),
        ('💬', '教师台词', '"Let\'s learn these words in 4 groups. Pay attention to the difference between flight, flat and fright."', ACCENT),
        ('⚡', '易错点提示', 'flight（航班）≠ flat（公寓）≠ fright（害怕），发音均为 /flæt/，需结合语境判断', RED),
        ('⏱', '时间安排', '8 分钟', GRAY),
    ], ACCENT, 7),
    (3, 'Step 3  听力预测 · Pre-listening', [
        ('🎧', '教学活动', '播放 P6 听力前 30 秒后暂停，引导学生预测：\n· "Who are the speakers?"\n· "Where are they?"\n· "What will they talk about?"', PRIM),
        ('💬', '教师台词', '"Before listening, let\'s predict. Look at the picture on P6. What can you see?"', ACCENT),
        ('🎒', '学生预期回答', 'Two people at the airport.  /  Maybe they are friends.', GREEN),
        ('⏱', '时间安排', '3 分钟', GRAY),
    ], GREEN, 8),
    (4, 'Step 4  听力训练 · While-listening', [
        ('🎧', '教学活动', '完整播放 P6 听力两遍：\n· 第一遍：学生听大意，回答 2 个核心问题\n· 第二遍：学生填 P5 表格（5 个关键信息）', PRIM),
        ('💬', '教师台词', '"Listen for the first time, get the main idea. Listen again and complete the table on P5."', ACCENT),
        ('🎒', '学生预期回答', 'Q1: A hotel room and a flight. / Q2: At 10:00 AM.', GREEN),
        ('⏱', '时间安排', '10 分钟', GRAY),
    ], (168, 85, 247), 9),
    (5, 'Step 5  听后输出 · Post-listening', [
        ('🗣', '教学活动', '小组活动：4 人一组，根据听力信息设计一段 30 秒的旅行对话：\n· 角色 A：问询者 (A: ...?)\n· 角色 B：回答者 (B: I am going to...)', PRIM),
        ('💬', '教师台词', '"Now work in groups of 4. Design a short dialogue about your travel plan."', ACCENT),
        ('🎒', '学生预期回答', '"Are you going to Paris?" / "Yes, I am. I am taking flight CA933."', GREEN),
        ('⏱', '时间安排', '8 分钟', GRAY),
    ], (236, 72, 153), 10),
    (6, 'Step 6  总结作业 · Wrap-up', [
        ('📝', '教学活动', '教师总结本课 3 个核心收获，引导学生回顾：\n· 12 个核心词汇\n· 同音辨析策略\n· 听力三步法', PRIM),
        ('💬', '教师台词', '"Today we learned 12 words, learned how to tell flight from flat, and practiced the 3-step listening strategy."', ACCENT),
        ('📌', '作业布置', '基础作业：单词拼写 + 句型转换 (P7 第 1-3 题)\n提高作业：写一段 80 词的旅行计划', GREEN),
        ('⏱', '时间安排', '6 分钟', GRAY),
    ], (14, 165, 233), 11),
]

# 生成所有
slide1()
slide2()
slide3()
slide4()
slide5()
for args in step_pages:
    num, title, content_blocks, color, page_id = args
    step_page(num, 6, title, content_blocks, color, page_id)
slide12()
slide13()
slide14()
slide15()
slide16()

# 列出
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    print(f'{f:40s} {os.path.getsize(p)//1024:>4d} KB')

print(f'\n共 {len(os.listdir(OUT))} 页设计稿已生成于 {OUT}')
