# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第2章第3节 糖类和脂质（人教2019版）。
#   21世纪教育网 同步学案：糖类的分类与脂质的功能（zy.21cnjy.com/13144127）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u2-4'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第2章第3节 糖类和脂质（人教2019版）',
    '21世纪教育网 同步学案：糖类的分类（单/二/多糖）与脂质功能（zy.21cnjy.com/13144127）',
]
mnemonic = '糖分单二多、单体葡萄糖；脂有脂肪储能、磷脂成膜、固醇调节；脂肪H多产能高。'
next_link = '下节课：无机物——水和无机盐，认识细胞中不可或缺的无机成分。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
