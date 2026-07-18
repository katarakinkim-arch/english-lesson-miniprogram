# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u5-2 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u5-2.json'), encoding='utf-8'))
sources = [
    '人教版必修1 第5章第2节《酶的特性》学案（21世纪教育网）',
    '教材：酶具高效性、专一性、作用条件温和；高温变性不可逆、低温抑制可逆',
    '锁钥学说与诱导契合模型（结构生物学通识）'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u5-2.pptx')
render(data, sources, out)
print('SAVED', out)
