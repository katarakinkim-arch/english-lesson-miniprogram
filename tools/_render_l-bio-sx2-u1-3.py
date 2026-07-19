# -*- coding: utf-8 -*-
# 本批次（chunk017）生物课渲染器：仅 import _kit_chunk017，调用统一 9 页结构。
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk017 import render

SOURCES = [
        '密度制约因素（竞争、传染病）作用随密度增大而增强；非密度制约因素（寒潮、干旱）与密度无关（Albert.io；eagri Lecture 9）。',
        '种群数量围绕 K 上下波动，是负反馈调节的结果（Britannica / 生态学教材）。',
    ]

if __name__ == '__main__':
    out = render('l-bio-sx2-u1-3', SOURCES)
    print('SAVED', out, 'slides=', 9)
