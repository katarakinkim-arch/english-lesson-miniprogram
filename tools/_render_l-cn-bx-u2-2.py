# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-2.py  （必修下 第二单元 第2课时）
# 课题：雷雨（节选）精读——周鲁冲突与人性的暗涌
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-2'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：维基百科 /《中国大百科全书》《雷雨》——曹禺 1934 年发表于《文学季刊》",
    "来源：人民教育出版社《普通高中教科书·语文必修下册》",
]

INTRO = "一天之内，旧事为何集中爆发？"

build_course(D, SOURCES, OUT, INTRO)
