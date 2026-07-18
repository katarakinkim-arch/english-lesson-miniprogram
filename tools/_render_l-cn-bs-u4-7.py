# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u4-7 写作实践与讲评——倡议书修改与提升
# 来源：宁波晚报《用心观察，掌握方法 把倡议书写得有理有据》；人教版《语文》必修上册教学参考书（倡议书评改）
from _render_fine_common import build

lead = "对照好倡议的标准，把自己的倡议书写得更扎实。"
prompt = "对照“好倡议四标准”，你改后的倡议书进步最大的是哪一条？"
sources = [
    "宁波晚报《用心观察，掌握方法 把倡议书写得有理有据》",
    "人教版《语文》必修上册教学参考书（倡议书评改）",
]
out = build('l-cn-bs-u4-7', lead, prompt, sources)
print('SAVED', out, 'slides=9')
