#!/bin/bash
# Resumable driver: ensure EVERY one of the 866 lessons has a §4.4-compliant,
# 4-layer-audit-PASS PPTX committed + pushed.
#
# Strategy:
#   - Iterate ALL chunks 000..085 (full coverage; resumable via progress JSON).
#   - Skip any lesson whose _fine_progress/<id>.json already says audit:PASS.
#   - For skipped-but-fine lessons, still stage their artifacts (in case a prior
#     render was done but never committed) — harmless if already committed.
#   - Otherwise render via tools/_render_lesson.py, audit (4 gates), and on PASS
#     write progress JSON + stage files.
#   - Commit per chunk (only when something actually changed) and push.
#
# FIX: use a bash array ADDED so `git add` never sees a leading-space pathspec
#      (the old bug that broke `git add $added` under zsh).
set +e
cd /Users/katarakin/Documents/english-lesson-miniprogram
PY=/Users/katarakin/.workbuddy/binaries/python/envs/default/bin/python
SKIP="l-cn-bs-u1-1 l-cn-bs-u1-2 l-cn-bs-u1-3 l-cn-bs-u1-4 l-cn-bs-u2-1 l-cn-bs-u2-2 l-cn-bs-u2-3 l-cn-bs-u2-4 l-cn-bs-u2-5 l-cn-bs-u2-6 l-cn-bs-u2-7 l-cn-bs-u2-8"
PASSPAT='"audit"[[:space:]]*:[[:space:]]*"PASS"'
mkdir -p preview_v7/_fine_progress

# Precompute a tiny title cache (avoids loading the 5.5MB lessons file per lesson).
"$PY" -c "import json;d=json.load(open('data/_all_lessons.json'));json.dump({k:(v.get('title') if isinstance(v,dict) else '') for k,v in d.get('byId',{}).items()},open('preview_v7/_titles.json','w'),ensure_ascii=False)"

# Stage the driver + helper files themselves once.
git add tools/_driver_render_remaining.sh preview_v7/_titles.json tools/_classroom_lib.py 2>/dev/null
git commit -q -m "chore: resumable pipeline driver + titles cache" 2>/dev/null || true

CHUNKS=""
for i in $(seq 0 85); do CHUNKS="$CHUNKS $(printf '%03d' $i)"; done

TOTAL=0; DONE=0; FAILS=""
for c in $CHUNKS; do
  f="preview_v7/_fine_chunks/chunk_$c.txt"
  [ -f "$f" ] || continue
  ADDED=()
  while IFS= read -r id; do
    [ -z "$id" ] && continue
    TOTAL=$((TOTAL+1))
    pj="preview_v7/_fine_progress/$id.json"
    subj=$(echo "$id" | cut -d- -f2)
    if [ -f "$pj" ] && grep -Eq "$PASSPAT" "$pj"; then
      # Already fine: make sure its artifacts are staged (recovers uncommitted renders).
      [ -f "preview_v7/$subj/$id.pptx" ] && ADDED+=("preview_v7/$subj/$id.pptx")
      ADDED+=("preview_v7/_fine_progress/$id.json")
      continue
    fi
    case " $SKIP " in *" $id "*) continue;; esac
    "$PY" tools/_render_lesson.py "$id" >/dev/null 2>&1 || { echo "RENDER FAIL $id"; FAILS="$FAILS $id"; continue; }
    res=$("$PY" tools/_run_audit_one.py "preview_v7/$subj/$id.pptx" 2>&1)
    if echo "$res" | grep -q "RESULT: PASS"; then
      "$PY" -c "import json;d=json.load(open('preview_v7/_titles.json'));open('preview_v7/_fine_progress/$id.json','w').write(json.dumps({'id':'$id','subj':'$subj','title':d.get('$id',''),'sources':['数据驱动生成(pipeline,未逐课联网调研)'],'photo':'学科配图/色块兜底','audit':'PASS','renderer':'tools/_render_lesson.py','note':'§4.4 pipeline render'},ensure_ascii=False))"
      ADDED+=("preview_v7/$subj/$id.pptx" "preview_v7/_fine_progress/$id.json")
      DONE=$((DONE+1))
    else
      echo "AUDIT FAIL $id"; FAILS="$FAILS $id"
    fi
  done < "$f"
  if [ ${#ADDED[@]} -gt 0 ]; then
    git add "${ADDED[@]}"
    if git commit -q -m "fine(pipeline): chunk_$c 数据驱动精细化渲染（§4.4 四层审计PASS）"; then
      env -u HTTP_PROXY -u HTTPS_PROXY GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -o ServerAliveInterval=20 -o ServerAliveCountMax=3" git push git@github.com:katarakinkim-arch/english-lesson-miniprogram.git main >/dev/null 2>&1 || echo "PUSH FAIL $c"
    else
      echo "commit skip $c (nothing new)"
    fi
  fi
  echo "CHUNK $c done (total=$TOTAL done=$DONE added=${#ADDED[@]})"
done
env -u HTTP_PROXY -u HTTPS_PROXY GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -o ServerAliveInterval=20 -o ServerAliveCountMax=3" git push git@github.com:katarakinkim-arch/english-lesson-miniprogram.git main >/dev/null 2>&1 || echo "FINAL PUSH FAIL"
echo "==== SUMMARY TOTAL=$TOTAL DONE=$DONE FAILS=$FAILS ===="
