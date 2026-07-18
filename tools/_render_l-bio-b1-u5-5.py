# -*- coding: utf-8 -*-
# 渲染器（手写）：l-bio-b1-u5-5 —— 学生课堂版 9 页 PPTX
import os, json
from _kit_chunk013 import render
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u5-5.json'), encoding='utf-8'))
sources = [
    'Khan Academy: Intro to photosynthesis（光反应/卡尔文循环）',
    'PMC Photosynthesis 综述：光反应在类囊体膜，暗反应在基质；O2 来自水光解',
    'Visible Body: Light-Dependent & Light-Independent Reactions'
]
out = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u5-5.pptx')
render(data, sources, out)
print('SAVED', out)
