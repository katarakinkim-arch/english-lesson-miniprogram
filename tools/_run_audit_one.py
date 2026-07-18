# tools/_run_audit_one.py
# Run all four audit gates on a SINGLE pptx (the __main__ blocks of _audit_text/
# _audit_scrim/_audit_layout glob only preview_v7/*.pptx, ignoring cn/ subfolders).
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(os.path.dirname(HERE))

TARGET = sys.argv[1] if len(sys.argv) > 1 else "preview_v7/cn/l-cn-bs-u2-7.pptx"

from _audit_text import audit as audit_text
from _audit_scrim import audit as audit_scrim
from _audit_layout import audit as audit_layout
import importlib.util
spec = importlib.util.spec_from_file_location("cb", os.path.join(HERE, "_check_bounds.py"))
cb = importlib.util.module_from_spec(spec)
# _check_bounds reads sys.argv[1] at import time; inject our target
sys.argv = ["_check_bounds.py", TARGET]
spec.loader.exec_module(cb)

ok = True
print("="*72); print("AUDIT TARGET:", TARGET); print("="*72)

rows, bh, wh = audit_text(TARGET)
print(f"\n[1/4] TEXT-TONE  slides={len(rows)}")
if bh:
    ok = False
    print(f"  >>> BLOCK-TONE {len(bh)} hit(s) — FAIL")
    for i, pat, ctx in bh:
        print(f"      slide {i:>2}: '{pat}'  …{ctx}…")
else:
    print("  BLOCK-TONE CLEAN")
if wh:
    print(f"  WARN-TONE {len(wh)} hit(s) — review:")
    for i, pat, ctx in wh:
        print(f"      slide {i:>2}: '{pat}'  …{ctx}…")
else:
    print("  WARN-TONE none")
risky = [r for r in rows if r[2] > 700]
if risky:
    print("  DENSITY >700 chars: " + ", ".join(f"s{r[0]}({r[2]})" for r in risky))
print("  SLIDE CHARS: " + " ".join(f"s{r[0]}:{r[2]}" for r in rows))

fails = audit_scrim(TARGET)
print(f"\n[2/4] SCRIM (text-on-photo)")
if fails:
    ok = False
    print(f"  >>> {len(fails)} UNPROTECTED — FAIL")
    for i, txt, ov in fails:
        print(f"      slide {i:>2}: '{txt}' overlap {ov}px^2")
else:
    print("  all photo+text slides PROTECTED")

fnd = audit_layout(TARGET)
print(f"\n[3/4] LAYOUT")
if fnd:
    hard = [(i, iss) for i, iss in fnd if any("TEXT_OVERFLOW" in x or "EMPTY" in x for x in iss)]
    for i, iss in fnd:
        print(f"      slide {i:>2}: " + " | ".join(iss))
    if hard:
        ok = False
        print("  >>> LAYOUT hard-fail (overflow/empty) present — FAIL")
    else:
        print("  (only PHOTO+TEXT advisories — verified by scrim audit above)")
else:
    print("  LAYOUT OK")

print(f"\n[4/4] BOUNDS: {cb.W_IN:.3f} x {cb.H_IN:.3f} in")
bproblems = 0
for i, slide in enumerate(cb.prs.slides, 1):
    worst_r = worst_b = 0.0
    for sh in slide.shapes:
        l = sh.left/914400.0 if sh.left is not None else 0
        t = sh.top/914400.0 if sh.top is not None else 0
        w = sh.width/914400.0 if sh.width is not None else 0
        h = sh.height/914400.0 if sh.height is not None else 0
        if l+w > cb.W_IN + cb.EPS: worst_r = max(worst_r, l+w-cb.W_IN)
        if t+h > cb.H_IN + cb.EPS: worst_b = max(worst_b, t+h-cb.H_IN)
    if worst_r>0 or worst_b>0:
        bproblems += 1
        print(f"  slide {i:02d}: OVERFLOW right+{worst_r:.2f} bottom+{worst_b:.2f}")
if bproblems==0:
    print("  ALL WITHIN BOUNDS")

print("\n" + "="*72)
print("RESULT:", "PASS (all four gates)" if ok and bproblems==0 else "FAIL — fix & re-render")
sys.exit(0 if (ok and bproblems==0) else 1)
