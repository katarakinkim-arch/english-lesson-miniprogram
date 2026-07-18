# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u7-7'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "人民教育出版社《语文·必修上册》第七单元写作任务",
    "统编教材「文学阅读与写作」任务群要求",
]
lead = "选一景、抓特征、融进情——把「很美」换成看得见的感觉。"
summary = "景物短文四步法：选景→特征→融情→修辞，情要化进景里。"
reflections = [
    "你笔下的景，是「空泛」还是「有特征」？差在哪里？",
    "写情时，你习惯硬加一句，还是让景自带情绪？",
    "挑一个范式，重写你以前写过的一段景物文字。",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
