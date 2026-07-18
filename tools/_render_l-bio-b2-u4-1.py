# -*- coding: utf-8 -*-
# l-bio-b2-u4-1 基因指导蛋白质合成（转录与翻译）—— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u4-1.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u4-1.pptx')
sources = [
    "Crick F. The central dogma of molecular biology. Nature 1970;227(5258):561-563.",
    "NCBI Biotechnology | Central Dogma of Biology: Classic View (ncbi.nlm.nih.gov).",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
