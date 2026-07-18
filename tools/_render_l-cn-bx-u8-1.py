# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u8-1.py  （必修下 第八单元 第1课时）
# 课题：谏太宗十思疏 精读——居安思危与谏诤艺术
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u8-1'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：瑞文网《魏徵〈谏太宗十思疏〉原文·注释·译文·鉴赏》。",
    "来源：人民教育出版社《必修下册》第八单元「思辨性阅读与表达（古代说理文）」。",
]

INTRO = "固本浚源、居安思危——一篇奏疏里的治国忧思与谏诤智慧。"

build_course(D, SOURCES, OUT, INTRO)
