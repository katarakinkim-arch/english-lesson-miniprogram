# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（手写精排，色块兜底）。
import os
from _fine_cn_kit import build, load_data, SOURCES, new_presentation

ID = 'l-cn-bs-u1-6'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = load_data(ID)
sources = SOURCES[ID]
prs, BLANK = new_presentation()
build(prs, BLANK, data, sources)
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
