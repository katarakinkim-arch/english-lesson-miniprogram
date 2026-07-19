# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '指数增长 J 型：dN/dt=rmax·N；逻辑斯蒂 S 型：dN/dt=rmax·N·(K−N)/K，增速在 K/2 处最大（Albert.io；learnhowtoscience）。',
        '环境容纳量 K 随环境变动而非固定上限；渔业捕捞保持在 K/2 附近产量最高（生态学教材）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx2-u1-2', SOURCES)
    print('SAVED', out, 'slides=', 9)
