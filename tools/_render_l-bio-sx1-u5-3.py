# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '植物通过激素与光受体（如光敏色素 phytochrome）协同感知并响应光、重力等环境信号（Britannica; OERTX Plant Sensory Systems）。',
        '根向地与茎背地同源（近地侧生长素多），结果相反只因根对生长素比茎敏感得多（权威综述与教材一致）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx1-u5-3', SOURCES)
    print('SAVED', out, 'slides=', 9)
