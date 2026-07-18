# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u5-1 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u5-1.json'), encoding='utf-8'))
sources = [
    '人教版高中生物必修1 第5章第1节《酶的作用和本质》学案（21世纪教育网）',
    '教材实验“比较过氧化氢在不同条件下的分解”（探究·实践）：酶降低活化能、催化高效',
    '内蒙古教育装备中心《比较过氧化氢…》创新实验案例（2023，jyt.nmg.gov.cn）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u5-1.pptx')
render(data, sources, out)
print('SAVED', out)
