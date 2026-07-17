# -*- coding: utf-8 -*-
"""
批量渲染 高一语文必修上册（bs）全部 64 课 v2 设计稿。
流程：提取JSON → 渲染17页PNG → 每课合成PDF → 合并总册PDF
用法: python tools/_batch_render_bs.py
"""
import os, sys, json, subprocess, glob, time

PYTHON = sys.executable
NODE = r'C:\Users\1\.workbuddy\binaries\node\versions\22.22.2\node.exe'
BASE = os.path.dirname(os.path.abspath(__file__))
MINIPROGRAM = os.path.dirname(BASE)
OUT_ROOT = os.path.join(MINIPROGRAM, 'cn_bs')          # 所有课的PNG输出根
PDF_ROOT  = os.path.join(MINIPROGRAM, 'cn_bs_pdfs')     # 单课PDF输出
COMBINED  = os.path.join(MINIPROGRAM, '高一语文必修上册-全套课件.pdf')

# ---- 从 lessons-cn.js 提取所有 bs（必修上）课 ID ----
def get_bs_lesson_ids():
    """用 node 快速提取所有 l-cn-bs-* 的 id"""
    js_code = """
const data = require('./data/lessons-cn.js');
const ids = data.filter(l => l.id && l.id.startsWith('l-cn-bs-')).map(l => l.id);
console.log(JSON.stringify(ids));
"""
    result = subprocess.run(
        [NODE, '-e', js_code],
        cwd=MINIPROGRAM,
        capture_output=True, text=True, encoding='utf-8'
    )
    ids = json.loads(result.stdout.strip())
    print(f"[INFO] 必修上册共 {len(ids)} 课")
    return ids

# ---- 单课：提取 JSON + 渲染 PNG ----
def render_one(lesson_id):
    out_dir = os.path.join(OUT_ROOT, lesson_id)
    os.makedirs(out_dir, exist_ok=True)
    
    json_path = os.path.join(BASE, f'_temp_{lesson_id}.json')
    
    # Step 1: 提取
    extract = subprocess.run(
        [NODE, os.path.join(BASE, '_extract_lesson.cjs'), lesson_id, 'cn'],
        cwd=MINIPROGRAM, capture_output=True, text=True, encoding='utf-8'
    )
    if extract.returncode != 0:
        print(f"  [WARN] {lesson_id} 提取失败: {extract.stderr[:200]}")
        return False
    
    # 重命名为带id的临时文件（因为_extract固定写lesson_cn.json，我们移过来）
    src_json = os.path.join(MINIPROGRAM, 'lesson_cn.json')
    if os.path.exists(src_json):
        if os.path.exists(json_path):
            os.remove(json_path)
        os.rename(src_json, json_path)
    
    # Step 2: 渲染
    start = time.time()
    rend = subprocess.run(
        [PYTHON, os.path.join(BASE, '_render_cn_v2.py'), json_path, out_dir],
        cwd=MINIPROGRAM, capture_output=True, text=True, encoding='utf-8'
    )
    elapsed = time.time() - start
    
    if rend.returncode != 0:
        print(f"  [FAIL] {lesson_id} 渲染失败 ({elapsed:.1f}s): {rend.stderr[:300]}")
        return False
    
    pngs = sorted(glob.glob(os.path.join(out_dir, 'slide_*.png')))
    print(f"  [OK]   {lesson_id} → {len(pngs)} 页 ({elapsed:.1f}s)")
    
    # 清理临时JSON
    if os.path.exists(json_path):
        os.remove(json_path)
    
    return len(pngs) > 0

# ---- 单课 PNG → PDF ----
def make_pdf(lesson_id, png_dir, pdf_path):
    from PIL import Image
    pngs = sorted(glob.glob(os.path.join(png_dir, 'slide_*.png')))
    if not pngs:
        return False
    imgs = [Image.open(p).convert('RGB') for p in pngs]
    imgs[0].save(pdf_path, 'PDF', resolution=150, save_all=True, append_images=imgs[1:])
    for im in imgs:
        im.close()
    return True

# ---- 合并所有课的 PNG 为总册 ----
# 注意：PIL 在 Windows 上无法直接 Image.open 读取 PDF，故合并时用 PNG 源。
def combine_all_pdfs(output_pdf, png_dirs):
    """直接读各课 PNG 目录，合并成总册 PDF。"""
    from PIL import Image

    all_images = []
    for png_dir in png_dirs:
        pngs = sorted(glob.glob(os.path.join(png_dir, 'slide_*.png')))
        for p in pngs:
            all_images.append(Image.open(p).convert('RGB'))

    if not all_images:
        print("[ERROR] 无任何页面可合并")
        return False

    print(f"[INFO] 合并 {len(all_images)} 页到总册...")
    all_images[0].save(output_pdf, 'PDF', resolution=150,
                       save_all=True, append_images=all_images[1:])
    size_kb = os.path.getsize(output_pdf) // 1024
    print(f"[OK] 总册完成: {output_pdf} ({size_kb} KB, {len(all_images)} 页)")
    return True

# ==================== 主流程 ====================
if __name__ == '__main__':
    ids = get_bs_lesson_ids()
    print(f"\n{'='*60}")
    print(f"批量渲染 高一语文必修上册 {len(ids)} 课")
    print(f"输出目录: {OUT_ROOT}")
    print(f"{'='*60}\n")
    
    os.makedirs(OUT_ROOT, exist_ok=True)
    os.makedirs(PDF_ROOT, exist_ok=True)
    
    success = 0
    fail = 0
    png_dirs = []  # 各课 PNG 目录，供合并总册

    t0 = time.time()
    for i, lid in enumerate(ids):
        print(f"[{i+1}/{len(ids)}] {lid}", end='')

        ok = render_one(lid)
        if ok:
            # 合成该课 PDF
            png_dir = os.path.join(OUT_ROOT, lid)
            pdf_path = os.path.join(PDF_ROOT, f"{lid}.pdf")
            if make_pdf(lid, png_dir, pdf_path):
                png_dirs.append(png_dir)
                success += 1
            else:
                fail += 1
                print("  [WARN] PDF生成失败")
        else:
            fail += 1

        # 每10课打印进度
        if (i+1) % 10 == 0 or i+1 == len(ids):
            elapsed = time.time() - t0
            print(f"\n  --- 进度: {i+1}/{len(ids)} | 成功:{success} 失败:{fail} | 耗时:{elapsed:.0f}s ---\n")

    total_time = time.time() - t0
    print(f"\n{'='*60}")
    print(f"渲染完成: 成功={success}, 失败={fail}, 总耗时={total_time:.0f}s")

    # 合并总册
    if png_dirs:
        combine_all_pdfs(COMBINED, png_dirs)
    
    print(f"{'='*60}")
    print(f"PPT预览(PNG): {OUT_ROOT}")
    print(f"单课PDF:     {PDF_ROOT}")
    print(f"总册PDF:     {COMBINED}")
