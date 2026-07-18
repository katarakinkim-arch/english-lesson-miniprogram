# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-6'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '中国孔子网《温良恭俭让》（出处《论语·学而》）',
    '徐州报业《蟾宫折桂：七里文脉上的成才期许》（2026-07-03）'
]
lead = '词语不只是工具，它装着古人的观念。'
summary = '成语和熟语里藏着敬谦、科举、伦理等文化观念，是读懂传统的活化石。'
reflections = [
    '举一个带文化观念的词语，说说它背后的观念。',
    '为什么同一个意思，古人要用这么文雅的说法？',
    '你愿意在作文里用哪类文化词，为什么？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
