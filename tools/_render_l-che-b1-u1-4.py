# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u1-4 —— 离子反应与离子方程式（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u1-4'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "阿伦尼乌斯1884年的电离(电解分离)理论说明溶液中存在离子，奠定离子反应的本质——离子之间的反应（台大CASE / askiitians）。",
    "离子方程式用实际参加反应的离子表示，揭示同一类反应的本质；写、拆、删、查为常用步骤（人教版必修第一册）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
