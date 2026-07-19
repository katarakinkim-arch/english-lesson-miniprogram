# -*- coding: utf-8 -*-
# 无机非金属材料 — 学生版 9 页 PPT（chunk022）
import os, json
from _classroom_lib import new_presentation
from _kit_chunk022 import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = json.load(open(os.path.join(ROOT, 'preview_v7/_fine_data/l-che-b2-u5-6.json'), encoding='utf-8'))

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
    adv = '结合本课梳理无机非金属材料的性质网络图。'
else:
    basic = ex.strip() or '整理本课核心方程式与概念。'
    adv = '尝试用本课知识解释一个生活或生产中的现象。'

ctx = {
    'id': DATA['id'],
    'subject': '化学',
    'title': DATA['title'],
    'unit': DATA['unitTitle'],
    'subtitle': '硅 · 二氧化硅 · 硅酸盐与新材料',
    'kicker': '高一 · 必修第二册 · 5单元',
    'grade_book': '高一 · 必修第二册（人教版）',
    'tags': DATA.get('tags', []),
    'objectives': DATA.get('objectives', []),
    'background': [DATA.get('textbookAnalysis', '')],
    'sources': ['科普中国·科学百科：二氧化硅 SiO₂（原子晶体，光导纤维原料）', '石英玻璃：高纯 SiO₂ 特种玻璃（“玻璃之王”）'],
    'keypoints': [l.strip() for l in DATA['keyPoints'].split('\n') if l.strip()],
    'methods': [l.strip() for l in DATA['teachingMethods'].split('\n') if l.strip()],
    'difficulties': [l.strip() for l in DATA['difficulties'].split('\n') if l.strip()],
    'blackboard': clean_bb(DATA.get('blackboard', '')),
    'exercises': [('基础 · 必做', basic), ('提高 · 选做', adv), ('拓展 · 衔接', '搜集生活中硅酸盐制品（玻璃、陶瓷、水泥）的实例。')],
    'summary': ['材料是人类文明的基石。', '本课核心：硅（半导体，芯片与太阳能电池）；SiO₂（原子晶体、光导纤维、刻蚀玻璃）；硅酸盐（水泥玻璃陶瓷）与新型材料。', '把“元素—性质—材料—应用”串成一条线。'],
    'thread': ['单元：化工生产中的重要非金属元素', '本课：无机非金属材料', '后续：第六单元 化学反应与能量'],
}

prs, BLANK = new_presentation()
build(prs, BLANK, ctx)
OUT = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u5-6.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
