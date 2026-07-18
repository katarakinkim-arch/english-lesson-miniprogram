# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u7-4'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "史铁生《我与地坛》（统编教材必修上册课文）",
    "人民教育出版社《语文·必修上册》第七单元导语",
]
lead = "一座荒芜的园子，一段深沉的母爱，照见生命如何重生。"
summary = "史铁生借地坛参透生死、借母爱重获力量，景·理·情三层交织。"
reflections = [
    "「荒芜但不衰败」对你而言，可能喻指怎样的处境？",
    "文中最触动你的是地坛还是母亲？它让你想到谁？",
    "尝试用「抓意象→析哲理→悟深情」读一篇你喜欢的散文。",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
