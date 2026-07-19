#!/bin/bash
# Focused driver: finish the REMAINING missing lessons so all 866 have a
# §4.4-compliant, 4-layer-audit-PASS PPTX committed + pushed.
#
# Logic per missing lesson id:
#   - cn hand-tuned (SKIP list): audit the EXISTING pptx; keep it (write PASS
#     json) if it passes; otherwise fall back to the pipeline renderer.
#   - everything else: render via tools/_render_lesson.py, audit, write PASS json.
#   - on render/audit failure -> recorded in FAILS and skipped.
set +e
cd /Users/katarakin/Documents/english-lesson-miniprogram
PY=/Users/katarakin/.workbuddy/binaries/python/envs/default/bin/python
PASSPAT='"audit"[[:space:]]*:[[:space:]]*"PASS"'
CN_SKIP="l-cn-bs-u1-1 l-cn-bs-u1-2 l-cn-bs-u1-3 l-cn-bs-u1-4 l-cn-bs-u2-1 l-cn-bs-u2-2 l-cn-bs-u2-3 l-cn-bs-u2-4 l-cn-bs-u2-5 l-cn-bs-u2-6 l-cn-bs-u2-7 l-cn-bs-u2-8"
mkdir -p preview_v7/_fine_progress

# tiny title cache
"$PY" -c "import json;d=json.load(open('data/_all_lessons.json'));json.dump({k:(v.get('title') if isinstance(v,dict) else '') for k,v in d.get('byId',{}).items()},open('preview_v7/_titles.json','w'),ensure_ascii=False)"

# compute exact missing set
"$PY" -c "
import json,os
d=json.load(open('data/_all_lessons.json'))['byId']
miss=[]
for k in d:
    subj=k.split('-')[1]
    pj='preview_v7/_fine_progress/%s.json'%k
    pptx='preview_v7/%s/%s.pptx'%(subj,k)
    ok=False
    if os.path.exists(pj):
        try:
            if json.load(open(pj)).get('audit')=='PASS': ok=True
        except: pass
    if not (ok and os.path.exists(pptx)):
        miss.append(k)
open('preview_v7/_missing.txt','w').write('\n'.join(miss))
print('missing computed:', len(miss))
"

TOTAL=0; DONE=0; FAILS=""; ADDED=()
while IFS= read -r id; do
  [ -z "$id" ] && continue
  TOTAL=$((TOTAL+1))
  subj=$(echo "$id" | cut -d- -f2)
  pj="preview_v7/_fine_progress/$id.json"
  if [ -f "$pj" ] && grep -Eq "$PASSPAT" "$pj" && [ -f "preview_v7/$subj/$id.pptx" ]; then continue; fi
  case " $CN_SKIP " in *" $id "*) 
    if [ -f "preview_v7/$subj/$id.pptx" ]; then
      res=$("$PY" tools/_run_audit_one.py "preview_v7/$subj/$id.pptx" 2>&1)
      if echo "$res" | grep -q "RESULT: PASS"; then
        "$PY" -c "import json;d=json.load(open('preview_v7/_titles.json'));open('preview_v7/_fine_progress/$id.json','w').write(json.dumps({'id':'$id','subj':'$subj','title':d.get('$id',''),'sources':['手写精排(§4.4)'],'photo':'手写精排','audit':'PASS','renderer':'hand-tuned','note':'保留手写精排版本'},ensure_ascii=False))"
        ADDED+=("preview_v7/_fine_progress/$id.json")
        DONE=$((DONE+1)); echo "CN KEEP $id"; continue
      fi
    fi
    ;;
  esac
  "$PY" tools/_render_lesson.py "$id" >/dev/null 2>&1 || { echo "RENDER FAIL $id"; FAILS="$FAILS $id"; continue; }
  res=$("$PY" tools/_run_audit_one.py "preview_v7/$subj/$id.pptx" 2>&1)
  if echo "$res" | grep -q "RESULT: PASS"; then
    "$PY" -c "import json;d=json.load(open('preview_v7/_titles.json'));open('preview_v7/_fine_progress/$id.json','w').write(json.dumps({'id':'$id','subj':'$subj','title':d.get('$id',''),'sources':['数据驱动生成(pipeline,未逐课联网调研)'],'photo':'学科配图/色块兜底','audit':'PASS','renderer':'tools/_render_lesson.py','note':'§4.4 pipeline render'},ensure_ascii=False))"
    ADDED+=("preview_v7/$subj/$id.pptx" "preview_v7/_fine_progress/$id.json")
    DONE=$((DONE+1))
  else
    echo "AUDIT FAIL $id"; FAILS="$FAILS $id"
  fi
done < preview_v7/_missing.txt

if [ ${#ADDED[@]} -gt 0 ]; then
  git add "${ADDED[@]}"
  if git commit -q -m "fine(pipeline): 补齐剩余 $DONE 课（§4.4 四层审计PASS）"; then
    env -u HTTP_PROXY -u HTTPS_PROXY GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -o ServerAliveInterval=20 -o ServerAliveCountMax=3" git push git@github.com:katarakinkim-arch/english-lesson-miniprogram.git main >/dev/null 2>&1 || echo "PUSH FAIL"
  else
    echo "commit skip (nothing new)"
  fi
fi
echo "==== MISSING SUMMARY TOTAL=$TOTAL DONE=$DONE FAILS=$FAILS ===="
