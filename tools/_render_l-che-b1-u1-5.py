# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u1-5 —— 氧化还原反应的概念（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u1-5'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "拉瓦锡(Antoine Lavoisier)1774年确立“氧化=与氧化合”的概念，现代氧化还原反应定义为电子转移（Britannica / 台大CASE）。",
    "氧化数(oxidation number)由IUPAC规范，用于追踪电子转移、判断氧化与还原，是配平氧化还原反应的工具（Britannica / IUPAC）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
