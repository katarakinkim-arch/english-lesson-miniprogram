# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u1-6 —— 氧化还原反应方程式的配平（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u1-6'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "1880年O.C. Johnson初步建立化合价变化法(离子-电子法)用于配平氧化还原反应方程式（北京大学《大学化学》）。",
    "氧化数概念经IUPAC规范，以“得失电子守恒”确定系数比例，是化合价升降法配平的核心依据（IUPAC / 人教版必修第一册）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
