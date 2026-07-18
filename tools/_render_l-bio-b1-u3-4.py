# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第3章第3节 细胞核——系统的控制中心（人教2019版）。
#   21世纪教育网 导学案：核膜/核仁/染色质与遗传信息库（zy.21cnjy.com/19251967）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u3-4'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第3章第3节 细胞核——系统的控制中心（人教2019版）',
    '21世纪教育网 导学案：核膜/核孔/核仁/染色质与遗传信息库（zy.21cnjy.com/19251967）',
]
mnemonic = '核膜双、核孔选、核仁造核糖；染色质=染色体同物异形；核是遗传信息库。'
next_link = '下节课：水进出细胞的原理——物质如何跨过细胞膜。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
