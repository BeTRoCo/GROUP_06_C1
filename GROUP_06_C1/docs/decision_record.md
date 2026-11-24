# Decision record · Group 06 (W1 → C1 → W2 → C2 → W3 → C3)

This file explains how the study developed: what feedback we received and what we did with it (part 1), which decisions we
changed or kept and why (part 2), how we chose the final visual design from our two individual W3 works (part 3), who did
what (part 4) and how we used AI (part 5). Each row points to the notebook part where the evidence is saved.
The wording corrections of earlier claims are listed in `docs/consistency_review.md`.

---

## 1. Feedback received and what we did with it

| Stage | Feedback (as received) | What we did | Where to check |
|---|---|---|---|
| **C1** (oral, at the C1 defense) | Avoid conclusions based on correlation (correlation is not causation) | All relationships are described as associations; the partial correlation (0.77 → 0.50) is read as "consistent with car strength acting on both", not as a measured effect | W2 part 2.5; final part 3.3; consistency review rows 8–9 |
| **C1** (oral) | Explain or avoid charts that pile up at 0 | Audit of the zero peak: 16.8 % of finishers end exactly in their grid slot, mostly at the front (boundary effect); figures redesigned | W2 part 2.4; final part 3.6; review row 12 |
| **C1** (oral) | Be clearer about the Y values of the different correlations | A "Y card" for each analysis; 0.81 (IDC, median per race), 0.77 (pooled) and 0.50 (pooled, team rank fixed) separated | W2 parts 2.1–2.2; review row 8 |
| **C1** (written, 83/100) | A high IDC is an association, not an effect of the grid; the partial correlation does not identify the causal effect of the car | Causal wording removed everywhere ("the start determines", "each slot lost costs") | W2 parts 1.1, 2.5; review row 9 |
| **C1** (written) | The setup recommendation by circuit is not identified by the data | Recommendation withdrawn: the setup is fixed before the grid exists and is not recorded; the evidence is now a planning input | W2 part 5; review row 15 |
| **C1** (written) | Monaco and the 40.4 % first-lap share need caution | Monaco: 19 circuits compared with a Holm correction, none differs (Monaco Holm p = 0.38). Lap 1: changes counted lap by lap, 10–13 % instead of 40 % | W2 parts 2.6–2.7; final parts 3.4–3.5; review rows 10–11 |
| **W2** (100/100) | Keep whole races in each partition | Split by season; every race lies in one subset; checked by assertions | C2 parts 2 and 4; final part 5 |
| **W2** | Use only information available before the start | Four inputs known when the grid is published; in-race and post-race variables blocked by an assertion | C2 part 3; final part 5; W2 leakage audit |
| **W2** | Evaluate results by regulation period | Validation reported for 2014–2021 rules and 2022 rules; test seasons are all 2022 rules | C2 part 4; final part 5.1 |
| **W2** | Avoid causal readings of rank relationships | Coefficients described as associations used for prediction | C2 part 6; final part 5.3 |
| **C2** (oral, at the C2 defense; confirmed by both members) | The instructor questioned whether the seasons used to evaluate the model had also been used to train it ("the model steps on its own tail"), and pointed out that the test seasons looked wrongly labelled on our split slide | See the detailed answer below | Final parts 5 and 6; slide "A fair test" |
| **W3** | No feedback was available when this version was frozen | — | — |

### How we answered the C2 feedback

**What caused the doubt.** Our C2 split slide showed one bar "Development 2014–2022" with the validation seasons 2018–2022
shaded inside it, and the final model was refitted on 2014–2022 (which includes the validation seasons) without saying so. A
reader could not see that each validation season was predicted by a model trained only on earlier seasons, so it looked as if
we evaluated on seasons we had trained on. The method was correct, but our evidence did not show it.

**What we changed or added.**
1. **One row per predicted season.** The final notebook prints, for every season from 2018 to 2024, the seasons it was trained
   on and its role (validation or test), and the slide shows the same grid. An assertion checks that every training race
   happens before every predicted race and that no race is in both sets (final part 5).
2. **Walk-forward test.** 2024 is now predicted by a model trained on 2014–2023, as a strategist would do. This changes none
   of the 919 test predictions of C2, so every C2 test result still holds (final part 6).
3. **What the test seasons were used for.** They were explored descriptively in the C1 EDA (for example the IDC by season), but
   no input, threshold, cleaning rule or model was chosen with them (W2 part 6.5; final part 6).
4. **Inputs from the same season.** The team rank uses only the standings after the previous round, never after the same
   race (W2 leakage risk R3; check C14: 0 mismatches).
5. **A view that keeps validation and test apart.** The final view of F1 by season groups the rows into "validation, 2014–2021
   rules", "validation, 2022 rules" and "test, evaluated once" (part 3 below).

---

## 2. Decision log: what we kept and what we changed

| Stage | Decision | Alternative considered | Reason and evidence | Kept or changed | Where |
|---|---|---|---|---|---|
| W1 | Study grid → result (line B) | Pit-stop efficiency (line A) | The recorded pit time is the whole pit-lane trip; the circuit explains 38 % of its variation (η² = 0.378) | Kept | Final part 1 |
| C1 | Seasons 2014–2024 | Whole history; 2011–2024 | One engine formula, one points scale, every table complete (coverage heatmap) | Kept | NB01 parts 3–4 |
| C1 | One row = one driver in one race | One row per race | The question is about each driver's start and result | Kept | NB02; README |
| C1 | IDC = median per-race Spearman with race bootstrap | Pooled correlation; pole conversion as main KPI | Ranks, skewed per-race values (Shapiro–Wilk p < 0.001); races are the independent units | Kept | NB03 parts 2 and 4 |
| C1 | Exclude Belgium 2021 (1 lap behind the safety car) | Keep it | Its order copies the grid by construction (−20 rows) | Kept | NB02 part 3; cleaning log |
| C1 | Grid 0 = pit-lane start, flagged | Treat as pole or delete | It is not a grid position (77 rows flagged, none deleted) | Kept | NB02 part 4 |
| C1 | Team rank after the previous round | Standings after the same race | The same-race rank already contains the result (leakage) | Kept | NB02 part 7; W2 R3 |
| C1 → W2 | Association wording; setup recommendation withdrawn; lap 1 and Monaco re-measured | Keep the C1 claims | C1 feedback (part 1) and new evidence | Changed | Review rows 9–11, 15 |
| W2 | Split by season: development 2014–2022, test 2023–2024 | Random 80/20; random races | Matches the use (predict the next races), keeps races whole, exposes the 2022 rule change | Kept | W2 part 6.1 |
| W2 | Expanding-window validation 2018–2022 | One validation season | Five checks across two regulation periods | Kept | W2 part 6.2 |
| C2 | Logistic regression, 4 pre-start inputs | Trees or ensembles | Binary target, explainable probability, enough for a first model; a simple model can be fully assessed | Kept | C2 part 4 |
| C2 | Reference = grid rule (top 10 on the grid score) | Majority class | It is what a strategist uses without a model, so it is the fair comparison | Kept | C2 part 4 |
| C2 | Threshold 0.5, checked on validation only | 0.35 (slightly higher validation F1) | At 0.5 the model predicts 48 % scorers vs 50 % real (about 10 per race); lower thresholds predict 11–12 scorers per race and over-promise points | Kept | Final part 5.1 |
| Final | Walk-forward evaluation (2024 trained with 2023) | C2 design (one model for both test seasons) | Matches how the model would be used; identical test predictions (919 of 919) | Changed | Final parts 5–6 |
| Final | Train on all earlier seasons | Only 2022-rules seasons; last three seasons | Neither alternative does better (2023: 0.795 and 0.793 vs 0.798; 2024: 0.818 and 0.822 vs 0.826); checked after freezing, not used to choose | Kept | Final part 6 |
| Final | Report the gain with its interval: +0.022 (−0.001 to +0.047) | "Almost includes zero" (C2) | The interval includes zero, so the gain is small and uncertain | Changed (wording) | Final part 5.2; review row 4 |
| C3 | Remove all data files; keep compact summaries | Keep `data/` | C3 rule; the notebooks keep their saved outputs | Changed | README part 6 |
| C3 | One final visual system built from both W3 works | Use one W3 only | Part 3 | Changed | Part 3; `notebooks/final_views.ipynb` |

---

## 3. W3 design selection and the final visual system

Both members did W3 individually from the same C2 results. Both chose the same three questions — *when* is the model
better, *what kind* of errors does it make, *where* does it change the prediction — and almost the same palette. The final
system keeps what both agreed on and takes, for each view, the version that best supports the task of the strategist.

| View (task) | Benjamín's W3 | Maximiliano's W3 | Selected for C3 and why |
|---|---|---|---|
| 1 · When: compare F1 by season, summarize by period | Dumbbell with validation **and** test seasons, grouped by stage and rules; "model − rule" column | Dumbbell with validation seasons; 2022-rules band | **Benjamín's**: it keeps validation and test apart with group headers, which answers the C2 feedback, and shows both test seasons |
| 2 · What kind: compare error counts | Four outcomes (FP, FN, TP, TN), errors highlighted | False positives and false negatives only; grid rule hatched | **Maximiliano's**: two error types are what the strategist needs; the hatch keeps the grid rule readable without color |
| 3 · Where: identify the disagreements, locate who was right | Stacked bars with count, share and the 102-of-919 context | Stacked bars with count and share, grid rule hatched | **Benjamín's layout** with Maximiliano's hatch: it adds the denominator (102 of 919 test rows) |

**Final rules (applied to every final view).**
- **Color:** blue `#2a78d6` = model; grey `#8a8984` = grid rule; orange `#eb6834` = highlight of the one value or subset the
  task points to. Descriptive charts that are not a model comparison use neutral ink, never the model blue.
- **Without color:** the grid rule is always hollow (markers) or hatched (bars), and every series has a direct text label.
- **Scales:** counts drawn as bars start at 0; F1 is drawn with dots on a zoomed common scale, and the note says so.
- **Numbers and labels:** F1 with three decimals, counts as whole rows, shares with their denominator; direct labels instead of
  legends; "model" and "grid rule" are the only names used for the two approaches.
- **Text:** the slide title states the finding; the subtitle states the task, period and *n*.
- **Where it is implemented:** `analysis/visual_system.py` (shared settings and helper functions) used by
  `notebooks/final_views.ipynb`, which draws the final views from saved summary results. The two W3 notebooks are kept
  unchanged in `w3/` as individual work.
- **Necessary differences:** the C1 and W2 exploratory figures were made before the visual system and keep their own style; they
  are not compared with the model views. View 1 uses a zoomed F1 axis (dots), while Views 2 and 3 use zero-based counts (bars),
  because they show different measures for different tasks.

---

## 4. Contributions

Both members took the main decisions together in shared sessions, reviewed each other's parts and can explain every notebook.

| Stage | Maximiliano Sandoval | Benjamín Toloza |
|---|---|---|
| W1 | Both: chose the two lines of inquiry, inspected the data and wrote the report together | |
| C1 | Framing and context adaptation, documentary support, seven-step map; EDA of the raw dataset (notebook 01) and Five Cs; report chapters 1–3 and 4.1–4.2; slides 1–7 | Cleaning and analytic table (notebook 02); KPI-driven EDA (notebook 03: IDC, support and control KPIs); ran the three notebooks end to end; report chapters 4.3–7; slides 8–16 |
| W2 | Reviewed the notebook against the brief and the C1 feedback table; checked the release | Led `W2_project.ipynb`: feedback-to-action table, validation checks, sampling, leakage audit, split design |
| C2 | Reviewed the model notebook and the brief; presented and defended | Built `2_C2_model.ipynb` (model, reference, validation, test), the brief and the slides; presented and defended |
| W3 | Individual W3 (`w3/maximiliano/`) | Individual W3 (`w3/benjamin/`) |
| C3 | `final_project.ipynb` (walk-forward evaluation, robustness, key numbers), `consistency_review.md`, first version of the final slides and script | Repository clean-up for the C3 rules, README and this decision record, final visual system from both W3 works (`final_views.ipynb`), presentation reorganised for the external and internal audiences |

**Individual reflections**

**Maximiliano Sandoval:** "In this last stage my main work was the walk-forward check and the consistency review. Going back
over every number showed me that our C2 method was right but our slide made it look wrong: the instructor saw the test seasons
inside the training bar and thought we were evaluating on data we had already used. I learned that the evidence has to show the
method, not only use it. A question I still have is whether the team's rank before the race is a good enough measure of car
strength, especially when the rules change, as they will in 2026."

**Benjamín Toloza:** "My main parts were the cleaning, the validation design in W2 and the first model in C2, and for C3 putting
the repository and the visual system together. The thing that changed my view most was reporting the gain with its interval:
+0.022 sounds like an improvement, but the interval includes zero, so the honest message is 'slightly better and uncertain'.
From W3 I learned that a correct number can still be read wrongly if the chart is not designed for the task, like our bars cut
at 0.70. I am still not sure if the gain would hold with more test seasons or under the 2026 rules."

---

## 5. AI use

| Tool | What we used it for | How we checked it |
|---|---|---|
| Claude (Anthropic), Cowork mode | Drafting code for the notebooks and figures; first drafts of explanations, slides and scripts in English; reviewing the work against each brief and rubric; organising the repository for C3 | We ran every notebook, used assertions for the key checks, compared every number in the slides with the executed outputs and `final_key_numbers.json`, and reviewed each decision so that we can explain it without help |

No AI is used during the presentation or the defense. Each notebook also states its own AI use.
