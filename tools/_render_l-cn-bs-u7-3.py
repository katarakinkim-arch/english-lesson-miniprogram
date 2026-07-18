# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u7-3'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "人民教育出版社《语文·必修上册》第七单元导语：人文主题「自然情怀」",
    "周刚《现代作家审美取向的文本解析——以〈故都的秋〉和〈荷塘月色〉为例》",
]
lead = "同写自然，融法各异——两篇散文，两种情景交融的范式。"
summary = "从《故都的秋》到《荷塘月色》，体会中国文人借自然安顿心灵的传统。"
reflections = [
    "哪一篇更打动你？它怎样用自然之景安顿了作者的心境？",
    "两文的「情景交融」有何不同——是以情驭景，还是以景衬情？",
    "用本单元学到的方法，写（或回想）一段属于你自己的景物文字。",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
