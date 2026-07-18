# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-6.py  （必修下 第七单元 第6课时）
# 课题：专题研讨——《红楼梦》的悲剧意蕴与女性观
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-6'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：叶朗《从美学眼光看〈红楼梦〉》——「有情之天下」被吞噬的悲剧。",
    "来源：柯岚《命若朝霜：〈红楼梦〉里的法律、社会与女性》——女性群体悲剧。",
]

INTRO = "家族盛衰、女儿群毁、时代无常——「千红一哭，万艳同悲」的悲剧交响。"

build_course(D, SOURCES, OUT, INTRO)
