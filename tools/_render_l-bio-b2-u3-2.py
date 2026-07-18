# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · DNA分子的结构，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u3-2'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "genome.gov：DNA Double Helix —— 1953 年沃森与克里克提出双螺旋结构。",
    "Nature Education Scitable：DNA Structure —— 碱基互补配对原则。",
]
build(d, sources, OUT=OUT)
