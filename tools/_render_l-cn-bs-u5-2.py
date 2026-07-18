# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u5-2'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '重庆日报《感受“整本书阅读”的魅力》（南开中学五步阅读法）',
    '21世纪教育网《第五单元〈乡土中国〉整本书阅读导读》'
]
lead = '读学术书，先见林，再见树。'
summary = '先见林再见树：浏览、略读、精读、研读、重读，配概念卡吃透学术书。'
reflections = [
    '你读一本难书，通常是从头啃还是先翻框架？',
    '一张概念卡，你打算记哪几栏？',
    '哪一步（浏览／精读／重读）你最想改进？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
