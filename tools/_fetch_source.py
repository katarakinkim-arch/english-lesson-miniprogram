# -*- coding: utf-8 -*-
"""Fetch a WEB-VERIFIED source summary for a lesson (runs on an OPEN-NETWORK machine).

Primary: Wikipedia REST summary API (zh, then en). Returns an authoritative one-paragraph
summary + the article URL. The driver captures the printed citation and embeds it.

Usage:  _fetch_source.py "<zh_query>" "<en_query>" <out_txt_path>
Prints a short citation line:  "<summary first sentence> — 来源: <url>"
Also writes the full summary + url to <out_txt_path>.
"""
import os, sys, json
try:
    from urllib.request import Request, urlopen
    from urllib.parse import quote
except Exception:
    from urllib2 import Request, urlopen, quote

UA = {'User-Agent': 'edu-lesson-finetune/1.0 (https://github.com; contact: teacher)'}

def get_json(url, timeout=25):
    req = Request(url, headers=UA)
    return json.loads(urlopen(req, timeout=timeout).read().decode('utf-8', 'ignore'))

def summary(lang, query):
    q = quote(query.encode('utf-8'))
    url = "https://%s.wikipedia.org/api/rest_v1/page/summary/%s" % (lang, q)
    try:
        d = get_json(url)
    except Exception:
        return None
    if not d.get('extract') or d.get('title') in (None, 'Not found.'):
        return None
    page = (d.get('content_urls') or {}).get('desktop', {}).get('page', '')
    return {'extract': d['extract'], 'url': page, 'title': d.get('title', '')}

def main():
    if len(sys.argv) < 4:
        print('')
        sys.exit(1)
    zh, en, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    res = None
    for q in [zh, en]:
        if not q:
            continue
        res = summary('zh', q) or summary('en', q)
        if res:
            break
    if not res:
        open(out_path, 'w').write('(未找到权威来源)\n')
        print('')
        sys.exit(0)
    # citation = first sentence, capped
    ext = res['extract']
    first = re.split(r'(?<=[。！？.!?])\s*', ext)[0] if '。' in ext or '.' in ext else ext
    cite = (first[:160] + ('…' if len(first) > 160 else '')) + "  — 来源：" + res['url']
    open(out_path, 'w').write(res['extract'] + "\n\n来源：" + res['url'] + "\n")
    print(cite)

if __name__ == '__main__':
    main()
