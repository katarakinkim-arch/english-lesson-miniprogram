# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u5-3 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u5-3.json'), encoding='utf-8'))
sources = [
    'Britannica: Adenosine triphosphate (ATP) — 细胞能量通货（britannica.com）',
    'ATP 结构简式 A-P~P~P，末端高能磷酸键水解释放约 30.5 kJ/mol（科普中国）',
    'Lipmann (1941) 提出“高能磷酸键”，ATP 为能量代谢中心分子'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u5-3.pptx')
render(data, sources, out)
print('SAVED', out)
