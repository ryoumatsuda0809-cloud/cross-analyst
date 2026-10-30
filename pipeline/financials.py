"""Step 3a: load the financial data and compute ratios in Python.

Why compute here instead of asking the LLM?
Language models are unreliable at arithmetic. Every number the model is
allowed to use is calculated here, shown with its formula, and later
checked against the final report (see check.py).

Input CSV format (one row per line item, one column per period):

    item,FY2023,FY2024,FY2025
    revenue,1200,1380,1610
    ...
"""
from __future__ import annotations

import csv
from pathlib import Path

# name -> (formula shown to the reader, function of a period's items)
RATIOS = {
    "current_ratio":        ("current_assets / current_liabilities",
                             lambda d: d["current_assets"] / d["current_liabilities"]),
    "quick_ratio":          ("(cash + receivables) / current_liabilities",
                             lambda d: (d["cash"] + d["receivables"]) / d["current_liabilities"]),
    "debt_to_equity":       ("total_liabilities / equity",
                             lambda d: d["total_liabilities"] / d["equity"]),
    "gross_margin":         ("gross_profit / revenue",
                             lambda d: d["gross_profit"] / d["revenue"]),
    "operating_margin":     ("operating_income / revenue",
                             lambda d: d["operating_income"] / d["revenue"]),
    "net_margin":           ("net_income / revenue",
                             lambda d: d["net_income"] / d["revenue"]),
    "roa":                  ("net_income / total_assets",
                             lambda d: d["net_income"] / d["total_assets"]),
    "roe":                  ("net_income / equity",
                             lambda d: d["net_income"] / d["equity"]),
    "interest_coverage":    ("operating_income / interest_expense",
                             lambda d: d["operating_income"] / d["interest_expense"]),
    "asset_turnover":       ("revenue / total_assets",
                             lambda d: d["revenue"] / d["total_assets"]),
    "dso_days":             ("receivables / revenue * 365",
                             lambda d: d["receivables"] / d["revenue"] * 365),
    "dio_days":             ("inventory / cost_of_sales * 365",
                             lambda d: d["inventory"] / d["cost_of_sales"] * 365),
    "dpo_days":             ("payables / cost_of_sales * 365",
                             lambda d: d["payables"] / d["cost_of_sales"] * 365),
    "cash_conversion_cycle": ("dso_days + dio_days - dpo_days",
                             lambda d: (d["receivables"] / d["revenue"] + d["inventory"] / d["cost_of_sales"]
                                        - d["payables"] / d["cost_of_sales"]) * 365),
    "accrual_ratio":        ("(net_income - operating_cash_flow) / total_assets",
                             lambda d: (d["net_income"] - d["operating_cash_flow"]) / d["total_assets"]),
    "ocf_to_net_income":    ("operating_cash_flow / net_income",
                             lambda d: d["operating_cash_flow"] / d["net_income"]),
}


def load(path: Path) -> tuple[list[str], dict[str, dict[str, float]]]:
    """Returns (periods, {period: {item: value}})."""
    with path.open(newline="", encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].lstrip().startswith("#")]   # skip comment lines
    if len(rows) < 2 or len(rows[0]) < 2:
        raise SystemExit(f"{path}: expected a header like 'item,FY2023,FY2024' and at least one data row")
    header, body = rows[0], [r for r in rows[1:] if r and r[0].strip() and not r[0].startswith("#")]
    periods = [h.strip() for h in header[1:]]
    data: dict[str, dict[str, float]] = {p: {} for p in periods}
    for r in body:
        item = r[0].strip()
        for p, v in zip(periods, r[1:]):
            if v.strip():
                data[p][item] = float(v.replace(",", ""))
    return periods, data


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
    # period-over-period revenue growth
    out["revenue_growth"] = {periods[0]: "n/a (first period)"}
    for prev, cur in zip(periods, periods[1:]):
        try:
            out["revenue_growth"][cur] = data[cur]["revenue"] / data[prev]["revenue"] - 1
        except (KeyError, ZeroDivisionError):
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
             "All values below were computed by `pipeline/financials.py`, not by the LLM.", "",
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


def all_numbers(periods, data, ratios) -> list[float]:
    """Every number the report is allowed to quote (used by check.py)."""
    nums = [v for p in periods for v in data[p].values()]
    nums += [v for vals in ratios.values() for v in vals.values() if not isinstance(v, str)]
    return nums
