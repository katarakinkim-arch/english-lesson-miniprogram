# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u5-7'
SOURCES = [
    '21世纪教育网《统编教材必修下册第五单元写作导引》：对象意识 / 场合意识 / 结构逻辑 / 修辞意识',
    '21世纪教育网《第五单元写作教学〈演讲稿的写作〉》：传声性、鼓动性、对象意识',
    '《学会鼓动和说服——例谈实用性阅读与交流任务群的实践》：演讲展示含撰写—排练—演讲—评价',
]
LEAD = '把一篇初稿，改成一则站得住的演说或说理文。'
SUMMARY = '好演说、好说理文，靠对象感、层次与适配场合的语言——三标准缺一不可。'
REFLECTIONS = [
    '翻出自己的一篇初稿，圈出最该补「对象感」的一处。',
    '用一句话说清：这篇演说想让听众改变什么。',
    '三个词概括你眼中「好演说」的样子。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
