# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-8.py  （必修下 第七单元 第8课时）
# 课题：单元活动——《红楼梦》研读分享会
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-8'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：人民教育出版社《必修下册》第七单元「单元活动」：研读分享与互评。",
    "来源：统编教材「整本书阅读与研讨」任务群——建构读书方法、提升鉴赏能力。",
]

INTRO = "从导入到方法，从研讨到写作——用一场分享，把红楼读成自己的。"

build_course(D, SOURCES, OUT, INTRO)
