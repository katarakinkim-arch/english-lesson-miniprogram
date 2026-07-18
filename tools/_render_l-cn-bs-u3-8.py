# -*- coding: utf-8 -*-
# 精细调研渲染器 · l-cn-bs-u3-8 单元学习任务——「古诗今绎」朗诵会与单元总结
# 来源：《中学语文古诗词朗读探究》（期刊）；课堂秀《如何在诗词教学中朗读？》
from _render_fine_common import build

lead = "八首诗词，用声音和现代话，让古诗活在你的表达里。"
prompt = "八首诗词里，哪一句最打动你？用“古诗新说”写一行：它让你对“生命的诗意”想到了什么？"
sources = [
    "《中学语文古诗词朗读探究》（期刊：轻重音·语速·情感）",
    "课堂秀《如何在诗词教学中朗读？》（节奏·重音·语调）",
]
out = build('l-cn-bs-u3-8', lead, prompt, sources)
print('SAVED', out, 'slides=9')
