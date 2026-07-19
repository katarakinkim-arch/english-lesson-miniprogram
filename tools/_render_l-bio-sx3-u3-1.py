# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u3-1《重组DNA技术的基本工具》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u3-1.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u3-1.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：限制酶/DNA连接酶/质粒载体
sources = [
    '来源：限制酶（分子手术刀）主要从原核生物分离，识别特定序列并切断磷酸二酯键，产生黏性/平末端，如 EcoRⅠ 识别 GAATTC（21cnjy 学案；百度百科「基因工程」）。',
    '来源：DNA 连接酶（分子缝合针）恢复被切断的磷酸二酯键；载体多为质粒——独立于核外、具自我复制能力的环状双链 DNA，需复制原点、标记基因与多克隆位点（Vedantu Tools of rDNA）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
