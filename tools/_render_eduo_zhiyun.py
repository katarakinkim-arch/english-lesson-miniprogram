# -*- coding: utf-8 -*-
# 《峨日朵雪峰之侧 / 致云雀》群文 课堂学生版 PPT 渲染器（手写精排，import 共享库）
# 融合来源：人教版优质课/实录共识招牌招式（昌耀·雪莱）
#   · 峨日朵：意象对比（雄奇壮美 vs 渺小柔弱）、「仅能征服的高度」、视听合一、知人论世（1962 困厄）
#   · 致云雀：「你好啊欢乐的精灵」、云雀=理想自我、通感（银色星光利箭）、比喻链、浪漫主义
#   · 群文：谦卑坚守 vs 欢唱自由、中西浪漫主义并置、青春价值单元呼应
import os
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, place_photo, scrim, textbox, rule, kicker,
    new_slide, page_num, caption, quote_block, step_card,
    new_presentation,
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO = {
    'snowpeak': os.path.join(BASE, 'preview_v7', '_eduo_zhiyun_photos', 'real_snowpeak.jpg'),
    'spider':   os.path.join(BASE, 'preview_v7', '_eduo_zhiyun_photos', 'real_spider.jpg'),
    'sunset':   os.path.join(BASE, 'preview_v7', '_eduo_zhiyun_photos', 'real_sunset.jpg'),
    'cliff':    os.path.join(BASE, 'preview_v7', '_eduo_zhiyun_photos', 'real_cliff.jpg'),
    'skylark':  os.path.join(BASE, 'preview_v7', '_eduo_zhiyun_photos', 'real_skylark.jpg'),
}

prs, BLANK = new_presentation()

# ---------- P1 封面 ----------
def s_cover(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['snowpeak'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.50)
    rule(s, M, M + Inches(0.45), Inches(0.9), GOLD, 3)
    textbox(s, M, M + Inches(0.65), Inches(10), Inches(0.5),
            [{'text': '必修上 第一单元 · 群文阅读', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, Inches(2.2), Inches(12), Inches(2.2),
            [{'text': '峨日朵雪峰之侧', 'size': 44, 'color': WHITE, 'bold': True, 'font': KAI},
             {'text': '致　云　雀', 'size': 44, 'color': WHITE, 'bold': True, 'font': KAI, 'space_before': 8}])
    textbox(s, M, Inches(4.7), Inches(12), Inches(0.7),
            [{'text': '昌　耀　·　雪　莱　两代诗人的青春之歌', 'size': 19, 'color': SOFT, 'font': HEI}])
    textbox(s, M, Inches(5.6), Inches(12), Inches(1.2),
            [{'text': '一座雪峰上的坚守，一只云雀里的飞翔——', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.4, 'space_after': 4},
             {'text': '谦卑与自由，都是青春面向理想的方式。', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.4}])
    page_num(s)


# ---------- P2 导览 ----------
def s_contents(s):
    bg(s, PAPER)
    kicker(s, '本课导览', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(10), Inches(0.8),
            [{'text': '十二步读懂两首诗', 'size': 32, 'color': INK, 'bold': True, 'font': KAI}])
    items = [
        ('01', '导入：雪峰之侧，谁守高度？'),
        ('02', '知人论世：昌耀的困厄与高度'),
        ('03', '《峨日朵》意象对比：雄奇 vs 渺小'),
        ('04', '《峨日朵》视听合一：落日与嚣鸣'),
        ('05', '「仅能征服的高度」读懂「此刻·仅」'),
        ('06', '《致云雀》导入：欢乐的精灵'),
        ('07', '《致云雀》云雀=理想自我（比喻链）'),
        ('08', '《致云雀》通感：银色星光的利箭'),
        ('09', '群文比较：谦卑坚守 vs 欢唱自由'),
        ('10', '学法：意象 → 象征 → 情感'),
        ('11', '青春的价值 · 单元呼应'),
        ('12', '分层作业'),
    ]
    paras = []
    for num, t in items:
        paras.append({'size': 15, 'color': INK, 'font': KAI, 'line': 1.25, 'space_after': 5,
                      'runs': [{'text': num + '  ', 'size': 15, 'color': FROST, 'bold': True, 'font': HEI},
                               {'text': t, 'size': 15, 'color': INK, 'font': KAI}]})
    textbox(s, M, M + Inches(1.7), CW, Inches(5.0), paras)
    page_num(s)


# ---------- P3 导入：雪峰与蜘蛛 ----------
def s_eduo_intro(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['snowpeak'], W - M - Inches(4.4), M, Inches(4.4), Inches(3.7))
    caption(s, '峨日朵雪峰 · 雄奇冷峻', W - M - Inches(4.4), M + Inches(3.8), Inches(4.4))
    place_photo(s, PHOTO['spider'], W - M - Inches(4.4), Inches(4.7), Inches(4.4), Inches(2.1))
    caption(s, '岩壁上的蜘蛛 · 渺小征服者', W - M - Inches(4.4), Inches(6.9), Inches(4.4))
    kicker(s, '导入 · 两个画面', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.8), Inches(0.6),
            [{'text': '雪峰之侧，谁在坚守高度？', 'size': 27, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(6.9), Inches(5.0),
            [{'text': '一边是峨日朵雪峰——雄奇、冷峻、高耸入云；一边是岩壁上渺小得可怜的蜘蛛。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '昌耀把镜头对准了这两个反差极大的画面。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '读了标题，你猜：守住高度的，会是强大的雄鹰、雪豹，还是这只不起眼的小蜘蛛？', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P4 知人论世：昌耀 ----------
def s_eduo_bg(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['cliff'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.56)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '知人论世 · 1962 的青海', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, M + Inches(1.3), Inches(11.5), Inches(0.8),
            [{'text': '昌耀：在困厄中站稳高度', 'size': 30, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(2.4), Inches(11.5), Inches(4.2),
            [{'text': '1956 年，19 岁的昌耀奔赴青海，投身大西北开发建设。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '1962 年写此诗时，他正遭受不公正待遇，在青海八宝农场劳动改造。', 'size': 17, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 14},
             {'text': '但他没有消沉——「在峨日朵雪峰之侧站稳了自己的高度」。这首诗，是精神不随时代「滑坡」的宣言。', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P5 意象对比：雄奇壮美 vs 渺小柔弱 ----------
def s_eduo_imagery(s):
    bg(s, PAPER)
    kicker(s, '《峨日朵》意象解码 · 强烈的反差', M, M, FROST)
    place_photo(s, PHOTO['sunset'], M, M + Inches(1.4), Inches(3.8), Inches(2.4))
    caption(s, '太阳 · 决然跃入山海', M, M + Inches(3.9), Inches(3.8))
    place_photo(s, PHOTO['cliff'], M + Inches(4.0), M + Inches(1.4), Inches(3.8), Inches(2.4))
    caption(s, '石砾 · 滑坡引动深渊嚣鸣', M + Inches(4.0), M + Inches(3.9), Inches(3.8))
    place_photo(s, PHOTO['spider'], M + Inches(8.0), M + Inches(1.4), Inches(3.8), Inches(2.4))
    caption(s, '蜘蛛 · 小得可怜', M + Inches(8.0), M + Inches(3.9), Inches(3.8))
    # 三组对比说明
    cw = (CW - Inches(0.3) * 2) / 3
    y = M + Inches(4.4)
    cards = [
        ('雄奇壮美组', '太阳 · 山海 · 石砾 · 深渊 · 巨石——营造阔大、险峻、壮美的氛围。', FROST),
        ('渺小柔弱组', '雄鹰、雪豹象征「强大」，蜘蛛象征「弱小」——形成强与弱的对照。', XIANG),
        ('惊人反转', '守住高度的不是雄鹰雪豹，而是小蜘蛛：真正的强大，是内在的精神。', GOLD),
    ]
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.3))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.18), cw - Inches(0.5), Inches(0.5),
                [{'text': t, 'size': 17, 'color': col, 'bold': True, 'font': HEI}])
        textbox(s, x + Inches(0.25), y + Inches(0.72), cw - Inches(0.5), Inches(1.4),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P6 视听合一 ----------
def s_eduo_av(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['sunset'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.54)
    textbox(s, M, M + Inches(0.6), Inches(11), Inches(0.5),
            [{'text': '《峨日朵》· 视听合一', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M, M + Inches(1.25), Inches(11.6), Inches(0.7),
            [{'text': '落日下坠，嚣鸣远去', 'size': 28, 'color': WHITE, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(2.2), CW,
                '正决然跃入一片引力无穷的山海。石砾不时滑坡，引动棕色深渊自上而下的一派嚣鸣，像军旅远去的喊杀声。',
                '《峨日朵雪峰之侧》', GOLD)
    textbox(s, M, M + Inches(4.5), CW, Inches(2.1),
            [{'text': '视觉：辉煌的落日决然下坠；听觉：滑坡石砾引动深渊嚣鸣，如军旅杀声渐远。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '视听合一，不只产生审美上的「崇高」，更在读者生理上引发一种紧张。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '而这一切「下坠」，正与攀登者向上的动势相反——衬托出人物内心的悲壮与坚忍。', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P7 仅能征服的高度 ----------
def s_eduo_height(s):
    bg(s, PAPER)
    kicker(s, '《峨日朵》· 诗眼', M, M, FROST)
    quote_block(s, M, M + Inches(1.2), CW, '这是我此刻仅能征服的高度了。', '《峨日朵雪峰之侧》结句', FROST)
    cards = [
        ('「此刻」', '说明他是「还未登顶」的攀登者——高度是此时此刻拼尽全力达到的，而非终点。', FROST),
        ('「仅」', '暗示目标与努力之间仍有差距；却不放弃，仍要继续征服下一个高度。', XIANG),
        ('「征服」', '登山象征对苦难的挑战；蜘蛛与我同享快慰——平凡生命也有精神的高度。', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(4.3)
    for i, (t, b, col) in enumerate(cards):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.2))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        textbox(s, x + Inches(0.25), y + Inches(0.18), cw - Inches(0.5), Inches(0.5),
                [{'text': t, 'size': 19, 'color': col, 'bold': True, 'font': KAI}])
        textbox(s, x + Inches(0.25), y + Inches(0.78), cw - Inches(0.5), Inches(1.3),
                [{'text': b, 'size': 14, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P8 致云雀导入：欢乐的精灵 ----------
def s_zhiyun_intro(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['skylark'], W - M - Inches(4.6), M, Inches(4.6), Inches(4.6))
    caption(s, '云雀 · 欢乐的精灵', W - M - Inches(4.6), M + Inches(4.7), Inches(4.6))
    kicker(s, '导入 · 一只鸟', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(6.8), Inches(0.6),
            [{'text': '你好啊，欢乐的精灵！', 'size': 27, 'color': INK, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.7), Inches(6.9), Inches(4.8),
            [{'text': '雪莱一落笔，就向云雀打招呼——不是写一只鸟，而是招呼一个「欢乐的精灵」。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '现实中的云雀，身形与麻雀相似，并不起眼。', 'size': 15, 'color': MUTED, 'font': KAI, 'line': 1.6, 'space_after': 12},
             {'text': '但雪莱笔下的云雀，被心中的烈火染红，成了欢乐、光明、自由的化身——这是诗人理想自我的外化。', 'size': 15, 'color': FROST, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P9 云雀=理想自我（比喻链） ----------
def s_zhiyun_symbol(s):
    bg(s, PAPER)
    place_photo(s, PHOTO['skylark'], 0, 0, W, H)
    scrim(s, 0, 0, W, H, INK, 0.55)
    kicker(s, '《致云雀》· 象征', M, M, GOLD)
    textbox(s, M, M + Inches(0.8), Inches(11), Inches(0.6),
            [{'text': '云雀，是诗人的理想自我', 'size': 28, 'color': WHITE, 'bold': True, 'font': KAI}])
    textbox(s, M, M + Inches(1.8), Inches(11.5), Inches(2.4),
            [{'text': '雪莱把云雀比作——', 'size': 17, 'color': GOLD, 'bold': True, 'font': KAI, 'space_after': 6},
             {'text': '诗人（真情流露）· 深闺少女（为爱所苦）· 萤火虫（光明不露形影）· 玫瑰（幽闭吐香）', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6, 'space_after': 10},
             {'text': '云雀振翅高飞＝诗人执着奋进；隐形播歌＝不求名利、只为唤起人间爱与同情。', 'size': 16, 'color': WHITE, 'font': KAI, 'line': 1.6}])
    # 凡人 vs 云雀
    cw = (CW - Inches(0.4)) / 2
    c1 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(4.5), cw, Inches(2.2))
    c1.fill.solid(); c1.fill.fore_color.rgb = WHITE; c1.line.color.rgb = MUTED; c1.line.width = Pt(1.3); c1.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(4.7), cw - Inches(0.6), Inches(0.5),
            [{'text': '凡人（现实中的我）', 'size': 16, 'color': MUTED, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(5.3), cw - Inches(0.6), Inches(1.3),
            [{'text': '前瞻后顾，渴求虚无之物，被现实束缚，永远为外物所累。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.5}])
    c2 = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(4.5), cw, Inches(2.2))
    c2.fill.solid(); c2.fill.fore_color.rgb = WHITE; c2.line.color.rgb = XIANG; c2.line.width = Pt(1.6); c2.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(4.7), cw - Inches(0.6), Inches(0.5),
            [{'text': '云雀（理想中的我）', 'size': 16, 'color': XIANG, 'bold': True, 'font': HEI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(5.3), cw - Inches(0.6), Inches(1.3),
            [{'text': '追求光明、蔑视地面、超越痛苦，向往理想世界——欢乐、自由、美丽。', 'size': 15, 'color': INK, 'font': KAI, 'line': 1.5}])
    page_num(s)


# ---------- P10 通感与比喻链 ----------
def s_zhiyun_synaesthesia(s):
    bg(s, PAPER)
    kicker(s, '《致云雀》· 修辞的奇崛', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '通感：把声音「看」成光', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.6), CW,
                '那犀利无比的乐音，似银色星光的利箭——', '《致云雀》第 4 节', FROST)
    cw = (CW - Inches(0.4)) / 2
    lc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(4.4), cw, Inches(2.3))
    lc.fill.solid(); lc.fill.fore_color.rgb = WHITE; lc.line.color.rgb = FROST; lc.line.width = Pt(1.6); lc.shadow.inherit = False
    textbox(s, M + Inches(0.3), M + Inches(4.6), cw - Inches(0.6), Inches(0.5),
            [{'text': '通感（移觉）', 'size': 17, 'color': FROST, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(0.3), M + Inches(5.2), cw - Inches(0.6), Inches(1.4),
            [{'text': '「乐音」像「银色星光利箭」——听觉化作视觉。写云雀歌声的高亢嘹亮，新奇而空灵。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    rc = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M + cw + Inches(0.4), M + Inches(4.4), cw, Inches(2.3))
    rc.fill.solid(); rc.fill.fore_color.rgb = WHITE; rc.line.color.rgb = XIANG; rc.line.width = Pt(1.6); rc.shadow.inherit = False
    textbox(s, M + cw + Inches(0.7), M + Inches(4.6), cw - Inches(0.6), Inches(0.5),
            [{'text': '比喻的奇想', 'size': 17, 'color': XIANG, 'bold': True, 'font': HEI}])
    textbox(s, M + cw + Inches(0.7), M + Inches(5.2), cw - Inches(0.6), Inches(1.4),
            [{'text': '「像一片烈火的轻云，掠过蔚蓝的天心」——红与蓝强烈反差，写出云雀一跃而上、边飞边唱的飒爽。', 'size': 14, 'color': INK, 'font': KAI, 'line': 1.55}])
    page_num(s)


# ---------- P11 群文比较：谦卑坚守 vs 欢唱自由 ----------
def s_compare(s):
    bg(s, PAPER)
    kicker(s, '群文比较 · 两种浪漫', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '同写理想，气象各不同', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    hdr = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, M + Inches(1.6), CW, Inches(0.6))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = INK; hdr.shadow.inherit = False
    textbox(s, M + Inches(0.25), M + Inches(1.68), Inches(3.0), Inches(0.45),
            [{'text': '比较维度', 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(3.6), M + Inches(1.68), Inches(4.0), Inches(0.45),
            [{'text': '《峨日朵》昌耀', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    textbox(s, M + Inches(8.0), M + Inches(1.68), Inches(4.0), Inches(0.45),
            [{'text': '《致云雀》雪莱', 'size': 15, 'color': GOLD, 'bold': True, 'font': HEI}])
    rows = [
        ('国度/流派', '中国当代诗', '英国浪漫主义'),
        ('主体形象', '贴壁攀登者', '高飞欢唱的云雀'),
        ('精神气质', '谦卑 · 坚守', '自由 · 欢唱'),
        ('核心手法', '意象对比·视听合一', '比喻·通感·对比'),
        ('面对落差', '承认有限，仍向上', '感受遥远，仍飞升'),
    ]
    y = M + Inches(2.35)
    for dim, a, b in rows:
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, M, y, CW, Inches(0.78))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = MUTED; card.line.width = Pt(0.8); card.shadow.inherit = False
        textbox(s, M + Inches(0.25), y + Inches(0.16), Inches(3.0), Inches(0.5),
                [{'text': dim, 'size': 15, 'color': INK, 'bold': True, 'font': HEI}])
        textbox(s, M + Inches(3.6), y + Inches(0.16), Inches(4.0), Inches(0.5),
                [{'text': a, 'size': 14, 'color': FROST, 'font': KAI}])
        textbox(s, M + Inches(8.0), y + Inches(0.16), Inches(4.0), Inches(0.5),
                [{'text': b, 'size': 14, 'color': XIANG, 'font': KAI}])
        y += Inches(0.86)
    page_num(s)


# ---------- P12 学法：意象 → 象征 → 情感 ----------
def s_method(s):
    bg(s, PAPER)
    kicker(s, '学法小结 · 现代诗研读路径', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '三步读懂一首现代诗', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    steps = [
        ('找意象', '圈出物象：雪峰、蜘蛛、云雀、星光……抓住画面。', FROST),
        ('明象征', '物象承载什么情志：坚守、谦卑、欢乐、自由……', XIANG),
        ('悟情感', '由象征抵达诗人心境与时代精神，读出青春的姿态。', GOLD),
    ]
    y = M + Inches(1.8)
    for i, (t, b, col) in enumerate(steps):
        step_card(s, M, y, CW, Inches(1.35), i + 1, t, [b], col)
        y += Inches(1.5)
    page_num(s)


# ---------- P13 青春的价值（单元呼应） ----------
def s_youth(s):
    bg(s, PAPER)
    kicker(s, '青春的价值 · 单元呼应', M, M, FROST)
    textbox(s, M, M + Inches(0.75), CW, Inches(0.6),
            [{'text': '坚守与飞翔，都是青春', 'size': 28, 'color': INK, 'bold': True, 'font': KAI}])
    quote_block(s, M, M + Inches(1.6), CW,
                '《峨日朵》以谦卑守住精神的高度，《致云雀》以欢唱飞向理想的晴空——一守一飞，都是青春面向理想的姿态。',
                '第一单元 · 青春的价值', FROST)
    textbox(s, M, M + Inches(4.3), CW, Inches(2.0),
            [{'text': '本单元还读《沁园春·长沙》的豪迈、《红烛》的赤诚、《百合花》《哦，香雪》的纯真——', 'size': 16, 'color': INK, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '青春从不是单一模样：它可以呐喊，可以低语，可以壮阔，也可以温柔。', 'size': 16, 'color': INK, 'bold': True, 'font': KAI, 'line': 1.6, 'space_after': 8},
             {'text': '重要的是——心怀理想，勇于超越。', 'size': 16, 'color': XIANG, 'bold': True, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- P14 作业（分层） ----------
def s_homework(s):
    bg(s, PAPER)
    kicker(s, '作业 · 分层', M, M, FROST)
    textbox(s, M, M + Inches(0.75), Inches(11), Inches(0.6),
            [{'text': '基础 · 提升 · 拓展', 'size': 26, 'color': INK, 'bold': True, 'font': KAI}])
    tiers = [
        ('基础 · 必做', '有感情朗读两首诗；从每首找出 3 个意象，写出其象征义。', FROST),
        ('提升 · 选做', '写一首 8 行内现代诗，以「青春的____」为题，用≥2 个意象承载情感。', XIANG),
        ('拓展 · 实践', '对比昌耀与雪莱：一个在雪峰之侧坚守，一个向晴空飞升，你更共鸣哪一种青春？', GOLD),
    ]
    cw = (CW - Inches(0.4) * 2) / 3
    y = M + Inches(1.7)
    for i, (tag, body, col) in enumerate(tiers):
        x = M + i * (cw + Inches(0.4))
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(2.7))
        card.fill.solid(); card.fill.fore_color.rgb = WHITE; card.line.color.rgb = col; card.line.width = Pt(1.6); card.shadow.inherit = False
        tagbar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.55))
        tagbar.fill.solid(); tagbar.fill.fore_color.rgb = col; tagbar.line.fill.background(); tagbar.shadow.inherit = False
        textbox(s, x, y + Inches(0.1), cw, Inches(0.4),
                [{'text': tag, 'size': 15, 'color': WHITE, 'bold': True, 'font': HEI, 'align': PP_ALIGN.CENTER}])
        textbox(s, x + Inches(0.25), y + Inches(0.75), cw - Inches(0.5), Inches(1.8),
                [{'text': body, 'size': 15, 'color': INK, 'font': KAI, 'line': 1.6}])
    page_num(s)


# ---------- BUILD ----------
for fn in [s_cover, s_contents, s_eduo_intro, s_eduo_bg, s_eduo_imagery, s_eduo_av,
           s_eduo_height, s_zhiyun_intro, s_zhiyun_symbol, s_zhiyun_synaesthesia,
           s_compare, s_method, s_youth, s_homework]:
    fn(new_slide(prs, BLANK))

OUT = os.path.join(BASE, 'preview_v7', 'eduo_zhiyun.pptx')
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
