# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u5-5'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '光明日报《包路芳：费孝通与〈乡土中国〉》（血缘地缘专节）',
    '费孝通《乡土中国·血缘和地缘》：地缘是契约社会的基础'
]
lead = '从血缘到契约，乡土在松动中走向现代。'
summary = '血缘定身份，地缘定契约；从血缘社会走向地缘社会，是乡土松动的一步。'
reflections = [
    '你的户籍、邻里，是血缘还是地缘在起作用？',
    '为什么现代社会更讲“契约”而非“亲疏”？',
    '从家乡到城市，你感受到这种分离了吗？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
