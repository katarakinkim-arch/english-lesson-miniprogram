# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第4章第1节 被动运输 第1课时 细胞吸水和失水（人教2019版）。
#   21世纪教育网 导学案：渗透作用与质壁分离复原（zy.21cnjy.com/19251971）。
#   教习网 学案：水进出细胞的原理（m.51jiaoxi.com/doc-5720702.html）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u4-1'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第4章第1节 被动运输 第1课时 细胞吸水和失水（人教2019版）',
    '21世纪教育网 导学案：渗透作用原理与质壁分离复原（zy.21cnjy.com/19251971）',
    '教习网 学案：水进出细胞的原理（m.51jiaoxi.com/doc-5720702.html）',
]
mnemonic = '渗透：水过半透膜，低水→高水（低溶质→高溶质）；原生质层=半透膜；浓外>液→分离，反之复原。'
next_link = '下节课：主动运输与被动运输——物质跨膜的方式有哪些。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
