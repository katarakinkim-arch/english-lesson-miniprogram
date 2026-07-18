# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u6-1 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u6-1.json'), encoding='utf-8'))
sources = [
    '每日科技名词《细胞周期》（article.xuexi.cn）：连续分裂细胞 G1/S/G2/M',
    '百度百科《细胞周期》；科普中国《细胞分裂周期》',
    '人教版必修1 第6章《细胞的增殖》学案（21世纪教育网）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u6-1.pptx')
render(data, sources, out)
print('SAVED', out)
