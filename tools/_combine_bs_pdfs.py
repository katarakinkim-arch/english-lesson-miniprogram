# -*- coding: utf-8 -*-
"""
独立合并器：把已渲染的 64 课 PNG 直接合成总册 PDF。
PNG 路径已存在于 cn_bs/<id>/slide_*.png，按 lessons-cn.js 顺序排列。
（PIL 在 Windows 上无法直接 Image.open 读取 PDF，故合并时用 PNG 源，不回读 PDF。）
用法: python tools/_combine_bs_pdfs.py
"""
import os, sys, json, subprocess, glob

PYTHON = sys.executable
NODE = r'C:\Users\1\.workbuddy\binaries\node\versions\22.22.2\node.exe'
BASE = os.path.dirname(os.path.abspath(__file__))
MINIPROGRAM = os.path.dirname(BASE)
OUT_ROOT = os.path.join(MINIPROGRAM, 'cn_bs')
COMBINED = os.path.join(MINIPROGRAM, '高一语文必修上册-全套课件.pdf')

def get_bs_lesson_ids():
    js_code = """
const data = require('./data/lessons-cn.js');
const ids = data.filter(l => l.id && l.id.startsWith('l-cn-bs-')).map(l => l.id);
console.log(JSON.stringify(ids));
"""
    result = subprocess.run([NODE, '-e', js_code], cwd=MINIPROGRAM,
                            capture_output=True, text=True, encoding='utf-8')
    return json.loads(result.stdout.strip())

def main():
    ids = get_bs_lesson_ids()
    print(f"[INFO] 必修上册共 {len(ids)} 课，开始合并总册...")

    from PIL import Image
    all_images = []
    missing = []
    for lid in ids:
        png_dir = os.path.join(OUT_ROOT, lid)
        pngs = sorted(glob.glob(os.path.join(png_dir, 'slide_*.png')))
        if not pngs:
            missing.append(lid)
            continue
        for p in pngs:
            all_images.append(Image.open(p).convert('RGB'))

    if missing:
        print(f"[WARN] 以下课缺 PNG，已跳过: {missing}")

    if not all_images:
        print("[ERROR] 无任何页面可合并")
        return

    print(f"[INFO] 合并 {len(all_images)} 页到总册...")
    all_images[0].save(COMBINED, 'PDF', resolution=150,
                       save_all=True, append_images=all_images[1:])
    size_kb = os.path.getsize(COMBINED) // 1024
    print(f"[OK] 总册完成: {COMBINED} ({size_kb} KB, {len(all_images)} 页)")

if __name__ == '__main__':
    main()
