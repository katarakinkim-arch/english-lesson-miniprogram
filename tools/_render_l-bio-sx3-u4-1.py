# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u4-1《转基因生物的安全性》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u4-1.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u4-1.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：转基因食品安全性评估与权威共识
sources = [
    '来源：我国对农业转基因生物实行分级、分阶段安全评价，含食用安全（毒性、致敏性）与环境安全（基因漂移、生物多样性）两部分（caas.cn；moa.gov.cn）。',
    '来源：经安全评价依法批准上市的转基因食品与传统食品同等安全；OECD、WHO 与 FAO 均得出结论其不比传统育种更有风险（moa.gov.cn 吴孔明、万建民院士访谈）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
