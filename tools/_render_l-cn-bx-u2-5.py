# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-5.py  （必修下 第二单元 第5课时）
# 课题：戏剧知识——冲突、潜台词与戏剧性
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-5'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：戏剧理论（刘安海、孙文宪《文学理论》）——戏剧冲突与潜台词",
    "来源：21cnjy《戏剧知识梳理》学案——戏剧语言与戏剧性",
]

INTRO = "读戏剧，抓什么才看得见匠心？"

build_course(D, SOURCES, OUT, INTRO)
