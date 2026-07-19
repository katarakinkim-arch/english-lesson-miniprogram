# -*- coding: utf-8 -*-
# 硫酸 — 学生版 9 页 PPT（chunk022）
import os, json
from _classroom_lib import new_presentation
from _kit_chunk022 import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = json.load(open(os.path.join(ROOT, 'preview_v7/_fine_data/l-che-b2-u5-2.json'), encoding='utf-8'))

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
    adv = '结合本课梳理硫酸的性质网络图。'
else:
    basic = ex.strip() or '整理本课核心方程式与概念。'
    adv = '尝试用本课知识解释一个生活或生产中的现象。'

ctx = {
    'id': DATA['id'],
    'subject': '化学',
    'title': DATA['title'],
    'unit': DATA['unitTitle'],
    'subtitle': '吸水性 · 脱水性 · 强氧化性',
    'kicker': '高一 · 必修第二册 · 5单元',
    'grade_book': '高一 · 必修第二册（人教版）',
    'tags': DATA.get('tags', []),
    'objectives': DATA.get('objectives', []),
    'background': [DATA.get('textbookAnalysis', '')],
    'sources': ['科普/教材：浓硫酸具吸水性、脱水性、强氧化性', 'Cu+2H₂SO₄(浓)→CuSO₄+SO₂↑+2H₂O（加热，见 arjunschool 等权威整理）'],
    'keypoints': [l.strip() for l in DATA['keyPoints'].split('\n') if l.strip()],
    'methods': [l.strip() for l in DATA['teachingMethods'].split('\n') if l.strip()],
    'difficulties': [l.strip() for l in DATA['difficulties'].split('\n') if l.strip()],
    'blackboard': clean_bb(DATA.get('blackboard', '')),
    'exercises': [('基础 · 必做', basic), ('提高 · 选做', adv), ('拓展 · 衔接', '比较浓硫酸与稀硫酸在组成、性质上的本质不同。')],
    'summary': ['硫酸是用途最广的化工原料之一。', '本课核心：浓硫酸的吸水性（物理、作干燥剂）、脱水性（化学、使有机物炭化）与强氧化性（与 Cu 等加热生成 SO₂）。', '稀释须“酸入水、沿壁慢搅”，呼应前课 SO₂，并衔接后续氮、氨的氧化还原体系。'],
    'thread': ['单元：化工生产中的重要非金属元素', '本课：硫酸', '后续：氮的氧化物与酸雨'],
}

prs, BLANK = new_presentation()
build(prs, BLANK, ctx)
OUT = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u5-2.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
