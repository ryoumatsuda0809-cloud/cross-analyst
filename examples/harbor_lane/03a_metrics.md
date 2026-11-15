# Financial data and computed metrics: Harbor Lane Supply Co. (FICTIONAL)

All values below were computed by `pipeline/financials.py`.

## Raw line items

| item | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| capital_expenditures | 120.0 | 180.0 | 220.0 |
| cash | 380.0 | 210.0 | 95.0 |
| cost_of_sales | 3,150.0 | 3,660.0 | 4,160.0 |
| current_assets | 1,560.0 | 1,900.0 | 2,340.0 |
| current_liabilities | 980.0 | 1,350.0 | 1,880.0 |
| depreciation | 60.0 | 70.0 | 80.0 |
| ebit | 290.0 | 310.0 | 300.0 |
| equity | 1,100.0 | 1,160.0 | 1,220.0 |
| gross_profit | 1,050.0 | 1,170.0 | 1,250.0 |
| interest_expense | 40.0 | 55.0 | 80.0 |
| inventory | 610.0 | 860.0 | 1,120.0 |
| net_income | 180.0 | 190.0 | 175.0 |
| operating_cash_flow | 240.0 | 90.0 | -60.0 |
| operating_income | 290.0 | 310.0 | 300.0 |
| payables | 430.0 | 470.0 | 520.0 |
| receivables | 520.0 | 790.0 | 1,080.0 |
| revenue | 4,200.0 | 4,830.0 | 5,410.0 |
| taxes | 60.0 | 65.0 | 60.0 |
| total_assets | 2,600.0 | 3,050.0 | 3,560.0 |
| total_debt | 700.0 | 950.0 | 1,300.0 |
| total_liabilities | 1,500.0 | 1,890.0 | 2,340.0 |
| undrawn_credit_lines | 300.0 | 200.0 | 80.0 |

## Computed ratios

| ratio | formula | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| current_ratio | `current_assets / current_liabilities` | 1.5918 | 1.4074 | 1.2447 |
| quick_ratio | `(cash + receivables) / current_liabilities` | 0.9184 | 0.7407 | 0.6250 |
| debt_to_equity | `total_liabilities / equity` | 1.3636 | 1.6293 | 1.9180 |
| gross_margin | `gross_profit / revenue` | 0.2500 | 0.2422 | 0.2311 |
| operating_margin | `operating_income / revenue` | 0.0690 | 0.0642 | 0.0555 |
| net_margin | `net_income / revenue` | 0.0429 | 0.0393 | 0.0323 |
| roa | `net_income / total_assets` | 0.0692 | 0.0623 | 0.0492 |
| roe | `net_income / equity` | 0.1636 | 0.1638 | 0.1434 |
| interest_coverage | `operating_income / interest_expense` | 7.2500 | 5.6364 | 3.7500 |
| asset_turnover | `revenue / total_assets` | 1.6154 | 1.5836 | 1.5197 |
| dso_days | `receivables / revenue * 365` | 45.2 | 59.7 | 72.9 |
| dio_days | `inventory / cost_of_sales * 365` | 70.7 | 85.8 | 98.3 |
| dpo_days | `payables / cost_of_sales * 365` | 49.8 | 46.9 | 45.6 |
| cash_conversion_cycle | `dso_days + dio_days - dpo_days` | 66.0 | 98.6 | 125.5 |
| accrual_ratio | `(net_income - operating_cash_flow) / total_assets` | -0.0231 | 0.0328 | 0.0660 |
| ocf_to_net_income | `operating_cash_flow / net_income` | 1.3333 | 0.4737 | -0.3429 |
| ebit_interest_coverage | `ebit / interest_expense` | 7.2500 | 5.6364 | 3.7500 |
| total_debt_to_assets | `total_debt / total_assets` | 0.2692 | 0.3115 | 0.3652 |
| free_cash_flow | `operating_income + depreciation - interest_expense - taxes - capital_expenditures` | 130.0 | 80.0 | 20.0 |
| free_cash_flow_to_assets | `free_cash_flow / total_assets` | 0.0500 | 0.0262 | 0.0056 |
| undrawn_credit_lines_to_assets | `undrawn_credit_lines / total_assets` | 0.1154 | 0.0656 | 0.0225 |
| revenue_growth | `revenue / previous revenue - 1` | n/a (first period) | 0.1500 | 0.1201 |
| dso_days_change | `dso_days - previous dso_days` | n/a (first period) | 14.5 | 13.2 |
| dio_days_change | `dio_days - previous dio_days` | n/a (first period) | 15.1 | 12.5 |
| dpo_days_change | `dpo_days - previous dpo_days` | n/a (first period) | -2.9538 | -1.2466 |
| cash_conversion_cycle_change | `cash_conversion_cycle - previous cash_conversion_cycle` | n/a (first period) | 32.5 | 26.9 |
