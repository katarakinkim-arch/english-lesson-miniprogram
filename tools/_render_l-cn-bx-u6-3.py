# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-3'
SOURCES = [
    '21世纪教育网《〈祝福〉〈林教头风雪山神庙〉联读教学设计》：同设风雪而命运迥异，环境「5面9点」',
    '陈小云《互动、共生：固化与异化》：恩格斯典型环境论，单元导语「人物与社会环境共生互动」',
    '赵洁《层级进阶》：单元大概念「个人命运与社会制度」',
]
LEAD = '同写人被环境压，一个被「吃」，一个被「逼」。'
SUMMARY = '异之后见共性：典型环境造典型性格——环境不是布景，是塑人的手。'
REFLECTIONS = [
    '双栏里，你最先填的是哪一格？为什么。',
    '用「吃 ↔ 逼」一句话说两文差异。',
    '三个词概括群文读法。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
