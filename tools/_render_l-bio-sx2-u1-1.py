# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '种群是同一区域同种生物的全部个体；种群变化 ΔN=(B+I)−(D+E)（Albert.io AP Biology Population Ecology）。',
        '种群密度是最基本的数量特征；年龄结构可预测趋势，而非直接决定密度（Britannica / 高中生物教材）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx2-u1-1', SOURCES)
    print('SAVED', out, 'slides=', 9)
