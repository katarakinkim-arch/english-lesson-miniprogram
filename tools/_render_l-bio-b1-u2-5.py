# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第2章第2节 无机物——水和无机盐（人教2019版）。
#   21世纪教育网 学案：自由水/结合水与无机盐的生理作用（zy.21cnjy.com/13144125）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u2-5'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第2章第2节 无机物——水和无机盐（人教2019版）',
    '21世纪教育网 学案：自由水/结合水比例与无机盐离子功能（zy.21cnjy.com/13144125）',
]
mnemonic = '自由水流动代谢旺，结合水成构抗逆强；无机盐多离子态，Fe/I/Ca各担当。'
next_link = '下节课：细胞膜的结构和功能——细胞边界如何既分隔又交流。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
