# -*- coding: utf-8 -*-
# l-bio-b2-u5-2 基因重组与染色体变异 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u5-2.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u5-2.pptx')
sources = [
    "MedlinePlus: Cri du chat syndrome（5 号染色体短臂缺失）。",
    "NCBI OMIM #123450：猫叫综合征（Lejeune 1963 首次描述）。",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
