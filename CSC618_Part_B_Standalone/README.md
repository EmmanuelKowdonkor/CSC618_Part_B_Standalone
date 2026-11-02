# CSC 618 Week 10 — Part B: Controlled Retrieval Evaluation

This is a **standalone** Part B project using the exact documents, queries, relevance sets, and System A/B rankings provided in the course assignment. The rankings are prescribed **hypothetical** lists, not retrieval-engine output.

## Files

- `part_b.py` — eight documents, three queries, supplied System A/B rankings; runs the experiment and calculates aggregates.
- `evaluation.py` — reusable Precision, Recall, F1, Precision@3, Reciprocal Rank, Average Precision, DCG and nDCG functions.
- `results/part_b_per_query.csv` — six system/query rows.
- `results/part_b_summary.json` — MAP, MRR, Q1 DCG@5 and nDCG@5.
- `run_windows.bat` / `run_mac.sh` — optional one-command runners.

## Step 1 — Open in VS Code (Windows)

1. Download the repository or project ZIP and **extract it**. Do not run code directly inside a ZIP.
2. Open VS Code, select **File > Open Folder**, and choose `CSC618_Part_B_Standalone`.
3. Choose **Terminal > New Terminal**. The prompt should end in `CSC618_Part_B_Standalone`.

## Step 2 — Check Python

In the VS Code terminal (PowerShell):

```powershell
py --version
```

Python 3.10 or later is recommended. If `py` is not available, try `python --version`.

**No pip installation is required.** All modules used by these two scripts (`csv`, `json`, `pathlib`, `statistics`, `math`) are included with Python. You do NOT need Java or Lucene for Part B.

## Step 3 — Execute the experiment

Windows PowerShell, from this project's folder:

```powershell
py part_b.py
```

Or, if `py` does not work:

```powershell
python part_b.py
```

You may alternatively run `run_windows.bat` from Command Prompt (or by double-clicking).

Mac/Linux terminal:

```bash
python3 --version
python3 part_b.py
```

Or use `bash run_mac.sh`.

## Step 4 — Inspect the output

The terminal prints six dictionaries (System A and B, queries Q1–Q3) followed by an `AGGREGATE` JSON summary. The script **regenerates** both files in the `results` folder:

- `results/part_b_per_query.csv`
- `results/part_b_summary.json`

For Excel, open `results/part_b_per_query.csv` directly.

Expected aggregate results (rounded to four decimal places):

| System | MAP | MRR | Q1 nDCG@5 | Q1 DCG@5 |
| --- | ---: | ---: | ---: | ---: |
| A | 0.8056 | 1.0000 | 0.9508 | 8.9307 |
| B | 0.4852 | 0.5000 | 0.6078 | 5.7085 |

These values use the assignment's supplied rankings and relevance judgments. F1 output such as `0.7499999999999999` is simply floating-point representation of `0.7500`.

## Where the answers come from

- `part_b.py`: `DOCUMENTS`, `QUERIES`, `RELEVANT`, `RANKINGS`, `GRADES_Q1` contain the supplied experimental input.
- `evaluation.py`: `precision_recall_f1`, `precision_at_k`, `reciprocal_rank`, `average_precision`, `dcg_at_k`, and `ndcg_at_k` implement the required metrics.
- `part_b.py`: `main` computes the six results, MAP, MRR, and Q1 DCG/nDCG.

The **written Part B PDF report** is a separate submission that contains the manual worked examples, full table, interpretations, and responses to questions (a)–(h). This code folder is reproducible evidence, not a substitute for the written report.

## Troubleshooting

- `ModuleNotFoundError: No module named 'evaluation'`: Check `part_b.py` and `evaluation.py` are in the **same folder**.
- `can't open file 'part_b.py'`: Open the correct project folder in VS Code, or run `cd` to it first.
- Missing `results` directory: The script automatically creates it.

Do not upload `.venv`, `__pycache__`, `.pyc`, passwords, or local machine files to GitHub.
