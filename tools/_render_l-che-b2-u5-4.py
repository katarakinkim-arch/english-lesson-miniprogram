# -*- coding: utf-8 -*-
# 氨和铵盐 — 学生版 9 页 PPT（chunk022）
import os, json
from _classroom_lib import new_presentation
from _kit_chunk022 import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = json.load(open(os.path.join(ROOT, 'preview_v7/_fine_data/l-che-b2-u5-4.json'), encoding='utf-8'))

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
    adv = '结合本课梳理氨和铵盐的性质网络图。'
else:
    basic = ex.strip() or '整理本课核心方程式与概念。'
    adv = '尝试用本课知识解释一个生活或生产中的现象。'

ctx = {
    'id': DATA['id'],
    'subject': '化学',
    'title': DATA['title'],
    'unit': DATA['unitTitle'],
    'subtitle': '喷泉实验 · 铵根检验 · 实验室制法',
    'kicker': '高一 · 必修第二册 · 5单元',
    'grade_book': '高一 · 必修第二册（人教版）',
    'tags': DATA.get('tags', []),
    'objectives': DATA.get('objectives', []),
    'background': [DATA.get('textbookAnalysis', '')],
    'sources': ['21世纪教育 高一化学人教版必修2 氨和铵盐 课件（喷泉实验、NH₄⁺ 检验）', 'Ammonia Fountain demonstration（NH₃ 极易溶于水、溶液呈碱性）'],
    'keypoints': [l.strip() for l in DATA['keyPoints'].split('\n') if l.strip()],
    'methods': [l.strip() for l in DATA['teachingMethods'].split('\n') if l.strip()],
    'difficulties': [l.strip() for l in DATA['difficulties'].split('\n') if l.strip()],
    'blackboard': clean_bb(DATA.get('blackboard', '')),
    'exercises': [('基础 · 必做', basic), ('提高 · 选做', adv), ('拓展 · 衔接', '用湿润红色石蕊试纸检验 NH₃，体会铵态氮肥的检验思路。')],
    'summary': ['氨是工业的“ nitrogen carrier”。', '本课核心：NH₃ 极易溶于水、水溶液呈碱性；与酸生成铵盐（白烟）；实验室制法与 NH₄⁺ 检验（加碱加热放 NH₃）。', '向前承接氮氧化物，向后衔接硝酸的工业制备（氨的催化氧化）。'],
    'thread': ['单元：化工生产中的重要非金属元素', '本课：氨和铵盐', '后续：硝酸（氨的催化氧化）'],
}

prs, BLANK = new_presentation()
build(prs, BLANK, ctx)
OUT = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u5-4.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
