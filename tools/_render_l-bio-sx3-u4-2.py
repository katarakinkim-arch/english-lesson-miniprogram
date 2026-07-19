# -*- coding: utf-8 -*-
# 课程 l-bio-sx3-u4-2《关注生殖性克隆与人性克隆》学生版 9 页 PPT
import os, json
from _kit_chunk019 import build, derive_lead, derive_summary, derive_reflections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-sx3-u4-2.json')
OUT = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-sx3-u4-2.pptx')

d = json.load(open(DATA, encoding='utf-8'))

# WebSearch 核实（2026-07-18）：生殖性克隆与治疗性克隆的国际立场
sources = [
    '来源：生殖性克隆以复制完整个体为目的，国际社会普遍禁止；2005 年联合国《关于人的克隆宣言》呼吁禁止违背人类尊严的克隆人（联合国新闻；Britannica）。',
    '来源：治疗性克隆经体细胞核移植获取胚胎干细胞用于医疗，受严格监管（如英国 HFEA 许可，胚胎发育至 14 天前销毁）；二者同用核移植而目的不同（联合国大学报告；CCTV）。',
]

build(d, sources, lead=derive_lead(d), summary=derive_summary(d),
      reflections=derive_reflections(d), OUT=OUT)
