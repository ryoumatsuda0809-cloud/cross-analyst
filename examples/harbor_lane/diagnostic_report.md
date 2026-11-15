# Financial Diagnostic Report: Harbor Lane Supply Co. (FICTIONAL)

## Summary

All applicable methods (M1, M2, M3, M4, M7) point the same way: worsening.

- **M1** Firm-level interest coverage ratio (simple threshold): the ratio fell in every period; lower is worse under this method, so the verdict is worsening. Threshold: not breached. Confidence: high.
- **M2** Free cash flow relative to total assets: the ratio fell in every period; lower is worse under this method, so the verdict is worsening. Threshold: none stated. Confidence: medium.
- **M3** Leverage (total debt over assets): the ratio rose in every period; higher is worse under this method, so the verdict is worsening. Threshold: none stated. Confidence: medium.
- **M4** Credit line availability (undrawn lines of credit over assets): the ratio fell in every period; lower is worse under this method, so the verdict is worsening. Threshold: none stated. Confidence: medium.
- **M7** Firm interest coverage below 2 (debt-at-risk criterion): the ratio fell in every period; lower is worse under this method, so the verdict is worsening. Threshold: not breached. Confidence: high.

## Findings

### M1: Firm-level interest coverage ratio (simple threshold)

- **What it means:** whether earnings are enough to cover interest expenses
- **Evidence:** `ebit_interest_coverage`, from 03a_metrics.md: FY2023 7.2500; FY2024 5.6364; FY2025 3.7500
- **Reading:** The ratio moved from 7.2500 (FY2023) to 3.7500 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: whether earnings are enough to cover interest expenses. It did not meet the threshold condition in any period.
- **Method and confidence:** M1; high, because the paper states a threshold and the ratio is available in every period.

### M2: Free cash flow relative to total assets

- **What it means:** how much cash the business generates after interest, taxes and investment, relative to its size
- **Evidence:** `free_cash_flow_to_assets`, from 03a_metrics.md: FY2023 0.0500; FY2024 0.0262; FY2025 0.0056
- **Reading:** The ratio moved from 0.0500 (FY2023) to 0.0056 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: how much cash the business generates after interest, taxes and investment, relative to its size.
- **Method and confidence:** M2; medium, because the paper states no threshold, so only the direction of change is judged.

### M3: Leverage (total debt over assets)

- **What it means:** how much of the company's assets is financed by debt
- **Evidence:** `total_debt_to_assets`, from 03a_metrics.md: FY2023 0.2692; FY2024 0.3115; FY2025 0.3652
- **Reading:** The ratio moved from 0.2692 (FY2023) to 0.3652 (FY2025) and rose in every period. Under this method that is the worse direction, which indicates a weakening in: how much of the company's assets is financed by debt.
- **Method and confidence:** M3; medium, because the paper states no threshold, so only the direction of change is judged.

### M4: Credit line availability (undrawn lines of credit over assets)

- **What it means:** how much unused borrowing capacity the company has as a buffer
- **Evidence:** `undrawn_credit_lines_to_assets`, from 03a_metrics.md: FY2023 0.1154; FY2024 0.0656; FY2025 0.0225
- **Reading:** The ratio moved from 0.1154 (FY2023) to 0.0225 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: how much unused borrowing capacity the company has as a buffer.
- **Method and confidence:** M4; medium, because the paper states no threshold, so only the direction of change is judged.

### M7: Firm interest coverage below 2 (debt-at-risk criterion)

- **What it means:** whether the company would count as a firm whose debt is at risk
- **Evidence:** `ebit_interest_coverage`, from 03a_metrics.md: FY2023 7.2500; FY2024 5.6364; FY2025 3.7500
- **Reading:** The ratio moved from 7.2500 (FY2023) to 3.7500 (FY2025) and fell in every period. Under this method that is the worse direction, which indicates a weakening in: whether the company would count as a firm whose debt is at risk. It did not meet the threshold condition in any period.
- **Method and confidence:** M7; high, because the paper states a threshold and the ratio is available in every period.

### Do the methods agree?

All applicable methods (M1, M2, M3, M4, M7) point the same way: worsening.

## Questions to verify with the company

1. operating_cash_flow fell every period (FY2023 240.0; FY2024 90.0; FY2025 -60.0) while net_income stayed positive (FY2023 180.0; FY2024 190.0; FY2025 175.0). What explains the gap between reported profit and cash from operations (for example slower customer payments, inventory purchases, or one-off items)?
2. receivables rose every period (FY2023 520.0; FY2024 790.0; FY2025 1,080.0), and dso_days also rose (FY2023 45.2; FY2024 59.7; FY2025 72.9). Did customer payment terms change, is a small number of customers behind the increase, or are collections slower?
3. inventory rose every period (FY2023 610.0; FY2024 860.0; FY2025 1,120.0), and dio_days also rose (FY2023 70.7; FY2024 85.8; FY2025 98.3). Was the build-up planned, and is any of the stock slow-moving?
4. capital_expenditures rose every period (FY2023 120.0; FY2024 180.0; FY2025 220.0) while free_cash_flow fell (FY2023 130.0; FY2024 80.0; FY2025 20.0). What was the money spent on, and how was it funded?
5. undrawn_credit_lines fell every period (FY2023 300.0; FY2024 200.0; FY2025 80.0). Were credit lines drawn, reduced or cancelled, and what are their terms, maturity dates and renewal plans?
6. total_debt (FY2023 700.0; FY2024 950.0; FY2025 1,300.0) and interest_expense (FY2023 40.0; FY2024 55.0; FY2025 80.0) both rose every period. Which part of the debt carries a floating rate, and when do fixed rates reset?
7. M5: Share of debt maturing within a year could not be applied because the data has no debt_maturing_within_one_year. Can the company supply it for FY2023 to FY2025?
8. M6: Debt composition (bonds relative to total debt) could not be applied because the data has no total_bonds. Can the company supply it for FY2023 to FY2025?
9. M8: Aggregate interest coverage and scenario projection is a sector-wide method. Is comparable sector or peer data available to put this company's figures in context?

## Methods used

| method | source paper | status | reason |
|---|---|---|---|
| M1: Firm-level interest coverage ratio (simple threshold) | fed_icr_vulnerabilities_2020.pdf | applied | - |
| M2: Free cash flow relative to total assets | fed_icr_vulnerabilities_2020.pdf | applied | - |
| M3: Leverage (total debt over assets) | fed_icr_vulnerabilities_2020.pdf | applied | - |
| M4: Credit line availability (undrawn lines of credit over assets) | fed_icr_vulnerabilities_2020.pdf | applied | - |
| M5: Share of debt maturing within a year | fed_icr_vulnerabilities_2020.pdf | not applicable | missing line item(s): debt_maturing_within_one_year |
| M6: Debt composition (bonds relative to total debt) | fed_icr_vulnerabilities_2020.pdf | not applicable | missing line item(s): total_bonds |
| M7: Firm interest coverage below 2 (debt-at-risk criterion) | fed_icr_stress_test_2024.pdf | applied | - |
| M8: Aggregate interest coverage and scenario projection | fed_icr_stress_test_2024.pdf | not applicable | aggregate-level method: it needs many firms or sector data, and this data is one company; missing line item(s): aggregate_ebit, aggregate_interest_expense |

## Limitations

- Every statement is a hypothesis from fixed rules applied to a few annual periods of year-end figures. None of it explains causes; the questions above are the way to find them.
- A threshold was used only where a paper states one (M1, M7). For every other method only the direction of change is reported.
- Thresholds come from the papers' own samples and may not suit this company.
- Methods not applied: M5, M6, M8. See the reasons in the Methods used table.
- All numbers are copied from 03a_metrics.md. No new calculation was made when writing this report.
