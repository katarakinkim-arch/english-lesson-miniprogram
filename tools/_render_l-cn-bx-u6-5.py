# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _kit_chunk009 import build

ID = 'l-cn-bx-u6-5'
SOURCES = [
    '罗锡英《比较文学视域下的〈促织〉和〈变形记〉》：同属变形母题，异化悲剧（方平1980首倡比较）',
    '21世纪教育网《〈促织〉〈变形记〉联读教学设计》：马克思「异化」释——物对人的统治；一悲一喜结局',
    '21世纪教育网群文教学设计：「整体荒诞、细节真实」，中西异化差异',
]
LEAD = '人变虫——中外两篇都用荒诞，写真实的痛。'
SUMMARY = '同用变形，异在指向：促织刺政治压榨，变形记写人性孤独——一题两解。'
REFLECTIONS = [
    '两篇里，哪一处「变形」最戳你？写一句。',
    '用「政治 ↔ 人性」说中西异。',
    '三个词概括你眼中的「异化」。',
]
build(ID, SOURCES, LEAD, SUMMARY, REFLECTIONS)
