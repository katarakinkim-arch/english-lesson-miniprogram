# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '五大类植物激素（auxin / cytokinin / gibberellin / ethylene / abscisic acid）及其协同拮抗关系（University of Minnesota Open Horticulture Textbook, open.lib.umn.edu）。',
        '顶端优势由顶芽产生的生长素向下运输维持；去顶后侧芽解除抑制（Thimann & Skoog, 1933；PMC4390985）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx1-u5-2', SOURCES)
    print('SAVED', out, 'slides=', 9)
