# -*- coding: utf-8 -*-
# 课程 l-bio-b1-u2-1《细胞中的元素和化合物》学生版 9 页 PPT
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b1-u2-1.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b1-u2-1.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：元素分类、C为核心、化合物含量、检测显色
sources = [
    '来源：成都师范学院《中学生物探究性实验指导手册》（cdnu.edu.cn）——检测原理：'
    '还原糖+斐林试剂→砖红色沉淀；脂肪+苏丹Ⅲ→橘黄色；蛋白质+双缩脲试剂→紫色；淀粉+碘→蓝色。',
    '来源：高中生物实验指导（hs-lab.cn）——本实验是唯一需水浴加热（还原糖）与唯一需显微镜（脂肪）的检测；'
    '选材须白/近白色以避免色素干扰，斐林试剂甲、乙液等量混匀现配现用。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
