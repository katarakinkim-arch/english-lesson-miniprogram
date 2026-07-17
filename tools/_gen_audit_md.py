# -*- coding: utf-8 -*-
"""从 _STANDARD_AUDIT.jsonl 生成去重后的汇总报告 _STANDARD_AUDIT.md。
按 id 去重（保留最后一条记录），统计 PASS/WARN/FAIL/ERROR，列出未达标课。
"""
import os, json, collections

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(BASE, 'preview_v7', '_STANDARD_AUDIT.jsonl')
OUT = os.path.join(BASE, 'preview_v7', '_STANDARD_AUDIT.md')

recs = {}
order = []
for line in open(LOG, encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    try:
        r = json.loads(line)
    except Exception:
        continue
    rid = r.get('id')
    if rid not in recs:
        order.append(rid)
    recs[rid] = r

c = collections.Counter(r['verdict'] for r in recs.values())
total = len(recs)
subj = collections.Counter(r.get('subj') for r in recs.values())
bad = [(r['id'], r['verdict'], r.get('block'), r.get('overflow'),
        r.get('scrim_unprotected'), r.get('bounds_over'))
       for r in recs.values() if r['verdict'] in ('FAIL', 'WARN', 'ERROR')]

L = []
L.append('# 课堂版 PPT 逐课审计汇总（四层门禁：教师口吻 / 文字溢出 / 照片遮罩 / 越界）\n')
L.append('总课数 **%d** ｜ PASS **%d** ｜ WARN **%d** ｜ FAIL **%d** ｜ ERROR **%d**\n' % (
    total, c.get('PASS', 0), c.get('WARN', 0), c.get('FAIL', 0), c.get('ERROR', 0)))
L.append('\n## 各学科分布\n')
for s in sorted(subj):
    L.append('- %s：%d 课' % (s, subj[s]))
if bad:
    L.append('\n## 未达标清单\n')
    for b in bad:
        L.append('- `%s` %s（block=%s overflow=%s scrim=%s bounds=%s）' % b)
else:
    L.append('\n## 结论\n')
    L.append('全部 **%d** 课通过四层审计门禁，达成「手精 + 每课必查」标准。\n' % total)
    L.append('教师口吻清零（block=0）、文字无溢出、照片文字页均有遮罩保护、无 shape 越界。\n')

open(OUT, 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', OUT, '| total', total, '| verdicts', dict(c))
