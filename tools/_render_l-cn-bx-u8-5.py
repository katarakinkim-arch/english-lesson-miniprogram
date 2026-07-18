# -*- coding: utf-8 -*-
# 课程 l-cn-bx-u8-5《六国论 精读——借古论今与中心论点》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-cn-bx-u8-5.json')
OUT = os.path.join(ROOT, 'preview_v7', 'cn', 'l-cn-bx-u8-5.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：苏洵史论，首句立论、分层论证、借古警宋
sources = [
    '来源：古诗文网《六国论》赏析（m.gushiwen.org）——苏洵开篇「六国破灭，非兵不利，战不善，弊在赂秦」，'
    '借古讽今抨击北宋对辽、西夏「岁币求和」，告诫统治者勿重蹈覆辙。',
    '来源：人民教育出版社配套教案（瑞文网 ruiwen.com）——论证结构总分总：分论点「赂秦而力亏」「不赂者以赂者丧」，'
    '以「抱薪救火」比喻赂秦，破立结合，为唐宋八大家政论典范。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
