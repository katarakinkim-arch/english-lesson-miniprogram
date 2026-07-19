# -*- coding: utf-8 -*-
# 硝酸 — 学生版 9 页 PPT（chunk022）
import os, json
from _classroom_lib import new_presentation
from _kit_chunk022 import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = json.load(open(os.path.join(ROOT, 'preview_v7/_fine_data/l-che-b2-u5-5.json'), encoding='utf-8'))

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
    adv = '结合本课梳理硝酸的性质网络图。'
else:
    basic = ex.strip() or '整理本课核心方程式与概念。'
    adv = '尝试用本课知识解释一个生活或生产中的现象。'

ctx = {
    'id': DATA['id'],
    'subject': '化学',
    'title': DATA['title'],
    'unit': DATA['unitTitle'],
    'subtitle': '强氧化性 · 钝化 · 不稳定',
    'kicker': '高一 · 必修第二册 · 5单元',
    'grade_book': '高一 · 必修第二册（人教版）',
    'tags': DATA.get('tags', []),
    'objectives': DATA.get('objectives', []),
    'background': [DATA.get('textbookAnalysis', '')],
    'sources': ['Chemca / Wikipedia: Nitric Acid（浓硝酸还原产物 NO₂、稀硝酸 NO；浓硝酸使 Fe、Al 钝化）', '奥斯特瓦尔德过程：NH₃ → NO → NO₂ → HNO₃'],
    'keypoints': [l.strip() for l in DATA['keyPoints'].split('\n') if l.strip()],
    'methods': [l.strip() for l in DATA['teachingMethods'].split('\n') if l.strip()],
    'difficulties': [l.strip() for l in DATA['difficulties'].split('\n') if l.strip()],
    'blackboard': clean_bb(DATA.get('blackboard', '')),
    'exercises': [('基础 · 必做', basic), ('提高 · 选做', adv), ('拓展 · 衔接', '对比浓、稀硝酸与 Cu 反应的产物差异，写两个方程式。')],
    'summary': ['硝酸是强氧化性酸。', '本课核心：不稳定（见光分解）、强酸通性、强氧化性（浓→NO₂、稀→NO）、使 Fe/Al 钝化。', '工业由氨经奥斯特瓦尔德过程制得，呼应本单元“氮的循环”。'],
    'thread': ['单元：化工生产中的重要非金属元素', '本课：硝酸', '后续：无机非金属材料'],
}

prs, BLANK = new_presentation()
build(prs, BLANK, ctx)
OUT = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u5-5.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
