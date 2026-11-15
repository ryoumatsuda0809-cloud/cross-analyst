"""Run with:  python -m pytest -q
Everything is offline: the pipeline needs no key, no account and no network."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from pipeline import cards as cardlib, check, financials, stages  # noqa: E402

CARDS_DIR = ROOT / "data/method_cards"
CSV = ROOT / "data/financials/harbor_lane_supply.csv"

# Runs diagnose.py with every socket operation turned into an error.
NO_NETWORK = (
    "import runpy, socket, sys\n"
    "def blocked(*a, **k):\n"
    "    raise RuntimeError('network access attempted')\n"
    "socket.socket.connect = blocked\n"
    "socket.create_connection = blocked\n"
    "socket.getaddrinfo = blocked\n"
    "path = sys.argv[1]\n"
    "sys.argv = [path] + sys.argv[2:]\n"
    "runpy.run_path(path, run_name='__main__')\n"
)


def run(*args, run_dir, offline=False):
    cmd = [sys.executable, "-c", NO_NETWORK, str(ROOT / "diagnose.py")] if offline else \
          [sys.executable, str(ROOT / "diagnose.py")]
    return subprocess.run([*cmd, *args, "--run", str(run_dir)], capture_output=True, text=True, cwd=ROOT)


@pytest.fixture(scope="module")
def full_run(tmp_path_factory):
    folder = tmp_path_factory.mktemp("full")
    r = run("run", run_dir=folder)
    assert r.returncode == 0, r.stdout + r.stderr
    return folder


def snapshot(folder: Path) -> dict:
    return {str(p.relative_to(folder)): p.read_bytes() for p in sorted(folder.rglob("*")) if p.is_file()}


def parse_diagnosis(run_dir: Path) -> dict:
    return stages._parse_diagnosis((run_dir / "03_diagnosis.md").read_text(encoding="utf-8"))


# --- the whole pipeline -------------------------------------------------------------------------
def test_run_creates_every_output(full_run):
    for name in ["01_extracted/_extraction_summary.md", "03a_metrics.md", "02_methods.md",
                 "03_diagnosis.md", "diagnostic_report.md", "check_result.txt"]:
        assert (full_run / name).exists(), name
    assert (full_run / "check_result.txt").read_text().startswith("PASS")


def test_extraction_summary_lists_every_paper(full_run):
    summary = (full_run / "01_extracted/_extraction_summary.md").read_text()
    for pdf in (ROOT / "data/papers").glob("*.pdf"):
        assert pdf.name in summary


def test_run_works_without_network(tmp_path):
    r = run("run", run_dir=tmp_path, offline=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert (tmp_path / "check_result.txt").read_text().startswith("PASS")


def test_same_command_twice_gives_identical_files(tmp_path):
    first, second = tmp_path / "a", tmp_path / "b"
    assert run("run", run_dir=first).returncode == 0
    assert run("run", run_dir=second).returncode == 0
    assert snapshot(first) == snapshot(second)
    before = snapshot(first)
    assert run("run", run_dir=first).returncode == 0      # again, into the same folder
    assert snapshot(first) == before


# --- method cards -------------------------------------------------------------------------------
def test_cards_have_every_field_and_unique_ids():
    cards = cardlib.load(CARDS_DIR)
    assert len(cards) >= 2
    assert len({c["id"] for c in cards}) == len(cards)
    assert {c["paper"]["file"] for c in cards} == {p.name for p in (ROOT / "data/papers").glob("*.pdf")}


def test_card_ratio_names_match_financials_or_the_data_lacks_the_inputs():
    periods, data = financials.load(CSV)
    items = set().union(*(data[p].keys() for p in periods))
    for c in cardlib.load(CARDS_DIR):
        if c["ratio"] in financials.RATIOS or c["ratio"] in ("revenue_growth",):
            assert all(i in items for i in c["inputs"]), c["id"]
        else:
            assert c["level"] == "aggregate" or any(i not in items for i in c["inputs"]), c["id"]


def test_every_card_quotation_exists_in_the_extracted_paper_text(full_run):
    for c in cardlib.load(CARDS_DIR):
        v = cardlib.verify(c, full_run / "01_extracted")
        assert v.found, f"{c['id']}: {v.note}"
        assert v.first_line <= v.last_line and v.lines


def test_quotation_match_ignores_line_breaks_but_nothing_else(tmp_path):
    ext = tmp_path / "01_extracted"
    ext.mkdir()
    (ext / "p.methods.txt").write_text("PAPER: x\n\nA firm is flagged when the ratio is\nbelow  one in a year.\n",
                                       encoding="utf-8")
    card = {"id": "M1", "paper": {"file": "p.pdf", "title": "x"},
            "quote": "A firm is flagged when the ratio is below one in a year."}
    v = cardlib.verify(card, ext)
    assert v.found and (v.first_line, v.last_line) == (3, 4)
    assert not cardlib.verify({**card, "quote": "A firm is flagged when the ratio is above one in a year."}, ext).found


def test_methods_stage_stops_when_a_quotation_is_not_in_the_paper(full_run, tmp_path):
    cards = tmp_path / "cards"
    shutil.copytree(CARDS_DIR, cards)
    target = cards / "fed_icr_vulnerabilities_2020.json"
    data = json.loads(target.read_text())
    data[0]["quote"] = "This sentence is not in the paper."
    target.write_text(json.dumps(data))
    work = tmp_path / "run"
    shutil.copytree(full_run, work)
    r = run("methods", "--cards", str(cards), run_dir=work)
    assert r.returncode != 0 and "M1" in (r.stdout + r.stderr)
    assert "NOT FOUND" in (work / "02_methods.md").read_text()


def test_stage_without_its_input_stops_with_a_clear_message(tmp_path):
    r = run("apply", run_dir=tmp_path)
    assert r.returncode != 0 and "metrics step" in (r.stdout + r.stderr)


# --- apply: rules -------------------------------------------------------------------------------
def test_trend_verdict_and_threshold_rules():
    assert stages.classify_trend([3, 2, 1]) == "falling"
    assert stages.classify_trend([1, 2, 3]) == "rising"
    assert stages.classify_trend([2, 2, 2]) == "flat"
    assert stages.classify_trend([1, 3, 2]) == "mixed"
    assert stages.classify_trend([1]) == "insufficient"
    assert stages.verdict_for("falling", "lower_is_worse") == "worsening"
    assert stages.verdict_for("falling", "higher_is_worse") == "improving"
    assert stages.verdict_for("rising", None) == "no verdict"
    assert stages.condition_met("<", 2, 1.5) and not stages.condition_met("<", 2, 2)


def test_aggregate_and_missing_data_methods_are_not_applicable_with_a_reason(full_run):
    by_id = {m["method"].split(":")[0]: m for m in parse_diagnosis(full_run)["methods"]}
    assert by_id["M8"]["applicable?"] == "no" and "aggregate" in by_id["M8"]["reason"]
    assert by_id["M5"]["applicable?"] == "no" and "missing line item" in by_id["M5"]["reason"]
    assert by_id["M1"]["applicable?"] == "yes"


def test_diagnosis_quotes_metric_values_exactly_as_written(full_run):
    metrics = (full_run / "03a_metrics.md").read_text()
    _, _, _, ratios = financials.read_markdown(full_run / "03a_metrics.md")
    for f in parse_diagnosis(full_run)["findings"]:
        ratio = f["fields"]["Evidence"].split("`")[1]
        for period, text in ratios[ratio].items():
            assert f"{period} {text}" in f["fields"]["Evidence"]
        assert ratio in metrics


def test_threshold_is_compared_for_the_firm_level_interest_coverage_cards(full_run):
    findings = {f["id"]: f for f in parse_diagnosis(full_run)["findings"]}
    assert findings["M1"]["fields"]["Threshold status"] == "not breached"
    assert findings["M7"]["fields"]["Verdict"] == "worsening"


# --- report: built from the diagnosis ----------------------------------------------------------
def test_report_is_assembled_from_the_diagnosis_file(full_run, tmp_path):
    work = tmp_path / "run"
    shutil.copytree(full_run, work)
    diag = work / "03_diagnosis.md"
    diag.write_text(diag.read_text().replace("What explains the gap between reported profit and cash from operations",
                                             "Why is cash from operations so far below profit"), encoding="utf-8")
    assert run("report", run_dir=work).returncode == 0
    assert "Why is cash from operations so far below profit" in (work / "diagnostic_report.md").read_text()


def test_report_has_the_expected_sections(full_run):
    text = (full_run / "diagnostic_report.md").read_text()
    for heading in ["## Summary", "## Findings", "## Questions to verify with the company",
                    "## Methods used", "## Limitations"]:
        assert heading in text


# --- check --------------------------------------------------------------------------------------
def test_check_catches_invented_numbers_and_ids(full_run, tmp_path):
    work = tmp_path / "run"
    shutil.copytree(full_run, work)
    fake = work / "diagnostic_report.md"
    fake.write_text("Current ratio was 1.2447 in FY2025 (M1). Margin fell to 3.2% (M1). "
                    "Debt is 0.4242 (M9).\n")
    problems = check.check_file(fake, work)
    assert any("0.4242" in p for p in problems)
    assert any("M9" in p for p in problems)
    assert not any("1.2447" in p or "3.2%" in p for p in problems)
    assert run("check", run_dir=work).returncode == 1


def test_check_fails_instead_of_passing_when_there_is_nothing_to_check(tmp_path):
    r = run("check", run_dir=tmp_path)
    assert r.returncode == 1
    assert (tmp_path / "check_result.txt").read_text().startswith("FAIL")


def test_check_reports_problems_in_both_documents(full_run, tmp_path):
    work = tmp_path / "run"
    shutil.copytree(full_run, work)
    for name in ("03_diagnosis.md", "diagnostic_report.md"):
        (work / name).write_text("Margin was 7.7777 (M1).\n")
    r = run("check", run_dir=work)
    assert r.returncode == 1 and r.stdout.count("[FAIL]") == 2


def _variant(tmp_path, edit):
    csv_text = edit(CSV.read_text(encoding="utf-8"))
    tmp_path.mkdir(parents=True, exist_ok=True)
    path = tmp_path / "variant.csv"
    path.write_text(csv_text, encoding="utf-8")
    out = tmp_path / "out"
    r = run("run", "--financials", str(path), run_dir=out)
    assert r.returncode == 0, r.stdout + r.stderr
    assert (out / "check_result.txt").read_text().startswith("PASS")
    return (out / "03_diagnosis.md").read_text(encoding="utf-8")


def test_zero_denominator_period_is_skipped_and_flagged(tmp_path):
    text = _variant(tmp_path, lambda t: t.replace("interest_expense,40,55,80", "interest_expense,40,0,80"))
    assert "Periods without a usable value:** FY2024" in text and "the comparison skips it" in text


def test_missing_line_item_is_named_in_the_reason(tmp_path):
    text = _variant(tmp_path, lambda t: "\n".join(l for l in t.splitlines() if not l.startswith("taxes,")))
    assert "free_cash_flow_to_assets is n/a in every period; missing line item(s): taxes" in text


def test_single_period_gives_low_confidence_and_a_threshold_breach_is_reported(tmp_path):
    text = _variant(tmp_path, lambda t: "\n".join(",".join(l.split(",")[:2]) if "," in l and not l.startswith("#") else l
                                                   for l in t.splitlines()))
    assert "fewer than two periods have a usable value" in text
    text = _variant(tmp_path / "b", lambda t: t.replace("ebit,290,310,300", "ebit,100,150,60")
                    .replace("interest_expense,40,55,80", "interest_expense,200,100,120"))
    assert "breached in FY2023, FY2025" in text and "Verdict:** mixed" in text


# --- arithmetic and input guards ----------------------------------------------------------------
def test_ratio_over_a_negative_or_zero_denominator_is_not_reported_as_a_number():
    items = {"net_income": -50, "equity": -200, "operating_cash_flow": 30, "ebit": 100, "interest_expense": 0}
    r = financials.compute(["FY2025"], {"FY2025": items})
    assert r["roe"]["FY2025"] == "n/a (negative equity)"                    # -50 / -200 must not read as +25%
    assert r["ocf_to_net_income"]["FY2025"] == "n/a (negative net_income)"
    assert r["ebit_interest_coverage"]["FY2025"] == "n/a (division by zero)"
    r = financials.compute(["FY2025"], {"FY2025": {"ebit": -100, "interest_expense": 40}})
    assert r["ebit_interest_coverage"]["FY2025"] == -2.5                    # a negative numerator is still meaningful


def _load_text(tmp_path, text):
    path = tmp_path / "f.csv"
    path.write_text(text, encoding="utf-8")
    return financials.load(path)


def test_financial_data_with_reversed_periods_or_bad_cells_is_refused(tmp_path):
    with pytest.raises(SystemExit, match="oldest to newest"):
        _load_text(tmp_path, "item,FY2025,FY2024,FY2023\nrevenue,3,2,1\n")
    with pytest.raises(SystemExit, match="not a number"):
        _load_text(tmp_path, "item,FY2024,FY2025\nrevenue,100,(60)\n")
    with pytest.raises(SystemExit, match="not a number"):
        _load_text(tmp_path, "item,FY2024,FY2025\nrevenue,100,nan\n")
    with pytest.raises(SystemExit, match="more than once"):
        _load_text(tmp_path, "item,FY2024,FY2025\nrevenue,1,2\nrevenue,3,4\n")
    with pytest.raises(SystemExit, match="not found"):
        financials.load(tmp_path / "nothing.csv")
    periods, data = _load_text(tmp_path, "item,Q4 2024,Q1 2025\nrevenue,\"1,200\",-5\n")
    assert periods == ["Q4 2024", "Q1 2025"] and data["Q4 2024"]["revenue"] == 1200


def test_quotation_must_match_whole_words_and_whole_numbers(tmp_path):
    ext = tmp_path / "01_extracted"
    ext.mkdir()
    (ext / "p.methods.txt").write_text("firms with ICRs below 2.5 are flagged, and so are firms below 20.\n"
                                       "Later: firms with ICRs below 2, or below 2.\n", encoding="utf-8")
    card = {"id": "M1", "paper": {"file": "p.pdf", "title": "x"}, "quote": "ICRs below 2"}
    v = cardlib.verify(card, ext)
    assert v.found and v.first_line == 2                                    # not the "below 2.5" on line 1
    (ext / "p.methods.txt").write_text("firms with ICRs below 2.5 or below 20\n", encoding="utf-8")
    assert not cardlib.verify(card, ext).found


def test_card_whose_inputs_differ_from_the_code_stops_the_run(full_run, tmp_path):
    for c in cardlib.load(CARDS_DIR):
        if c["ratio"] in financials.RATIOS:
            assert sorted(c["inputs"]) == financials.inputs_of(c["ratio"]), c["id"]
    cards = tmp_path / "cards"
    shutil.copytree(CARDS_DIR, cards)
    target = cards / "fed_icr_vulnerabilities_2020.json"
    data = json.loads(target.read_text())
    data[0]["inputs"] = ["operating_income", "interest_expense"]           # M1 says EBIT in the paper and the code
    target.write_text(json.dumps(data))
    work = tmp_path / "run"
    shutil.copytree(full_run, work)
    r = run("methods", "--cards", str(cards), run_dir=work)
    assert r.returncode != 0 and "does not match the code" in (r.stdout + r.stderr)


def test_check_does_not_accept_line_numbers_or_rescaled_values():
    methods = ("| M7 | p.pdf | 01_extracted/p.methods.txt | 204-204 | FOUND |\n"
               "- **Threshold:** `x` < 30\n- **Quotation:**\n  > about 69 percent of debt\n"
               "- **Verification:** FOUND in `p`, lines 204-204\n  ```text\n  only 47 firms\n  ```\n")
    allowed = check.allowed_values("| dso_days | 0.2500 |", check.card_text(methods))
    assert check.matches("30", allowed) and check.matches("25%", allowed) and check.matches("0.25", allowed)
    for invented in ("204", "69", "47", "91", "91.25", "25"):              # 91.25 = 0.25 * 365, 25 = 0.25 * 100
        assert not check.matches(invented, allowed), invented


def test_report_summary_orders_method_ids_as_numbers(tmp_path):
    names = [f"M{i}" for i in (10, 2, 1)]
    diag = ["# Diagnosis: X", "", "## Applicability", "", "| method | paper | applicable? | reason |", "|---|---|---|---|"]
    diag += [f"| {n}: n | p.pdf | yes | ok |" for n in names] + ["", "## Findings", ""]
    for n in names:
        diag += [f"### {n}: n", "- **Threshold status:** none stated", "- **Verdict:** worsening", ""]
    diag += ["## Where methods disagree", "", "x", "", "## What the data cannot tell us", "", "- q"]
    (tmp_path / "03_diagnosis.md").write_text("\n".join(diag) + "\n", encoding="utf-8")
    stages.run_report(tmp_path)
    summary = (tmp_path / "diagnostic_report.md").read_text().split("## Findings")[0]
    assert summary.index("**M1**") < summary.index("**M2**") < summary.index("**M10**")


def test_common_line_item_names_are_mapped_to_the_pipeline_names(tmp_path):
    text = ("item,FY2024,FY2025\nNet Sales,100,120\nCost of Goods Sold,60,70\nOperating Profit,20,25\n"
            "Interest Expense,5,5\n売上高メモ,1,2\n")
    periods, data = _load_text(tmp_path, text)
    assert data["FY2025"]["revenue"] == 120 and data["FY2025"]["cost_of_sales"] == 70
    assert data["FY2025"]["operating_income"] == 25 and data["FY2025"]["interest_expense"] == 5
    assert data["FY2025"]["売上高メモ"] == 2                       # unknown names are kept, not guessed
    ratios = financials.compute(periods, data)
    assert ratios["operating_margin"]["FY2025"] == pytest.approx(25 / 120)


def test_two_rows_with_the_same_meaning_are_refused(tmp_path):
    with pytest.raises(SystemExit, match="more than once"):
        _load_text(tmp_path, "item,FY2024,FY2025\nrevenue,100,120\nNet Sales,100,120\n")


def test_committed_example_outputs_match_a_fresh_run(full_run):
    """examples/harbor_lane/ is what a reader sees on GitHub; it must be what the code produces today.
    If this fails after a deliberate change, regenerate the folder (see README, 'Example output')."""
    example = ROOT / "examples" / "harbor_lane"
    names = ["diagnostic_report.md", "03_diagnosis.md", "03a_metrics.md", "02_methods.md", "check_result.txt"]
    for name in names:
        assert (example / name).read_text(encoding="utf-8") == (full_run / name).read_text(encoding="utf-8"), name
