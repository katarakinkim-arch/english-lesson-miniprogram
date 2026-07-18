# -*- coding: utf-8 -*-
import os, json
from _render_fine_lib import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID = 'l-cn-bs-u7-5'
with open(os.path.join(ROOT, 'preview_v7', '_fine_data', ID + '.json'), encoding='utf-8') as f:
    d = json.load(f)

sources = [
    "苏轼《赤壁赋》（统编教材必修上册课文）",
    "人民教育出版社《语文·必修上册》第七单元导语",
]
lead = "贬谪夜游，主客问答——在江山风月里，把悲愁读成旷达。"
summary = "苏轼以「水月之喻」化解悲愁，由变与不变走向知足旷达。"
reflections = [
    "客之所悲与苏子之解，你更认同哪一种心境？",
    "「变中有不变」能不能安慰你的一次烦恼？",
    "用「抓主客→明水月喻→悟旷达」的思路，重读一段古文。",
]
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
build(d, sources, lead, summary, reflections, OUT)
