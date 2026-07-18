# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u5-6'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '人民日报《理解乡土，才能读懂中国》（留存·松动·转化）',
    '北京日报《从“乡土”中寻找“根”的力量》（创造性转化）'
]
lead = '乡土未死，它正在转化中重生。'
summary = '乡土在留存、松动与转化中重生，传统可被创造性地接进现代生活。'
reflections = [
    '你眼里“乡土”正在消失，还是换了一种样子？',
    '举一个传统被现代转化的例子。',
    '你愿意从乡土里继承哪一点“根”的力量？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
