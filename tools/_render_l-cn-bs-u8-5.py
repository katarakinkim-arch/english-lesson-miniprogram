# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-5'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '人民日报海外版《成语可以这样学》（2016-08-27）',
    '人民教育出版社·统编版必修上第八单元课件（21世纪教育网）'
]
lead = '成语是汉语浓缩的文化结晶，读得懂来源，才用得对。'
summary = '成语大多有出处，读懂来源、看清结构，才能在语境里用得准、用得活。'
reflections = [
    '你平时用成语，是先想来源还是先套意思？',
    '找一个你常误用的成语，说说它真正的来源和意思。',
    '试着用一个成语，写一句贴合语境的话。'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
