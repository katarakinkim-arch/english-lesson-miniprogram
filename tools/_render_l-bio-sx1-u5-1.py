# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        'Darwin 与 Darwin（1880）用胚芽鞘实验证明：感光在尖端、弯曲在下部，并推测尖端产生可下传的“影响”（Phototropism: Bending towards Enlightenment, PMC1456868）。',
        'Boysen-Jensen（1913）以明胶片证明该信号可透过并下传；Went（1928）将其命名为 auxin，并提出 Cholodny–Went 模型（单侧光使生长素向背光侧侧向运输）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx1-u5-1', SOURCES)
    print('SAVED', out, 'slides=', 9)
