#!/usr/bin/env python3
"""Generate the two SYNTHETIC sample papers in data/papers/.

They are not real publications. They exist so the pipeline can be tested
without any copyrighted material. Released under CC0 (public domain).

    pip install reportlab
    python scripts/make_sample_papers.py
"""
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

OUT = Path(__file__).resolve().parent.parent / "data/papers"
NOTICE = ("SYNTHETIC SAMPLE PAPER. Written only to test this repository. Not a real publication; "
          "the authors and findings are invented. Released under CC0 1.0 (public domain).")

PAPERS = {
    "sample_liquidity_screen.pdf": {
        "title": "A Liquidity Stress Screen for Small Wholesale Firms",
        "sections": [
            ("Abstract", "We propose a three-test screen that flags liquidity stress in small wholesale "
             "firms using only annual financial statements."),
            ("1 Introduction", "Small wholesalers often grow sales while running out of cash. Traditional "
             "single-ratio checks miss this pattern because each ratio can look acceptable on its own."),
            ("2 Method", "The screen applies three tests to each fiscal year. "
             "Test L1: the current ratio (current assets divided by current liabilities) is below 1.2. "
             "Test L2: the quick ratio (cash plus receivables, divided by current liabilities) is below 0.8. "
             "Test L3: the cash conversion cycle (days sales outstanding plus days inventory outstanding "
             "minus days payables outstanding) is above 90 days, or has lengthened by more than 15 days "
             "compared with the previous year. "
             "A firm-year is classified as \"in liquidity stress\" when at least two of the three tests are met. "
             "When only one test is met, the firm-year is classified as \"watch\"."),
            ("3 Results", "In our illustrative sample, firms classified as in liquidity stress were more likely "
             "to seek emergency financing within the following year."),
            ("4 Limitations", "The thresholds were chosen for wholesale firms and may not transfer to other "
             "industries. The screen uses year-end balances, which can be distorted by seasonality."),
            ("References", "None. This is a synthetic paper."),
        ],
    },
    "sample_accrual_screen.pdf": {
        "title": "Cash-Backed Earnings: An Accrual Screen for Owner-Managed Firms",
        "sections": [
            ("Abstract", "We describe a simple screen for whether reported profits are backed by operating cash."),
            ("1 Introduction", "Owner-managed firms can report steady profits while cash flow deteriorates, "
             "for example when receivables grow faster than sales."),
            ("2 Methodology", "Measure A1 is the accrual ratio, defined as net income minus operating cash flow, "
             "divided by total assets. An accrual ratio above 0.10 indicates that earnings are weakly backed by "
             "cash. Measure A2 is the cash coverage of earnings, defined as operating cash flow divided by net "
             "income. A value below 0.5 in two consecutive years indicates persistent earnings without cash. "
             "Measure A3 compares the growth of days sales outstanding with the growth of revenue: if days "
             "sales outstanding rises in a year in which revenue also rises, receivables are building up faster "
             "than sales. A firm is flagged when A1 or A2 is met; A3 is reported as supporting evidence only."),
            ("3 Results", "In our illustrative cases, A2 detected cash problems earlier than A1."),
            ("4 Limitations", "The screen cannot tell whether a receivables build-up is caused by deliberate "
             "credit policy, a few large customers, or collection problems. That requires information from inside "
             "the firm."),
            ("References", "None. This is a synthetic paper."),
        ],
    },
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    for name, paper in PAPERS.items():
        doc = SimpleDocTemplate(str(OUT / name), pagesize=A4, title=paper["title"], author="Synthetic sample", invariant=1)
        story = [Paragraph(paper["title"], styles["Title"]),
                 Paragraph("Sample Author A, Sample Author B", styles["Normal"]),
                 Paragraph(NOTICE, styles["Italic"]), Spacer(1, 12)]
        for heading, body in paper["sections"]:
            story += [Paragraph(heading, styles["Heading2"]), Paragraph(body, styles["BodyText"]), Spacer(1, 8)]
        doc.build(story)
        print(f"wrote {OUT / name}")


if __name__ == "__main__":
    main()
