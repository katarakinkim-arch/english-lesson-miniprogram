# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · 孟德尔两对相对性状杂交与自由组合定律，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u1-3'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "Nature Education Scitable：Dihybrid Cross —— 两对相对性状的双因子杂交与 9:3:3:1。",
    "genome.gov（美国国家人类基因组研究所）：Mendel's Peas —— 孟德尔豌豆杂交实验。",
]
build(d, sources, OUT=OUT)
