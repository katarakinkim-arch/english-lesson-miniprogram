# -*- coding: utf-8 -*-
# 课程 l-cn-bx-u8-8《单元活动——思辨论坛与理性表达反思》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-cn-bx-u8-8.json')
OUT = os.path.join(ROOT, 'preview_v7', 'cn', 'l-cn-bx-u8-8.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：必修下第八单元收官——思辨论坛与理性表达评价量表
sources = [
    '来源：myzxsx.com《淬炼思想的锋刃：在论述的疆场培育理性精神》——'
    '以「青年思辨论坛」为总情境：解构大师论证「兵法」、建立思维「模型库」、现场论辩并复盘，培育理性文风。',
    '来源：河北教育网《思辨性阅读与表达》教学实践（hebtv.com）——'
    '单元任务「解蔽—对话—重构」三阶：文本梳理→对比推理与辩论品鉴→整合重构为结构化表达；自评—互评结合。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
