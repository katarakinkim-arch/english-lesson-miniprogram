# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u5-4'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    '中央党校《在乡村振兴中重建社区治理共同体》（礼治·无讼·调解）',
    '安徽检察《乡土中国·无讼》（费孝通田野调查）'
]
lead = '乡土靠礼，也靠理；读懂它，才懂今日之治。'
summary = '乡土靠礼俗与调解维持秩序，“无讼”不是没纠纷，而是把事化在礼中。'
reflections = [
    '你家乡解决矛盾，靠讲理还是靠调解？',
    '今天打官司和过去“无讼”，各有什么利弊？',
    '礼治在今天还有哪些痕迹？'
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
