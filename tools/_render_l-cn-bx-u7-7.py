# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-7.py  （必修下 第七单元 第7课时）
# 课题：写作指导与讲评——红楼读书报告
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-7'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：人民教育出版社《必修下册》第七单元「写作」任务：学写读书报告。",
    "来源：周剑斌《浅谈〈红楼梦〉整本书阅读教学》——读书报告常见三类问题。",
]

INTRO = "引、述、析、评——把一整本书，写成一篇有自己的声音的报告。"

build_course(D, SOURCES, OUT, INTRO)
