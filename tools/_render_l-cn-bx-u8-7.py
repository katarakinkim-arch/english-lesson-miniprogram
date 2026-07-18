# -*- coding: utf-8 -*-
# 课程 l-cn-bx-u8-7《写作实践与讲评——议论文修改与提升》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-cn-bx-u8-7.json')
OUT = os.path.join(ROOT, 'preview_v7', 'cn', 'l-cn-bx-u8-7.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：议论文升格「点、释、例、析」与修改范式
sources = [
    '来源：广东教育资源平台《聚焦逻辑升格，助力作文备考》（zy.gdedu.gov.cn）——'
    '「原文呈现—问题诊断—逻辑优化—升格示范」四步流程，核心是让「论点—论据—论证」形成严密链条，摒弃事例堆砌。',
    '来源：期刊《高三作文升格训练中教学评协同推进的实践模式探究》——'
    '借鉴《谏太宗十思疏》递进结构、《六国论》「弊在赂秦—赂秦力亏」因果链优化作文逻辑，'
    '小组互评聚焦「结构/论据关联/逻辑衔接」三维。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
