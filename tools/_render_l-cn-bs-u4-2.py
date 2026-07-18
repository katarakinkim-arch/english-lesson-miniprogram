# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-2 调查方法指导——怎样做家乡文化调查
# 来源：《研究性学习活动·访谈法》；人教版《语文》必修上册教学参考书（访谈基本概念与方法）
from _render_fine_common import build

lead = "想弄清一件事，先学会怎么问、怎么记。"
prompt = "如果要采访一位长辈，你的第一个问题会是什么？为什么这么问？"
sources = [
    "《研究性学习活动·访谈法》（提纲结构·由浅入深）",
    "人教版《语文》必修上册教学参考书（访谈基本概念与方法）",
]
out = build('l-cn-bs-u4-2', lead, prompt, sources)
print('SAVED', out, 'slides=9')
