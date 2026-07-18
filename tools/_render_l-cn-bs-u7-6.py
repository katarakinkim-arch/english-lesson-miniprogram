# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u7-6'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "姚鼐《登泰山记》（桐城派，「雅洁」文风）",
    "李燕《情景交融，古今同一》（教学论文，析《登泰山记》白描）",
]
lead = "风雪除夕，简净数笔——桐城派用白描画出一座泰山。"
summary = "姚鼐以雅洁白描记登山次第，与浓墨抒情的写法对照成趣。"
reflections = [
    "「苍山负雪，明烛天南」八个字，你眼前浮现怎样的画面？",
    "写景时，简净与繁富两种路数，你更想学哪一种？",
    "试着用白描写一处你见过的风景，少形容、多画意。",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
