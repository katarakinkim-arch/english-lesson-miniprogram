# -*- coding: utf-8 -*-
# 原电池 — 学生版 9 页 PPT（chunk022）
import os, json
from _classroom_lib import new_presentation
from _kit_chunk022 import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = json.load(open(os.path.join(ROOT, 'preview_v7/_fine_data/l-che-b2-u6-2.json'), encoding='utf-8'))

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
    adv = '结合本课梳理原电池的性质网络图。'
else:
    basic = ex.strip() or '整理本课核心方程式与概念。'
    adv = '尝试用本课知识解释一个生活或生产中的现象。'

ctx = {
    'id': DATA['id'],
    'subject': '化学',
    'title': DATA['title'],
    'unit': DATA['unitTitle'],
    'subtitle': '化学能转化为电能',
    'kicker': '高一 · 必修第二册 · 6单元',
    'grade_book': '高一 · 必修第二册（人教版）',
    'tags': DATA.get('tags', []),
    'objectives': DATA.get('objectives', []),
    'background': [DATA.get('textbookAnalysis', '')],
    'sources': ['Chemistry LibreTexts: Galvanic Cells（负极氧化、正极还原，电子由负极流向正极）', '丹尼尔电池 Zn|ZnSO₄||CuSO₄|Cu：E°cell=E°cathode−E°anode'],
    'keypoints': [l.strip() for l in DATA['keyPoints'].split('\n') if l.strip()],
    'methods': [l.strip() for l in DATA['teachingMethods'].split('\n') if l.strip()],
    'difficulties': [l.strip() for l in DATA['difficulties'].split('\n') if l.strip()],
    'blackboard': clean_bb(DATA.get('blackboard', '')),
    'exercises': [('基础 · 必做', basic), ('提高 · 选做', adv), ('拓展 · 衔接', '观察干电池/水果电池，判断正负极与电子流向。')],
    'summary': ['化学能可直接变电能。', '本课核心：负极（活泼金属）失电子氧化、正极得电子还原；电子由负极经外电路流向正极（电流相反）。', '构成需两电极+电解质+闭合回路，向后衔接反应速率与限度。'],
    'thread': ['单元：化学反应与能量', '本课：原电池', '后续：化学反应速率与限度'],
}

prs, BLANK = new_presentation()
build(prs, BLANK, ctx)
OUT = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u6-2.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
