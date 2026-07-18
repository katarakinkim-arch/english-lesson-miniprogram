# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-8'
SOURCES = [
    '姚勇文名师工作室 评析《「变」的魔术——第六单元》：「洞察世间冷暖，品味百味人生」人物展览角',
    '21世纪教育网《第六单元教学设计》：第9课时展示分享活动，让分享成为习惯',
    '今日头条 基于核心概念的语文大单元教学：第六单元人文主题「观察与批判」',
]
LEAD = '让五篇人物在论坛里碰面，用短评支撑你眼中的他们。'
SUMMARY = '从祥林嫂到格里高尔，小说把人放进环境，让我们看见自己与时代。'
REFLECTIONS = [
    '论坛里，你最想谈哪个人物？用一句点题。',
    '用「靶 / 文 / 析」评价一次发言。',
    '三个词概括你对本单元的新认识。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
