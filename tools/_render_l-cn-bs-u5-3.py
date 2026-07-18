# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u5-3'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '爱思想 aisixiang.com 费孝通《乡土中国·差序格局》原文',
    '光明日报《包路芳：费孝通与〈乡土中国〉》（差序格局专节）'
]
lead = '一圈水波，照见中国人与人的远近。'
summary = '差序格局像水波纹，以“己”为中心分出亲疏；团体格局像柴捆，界限清晰。'
reflections = [
    '用一圈水波，画出你身边人际关系的远近。',
    '公私在你生活里，会因圈子不同而“伸缩”吗？',
    '差序格局和团体格局，你更熟悉哪一种？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
