# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-1 单元导入——家乡文化面面观
# 来源：人教版《语文》必修上册教学参考书（第四单元目标与编写意图）；21世纪教育网《必修上第四单元大单元教学设计》
from _render_fine_common import build

lead = "家乡不只有远方，更有身边值得记录的人、物与故事。"
prompt = "你的家乡有什么“只有那儿才有”的东西？用五要素框架，它属于哪一类？"
sources = [
    "人教版《语文》必修上册教学参考书（第四单元目标与编写意图）",
    "21世纪教育网《必修上第四单元大单元教学设计》（当代文化参与）",
]
out = build('l-cn-bs-u4-1', lead, prompt, sources)
print('SAVED', out, 'slides=9')
