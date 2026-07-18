# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-5 资料整理与撰写——风物志与调查报告
# 来源：人教版《语文》必修上册教学参考书（调查报告要素）；21世纪教育网《必修上第四单元大单元教学设计》
from _render_fine_common import build

lead = "把卡片变成文章，让家乡的故事被更多人看见。"
prompt = "你写成的风物志或调查报告，最想让人记住的是哪一句？"
sources = [
    "人教版《语文》必修上册教学参考书（调查报告要素）",
    "21世纪教育网《必修上第四单元大单元教学设计》（资料整理与撰写）",
]
out = build('l-cn-bs-u4-5', lead, prompt, sources)
print('SAVED', out, 'slides=9')
