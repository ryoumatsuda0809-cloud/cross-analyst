"""The three rule-based stages that sit between the extracted papers and the final report.

    methods  data/method_cards/*.json + 01_extracted/*.methods.txt  ->  02_methods.md
    apply    method cards + 03a_metrics.md                          ->  03_diagnosis.md
    report   03_diagnosis.md                                        ->  diagnostic_report.md

Nothing here uses the network and nothing is computed: every figure is copied, exactly as
written, from 03a_metrics.md. Judgements are comparisons only (is a value below a threshold,
did a series rise or fall), so the same inputs always give byte-identical outputs.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from . import cards as cardlib
from . import financials

EXTRACTED = "01_extracted"

DIRECTION_TEXT = {"lower_is_worse": "lower is worse", "higher_is_worse": "higher is worse", None: "not stated in the paper"}
BASIS_TEXT = {"paper": "stated in the paper", "inferred": "inferred from the paper, not stated", "not_stated": "not stated"}
TREND_TEXT = {"rising": "rose in every period", "falling": "fell in every period",
              "flat": "did not change", "mixed": "moved up and down",
              "insufficient": "has fewer than two usable periods"}


# ---------------------------------------------------------------------------
# methods: method cards -> 02_methods.md
# ---------------------------------------------------------------------------
def run_methods(run: Path, cards_dir: Path) -> Path:
    cards = cardlib.load(cards_dir)
    extracted = run / EXTRACTED
    if not extracted.is_dir():
        raise SystemExit(f"{extracted} does not exist. Run the extract step first.")
    results = [cardlib.verify(c, extracted) for c in cards]
    out = run / "02_methods.md"
    out.write_text(_methods_markdown(cards, results, extracted, sorted(p.name for p in cards_dir.glob("*.json"))),
                   encoding="utf-8")
    failed = [r for r in results if not r.found]
    for c, r in zip(cards, results):
        where = f"{r.checked_file} lines {r.first_line}-{r.last_line}" if r.found else r.note
        print(f"  {c['id']}: {'FOUND' if r.found else 'NOT FOUND'} ({where})")
    print(f"  {len(cards)} card(s), {len(cards) - len(failed)} verified -> {out.name}")
    if failed:
        raise SystemExit("Quotation not found for card(s): " + ", ".join(r.card_id for r in failed)
                         + ". Fix the card or the paper text, then run the methods step again.")
    return out


def _threshold_text(card: dict) -> str:
    th = card["threshold"]
    return "None stated in the paper." if th is None else f"`{card['ratio']}` {th['operator']} {th['value']}"


def _methods_markdown(cards, results, extracted: Path, card_files: list[str]) -> str:
    covered = {Path(c["paper"]["file"]).stem for c in cards}
    uncovered = sorted(p.name.removesuffix(".methods.txt") for p in extracted.glob("*.methods.txt")
                       if p.name.removesuffix(".methods.txt") not in covered)
    lines = ["# Method cards", "",
             f"Cards read from: {', '.join(card_files)}. Each quotation was searched for in the paper's extracted "
             "method text (line breaks and repeated spaces ignored, nothing else).", "",
             "## Verification summary", "",
             "| card | paper file | checked against | lines | result |", "|---|---|---|---|---|"]
    for c, r in zip(cards, results):
        span = f"{r.first_line}-{r.last_line}" if r.found else "-"
        lines.append(f"| {c['id']} | {c['paper']['file']} | {r.checked_file} | {span} | "
                     f"{'FOUND' if r.found else 'NOT FOUND'} |")
    if uncovered:
        lines += ["", "Papers with no card: " + ", ".join(uncovered) + "."]
    for c, r in zip(cards, results):
        lines += ["", f"## {c['id']}: {c['name']}", "",
                  f"- **Source:** {c['paper']['file']} (\"{c['paper']['title']}\")",
                  f"- **Level:** {c['level']}",
                  f"- **What it diagnoses:** {c['diagnoses']}",
                  f"- **Ratio used:** `{c['ratio']}`",
                  f"- **Inputs required:** {', '.join(c['inputs'])}",
                  f"- **Formula:** `{c['formula']}`",
                  f"- **Threshold:** {_threshold_text(c)}",
                  f"- **Bad direction:** {DIRECTION_TEXT[c['bad_direction']]} (basis: {BASIS_TEXT[c['direction_basis']]})"]
        if c.get("notes"):
            lines.append(f"- **Notes:** {c['notes']}")
        lines += ["- **Quotation:**", f"  > {c['quote']}"]
        if r.found:
            lines += [f"- **Verification:** FOUND in `{r.checked_file}`, lines {r.first_line}-{r.last_line}",
                      "- **Matching lines:**", "  ```text"] + [f"  {ln}" for ln in r.lines] + ["  ```"]
        else:
            lines.append(f"- **Verification:** NOT FOUND in `{r.checked_file}` ({r.note}). This card must not be used.")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# apply: cards + 03a_metrics.md -> 03_diagnosis.md
# ---------------------------------------------------------------------------
@dataclass
class Assessment:
    card: dict
    applicable: bool
    reasons: list[str]
    series: list = field(default_factory=list)      # [(period, text as written in 03a, float)] usable periods only
    unusable: list = field(default_factory=list)    # periods where the ratio is n/a
    trend: str = ""
    verdict: str = ""
    breached: list = field(default_factory=list)    # periods where the threshold condition is met
    confidence: str = ""
    confidence_why: str = ""


def classify_trend(values: list[float]) -> str:
    """Comparison only: rising / falling / flat / mixed, from consecutive pairs."""
    if len(values) < 2:
        return "insufficient"
    pairs = list(zip(values, values[1:]))
    if all(b > a for a, b in pairs):
        return "rising"
    if all(b < a for a, b in pairs):
        return "falling"
    if all(b == a for a, b in pairs):
        return "flat"
    return "mixed"


def verdict_for(trend: str, direction) -> str:
    if direction is None or trend == "insufficient":
        return "no verdict"
    if trend in ("mixed", "flat"):
        return "mixed" if trend == "mixed" else "unchanged"
    return "worsening" if (trend == "falling") == (direction == "lower_is_worse") else "improving"


def condition_met(operator: str, value: float, x: float) -> bool:
    return {"<": x < value, "<=": x <= value, ">": x > value, ">=": x >= value}[operator]


def assess(card: dict, verification: cardlib.Verification, periods, raw, ratios) -> Assessment:
    reasons = []
    if not verification.found:
        reasons.append("the card's quotation was not found in the paper text")
    if card["level"] == "aggregate":
        reasons.append("aggregate-level method: it needs many firms or sector data, and this data is one company")
    missing = [i for i in card["inputs"] if i not in raw]
    if card["ratio"] not in ratios:
        if missing:
            reasons.append("missing line item(s): " + ", ".join(missing))
        else:
            reasons.append(f"ratio {card['ratio']} is not in 03a_metrics.md")
    if reasons:
        return Assessment(card, False, reasons)

    cells = [(p, ratios[card["ratio"]].get(p, "n/a")) for p in periods]
    series = [(p, s, financials.to_float(s)) for p, s in cells if financials.to_float(s) is not None]
    unusable = [p for p, s in cells if financials.to_float(s) is None]
    if not series:
        why = f"{card['ratio']} is n/a in every period"
        return Assessment(card, False, [why + ("; missing line item(s): " + ", ".join(missing) if missing else "")])

    a = Assessment(card, True, ["all inputs available"], series, unusable)
    a.trend = classify_trend([v for _, _, v in series])
    a.verdict = verdict_for(a.trend, card["bad_direction"])
    th = card["threshold"]
    if th:
        a.breached = [p for p, _, v in series if condition_met(th["operator"], th["value"], v)]
    if a.trend == "insufficient":
        a.confidence, a.confidence_why = "low", "fewer than two periods have a usable value"
    elif unusable:
        a.confidence, a.confidence_why = "low", "the ratio is n/a in at least one period, so the comparison skips it"
    elif th:
        a.confidence, a.confidence_why = "high", "the paper states a threshold and the ratio is available in every period"
    else:
        a.confidence, a.confidence_why = "medium", "the paper states no threshold, so only the direction of change is judged"
    return a


def _quote_series(series) -> str:
    return "; ".join(f"{p} {s}" for p, s, _ in series)


def _first_last(series) -> str:
    (p1, s1, _), (pn, sn, _) = series[0], series[-1]
    return f"from {s1} ({p1}) to {sn} ({pn})"


def _finding(a: Assessment) -> list[str]:
    c = a.card
    th = c["threshold"]
    lines = [f"### {c['id']}: {c['name']}",
             f"- **What it measures:** {c['diagnoses']}",
             f"- **Evidence:** `{c['ratio']}`, from 03a_metrics.md: {_quote_series(a.series)}"]
    if th:
        word = {"<": "below", "<=": "at or below", ">": "above", ">=": "at or above"}[th["operator"]]
        per_period = "; ".join(f"{p} {s}: {'yes' if p in a.breached else 'no'}" for p, s, _ in a.series)
        lines += [f"- **Threshold used:** `{c['ratio']}` {th['operator']} {th['value']} (quoted from the paper on the {c['id']} card)",
                  f"- **Against the threshold ({word} {th['value']}?):** {per_period}",
                  "- **Threshold status:** " + (("breached in " + ", ".join(a.breached)) if a.breached else "not breached")]
    else:
        lines += ["- **Threshold used:** none stated", "- **Threshold status:** none stated"]
    if a.unusable:
        lines.append(f"- **Periods without a usable value:** {', '.join(a.unusable)} (n/a in 03a_metrics.md)")
    lines += [f"- **Trend over {len(a.series)} period(s):** the ratio {TREND_TEXT[a.trend]}",
              f"- **Direction of this method:** {DIRECTION_TEXT[c['bad_direction']]} (basis: {BASIS_TEXT[c['direction_basis']]})",
              f"- **Verdict:** {a.verdict}"]
    if a.series and a.trend not in ("insufficient",):
        result = f"The ratio moved {_first_last(a.series)} and {TREND_TEXT[a.trend]}."
    else:
        result = "The ratio cannot show a trend."
    if a.verdict == "worsening":
        result += f" Under this method that is the worse direction, which indicates a weakening in: {c['diagnoses']}."
    elif a.verdict == "improving":
        result += f" Under this method that is the better direction, which is consistent with an improvement in: {c['diagnoses']}."
    elif a.verdict == "no verdict":
        result += " The paper gives no direction for this measure, so no verdict is drawn."
    if th:
        result += (" It met the threshold condition in " + ", ".join(a.breached) + "." if a.breached
                   else " It did not meet the threshold condition in any period.")
    lines += [f"- **Result:** {result}", f"- **Confidence:** {a.confidence}, because {a.confidence_why}.", ""]
    return lines


def _agreement(applied: list[Assessment]) -> str:
    judged = [a for a in applied if a.verdict in ("worsening", "improving", "mixed", "unchanged")]
    if len(judged) < 2:
        return "Fewer than two applicable methods give a verdict, so there is nothing to compare."
    groups: dict[str, list[str]] = {}
    for a in judged:
        groups.setdefault(a.verdict, []).append(a.card["id"])
    if len(groups) == 1:
        verdict, ids = next(iter(groups.items()))
        return f"All applicable methods ({', '.join(ids)}) point the same way: {verdict}."
    parts = [f"{', '.join(ids)}: {verdict}" for verdict, ids in groups.items()]
    return "The applicable methods do not all point the same way (" + "; ".join(parts) + "). No attempt is made to decide which is right."


def _series_for(table, key, periods):
    row = table.get(key)
    if not row:
        return None
    cells = [(p, row.get(p, "n/a")) for p in periods]
    if any(financials.to_float(s) is None for _, s in cells):
        return None
    return [(p, s, financials.to_float(s)) for p, s in cells]


def _trend(series) -> str:
    return classify_trend([v for _, _, v in series]) if series else ""


def _questions(periods, raw, ratios, assessments) -> list[str]:
    """Questions the numbers raise but cannot answer. Each rule is a comparison on 03a values."""
    qs = []
    ocf, ni = _series_for(raw, "operating_cash_flow", periods), _series_for(raw, "net_income", periods)
    if ocf and ni and _trend(ocf) == "falling" and all(v > 0 for _, _, v in ni):
        qs.append(f"operating_cash_flow fell every period ({_quote_series(ocf)}) while net_income stayed positive "
                  f"({_quote_series(ni)}). What explains the gap between reported profit and cash from operations "
                  "(for example slower customer payments, inventory purchases, or one-off items)?")
    rec, dso = _series_for(raw, "receivables", periods), _series_for(ratios, "dso_days", periods)
    if rec and _trend(rec) == "rising":
        extra = f", and dso_days also rose ({_quote_series(dso)})" if dso and _trend(dso) == "rising" else ""
        qs.append(f"receivables rose every period ({_quote_series(rec)}){extra}. Did customer payment terms change, "
                  "is a small number of customers behind the increase, or are collections slower?")
    inv, dio = _series_for(raw, "inventory", periods), _series_for(ratios, "dio_days", periods)
    if inv and _trend(inv) == "rising":
        extra = f", and dio_days also rose ({_quote_series(dio)})" if dio and _trend(dio) == "rising" else ""
        qs.append(f"inventory rose every period ({_quote_series(inv)}){extra}. Was the build-up planned, "
                  "and is any of the stock slow-moving?")
    capex, fcf = _series_for(raw, "capital_expenditures", periods), _series_for(ratios, "free_cash_flow", periods)
    if capex and _trend(capex) == "rising" and (not fcf or _trend(fcf) == "falling"):
        extra = f" while free_cash_flow fell ({_quote_series(fcf)})" if fcf else ""
        qs.append(f"capital_expenditures rose every period ({_quote_series(capex)}){extra}. "
                  "What was the money spent on, and how was it funded?")
    lines = _series_for(raw, "undrawn_credit_lines", periods)
    if lines and _trend(lines) == "falling":
        qs.append(f"undrawn_credit_lines fell every period ({_quote_series(lines)}). Were credit lines drawn, reduced "
                  "or cancelled, and what are their terms, maturity dates and renewal plans?")
    debt, interest = _series_for(raw, "total_debt", periods), _series_for(raw, "interest_expense", periods)
    if debt and interest and _trend(debt) == "rising" and _trend(interest) == "rising":
        qs.append(f"total_debt ({_quote_series(debt)}) and interest_expense ({_quote_series(interest)}) both rose "
                  "every period. Which part of the debt carries a floating rate, and when do fixed rates reset?")
    for a in assessments:
        c = a.card
        if a.applicable:
            continue
        missing = [i for i in c["inputs"] if i not in raw]
        if c["level"] == "firm" and missing:
            qs.append(f"{c['id']}: {c['name']} could not be applied because the data has no {', '.join(missing)}. "
                      f"Can the company supply it for {periods[0]} to {periods[-1]}?")
        elif c["level"] == "aggregate":
            qs.append(f"{c['id']}: {c['name']} is a sector-wide method. Is comparable sector or peer data "
                      "available to put this company's figures in context?")
    return qs


def run_apply(run: Path, cards_dir: Path) -> Path:
    cards = cardlib.load(cards_dir)
    metrics = run / "03a_metrics.md"
    if not metrics.exists():
        raise SystemExit(f"{metrics} does not exist. Run the metrics step first.")
    if not (run / "02_methods.md").exists():
        raise SystemExit(f"{run / '02_methods.md'} does not exist. Run the methods step first.")
    company, periods, raw, ratios = financials.read_markdown(metrics)
    assessments = [assess(c, cardlib.verify(c, run / EXTRACTED), periods, raw, ratios) for c in cards]
    applied = [a for a in assessments if a.applicable]

    lines = [f"# Diagnosis: {company}", "",
             "Every figure below is copied from 03a_metrics.md. No figure is computed in this step.", "",
             "## Applicability", "",
             "| method | level | paper | ratio | inputs required | available in 03a? | applicable? | reason |",
             "|---|---|---|---|---|---|---|---|"]
    for a in assessments:
        c = a.card
        lines.append(f"| {c['id']}: {c['name']} | {c['level']} | {c['paper']['file']} | {c['ratio']} | {', '.join(c['inputs'])} | "
                     f"{'yes' if c['ratio'] in ratios else 'no'} | {'yes' if a.applicable else 'no'} | "
                     f"{'; '.join(a.reasons)} |")
    lines += ["", "## Findings", ""]
    if applied:
        for a in applied:
            lines += _finding(a)
    else:
        lines += ["No method could be applied to this data.", ""]
    lines += ["## Where methods disagree", "", _agreement(applied), "",
              "## What the data cannot tell us", ""]
    questions = _questions(periods, raw, ratios, assessments)
    lines += [f"- {q}" for q in questions] or ["- No open question was raised by the rules."]
    out = run / "03_diagnosis.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  {len(applied)} of {len(assessments)} method(s) applicable, {len(questions)} open question(s) -> {out.name}")
    return out


# ---------------------------------------------------------------------------
# report: 03_diagnosis.md -> diagnostic_report.md
# ---------------------------------------------------------------------------
def _parse_diagnosis(text: str) -> dict:
    title = next((ln for ln in text.splitlines() if ln.startswith("# Diagnosis:")), "# Diagnosis:")
    sections: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    for needed in ("Applicability", "Findings", "Where methods disagree", "What the data cannot tell us"):
        if needed not in sections:
            raise SystemExit(f"03_diagnosis.md has no '{needed}' section. Run the apply step again.")

    table = [ln for ln in sections["Applicability"] if ln.startswith("|")]
    header = [c.strip() for c in table[0].strip("|").split("|")]
    methods = [dict(zip(header, [c.strip() for c in row.strip("|").split("|")])) for row in table[2:]]

    findings, current_f = [], None
    for line in sections["Findings"]:
        m = re.match(r"### (M\d+): (.*)", line)
        if m:
            current_f = {"id": m.group(1), "name": m.group(2), "fields": {}}
            findings.append(current_f)
        elif current_f is not None:
            b = re.match(r"- \*\*(.+?):\*\* (.*)", line)
            if b:
                current_f["fields"][b.group(1)] = b.group(2)
    return {
        "company": title.split(":", 1)[1].strip(),
        "methods": methods,
        "findings": findings,
        "agreement": " ".join(ln for ln in sections["Where methods disagree"] if ln.strip()),
        "questions": [ln[2:] for ln in sections["What the data cannot tell us"] if ln.startswith("- ")],
    }


def _field(finding: dict, prefix: str) -> str:
    return next((v for k, v in finding["fields"].items() if k.startswith(prefix)), "")


def run_report(run: Path) -> Path:
    src = run / "03_diagnosis.md"
    if not src.exists():
        raise SystemExit(f"{src} does not exist. Run the apply step first.")
    d = _parse_diagnosis(src.read_text(encoding="utf-8"))
    findings = d["findings"]

    def priority(f):
        return (0 if _field(f, "Threshold status").startswith("breached") else 1,
                0 if _field(f, "Verdict") == "worsening" else 1, f["id"])

    lines = [f"# Financial Diagnostic Report: {d['company']}", "", "## Summary", ""]
    if findings:
        lines += [d["agreement"], ""]
        for f in sorted(findings, key=priority)[:5]:
            status = _field(f, "Threshold status")
            lines.append(f"- **{f['id']}** {f['name']}: {_field(f, 'Trend')}; "
                         f"{_field(f, 'Direction').split(' (')[0]} under this method, so the verdict is "
                         f"{_field(f, 'Verdict')}. Threshold: {status}. Confidence: {_field(f, 'Confidence').split(',')[0]}.")
        if len(findings) > 5:
            lines.append(f"- {len(findings) - 5} further finding(s) are listed under Findings.")
    else:
        lines.append("No method could be applied to this data, so there are no findings.")

    lines += ["", "## Findings", ""]
    for f in findings:
        lines += [f"### {f['id']}: {f['name']}", "",
                  f"- **What it means:** {_field(f, 'What it measures')}",
                  f"- **Evidence:** {_field(f, 'Evidence')}",
                  f"- **Reading:** {_field(f, 'Result')}",
                  f"- **Method and confidence:** {f['id']}; {_field(f, 'Confidence')}", ""]
    lines += ["### Do the methods agree?", "", d["agreement"], "",
              "## Questions to verify with the company", ""]
    lines += [f"{i}. {q}" for i, q in enumerate(d["questions"], 1)] or ["No open question was raised."]

    lines += ["", "## Methods used", "", "| method | source paper | status | reason |", "|---|---|---|---|"]
    for m in d["methods"]:
        lines.append(f"| {m['method']} | {m['paper']} | {'applied' if m['applicable?'] == 'yes' else 'not applicable'} | "
                     f"{m['reason'] if m['applicable?'] != 'yes' else '-'} |")
    lines += ["", "## Limitations", ""]
    stated = [f["id"] for f in findings if _field(f, "Threshold used").startswith("`")]
    not_applied = [m["method"].split(":")[0] for m in d["methods"] if m["applicable?"] != "yes"]
    lines += [
        "- Every statement is a hypothesis from fixed rules applied to a few annual periods of year-end figures. "
        "None of it explains causes; the questions above are the way to find them.",
        ("- A threshold was used only where a paper states one (" + ", ".join(stated) + "). "
         "For every other method only the direction of change is reported.") if stated else
        "- No method here has a threshold stated in its paper, so only directions of change are reported.",
        "- Thresholds come from the papers' own samples and may not suit this company.",
        ("- Methods not applied: " + ", ".join(not_applied) + ". See the reasons in the Methods used table.") if not_applied else
        "- Every method card could be applied.",
        "- All numbers are copied from 03a_metrics.md. No new calculation was made when writing this report.",
    ]
    out = run / "diagnostic_report.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  {len(findings)} finding(s) -> {out.name}")
    return out
