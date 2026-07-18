# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第4章 第3节 物质跨膜运输的方式（人教2019版）。
#   学科网 学案：大分子运输与生物膜流动镶嵌模型（zxxk.com/soft/6733984）。
#   21世纪教育网 学案：生物膜的流动镶嵌模型（zy.21cnjy.com/19251976）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u4-3'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第4章 第3节 物质跨膜运输的方式（人教2019版）',
    '学科网 学案：大分子运输与生物膜流动镶嵌模型（zxxk.com/soft/6733984）',
    '21世纪教育网 学案：生物膜的流动镶嵌模型（zy.21cnjy.com/19251976）',
]
mnemonic = '胞吞内陷成囊、胞吐囊泡融合；不穿磷脂层、靠流动、耗能；小结：小离子跨膜、大分膜泡。'
next_link = '本单元结束：回顾物质的输入和输出，建立完整知识网络。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
