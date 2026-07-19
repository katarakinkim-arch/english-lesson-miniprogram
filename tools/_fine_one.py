# -*- coding: utf-8 -*-
"""Per-lesson FINE renderer (genuine fine-tuning).

Reuses the proven 9-page hand-tuned structure from _render_lesson.py (geometry already
passes the 4-layer audit), but:
  * injects the LESSON-SPECIFIC REAL PHOTO (downloaded by _fetch_photo.py into
    tools/_photos_<id>/cover.jpg) instead of the generic subject pool / color block;
  * embeds the WEB-VERIFIED SOURCE (fetched by _fetch_source.py) as a citation line.

Usage:  _fine_one.py <lesson_id> [photo_path] [source_text]
If photo missing -> falls back to generic pool (still renders). If source missing -> no cite.
"""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(os.path.dirname(HERE))

from _audit_text import BLOCK, WHITELIST
import _classroom_lib as L
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# reuse proven helpers + page builders from the generic renderer
from _render_lesson import (
    load, clean, split_lines, info_card, scrub_label, homework_segs, _bb_font,
    p_cover, p_objectives, p_keypoints, p_method, p_difficulties, p_blackboard,
    p_homework, p_summary, photo_for,
)

def p_background_fine(s, les, photo, source_cite, photo_caption=None):
    """Background slide with the lesson's REAL photo + verified source citation."""
    L.bg(s)
    L.kicker(s, '课文背景', L.M, L.M, L.XIANG)
    txt = clean(les.get('textbookAnalysis', ''))
    if not txt:
        lt = scrub_label(les.get('lessonTypeName', ''))
        if lt:
            txt = (f"《{clean(les.get('title',''))}》是{les.get('book','')}第{les.get('unitNumber','')}单元"
                   f"「{les.get('unitTitle','')}」的内容，属于{lt}。")
        else:
            txt = (f"《{clean(les.get('title',''))}》是{les.get('book','')}第{les.get('unitNumber','')}单元"
                   f"「{les.get('unitTitle','')}」的重要内容。")
    # body text (left column)
    runs = [{'text': txt, 'size': 16, 'color': L.INK, 'font': L.KAI, 'line': 1.5, 'space_after': 6}]
    if source_cite:
        runs.append({'text': f"资料来源（联网核实）：{source_cite}",
                     'size': 11, 'color': L.MUTED, 'font': L.HEI, 'line': 1.3})
    L.textbox(s, L.M, L.M + Inches(0.95), Inches(7.4), Inches(4.7), runs)
    # real photo on the right (place_photo adds the protective scrim)
    if photo and os.path.exists(photo):
        px = L.M + Inches(8.1); pw = Inches(4.5); ph = Inches(3.4)
        L.place_photo(s, photo, int(px), int(L.M + Inches(0.95)), int(pw), int(ph))
        cap = photo_caption or "本课真实资料图（自由授权）"
        L.caption(s, cap, px, L.M + Inches(0.95) + ph + Inches(0.05), pw)
    else:
        path, name = photo_for(les.get('_subj', 'cn'), 0)
        if os.path.exists(path):
            px = L.M + Inches(8.1); pw = Inches(4.5); ph = Inches(3.4)
            L.place_photo(s, path, int(px), int(L.M + Inches(0.95)), int(pw), int(ph))
            L.caption(s, f"资料图（自由授权，复用 {name}）", px, L.M + Inches(0.95) + ph + Inches(0.05), pw)
    L.page_num(s)

def render(id_, photo=None, source_cite=''):
    les = load(id_)
    if not les:
        print('NOT FOUND', id_); sys.exit(2)
    subj = les.get('_subj', 'cn')
    L.PAGE[0] = 0
    # read CC attribution next to the photo (if present)
    photo_caption = None
    if photo and os.path.exists(photo):
        attrib_path = photo + '.attrib.json'
        if os.path.exists(attrib_path):
            try:
                a = json.load(open(attrib_path, encoding='utf-8'))
                lic = a.get('license', '')
                au = a.get('author', '')
                cap = '真实资料图'
                if lic:
                    cap += ' · ' + lic
                if au:
                    cap += ' · ' + au
                photo_caption = cap
            except Exception:
                pass
    prs, BLANK = L.new_presentation()
    s1 = L.new_slide(prs, BLANK); p_cover(s1, les)
    s2 = L.new_slide(prs, BLANK); p_objectives(s2, les)
    s3 = L.new_slide(prs, BLANK); p_background_fine(s3, les, photo, source_cite, photo_caption)
    s4 = L.new_slide(prs, BLANK); p_keypoints(s4, les)
    s5 = L.new_slide(prs, BLANK); p_method(s5, les, subj, 1)
    s6 = L.new_slide(prs, BLANK); p_difficulties(s6, les)
    s7 = L.new_slide(prs, BLANK); p_blackboard(s7, les)
    s8 = L.new_slide(prs, BLANK); p_homework(s8, les)
    s9 = L.new_slide(prs, BLANK); p_summary(s9, les)
    out_dir = os.path.join('preview_v7', subj)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, id_ + '.pptx')
    prs.save(out)
    print('SAVED', out, 'slides=', len(prs.slides._sldIdLst))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: _fine_one.py <lesson_id> [photo] [source]'); sys.exit(1)
    pid = sys.argv[1]
    ph = sys.argv[2] if len(sys.argv) > 2 else None
    sc = sys.argv[3] if len(sys.argv) > 3 else ''
    render(pid, ph, sc)
