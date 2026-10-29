# GROUP_06 — How strongly is the starting position associated with the result in Formula 1? (2014–2024)

**Business Intelligence · IIB423T-1 · Universidad del Desarrollo**
Group 06: Maximiliano Sandoval Mosser and Benjamín Toloza Cossio · Instructor: Tomás Fontecilla Correa

| Submission | Date | Main artefact |
|---|---|---|
| W1 | September 2026 | Two candidate lines of inquiry (report submitted separately) |
| C1 | 29 September 2026 | `analysis/01–03` notebooks, `report/`, `presentation/` (kept unchanged) |
| **W2** | **29 October 2026** | **`notebooks/W2_project.ipynb`** + `data/processed/w2_*` + `analysis/figures/W2_*` |

## Project idea (unchanged since C1, wording corrected in W2)
**Question.** How strongly does the starting order agree with the finishing order in the 2014–2024 Formula 1 World
Championship, does that agreement differ by circuit, and how much of it remains when the team's pre-race strength is held fixed?

**Proposed user and decision (our proposal).** A team strategist who has to decide how much value to place on grid position
when preparing a race weekend. The data give an **input** to that decision (finishing outcomes *associated* with each grid slot);
they do not evaluate car setups, which are not recorded (see W2, part 5).

**Unit of observation.** One driver in one race (`raceId` + `driverId`): 4,606 rows, 227 races.

## KPIs
| Role | KPI | Definition |
|---|---|---|
| Main | **IDC** (grid–result agreement index) | Median per-race Spearman ρ(grid, final position), finishers only, with 95 % bootstrap CI |
| Support | **P(top 10 \| grid block)** | Share of starters in each grid block who finish in the points |
| Support | **Pole conversion** | Share of races won from P1 |
| Control | **Partial ρ** | Spearman(grid, final) conditional on the team's championship rank before the race |

In C1 the IDC was called "Grid *Determinism* Index". The formula is unchanged, but W2 reads it as an **association** (grid and
result agree), not as an effect of the grid, following the instructor's C1 feedback.

## W2 in short (what changed after C1)
- Feedback-to-action table with 11 entries (C1 written and oral feedback, plus self-audit).
- Conclusions corrected: Monaco is not distinguishable after correcting for 19 comparisons; lap 1 holds 10–13 % of all position
  changes when counted lap by lap (40.4 % in C1 was a net-snapshot upper bound); the setup recommendation by circuit is withdrawn.
- Redesigned figures (no piles at 0 without explanation, no KDE, % axes) and a "Y card" defining every outcome.
- 15 executable validation checks, data dictionary, row counts before/after (no row removed in W2).
- Target vs. observed vs. analytical population, two-plus coverage biases and a reproducible 25 % subsample of races.
- Leakage audit (8 risks) with decision times T0–T3.
- Chronological split: development 2014–2022, test 2023–2024; expanding-window validation by season; preprocessing fitted on
  training data only. No model is fitted in W2.

## Structure and run order
```
GROUP_06_C1/
├── README.md                     ← this file (entry point)
├── requirements.txt
├── analysis/
│   ├── 01_EDA_raw_dataset.ipynb           1) C1: EDA of the raw Kaggle dataset (1950–2024)
│   ├── 02_cleaning_analytic_table.ipynb   2) C1: cleaning → analytic table 2014–2024
│   ├── 03_EDA_KPI.ipynb                   3) C1: KPI-driven EDA
│   └── figures/                           PNGs written by the notebooks (E1_* = 01, E2_* = 03, W2_* = W2)
├── notebooks/
│   └── W2_project.ipynb                   4) W2: feedback, revised EDA, validation, sampling, leakage, split design
├── data/
│   ├── raw/          original CSVs from Kaggle (input, never modified)
│   └── processed/    outputs written by notebooks 02, 03 and W2
├── report/           C1 report (docx + pdf)
└── presentation/     C1 slides (pdf)
```
Run the notebooks **in order 01 → 02 → 03 → W2** (W2 reads the analytic table written by 02 and the raw CSVs). Open the whole
`GROUP_06_C1` folder in VS Code or Jupyter and use *Restart & Run All* in each notebook. Paths are project-relative: each
notebook finds the project folder by itself (it looks for `data/raw/races.csv`), so it works from `analysis/` and `notebooks/`.

## Data provenance
- **Source:** *Formula 1 World Championship (1950–2024)*, Kaggle, user rohanrao, data from the Ergast API.
  https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020 — downloaded on 10 September 2026.
  Public data; no personal or confidential records.
- **Files used (12 of 14)** in `data/raw/`: `races`, `results`, `qualifying`, `lap_times`, `pit_stops`, `sprint_results`,
  `constructor_standings`, `driver_standings`, `drivers`, `constructors`, `circuits`, `status`.
  Not used: `seasons.csv` (only URLs) and `constructor_results.csv` (duplicates information in `results`).
- Missing values are encoded as `\N` in the original files.
- The data end with the 2024 season (Ergast stopped updating); seasons from 2025 onwards are not covered.
- **To rebuild from scratch:** download the ZIP from the Kaggle page above, copy the 12 CSVs into `data/raw/` and run
  01 → 02 → 03 → W2.

### Processed outputs (`data/processed/`)
| File | Written by | Content |
|---|---|---|
| `analytic_driver_race_2014_2024.csv` | 02 | One row = one driver in one race (4,606 rows, 42 columns, 227 races) |
| `data_dictionary.csv` | 02 | Description, type and % missing of every column |
| `cleaning_log.csv` | 02 | Each cleaning rule, rows before/after and evidence |
| `race_level_kpis.csv` | 03 | One row per race: ρ, τ, volatility, pole win, DNF rate |
| `kpi_IDC_by_circuit.csv` | 03 | IDC with bootstrap CI per circuit (≥ 5 races) |
| `kpi_P_top10_by_grid_block.csv` | 03 | P(top 10), P(podium), P(win), DNF rate by grid block |
| `kpi_pole_conversion_by_circuit.csv` | 03 | Pole conversion with Wilson CI per circuit |
| `kpi_summary_by_circuit.csv` | 03 | Dashboard-ready table joining all per-circuit KPIs |
| `analytic_driver_race_2014_2024_w2.csv` | W2 | C1 table + `circuit_prior_races`, `starters_in_race`, `flag_status_anomaly` (4,606 rows, 45 columns) |
| `w2_data_dictionary.csv` | W2 | Expected type, acceptable values, meaning of missing values, decision time, role |
| `w2_validation_checks.csv` | W2 | 15 validation checks: rule, rows checked, violations, result, action |
| `w2_leakage_audit.csv` | W2 | 8 leakage risks: status, evidence, consequence, mitigation |
| `w2_split_assignment.csv` | W2 | `raceId`, `driverId`, `year`, `split` (development / test) |
| `w2_subsample_race_ids.csv` | W2 | Race ids of the reproducible 25 % subsample (seed 2026) |

### Main cleaning decisions (details in notebook 02, `cleaning_log.csv` and W2 part 3)
1. Period 2014–2024 (one engine formula, one points scale, knockout qualifying, all tables complete).
2. Belgium 2021 excluded (1 lap behind the safety car: the order copies the grid).
3. `grid = 0` = pit-lane start → flagged, `grid` set to NaN (never "position 0").
4. `fastest_lap_rank = 0` = no timed lap → NaN.
5. Qualifying times parsed to seconds; gap to the fastest in % (> 7 % flagged).
6. Race pace = median lap excluding lap 1, pit in/out laps and laps > 107 % of the race median.
7. Team strength = constructor standings **after the previous round** (avoids leakage); round 1 uses previous season's final standings by team lineage.
8. 20 constructor ids grouped into 12 team lineages (e.g. Force India → Racing Point → Aston Martin).
9. **W2:** `circuit_prior_races` replaces `circuit_races` for any predictive use (the C1 column counted future seasons).
10. **W2:** two rows flagged and kept: Bianchi, Australia 2014 (took the flag but < 90 % distance, not classified) and Bottas,
    Belgium 2015 (classified 9th with a "Power Unit" status).

### Train / validation / test design (W2 part 6)
- **Test:** seasons 2023–2024 (46 races, 919 rows, 20 %). Not used to choose features, thresholds, imputation or models.
- **Development:** seasons 2014–2022 (181 races, 3,687 rows), with expanding-window validation by season (validate 2018 … 2022).
- Split by whole seasons, so no race is shared between subsets. Preprocessing (median imputation, one-hot encoding) is fitted on
  training data only.

## Software
Python 3.10+ with `pandas`, `numpy`, `scipy`, `matplotlib` and, for W2, `scikit-learn` (see `requirements.txt`).
Install: `pip install -r requirements.txt`. The versions used are printed in the first code cell of each notebook. Seeds are
fixed (`np.random.default_rng(2026)`), so bootstrap and sampling results are reproducible.

## Execution status
All notebooks run top to bottom with *Restart & Run All* (sequential execution counts, no errors). Figures in
`analysis/figures/` and tables in `data/processed/` are regenerated on every run.

## AI use
Claude (Anthropic, Cowork mode) was used in C1 and W2 to propose KPIs and structure, draft notebook code and text, and review
consistency against the briefs and the instructor's feedback. Every number reported in the notebooks is produced by the
executed code; the team verified interpretations against the outputs. The W2 disclosure is in part 8 of `W2_project.ipynb`.
