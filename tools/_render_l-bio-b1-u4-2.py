# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《生物学·必修1·分子与细胞》第4章第2节 主动运输与胞吞、胞吐（人教2019版）。
#   学科网 学案：主动运输特点意义与被动运输对比（zxxk.com/soft/55115544）。
#   教习网 学案：自由扩散/协助扩散/主动运输（51jiaoxi.com/doc-12845960.html）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u4-2'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第4章第2节 主动运输与胞吞、胞吐（人教2019版）',
    '学科网 学案：主动运输特点意义与被动运输对比（zxxk.com/soft/55115544）',
    '教习网 学案：自由扩散/协助扩散/主动运输（51jiaoxi.com/doc-12845960.html）',
]
mnemonic = '自由扩散顺不载不耗、协助扩散顺载不耗、主动运输逆载耗能；主动维持浓度差。'
next_link = '下节课：胞吞、胞吐与细胞膜的流动性——大分子如何进出细胞。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
