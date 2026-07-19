# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  Chem LibreTexts / 大学化学教材：ΔH=H(生成物)−H(反应物)，为状态函数；放热ΔH<0，吸热ΔH>0。ΔH≈Σ断键能−Σ成键能。
#  标准压力取 100 kPa；焓变只与始末态有关（盖斯定律）。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-sx1-u1-1.json'), encoding='utf-8'))
sources = [
    'Chem LibreTexts / 大学化学教材：ΔH=H(生成物)−H(反应物)，为状态函数；放热 ΔH<0，吸热 ΔH>0。ΔH≈Σ断键能−Σ成键能。',
    '标准压力取 100 kPa；焓变只与始末态有关（盖斯定律）。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-sx1-u1-1.pptx')
build_pptx(data, sources, out)
