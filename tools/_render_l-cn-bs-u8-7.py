# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-7'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '新华网《太全了！大家都来看看咋说敬语》（2016-06-16）',
    '广东教育资源《语言表达要得体》导学案'
]
lead = '用词两道关：准确是底线，得体是高分。'
summary = '准确是底线，得体是高分；看对象、看场合、看语体，词才用得恰当。'
reflections = [
    '写一封正式的求助短信，你会注意哪些敬谦词？',
    '同一件事，对朋友和对长辈说法有何不同？',
    '你最容易在哪种场合用词不当？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
