# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · 伴性遗传（二）类型与应用，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u2-4'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "LibreTexts Biology：Sex-Linked Inheritance —— X 连锁显性与 Y 连锁遗传。",
    "MedlinePlus：Genetic Conditions —— 伴性遗传病的系谱与风险评估。",
]
build(d, sources, OUT=OUT)
