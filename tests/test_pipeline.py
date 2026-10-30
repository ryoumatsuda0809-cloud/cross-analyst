"""Run with:  python -m pytest -q
No API key needed: every test uses the mock model or no model at all."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from pipeline import check, stages  # noqa: E402


def run(*args, run_dir):
    return subprocess.run([sys.executable, str(ROOT / "diagnose.py"), *args, "--run", str(run_dir)],
                          capture_output=True, text=True, cwd=ROOT)


@pytest.fixture
def mock_run(tmp_path):
    r = run("run", "--mock", run_dir=tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    return tmp_path


def test_mock_run_creates_every_output(mock_run):
    for name in ["01_extracted/_extraction_summary.md", "03a_metrics.md", "02_methods.md",
                 "03_diagnosis.md", "diagnostic_report.md", "run_record.json", "check_result.txt"]:
        assert (mock_run / name).exists(), name
    assert (mock_run / "check_result.txt").read_text().startswith("PASS")


def test_both_sample_papers_have_a_method_section(mock_run):
    summary = (mock_run / "01_extracted/_extraction_summary.md").read_text()
    assert "FALLBACK" not in summary


def test_methods_stage_never_sees_financial_data(mock_run):
    prompt, files = stages.build_prompt("methods", mock_run)
    assert all(f.name.endswith(".methods.txt") for f in files)
    assert "Harbor Lane" not in prompt and "operating_cash_flow,240" not in prompt and "4,200" not in prompt


def test_apply_stage_gets_method_cards_not_raw_papers(mock_run):
    _, files = stages.build_prompt("apply", mock_run)
    assert sorted(f.name for f in files) == ["02_methods.md", "03a_metrics.md"]


def test_check_catches_invented_numbers_and_ids(mock_run):
    fake = mock_run / "diagnostic_report.md"
    fake.write_text("Current ratio was 1.2447 in FY2025 (M1). Margin fell to 3.2% (M1). "
                    "Debt is 0.4242 (M9).\n")
    problems = check.check_file(fake, mock_run)
    assert any("0.4242" in p for p in problems)
    assert any("M9" in p for p in problems)
    assert not any("1.2447" in p or "3.2%" in p for p in problems)


def test_dry_run_calls_no_model(tmp_path):
    run("extract", run_dir=tmp_path)
    r = run("methods", "--dry", run_dir=tmp_path)
    assert r.returncode == 0, r.stderr
    assert (tmp_path / "_prompt_methods.txt").exists()
    assert not (tmp_path / "02_methods.md").exists()
