# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  CIE iGCSE 金属冶炼：活泼金属(K~Al)电解；中等(Zn~Cu)热还原；不活泼(Hg~Ag)热分解。冰晶石将Al₂O₃熔点由约2050℃降至约950℃。
#  Hall–Héroult 法(1886)：电解熔融 Al₂O₃(冰晶石)制铝。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-b2-u8-1.json'), encoding='utf-8'))
sources = [
    'CIE iGCSE 金属冶炼：活泼金属(K~Al)电解；中等(Zn~Cu)热还原；不活泼(Hg~Ag)热分解。冰晶石将 Al₂O₃ 熔点由约2050℃降至约950℃。',
    'Hall–Héroult 法(1886)：电解熔融 Al₂O₃(冰晶石)制铝。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u8-1.pptx')
build_pptx(data, sources, out)
