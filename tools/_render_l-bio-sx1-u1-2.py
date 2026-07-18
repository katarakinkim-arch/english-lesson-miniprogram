# -*- coding: utf-8 -*-
# l-bio-sx1-u1-2 内环境的稳态 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx1-u1-2.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx1-u1-2.pptx')
sources = [
    "yixue.com: 内环境稳态（Walter Cannon 1926 提出 homeostasis）。",
    "Billman GE. Homeostasis. Front Physiol 2020（Bernard→Cannon 负反馈调节）。",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
