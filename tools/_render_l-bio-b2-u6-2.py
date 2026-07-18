# -*- coding: utf-8 -*-
# l-bio-b2-u6-2 隔离与物种形成 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u6-2.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u6-2.pptx')
sources = [
    "Biology Insights: Postzygotic barriers & the sterile mule（马 64 · 驴 62 → 骡 63 不育）。",
    "PMC: Genomic incompatibilities in the hybrid mule (Equus, 2022).",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
