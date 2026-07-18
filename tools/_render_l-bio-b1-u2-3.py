# -*- coding: utf-8 -*-
# 精细调研来源（已 WebSearch 核实）：
#   教材：人民教育出版社《普通高中教科书·生物学·必修1·分子与细胞》第2章第5节（人教2019版）。
#   21世纪教育网 同步学案：核酸由核苷酸连接而成，DNA/RNA 化学组成与分布对比（zy.21cnjy.com/13144133）。
#   教习网 导学案：遗传信息储存在脱氧核苷酸的排列顺序中；DNA双链、RNA单链（www.51jiaoxi.com/doc-17143136.html）。
import os, json
from _kit_chunk012 import build_bio_pptx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-bio-b1-u2-3'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))

sources = [
    '人民教育出版社《生物学·必修1·分子与细胞》第2章第5节（人教2019版）',
    '21世纪教育网 同步学案：DNA/RNA 化学组成与分布对比（zy.21cnjy.com/13144133）',
]
mnemonic = 'DNA脱氧核糖、碱基A/T/C/G；RNA核糖、碱基A/U/C/G；信息在排列顺序。'
next_link = '下节课：糖类和脂质——生物体的能源与结构物质。'

out = os.path.join(ROOT, 'preview_v7', 'bio', ID + '.pptx')
build_bio_pptx(data, sources, out, mnemonic=mnemonic, next_link=next_link)
print('SAVED', out)
