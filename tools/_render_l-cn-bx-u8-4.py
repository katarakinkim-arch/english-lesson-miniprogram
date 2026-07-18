# -*- coding: utf-8 -*-
# 课程 l-cn-bx-u8-4《阿房宫赋 精读——借古讽今与赋体铺陈》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-cn-bx-u8-4.json')
OUT = os.path.join(ROOT, 'preview_v7', 'cn', 'l-cn-bx-u8-4.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：杜牧借秦警唐，赋体铺陈为讽谏蓄势
sources = [
    '来源：金圣叹《金圣叹批才子古文》评《阿房宫赋》「穷其极丽，至矣尽矣！却是一篇最清出的文字」；'
    '元·祝尧《古赋辨体》称「至杜牧之《阿房宫赋》，古今脍炙」。',
    '来源：教学实录（瑞文网 ruiwen.com）——赋「铺事写志」（托物言志）：前半铺陈宫殿—美人—珍宝，'
    '后半议论秦亡教训，劝诫唐敬宗勿蹈覆辙；「六王毕，四海一，蜀山兀，阿房出」仅十二字写尽统一气象。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
