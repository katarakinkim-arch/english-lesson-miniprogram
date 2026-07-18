# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第3章第2节 生物膜系统与细胞的协调配合（人教2019版）。
#   21世纪教育网 学案：分泌蛋白合成运输与同位素标记法（zy.21cnjy.com/13471039）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u3-3'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第3章第2节 生物膜系统与细胞的协调配合（人教2019版）',
    '21世纪教育网 学案：分泌蛋白合成运输途径与同位素标记法（zy.21cnjy.com/13471039）',
]
mnemonic = '分泌蛋白：核糖合成→内质加工→高尔包装→胞吐出膜；3H亮氨酸追踪证顺序。'
next_link = '下节课：细胞核——系统的控制中心。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
