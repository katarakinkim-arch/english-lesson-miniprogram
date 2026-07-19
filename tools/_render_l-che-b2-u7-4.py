# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  Master Organic Chemistry：Fischer 酯化（1895 Emil Fischer）为酸催化可逆平衡 RCOOH+R'OH⇌RCOOR'+H₂O。
#  有机化学教材：酯化机理"酸脱羟基、醇脱氢"，水中氧来自羧基。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-b2-u7-4.json'), encoding='utf-8'))
sources = [
    'Master Organic Chemistry：Fischer 酯化（1895 Emil Fischer）为酸催化可逆平衡 RCOOH+R\'OH⇌RCOOR\'+H₂O。',
    '有机化学教材：酯化机理"酸脱羟基、醇脱氢"，水中氧来自羧基。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u7-4.pptx')
build_pptx(data, sources, out)
