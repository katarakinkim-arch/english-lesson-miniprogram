# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  中学化学教学资料：乙醇与钠 2CH₃CH₂OH+2Na→2CH₃CH₂ONa+H₂↑，比水缓和；催化氧化得乙醛。
#  人教版必修第二册 第七章：羟基(–OH)决定乙醇的主要化学性质。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-b2-u7-3.json'), encoding='utf-8'))
sources = [
    '中学化学教学资料：乙醇与钠 2CH₃CH₂OH+2Na→2CH₃CH₂ONa+H₂↑，较水缓和；催化氧化得乙醛。',
    '人教版必修第二册 第七章：羟基(–OH)决定乙醇的主要化学性质。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u7-3.pptx')
build_pptx(data, sources, out)
