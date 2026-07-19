# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  OpenStax《有机化学》：甲烷为正四面体结构，键角109.5°，碳原子sp³杂化（Linus Pauling, 1931）。
#  Chemistry LibreTexts：甲烷四根C–H键完全等价，键角109.5°，是最简单的有机化合物。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-b2-u7-1.json'), encoding='utf-8'))
sources = [
    'OpenStax《有机化学》：甲烷为正四面体，键角109.5°，碳 sp³ 杂化（Linus Pauling, 1931）。',
    'Chemistry LibreTexts：甲烷四根 C–H 键完全等价，是最简单的有机化合物。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u7-1.pptx')
build_pptx(data, sources, out)
