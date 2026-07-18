# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第3章第1节 细胞膜的结构和功能（人教2019版）。
#   21世纪教育网 学案：流动镶嵌模型与选择透过性（zy.21cnjy.com/14063633）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u3-1'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第3章第1节 细胞膜的结构和功能（人教2019版）',
    '21世纪教育网 学案：流动镶嵌模型、磷脂排布与选择透过性（zy.21cnjy.com/14063633）',
]
mnemonic = '磷脂双分子层作支架，蛋白镶/嵌/贯穿；糖被在外侧；结构流动、功能选择透过。'
next_link = '下节课：细胞器之间的分工——细胞内的"车间"各司其职。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
