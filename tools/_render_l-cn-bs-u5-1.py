# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u5-1'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '光明日报《包路芳：费孝通与〈乡土中国〉》（2020-11-01）',
    '人民日报《理解乡土，才能读懂中国》（2025-10-31）'
]
lead = '从一块土地、一个村庄，读懂中国的基层。'
summary = '《乡土中国》用14篇田野调查，剖开中国基层社会的根与理。'
reflections = [
    '你印象里的“乡土”是什么？读前和读完会有什么不同？',
    '为什么读懂乡土，才能读懂中国？',
    '你最想从这本书里弄清哪个概念？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
