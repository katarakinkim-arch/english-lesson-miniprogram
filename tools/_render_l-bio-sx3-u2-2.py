# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u2-2《动物细胞工程》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u2-2.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u2-2.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：克隆羊多莉与单克隆抗体杂交瘤技术
sources = [
    '来源：1997 年英国罗斯林研究所 Ian Wilmut 团队在《Nature》发表体细胞克隆羊「多莉」，标志哺乳动物体细胞核克隆时代到来（worldscience.cn《动物克隆技术》）。',
    '来源：单克隆抗体由 César Milstein 与 Georges Köhler 于 1975 年以杂交瘤技术实现规模化制备（百度百科「动物细胞工程」）；动物细胞培养是其余动物细胞工程技术的基础。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
