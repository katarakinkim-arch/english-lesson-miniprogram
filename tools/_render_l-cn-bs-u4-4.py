# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-4 实地调查实践（二）——口述史采访
# 来源：人教版《语文》必修上册教学参考书（访谈法·王思斌）；《研究性学习活动·访谈法》（原话记录·追问推进）
from _render_fine_common import build

lead = "听长辈讲过去，把原话记下来，让记忆不被忘掉。"
prompt = "你听到的最打动人的一句“原话”是什么？它藏着怎样的文化记忆？"
sources = [
    "人教版《语文》必修上册教学参考书（访谈法·王思斌）",
    "《研究性学习活动·访谈法》（原话记录·追问推进）",
]
out = build('l-cn-bs-u4-4', lead, prompt, sources)
print('SAVED', out, 'slides=9')
