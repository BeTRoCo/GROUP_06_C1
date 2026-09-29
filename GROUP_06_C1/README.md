# GROUP_06 · C1 — How much does the start determine the result in Formula 1? (2014–2024)

**Business Intelligence · IIB423T-1 · Universidad del Desarrollo**
Group 06: Maximiliano Sandoval Mosser and Benjamín Toloza Cossio · Instructor: Tomás Fontecilla Correa
Submission: C1 (first project delivery), version 1 · 29 September 2026

## Project idea
**Question.** How strong is the relationship between starting position and final position in the 2014–2024 Formula 1
World Championship, does it vary by circuit, and how much of it remains once the strength of the car is taken into account?

**Proposed user and decision (our proposal).** A team strategist deciding, circuit by circuit, how far to lean the single
(parc fermé) car setup towards one-lap qualifying pace or towards race pace.

**Selected line:** Candidate B from W1 (see chapter 2 of the C1 report).

## KPIs
| Role | KPI | Definition |
|---|---|---|
| Main | **IDC** (Grid Determinism Index) by circuit | Median per-race Spearman ρ(grid, final position), finishers only, with 95 % bootstrap CI |
| Support | **P(top 10 \| grid block)** | Share of starters in each grid block who finish in the points |
| Support | **Pole conversion** | Share of races won from P1 |
| Control | **Partial ρ** | Spearman(grid, final) controlling for the team's championship rank before the race |

**Why the IDC:** it answers the strategist's decision directly (how much the order is decided before the race), it uses the
whole finishing order (not only the winner), it is comparable across circuits, and it is ordinal-appropriate.

## Structure and run order
```
GROUP_06_C1/
├── README.md                     ← this file (entry point)
├── requirements.txt
├── analysis/
│   ├── 01_EDA_raw_dataset.ipynb           1) EDA of the raw Kaggle dataset (1950–2024)
│   ├── 02_cleaning_analytic_table.ipynb   2) Cleaning → analytic table 2014–2024
│   ├── 03_EDA_KPI.ipynb                   3) KPI-driven EDA (distributions, densities, correlations, KPIs)
│   └── figures/                           PNG figures written by the notebooks (E1_* = notebook 01, E2_* = notebook 03)
├── data/
│   ├── raw/          original CSVs from Kaggle (input, never modified)
│   └── processed/    outputs written by notebooks 02 and 03
├── report/           GROUP_06_C1_Report.docx (editable source) + GROUP_06_C1_Report.pdf (exported by the team)
└── presentation/     GROUP_06_C1_Slides.pdf (exported by the team from the slide deck)
```
Run the notebooks **in order 01 → 02 → 03** (03 reads the table written by 02). Open the whole `GROUP_06_C1` folder in
VS Code or Jupyter and use *Restart & Run All* in each notebook. Paths are project-relative: each notebook finds the project
folder by itself (it looks for `data/raw/races.csv`).

## Data
- **Source:** *Formula 1 World Championship (1950–2024)*, Kaggle, user rohanrao, data from the Ergast API.
  https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020 — downloaded on 10 September 2026.
- **Files used (12 of 14)** in `data/raw/`: `races`, `results`, `qualifying`, `lap_times`, `pit_stops`, `sprint_results`,
  `constructor_standings`, `driver_standings`, `drivers`, `constructors`, `circuits`, `status`.
  Not used: `seasons.csv` (only URLs) and `constructor_results.csv` (duplicates information in `results`).
- Missing values are encoded as `\N` in the original files.
- **To rebuild from scratch:** download the ZIP from the Kaggle page above, copy the 12 CSVs into `data/raw/` and run 01 → 02 → 03.

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

### Main cleaning decisions (details in notebook 02 and `cleaning_log.csv`)
1. Period 2014–2024 (one engine formula, one points scale, knockout qualifying, all tables complete).
2. Belgium 2021 excluded (1 lap behind the safety car: the order copies the grid).
3. `grid = 0` = pit-lane start → flagged, `grid` set to NaN (never "position 0").
4. `fastest_lap_rank = 0` = no timed lap → NaN.
5. Qualifying times parsed to seconds; gap to the fastest in % (> 7 % flagged).
6. Race pace = median lap excluding lap 1, pit in/out laps and laps > 107 % of the race median.
7. Team strength = constructor standings **after the previous round** (avoids leakage); round 1 uses previous season's final standings by team lineage.
8. 20 constructor ids grouped into 12 team lineages (e.g. Force India → Racing Point → Aston Martin).

## Software
Python 3.10+ with `pandas`, `numpy`, `scipy`, `matplotlib` (see `requirements.txt`). The submitted notebooks were executed by the
team with **Python 3.13.7**, pandas 3.0.2, numpy 2.4.4, scipy 1.17.1 and matplotlib 3.10.9; they use no version-specific features
and also run with pandas 2.2. Install: `pip install -r requirements.txt`. Seeds are fixed (`np.random.default_rng(2026)`) so
bootstrap results are reproducible.

## Execution status
All three notebooks run top to bottom with *Restart & Run All* (sequential execution counts, no errors). There are no unresolved
execution issues. Figures in `analysis/figures/` and tables in `data/processed/` are regenerated on every run.

## AI use
Claude (Anthropic, Cowork mode) was used to propose KPIs, draft the notebooks and review consistency. Every number reported in
the notebooks is produced by the executed code; interpretations were checked against the outputs.
