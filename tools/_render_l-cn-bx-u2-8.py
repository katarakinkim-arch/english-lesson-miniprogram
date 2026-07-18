# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-8.py  （必修下 第二单元 第8课时）
# 课题：单元活动——课本剧展演与戏剧论坛
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-8'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：统编教材第二单元教学设计「演绎悲悯 感悟良知」",
    "来源：21cnjy 第二单元教学设计（课本剧展演与戏剧论坛）",
]

INTRO = "用展演与论坛，为单元收官。"

build_course(D, SOURCES, OUT, INTRO)
