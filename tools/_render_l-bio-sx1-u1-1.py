# -*- coding: utf-8 -*-
# l-bio-sx1-u1-1 细胞生活的环境 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx1-u1-1.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx1-u1-1.pptx')
sources = [
    "北京协和医院: 人体“内环境”的奥秘（Claude Bernard 内环境学说）。",
    "NCBI Bookshelf: Physiology, Body Fluids（细胞外液约占体重 1/3）。",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
