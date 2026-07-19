# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u2-3 —— 氯气的化学性质（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u2-3'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "氯气由瑞典化学家舍勒(Carl Wilhelm Scheele)于1774年用软锰矿与浓盐酸加热制得；戴维1810年确证其为元素并命名为chlorine（希腊语“黄绿色”）（Britannica / 百度百科）。",
    "氯原子最外层7个电子，反应中易得电子，故Cl₂具强氧化性，能把Fe、Cu氧化到高价氯化物（人教版必修第一册）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
