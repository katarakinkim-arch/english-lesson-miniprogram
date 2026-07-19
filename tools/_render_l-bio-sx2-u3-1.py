# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '生态系统 = 生物群落 + 无机环境；组成含非生物物质能量、生产者、消费者、分解者（Britannica ecosystem / Trophic-levels）。',
        '营养级自生产者起算；食物链仅含生产者与消费者，分解者在链外（Britannica food-web）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx2-u3-1', SOURCES)
    print('SAVED', out, 'slides=', 9)
