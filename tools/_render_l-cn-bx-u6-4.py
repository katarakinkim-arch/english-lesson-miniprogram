# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-4'
SOURCES = [
    '语文网《装在套子里的人》课文解说（必修下册第六单元）：套子=法令 / 陈规 / 奴性心理，夸张与讽刺',
    '瑞文网《装在套子里的人》教学参考：别里科夫是专制产物，「套子」成隐喻象征',
    '戈宝权《契诃夫与中国》：「不能够再这样生活下去」',
]
LEAD = '一个把一切套起来的人，让全城都怕——可笑又可悲。'
SUMMARY = '套子象征专制对个性的扼杀；讽刺在可笑之下，藏着沉重的悲。'
REFLECTIONS = [
    '别里科夫的「怪」背后，你看到什么？写一句。',
    '用「行为 / 思想」两层说「套子」。',
    '三个词概括你眼中的讽刺。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
