# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u6-3 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u6-3.json'), encoding='utf-8'))
sources = [
    '成都师范学院 中学生物探究性实验指导手册【实验11】（cdnu.edu.cn）',
    '21世纪教育网 实验复习：解离→漂洗→染色→制片 流程',
    '分生区细胞特点：正方形、排列紧密（教材）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u6-3.pptx')
render(data, sources, out)
print('SAVED', out)
