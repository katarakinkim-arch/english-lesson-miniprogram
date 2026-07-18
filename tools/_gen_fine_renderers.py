# -*- coding: utf-8 -*-
# 生成 10 个 tools/_render_<id>.py（按 §4.4 每课一个渲染器）。
import os
IDS = [
    'l-cn-bs-u1-5', 'l-cn-bs-u1-6', 'l-cn-bs-u1-7', 'l-cn-bs-u1-8',
    'l-cn-bs-u3-1', 'l-cn-bs-u3-2', 'l-cn-bs-u3-3',
    'l-cn-bs-u3-4', 'l-cn-bs-u3-5', 'l-cn-bs-u3-6',
]
HERE = os.path.dirname(os.path.abspath(__file__))
TPL = '''# -*- coding: utf-8 -*-
# 学生版 9 页课堂 PPT 渲染器（手写精排，色块兜底）。
import os
from _fine_cn_kit import build, load_data, SOURCES, new_presentation

ID = '{id}'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
data = load_data(ID)
sources = SOURCES[ID]
prs, BLANK = new_presentation()
build(prs, BLANK, data, sources)
OUT = os.path.join(ROOT, 'preview_v7', 'cn', ID + '.pptx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
prs.save(OUT)
print('SAVED', OUT, 'slides=', len(prs.slides._sldIdLst))
'''
for id_ in IDS:
    path = os.path.join(HERE, '_render_' + id_ + '.py')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(TPL.format(id=id_))
    print('wrote', path)
print('done', len(IDS))
