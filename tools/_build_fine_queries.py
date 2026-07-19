# -*- coding: utf-8 -*-
"""Build per-lesson fine-tuning query words for the 636 pipeline lessons.

Pure local computation (no network). For each lesson whose progress JSON marks it as
data-driven / pipeline (NOT already genuinely fine-tuned), derive:
  - photo_q[_en] : image search query (zh + english terms) for a real, freely-licensed photo
  - source_q[_en]: web-verification query (for Wikipedia / WebSearch) to cite an authoritative source

Output: tools/_fine_queries.json  { <id>: {...} }
The open-network run reads this and fetches real photos + verified sources.
"""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)
sys.path.insert(0, HERE)

SUBJ_EN = {
    'cn': 'Chinese literature', 'eng': 'English learning', 'pol': 'politics',
    'his': 'history', 'math': 'mathematics', 'che': 'chemistry', 'bio': 'biology',
    'geo': 'geography', 'phy': 'physics',
}
SUBJ_PHOTO_HINT = {
    'cn': '文学 课文', 'eng': 'English campus', 'pol': '政治 会议', 'his': '历史 文物',
    'math': '数学 公式', 'che': '化学 实验', 'bio': '生物 显微', 'geo': '地理 地貌',
    'phy': '物理 实验',
}

def clean(t):
    return re.sub(r'\s+', ' ', str(t or '')).strip()

def ascii_terms(*texts):
    out = []
    seen = set()
    for t in texts:
        for tok in re.findall(r'[A-Za-z][A-Za-z\-]{2,}', str(t or '')):
            tok = tok.strip('-')
            if len(tok) >= 3 and tok.lower() not in seen:
                seen.add(tok.lower()); out.append(tok)
    return out

def is_pipeline(id_):
    pj = os.path.join('preview_v7', '_fine_progress', id_ + '.json')
    if not os.path.exists(pj):
        return True  # no record -> treat as needing fine-tune
    try:
        d = json.load(open(pj, encoding='utf-8'))
    except Exception:
        return True
    src = ' '.join(d.get('sources', []) or [])
    if '数据驱动' in src or 'pipeline' in src.lower():
        return True
    return False

def main():
    data = json.load(open('data/_all_lessons.json', encoding='utf-8'))['byId']
    out = {}
    n = 0
    for id_, les in data.items():
        if not is_pipeline(id_):
            continue
        subj = les.get('_subj', id_.split('-')[1])
        title = clean(les.get('title', ''))
        unit = clean(les.get('unitTitle', ''))
        tags = les.get('tags') or []
        kp = clean(les.get('keyPoints', ''))
        terms = ascii_terms(title, kp, unit, ' '.join(tags), les.get('overview', ''))
        en = SUBJ_EN.get(subj, '')
        # photo query (zh): title is the most specific; add subject hint if short
        photo_q = title
        if len(title) < 6:
            photo_q = f"{title} {SUBJ_PHOTO_HINT.get(subj,'')}".strip()
        # english photo query: subject english + extracted english terms (Commons is english-rich)
        photo_q_en = en
        if terms:
            photo_q_en = (en + ' ' + ' '.join(terms[:4])).strip()
        # verification query
        source_q = f"{title} {subj} 定义 原理 内容".strip()
        source_q_en = (en + ' ' + (terms[0] if terms else title)).strip()
        out[id_] = {
            'id': id_, 'subj': subj, 'title': title,
            'photo_q': photo_q, 'photo_q_en': photo_q_en,
            'source_q': source_q, 'source_q_en': source_q_en,
            'en_terms': terms[:6], 'unit': unit,
        }
        n += 1
    with open(os.path.join(HERE, '_fine_queries.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('WROTE', n, 'fine-tune queries ->', os.path.join(HERE, '_fine_queries.json'))

if __name__ == '__main__':
    main()
