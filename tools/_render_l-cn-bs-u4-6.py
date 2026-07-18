# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-6 写作指导——学写倡议书（参与家乡文化建设）
# 来源：宁波晚报《用心观察，掌握方法 把倡议书写得有理有据》；学科网《倡议书写作模板》
from _render_fine_common import build

lead = "为家乡文化提一条倡议，让改变从一句具体的话开始。"
prompt = "你想为家乡文化发出的一条倡议是什么？它具体可做到吗？"
sources = [
    "宁波晚报《用心观察，掌握方法 把倡议书写得有理有据》",
    "学科网《倡议书写作模板》（标题·称呼·正文·落款）",
]
out = build('l-cn-bs-u4-6', lead, prompt, sources)
print('SAVED', out, 'slides=9')
