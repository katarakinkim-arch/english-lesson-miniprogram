# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · 基因在染色体上，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u2-2'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "中国科普博览 kepu.net.cn：摩尔根果蝇实验 —— 白眼基因位于 X 染色体。",
    "Nature Education Scitable：Genes Are on Chromosomes —— 萨顿—摩尔根学说。",
]
build(d, sources, OUT=OUT)
