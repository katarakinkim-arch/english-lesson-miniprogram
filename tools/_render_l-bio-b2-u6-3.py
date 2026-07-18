# -*- coding: utf-8 -*-
# l-bio-b2-u6-3 共同进化与生物多样性 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u6-3.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u6-3.pptx')
sources = [
    "Ehrlich PR, Raven PH (1964) 提出协同进化（植物与植食昆虫的相互选择）。",
    "Frontiers in Ecology and Evolution (2021): Coevolution review.",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
