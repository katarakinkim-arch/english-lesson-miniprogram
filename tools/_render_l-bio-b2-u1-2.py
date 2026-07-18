# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · 分离定律的实质与应用，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u1-2'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "Nature Education Scitable：Test Crosses —— 测交用于确定显性个体的基因型。",
    "LibreTexts Biology：Mendel's Law of Segregation —— 分离定律。",
]
build(d, sources, OUT=OUT)
