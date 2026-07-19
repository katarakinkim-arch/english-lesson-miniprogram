# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u2-2 —— 钠的化合物（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u2-2'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "过氧化钠Na₂O₂能与CO₂、H₂O反应放出O₂（2Na₂O₂+2CO₂=2Na₂CO₃+O₂），用作呼吸面具、潜水艇的供氧剂（MITCHEM / 1010jiajiao）。",
    "Na₂CO₃与NaHCO₃在溶解性、热稳定性、与酸反应速率上差异显著，是鉴别碳酸钠与碳酸氢钠的依据（人教版必修第一册）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
