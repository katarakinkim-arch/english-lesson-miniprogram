"""把 4 张新图重命名+转 JPEG，并扫描是否有可见水印。"""
import os, re
from PIL import Image

SRC = r'C:\Users\1\WorkBuddy\2026-07-08-15-47-48\miniprogram\subpackages\eng\images\lessons\l-eng-b1-u2-ls'
NAMES = ['passport', 'boardingpass', 'suitcase', 'map']

files = [f for f in os.listdir(SRC) if f.endswith('.png')]
files.sort()  # 按字母序：Ch(护照) → an(机票) → ro(行李) → fo(地图)
print('文件顺序:', files)

assert len(files) == 4, f'期望 4 张，实际 {len(files)}'

results = []
for f, short in zip(files, NAMES):
    src = os.path.join(SRC, f)
    dst = os.path.join(SRC, short + '.jpg')
    im = Image.open(src).convert('RGB')
    im.thumbnail((800, 800))
    im.save(dst, 'JPEG', quality=82, optimize=True)
    size_kb = round(os.path.getsize(dst) / 1024, 1)
    print(f'  {short}.jpg  {im.size}  {size_kb} KB')
    results.append((short, dst))
    os.remove(src)

# 简单水印自检：扫描图像右下角 200x60 区域，是否有大量灰白色像素聚集（典型水印特征）
print('\n水印自检（扫描右下角 200x60 区域）:')
for short, path in results:
    im = Image.open(path).convert('RGB')
    w, h = im.size
    crop = im.crop((w-220, h-90, w-20, h-30))
    px = list(crop.getdata())
    # 计算白色像素占比
    white_ratio = sum(1 for r,g,b in px if r>220 and g>220 and b>220) / len(px)
    # 计算像素平均亮度
    avg = sum(r+g+b for r,g,b in px) / (3*len(px))
    flag = '疑似水印' if white_ratio > 0.5 else '无明显水印'
    print(f'  {short}: 白像素占比={white_ratio:.1%}, 平均亮度={avg:.0f}, {flag}')

# 总大小
total = sum(os.path.getsize(p) for _,p in results) + os.path.getsize(os.path.join(SRC,'listening.wav'))
print(f'\n总大小: {round(total/1024,1)} KB')
