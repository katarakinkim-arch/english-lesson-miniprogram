# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u1-3 —— 电解质的电离（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u1-3'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "“电解质(electrolyte)”一词由迈克尔·法拉第(Michael Faraday)于1834年提出，研究电解定律时创立（RSC 图书章节 / 百度百科）。",
    "阿伦尼乌斯(Svante Arrhenius)1884年提出电离理论：电解质溶于水会自发离解成自由移动的离子，无需通电；1903年获诺贝尔化学奖（台大CASE / Britannica）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
