# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-1'
SOURCES = [
    '人民教育出版社《普通高中教科书语文必修下册》第六单元（人文主题·观察与批判）',
    '赵洁《层级进阶：〈祝福〉「不可靠叙述」意蕴的教学探索》：许寿裳评「惨在礼教吃祥林嫂」',
    '瑞文网《谈谈祥林嫂外貌变化和封建礼教的关系》',
]
LEAD = '在祝福的鞭炮声里，读一个被环境「吃」掉的女人。'
SUMMARY = '祥林嫂的死，不在个人命苦，而在封建礼教与冷漠世风——环境「吃人」。'
REFLECTIONS = [
    '祥林嫂命运里，哪一步最让你难受？写下来。',
    '用「热闹 ↔ 死」说说环境的作用。',
    '三个词概括你眼中的鲁镇。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
