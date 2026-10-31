#!/usr/bin/env python3
"""cross-analyst: paper-to-diagnosis pipeline (rule-based, runs offline).

    python diagnose.py run                        # whole pipeline, end to end
    python diagnose.py extract                    # step 1-2: PDFs -> text + method sections
    python diagnose.py metrics                    # step 3a: CSV -> computed ratios
    python diagnose.py methods                    # method cards -> quotation check -> 02_methods.md
    python diagnose.py apply                      # rules -> 03_diagnosis.md
    python diagnose.py report                     # template -> diagnostic_report.md
    python diagnose.py check                      # verify numbers and method IDs in the outputs

Common options: --papers DIR  --financials CSV  --cards DIR  --run DIR
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from pipeline import check, financials, pdf_extract, stages  # noqa: E402


def company_name(csv_path: Path) -> str:
    for line in csv_path.read_text(encoding="utf-8").splitlines():
        if line.lower().startswith("# company:"):
            return line.split(":", 1)[1].strip()
    return csv_path.stem


def step_extract(a) -> None:
    out = a.run / "01_extracted"
    out.mkdir(parents=True, exist_ok=True)
    papers = pdf_extract.read_folder(a.papers)
    summary = ["# Extraction summary", "", "| file | title | pages | sections found | method text from | warnings |",
               "|---|---|---|---|---|---|"]
    for p in papers:
        (out / f"{p.path.stem}.full.txt").write_text(p.text, encoding="utf-8")
        (out / f"{p.path.stem}.methods.txt").write_text(
            f"PAPER: {p.title}\nFILE: {p.path.name}\n\n{p.method_text}\n", encoding="utf-8")
        sections = ", ".join(k for k in p.sections if k != "_front")
        summary.append(f"| {p.path.name} | {p.title} | {p.pages} | {sections or '-'} | {p.method_source} | "
                       f"{' '.join(p.warnings) or '-'} |")
        flag = "  [WARN] " + " ".join(p.warnings) if p.warnings else ""
        print(f"  {p.path.name}: {p.pages} page(s), method text from [{p.method_source}], "
              f"{len(p.method_text):,} chars{flag}")
    (out / "_extraction_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")


def step_metrics(a) -> None:
    periods, data = financials.load(a.financials)
    ratios = financials.compute(periods, data)
    md = financials.to_markdown(company_name(a.financials), periods, data, ratios)
    (a.run / "03a_metrics.md").write_text(md, encoding="utf-8")
    missing = sorted({v for vals in ratios.values() for v in vals.values() if isinstance(v, str) and "missing" in v})
    print(f"  {a.financials.name}: {len(periods)} period(s), {len(ratios)} ratios -> 03a_metrics.md")
    for m in missing:
        print(f"    [WARN] {m}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["run", "extract", "metrics", "methods", "apply", "report", "check"])
    ap.add_argument("--papers", type=Path, default=ROOT / "data/papers")
    ap.add_argument("--financials", type=Path, default=ROOT / "data/financials/harbor_lane_supply.csv")
    ap.add_argument("--cards", type=Path, default=ROOT / "data/method_cards", help="folder of method card JSON files")
    ap.add_argument("--run", type=Path, default=ROOT / "outputs/latest", help="folder for this run's outputs")
    a = ap.parse_args()

    a.run.mkdir(parents=True, exist_ok=True)
    plan = {"run": ["extract", "metrics", "methods", "apply", "report", "check"]}.get(a.command, [a.command])
    print(f"Run folder: {a.run}")

    for step in plan:
        print(f"\n[{step}]")
        if step == "extract":
            step_extract(a)
        elif step == "metrics":
            step_metrics(a)
        elif step == "methods":
            stages.run_methods(a.run, a.cards)
        elif step == "apply":
            stages.run_apply(a.run, a.cards)
        elif step == "report":
            stages.run_report(a.run)
        elif step == "check":
            ok = check.run_checks(a.run)
            if a.command == "check" and not ok:
                sys.exit(1)

    report = a.run / "diagnostic_report.md"
    if a.command == "run" and report.exists():
        print(f"\nDone. Report: {report}")


if __name__ == "__main__":
    main()
