# -*- coding: utf-8 -*-
# 精细调研来源（已逐条 WebSearch 核实）：
#  Vedantu 食物成分检测：淀粉遇碘变蓝黑；还原糖(葡萄糖)与本尼迪克/新制Cu(OH)₂生成砖红Cu₂O；双缩脲检蛋白显紫。
#  GCSE 生物笔记：油脂=甘油+脂肪酸；蛋白质由氨基酸经肽键连接。
import os, json
from _kit_chunk023 import build_pptx
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = json.load(open(os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-che-b2-u7-5.json'), encoding='utf-8'))
sources = [
    'Vedantu 食物检测：淀粉遇碘变蓝黑；还原糖(葡萄糖)与新制 Cu(OH)₂ 生成砖红 Cu₂O；双缩脲检蛋白显紫。',
    'GCSE 生物笔记：油脂=甘油+脂肪酸；蛋白质由氨基酸经肽键连接。',
]
out = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u7-5.pptx')
build_pptx(data, sources, out)
