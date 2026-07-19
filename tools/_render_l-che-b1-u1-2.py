# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u1-2 —— 物质的转化（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u1-2'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "物质的转化遵循类别决定路径：金属→碱性氧化物→碱→盐，非金属→酸性氧化物→酸→盐（chemguide / 高中化学教材）。",
    "价-类二维图以横轴类别、纵轴价态表示物质转化，是元素化合物学习的核心认知工具（人教版必修第一册）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
