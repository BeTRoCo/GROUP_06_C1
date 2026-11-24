# GROUP_06 — How much does the starting grid shape a Formula 1 race? (2014–2024)

**Business Intelligence · IIB423T-1 · Universidad del Desarrollo**
Group 06: **Maximiliano Sandoval Mosser** and **Benjamín Toloza Cossio** · Instructor: Tomás Fontecilla Correa

**Version assessed for C3: GitHub release `C3`** (tag `C3`). Earlier releases are kept for history only.

---

## 1. How to read this repository (no installation, no data download)

Every notebook is saved **already executed**, with its tables, metrics and figures visible. The reviewer does not need to run
code, install software or download data. Following the C3 rules, **no data files are included** (see part 6), so the code cells
that read data are there to show the method next to each saved output; they are not meant to be re-run by the reviewer.

| Step | File | What you will find | Stage |
|---|---|---|---|
| 0 | `README.md` | Question, team, file roles, reading order, software | — |
| 1 | `analysis/01_EDA_raw_dataset.ipynb` | Source, version, tables, row meaning, coverage by year, integrity checks, duplicates, special codes; why 2014–2024 | C1 |
| 2 | `analysis/02_cleaning_analytic_table.ipynb` | Cleaning rules and how each one changed the rows (26,759 → 4,626 → 4,606); joins; data dictionary | C1 |
| 3 | `analysis/03_EDA_KPI.ipynb` | Distributions, IDC (main KPI), support and control KPIs, circuits, lap 1 | C1 |
| 4 | `notebooks/W2_project.ipynb` | Feedback-to-action table, 15 validation checks, sampling, leakage audit, train/validation/test design | W2 |
| 5 | `notebooks/2_C2_model.ipynb` | First model (as submitted in C2): logistic regression vs the grid rule | C2 |
| 6 | `notebooks/final_project.ipynb` (+ `.html`) | **One source of truth for every number in the final presentation**: walk-forward evaluation, final test, what the model adds, robustness | Final |
| 7 | `w3/benjamin/` and `w3/maximiliano/` | The two individual W3 visual systems (before/after views, rules, notebook) | W3 |
| 8 | `notebooks/final_views.ipynb` + `analysis/visual_system.py` | The final views of the presentation, drawn with the shared visual rules from saved summary results | C3 |
| 9 | `docs/decision_record.md` | Feedback received and what we did, decision log, W3 design selection, contributions, AI use | All |
| 10 | `docs/consistency_review.md` | 15 earlier claims checked and corrected so that every stage tells the same story | Final |
| 11 | `presentation/GROUP_06_C3_Presentation.pptx` (+ `.pdf`) | Final presentation: part 1 for the Head of Strategy, part 2 for the reviewer. Earlier slides of C1 and C2 are kept in the same folder | C3 |

**Short route (about 15 minutes):** README → `notebooks/final_project.ipynb` → `notebooks/final_views.ipynb` → `docs/decision_record.md` → `presentation/`.

## 2. The study in one paragraph

We study how closely the finishing order follows the starting grid in the 2014–2024 Formula 1 World Championship, and
whether, before the start, we can predict which drivers will finish in the points. The finishing order follows the grid
closely (IDC 0.81), but this is an **association**: part of it goes with car strength, no circuit stands out, and lap 1
holds only 10–13 % of position changes. A simple pre-race logistic regression that adds team strength predicts points
slightly better than the grid rule "the top 10 on the grid score points" (test F1 0.812 vs 0.790), but the gain is small
and its 95 % interval includes zero (−0.001 to +0.047).

## 3. Question, user and KPIs

- **Question:** How closely does the finishing order follow the starting grid, and can we use that, before the race, to predict who scores points?
- **Proposed user:** a team race strategist, who uses the evidence as a planning input before the race (what usually happens from each grid slot), not as a promise of what a better grid would cause.
- **Unit of observation:** one driver in one race (`raceId` + `driverId`): **4,606 rows, 227 races**, seasons 2014–2024 (3,751 finishers with a grid slot).
- **Main KPI — IDC:** median over races of the per-race Spearman correlation between grid slot and finishing position (finishers), with a 95 % bootstrap interval over races. +1 = same order as the grid, 0 = no relation.
- **Support KPIs:** share of starters who score points by grid block; pole conversion. **Control:** partial Spearman correlation holding the team's championship rank before the race fixed (an association, not an effect).
- **Prediction (C2 and final):** positive class = finishes in the top 10. Four inputs known when the grid is published (grid slot, pit-lane start, team rank after the previous round, qualifying gap). Logistic regression vs the grid rule.

## 4. Pipeline: from inputs to the final message

| # | Input | Notebook | Main steps and settings | Saved outputs (in this repository) | Used in |
|---|---|---|---|---|---|
| 1 | 12 raw Kaggle CSV files (not included) | `analysis/01` | Inventory, integrity between tables, coverage by year, duplicates, `\N` codes | Figures `E1_*` | Choice of period 2014–2024 |
| 2 | Raw files | `analysis/02` | Period filter, exclusion of Belgium 2021, pit-lane starts flagged, joins validated one-to-one, team rank after the previous round | `cleaning_log.csv`, `data_dictionary.csv` | Analytic table (4,606 rows) |
| 3 | Analytic table | `analysis/03` | IDC with race bootstrap, points by grid block, partial correlation, circuits, lap 1 | `kpi_*.csv`, figures `E2_*` | Slides "the finishing order follows the grid" |
| 4 | Analytic table | `notebooks/W2_project` | 15 checks, leakage audit (8 risks), 25 % subsample, season split (development 2014–2022, test 2023–2024) | `w2_validation_checks.csv`, `w2_leakage_audit.csv`, `w2_data_dictionary.csv`, figures `W2_*` | Data trust, split design |
| 5 | Analytic table + split | `notebooks/2_C2_model` | Logistic regression (median imputation, scaling, L2, C = 1, threshold 0.5) vs grid rule; validation 2018–2022; test 2023–2024 once | Figures `C2_*` | C2 results |
| 6 | Analytic table | `notebooks/final_project` | Walk-forward: each season predicted from earlier seasons only; final test; disagreements; robustness (same 919 test predictions as C2) | `final_key_numbers.json`, `final_validation_by_season.csv`, `final_validation_by_period.csv`, figures `FINAL_*` | Every number in the final slides |
| 7 | Saved summary results (step 6) | `notebooks/final_views` | Shared visual rules (`analysis/visual_system.py`) applied to the final views | Figures `analysis/figures/C3_*` | Final presentation charts |

## 5. Evaluation design (season by season)

Each season is predicted by a model trained on **all earlier seasons only** (walk-forward, expanding window):

| Predicted season | Trained on | Role |
|---|---|---|
| 2018 … 2022 | 2014 … the season before | Validation: model choices and threshold checked here |
| 2023 | 2014–2022 | Test, evaluated with the specification frozen |
| 2024 | 2014–2023 | Test, evaluated with the specification frozen |

Whole seasons are used, so no race is split. Preprocessing (median imputation, scaling) is fitted on the training seasons
of each step only, and an assertion checks that every training race happens before every predicted race. The C2 design
(one model trained on 2014–2022 for both test seasons) gives **identical test predictions** (919 of 919;
`notebooks/final_project.ipynb`, part 6). How this answers the C2 feedback is explained in `docs/decision_record.md`, part 1.

## 6. Data: source, scope and what is not included

- **Source:** *Formula 1 World Championship (1950–2024)*, Kaggle, user rohanrao, data from the Ergast API:
  https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020 — version with data up to the 2024 season,
  downloaded on 10 September 2026. Public data; no personal or confidential records.
- **Files used (12 of 14):** `races`, `results`, `qualifying`, `lap_times`, `pit_stops`, `sprint_results`,
  `constructor_standings`, `driver_standings`, `drivers`, `constructors`, `circuits`, `status`. Missing values are encoded as `\N`.
- **Scope used:** seasons 2014–2024, 227 races, 4,606 driver-race rows (one row = one driver in one race).
  Units: positions (rank), seconds and % for qualifying and pace gaps, points.
- **Where the data are described:** notebooks 01 (raw tables, coverage, quality issues), 02 (preparation and how each rule
  changed the rows) and W2 part 3 (data dictionary and checks).

**Not included (C3 rule: no data files).** The raw CSV files (`data/raw/`), the analytic tables
(`analytic_driver_race_2014_2024*.csv`), the row-level split, subsample and prediction files (`w2_split_assignment.csv`,
`w2_subsample_race_ids.csv`, `final_walk_forward_predictions.csv`, `w3/maximiliano/data/c2_test_predictions.csv`) and the
race-level table `race_level_kpis.csv`.

**Included: compact summary tables only** — cleaning log, data dictionaries, validation checks, leakage audit, KPI tables
by circuit and grid block (19 and 6 rows), validation F1 by season and period, `final_key_numbers.json`, and the small value
tables of the W3 views.

**To rebuild from scratch (optional):** download the Kaggle ZIP, copy the 12 CSV files into `data/raw/`, and run
01 → 02 → 03 → W2 → 2_C2_model → final_project → final_views with *Restart & Run All*. Each notebook finds the project
folder by itself. Seeds are fixed (2026).

## 7. Software

| Notebooks | Python | Main libraries |
|---|---|---|
| `analysis/01–03`, `W2_project`, `2_C2_model` | 3.13.7 | pandas 3.0.2, numpy 2.4.4, scipy 1.17.1, matplotlib 3.10.9, scikit-learn 1.9.1 |
| `final_project`, `w3/maximiliano` | 3.13.18 | pandas 3.0.5, numpy 2.5.3, scikit-learn 1.9.1, matplotlib 3.11.2 |
| `w3/benjamin`, `final_views` | 3.13.18 | pandas 3.0.5, numpy 2.5.3, matplotlib 3.11.2 (printed in the first code cell of `final_views`) |

`requirements.txt` lists the minimum versions. Jupyter (or VS Code) is only needed to re-run, not to read.

## 8. Decisions, feedback, contributions and AI use

- `docs/decision_record.md`: feedback from C1, W2 and C2 and what we did with it; decisions kept or changed; W3 design
  selection; contributions of each member; AI use.
- `docs/consistency_review.md`: 15 claims from earlier stages and their final, consistent version.

**AI use.** Claude (Anthropic) was used across the project to draft code and text, to review consistency against the briefs
and rubrics, and to organise this repository. We ran every notebook, checked the numbers against the executed outputs and
`final_key_numbers.json`, and can explain each decision. No AI is used during the presentation or defense. Each notebook
states its own AI use.
