"""
课堂版PPT渲染器 — 沁园春·长沙 (14页)
费曼可视化原则：每页一个视觉主体+一句诗文，图为主、字为辅
16:9 (1280x720) 投影尺寸，真实照片全屏背景 + 大字覆盖
统一风格：墨蓝底栏 + 霜红强调色 + 白字诗句
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# ── 路径 ──
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE, 'classroom_images')
OUT_DIR = os.path.join(BASE, 'cn_qyc_classroom')
os.makedirs(OUT_DIR, exist_ok=True)

# ── 幻灯尺寸 ──
W, H = 1280, 720

# ── 配色 ──
INK     = (28, 43, 51)        # 墨蓝
FROST   = (178, 58, 42)       # 霜红
XIANG   = (46, 125, 107)      # 湘碧
ACCENT  = (194, 112, 61)      # 陶土橙
WHITE   = (255, 255, 255)
GOLD    = (240, 210, 140)     # 暖金
DARK_BG = (18, 22, 28)        # 深黑背景
GRAY60  = (153, 153, 153)

# ── 字体 ──
FONT_BOLD = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", 80)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", 96)
FONT_BIG   = ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc", 64)
FONT_MED   = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 32)
FONT_SM    = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 24)
FONT_XS    = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 18)

# ── 工具函数 ──
def load_img(name):
    """加载图片并适配1280x720（居中裁切填充）"""
    path = os.path.join(IMG_DIR, name)
    img = Image.open(path).convert('RGB')
    iw, ih = img.size
    # 计算裁切区域——保持比例填满1280x720
    target_ratio = W / H
    img_ratio = iw / ih
    if img_ratio > target_ratio:
        # 图片更宽——裁左右
        new_w = int(ih * target_ratio)
        left = (iw - new_w) // 2
        img = img.crop((left, 0, left + new_w, ih))
    else:
        # 图片更高——裁上下
        new_h = int(iw / target_ratio)
        top = (ih - new_h) // 2
        img = img.crop((0, top, iw, top + new_h))
    return img.resize((W, H), Image.LANCZOS)

def darken(img, amount=0.25):
    """轻微压暗图片，确保白色文字可读"""
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(1.0 - amount)

def add_gradient_overlay(draw, direction='bottom', start_opacity=0, end_opacity=160):
    """添加渐变蒙层：上半透明→下半黑，使大字可读"""
    for y in range(H):
        if direction == 'bottom':
            alpha = int(start_opacity + (end_opacity - start_opacity) * (y / H * 1.5))
        else:
            alpha = int(start_opacity + (end_opacity - start_opacity) * ((H - y) / H * 1.5))
        alpha = max(0, min(255, alpha))
        if alpha > 0:
            draw.rectangle([(0, y), (W, y)], fill=(0, 0, 0, alpha))

def draw_bottom_bar(draw, page_num, total=14, label=""):
    """统一底部状态栏"""
    # 底部细线
    draw.line([(60, H - 50), (W - 60, H - 50)], fill=FROST + (120,), width=2)
    # 页码
    draw.text((W - 120, H - 42), f"{page_num}/{total}", font=FONT_XS, fill=GRAY60)
    if label:
        draw.text((60, H - 42), label, font=FONT_XS, fill=FROST)

def text_with_shadow(draw, x, y, text, font, fill=WHITE, shadow_color=(0,0,0,80)):
    """带阴影的大字文本"""
    draw.text((x+2, y+2), text, font=font, fill=shadow_color)
    draw.text((x, y), text, font=font, fill=fill)

def draw_verse_page(img_name, verse_lines, page_num, label="",
                    verse_color=WHITE, secondary_lines=None, keyword=None):
    """
    通用诗句页：照片背景 + 大字诗句
    verse_lines: [(text, font, y_offset), ...]
    每行居中，从y=H//2-80开始向下排列
    """
    bg = load_img(img_name)
    bg = darken(bg, 0.2)
    draw = ImageDraw.Draw(bg, 'RGBA')
    add_gradient_overlay(draw, 'bottom', 40, 200)

    # 绘制诗句
    total_h = sum(f.size for _, f, _ in verse_lines) + (len(verse_lines)-1) * 10
    start_y = (H - total_h) // 2

    current_y = start_y
    for text, font, _ in verse_lines:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        x = (W - tw) // 2
        text_with_shadow(draw, x, current_y, text, font, fill=verse_color)
        current_y += font.size + 10

    # 副行（如果有）
    if secondary_lines:
        current_y += 20
        for text, font, color in secondary_lines:
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            x = (W - tw) // 2
            draw.text((x, current_y), text, font=font, fill=color)
            current_y += font.size + 4

    # 关键词标注（如果有）
    if keyword:
        kw_x, kw_y, kw_text, kw_color = keyword
        draw.text((kw_x, kw_y), kw_text, font=FONT_SM, fill=kw_color)

    draw_bottom_bar(draw, page_num, label=label)
    return bg


# ═══════════════════════════════════════════════
# 页面定义
# ═══════════════════════════════════════════════

def page01_cover():
    """封面"""
    bg = load_img('00_cover.jpg')
    bg = darken(bg, 0.35)
    draw = ImageDraw.Draw(bg, 'RGBA')
    add_gradient_overlay(draw, 'bottom', 100, 220)

    # 主标题
    title = "沁园春·长沙"
    bbox = draw.textbbox((0, 0), title, font=FONT_TITLE)
    tw = bbox[2] - bbox[0]
    text_with_shadow(draw, (W - tw) // 2, H//2 - 100, title, FONT_TITLE, GOLD)

    # 作者
    author = "毛泽东"
    bbox2 = draw.textbbox((0, 0), author, font=FONT_BOLD)
    tw2 = bbox2[2] - bbox2[0]
    draw.text(((W - tw2)//2, H//2), author, font=FONT_BOLD, fill=WHITE)

    # 副标题
    sub = "高中语文 · 必修上册 · 第一单元"
    bbox3 = draw.textbbox((0, 0), sub, font=FONT_MED)
    tw3 = bbox3[2] - bbox3[0]
    draw.text(((W - tw3)//2, H//2 + 80), sub, font=FONT_MED, fill=GRAY60)

    draw_bottom_bar(draw, 1, label="课堂讲授PPT")
    return bg


def page02_stand():
    """独立寒秋"""
    return draw_verse_page(
        '01_river_island.jpg',
        [("独立寒秋，湘江北去，橘子洲头", FONT_BIG, WHITE)],
        2, label="上阕 · 起句",
        secondary_lines=[
            ("时 间：深秋  |  地 点：橘子洲  |  人 物：独立远眺", FONT_SM, GOLD)
        ]
    )


def page03_red_mountains():
    """万山红遍"""
    return draw_verse_page(
        '02_autumn_mountains.jpg',
        [("看万山红遍", FONT_TITLE, WHITE)],
        3, label="上阕 · 远眺",
        secondary_lines=[
            ("「万」山之多  「遍」红之广——远眺全景", FONT_SM, ACCENT)
        ]
    )


def page04_forest():
    """层林尽染"""
    return draw_verse_page(
        '03_autumn_forest.jpg',
        [("层林尽染", FONT_TITLE, WHITE)],
        4, label="上阕 · 远眺",
        secondary_lines=[
            ("「层」层次丰富  「染」如画着色——山林如画", FONT_SM, ACCENT)
        ]
    )


def page05_green_river():
    """漫江碧透"""
    return draw_verse_page(
        '04_green_river.jpg',
        [("漫江碧透", FONT_TITLE, WHITE)],
        5, label="上阕 · 近观",
        secondary_lines=[
            ("「漫」江水满溢  「透」清澈见底——碧水长流", FONT_SM, ACCENT)
        ]
    )


def page06_boats():
    """百舸争流"""
    return draw_verse_page(
        '05_boats.jpg',
        [("百舸争流", FONT_TITLE, WHITE)],
        6, label="上阕 · 近观",
        secondary_lines=[
            ("「争」千帆竞发  「流」乘风破浪——昂扬奋进", FONT_SM, ACCENT)
        ]
    )


def page07_eagle():
    """鹰击长空"""
    return draw_verse_page(
        '06_eagle.jpg',
        [("鹰击长空", FONT_TITLE, WHITE)],
        7, label="上阕 · 仰视",
        secondary_lines=[
            ("「击」矫健有力——雄鹰展翅，冲破长空", FONT_SM, ACCENT)
        ]
    )


def page08_fish():
    """鱼翔浅底"""
    return draw_verse_page(
        '07_fish.jpg',
        [("鱼翔浅底", FONT_TITLE, WHITE)],
        8, label="上阕 · 俯瞰",
        secondary_lines=[
            ("「翔」自在轻快——鱼游水底，如在天空飞翔", FONT_SM, ACCENT)
        ]
    )


def page09_summary():
    """万类霜天竞自由——上阕意象总结"""
    # 使用渐变背景 + 意象图标排列
    bg = Image.new('RGB', (W, H), DARK_BG)
    draw = ImageDraw.Draw(bg, 'RGBA')

    # 顶部装饰线
    draw.rectangle([(80, 80), (W-80, 86)], fill=FROST)

    # 主句
    verse = "万类霜天竞自由"
    bbox = draw.textbbox((0, 0), verse, font=FONT_BOLD)
    tw = bbox[2] - bbox[0]
    text_with_shadow(draw, (W-tw)//2, 120, verse, FONT_BOLD, GOLD)

    # 意象总结卡：六个意象 + 对应的视觉词
    imageries = [
        ("万 山", "红遍", FROST),
        ("层 林", "尽染", ACCENT),
        ("漫 江", "碧透", XIANG),
        ("百 舸", "争流", WHITE),
        ("鹰", "击", GOLD),
        ("鱼", "翔", XIANG),
    ]
    card_w, card_h = 180, 100
    start_x = (W - 3 * card_w - 2 * 40) // 2
    start_y = 280
    for i, (name, verb, color) in enumerate(imageries):
        col = i % 3
        row = i // 3
        cx = start_x + col * (card_w + 40)
        cy = start_y + row * (card_h + 20)
        # 卡片背景
        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)], 12,
                               fill=(30, 36, 45), outline=color + (80,), width=1)
        # 顶部色条
        draw.rectangle([(cx, cy), (cx + card_w, cy + 4)], fill=color)
        # 意象名
        nbox = draw.textbbox((0, 0), name, font=FONT_MED)
        draw.text((cx + (card_w - nbox[2] + nbox[0])//2, cy + 12),
                  name, font=FONT_MED, fill=WHITE)
        # 动词
        vbox = draw.textbbox((0, 0), verb, font=FONT_SM)
        draw.text((cx + (card_w - vbox[2] + vbox[0])//2, cy + 58),
                  verb, font=FONT_SM, fill=color)

    # 底部总结
    summary = "色彩绚烂 · 生机勃勃 · 壮丽开阔 —— 一反古人悲秋，歌颂秋日的生命力"
    sbox = draw.textbbox((0, 0), summary, font=FONT_SM)
    draw.text(((W - sbox[2] + sbox[0])//2, 530), summary, font=FONT_SM, fill=GRAY60)

    draw_bottom_bar(draw, 9, label="上阕 · 意象总结")
    return bg


def page10_youth():
    """恰同学少年——下阕开启"""
    bg = Image.new('RGB', (W, H), (24, 30, 38))
    draw = ImageDraw.Draw(bg, 'RGBA')

    # 装饰性顶部渐变条
    for y in range(100):
        alpha = int(80 * (1 - y/100))
        draw.rectangle([(0, y), (W, y)], fill=FROST + (alpha,))

    # 诗句
    lines = [
        ("恰同学少年，风华正茂", FONT_BIG, WHITE),
        ("书生意气，挥斥方遒", FONT_BIG, GOLD),
    ]
    sy = 160
    for text, font, color in lines:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        text_with_shadow(draw, (W-tw)//2, sy, text, font, color)
        sy += font.size + 20

    # 形象卡片
    traits = [
        ("风华正茂", "青春年少，才华横溢"),
        ("挥斥方遒", "热情奔放，敢想敢做"),
        ("指点江山", "激昂慷慨，心系天下"),
        ("粪土万户侯", "蔑视权贵，救国救民"),
    ]
    card_w = 260
    card_h = 100
    gx = (W - 2 * card_w - 60) // 2
    for i, (label, desc) in enumerate(traits):
        cx = gx + (i % 2) * (card_w + 60)
        cy = 380 + (i // 2) * (card_h + 16)
        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)], 10,
                               fill=(35, 42, 52), outline=ACCENT + (60,))
        draw.rectangle([(cx, cy), (cx + card_w, cy + 3)], fill=ACCENT)
        lbox = draw.textbbox((0, 0), label, font=FONT_MED)
        draw.text((cx + 14, cy + 10), label, font=FONT_MED, fill=GOLD)
        dbox = draw.textbbox((0, 0), desc, font=FONT_SM)
        draw.text((cx + 14, cy + 60), desc, font=FONT_SM, fill=GRAY60)

    sub = "一代革命青年的群像：以天下为己任，矢志振兴中华"
    sbox = draw.textbbox((0, 0), sub, font=FONT_SM)
    draw.text(((W - sbox[2] + sbox[0])//2, 600), sub, font=FONT_SM, fill=GRAY60)

    draw_bottom_bar(draw, 10, label="下阕 · 峥嵘岁月")
    return bg


def page11_point():
    """指点江山 激扬文字"""
    bg = Image.new('RGB', (W, H), DARK_BG)
    draw = ImageDraw.Draw(bg, 'RGBA')

    # 斜向装饰色块
    for i in range(0, W, 3):
        # 渐变横条
        pass

    lines = [
        ("指点江山，激扬文字", FONT_BIG, WHITE),
        ("粪土当年万户侯", FONT_BOLD, GOLD),
    ]
    sy = 200
    for text, font, color in lines:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        text_with_shadow(draw, (W-tw)//2, sy, text, font, color)
        sy += font.size + 20

    # 关键注解
    notes = [
        "「指点」评述褒贬，干预时政", 
        "「激扬」激浊扬清，慷慨激昂",
        "「粪土」视……如粪土——蔑视权贵的革命气概",
    ]
    ny = 420
    for note in notes:
        nbox = draw.textbbox((0, 0), note, font=FONT_SM)
        draw.text(((W - nbox[2] + nbox[0])//2, ny), note, font=FONT_SM, fill=GRAY60)
        ny += 36

    draw_bottom_bar(draw, 11, label="下阕 · 革命豪情")
    return bg


def page12_waves():
    """到中流击水 浪遏飞舟"""
    return draw_verse_page(
        '08_waves.jpg',
        [("到中流击水，浪遏飞舟", FONT_BIG, WHITE)],
        12, label="下阕 · 中流击水",
        secondary_lines=[
            ("化用「中流击楫」典故——祖逖北伐，誓清中原", FONT_SM, GOLD),
            ("含蓄回答上阕「谁主沉浮」之问——青年就是答案", FONT_SM, ACCENT),
        ]
    )


def page13_question():
    """问苍茫大地 谁主沉浮"""
    bg = load_img('00_cover.jpg')
    bg = darken(bg, 0.4)
    draw = ImageDraw.Draw(bg, 'RGBA')
    add_gradient_overlay(draw, 'bottom', 60, 220)

    verse = "问苍茫大地，谁主沉浮？"
    bbox = draw.textbbox((0, 0), verse, font=FONT_TITLE)
    tw = bbox[2] - bbox[0]
    text_with_shadow(draw, (W-tw)//2, H//2 - 60, verse, FONT_TITLE, GOLD)

    answer = "—— 到中流击水，浪遏飞舟"
    abox = draw.textbbox((0, 0), answer, font=FONT_BIG)
    atw = abox[2] - abox[0]
    draw.text(((W - atw)//2, H//2 + 40), answer, font=FONT_BIG, fill=WHITE)

    draw_bottom_bar(draw, 13, label="全词 · 主旨升华")
    return bg


def page14_ending():
    """课后思考"""
    bg = Image.new('RGB', (W, H), DARK_BG)
    draw = ImageDraw.Draw(bg, 'RGBA')

    # 顶部装饰
    draw.rectangle([(80, 60), (W-80, 66)], fill=FROST)

    title = "课后思考"
    tbox = draw.textbbox((0, 0), title, font=FONT_BOLD)
    draw.text(((W - tbox[2] + tbox[0])//2, 100), title, font=FONT_BOLD, fill=GOLD)

    questions = [
        "1. 词中描绘了哪些意象？这些意象组合营造了怎样的意境？",
        "2. 「鹰击长空」能否换成「鹰飞长空」？为什么？",
        "3. 上阕的「看」与下阕的「忆」在全词结构上有何作用？",
        "4. 结合写作背景，谈谈「谁主沉浮」的深层含义。",
    ]
    qy = 200
    for q in questions:
        draw.text((120, qy), q, font=FONT_MED, fill=WHITE)
        qy += 70

    # 底部关键词
    keywords = "意象 · 炼字 · 情景交融 · 以天下为己任"
    kbox = draw.textbbox((0, 0), keywords, font=FONT_SM)
    draw.text(((W - kbox[2] + kbox[0])//2, 540), keywords, font=FONT_SM, fill=FROST)

    signature = "—— 毛泽东《沁园春·长沙》"
    sbox = draw.textbbox((0, 0), signature, font=FONT_SM)
    draw.text(((W - sbox[2] + sbox[0])//2, 580), signature, font=FONT_SM, fill=GRAY60)

    draw_bottom_bar(draw, 14, label="课堂讲授PPT")
    return bg


# ═══════════════════════════════════════════════
# 生成全部
# ═══════════════════════════════════════════════

PAGES = [
    page01_cover,
    page02_stand,
    page03_red_mountains,
    page04_forest,
    page05_green_river,
    page06_boats,
    page07_eagle,
    page08_fish,
    page09_summary,
    page10_youth,
    page11_point,
    page12_waves,
    page13_question,
    page14_ending,
]

def render_all():
    slides = []
    for i, page_fn in enumerate(PAGES):
        print(f"Rendering slide {i+1:02d}...")
        slide = page_fn()
        png_path = os.path.join(OUT_DIR, f"slide_{i+1:02d}.png")
        slide.save(png_path, 'PNG')
        slides.append(slide)
        print(f"  -> {png_path} ({slide.size[0]}x{slide.size[1]})")

    # 合成PDF
    pdf_path = os.path.join(OUT_DIR, "沁园春长沙-课堂版PPT.pdf")
    # Convert all to RGB mode for PDF
    slides_rgb = [s.convert('RGB') for s in slides]
    slides_rgb[0].save(pdf_path, 'PDF', resolution=150,
                       save_all=True, append_images=slides_rgb[1:])
    pdf_size = os.path.getsize(pdf_path)
    print(f"\nPDF: {pdf_path} ({pdf_size} bytes)")

    # 复制到桌面
    import shutil
    desktop = os.path.expanduser("~/Desktop")
    desk_pdf = os.path.join(desktop, "沁园春长沙-课堂版PPT.pdf")
    shutil.copy(pdf_path, desk_pdf)
    print(f"Copied to desktop: {desk_pdf}")

    print(f"\nDone! {len(slides)} slides rendered.")

if __name__ == '__main__':
    render_all()
