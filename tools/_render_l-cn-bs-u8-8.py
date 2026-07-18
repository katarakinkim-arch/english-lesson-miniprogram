# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-8'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '统编教材高中语文必修上第八单元学习任务设计（搜狐教育，2021）',
    '21世纪教育网《第八单元·丰富词语积累》教学设计'
]
lead = '把读到的、写到的，汇成一本自己的词语本。'
summary = '分类、联想、语境三法并用，把零散词语汇成一本属于自己的词语本。'
reflections = [
    '你打算按什么线索来整理自己的词语本？',
    '分享一个你最近记下的好词，说说为什么收它。',
    '哪种积累法（分类／联想／语境）你最想试？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
