# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（生物 必修2 · DNA是主要的遗传物质，色块兜底）。
import os, json
from _kit_chunk014 import build

ID = 'l-bio-b2-u3-1'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
d = json.load(open(DATA, encoding='utf-8'))
sources = [
    "Nature Education Scitable：Griffith & Avery —— DNA 是遗传物质的证据。",
    "genome.gov：Hershey–Chase Experiment —— 噬菌体实验确证 DNA 为遗传物质。",
]
build(d, sources, OUT=OUT)
