# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  Studysmarter：标准燃烧热指 101 kPa 下 1 mol 可燃物完全燃烧生成稳定氧化物(CO₂(g)、H₂O(l))的焓变，恒为放热。
#  Vedantu：强酸强碱中和热约 −57.3 kJ/mol，本质 H⁺(aq)+OH⁻(aq)→H₂O(l)。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-sx1-u1-3.json'), encoding='utf-8'))
sources = [
    'Studysmarter：标准燃烧热指 101 kPa 下 1 mol 可燃物完全燃烧生成稳定氧化物(CO₂(g)、H₂O(l))的焓变，恒为放热。',
    'Vedantu：强酸强碱中和热约 −57.3 kJ/mol，本质 H⁺(aq)+OH⁻(aq)→H₂O(l)。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-sx1-u1-3.pptx')
build_pptx(data, sources, out)
