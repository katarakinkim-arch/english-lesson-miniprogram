# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-7.py  （必修下 第二单元 第7课时）
# 课题：写作实践与讲评——剧本/评论修改与提升
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-7'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：「互评自改式」作文教学——同伴互评与自我修正",
    "来源：湖北日报《换种方式改作文》——过程性评价与学生主体",
]

INTRO = "好戏剧文，好在哪里、怎样改得更好？"

build_course(D, SOURCES, OUT, INTRO)
