#!/usr/bin/env python3
"""cross-analyst: paper-to-diagnosis pipeline (LLM API).

    python diagnose.py run      --mock            # whole pipeline, fake model, no API key needed
    python diagnose.py run                        # whole pipeline with the LLM API
    python diagnose.py extract                    # step 1-2: PDFs -> text + method sections (no LLM)
    python diagnose.py metrics                    # step 3a: CSV -> computed ratios (no LLM)
    python diagnose.py methods | apply | report   # one LLM stage at a time
    python diagnose.py check                      # verify numbers and method IDs in the outputs
    python diagnose.py models                     # list the models your API key can use

Common options: --papers DIR  --financials CSV  --run DIR  --model NAME  --mock  --dry
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from pipeline import check, financials, llm, pdf_extract, stages  # noqa: E402


def load_dotenv(path: Path) -> None:
    """Tiny .env reader (KEY=value per line), so no extra package is needed."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


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
    load_dotenv(ROOT / ".env")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["run", "extract", "metrics", "methods", "apply", "report", "check", "models"])
    ap.add_argument("--papers", type=Path, default=ROOT / "data/papers")
    ap.add_argument("--financials", type=Path, default=ROOT / "data/financials/harbor_lane_supply.csv")
    ap.add_argument("--run", type=Path, default=ROOT / "outputs/latest", help="folder for this run's outputs")
    ap.add_argument("--model", help="model name (default: LLM_MODEL in .env)")
    ap.add_argument("--mock", action="store_true", help="use a fake model; tests the pipeline without an API key")
    ap.add_argument("--dry", action="store_true", help="build the prompts and save them, but do not call the model")
    a = ap.parse_args()

    if a.command == "models":
        print("\n".join(llm.list_models()))
        return

    a.run.mkdir(parents=True, exist_ok=True)
    llm_steps = ["methods", "apply", "report"]
    plan = {"run": ["extract", "metrics", *llm_steps, "check"]}.get(a.command, [a.command])
    needs_model = any(s in llm_steps for s in plan) and not a.mock and not a.dry
    model = llm.model_name(a.model) if needs_model else (a.model or "MOCK" if a.mock else a.model or "-")
    print(f"Run folder: {a.run}   Model: {model}")

    for step in plan:
        print(f"\n[{step}]")
        if step == "extract":
            step_extract(a)
        elif step == "metrics":
            step_metrics(a)
        elif step in llm_steps:
            stages.run_stage(step, a.run, model, mock=a.mock, dry=a.dry)
            if a.dry and a.command == "run":
                print("  (dry run stops here: later stages need this stage's real output)")
                return
        elif step == "check":
            ok = check.run_checks(a.run)
            if a.command == "check" and not ok:
                sys.exit(1)

    report = a.run / "diagnostic_report.md"
    if a.command == "run" and report.exists():
        print(f"\nDone. Report: {report}")


if __name__ == "__main__":
    main()
