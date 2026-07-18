# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · 减数分裂和受精作用，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u2-1'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "Britannica：Sexual Reproduction —— 减数分裂使配子染色体数目减半。",
    "武汉大学《普通生物学》：减数分裂与受精作用维持染色体数目恒定。",
]
build(d, sources, OUT=OUT)
