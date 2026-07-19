# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u2-1 —— 钠的性质（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u2-1'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "钠由英国化学家汉弗里·戴维(Humphry Davy)于1807年通过电解熔融氢氧化钠首次制得，并以拉丁文Natrium得名Na（台大CASE / 百度百科）。",
    "钠原子最外层仅1个电子(3s¹)，极易失去，因此具强还原性、化学性质极活泼（百度百科 / 人教版必修第一册）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
