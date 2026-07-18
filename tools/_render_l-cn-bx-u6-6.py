# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-6'
SOURCES = [
    '21世纪教育网《统编版高中语文必修上册「学写文学短评」教案》：定题宜小、引—析—评、叙议结合',
    '王从华《建立文学短评写作学习元素的进阶规划》：「引—析—评」结构',
    '21世纪教育网《第三单元 学写文学短评》：以小见大、叙议结合',
]
LEAD = '把「我喜欢」变成「我认为」——学写一篇小说短评。'
SUMMARY = '好短评 = 定小靶 + 引原句 + 析人物环境主题；去我加文，评论才立。'
REFLECTIONS = [
    '挑一个人物，写下一句你想评的「靶心」。',
    '用「靶 / 文 / 析」说清短评三步。',
    '三个词概括你眼中的好评论。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
