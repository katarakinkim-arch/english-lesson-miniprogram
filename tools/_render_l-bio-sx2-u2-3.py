# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '群落演替是优势种随时间被另一群落替代的过程；初生演替始于裸岩，次生演替始于保留土壤之地、速度更快（Britannica kids ecology）。',
        '人类活动可加速、延缓或改变演替方向（如退耕还林促进正向演替）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx2-u2-3', SOURCES)
    print('SAVED', out, 'slides=', 9)
