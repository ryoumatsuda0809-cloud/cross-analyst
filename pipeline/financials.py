"""Step 3a: load the financial data and compute ratios in Python.

All arithmetic in the project happens here. Every number the diagnosis and
the report may quote is calculated in this file, shown with its formula in
03a_metrics.md, and later checked against both documents (see check.py).

Input CSV format (one row per line item, one column per period):

    item,FY2023,FY2024,FY2025
    revenue,1200,1380,1610
    ...
"""
from __future__ import annotations

import csv
import math
import re
from pathlib import Path

class Undefined(Exception):
    """The ratio has no meaning for this period (the reason is the message)."""


def _div(num: float, d, den_item: str) -> float:
    """num / d[den_item], but only when the denominator is positive.

    A ratio over a zero denominator does not exist, and over a negative one its sign is misleading
    (negative net income over negative equity would show as a healthy positive return on equity).
    """
    den = d[den_item]
    if den == 0:
        raise ZeroDivisionError
    if den < 0:
        raise Undefined(f"negative {den_item}")
    return num / den


def _fcf(d) -> float:
    return d["operating_income"] + d["depreciation"] - d["interest_expense"] - d["taxes"] - d["capital_expenditures"]


# name -> (formula shown to the reader, function of a period's items)
RATIOS = {
    "current_ratio":        ("current_assets / current_liabilities",
                             lambda d: _div(d["current_assets"], d, "current_liabilities")),
    "quick_ratio":          ("(cash + receivables) / current_liabilities",
                             lambda d: _div(d["cash"] + d["receivables"], d, "current_liabilities")),
    "debt_to_equity":       ("total_liabilities / equity",
                             lambda d: _div(d["total_liabilities"], d, "equity")),
    "gross_margin":         ("gross_profit / revenue",
                             lambda d: _div(d["gross_profit"], d, "revenue")),
    "operating_margin":     ("operating_income / revenue",
                             lambda d: _div(d["operating_income"], d, "revenue")),
    "net_margin":           ("net_income / revenue",
                             lambda d: _div(d["net_income"], d, "revenue")),
    "roa":                  ("net_income / total_assets",
                             lambda d: _div(d["net_income"], d, "total_assets")),
    "roe":                  ("net_income / equity",
                             lambda d: _div(d["net_income"], d, "equity")),
    "interest_coverage":    ("operating_income / interest_expense",
                             lambda d: _div(d["operating_income"], d, "interest_expense")),
    "asset_turnover":       ("revenue / total_assets",
                             lambda d: _div(d["revenue"], d, "total_assets")),
    "dso_days":             ("receivables / revenue * 365",
                             lambda d: _div(d["receivables"], d, "revenue") * 365),
    "dio_days":             ("inventory / cost_of_sales * 365",
                             lambda d: _div(d["inventory"], d, "cost_of_sales") * 365),
    "dpo_days":             ("payables / cost_of_sales * 365",
                             lambda d: _div(d["payables"], d, "cost_of_sales") * 365),
    "cash_conversion_cycle": ("dso_days + dio_days - dpo_days",
                             lambda d: (_div(d["receivables"], d, "revenue") + _div(d["inventory"], d, "cost_of_sales")
                                        - _div(d["payables"], d, "cost_of_sales")) * 365),
    "accrual_ratio":        ("(net_income - operating_cash_flow) / total_assets",
                             lambda d: _div(d["net_income"] - d["operating_cash_flow"], d, "total_assets")),
    "ocf_to_net_income":    ("operating_cash_flow / net_income",
                             lambda d: _div(d["operating_cash_flow"], d, "net_income")),
    # Ratios used by the interest coverage papers
    "ebit_interest_coverage": ("ebit / interest_expense",
                               lambda d: _div(d["ebit"], d, "interest_expense")),
    "total_debt_to_assets":   ("total_debt / total_assets",
                               lambda d: _div(d["total_debt"], d, "total_assets")),
    "free_cash_flow":         ("operating_income + depreciation - interest_expense - taxes - capital_expenditures",
                               _fcf),
    "free_cash_flow_to_assets": ("free_cash_flow / total_assets",
                               lambda d: _div(_fcf(d), d, "total_assets")),
    "undrawn_credit_lines_to_assets": ("undrawn_credit_lines / total_assets",
                               lambda d: _div(d["undrawn_credit_lines"], d, "total_assets")),
}


class _Recorder(dict):
    """Stands in for a period's items and remembers which ones a ratio asked for."""

    def __missing__(self, key):
        self[key] = 1.0
        return 1.0


def inputs_of(ratio: str) -> list[str]:
    """The line items the ratio's function actually reads (so a method card's `inputs` can be checked)."""
    rec = _Recorder()
    RATIOS[ratio][1](rec)
    return sorted(rec)


# Other names a data file may use for the line items above. The key is the normalized spelling
# (lower case, spaces and hyphens as "_"); an unknown name is kept as written and simply goes unused.
ALIASES = {
    "revenue": ("sales", "net_sales", "total_revenue", "total_sales", "売上高", "売上"),
    "cost_of_sales": ("cost_of_goods_sold", "cogs", "cost_of_revenue", "売上原価"),
    "gross_profit": ("gross_income", "売上総利益"),
    "operating_income": ("operating_profit", "income_from_operations", "営業利益"),
    "ebit": ("earnings_before_interest_and_taxes",),
    "depreciation": ("depreciation_and_amortization", "d_and_a", "減価償却費"),
    "interest_expense": ("interest_paid", "interest_expenses", "支払利息"),
    "taxes": ("income_taxes", "income_tax_expense", "tax_expense", "法人税等"),
    "net_income": ("net_profit", "net_earnings", "profit_for_the_year", "当期純利益"),
    "operating_cash_flow": ("cash_from_operations", "cash_flow_from_operations", "ocf", "営業キャッシュフロー"),
    "capital_expenditures": ("capex", "capital_expenditure", "設備投資"),
    "cash": ("cash_and_equivalents", "cash_and_cash_equivalents", "現金及び預金"),
    "receivables": ("accounts_receivable", "trade_receivables", "売掛金"),
    "inventory": ("inventories", "棚卸資産"),
    "current_assets": ("total_current_assets", "流動資産"),
    "payables": ("accounts_payable", "trade_payables", "買掛金"),
    "current_liabilities": ("total_current_liabilities", "流動負債"),
    "total_debt": ("interest_bearing_debt", "borrowings", "有利子負債"),
    "undrawn_credit_lines": ("undrawn_credit_facilities", "unused_credit_lines"),
    "total_assets": ("assets_total", "総資産", "資産合計"),
    "total_liabilities": ("liabilities_total", "負債合計"),
    "equity": ("shareholders_equity", "stockholders_equity", "total_equity", "純資産", "自己資本"),
}
_CANONICAL = {alias: name for name, aliases in ALIASES.items() for alias in aliases}


def canonical_item(name: str) -> str:
    """The name this pipeline uses for a line item ('Net Sales' -> 'revenue'); unknown names are kept as written."""
    key = re.sub(r"[\s\-]+", "_", name.strip().lower().replace("&", "and"))
    if key in ALIASES:
        return key
    return _CANONICAL.get(key, name.strip())


def load(path: Path) -> tuple[list[str], dict[str, dict[str, float]]]:
    """Returns (periods, {period: {item: value}}). Line item names are mapped with canonical_item()."""
    if not path.is_file():
        raise SystemExit(f"{path}: financial data file not found. Pass one with --financials path/to/company.csv")
    with path.open(newline="", encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].lstrip().startswith("#")]   # skip comment lines
    if len(rows) < 2 or len(rows[0]) < 2:
        raise SystemExit(f"{path}: expected a header like 'item,FY2023,FY2024' and at least one data row")
    header, body = rows[0], [r for r in rows[1:] if r and r[0].strip() and not r[0].startswith("#")]
    periods = [h.strip() for h in header[1:]]
    if "" in periods or len(set(periods)) != len(periods):
        raise SystemExit(f"{path}: every period column needs its own name (got {', '.join(periods)})")
    _check_period_order(path, periods)
    data: dict[str, dict[str, float]] = {p: {} for p in periods}
    seen = set()
    for r in body:
        item = canonical_item(r[0])
        if item in seen:
            raise SystemExit(f"{path}: line item '{item}' appears more than once "
                             f"(including under another name, e.g. '{r[0].strip()}')")
        seen.add(item)
        for p, v in zip(periods, r[1:]):
            if v.strip():
                data[p][item] = _number(v, path, item, p)
    return periods, data


def _number(cell: str, path: Path, item: str, period: str) -> float:
    try:
        value = float(cell.replace(",", ""))
    except ValueError:
        value = math.nan
    if not math.isfinite(value):
        raise SystemExit(f"{path}: {item} in {period} is not a number: '{cell.strip()}' "
                         "(write negatives as -60, not (60); leave the cell empty when there is no value)")
    return value


def _check_period_order(path: Path, periods: list[str]) -> None:
    """Trends compare each period with the one to its left, so the columns must run oldest to newest."""
    years = [re.search(r"(?<!\d)(?:19|20)\d{2}(?!\d)", p) for p in periods]
    if not all(years):
        return                              # labels without a four-digit year cannot be checked
    years = [int(m.group()) for m in years]
    if any(b < a for a, b in zip(years, years[1:])):
        raise SystemExit(f"{path}: period columns must run from oldest to newest, left to right "
                         f"(got {', '.join(periods)}). Reorder the columns; otherwise every trend would be reversed.")


def compute(periods, data):
    """Returns {ratio: {period: value or reason-string}}."""
    out = {}
    for name, (_, fn) in RATIOS.items():
        out[name] = {}
        for p in periods:
            try:
                out[name][p] = fn(data[p])
            except KeyError as e:
                out[name][p] = f"n/a (missing {e.args[0]})"
            except ZeroDivisionError:
                out[name][p] = "n/a (division by zero)"
            except Undefined as e:
                out[name][p] = f"n/a ({e})"
    # period-over-period revenue growth
    out["revenue_growth"] = {periods[0]: "n/a (first period)"}
    for prev, cur in zip(periods, periods[1:]):
        try:
            out["revenue_growth"][cur] = _div(data[cur]["revenue"], data[prev], "revenue") - 1
        except (KeyError, ZeroDivisionError, Undefined):
            out["revenue_growth"][cur] = "n/a"
    # change vs previous period for the "days" metrics (methods often test whether a cycle lengthened)
    for name in ("dso_days", "dio_days", "dpo_days", "cash_conversion_cycle"):
        ch = {periods[0]: "n/a (first period)"}
        for prev, cur in zip(periods, periods[1:]):
            a, b = out[name][prev], out[name][cur]
            ch[cur] = b - a if not isinstance(a, str) and not isinstance(b, str) else "n/a"
        out[f"{name}_change"] = ch
    return out


def fmt(v) -> str:
    if isinstance(v, str):
        return v
    return f"{v:,.4f}" if abs(v) < 10 else f"{v:,.1f}"


def to_markdown(company: str, periods, data, ratios) -> str:
    lines = [f"# Financial data and computed metrics: {company}", "",
             "All values below were computed by `pipeline/financials.py`.", "",
             "## Raw line items", "", "| item | " + " | ".join(periods) + " |",
             "|---|" + "---|" * len(periods)]
    items = sorted({k for p in periods for k in data[p]})
    for it in items:
        lines.append(f"| {it} | " + " | ".join(fmt(data[p].get(it, "n/a")) for p in periods) + " |")
    lines += ["", "## Computed ratios", "", "| ratio | formula | " + " | ".join(periods) + " |",
              "|---|---|" + "---|" * len(periods)]
    formulas = {k: f for k, (f, _) in RATIOS.items()}
    formulas["revenue_growth"] = "revenue / previous revenue - 1"
    for name in ("dso_days", "dio_days", "dpo_days", "cash_conversion_cycle"):
        formulas[f"{name}_change"] = f"{name} - previous {name}"
    for name, vals in ratios.items():
        lines.append(f"| {name} | `{formulas[name]}` | " + " | ".join(fmt(vals[p]) for p in periods) + " |")
    return "\n".join(lines) + "\n"


def to_float(text: str):
    """Value of a cell written by to_markdown, or None for 'n/a ...' cells."""
    text = text.strip()
    if text.startswith("n/a"):
        return None
    try:
        return float(text.replace(",", ""))
    except ValueError:
        return None


def read_markdown(path: Path):
    """Read 03a_metrics.md back. Returns (company, periods, raw, ratios).

    raw and ratios map a name to {period: cell text exactly as written in the file}, so later
    steps can quote a value without recomputing it.
    """
    company, periods = "", []
    raw: dict[str, dict[str, str]] = {}
    ratios: dict[str, dict[str, str]] = {}
    section = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# Financial data and computed metrics:"):
            company = line.split(":", 1)[1].strip()
        elif line.startswith("## "):
            section = line[3:].strip()
        elif line.startswith("|") and section in ("Raw line items", "Computed ratios"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells[0] in ("item", "ratio"):
                periods = cells[1:] if section == "Raw line items" else cells[2:]
            elif not cells[0].startswith("---"):
                if section == "Raw line items":
                    raw[cells[0]] = dict(zip(periods, cells[1:]))
                else:
                    ratios[cells[0]] = dict(zip(periods, cells[2:]))
    if not periods or not ratios:
        raise SystemExit(f"{path}: not a 03a_metrics.md file. Run the metrics step first.")
    return company, periods, raw, ratios


def all_numbers(periods, data, ratios) -> list[float]:
    """Every number the report is allowed to quote (used by check.py)."""
    nums = [v for p in periods for v in data[p].values()]
    nums += [v for vals in ratios.values() for v in vals.values() if not isinstance(v, str)]
    return nums
