# -*- coding: utf-8 -*-
# l-bio-b2-u5-1 基因突变 —— 学生版 9 页课堂 PPT
import os
from _kit_chunk015 import render_bio

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
json_path = os.path.join(ROOT, 'preview_v7', '_fine_data', 'l-bio-b2-u5-1.json')
out_path = os.path.join(ROOT, 'preview_v7', 'bio', 'l-bio-b2-u5-1.pptx')
sources = [
    "Ingram VM (1956) 鉴定镰刀型贫血由 β-珠蛋白基因单碱基替换（A→T）导致。",
    "NCBI GeneReviews: Sickle Cell Disease（HBB c.20A>T, p.Glu6Val）。",
]
render_bio(json_path, sources, out_path)
print('SAVED', out_path)
