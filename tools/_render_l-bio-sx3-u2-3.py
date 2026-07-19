# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u2-3《胚胎工程》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u2-3.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u2-3.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：体外受精-胚胎移植与试管婴儿
sources = [
    '来源：1978 年英国剑桥 Robert Edwards 以体外受精-胚胎移植（IVF-ET）培育世界首例试管婴儿，并因此获 2010 年诺贝尔生理学或医学奖（gdpmaa.com 世界胚胎学家日）。',
    '来源：体外受精-胚胎移植将精卵取出体外受精、培养为早期胚胎后移入子宫；胚胎移植是胚胎工程的末端关键步骤（MedlinePlus In vitro fertilization）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
