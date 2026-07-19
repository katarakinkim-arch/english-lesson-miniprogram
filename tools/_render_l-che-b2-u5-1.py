# -*- coding: utf-8 -*-
# 硫单质与二氧化硫 — 学生版 9 页 PPT（chunk022）
import os, json
from _classroom_lib import new_presentation
from _kit_chunk022 import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = json.load(open(os.path.join(ROOT, 'preview_v7/_fine_data/l-che-b2-u5-1.json'), encoding='utf-8'))

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
    adv = '结合本课梳理硫单质与二氧化硫的性质网络图。'
else:
    basic = ex.strip() or '整理本课核心方程式与概念。'
    adv = '尝试用本课知识解释一个生活或生产中的现象。'

ctx = {
    'id': DATA['id'],
    'subject': '化学',
    'title': DATA['title'],
    'unit': DATA['unitTitle'],
    'subtitle': '二氧化硫的性质与酸雨关联',
    'kicker': '高一 · 必修第二册 · 5单元',
    'grade_book': '高一 · 必修第二册（人教版）',
    'tags': DATA.get('tags', []),
    'objectives': DATA.get('objectives', []),
    'background': [DATA.get('textbookAnalysis', '')],
    'sources': ['Encyclopædia Britannica: Sulfur dioxide（SO₂ 为无色有毒气体，大气污染物与酸雨前体）', '教材分析：SO₂ 为酸性氧化物，漂白为化合可逆、非氧化'],
    'keypoints': [l.strip() for l in DATA['keyPoints'].split('\n') if l.strip()],
    'methods': [l.strip() for l in DATA['teachingMethods'].split('\n') if l.strip()],
    'difficulties': [l.strip() for l in DATA['difficulties'].split('\n') if l.strip()],
    'blackboard': clean_bb(DATA.get('blackboard', '')),
    'exercises': [('基础 · 必做', basic), ('提高 · 选做', adv), ('拓展 · 衔接', '查阅本地空气质量日报，找一找 SO₂ 与酸雨的关联数据。')],
    'summary': ['本单元“化工生产中的重要非金属元素”从硫切入，二氧化硫是典型酸性氧化物。', '本课核心：SO₂ 的酸性氧化物通性、漂白（化合、可逆、非氧化）与还原性——与氯水氧化漂白本质不同。', '向前衔接硫酸（下节课），向后呼应氮氧化物与酸雨，构建“性质—用途—危害”一体的非金属观。'],
    'thread': ['单元：化工生产中的重要非金属元素', '本课：硫单质与二氧化硫（单元第1课时）', '后续：硫酸 → 氮氧化物 → 氨 → 硝酸 → 无机材料'],
}

prs, BLANK = new_presentation()
build(prs, BLANK, ctx)
OUT = os.path.join(ROOT, 'preview_v7', 'che', 'l-che-b2-u5-1.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
