# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-6.py  （必修下 第二单元 第6课时）
# 课题：写作指导——学写剧本片段与戏剧评论
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-6'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：剧本写作指导（余卫兵）——剧本要素与舞台说明",
    "来源：课本剧写作资料——台词、独白与舞台提示",
]

INTRO = "把读过的剧，写成可演的剧本或评论。"

build_course(D, SOURCES, OUT, INTRO)
