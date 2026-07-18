# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-2'
SOURCES = [
    '《林教头风雪山神庙》「风雪」描写赏析：自然风雪推动情节、烘托人物，揭示「官逼民反」',
    '雷珊珊《品风雪妙笔 析环境深意》合格课：风雪四重作用与双层象征',
    '瑞文网教案：「紧」字渲染紧张气氛，为情节做铺垫',
]
LEAD = '一场风雪，把一个安分教头逼成了落草的好汉。'
SUMMARY = '林冲之反不在天性，是被逼；风雪既是天气，也是压顶的世道。'
REFLECTIONS = [
    '林冲性格里，哪一步转折最关键？写一句。',
    '用「忍 → 反」说说环境怎样推动转变。',
    '三个词概括你眼中的林冲。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
