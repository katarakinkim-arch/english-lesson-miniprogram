# -*- coding: utf-8 -*-
# 课程 l-bio-b1-u1-2《细胞的多样性和统一性》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u1-2.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u1-2.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：原核/真核根本区别、统一性、蓝藻光合、高倍镜
sources = [
    '来源：人教版(2019)必修1《1.2 细胞的多样性和统一性》知识清单（21cnjy.com）——'
    '科学家据有无核膜包被的细胞核，将细胞分为原核/真核；原核如细菌、蓝细菌（含藻蓝素叶绿素能光合），真核如动植物真菌。',
    '来源：细胞结构科普（中国科学院 lkx.cas.cn）——原核与真核细胞共有细胞膜、细胞质、核糖体、DNA；'
    '统一性体现于化学组成、结构、遗传物质（均以DNA为遗传物质）与直接能源物质（ATP）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
