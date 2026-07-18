# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-2.py  （必修下 第七单元 第2课时）
# 课题：阅读方法指导——抓脉络·理人物·品结构
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-2'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：周剑斌《浅谈〈红楼梦〉整本书阅读教学》（期刊网）——三种阅读法与最佳读本。",
    "来源：人民教育出版社《必修下册》第七单元「学习任务」：把握人物关系、体会性格、欣赏诗词。",
]

INTRO = "以回目为纲，以人物卡为器，在百万字里理出自己的阅读地图。"

build_course(D, SOURCES, OUT, INTRO)
