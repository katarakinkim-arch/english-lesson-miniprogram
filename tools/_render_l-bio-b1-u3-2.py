# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第3章第2节 细胞器之间的分工（人教2019版）。
#   21世纪教育网 学案：线粒体/叶绿体/内质网/高尔基体等八大细胞器（zy.21cnjy.com/13471038）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u3-2'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第3章第2节 细胞器之间的分工（人教2019版）',
    '21世纪教育网 学案：线粒体/叶绿体/内质网/高尔基体/核糖体/溶酶体/中心体/细胞骨架（zy.21cnjy.com/13471038）',
]
mnemonic = '双层线叶、单层网高溶泡、无膜糖中；动物有中心体、植物有叶绿液泡。'
next_link = '下节课：生物膜系统与细胞的协调配合——追踪分泌蛋白的旅程。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
