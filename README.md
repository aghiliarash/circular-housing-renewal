# Circular Housing Renewal under Inflation: Cost Risk, Carbon Attribution, and Grant Portfolios
**Operationalizing Stochastic Life-Cycle Costing and Geospatial Portfolio Selection in High-Inflation Urban Renewal**  
`License: MIT` `Python 3.10+` `NumPy` `SciPy` `GeoPandas` `OSMnx` `Reproducible`

---

## 📋 Overview
This repository provides a complete simulation-calibrated analytical pipeline for evaluating circular housing renewal under extreme macroeconomic volatility. The study couples stochastic life-cycle costing (LCC), dynamic whole-life carbon (WLC) accounting, and chance-constrained portfolio selection to govern multi-site urban transformation programs in Istanbul (Turkish Law No. 6306).

### The Challenge
Transitioning from virgin-material reconstruction to circular structural retrofitting requires higher upfront capital expenditure at contract award. Recovering this investment depends on avoiding future replacement outlays over a multi-decade horizon. In economies experiencing high construction inflation (+77.07% real drift), deterministic appraisals obscure upper-tail expenditure risk, while traditional carbon assessments conflate operational electrification with physical material reuse.

### Key Innovation
A hybrid numerical and geospatial evaluation architecture combining:

- **Stochastic Price Dynamics:** Mean-reverting Ornstein–Uhlenbeck (O–U) models capturing real construction drift and virgin-salvage market correlations.
- **Symmetric Carbon Attribution:** Strict boundary separation between 30-year grid-dynamic operational emissions, invariant embodied circularity, and Year-60 end-of-life credits.
- **Chance-Constrained Governance:** Lognormal portfolio optimization assessing multi-site procurement feasibility beneath statutory municipal grant ceilings.
- **Empirical Geospatial Validation:** Live 3D morphology (VoxCity) and arterial road-network routing (OSMnx) to benchmark theoretical building archetypes and spatial bundling assumptions.

---

## 🚀 Quick Start

### Installation

```bash

git clone https://github.com/aghiliarash/circular-housing-renewal-inflation.git
cd circular-housing-renewal-inflation
```

### Dependencies

```bash
The pipeline is divided into Core Analytics (fast, offline) and Geospatial Validation (requires internet and spatial libraries).
1. Core Analytics (Base Environment)
Bash
pip install numpy scipy pandas matplotlib pyyaml
2. Geospatial Validation (Conda Environment Recommended)
conda env create -f environment.yml
conda activate ual_istanbul
Run the Pipelines
Execute Core Analytics & Figure Generation:
Bash
python appendix_controls_v2.py
python generate_all_figures.py
Execute Live Geospatial Calibration:
python run_ual_validation.py
All outputs map to the outputs/tables/ and outputs/figures/ directories.
```

## 📁 Repository Structure

File / Directory	Purpose
appendix_controls_v2.py	Master script — Complete 8-module reproducible core pipeline and verification suite (CHK-1 to CHK-7).
run_ual_validation.py	Geospatial script — Live empirical extraction using VoxCity, GBMI, and OSMnx.
generate_all_figures.py	Plotting script — Renders 300-dpi publication-ready graphics.
config/study_spec.yaml	Single source of truth for all design decisions, inputs, and accounting parameters.
data/	Stores published macroeconomic series and grid emission vectors.
outputs/	Auto-generated target directory for all CSV tables, logs, and figures.

## 🔧 Methodological Approach

### 1. **Stochastic Price-Path Generation (O–U Process)**

Real annual escalation rates for virgin materials, salvaged components, and energy tariffs evolve as correlated continuous-time mean-reverting diffusion processes. In the 40,000-draw Monte Carlo simulation, rates update via exact discrete annual recursion following a two-year tender price lock-in:

r_m(t) = μ_m + exp(-θ_m)[r_m(t-1) - μ_m] + ε_m(t)

where ε_m(t) ~ N(0, [σ_m² / 2θ_m][1 - exp(-2θ_m)])

### 2. **Whole-Life Carbon (Boundary S)**

The primary physical ledger sums undiscounted emissions across upfront embodied modules (A1–A5), 30-year replacements (B4), and 30-year operational energy (B6). Monetized carbon at $75/tCO₂e applies study-specific discounting exclusively to monetary present values. Year-60 demolition and beyond-boundary reuse credits are sequestered into a separate embodied-only reconciliation memorandum.
3. Chance-Constrained Portfolio Selection
The municipal agency selects a non-empty subset S from 15 candidate portfolios subject to a probabilistic reliability constraint under lognormal cost uncertainty (CV=3.0%):
P[Cost(S) ≤ B_max] = Φ( [ln(B_max / μ_Cost(S)) + 0.5 σ_log²] / σ_log ) ≥ 0.950
4. Open Geospatial Validation
To ensure the 80.0 m²/unit stylized archetype matches empirical urban form, the run_ual_validation.py script queries 3D footprints across four Istanbul Law No. 6306 districts, establishing empirical envelope distributions and testing multi-site framework bundling against drivable arterial road distances (OSMnx).

## 📊 Key Features

### Integrated Appraisal
Couples **Tier I** direct budget, **Tier II** financial LCC, and **Tier III** societal LCC within a single analytical boundary.

### Global Sensitivity Design
**Saltelli-Jansen estimator** across **3.93 million evaluations** separates:

- Parametric uncertainty (Sobol indices)
- Intrinsic Brownian path dispersion (Nested Law of Total Variance)

### Interpretability-First Architecture

| Feature | Description |
|---------|-------------|
| ✅ Transparent Design | All cost build-ups, carbon attribution steps, and stochastic boundaries documented as strict accounting identities |
| ✅ Automated Verification | CHK-1 to CHK-7 validate comparator symmetry, quartile reconciliation, and exact normal-inverse probabilities |
| ✅ Reproducible | Fixed random seeds (`20260410`) and deterministic YAML configurations |

---

## ⚠️ Important Notes

### What This Is

- ✅ A **parameterized numerical scenario experiment** coupling stochastic economics and geospatial portfolio governance
- ✅ A **computational transparency exercise** establishing conditional comparative benchmarks for circular housing renewal
- ✅ A **reproducible framework** demonstrating how spatial logistics and inflation exposure shift municipal grant feasibility

### What This Is NOT

- ❌ An ex-post econometric evaluation of completed construction contracts
- ❌ A substitute for physical concrete core testing or certified secondary-material market transaction logs
- ❌ An operational tool ready for blind deployment without local price, structural, and energy grid recalibration

### Proper Use

All inferences remain **strictly bounded to the calibrated simulation architecture**. Parameter variance rankings and tail-exceedance probabilities represent computational relationships within the specified baseline (Istanbul 2016–2025 macro regime), requiring localized empirical updates prior to field tendering.

---

## 📈 Expected Outputs

| File | Description |
|------|-------------|
| `Table_4a_risk.csv` | Stochastic budget metrics |
| `Table_4b_quartiles.csv` | Quartile-stratified exceedance rates |
| `Table_5_deterministic_accounts.csv` | Baseline Tier I, II, and III cash flows |
| `Table_6_carbon_ledger.csv` | Physical and monetized Boundary S carbon attribution |
| `Table_7_portfolios.csv` | Feasibility thresholds and subset ranking variations |
| `Table_S13_sobol.csv` | First- and total-order parameter sensitivity indices |
| `Table_S17_geospatial.csv` | Empirical morphology (VoxCity) and network-adjusted grant caps (OSMnx) |
| `appendix_controls_v2_log.txt` | Automated Pass/Fail verification log |
| `Figure_*.png/.pdf` | Publication-ready, 300-dpi graphics |

---

## 🔬 Calibration Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| `N_DRAWS` | 40,000 | Baseline Monte Carlo sample size |
| `SEED` | 20260410 | Ensures exact reproduction of all quartiles and standard errors |
| Virgin Drift (μ_v) | 6.55%/yr | Calibrated to 2016–2025 TRY-real differential construction escalation |
| Energy Drift (μ_e) | 3.50%/yr | Calibrated to 2016–2025 residential EPDK retail tariffs |
| Grant CV | 3.0% | Lognormal uncertainty surrounding municipal tender execution |
| Feasibility Target | 95.0% | Statutory reliability threshold for multi-site grant coverage |

---

## 📚 Citation
If you utilize this pipeline or framework, please cite the associated manuscript:

```bibtex
@article{your_name_2026,
  author = {[Author Names]},
  title = {Circular Housing Renewal under Inflation: Cost Risk, Carbon Attribution, and Grant Portfolios},
  year = {2026},
  journal = {Journal of Urban Planning and Development (ASCE)},
  url = {https://github.com/[your-username]/circular-housing-renewal-inflation}
}
```
## 📜 License

MIT License. free for academic and research use with attribution. See [LICENSE](LICENSE) for full text.
---

## ✉️ Contact & Contributing

Questions or feedback? Please open a GitHub issue.

**Last Updated:** 2026  
**Maintainer:** aghiliarash

