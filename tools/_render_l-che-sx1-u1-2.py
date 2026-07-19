# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  中学化学教学：热化学方程式必须注明物质状态(s/l/g/aq)；系数表示物质的量，可用分数；ΔH与计量数成正比，逆反应变号。
#  Chem LibreTexts：状态不同反应热不同（如 H₂O(g) 与 H₂O(l) 相差汽化热）。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-sx1-u1-2.json'), encoding='utf-8'))
sources = [
    '中学化学教学：热化学方程式必须注明物质状态(s/l/g/aq)；系数表物质的量，可用分数；ΔH 与计量数成正比，逆反应变号。',
    'Chem LibreTexts：状态不同反应热不同（如 H₂O(g) 与 H₂O(l) 相差汽化热）。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-sx1-u1-2.pptx')
build_pptx(data, sources, out)
