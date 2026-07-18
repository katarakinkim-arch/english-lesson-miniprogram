# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-1.py  （必修下 第二单元 第1课时）
# 课题：窦娥冤（节选）精读——悲剧冲突与「血溅白练」之誓
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-1'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：维基百科《窦娥冤》——关汉卿与元杂剧（全名《感天动地窦娥冤》）",
    "来源：人民教育出版社《普通高中教科书·语文必修下册》",
]

INTRO = "一个弱女子的奇冤，如何感天动地？"

build_course(D, SOURCES, OUT, INTRO)
