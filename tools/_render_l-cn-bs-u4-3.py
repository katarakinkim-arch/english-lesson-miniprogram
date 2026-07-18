# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-3 实地调查实践（一）——家乡风物走访
# 来源：21世纪教育网《必修上第四单元大单元教学设计》（记录家乡的人和物）；人教版教学参考书（风物志写法）
from _render_fine_common import build

lead = "走近一处风物，用眼睛和耳朵，把记忆留下来。"
prompt = "你走访的那处风物，最值得记住的特征和故事是什么？"
sources = [
    "21世纪教育网《必修上第四单元大单元教学设计》（记录家乡的人和物）",
    "人教版《语文》必修上册教学参考书（风物志写法）",
]
out = build('l-cn-bs-u4-3', lead, prompt, sources)
print('SAVED', out, 'slides=9')
