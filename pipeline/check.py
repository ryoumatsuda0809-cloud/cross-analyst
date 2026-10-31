"""Step 4b: check the diagnosis and the report against the computed data.

1. Every number in them must exist in 03a_metrics.md or 02_methods.md
   (allowing for rounding and for ratios written as percentages).
2. Every method ID they mention (M1, M2, ...) must exist in 02_methods.md.

It cannot judge whether the reasoning is good. That part is yours.
"""
from __future__ import annotations

import re
from pathlib import Path

NUM = re.compile(r"(?<![\w.])-?\d[\d,]*(?:\.\d+)?%?")
METHOD_ID = re.compile(r"\bM(\d+)\b")


def numbers_in(text: str) -> list[str]:
    return NUM.findall(text)


def _value(tok: str) -> tuple[float, int, bool]:
    pct = tok.endswith("%")
    t = tok.rstrip("%").replace(",", "")
    decimals = len(t.split(".")[1]) if "." in t else 0
    return float(t), decimals, pct


def allowed_values(*texts: str) -> list[float]:
    vals = []
    for text in texts:
        for tok in numbers_in(text):
            v, _, pct = _value(tok)
            vals.append(v / 100 if pct else v)
    return vals


def matches(tok: str, allowed: list[float]) -> bool:
    v, d, pct = _value(tok)
    for a in allowed:
        candidates = [a * 100] if pct else [a, a * 100, a * 365]
        for c in candidates:
            if round(c, d) == v or abs(c - v) <= 0.5 * 10 ** -d:
                return True
    return False


def ignorable(tok: str) -> bool:
    v, d, pct = _value(tok)
    if pct:
        return False
    if d == 0 and 1900 <= v <= 2100:     # years
        return True
    if d == 0 and 0 <= v <= 10:          # counts, list numbers, "3 bullets"
        return True
    return False


def check_file(target: Path, run: Path) -> list[str]:
    problems = []
    text = target.read_text(encoding="utf-8")
    metrics = (run / "03a_metrics.md").read_text(encoding="utf-8")
    methods = (run / "02_methods.md").read_text(encoding="utf-8")
    allowed = allowed_values(metrics, methods)

    clean = METHOD_ID.sub("", text)                      # "M2" is an ID, not a number
    clean = re.sub(r"\bFY\d{2,4}\b", "", clean)
    for tok in sorted(set(numbers_in(clean))):
        if not ignorable(tok) and not matches(tok, allowed):
            problems.append(f"number not found in metrics or method cards: {tok}")

    known = set(METHOD_ID.findall(methods))
    for mid in sorted(set(METHOD_ID.findall(text)), key=int):
        if mid not in known:
            problems.append(f"method ID M{mid} does not exist in 02_methods.md")
    return problems


def run_checks(run: Path) -> bool:
    ok, checked = True, 0
    refs = True
    for name in ("03a_metrics.md", "02_methods.md"):
        if not (run / name).exists():
            print(f"  [FAIL] {name} is missing, so nothing can be checked. Run the earlier steps first.")
            refs = ok = False
    for name in ("03_diagnosis.md", "diagnostic_report.md"):
        f = run / name
        if not refs or not f.exists():
            print(f"  - {name}: not created yet, skipped")
            continue
        checked += 1
        problems = check_file(f, run)
        if problems:
            ok = False
            print(f"  [FAIL] {name}: {len(problems)} problem(s)")
            for p in problems:
                print(f"      - {p}")
        else:
            print(f"  [OK] {name}: every number and method ID is traceable")
    if checked == 0:
        ok = False
        print("  [FAIL] no document was checked")
    (run / "check_result.txt").write_text("PASS\n" if ok else "FAIL (see terminal output)\n", encoding="utf-8")
    return ok
