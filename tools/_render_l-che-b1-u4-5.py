# -*- coding: utf-8 -*-
# 化学键 离子键与共价键 — 学生版 9 页 PPT（chunk022）
import os, json
from _classroom_lib import new_presentation
from _kit_chunk022 import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = json.load(open(os.path.join(ROOT, 'preview_v7/_fine_data/l-che-b1-u4-5.json'), encoding='utf-8'))

def clean_bb(bb):
    box = set('\u250c\u2510\u2514\u2518\u2502\u2500\u251c\u2524\u252c\u2534\u253c')
    out = []
    for ln in bb.split('\n'):
        ln = ''.join(ch for ch in ln if ch not in box).strip()
        if ln:
            out.append(ln)
    return out

ex = DATA.get('exercises', '')
basic = ''; adv = ''
if '【提高作业】' in ex:
    b, a = ex.split('【提高作业】', 1)
    basic = b.replace('【基础作业】', '').strip()
    adv = a.strip()
elif '【基础作业】' in ex:
    basic = ex.replace('【基础作业】', '').strip()
    adv = '结合本课梳理化学键 离子键与共价键的性质网络图。'
else:
    basic = ex.strip() or '整理本课核心方程式与概念。'
    adv = '尝试用本课知识解释一个生活或生产中的现象。'

ctx = {
    'id': DATA['id'],
    'subject': '化学',
    'title': DATA['title'],
    'unit': DATA['unitTitle'],
    'subtitle': '离子键与共价键：成键本质与判别',
    'kicker': '高一 · 必修第一册 · 4单元',
    'grade_book': '高一 · 必修第一册（人教版）',
    'tags': DATA.get('tags', []),
    'objectives': DATA.get('objectives', []),
    'background': [DATA.get('textbookAnalysis', '')],
    'sources': ['OpenStax《Chemistry 2e》7.2 Covalent Bonding（共价键：非金属间共用电子对）', 'Chemistry LibreTexts《Ionic and Covalent Bonding》（离子键：阴、阳离子间静电作用）'],
    'keypoints': [l.strip() for l in DATA['keyPoints'].split('\n') if l.strip()],
    'methods': [l.strip() for l in DATA['teachingMethods'].split('\n') if l.strip()],
    'difficulties': [l.strip() for l in DATA['difficulties'].split('\n') if l.strip()],
    'blackboard': clean_bb(DATA.get('blackboard', '')),
    'exercises': [('基础 · 必做', basic), ('提高 · 选做', adv), ('拓展 · 衔接', '用电子式表示 NaCl、HCl 的形成过程，体会两类键的差异。')],
    'summary': ['本单元“物质结构 元素周期律”聚焦微粒间作用力。', '本课核心：化学键是相邻原子间的强烈相互作用；离子键（阴、阳离子静电作用，活泼金属+非金属）与共价键（共用电子对，非金属间）的成键本质与判别。', '向前衔接电子式，向后贯通物质性质与晶体结构。'],
    'thread': ['单元：物质结构 元素周期律', '本课：化学键 离子键与共价键', '后续：电子式与分子结构'],
}

prs, BLANK = new_presentation()
build(prs, BLANK, ctx)
OUT = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b1-u4-5.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
