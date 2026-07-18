# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u3-1.py  （必修下 第三单元 第1课时）
# 课题：青蒿素：人类征服疾病的一小步 精读
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u3-1'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：科学技术部 / 新华网——屠呦呦与青蒿素（2015 诺贝尔生理学或医学奖）",
    "来源：屠呦呦诺奖演讲《青蒿素——中医药给世界的一份礼物》",
]

INTRO = "一株青蒿，怎样成为救人的良药？"

build_course(D, SOURCES, OUT, INTRO)
