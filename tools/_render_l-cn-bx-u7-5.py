# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-5.py  （必修下 第七单元 第5课时）
# 课题：专题研讨——《红楼梦》的语言与诗词
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-5'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：澎湃新闻《青春王国的生命之音——〈红楼梦〉诗词赏析》（何郁、苗怀明）。",
    "来源：光明日报《从诗魁更迭看曹雪芹的诗学趋向》——「诗言志」与「诗缘情」复调。",
]

INTRO = "个性化语言写人，诗词文赋写心；曹雪芹「因人赋笔，文为心声」。"

build_course(D, SOURCES, OUT, INTRO)
