# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u2-1《植物细胞工程》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u2-1.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u2-1.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：细胞全能性学说与植物组织培养流程
sources = [
    '来源：细胞全能性由德国植物学家 Haberlandt 于 1902 年提出；1958 年 Steward 以胡萝卜游离细胞培养成完整植株，印证已分化细胞具发育为完整个体的潜能（plantscience.cn《植物细胞的遗传全能性与组织培养形态发生控制》）。',
    '来源：植物组织培养核心流程为「外植体→脱分化→愈伤组织→再分化→植株」；脱/再分化概念见百度百科「脱分化（dedifferentiation）」，生长素与细胞分裂素比例调控分化方向。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
