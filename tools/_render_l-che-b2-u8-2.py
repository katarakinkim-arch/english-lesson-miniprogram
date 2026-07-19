# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  ACS / 美国环保署(EPA)：绿色化学 12 原则由 Anastas 与 Warner 于 1998 年提出，核心是源头预防污染、原子经济性。
#  Britannica：绿色化学旨在设计化学产品与工艺，从源头减少或消除有害物质。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-b2-u8-2.json'), encoding='utf-8'))
sources = [
    'ACS / 美国环保署(EPA)：绿色化学 12 原则由 Anastas 与 Warner 于 1998 年提出，核心为源头预防污染、原子经济性。',
    'Britannica：绿色化学旨在设计化学产品与工艺，从源头减少或消除有害物质。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u8-2.pptx')
build_pptx(data, sources, out)
