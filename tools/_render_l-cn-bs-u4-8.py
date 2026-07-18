# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-8 单元活动——「家乡文化」分享会与成果展示
# 来源：人教版《语文》必修上册教学参考书（第四单元活动）；21世纪教育网《必修上第四单元大单元教学设计》
from _render_fine_common import build

lead = "把调查、写作和倡议串起来，为家乡做一件实在的事。"
prompt = "这次“看→写→做”，你为家乡做的一件小事是什么？还能继续做什么？"
sources = [
    "人教版《语文》必修上册教学参考书（第四单元活动）",
    "21世纪教育网《必修上第四单元大单元教学设计》（成果展示）",
]
out = build('l-cn-bs-u4-8', lead, prompt, sources)
print('SAVED', out, 'slides=9')
