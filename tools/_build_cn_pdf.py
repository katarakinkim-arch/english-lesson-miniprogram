# -*- coding: utf-8 -*-
"""把 cn_preview/ 的 17 张设计稿 PNG 合成为 l-cn-bs-u1-1.pdf（先看用）。"""
import os
from PIL import Image

OUT = 'cn_preview'
PDF_OUT = 'l-cn-bs-u1-1.pdf'
slides = sorted([f for f in os.listdir(OUT) if f.endswith('.png')])
images = [Image.open(os.path.join(OUT, s)).convert('RGB') for s in slides]
if images:
    images[0].save(PDF_OUT, 'PDF', save_all=True, append_images=images[1:])
print(f'PDF -> {PDF_OUT} ({os.path.getsize(PDF_OUT)//1024} KB, {len(images)} 页)')
