# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u3-2.py  （必修下 第三单元 第2课时）
# 课题：一名物理学家的教育历程 精读
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u3-2'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：维基百科 / 百度百科 加来道雄（Michio Kaku）——理论物理学家、超弦理论奠基人",
    "来源：人教版课文《一名物理学家的教育历程》",
]

INTRO = "一条鲤鱼，如何引出对高维宇宙的遐想？"

build_course(D, SOURCES, OUT, INTRO)
