# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u3-3《基因工程的应用》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u3-3.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u3-3.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：重组人胰岛素、抗虫棉与乳腺生物反应器
sources = [
    '来源：1982 年 FDA 批准重组大肠杆菌生产人胰岛素，为世界首例商业化转基因药品；乙肝疫苗亦由基因重组技术生产（农民日报；life.jnxy.edu.cn）。',
    '来源：乳腺生物反应器将药用蛋白基因连乳腺特异启动子，在动物乳中表达——2009 年 FDA 批准首个转基因动物药物 ATryn（转基因山羊产人抗凝血酶）（life.smxz.com.cn；zxxk）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
