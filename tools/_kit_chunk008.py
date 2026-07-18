# -*- coding: utf-8 -*-
"""chunk_008 批专用共享渲染套件（不覆盖他人已建文件）。

复用 _fine_render 的 9 页构建函数与 _classroom_lib 设计系统；
背景页支持「可选真实照片」：照片 + 墨蓝遮罩(INK, 55%) + 白色来源文字，
该遮罩即审计所需的 protective 层，可安全通过四层审计；
无契合照片则学科色块兜底，并标注「本课件未使用无关配图」。

页面结构（学生视角、中性口吻，无「教师/老师」字样）：
封面 / 学习目标 / 背景与权威调研 / 重点 / 方法 / 难点 / 板书精华 / 作业 / 单元小结
"""
import os, json
from _fine_render import (
    load, clean, split_lines, strip_key, cn,
    s_cover, s_objectives, s_keypoints, s_methods, s_difficulties,
    s_blackboard, s_exercises, s_summary,
    new_presentation, new_slide,
)
from _classroom_lib import (
    PAPER, INK, FROST, XIANG, MUTED, WHITE, GOLD, SOFT,
    KAI, HEI, W, H, M, CW, Inches, Pt, MSO_SHAPE, PP_ALIGN,
    set_ea, bg, textbox, rule, kicker, page_num, place_photo, scrim,
)

HERE = os.path.dirname(os.path.abspath(__file__))

# 仅允许 tools/_photos_u2_* 中已下载的自由授权真实照片；清单见规范 §照片 条。
_ALLOWED_PHOTOS = {
    "harvest.jpg", "ricefield.jpg", "plantago.jpg", "tibet.jpg",
    "wangfujing.jpg", "zhang_binggui.jpg", "craft.jpg", "renmin.jpg",
    "watch.jpg", "mic.jpg", "vintagemic.jpg", "ctype.jpg", "typewriter.jpg",
}

def _find_photo(name):
    if not name or name not in _ALLOWED_PHOTOS:
        return None
    for root, _, files in os.walk(HERE):
        if os.path.basename(root).startswith('_photos_u2'):
            if name in files:
                return os.path.join(root, name)
    # 兜底：全盘查找
    for root, _, files in os.walk(HERE):
        if name in files:
            return os.path.join(root, name)
    return None

def s_background(s, d, ex, photo=None):
    bg(s, PAPER)
    kicker(s, '背景与权威调研', M, M, FROST)
    col_w = (CW - Inches(0.5)) / 2
    lx = M
    ta = clean(d.get('textbookAnalysis', ''))
    textbox(s, lx, M + Inches(1.25), col_w, Inches(4.7),
            [{'text': ta, 'size': 14.5, 'color': INK, 'font': KAI, 'line': 1.5, 'space_after': 8}])
    rx = M + col_w + Inches(0.5)
    panel_y = M + Inches(1.25)
    panel_h = Inches(4.7)
    path = _find_photo(photo) if photo else None
    if path:
        place_photo(s, path, rx, panel_y, col_w, panel_h)
        scrim(s, rx, panel_y, col_w, panel_h, INK, 55)
        textbox(s, rx + Inches(0.3), panel_y + Inches(0.2), col_w - Inches(0.6), Inches(0.5),
                [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
        src_paras = [{'text': '· ' + clean(src), 'size': 12.5, 'color': WHITE, 'font': KAI,
                      'line': 1.45, 'space_after': 7}
                     for src in ex['sources'] if clean(src).strip()]
        src_paras.append({'text': '配图：%s（Wikimedia Commons，自由授权）' % photo,
                          'size': 10.5, 'color': SOFT, 'font': HEI, 'line': 1.3, 'space_before': 6})
        textbox(s, rx + Inches(0.3), panel_y + Inches(0.8), col_w - Inches(0.6), panel_h - Inches(1.0), src_paras)
        page_num(s)
        return
    # 学科色块兜底（无契合真实照片）
    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, panel_y, col_w, panel_h)
    panel.fill.solid(); panel.fill.fore_color.rgb = INK; panel.shadow.inherit = False
    textbox(s, rx + Inches(0.3), panel_y + Inches(0.2), col_w - Inches(0.6), Inches(0.5),
            [{'text': '权威来源', 'size': 16, 'color': GOLD, 'bold': True, 'font': KAI}])
    src_paras = [{'text': '· ' + clean(src), 'size': 12.5, 'color': WHITE, 'font': KAI,
                  'line': 1.45, 'space_after': 7}
                 for src in ex['sources'] if clean(src).strip()]
    src_paras.append({'text': '本课件未使用无关配图（学科色块兜底）',
                      'size': 11.5, 'color': SOFT, 'font': HEI, 'line': 1.4, 'space_before': 6})
    textbox(s, rx + Inches(0.3), panel_y + Inches(0.8), col_w - Inches(0.6), panel_h - Inches(1.0), src_paras)
    page_num(s)

def render(lesson_id, lead, sources, photo=None):
    d = load(lesson_id)
    ex = {"lead": lead, "sources": sources}
    for k in ('title', 'book', 'unitTitle'):
        d[k] = clean(d.get(k, ''))
    prs, BLANK = new_presentation()
    seq = [
        lambda s: s_cover(s, d, ex),
        lambda s: s_objectives(s, d),
        lambda s: s_background(s, d, ex, photo),
        lambda s: s_keypoints(s, d),
        lambda s: s_methods(s, d),
        lambda s: s_difficulties(s, d),
        lambda s: s_blackboard(s, d),
        lambda s: s_exercises(s, d),
        lambda s: s_summary(s, d),
    ]
    for fn in seq:
        fn(new_slide(prs, BLANK))
    out = os.path.join(HERE, '..', 'preview_v7', 'cn', '%s.pptx' % lesson_id)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    prs.save(out)
    print('SAVED', out, 'slides=', len(prs.slides._sldIdLst))
