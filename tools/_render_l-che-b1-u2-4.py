# -*- coding: utf-8 -*-
"""渲染 l-che-b1-u2-4 —— 氯气的实验室制法与氯离子检验（学生版 9 页）"""
import os, json
import _kit_chunk020 as kit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-che-b1-u2-4'
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8'))
sources = [
    "实验室用MnO₂与浓盐酸加热制Cl₂：MnO₂+4HCl(浓)=MnCl₂+Cl₂↑+2H₂O，原理最早由舍勒发现（1010jiajiao / jsccn）。",
    "检验Cl⁻：先加稀HNO₃酸化排除CO₃²⁻等干扰，再加AgNO₃得白色AgCl沉淀（人教版必修第一册 / jsccn）。",
]
photo_note = '本课件未使用无关配图，以学科配色块呈现'
OUT = os.path.join(ROOT, 'preview_v7', 'che', ID + '.pptx')
kit.build(data, sources, photo_note, OUT)
