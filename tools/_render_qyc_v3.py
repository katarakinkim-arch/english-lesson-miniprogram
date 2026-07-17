# -*- coding: utf-8 -*-
"""
v3 精美/商业化 PPT 设计稿渲染器 —— 《沁园春·长沙》精读(上) 意象与情感
融合：市场参考(文体/朗读/四图/视角/炼字10字/悲秋对照/典故) + 我们六要素(台词/预设/分层/易错/板书/作业)
视觉：主题绑定配色(霜红=万山红遍/湘碧=漫江碧透/墨蓝=鹰击) + 手绘插画 + 商业化页眉卡片
输出：18 页 PNG → 单课 PDF
用法: python tools/_render_qyc_v3.py
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cn_qyc_v3')
os.makedirs(OUT, exist_ok=True)

# ---- 主题配色（绑定课文意象）----
BG     = (247, 245, 240)   # 暖纸白
INK    = (28, 43, 51)      # 墨蓝（鹰击长空）
ACCENT = (194, 112, 61)    # 陶土橙（主强调）
FROST  = (178, 58, 42)     # 霜红（万山红遍 / 枫叶）
XIANG  = (46, 125, 107)    # 湘碧（漫江碧透）
MUTED  = (138, 133, 128)   # 辅灰
LINE   = (216, 210, 200)   # 细线
CARD   = (255, 253, 249)   # 卡片底
SOFT   = (250, 244, 238)   # 软底

F_BD = r'C:\Windows\Fonts\msyhbd.ttc'
F_RG = r'C:\Windows\Fonts\msyh.ttc'
F_LT = r'C:\Windows\Fonts\msyhl.ttc'

def font(size, bd=False, lt=False):
    if bd: return ImageFont.truetype(F_BD, size)
    if lt: return ImageFont.truetype(F_LT, size)
    return ImageFont.truetype(F_RG, size)

PAGES = []
def add(img, name):
    PAGES.append((img, name))

def new_page(page_no, total=18, sec=''):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    # 顶部页眉条
    d.rectangle([0, 0, W, 6], fill=INK)
    d.rectangle([0, 6, W, 9], fill=ACCENT)
    # 页眉文字
    d.text((48, 20), '沁园春·长沙  |  意象与情感 · 第一课时', font=font(15), fill=MUTED)
    if sec:
        d.text((W//2, 20), sec, font=font(15, lt=True), fill=MUTED, anchor='mm')
    # 页脚
    d.text((W-48, H-26), f'{page_no:02d} / {total:02d}', font=font(13, lt=True), fill=MUTED, anchor='rm')
    d.text((48, H-26), '必修上册 · 第一单元 青春的价值', font=font(12, lt=True), fill=MUTED)
    return img, d

def wrap(text, fnt, max_w):
    """中文按字符宽度换行"""
    lines, cur = [], ''
    for ch in text:
        if ch == '\n':
            lines.append(cur); cur = ''; continue
        if fnt.getlength(cur + ch) > max_w and cur:
            lines.append(cur); cur = ch
        else:
            cur += ch
    if cur: lines.append(cur)
    return lines

def text(d, x, y, s, font, fill, max_w=None, lh=None):
    if max_w:
        lines = wrap(s, font, max_w)
    else:
        lines = s.split('\n')
    lh = lh or (font.size + 6)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def card(d, x, y, w, h, accent=ACCENT, top_bar=True):
    """白底圆角卡片 + 顶部色条"""
    d.rounded_rectangle([x, y, x+w, y+h], radius=10, fill=CARD, outline=LINE, width=1)
    if top_bar:
        d.rounded_rectangle([x, y, x+w, y+5], radius=10, fill=accent)
        d.rectangle([x, y+3, x+w, y+5], fill=accent)
    return

def chip(d, x, y, label, color, fnt=None):
    fnt = fnt or font(15, bd=True)
    tw = fnt.getlength(label) + 22
    d.rounded_rectangle([x, y, x+tw, y+30], radius=15, fill=color)
    d.text((x+11, y+15), label, font=fnt, fill=(255,255,255), anchor='lm')
    return x + tw + 10

# ---- 手绘插画 ----
def draw_cover_art(d, x, y, w, h):
    """封面：橘子洲秋景 —— 远山霜红 + 湘江湘碧 + 鹰"""
    # 远山层（霜红渐深）
    d.polygon([(x, y+h*0.62),(x+w*0.18, y+h*0.30),(x+w*0.36, y+h*0.45),(x+w*0.55, y+h*0.25),
               (x+w*0.72, y+h*0.40),(x+w*0.9, y+h*0.28),(x+w, y+h*0.5),(x+w, y+h*0.7),(x, y+h*0.7)],
              fill=(178,58,42))
    d.polygon([(x, y+h*0.7),(x+w*0.25, y+h*0.5),(x+w*0.5, y+h*0.6),(x+w*0.78, y+h*0.48),
               (x+w, y+h*0.58),(x+w, y+h*0.72),(x, y+h*0.72)], fill=(140,40,32))
    # 湘江
    d.rectangle([x, y+h*0.72, x+w, y+h], fill=(46,125,107))
    # 江面波纹
    for i in range(4):
        yy = y+h*0.76 + i*14
        d.line([(x+20, yy),(x+w-20, yy)], fill=(255,253,249,80), width=2)
    # 一只鹰（墨蓝简笔）
    ex, ey = x+w*0.7, y+h*0.34
    d.line([(ex-26, ey+4),(ex-6, ey-2),(ex, ey),(ex+6, ey-2),(ex+26, ey+4)], fill=INK, width=3)
    d.line([(ex, ey),(ex, ey+10)], fill=INK, width=3)
    # 橘子洲轮廓
    d.polygon([(x+w*0.38, y+h*0.74),(x+w*0.45, y+h*0.70),(x+w*0.6, y+h*0.71),(x+w*0.58, y+h*0.74)], fill=(120,90,60))

def draw_maple(d, cx, cy, r, color):
    """简化枫叶（五瓣星形近似）"""
    pts = []
    for i in range(10):
        a = -math.pi/2 + i*math.pi/5
        rr = r if i%2==0 else r*0.45
        pts.append((cx+rr*math.cos(a), cy+rr*math.sin(a)))
    d.polygon(pts, fill=color)

def draw_eagle_icon(d, cx, cy, s, color):
    d.line([(cx-s, cy),(cx-s*0.3, cy-s*0.3),(cx, cy-s*0.1),(cx+s*0.3, cy-s*0.3),(cx+s, cy)], fill=color, width=max(2,s//8))
    d.line([(cx, cy-s*0.1),(cx, cy+s*0.4)], fill=color, width=max(2,s//8))

def draw_fish_icon(d, cx, cy, s, color):
    d.ellipse([cx-s, cy-s*0.4, cx+s*0.5, cy+s*0.4], fill=color)
    d.polygon([(cx-s, cy),(cx-s*1.4, cy-s*0.5),(cx-s*1.4, cy+s*0.5)], fill=color)

# ==================== 18 页 ====================
TOTAL = 18

# ---- P1 封面 ----
img, d = new_page(1, TOTAL)
draw_cover_art(d, 60, 300, 520, 300)
# 右侧标题区
d.text((640, 250), '沁园春·长沙', font=font(74, bd=True), fill=INK)
d.line([(640, 345),(1120, 345)], fill=ACCENT, width=3)
d.text((644, 365), '意象与情感', font=font(34), fill=FROST)
d.text((644, 420), '第一课时  ·  课文精读（上）', font=font(20), fill=MUTED)
d.text((644, 458), '毛泽东  /  1925年秋  ·  橘子洲', font=font(18, lt=True), fill=MUTED)
# 标签
chip(d, 644, 510, '诗词精读', FROST)
chip(d, 760, 510, '意象品析', XIANG)
chip(d, 876, 510, '炼字比较', INK)
d.text((644, 600), '人教版（统编）高中语文  必修上册  第一单元', font=font(15, lt=True), fill=MUTED)
d.text((644, 625), '青春的价值  ·  文学阅读与写作任务群', font=font(15, lt=True), fill=MUTED)
add(img, '01_cover')

# ---- P2 课堂导览 ----
img, d = new_page(2, TOTAL, '课堂导览')
d.text((48, 70), '课堂导览', font=font(38, bd=True), fill=INK)
d.text((48, 122), '6 个环节  ·  45 分钟  ·  聚焦上阕「意象与情感」', font=font(17), fill=MUTED)
steps = [
    ('01','文体背景','5min','词·词牌·分类 + 1925时代之问',FROST),
    ('02','诵读感知','8min','字音·节拍·重音·情感曲线',XIANG),
    ('03','圈点意象','15min','六意象卡片 + 视角转换图',FROST),
    ('04','炼字品析','10min','击/翔替换比较 + 十字炼字',ACCENT),
    ('05','悲秋对照','5min','古人悲秋 vs 毛泽东颂秋',INK),
    ('06','情感推导','2min','景→问→情 + 典故',XIANG),
]
cw, ch = 360, 130
for i,(no,name,tm,desc,c) in enumerate(steps):
    col, row = i%3, i//3
    x, y = 48+col*(cw+22), 175+row*(ch+22)
    card(d, x, y, cw, ch, accent=c)
    d.text((x+24, y+22), no, font=font(30, bd=True), fill=c)
    d.text((x+95, y+26), name, font=font(22, bd=True), fill=INK)
    chip(d, x+cw-78, y+22, tm, c, font(13, bd=True))
    text(d, x+95, y+62, desc, font(15), fill=MUTED, max_w=cw-120)
    d.text((x+24, y+ch-26), '—'*18, font=font(12, lt=True), fill=LINE)
add(img, '02_overview')

# ---- P3 学情与目标 ----
img, d = new_page(3, TOTAL, '学情与目标')
d.text((48, 70), '学情分析 与 素养目标', font=font(34, bd=True), fill=INK)
# 左：学情
card(d, 48, 145, 560, 470, accent=FROST)
d.text((72, 168), '学情分析', font=font(22, bd=True), fill=FROST)
ly = 210
for tag, body in [
    ('A 班','初中已学《沁园春·雪》，懂词牌格式，能概括大意，但意象分析停留在「写景很美」，缺「意象→情感」推导路径。'),
    ('B 班','朗读节奏感弱，「看/忆/问」三领字易读破句；「粪土当年万户侯」等典故不熟。'),
    ('共同问题','把「读诗」等同于「翻译」，忽略诵读节奏与意象组合的画面感。'),
]:
    chip(d, 72, ly, tag, FROST if tag!='共同问题' else MUTED, font(14, bd=True))
    ly = text(d, 72, ly+36, body, font(16), fill=INK, max_w=500) + 14
# 右：目标
card(d, 632, 145, 600, 470, accent=XIANG)
d.text((656, 168), '核心素养目标', font=font(22, bd=True), fill=XIANG)
objs = [
    ('语言能力','准确朗读全词，把握「看/忆/问」三领字统领作用，说出6+核心意象及特征。'),
    ('文化意识','理解青年毛泽东以天下为己任的革命情怀，体会「同学少年」对当代青年的启示。'),
    ('思维品质','经「意象群→画面→情感」推导路径，培养从具象到抽象的文学思维。'),
    ('学习能力','掌握「圈意象→标特征→串联画面→推导情感」诗词研读四步法并迁移。'),
]
oy = 210
colors = [FROST, XIANG, ACCENT, INK]
for (t,b),c in zip(objs, colors):
    d.ellipse([656, oy+4, 676, oy+24], fill=c)
    d.text((690, oy), t, font=font(17, bd=True), fill=c)
    oy = text(d, 690, oy+26, b, font(15), fill=INK, max_w=520) + 12
add(img, '03_goals')

# ---- P4 文体知识 ----
img, d = new_page(4, TOTAL, '文体知识')
d.text((48, 70), '文体知识 · 词与词牌', font=font(34, bd=True), fill=INK)
d.text((48, 122), '【市场参考补缺】读懂「沁园春」三个字，是读全词的起点', font=font(16), fill=MUTED)
# 左：词
card(d, 48, 165, 560, 250, accent=FROST)
d.text((72, 188), '词', font=font(26, bd=True), fill=FROST)
text(d, 72, 232, '又称「长短句」「诗余」「曲子词」，萌芽隋唐，盛于两宋。'
     '特点是：调有定格，句有定数，字有定声。', font=font(16), fill=INK, max_w=510)
# 右：词牌 vs 题目
card(d, 632, 165, 600, 250, accent=XIANG)
d.text((656, 188), '词牌  vs  题目', font=font(26, bd=True), fill=XIANG)
d.text((656, 232), '沁园春 · 长沙', font=font(30, bd=True), fill=INK)
d.text((656, 278), '「沁园春」= 词牌（规定字数/句数/平仄韵律，如曲谱）', font=font(15), fill=MUTED)
d.text((656, 304), '「长沙」= 题目（词的内容所在，写长沙之景）', font=font(15), fill=MUTED)
text(d, 656, 340, '沁园来历：东汉明帝女沁水公主园林被外戚窦宪强夺，后人咏其事，'
     '渐成「沁园春」词牌。', font=font(14, lt=True), fill=MUTED, max_w=540)
# 下：分类
card(d, 48, 435, 1184, 175, accent=ACCENT)
d.text((72, 458), '按字数分类', font=font(22, bd=True), fill=ACCENT)
cats = [('小令','≤58字'), ('中调','59–90字'), ('长调','≥91字')]
cx = 72
for name, rng in cats:
    d.rounded_rectangle([cx, 500, cx+150, 560], radius=8, fill=SOFT, outline=LINE)
    d.text((cx+75, 518), name, font=font(20, bd=True), fill=INK, anchor='mm')
    d.text((cx+75, 545), rng, font=font(14), fill=MUTED, anchor='mm')
    cx += 180
d.text((660, 510), '本词 = 长调 · 双调（上下两阕）', font=font(19, bd=True), fill=FROST)
d.text((660, 542), '全词114字，上阕13句下阕12句，一气贯通', font=font(15), fill=MUTED)
add(img, '04_wenti')

# ---- P5 时代背景 ----
img, d = new_page(5, TOTAL, '时代背景')
d.text((48, 70), '时代背景 · 1925', font=font(34, bd=True), fill=INK)
d.text((48, 122), '「谁主沉浮」不是空发感慨，而是一个时代之问', font=font(16), fill=MUTED)
# 时间轴
card(d, 48, 165, 1184, 200, accent=FROST)
tx = 80
d.line([(tx, 250),(1200, 250)], fill=LINE, width=3)
events = [
    (90,'1911','18岁到长沙\n革命活动13年'),
    (340,'1918','就读湖南一师\n创新民学会'),
    (620,'1925','重游橘子洲\n写下本词'),
    (920,'1926','北伐战争前夜\n革命蓬勃发展'),
]
for x,yr,desc in events:
    d.ellipse([x-9, 241, x+9, 259], fill=FROST)
    d.text((x, 222), yr, font=font(18, bd=True), fill=FROST, anchor='mm')
    text(d, x-60, 270, desc, font(14), fill=INK, max_w=140)
# 关键解读
card(d, 48, 385, 1184, 225, accent=INK)
d.text((72, 408), '为何要「问苍茫大地，谁主沉浮」？', font=font(22, bd=True), fill=INK)
text(d, 72, 450, '1925年大革命前夕，工农运动如旭日东升，反动势力疯狂打压。中华民族命运悬而未决：'
     '是继续沉沦，还是冲破黑暗？——「谁来主宰中国未来」成为时代焦点。', font=font(16), fill=INK, max_w=1130)
text(d, 72, 510, '毛泽东是年深秋离开韶山赴广州主持农民运动讲习所，途经长沙重游橘子洲，'
     '面对绚烂秋景，联想革命形势与往昔岁月，心潮澎湃，写下此词。', font=font(16), fill=INK, max_w=1130)
d.text((72, 568), '教学锚点：理解「沉浮」= 国家命运兴衰，非字面浮沉；「主」= 主宰。', font=font(15, bd=True), fill=ACCENT)
add(img, '05_bg')

# ---- P6 朗读指导 ----
img, d = new_page(6, TOTAL, '朗读指导')
d.text((48, 70), '朗读指导 · 字音 · 节拍 · 重音', font=font(34, bd=True), fill=INK)
# 字音
card(d, 48, 140, 600, 200, accent=FROST)
d.text((72, 162), '① 字音正读', font=font(20, bd=True), fill=FROST)
zy = [('百舸','gě'),('寥廓','liáo kuò'),('方遒','qiú'),('峥嵘','zhēng róng'),('浪遏','è'),('桔子洲','jú')]
zx, zy2 = 72, 198
for w,p in zy:
    d.text((zx, zy2), w, font=font(17, bd=True), fill=INK)
    d.text((zx+70, zy2), p, font=font(15), fill=FROST)
    zy2 += 30
    if zy2 > 320: zy2 = 198; zx += 200
# 节拍
card(d, 664, 140, 568, 200, accent=XIANG)
d.text((688, 162), '② 节拍停顿', font=font(20, bd=True), fill=XIANG)
jp = ['四字句  二二式：独立/寒秋  湘江/北去',
      '五字句  一四式：恰/同学少年  问/苍茫大地',
      '七字句  二五式：粪土/当年万户侯',
      '七字句  四三式：万类霜天/竞自由',
      '领字后须微顿：看/万山红遍  忆/往昔峥嵘']
jy = 198
for s in jp:
    jy = text(d, 688, jy, s, font(15), fill=INK, max_w=530) + 4
# 情感曲线
card(d, 48, 355, 1184, 255, accent=ACCENT)
d.text((72, 378), '③ 情感曲线', font=font(20, bd=True), fill=ACCENT)
d.text((72, 410), '全词情感起伏——从壮景豪情到忧思追问，再到青春自信、豪迈作答', font=font(15), fill=MUTED)
# 手绘折线
pts = [(120,540,'豪壮'),(340,470,'忧思'),(560,560,'欣喜'),(780,440,'自信'),(1000,500,'豪迈'),(1180,460,'↗')]
d.line([(120,540),(340,470),(560,560),(780,440),(1000,500),(1180,460)], fill=ACCENT, width=3, joint='curve')
for x,y,lab in pts:
    d.ellipse([x-6,y-6,x+6,y+6], fill=ACCENT)
    d.text((x, y-30), lab, font=font(15, bd=True), fill=INK, anchor='mm')
d.text((72, 588), '读法提示：上阕「看」字七句渐快渐高，「竞自由」收缩有力；下阕「恰」字七句一气相应。', font=font(14, lt=True), fill=MUTED)
add(img, '06_read')

# ---- P7 全词结构图 ----
img, d = new_page(7, TOTAL, '全词结构')
d.text((48, 70), '全词结构 · 四幅图', font=font(34, bd=True), fill=INK)
d.text((48, 122), '【市场参考补缺】上阕写景 下阕抒情，「问—答」贯穿全词', font=font(16), fill=MUTED)
figs = [
    ('独立寒秋图','立 · 点时地环境','独立寒秋 湘江北去 橘子洲头',FROST,'上阕'),
    ('湘江秋景图','看 · 远近仰俯动静','万山层林 漫江百舸 鹰鱼万类',XIANG,'上阕 ★本课'),
    ('峥嵘岁月图','忆 · 同学少年风华','风华正茂 挥斥方遒 指点江山',INK,'下阕'),
    ('中流击水图','记 · 浪遏飞舟','到中流击水 浪遏飞舟',ACCENT,'下阕'),
]
fw, fh = 282, 230
for i,(name,key,verse,c,part) in enumerate(figs):
    x, y = 48+i*(fw+20), 165
    star = '★' if '★' in part else ''
    card(d, x, y, fw, fh, accent=c)
    d.text((x+20, y+22), name, font=font(20, bd=True), fill=c)
    d.text((x+20, y+58), key, font=font(15), fill=MUTED)
    d.text((x+20, y+88), verse, font=font(16, bd=True), fill=INK)
    chip(d, x+20, y+fh-44, part.replace('★','').strip(), c, font(13, bd=True))
    if star:
        d.text((x+fw-30, y+18), '★', font=font(22, bd=True), fill=ACCENT)
# 枢纽
card(d, 48, 425, 1184, 185, accent=ACCENT)
d.text((72, 450), '结构枢纽：问 — 答', font=font(22, bd=True), fill=ACCENT)
d.text((72, 490), '上阕「问苍茫大地，谁主沉浮？」  →  下阕「同学少年」含蓄作答', font=font(19, bd=True), fill=INK)
d.text((72, 528), '上阕写景为抒情蓄势，下阕忆事呼应作答；景中寓情，情中显志。', font=font(16), fill=MUTED)
d.text((72, 565), '本课聚焦：上阕两图（独立寒秋图 + 湘江秋景图），即「意象与情感」核心。', font=font(15, bd=True), fill=FROST)
add(img, '07_struct')

# ---- P8 Step1 导入 ----
img, d = new_page(8, TOTAL, 'Step 1 · 导入')
d.text((48, 70), 'Step 1  导入  Lead-in', font=font(34, bd=True), fill=INK)
chip(d, 48, 122, '5 min', FROST, font(16, bd=True))
# 教师台词
card(d, 48, 170, 1184, 120, accent=FROST)
d.text((72, 192), '教师台词', font=font(18, bd=True), fill=FROST)
text(d, 72, 224, '「青春是什么颜色？用一个词，或一句诗，来形容你心中的青春。」', font=font(20), fill=INK, max_w=1130)
# 预设回答
card(d, 48, 305, 700, 175, accent=XIANG)
d.text((72, 328), '预设回答', font=font(18, bd=True), fill=XIANG)
for i,a in enumerate(['红色——热血','绿色——生机','像火一样']):
    d.text((72, 360+i*32), '·  '+a, font=font(17), fill=INK)
# 分层
card(d, 768, 305, 464, 175, accent=ACCENT)
d.text((792, 328), '差异化提示', font=font(18, bd=True), fill=ACCENT)
text(d, 792, 360, 'B班：说一个词即可\nA班：用完整句「我觉得青春像……因为……」', font=font(16), fill=INK, max_w=420)
# 板书+易错
card(d, 48, 495, 700, 120, accent=INK)
d.text((72, 518), '板书时机', font=font(17, bd=True), fill=INK)
text(d, 72, 548, '黑板中央写「青春」，外围圈学生回答关键词。', font=font(15), fill=INK, max_w=660)
card(d, 768, 495, 464, 120, accent=MUTED)
d.text((792, 518), '易错点提醒', font=font(17, bd=True), fill=MUTED)
text(d, 792, 548, '这不是自由讨论课，要聚焦「青春的价值」单元主题，及时收束。', font=font(15), fill=INK, max_w=420)
add(img, '08_step1')

# ---- P9 Step2 诵读感知 ----
img, d = new_page(9, TOTAL, 'Step 2 · 诵读感知')
d.text((48, 70), 'Step 2  诵读感知  First Reading', font=font(34, bd=True), fill=INK)
chip(d, 48, 122, '8 min', XIANG, font(16, bd=True))
card(d, 48, 170, 1184, 110, accent=FROST)
d.text((72, 192), '教师台词', font=font(18, bd=True), fill=FROST)
text(d, 72, 224, '教师范读一遍（注意「看/忆/问」三领字停顿）→ 播放方明朗诵音频 →「听完后，用一个词概括这首词给你的整体感受。」', font=font(17), fill=INK, max_w=1130)
card(d, 48, 295, 580, 160, accent=XIANG)
d.text((72, 318), '预设回答', font=font(18, bd=True), fill=XIANG)
for i,a in enumerate(['壮阔','豪迈','有力量']):
    d.text((72, 350+i*32), '·  '+a, font=font(17), fill=INK)
d.text((300, 318), '板书', font=font(16, bd=True), fill=MUTED)
d.text((300, 350), '在「青春」旁板书', font=font(15), fill=MUTED)
d.text((300, 378), '「壮阔·豪迈」', font=font(19, bd=True), fill=FROST)
card(d, 648, 295, 584, 160, accent=ACCENT)
d.text((672, 318), '易错点提醒', font=font(18, bd=True), fill=ACCENT)
text(d, 672, 350, '①「沁园春」是词牌名非题目，题目是「长沙」\n②「看万山红遍」的「看」字后须微顿，非一口气读完\n③ 三领字「看/忆/问」统领后文，停顿要有交代感', font=font(15), fill=INK, max_w=540)
card(d, 48, 470, 1184, 145, accent=INK)
d.text((72, 493), '差异化提示', font=font(18, bd=True), fill=INK)
text(d, 72, 525, 'B班：只需说感受词\nA班：需说出「哪一句让你有这种感觉」，把感受落到具体诗句。', font=font(16), fill=INK, max_w=1130)
add(img, '09_step2')

# ---- P10 Step3 圈点意象 ----
img, d = new_page(10, TOTAL, 'Step 3 · 圈点意象')
d.text((48, 70), 'Step 3  上阕精读 · 圈点意象', font=font(34, bd=True), fill=INK)
chip(d, 48, 122, '15 min', FROST, font(16, bd=True))
d.text((280, 126), '「看」字统领上阕景物 —— 圈意象 · 标特征 · 串联画面', font=font(16), fill=MUTED)
# 六意象卡片
yi = [
    ('万山','红遍','热烈·范围广',FROST,'山'),
    ('层林','尽染','层次·秋色深',FROST,'林'),
    ('漫江','碧透','澄澈·水深阔',XIANG,'江'),
    ('百舸','争流','动感·千帆发',XIANG,'舸'),
    ('鹰','击长空','力量·搏击',INK,'鹰'),
    ('鱼','翔浅底','自由·超越',XIANG,'鱼'),
]
iw, ih = 372, 150
for i,(name,mod,feat,c,icon) in enumerate(yi):
    col, row = i%3, i//3
    x, y = 48+col*(iw+22), 170+row*(ih+18)
    card(d, x, y, iw, ih, accent=c)
    d.text((x+22, y+22), name, font=font(26, bd=True), fill=c)
    d.text((x+22, y+62), '修饰：'+mod, font=font(17), fill=INK)
    d.text((x+22, y+92), '特征：'+feat, font=font(15), fill=MUTED)
    # 图标
    if icon=='鹰': draw_eagle_icon(d, x+iw-45, y+55, 30, c)
    elif icon=='鱼': draw_fish_icon(d, x+iw-45, y+60, 28, c)
    elif icon in ('山','林'): d.polygon([(x+iw-70,y+85),(x+iw-45,y+35),(x+iw-20,y+85)], fill=c)
    elif icon in ('江','舸'):
        d.rectangle([x+iw-70, y+60, x+iw-20, y+80], fill=c)
        if icon=='舸': d.polygon([(x+iw-40,y+55),(x+iw-25,y+70),(x+iw-40,y+70)], fill=INK)
# 分层
card(d, 48, 505, 1184, 110, accent=ACCENT)
d.text((72, 528), '差异化提示', font=font(18, bd=True), fill=ACCENT)
text(d, 72, 560, 'B班：只填前4个意象 + 修饰语\nA班：全部6组填写，并补「感受」列（如：鹰·击 → 搏击长空的雄心）', font=font(16), fill=INK, max_w=1130)
add(img, '10_step3')

# ---- P11 视角转换图 ----
img, d = new_page(11, TOTAL, '视角转换')
d.text((48, 70), '视角转换 · 湘江秋景图的镜头语言', font=font(34, bd=True), fill=INK)
d.text((48, 122), '【市场参考补缺】远近 · 仰俯 · 动静 三组对照，画面立体', font=font(16), fill=MUTED)
# 四象限
qx, qy, qw, qh = 300, 175, 680, 380
d.rectangle([qx, qy, qx+qw, qy+qh], fill=SOFT, outline=LINE, width=1)
d.line([(qx, qy+qh//2),(qx+qw, qy+qh//2)], fill=LINE, width=2)
d.line([(qx+qw//2, qy),(qx+qw//2, qy+qh)], fill=LINE, width=2)
quad = [
    (qx, qy, '远眺','万山红遍 · 层林尽染',FROST),
    (qx+qw//2, qy, '近观','漫江碧透 · 百舸争流',XIANG),
    (qx, qy+qh//2, '仰视','鹰击长空',INK),
    (qx+qw//2, qy+qh//2, '俯瞰','鱼翔浅底',XIANG),
]
for x,y,name,verse,c in quad:
    d.text((x+qw//4, y+50), name, font=font(26, bd=True), fill=c, anchor='mm')
    d.text((x+qw//4, y+95), verse, font=font(16), fill=INK, anchor='mm')
# 中心
d.ellipse([qx+qw//2-50, qy+qh//2-50, qx+qw//2+50, qy+qh//2+50], fill=ACCENT)
d.text((qx+qw//2, qy+qh//2-10), '总写', font=font(16, bd=True), fill=(255,255,255), anchor='mm')
d.text((qx+qw//2, qy+qh//2+12), '万类霜天\n竞自由', font=font(13), fill=(255,255,255), anchor='mm')
# 右侧解读
card(d, 1010, 175, 222, 380, accent=ACCENT)
d.text((1034, 198), '三组对照', font=font(18, bd=True), fill=ACCENT)
text(d, 1034, 235, '远 ↔ 近\n仰 ↔ 俯\n动 ↔ 静', font=font(18, bd=True), fill=INK)
text(d, 1034, 330, '镜头由远及近、由仰到俯，由静转动——一幅立体的、有呼吸的秋景。', font=font(15), fill=MUTED, max_w=180)
# 教学锚点
card(d, 48, 575, 1184, 60, accent=FROST)
d.text((72, 590), '教学锚点：让学生用「摄影镜头」比喻——诗人是导演，「看」字是开机键，七句是七个分镜。', font=font(16, bd=True), fill=FROST)
add(img, '11_view')

# ---- P12 Step4 炼字品析 ----
img, d = new_page(12, TOTAL, 'Step 4 · 炼字品析')
d.text((48, 70), 'Step 4  炼字品析 · 替换比较', font=font(34, bd=True), fill=INK)
chip(d, 48, 122, '10 min', ACCENT, font(16, bd=True))
# 击 vs 飞
card(d, 48, 170, 580, 230, accent=FROST)
d.text((72, 195), '鹰「击」长空  vs  鹰「飞」长空', font=font(19, bd=True), fill=FROST)
draw_eagle_icon(d, 560, 250, 28, FROST)
d.text((72, 240), '击', font=font(60, bd=True), fill=FROST)
text(d, 175, 250, '搏击 · 力量 · 矫健\n俯冲长空的力度感', font=font(17), fill=INK, max_w=350)
d.text((72, 330), '飞', font=font(28, bd=True), fill=MUTED)
d.text((175, 335), '平淡 · 缺力量', font=font(16), fill=MUTED)
# 翔 vs 游
card(d, 648, 170, 584, 230, accent=XIANG)
d.text((672, 195), '鱼「翔」浅底  vs  鱼「游」浅底', font=font(19, bd=True), fill=XIANG)
draw_fish_icon(d, 1160, 250, 26, XIANG)
d.text((672, 240), '翔', font=font(60, bd=True), fill=XIANG)
text(d, 775, 250, '翱翔 · 自由 · 超越\n赋鱼以鸟的自由感（比喻）', font=font(17), fill=INK, max_w=350)
d.text((672, 330), '游', font=font(28, bd=True), fill=MUTED)
d.text((775, 335), '平淡 · 缺张力', font=font(16), fill=MUTED)
# 十字炼字
card(d, 48, 420, 1184, 195, accent=INK)
d.text((72, 443), '【扩展】十字炼字表', font=font(19, bd=True), fill=INK)
d.text((72, 475), '万 · 遍 · 层 · 染 · 漫 · 透 · 百 · 争 · 击 · 翔 · 竞', font=font(22, bd=True), fill=FROST)
text(d, 72, 515, '万=山多  遍=红广  层=叠叠  染=秋深(拟人)  漫=水满  透=澄澈\n百=舸多  争=千帆发  击=矫健有力  翔=自由轻快  竞=蓬勃生命力', font=font(15), fill=INK, max_w=1130)
d.text((72, 588), '差异化：B班说出「哪个好」即可；A班说出「为什么好」——从力度、方向、情感色彩分析。', font=font(14, lt=True), fill=MUTED)
add(img, '12_step4')

# ---- P13 悲秋对照 ----
img, d = new_page(13, TOTAL, '悲秋对照')
d.text((48, 70), '悲秋对照 · 知人论世', font=font(34, bd=True), fill=INK)
d.text((48, 122), '【市场参考补缺·深度】为何毛泽东笔下的秋不悲？', font=font(16), fill=MUTED)
# 左：古人悲秋
card(d, 48, 165, 560, 360, accent=MUTED)
d.text((72, 190), '古人悲秋', font=font(24, bd=True), fill=MUTED)
guren = [
    ('杜甫《登高》','万里悲秋常作客，百年多病独登台'),
    ('马致远《天净沙》','枯藤老树昏鸦……断肠人在天涯'),
    ('李煜《相见欢》','寂寞梧桐深院锁清秋'),
    ('曹丕《燕歌行》','秋风萧瑟天气凉，草木摇落露为霜'),
]
gy = 235
for t,v in guren:
    d.text((72, gy), t, font=font(15, bd=True), fill=MUTED)
    d.text((72, gy+22), v, font=font(15), fill=INK)
    gy += 56
d.text((72, 500), '意象：黄花 / 枯草 / 寒蝉 / 暮鸦 —— 肃杀感伤', font=font(14, lt=True), fill=MUTED)
# 右：毛泽东颂秋
card(d, 632, 165, 600, 360, accent=FROST)
d.text((656, 190), '毛泽东颂秋', font=font(24, bd=True), fill=FROST)
draw_maple(d, 1160, 210, 16, FROST)
d.text((656, 240), '看万山红遍，层林尽染', font=font(18, bd=True), fill=FROST)
d.text((656, 272), '漫江碧透，百舸争流', font=font(18, bd=True), fill=XIANG)
d.text((656, 304), '鹰击长空，鱼翔浅底', font=font(18, bd=True), fill=INK)
d.text((656, 336), '万类霜天竞自由', font=font(18, bd=True), fill=ACCENT)
d.text((656, 390), '意象：红山 / 碧江 / 鹰 / 鱼 —— 绚烂 · 生机 · 壮阔', font=font(15, bd=True), fill=FROST)
# 知人论世
card(d, 48, 540, 1184, 85, accent=ACCENT)
d.text((72, 562), '为何不悲秋？· 知人论世', font=font(18, bd=True), fill=ACCENT)
text(d, 72, 590, '革命者胸怀 · 乐观向上永不消沉的性格 · 以天下为己任的抱负 —— 同样是秋，胸襟不同，笔下的秋便不同。', font=font(15), fill=INK, max_w=1130)
add(img, '13_autumn')

# ---- P14 Step5 情感推导 ----
img, d = new_page(14, TOTAL, 'Step 5 · 情感推导')
d.text((48, 70), 'Step 5  情感推导 · 从景到情', font=font(34, bd=True), fill=INK)
chip(d, 48, 122, '5 min', XIANG, font(16, bd=True))
# 景→问→情链
card(d, 48, 170, 1184, 160, accent=FROST)
d.text((72, 195), '情感脉络', font=font(20, bd=True), fill=FROST)
chain = [('景','壮阔',FROST),('→',None,MUTED),('问','谁主沉浮',ACCENT),('→',None,MUTED),('情','担当',XIANG)]
cx = 200
for lab,val,c in chain:
    if lab=='→':
        d.text((cx, 270), '→', font=font(40, bd=True), fill=MUTED)
        cx += 90
    else:
        d.rounded_rectangle([cx, 240, cx+180, 320], radius=12, fill=c)
        d.text((cx+90, 262), lab, font=font(26, bd=True), fill=(255,255,255), anchor='mm')
        d.text((cx+90, 295), val, font=font(16), fill=(255,255,255), anchor='mm')
        cx += 200
# 典故
card(d, 48, 345, 580, 245, accent=INK)
d.text((72, 368), '文化常识 · 典故', font=font(19, bd=True), fill=INK)
text(d, 72, 405, '① 万户侯：汉代最高一级侯爵，享万户赋税，后泛指高官贵爵。「粪土当年万户侯」= 视反动军阀如粪土。\n\n② 中流击楫：东晋祖逖北伐渡江，中流击桨誓曰「不能平定中原如江水一去不返」。「中流击水」化用此典，表革命雄心。', font=font(15), fill=INK, max_w=520)
# 分层
card(d, 648, 345, 584, 245, accent=ACCENT)
d.text((672, 368), '差异化提示 + 易错', font=font(19, bd=True), fill=ACCENT)
text(d, 672, 405, 'B班：说出「他在关心国家命运」即可\nA班：说出「景物壮阔暗示力量积蓄，问句表达革命者主动担当的豪情」\n\n易错：「沉浮」指国家命运兴衰，非字面浮沉；联系「主」字理解为「主宰」。', font=font(15), fill=INK, max_w=540)
add(img, '14_step5')

# ---- P15 板书设计 ----
img, d = new_page(15, TOTAL, '板书设计')
d.text((48, 70), '板书设计', font=font(34, bd=True), fill=INK)
# 板书框
bx, by, bw, bh = 200, 150, 880, 470
d.rectangle([bx, by, bx+bw, by+bh], fill=(250,248,243), outline=INK, width=3)
d.text((bx+bw//2, by+30), '沁园春·长沙', font=font(26, bd=True), fill=INK, anchor='mm')
d.line([(bx+40, by+60),(bx+bw-40, by+60)], fill=LINE, width=1)
# 青春
d.text((bx+bw//2, by+90), '青春：壮阔 · 豪迈', font=font(20, bd=True), fill=FROST, anchor='mm')
# 意象表
d.text((bx+40, by+135), '看 → 景（意象）', font=font(18, bd=True), fill=INK)
rows = [('万山','红','热烈'),('层林','染','层次'),('漫江','碧','澄澈'),('百舸','争','动感'),('鹰','击','力量 ←炼字'),('鱼','翔','自由 ←炼字')]
ry = by+170
for n,m,f in rows:
    d.text((bx+60, ry), n, font=font(16, bd=True), fill=FROST)
    d.text((bx+200, ry), '| '+m, font=font(16), fill=INK)
    d.text((bx+320, ry), '| '+f, font=font(16), fill=INK)
    ry += 28
# 炼字
d.text((bx+480, by+170), '炼字', font=font(18, bd=True), fill=ACCENT)
d.text((bx+480, by+205), '击 → 力量·搏击', font=font(16), fill=ACCENT)
d.text((bx+480, by+235), '翔 → 自由·超越', font=font(16), fill=ACCENT)
# 情感链
d.text((bx+40, by+360), '景 → 问 → 情', font=font(18, bd=True), fill=INK)
d.text((bx+60, by+395), '壮阔  沉浮  担当', font=font(15), fill=MUTED)
# 四步法
d.text((bx+480, by+360), '【读诗四步法】', font=font(17, bd=True), fill=XIANG)
text(d, bx+480, by+395, '圈意象 → 标特征\n→ 串联画面 → 推导情感', font=font(15), fill=INK, max_w=300)
add(img, '15_blackboard')

# ---- P16 分层作业 ----
img, d = new_page(16, TOTAL, '分层作业')
d.text((48, 70), '分层作业', font=font(34, bd=True), fill=INK)
# 基础
card(d, 48, 145, 580, 300, accent=XIANG)
d.text((72, 170), '基础作业', font=font(22, bd=True), fill=XIANG)
text(d, 72, 215, '1. 背诵并默写《沁园春·长沙》上阕，要求书写规范、标点正确。\n\n2. 完成意象表格（意象 | 修饰语 | 特征 | 感受），至少6组。', font=font(16), fill=INK, max_w=520)
# 提高
card(d, 648, 145, 584, 300, accent=FROST)
d.text((672, 170), '提高作业', font=font(22, bd=True), fill=FROST)
text(d, 672, 215, '从「击 / 翔 / 染 / 争」中任选一字，写一段150字炼字品析：\n① 该字的字面义\n② 该字营造的画面感\n③ 该字传达的情感', font=font(16), fill=INK, max_w=520)
# 参考答案
card(d, 48, 460, 1184, 175, accent=MUTED)
d.text((72, 483), '参考答案 —— 教师用', font=font(18, bd=True), fill=MUTED)
text(d, 72, 515, '基础2 示例：万山 | 红遍 | 热烈 | 如火的革命激情；鹰 | 击长空 | 力量 | 搏击长空的雄心。\n提高（以「击」为例）：「击」字面为搏击、敲击，营造鹰俯冲长空的力量画面，传达革命者不畏艰险、主动出击的豪情。能写出三点即满分；能对比「飞」字的平淡再加1分。', font=font(15), fill=INK, max_w=1130)
add(img, '16_homework')

# ---- P17 小结反思 ----
img, d = new_page(17, TOTAL, '小结反思')
d.text((48, 70), '小结 · 读诗四步法', font=font(34, bd=True), fill=INK)
# 四步法大图
card(d, 48, 140, 1184, 170, accent=XIANG)
d.text((72, 165), '读诗四步法', font=font(22, bd=True), fill=XIANG)
steps4 = [('① 圈意象','找出诗中物象'),('② 标特征','标注修饰与特点'),('③ 串联画面','组合成完整图景'),('④ 推导情感','由景及情升华')]
sx = 72
for t,b in steps4:
    d.rounded_rectangle([sx, 215, sx+260, 280], radius=10, fill=SOFT, outline=LINE)
    d.text((sx+130, 233), t, font=font(18, bd=True), fill=XIANG, anchor='mm')
    d.text((sx+130, 260), b, font=font(14), fill=MUTED, anchor='mm')
    sx += 290
# 反思
card(d, 48, 325, 580, 305, accent=FROST)
d.text((72, 350), '教学反思', font=font(20, bd=True), fill=FROST)
text(d, 72, 390, '✅ 亮点：替换比较法（击→飞）让学生直观感受炼字之妙，B班参与度明显高于平时；意象表格支架有效降低品析门槛。\n\n⚠️ 需改进：时代背景介绍偏短，部分学生对「谁主沉浮」仍停留在字面；下次增加时间轴图示（本版已补）。\n\n📌 下节衔接：下阕「忆青春」——「同学少年」与上阕秋景对照，从「问」到「答」，回扣本课「景→问→情」脉络。', font=font(14), fill=INK, max_w=520)
card(d, 648, 325, 584, 305, accent=ACCENT)
d.text((672, 350), '本课升级说明', font=font(20, bd=True), fill=ACCENT)
text(d, 672, 390, '本版融合市场验证课件（学科网/21cnjy）补缺：\n· 文体知识页（词/词牌/分类）\n· 系统朗读指导（字音/节拍/情感曲线）\n· 四幅图全词结构框架\n· 视角转换图（远近仰俯动静）\n· 十字炼字扩展\n· 悲秋对照·知人论世\n· 万户侯/中流击楫典故\n\n保留我们差异化：教师台词/学生预设/A·B分层/易错点/板书/分层作业。', font=font(13), fill=INK, max_w=540)
add(img, '17_summary')

# ---- P18 封底 ----
img, d = new_page(18, TOTAL)
d.rectangle([0, 0, W, H], BG)
d.rectangle([0, H//2-2, W, H//2+2], fill=ACCENT)
d.text((W//2, H//2-90), '沁园春·长沙', font=font(50, bd=True), fill=INK, anchor='mm')
d.text((W//2, H//2-40), '意象与情感 · 第一课时', font=font(22), fill=FROST, anchor='mm')
d.text((W//2, H//2+50), '问苍茫大地，谁主沉浮？', font=font(24, lt=True), fill=MUTED, anchor='mm')
d.text((W//2, H//2+95), '—— 同学少年，风华正茂 ——', font=font(16, lt=True), fill=MUTED, anchor='mm')
d.text((W//2, H-50), '高中语文教案 · v3 精美版  |  必修上册 第一单元', font=font(13, lt=True), fill=MUTED, anchor='mm')
add(img, '18_end')

# ==================== 输出 ====================
for i,(im, name) in enumerate(PAGES):
    im.save(os.path.join(OUT, f'slide_{i+1:02d}_{name}.png'))
print(f'已渲染 {len(PAGES)} 页 → {OUT}')

# 合成 PDF
imgs = [Image.open(os.path.join(OUT, f'slide_{i+1:02d}_{n}.png')).convert('RGB') for i,(im,n) in enumerate(PAGES)]
pdf_path = os.path.join(os.path.dirname(OUT), '高一语文-沁园春长沙-v3精美版.pdf')
imgs[0].save(pdf_path, 'PDF', resolution=150, save_all=True, append_images=imgs[1:])
print(f'PDF → {pdf_path} ({os.path.getsize(pdf_path)//1024} KB, {len(imgs)} 页)')
