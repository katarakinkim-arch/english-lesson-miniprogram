# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-2'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "王力《汉语史稿》：词义演变（本义 / 引申义 / 比喻义）",
    "中国社会科学院语言研究所《现代汉语词典》",
]
lead = "一个词有三副面孔：本义、引申义、比喻义，莫望文生义。"
summary = "溯源本义、理清引申、辨明比喻，是准确解词的三步法。"
reflections = [
    "遇到熟词，你会先查本义，还是直接按今义理解？",
    "「不刊之论」为什么不能望文生义？你还能举出别的吗？",
    "写作选词前，先想清楚它的本义和比喻义，会有什么不同？",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
