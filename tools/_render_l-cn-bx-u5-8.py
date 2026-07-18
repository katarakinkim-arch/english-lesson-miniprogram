# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u5-8'
SOURCES = [
    '《学会鼓动和说服——例谈实用性阅读与交流任务群的实践》：系统实践迁移，演讲活动含观点—逻辑—撰写—排练—评价',
    '21世纪教育网《统编教材必修下册第五单元写作导引》：实用性阅读与交流任务群',
    '基于UbD理论的大单元教学：第五单元人文主题「抱负与使命」',
]
LEAD = '把读到的、写到的、讲到的，汇成一次登台与一份反思。'
SUMMARY = '从马克思到林觉民，实用言说以真知与真情动人，对象是魂。'
REFLECTIONS = [
    '哪一篇演说最打动你？用一句话说清原因。',
    '用「对象 / 层次 / 鼓动」三个词评价一次发言。',
    '写一句你对接下来的语文学习的期待。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
