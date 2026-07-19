# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u4-3《生物武器与生物技术伦理》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u4-3.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u4-3.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：《禁止生物武器公约》与生物武器特点
sources = [
    '来源：《禁止生物武器公约》（BWC，1972 签署、1975 生效）全面禁止发展、生产、储存生物与毒素武器，是首部禁止整类大规模杀伤性武器的多边条约（un.org 生物武器；BWC 手册）。',
    '来源：生物武器具传染性强、传播途径多、成本低、难防控等特点；科技须向善，生物技术应服务于和平（un.org/disarmament）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
