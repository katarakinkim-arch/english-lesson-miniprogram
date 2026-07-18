# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u8-2.py  （必修下 第八单元 第2课时）
# 课题：答司马谏议书 精读——驳论艺术与变法立场
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u8-2'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

SOURCES = [
    "来源：可可诗词网《王安石〈答司马谏议书〉》——驳「侵官生事征利拒谏」四罪。",
    "来源：人民教育出版社《必修下册》第八单元——古代说理文思辨性阅读。",
]

INTRO = "名实之辨、以守为攻——三百余字回信里的变法立场与驳论锋芒。"

build_course(D, SOURCES, OUT, INTRO)
