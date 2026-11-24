# Consistency review for the final presentation

This file lists the checks made before the final presentation, so that every number and claim tells the same story
across W1, C1, W2, C2 and W3. All final values come from `notebooks/final_project.ipynb`
(`data/processed/final_key_numbers.json`).

| # | Topic | Earlier wording or design | Final, consistent version | Evidence |
|---|---|---|---|---|
| 1 | Evaluation years | C2 trained one model on 2014–2022 and applied it to both 2023 and 2024 (2024 predicted two seasons ahead) | Every season 2018–2024 is predicted from all earlier seasons only; 2018–2022 validation, 2023–2024 test | final part 5; identical test predictions (919 of 919), part 6 |
| 2 | Training across regulation periods | Training mixes 2014–2021 and 2022 rules; test is all 2022 rules | Results reported by period; training only on 2022 rules or on the last three seasons does not do better; the regime change is a stated limit | final parts 5.1 and 6 |
| 3 | Test seasons seen in EDA | Not stated in the C2 slides | The test seasons were explored descriptively in C1; no modelling choice (inputs, threshold, model) was made with them | final part 6; W2 part 6.5 |
| 4 | Interval of the test F1 gain | "almost includes zero" (C2 notebook and script) | The 95 % race-bootstrap interval (−0.001 to +0.047) **includes** zero: the gain is small and uncertain | final part 5.2 |
| 5 | 2023 vs 2024 | "in 2023–2024 the grid order held more" (C2 script) | 2023 had the lowest grid–result agreement (IDC 0.72), so the grid rule was weakest and the model helped; in 2024 (IDC 0.86) the grid rule was hard to beat | final parts 3.1 and 5.2 |
| 6 | Range of the per-race correlation | "IDC from 0 to 1" | Spearman ranges from −1 to +1 (one race is below zero); the IDC is the median, 0.811 | final part 3.1 |
| 7 | IDC interval | 0.79–0.83 (C1) and 0.789–0.835 (W2), with different numbers of resamples | One computation: 95 % CI 0.792–0.835 (5,000 race resamples, seed 2026) | final part 3.1 |
| 8 | Three different correlations | 0.81, 0.77 and 0.50 shown together in C1 | 0.81 = IDC (median of per-race values); 0.77 = pooled over all finishers; 0.50 = pooled, holding team rank fixed | final parts 3.1 and 3.3 |
| 9 | Causal language | "the start determines", "a large part is the car", "each slot lost costs" (C1) | Association throughout; the partial correlation is consistent with car strength acting on both, not a measured effect | final part 3.3 |
| 10 | Circuits and Monaco | "only Monaco is clearly above the average" (C1) | No circuit differs after correcting for 19 comparisons (Holm); Monaco Holm p = 0.38 | final part 3.4 |
| 11 | Lap 1 | "40 % of position changes happen on lap 1" (C1, net snapshots) | 10–13 % counted lap by lap; lap 1 is the most intense lap (6.5× a later lap) | final part 3.5 |
| 12 | Exact zeros | Piles at 0 in C1 figures | 16.8 % of finishers end exactly in their grid slot (1.5× the neighbours), mostly at the front (57 % of finishers from pole vs 6 % from P16+): a boundary effect; the IDC is not affected | final part 3.6 |
| 13 | Points by grid block | Denominator not always stated | All starters with a grid slot, retirements included | final part 3.2 |
| 14 | Disagreements with the grid rule | "the model is right in 61 %" | 62 of 102, with a race-bootstrap interval of 50–72 %: no significance claim, consistent with the uncertain overall gain | final part 5.3 |
| 15 | Setup recommendation | "lean the setup toward qualifying, circuit by circuit" (C1) | Withdrawn: the setup is fixed before the grid exists and is not recorded; the evidence is a planning input | W2 part 5 |
