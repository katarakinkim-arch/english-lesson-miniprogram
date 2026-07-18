# -*- coding: utf-8 -*-
# l-bio-b2-u6-1 现代生物进化理论的主要内容 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u6-1.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u6-1.pptx')
sources = [
    "OpenStax Biology: Population Evolution（现代综合进化论 / 现代达尔文主义）。",
    "Britannica: Hardy-Weinberg law（遗传平衡定律）。",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
