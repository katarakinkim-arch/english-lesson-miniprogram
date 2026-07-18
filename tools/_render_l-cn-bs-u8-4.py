# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-4'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "人民教育出版社《语文·必修上册》第八单元「词语解释」",
    "词汇学近义辨析：轻重 / 范围 / 搭配 / 色彩 / 语体 五维度",
]
lead = "希望、期望、渴望——不止「差不多」，要用五维度比异。"
summary = "近义辨析五维度：轻重 / 范围 / 搭配 / 色彩 / 语体，再定语境。"
reflections = [
    "你写作文选词，是靠语感还是有维度地比一比？",
    "「希望 / 期望 / 渴望」用在哪句里，最贴合你的心境？",
    "遇到一组近义，你怎样挑出那个最贴切的词？",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
