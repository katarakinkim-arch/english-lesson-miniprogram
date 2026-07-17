# -*- coding: utf-8 -*-
"""批量渲染驱动：把 _lessons_all.json 里每课渲染成课堂学生版 PPTX。
用法:
  python _build_classroom_all.py 语文            # 渲染单科
  python _build_classroom_all.py all             # 渲染全部 9 科
  python _build_classroom_all.py 语文 --preview 8 # 额外生成前8课的 PDF 预览
输出: preview_v7/<subject>/<id>.pptx
"""
import os, sys, json, argparse, glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _classroom_ppt import render_lesson

BASE = os.path.dirname(HERE)
JSON_PATH = os.path.join(BASE, 'preview_v7', '_lessons_all.json')

def load():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def render_subject(subj, lessons, do_preview=0):
    out_dir = os.path.join(BASE, 'preview_v7', subj)
    os.makedirs(out_dir, exist_ok=True)
    n = 0
    for les in lessons:
        lid = les.get('id') or ('lesson_%d' % n)
        pptx = os.path.join(out_dir, lid + '.pptx')
        try:
            render_lesson(les, pptx, photos=None, research=None)
            n += 1
        except Exception as e:
            print('  ERR', lid, repr(e)[:120])
    print('  %s: %d PPTX -> %s' % (subj, n, out_dir))
    # 预览（可选）：取前 do_preview 课生成 PNG+PDF
    if do_preview > 0:
        gen_previews(subj, out_dir, lessons, do_preview)
    return n

def gen_previews(subj, out_dir, lessons, count):
    """生成前 count 课的 PNG 预览 + 合并 PDF（用现有 _pptx_to_png.py）。"""
    import subprocess
    png_tool = os.path.join(HERE, '_pptx_to_png.py')
    if not os.path.exists(png_tool):
        print('  (skip preview: no _pptx_to_png.py)')
        return
    sel = lessons[:count]
    pdfs = []
    for les in sel:
        lid = les.get('id')
        pptx = os.path.join(out_dir, lid + '.pptx')
        png_dir = os.path.join(out_dir, '_preview_' + lid)
        try:
            subprocess.run([sys.executable, png_tool, pptx, png_dir],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
            pngs = sorted(glob.glob(os.path.join(png_dir, '*.png')))
            if pngs:
                from PIL import Image
                imgs = [Image.open(p).convert('RGB') for p in pngs]
                pdf = os.path.join(out_dir, lid + '_preview.pdf')
                imgs[0].save(pdf, 'PDF', save_all=True, append_images=imgs[1:])
                pdfs.append(pdf)
        except Exception as e:
            print('  preview ERR', lid, repr(e)[:80])
    if pdfs:
        print('  previews: %d PDF' % len(pdfs))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('subject', help='科目名 或 all')
    ap.add_argument('--preview', type=int, default=0, help='生成前N课PDF预览')
    args = ap.parse_args()
    data = load()
    if args.subject == 'all':
        total = 0
        for subj, lessons in data.items():
            print('==', subj)
            total += render_subject(subj, lessons, do_preview=args.preview)
        print('TOTAL', total)
    else:
        lessons = data.get(args.subject)
        if not lessons:
            print('NO SUBJECT', args.subject, '| available:', list(data.keys()))
            return
        render_subject(args.subject, lessons, do_preview=args.preview)

if __name__ == '__main__':
    main()
