# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '荒漠、草原、森林、湿地等群落类型由水热组合决定；荒漠极旱、森林湿润且分层最丰富（Britannica ecology）。',
        '湿地为水陆交错带，生物多样性高，具净化水质与蓄洪功能（“地球之肾”）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx2-u2-2', SOURCES)
    print('SAVED', out, 'slides=', 9)
