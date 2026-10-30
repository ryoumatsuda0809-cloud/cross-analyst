# cross-analyst: from research papers to a financial diagnostic report

A small Python pipeline that

1. reads research papers (PDF) from a local folder,
2. extracts their text and finds the sections that describe their **methods**,
3. uses an LLM API to turn those methods into "method cards" and apply them to a company's financial data,
4. writes a **Markdown diagnostic report**, and checks that every number in it can be traced back to the data.

Everything in `data/` is **fictional**. The two sample papers are synthetic (written to test this repository, CC0)
and the company "Harbor Lane Supply Co." does not exist.

---

## Design in one paragraph

The model never gets tools. It cannot open files, browse, or run code. This program decides exactly what text
each LLM stage receives (see the `STAGES` table in `pipeline/stages.py`) and pastes it into the prompt. That gives
three guarantees you can check yourself:

| Guarantee | How |
|---|---|
| The method stage cannot tailor methods to the company | it is never given the financial data (`forbidden` in `STAGES`; tested in `tests/`) |
| The model does no arithmetic | all ratios are computed in Python (`pipeline/financials.py`) with formulas shown |
| Numbers in the report are not invented | `pipeline/check.py` matches every number in the report against the computed data |

Every LLM call is logged in `run_record.json`: model, token counts, and the SHA-256 of every file sent.

```
data/papers/*.pdf
   |  [extract]  (no LLM)
   v
01_extracted/*.methods.txt
   |  [methods]  (LLM)
   v
02_methods.md ----------------------+
                                    |  [apply]  (LLM)
data/financials/*.csv               +------------------> 03_diagnosis.md
   |  [metrics]  (no LLM)           |                        |  [report]  (LLM)
   v                                |                        v
03a_metrics.md ---------------------+               diagnostic_report.md
                                                             |  [check]  (no LLM)
                                                             v
                                                     check_result.txt
```

| Step | Command | Uses LLM? | Output |
|---|---|---|---|
| 1-2 Read PDFs, split sections | `extract` | no | `01_extracted/` |
| 3a Compute ratios | `metrics` | no | `03a_metrics.md` |
| 2 Identify methods | `methods` | yes | `02_methods.md` |
| 3 Apply methods to data | `apply` | yes | `03_diagnosis.md` |
| 4 Write the report | `report` | yes | `diagnostic_report.md` |
| 4 Verify the report | `check` | no | `check_result.txt` |

---

## Setup (once)

Requires Python 3.10 or newer.

```bash
git clone <this repository URL> cross-analyst
cd cross-analyst
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### API key

1. Get an API key from your LLM provider's developer console. The provider adapter is `pipeline/llm.py`;
   its header comment says which SDK it uses.
2. Copy the example file and put your key into it:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env`. **`.env` is in `.gitignore`. Never commit it, and never show it on screen.**
3. Check which models your key can use, and put one in `.env` as `LLM_MODEL`:
   ```bash
   python diagnose.py models
   ```

> **Data privacy.** On some providers' free tiers, your prompts may be used to improve their products.
> Use a free tier only with fictional or public data like the samples here. For real company data,
> use a paid key and check the provider's current terms.

---

## Running

### 1. Test the pipeline without an API key

```bash
python diagnose.py run --mock --run outputs/mock
python -m pytest -q
```

The mock model writes placeholder text. It only proves that every step runs and every file is created.

### 2. See exactly what the model will receive (no API call)

```bash
python diagnose.py extract --run outputs/run1
python diagnose.py metrics --run outputs/run1
python diagnose.py methods --dry --run outputs/run1
```

Open `outputs/run1/_prompt_methods.txt`. That file is the complete text the model would receive. Nothing else is sent.

### 3. Real run

```bash
python diagnose.py run --run outputs/run1
```

or one stage at a time, reading each output before moving on:

```bash
python diagnose.py extract --run outputs/run1     # then read 01_extracted/_extraction_summary.md
python diagnose.py metrics --run outputs/run1     # then read 03a_metrics.md
python diagnose.py methods --run outputs/run1     # then read 02_methods.md
python diagnose.py apply   --run outputs/run1     # then read 03_diagnosis.md
python diagnose.py report  --run outputs/run1     # then read diagnostic_report.md
python diagnose.py check   --run outputs/run1
```

### Using your own papers and data

```bash
python diagnose.py run --papers path/to/pdfs --financials path/to/company.csv --run outputs/mycase
```

The CSV has one row per line item and one column per period. Lines starting with `#` are comments;
`# company: <name>` sets the company name. See `data/financials/harbor_lane_supply.csv`.
Line item names the ratios use: `revenue, cost_of_sales, gross_profit, operating_income, interest_expense,
net_income, operating_cash_flow, cash, receivables, inventory, current_assets, payables,
current_liabilities, total_assets, total_liabilities, equity`. Missing items are reported as `n/a`.

Only use PDFs you have the right to use (public domain, CC0, or a licence that allows it).

---

## What to look at after a run (review checklist)

1. **`01_extracted/_extraction_summary.md`**: did each paper's method text come from a real Methods section,
   or from `FALLBACK`? Any "no text layer" warning means the PDF is a scanned image.
2. **`02_methods.md`**: does every threshold have a quotation from the paper? Compare with the PDF.
3. **`03_diagnosis.md`**: are non-applicable methods marked as such, with the missing input named?
4. **`check`**: any number flagged here was not in the data. Treat it as an error.
5. **`_note_<stage>.md`**: the model's own note on what it could not do.
6. **`run_record.json`**: which model ran, and what was sent.

`check` can tell you whether numbers are traceable. It cannot tell you whether the reasoning is good. That part is the reviewer's job.

---

## Troubleshooting

| Message | Meaning / fix |
|---|---|
| `LLM_API_KEY is not set` | create `.env` from `.env.example`, or use `--mock` |
| `LLM_MODEL is not set` | run `python diagnose.py models` and put a name in `.env` |
| `the model did not use the output markers` | the raw answer is saved as `_raw_<stage>.md`; run the stage again |
| `LLM API error ... retrying` | usually a rate limit on a free tier; wait, or use a lighter model |
| `No text layer` | the PDF is scanned; run OCR on it first |
| `No Methods/Model heading found` | the whole paper was sent instead; check `02_methods.md` carefully |
| `Stage 'apply' has no input yet` | run the earlier steps first (or use `run`) |

## Repository layout

```
diagnose.py              command-line entry point
pipeline/pdf_extract.py  PDF -> text -> sections
pipeline/financials.py   CSV -> ratios (Python arithmetic)
pipeline/stages.py       what each LLM stage sees; output markers; run record; mock model
pipeline/llm.py          provider adapter: the only file that calls the LLM API
pipeline/check.py        traceability check for numbers and method IDs
pipeline/prompts/        the three prompt templates
data/                    fictional sample papers and financials
scripts/                 regenerates the sample PDFs
tests/                   pytest, no API key needed
```
