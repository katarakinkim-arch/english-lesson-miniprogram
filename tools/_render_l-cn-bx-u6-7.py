# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-7'
SOURCES = [
    '21世纪教育网《统编版高中语文必修上册「学写文学短评」教案》：定题宜小、引—析—评、叙议结合',
    '王从华《建立文学短评写作学习元素的进阶规划》：「引—析—评」结构',
    '21世纪教育网《第三单元 学写文学短评》：以小见大、叙议结合',
]
LEAD = '把一篇感言，改成一份站得住的小说短评。'
SUMMARY = '三典型——无靶、无引文、无分析；改法是缩靶、补文、加析。'
REFLECTIONS = [
    '翻出初稿，圈出最该「缩靶」的一处。',
    '用「缩 / 补 / 展」说清改法三方向。',
    '三个词概括你眼中的好短评。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
