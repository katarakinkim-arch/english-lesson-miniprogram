# -*- coding: utf-8 -*-
# 课程 l-cn-bx-u8-3《群文阅读——古代说理艺术：立论与驳论》学生版 9 页 PPT
# 渲染：chunk011 通用引擎（tools/_kit_chunk011.py）
import os, json
from _kit_chunk011 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-cn-bx-u8-3.json')
OUT = os.path.join(ROOT, 'preview_v7', 'cn', 'l-cn-bx-u8-3.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：必修下第八单元「责任与担当」群文，魏征立论 vs 王安石驳论
sources = [
    '来源：济南市教育教学研究院《群文阅读中的问题引领——统编高中语文必修(下)第八单元教学举例》（jggz.jinan-edu.cn）——'
    '第八单元两组四篇古代思辨文，第一组《谏太宗十思疏》取立论模式（以「思」为线、层层递进），'
    '《答司马谏议书》落「立论与批驳结合」的论述思路，核心任务为「倾听理性的声音」。',
    '来源：21世纪教育网《谏太宗十思疏》《答司马谏议书》比较阅读任务式教案（zy.21cnjy.com）——'
    '魏征以「居安思危，戒奢以俭」立论、比喻论证开篇；王安石先立「名实之争」根本分歧，再逐条驳斥司马光五点责难，先破后立。',
]

build(d, sources,
      lead=derive_lead(d),
      summary=derive_summary(d),
      reflections=derive_reflections(d),
      OUT=OUT)
