# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-1'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "中国大百科全书 / 百度百科「语义场」词条（J. Trier 语义场理论）",
    "人民教育出版社《语文·必修上册》第八单元导语",
]
lead = "词不是孤岛——把它们连成家族，积累才成网而非成堆。"
summary = "词语以「家族」（语义场）方式存在，网络化积累胜过抄词表。"
reflections = [
    "你平时积累词语，是抄词表还是织成网络？",
    "举一组近义词，说说它们微妙的差别在哪里？",
    "今天起，你想建立自己的哪一个「词语家族」？",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
