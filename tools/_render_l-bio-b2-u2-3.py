# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · 伴性遗传（一）概念与红绿色盲，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u2-3'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "百度百科：红绿色盲 —— X 连锁隐性遗传的典型实例。",
    "美国国家眼科研究所 NEI：Color Blindness —— 色觉缺陷的遗传基础。",
]
build(d, sources, OUT=OUT)
