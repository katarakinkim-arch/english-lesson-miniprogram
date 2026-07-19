# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u3-4《蛋白质工程》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u3-4.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u3-4.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：蛋白质工程与逆中心法则、定向进化
sources = [
    '来源：蛋白质工程以蛋白质结构-功能关系为基础，通过基因修饰或合成定向改造蛋白质，被称为「第二代基因工程」（百度百科「蛋白质工程」；1010jiajiao）。',
    '来源：思路为逆中心法则——预期功能→设计结构→推测氨基酸序列→改造/合成基因；酶的定向进化可提升热稳定性与活性（人民网科普中国《在试管中"驯化"蛋白质》）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
