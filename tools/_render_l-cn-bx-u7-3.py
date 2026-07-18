# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-3.py  （必修下 第七单元 第3课时）
# 课题：专题研讨——宝黛钗人物形象比较
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-3'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：周思源《周思源看红楼》——宝玉厌仕途经济、黛玉「木石前盟」、宝钗理性现实。",
    "来源：维基百科《红楼梦》——宝黛钗爱情婚姻悲剧主线与「金玉良缘」。",
]

INTRO = "宝玉、黛玉、宝钗，三种生命姿态，一场「木石」与「金玉」的对照。"

build_course(D, SOURCES, OUT, INTRO)
