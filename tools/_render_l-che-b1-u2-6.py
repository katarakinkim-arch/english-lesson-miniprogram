# -*- coding: utf-8 -*-
# 化学 chunk021 · l-che-b1-u2-6《气体摩尔体积 物质的量浓度》学生版 9 页
from _kit_chunk021 import main_render

SOURCES = [
    "科普中国《气体摩尔体积》：标况(0℃,101.325kPa) Vm≈22.4 L/mol，决定于分子间平均距离。",
    "百度百科《标准状况》：STP 为 0℃、101.325 kPa。",
]
SIGNATURE = "22.4 L/mol 先画“红线”：标况+气体两条都满足才用；定容俯视/仰视用图判断。"
main_render('l-che-b1-u2-6', SOURCES, SIGNATURE, 'tools/_render_l-che-b1-u2-6.py')
