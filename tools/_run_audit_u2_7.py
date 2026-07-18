# tools/_run_audit_u2_7.py
# Runs all four audits directly on a single target pptx (the __main__ blocks of
# _audit_text/_audit_scrim/_audit_layout glob only preview_v7/*.pptx, ignoring cn/).
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(os.path.dirname(HERE))  # project root

TARGET = sys.argv[1] if len(sys.argv) > 1 else "preview_v7/cn/l-cn-bs-u2-7.pptx"

from _audit_text import audit as audit_text
from _audit_scrim import audit as audit_scrim
from _audit_layout import audit as audit_layout

ok = True
print("="*72)
print("AUDIT TARGET:", TARGET)
print("="*72)

# --- 1. TEXT TONE ---
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
    print(f"  WARN-TONE {len(wh)} hit(s) — human review:")
    for i, pat, ctx in wh:
        print(f"      slide {i:>2}: '{pat}'  …{ctx}…")
else:
    print("  WARN-TONE none")
risky = [r for r in rows if r[2] > 700]
if risky:
    print("  DENSITY >700 chars: " + ", ".join(f"s{r[0]}({r[2]})" for r in risky))
print("  SLIDE CHARS: " + " ".join(f"s{r[0]}:{r[2]}" for r in rows))

# --- 2. SCRIM (text-on-photo protection) ---
fails = audit_scrim(TARGET)
print(f"\n[2/4] SCRIM (text-on-photo)")
if fails:
    ok = False
    print(f"  >>> {len(fails)} UNPROTECTED — FAIL")
    for i, txt, ov in fails:
        print(f"      slide {i:>2}: '{txt}' overlap {ov}px^2")
else:
    print("  all photo+text slides PROTECTED")

# --- 3. LAYOUT (overflow / photo-text / empty) ---
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

print("\n[4/4] BOUNDS — run separately via _check_bounds.py")
print("="*72)
print("RESULT:", "PASS (text/scrim/layout)" if ok else "FAIL — fix renderer & re-render")
sys.exit(0 if ok else 1)
