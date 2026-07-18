# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-4.py  （必修下 第七单元 第4课时）
# 课题：专题研讨——贾府环境与文化空间
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-4'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：澎湃新闻《丹青探红楼：大观园里的建筑美学与人物性格命运》（吴文化博物馆）。",
    "来源：新浪《〈红楼梦〉的空间规划智慧》——潇湘馆竹、蘅芜苑香草与人物契合。",
]

INTRO = "贾府是礼法的坐标，大观园是青春的囚笼；一砖一瓦，皆映人心。"

build_course(D, SOURCES, OUT, INTRO)
