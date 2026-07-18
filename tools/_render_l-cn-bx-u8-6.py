# -*- coding: utf-8 -*-
# 课程 l-cn-bx-u8-6《方法指导——学写议论文（立论·论据·论证）》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-cn-bx-u8-6.json')
OUT = os.path.join(ROOT, 'preview_v7', 'cn', 'l-cn-bx-u8-6.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：议论文三要素与论证逻辑
sources = [
    '来源：《中国教育报》2022-12-23 第9版《参透教材，提升思辨能力》（jyb.cn）——'
    '议论文框架含典型结构与开头结尾类型；论证方法可模仿《劝学》比喻论证、《师说》对比论证、'
    '《邹忌讽齐王纳谏》类比论证。',
    '来源：北京教育考试院《四步越过高考议论文写作这道坎》（bjeea.cn）——'
    '「引言—正文（论点+论据+论证）—结论」框架；论据应典型权威，运用因果/对比/类比分析使论据与论点紧密结合。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
