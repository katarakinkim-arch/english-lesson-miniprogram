# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  Chem LibreTexts《乙烯的聚合》：n CH₂=CH₂ → –(CH₂CH₂)–n，双键打开相连成链生成聚乙烯。
#  有机化学教材：加成反应特征为双键中一个 π 键断裂，原子加在双键两端。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-b2-u7-2.json'), encoding='utf-8'))
sources = [
    'Chem LibreTexts《乙烯的聚合》：n CH₂=CH₂ → –(CH₂CH₂)–n，双键打开相连成链得聚乙烯。',
    '有机化学教材：加成反应特征为双键中一个 π 键断裂，原子加在双键两端。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u7-2.pptx')
build_pptx(data, sources, out)
