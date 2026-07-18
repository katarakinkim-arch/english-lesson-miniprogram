# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u5-4 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u5-4.json'), encoding='utf-8'))
sources = [
    'Monash University: The process of aerobic respiration（三阶段场所与产物）',
    'LibreTexts: Cellular Respiration（糖酵解/柠檬酸循环/电子传递链）',
    '总反应式 C6H12O6+6O2→6CO2+6H2O+能量（教材）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u5-4.pptx')
render(data, sources, out)
print('SAVED', out)
