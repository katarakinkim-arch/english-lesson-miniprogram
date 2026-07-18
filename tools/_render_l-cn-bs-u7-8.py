# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u7-8'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "人民教育出版社《语文·必修上册》第七单元收官设计",
    "单元写作评价：景具体 · 情融入 · 修辞贴",
]
lead = "好短文三标准：景具体、情融入、修辞贴——改一改，读一读。"
summary = "借讲评三典型与分享会，回望「精读→群文→写作」的完整路径。"
reflections = [
    "你的短文属于三典型里的哪一类？下一步怎么改？",
    "本单元哪一篇的写法，你最想用到自己的文字里？",
    "用「自然之眼」看世界，用「景物之笔」写自己——你打算怎么做？",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
