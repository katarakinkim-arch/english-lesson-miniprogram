# -*- coding: utf-8 -*-
# 课程 l-bio-b1-u2-2《蛋白质是生命活动的主要承担者》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u2-2.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u2-2.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：氨基酸脱水缩合、肽键公式、结构多样性、变性
sources = [
    '来源：人教版(2019)必修1 第2章第4节《蛋白质是生命活动的主要承担者》必背知识点（21cnjy.com）——'
    '功能含结构蛋白、催化（酶）、运输（血红蛋白）、信息传递（胰岛素）、免疫（抗体）；人体21种氨基酸，8种必需。',
    '来源：同步课堂《生命活动的主要承担者——蛋白质》（tongzhuo100.com）——'
    '结构多样性源于氨基酸种类/数目/排列顺序及肽链空间结构千差万别；'
    '变性仅破坏空间结构不破坏肽键，仍与双缩脲试剂呈紫色。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
