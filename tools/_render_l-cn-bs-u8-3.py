# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u8-3'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "王力《汉语史稿》：古今词义演变（扩大 / 缩小 / 转移 / 色彩变）",
    "《现代汉语词典》：古今异义辨析",
]
lead = "江可专指长江，走曾是跑——读古文，遇熟词先疑。"
summary = "古今词义有扩大、缩小、转移、色彩变四类，读古不套今义。"
reflections = [
    "你读古文时，有没有把今义套到古字上的误判？",
    "四类演变里，哪一类最容易让你读错？",
    "下一回遇见熟词，你会先「疑」一下它的古义吗？",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
