# -*- coding: utf-8 -*-
# l-bio-b2-u4-2 基因表达与性状的关系 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u4-2.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u4-2.pptx')
sources = [
    "Beadle GW, Tatum EL. Genetic control of biochemical reactions in Neurospora. PNAS 1941;27(11):499-506.",
    "Britannica: one gene-one enzyme hypothesis (Beadle & Tatum, 1940s).",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
