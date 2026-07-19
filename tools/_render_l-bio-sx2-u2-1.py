# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '群落是一定区域内各种生物种群的集合（含植物、动物、微生物）；物种经竞争、捕食、寄生、互利共生相互作用（Britannica community-biology）。',
        '森林自上而下分层、池塘挺水/浮水/沉水分层，分层提高了对资源的利用率（教材与生态学综述）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx2-u2-1', SOURCES)
    print('SAVED', out, 'slides=', 9)
