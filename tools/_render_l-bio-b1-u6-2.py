# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u6-2 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u6-2.json'), encoding='utf-8'))
sources = [
    '21世纪教育网 必修1 第6章学案：有丝分裂各期特征与记忆口诀',
    '中公《有丝分裂》教学案例：前期中期后期末期变化',
    '动植物有丝分裂区别（前期纺锤体、末期细胞板/缢裂）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u6-2.pptx')
render(data, sources, out)
print('SAVED', out)
