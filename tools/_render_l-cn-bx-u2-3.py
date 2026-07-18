# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-3.py  （必修下 第二单元 第3课时）
# 课题：群文阅读——窦娥冤·雷雨 悲剧比较
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-3'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：统编教材单元定位——第二单元人文主题「良知与悲悯」",
    "来源：21cnjy《窦娥冤·雷雨·哈姆莱特联读教学设计》",
]

INTRO = "同是悲剧，窦娥与雷雨的路径有何不同？"

build_course(D, SOURCES, OUT, INTRO)
