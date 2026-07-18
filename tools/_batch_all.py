# -*- coding: utf-8 -*-
"""Batch-generate and 4-gate-audit EVERY lesson in data/_all_lessons.json.

Usage:
  python tools/_batch_all.py                 # all 866
  python tools/_batch_all.py --subj cn       # only Chinese
  python tools/_batch_all.py --limit 20      # first 20 (smoke test)
  python tools/_batch_all.py --force         # re-render even if pptx exists

Never aborts on a single bad lesson: failures are recorded and the run continues.
Results -> preview_v7/_BATCH_RESULTS.json
"""
import os, sys, json, argparse, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)

import _render_lesson as R
import _audit_text, _audit_scrim, _audit_layout

def bounds_ok(path):
    prs = _audit_text.Presentation(path)  # reuse pptx
    W = prs.slide_width/914400.0; H = prs.slide_height/914400.0; EPS=0.02
    for slide in prs.slides:
        for sh in slide.shapes:
            l=sh.left/914400.0 if sh.left is not None else 0
            t=sh.top/914400.0 if sh.top is not None else 0
            w=sh.width/914400.0 if sh.width is not None else 0
            h=sh.height/914400.0 if sh.height is not None else 0
            if l+w > W+EPS or t+h > H+EPS:
                return False
    return True

def audit_one(path):
    rows, bh, wh = _audit_text.audit(path)
    scrim = _audit_scrim.audit(path)
    fnd = _audit_layout.audit(path)
    hard = [(i,iss) for i,iss in fnd if any('TEXT_OVERFLOW' in x or 'EMPTY' in x for x in iss)]
    b = bounds_ok(path)
    ok = (len(bh)==0) and (len(scrim)==0) and (not hard) and b
    return ok, {'block': len(bh), 'scrim': len(scrim), 'layout_hard': len(hard), 'bounds': b,
                'warn': len(wh), 'slides': len(rows)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--subj', default=None)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()

    with open('data/_all_lessons.json', encoding='utf-8') as f:
        data = json.load(f)
    ids = data['ids']
    if args.subj:
        ids = [i for i in ids if data['byId'][i].get('_subj') == args.subj]
    if args.limit:
        ids = ids[:args.limit]

    results = {}
    done = passn = failn = 0
    for i, lid in enumerate(ids, 1):
        out = os.path.join('preview_v7', data['byId'][lid].get('_subj','cn'), lid + '.pptx')
        try:
            if not args.force and os.path.exists(out):
                # already rendered; just audit to refresh status
                ok, det = audit_one(out)
            else:
                R.render(lid)
                ok, det = audit_one(out)
            results[lid] = 'PASS' if ok else 'FAIL'
            if ok: passn += 1
            else:
                failn += 1
                results[lid + '__detail'] = det
        except Exception as e:
            results[lid] = 'ERROR'
            results[lid + '__err'] = str(e)[:200]
            failn += 1
        done += 1
        if done % 25 == 0 or done == len(ids):
            print(f"  [{done}/{len(ids)}] pass={passn} fail={failn}", flush=True)

    os.makedirs('preview_v7', exist_ok=True)
    with open('preview_v7/_BATCH_RESULTS.json', 'w', encoding='utf-8') as f:
        json.dump({'total': len(ids), 'pass': passn, 'fail': failn, 'results': results}, f, ensure_ascii=False, indent=1)
    print(f"DONE total={len(ids)} PASS={passn} FAIL={failn}")

if __name__ == '__main__':
    main()
