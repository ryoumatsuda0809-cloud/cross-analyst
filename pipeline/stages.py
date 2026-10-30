"""The LLM stages, and exactly what each one is allowed to see.

This table is the core of the design. A stage receives only the files listed
under "inputs". The model cannot open anything else, because it has no tools:
this program reads the files and pastes them into the prompt.

"forbidden" is a second, explicit guard. Example: the methods stage must not
see the financial data. If it did, the model could pick or bend methods to
fit the numbers it already saw, and the diagnosis would no longer be an
independent test of the data. (The same idea as keeping a hypothesis sealed
until the field evidence is in.)
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from . import llm

PROMPTS = Path(__file__).parent / "prompts"
OUT_BEGIN, OUT_END = "<<<OUTPUT START>>>", "<<<OUTPUT END>>>"

STAGES = {
    "methods": {
        "prompt": "methods.md",
        "inputs": ["01_extracted/*.methods.txt"],
        "forbidden": ["03a_metrics.md", "*.csv"],
        "output": "02_methods.md",
    },
    "apply": {
        "prompt": "apply.md",
        "inputs": ["02_methods.md", "03a_metrics.md"],
        "forbidden": ["01_extracted/*"],          # only the method cards, so every step is traceable
        "output": "03_diagnosis.md",
    },
    "report": {
        "prompt": "report.md",
        "inputs": ["02_methods.md", "03a_metrics.md", "03_diagnosis.md"],
        "forbidden": ["01_extracted/*"],
        "output": "diagnostic_report.md",
    },
}


def _files(run: Path, patterns: list[str]) -> list[Path]:
    found = []
    for pat in patterns:
        found += sorted(run.glob(pat))
    return found


def gather(stage: str, run: Path) -> list[Path]:
    st = STAGES[stage]
    files = _files(run, st["inputs"])
    if not files:
        raise SystemExit(f"Stage '{stage}' has no input yet: {st['inputs']} in {run}. Run the earlier step first.")
    banned = set(_files(run, st["forbidden"]))
    leaked = [f for f in files if f in banned]
    if leaked:   # can only happen if someone edits the table above
        raise SystemExit(f"Stage '{stage}' would receive forbidden files: {leaked}. Stopping.")
    return files


def build_prompt(stage: str, run: Path) -> tuple[str, list[Path]]:
    st = STAGES[stage]
    files = gather(stage, run)
    template = (PROMPTS / st["prompt"]).read_text(encoding="utf-8")
    head = (
        "HOW THIS RUN WORKS (from the program)\n"
        "You have no tools: you cannot open files, browse, or run code. Everything you may use is attached "
        "at the end of this message as [ATTACHMENT] blocks. If something is not attached, you do not have it; "
        "say so instead of guessing.\n"
        f"Write the full content of {st['output']} between a line containing only {OUT_BEGIN} and a line "
        f"containing only {OUT_END}. After {OUT_END}, add a short note on anything you could not do.\n\n"
    )
    att = "".join(f"\n\n[ATTACHMENT] {f.relative_to(run)}\n`````\n{f.read_text(encoding='utf-8')}\n`````"
                  for f in files)
    return head + template + att, files


def run_stage(stage: str, run: Path, model: str, mock: bool = False, dry: bool = False) -> Path | None:
    st = STAGES[stage]
    prompt, files = build_prompt(stage, run)
    record = {
        "stage": stage,
        "time_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": "MOCK" if mock else model,
        "prompt_template": f"pipeline/prompts/{st['prompt']}",
        "inputs": [{"file": str(f.relative_to(run)),
                    "sha256": hashlib.sha256(f.read_bytes()).hexdigest()} for f in files],
        "prompt_chars": len(prompt),
    }
    if dry:
        (run / f"_prompt_{stage}.txt").write_text(prompt, encoding="utf-8")
        print(f"  [dry] {stage}: {len(files)} file(s), {len(prompt):,} chars -> _prompt_{stage}.txt (no LLM call)")
        return None

    res = mock_response(stage, files) if mock else llm.call(prompt, model)
    record.update({k: res.get(k) for k in ("input_tokens", "output_tokens", "seconds")})

    m = re.search(rf"^{re.escape(OUT_BEGIN)}\s*\n(.*?)\n{re.escape(OUT_END)}\s*$", res["text"], re.S | re.M)
    if not m:
        raw = run / f"_raw_{stage}.md"
        raw.write_text(res["text"], encoding="utf-8")
        _log(run, record | {"error": "output markers missing"})
        raise SystemExit(f"Stage '{stage}': the model did not use the output markers. Raw answer saved to {raw.name}")
    out = run / st["output"]
    out.write_text(m.group(1).strip() + "\n", encoding="utf-8")
    note = res["text"][m.end():].strip()
    if note:
        (run / f"_note_{stage}.md").write_text(note + "\n", encoding="utf-8")
    record["output"] = {"file": st["output"], "sha256": hashlib.sha256(out.read_bytes()).hexdigest()}
    _log(run, record)
    print(f"  {stage}: -> {st['output']}  ({record.get('seconds')}s, "
          f"in {record.get('input_tokens')} / out {record.get('output_tokens')} tokens)")
    return out


def _log(run: Path, record: dict) -> None:
    path = run / "run_record.json"
    log = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    log.append(record)
    path.write_text(json.dumps(log, indent=1, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# --mock: a fake model, so the pipeline can be tested without an API key.
# It never invents numbers, so check.py should pass on a mock run.
# ---------------------------------------------------------------------------
def mock_response(stage: str, files: list[Path]) -> dict:
    if stage == "methods":
        cards = []
        for i, f in enumerate(files, 1):
            title = f.read_text(encoding="utf-8").splitlines()[0].removeprefix("PAPER: ").strip()
            cards.append(f"## M{i}: (mock) method from \"{title}\"\n\n- Source: {f.name}\n"
                         "- Inputs required: (mock)\n- Procedure: (mock)\n- Interpretation: (mock)\n")
        body = "# Method cards (MOCK)\n\n" + "\n".join(cards)
    elif stage == "apply":
        body = ("# Diagnosis (MOCK)\n\n| method | finding | evidence | confidence |\n|---|---|---|---|\n"
                "| M1 | (mock finding) | see 03a_metrics.md | low |\n")
    else:
        body = ("# Diagnostic report (MOCK)\n\nThis report was produced by the mock model. "
                "It only proves that the pipeline runs end to end.\n\n## Findings\n\n- M1: (mock)\n")
    text = f"{OUT_BEGIN}\n{body}\n{OUT_END}\nMock run: nothing to report."
    return {"text": text, "input_tokens": 0, "output_tokens": 0, "seconds": 0.0}
