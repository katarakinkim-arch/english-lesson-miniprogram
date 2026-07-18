# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u6-4 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u6-4.json'), encoding='utf-8'))
sources = [
    '安庆师范大学《减数分裂和受精作用》（smkx.aqnu.edu.cn）',
    '21世纪教育网 必修2 教案：同源染色体/联会/四分体/交叉互换',
    '魏斯曼预测 + 精子卵细胞形成差异（均等/不均等分裂）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u6-4.pptx')
render(data, sources, out)
print('SAVED', out)
