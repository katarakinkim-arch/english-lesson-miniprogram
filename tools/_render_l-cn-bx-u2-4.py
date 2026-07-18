# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u2-4.py  （必修下 第二单元 第4课时）
# 课题：哈姆莱特（节选）精读——人文主义与「延宕」之谜
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u2-4'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：维基百科 / 百度百科《To be or not to be》——朱生豪译「生存还是毁灭」",
    "来源：人民教育出版社《普通高中教科书·语文必修下册》",
]

INTRO = "生存还是毁灭，哈姆莱特为何迟疑？"

build_course(D, SOURCES, OUT, INTRO)
