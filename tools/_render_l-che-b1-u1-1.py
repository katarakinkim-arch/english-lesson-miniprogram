# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u1-1 —— 物质的分类（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u1-1'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "胶体与丁达尔效应：英国物理学家约翰·丁达尔(John Tyndall)于1869年发现并命名；胶体粒子直径约1–100 nm，小于可见光波长(400–760 nm)，对光散射形成光亮通路，可用于区分溶液与胶体（Britannica / 维基百科）。",
    "分类是化学研究的基本方法：初中已建立混合物/纯净物、单质/化合物框架，高中引入交叉分类与树状分类，并为离子反应、氧化还原反应建立认知基础（人教版必修第一册）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
