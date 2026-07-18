# -*- coding: utf-8 -*-
# 课程 l-bio-b1-u1-1《细胞是生命活动的基本单位》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u1-1.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u1-1.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：细胞学说建立（施莱登/施旺/魏尔肖）与生命系统层次
sources = [
    '来源：中国科学院古脊椎动物与古人类研究所《遗传学再叙》（ivpp.cas.cn）——'
    '1838年施莱登发表「植物发生论」，1839年施旺提出「细胞学说」并扩展至所有生命；'
    '1858年魏尔肖补充「细胞通过分裂产生新细胞」，恩格斯列其为19世纪三大自然科学发现之一。',
    '来源：科普中国《显微镜的发现与细胞学说的提出》（kepuchina.cn）——'
    '1665年胡克用自制显微镜观察软木首次命名 cell；施莱登、施旺建立学说揭示生物界结构统一性；'
    '魏尔肖补全「新细胞来自已存在的细胞」。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
