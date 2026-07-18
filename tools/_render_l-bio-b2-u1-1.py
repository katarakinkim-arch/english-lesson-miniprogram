# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b2-u1-1 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u1-1.json'), encoding='utf-8'))
sources = [
    '每日科技名词《孟德尔遗传定律》（article.xuexi.cn）',
    '华南师范大学《第二章 孟德尔定律》：豌豆闭花授粉，F2 性状分离 3:1',
    '假说—演绎法：观察→假说→演绎推理→测交验证（shengwu.7139.com）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u1-1.pptx')
render(data, sources, out)
print('SAVED', out)
