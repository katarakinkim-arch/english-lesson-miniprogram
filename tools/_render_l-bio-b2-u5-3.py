# -*- coding: utf-8 -*-
# l-bio-b2-u5-3 人类遗传病 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u5-3.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u5-3.pptx')
sources = [
    "CDC: Genetic Disorders（单基因 / 染色体 / 多因子三类）。",
    "MedlinePlus: Genetic Disorders（遗传病分类与举例）。",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
