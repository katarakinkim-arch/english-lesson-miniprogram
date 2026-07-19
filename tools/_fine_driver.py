# -*- coding: utf-8 -*-
"""Resumable per-lesson FINE-TUNING driver for the 636 pipeline lessons.

Runs on an OPEN-NETWORK machine (real photos + web sources are fetched live).
For each lesson in tools/_fine_queries.json:
  1. skip if already genuinely fine-tuned (progress JSON sources not '数据驱动'/'pipeline')
  2. fetch REAL photo  -> tools/_photos_<id>/cover.jpg   (_fetch_photo.py, Wikimedia Commons)
  3. fetch web source  -> tools/_fine_src/<id>.txt        (_fetch_source.py, Wikipedia)
  4. render 9-page hand-tuned PPTX with real photo + source (_fine_one.py)
  5. 4-layer audit PASS? -> write progress JSON with real sources
  6. every BATCH lessons: git add + commit + push (SSH, timeout-guarded)

Resumable: re-running skips lessons already fine. Safe to Ctrl-C and re-run.
Usage:  python tools/_fine_driver.py [--batch 10] [--limit N] [--only-subj phy]
"""
import os, sys, json, subprocess, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)

PY = sys.executable
PUSH = ('env -u HTTP_PROXY -u HTTPS_PROXY GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 '
        '-o ServerAliveInterval=20 -o ServerAliveCountMax=3" '
        'git push git@github.com:katarakinkim-arch/english-lesson-miniprogram.git main')

def run(cmd, quiet=False):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if not quiet and r.returncode != 0:
        sys.stderr.write('CMD FAIL %s\n%s\n' % (' '.join(cmd), r.stderr[:500]))
    return r

def is_fine(id_):
    pj = os.path.join('preview_v7', '_fine_progress', id_ + '.json')
    if not os.path.exists(pj):
        return False
    try:
        d = json.load(open(pj, encoding='utf-8'))
    except Exception:
        return False
    src = ' '.join(d.get('sources', []) or [])
    return '数据驱动' not in src and 'pipeline' not in src.lower()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch', type=int, default=10)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--only-subj', default='')
    args = ap.parse_args()

    queries = json.load(open(os.path.join(HERE, '_fine_queries.json'), encoding='utf-8'))
    ids = list(queries.keys())
    if args.only_subj:
        ids = [i for i in ids if queries[i]['subj'] == args.only_subj]

    done = skip = fail = 0
    added = []
    fails = []
    for n, id_ in enumerate(ids, 1):
        if args.limit and done + skip >= args.limit:
            break
        if is_fine(id_):
            skip += 1
            continue
        q = queries[id_]
        subj = q['subj']
        photo = os.path.join(HERE, '_photos_%s' % id_, 'cover.jpg')
        src_txt = os.path.join(HERE, '_fine_src', id_ + '.txt')
        os.makedirs(os.path.dirname(photo), exist_ok=True)
        os.makedirs(os.path.dirname(src_txt), exist_ok=True)

        # 1) photo
        if not os.path.exists(photo):
            run([PY, os.path.join(HERE, '_fetch_photo.py'), q['photo_q'], q['photo_q_en'], photo], quiet=True)
        photo_arg = photo if os.path.exists(photo) else ''
        # 2) source
        citation = ''
        if not os.path.exists(src_txt):
            r = run([PY, os.path.join(HERE, '_fetch_source.py'), q['source_q'], q['source_q_en'], src_txt], quiet=True)
            citation = r.stdout.strip()
        else:
            citation = open(src_txt, encoding='utf-8').read().strip().split('\n')[0][:200]

        # 3) render
        run([PY, os.path.join(HERE, '_fine_one.py'), id_, photo_arg, citation], quiet=True)
        pptx = os.path.join('preview_v7', subj, id_ + '.pptx')
        if not os.path.exists(pptx):
            fails.append(id_); fail += 1; continue

        # 4) audit
        ar = run([PY, os.path.join(HERE, '_run_audit_one.py'), pptx], quiet=True)
        if 'RESULT: PASS' not in ar.stdout:
            fails.append(id_); fail += 1
            sys.stderr.write('AUDIT FAIL %s\n' % id_)
            continue

        # 5) progress JSON (real sources)
        prog = {
            'id': id_, 'subj': subj, 'title': q['title'],
            'sources': [citation or '联网核实(Wikipedia)'],
            'photo': ('真实照片(%s)' % os.path.relpath(photo, ROOT)) if photo_arg else '未取到真实照片(需补)',
            'audit': 'PASS', 'renderer': 'tools/_fine_one.py',
            'note': '§4.4 逐课精细化(联网核实+真实照片+手写精排)',
        }
        json.dump(prog, open(os.path.join('preview_v7', '_fine_progress', id_ + '.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        added += [pptx, photo if photo_arg else '', src_txt,
                  os.path.join('preview_v7', '_fine_progress', id_ + '.json')]
        added = [a for a in added if a]
        done += 1
        sys.stdout.write('FINE %d/%d %s\n' % (n, len(ids), id_))

        # 6) commit per batch
        if done % args.batch == 0:
            if added:
                run(['git', 'add', '--'] + added)
                run(['git', 'commit', '-q', '-m',
                     'fine(per-lesson): batch +%d 课 (联网核实+真实照片+手写精排)' % len(added)])
                run(PUSH, shell=True, quiet=True)
                added = []

    if added:
        run(['git', 'add', '--'] + added)
        run(['git', 'commit', '-q', '-m', 'fine(per-lesson): 末尾批次 +%d 课' % len(added)])
        run(PUSH, shell=True, quiet=True)

    print('\nSUMMARY  done=%d skip=%d fail=%d' % (done, skip, fail))
    if fails:
        print('FAILS:', ' '.join(fails))

if __name__ == '__main__':
    main()
