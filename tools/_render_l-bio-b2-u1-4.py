# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · 自由组合定律的实质与应用，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u1-4'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "Nature Education Scitable：Independent Assortment —— 非同源染色体自由组合。",
    "Britannica：Gregor Mendel —— 孟德尔与遗传定律。",
]
build(d, sources, OUT=OUT)
