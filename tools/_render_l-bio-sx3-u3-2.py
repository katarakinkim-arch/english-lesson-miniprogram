# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u3-2《基因工程的基本操作程序》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u3-2.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u3-2.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：基因工程四步程序与表达载体
sources = [
    '来源：基因工程四步为获基因→建载体→导入受体→检测鉴定；表达载体=目的基因+启动子（RNA 聚合酶结合以驱动转录）+终止子+标记基因（gaokaoq.com；百度百科）。',
    '来源：导入依受体而异——植物常用农杆菌转化法、动物用显微注射、微生物用 Ca²⁺ 处理成感受态细胞；检测含 DNA/RNA/蛋白质水平与个体鉴定（百度百科「基因工程的基本操作程序」）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
