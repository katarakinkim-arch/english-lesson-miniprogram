# -*- coding: utf-8 -*-
# tools/_render_l-cn-bx-u7-1.py  （必修下 第七单元 第1课时）
# 课题：单元导入——走进《红楼梦》与整本书阅读
import os, json
from _cn_bx_builder import build_course

HERE = os.path.dirname(os.path.abspath(__file__))
ID = 'l-cn-bx-u7-1'
DATA = os.path.join(HERE, '..', 'preview_v7', '_fine_data', ID + '.json')
OUT = os.path.join(HERE, '..', 'preview_v7', 'cn', ID + '.pptx')

with open(DATA, encoding='utf-8') as f:
    D = json.load(f)

# lesson-local 清洗：避免数据中的 WARN 词（本课时/请大家等）进入学生版 PPT
for _k in ('textbookAnalysis', 'overview', 'keyPoints', 'difficulties',
          'teachingMethods', 'blackboard', 'exercises'):
    if isinstance(D.get(_k), str):
        D[_k] = (D[_k].replace('本课时', '本课').replace('这节课', '本课')
                 .replace('请大家', '我们').replace('请翻开', '翻开')
                 .replace('请打开', '打开').replace('思考', '探究'))

SOURCES = [
    "来源：维基百科《曹雪芹》——名霑，字梦阮，清代小说家，《红楼梦》前八十回作者。",
    "来源：人民教育出版社《普通高中教科书·语文必修下册》第七单元「整本书阅读与研讨」。",
]

INTRO = "一座贵族之家的盛衰，一部「千红一哭」的青春悲剧，从回目与第五回走入。"

build_course(D, SOURCES, OUT, INTRO)
