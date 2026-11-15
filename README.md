# Circular Housing Renewal under Inflation

**Reproducible analysis of cost risk, carbon attribution, and grant portfolios for circular structural retrofits in Istanbul.**

## Overview

This repository accompanies a study comparing circular structural retrofits with demolition and reconstruction under construction-price uncertainty. It provides reproducible scripts for municipal renewal portfolio analysis in the context of Türkiye's Law No. 6306, covering financial cost, whole-life carbon, and grant-budget reliability.

The numerical results are conditional on the specified models and assumptions; they are not estimates from a representative sample of observed building projects.

## Quick start

### Core analysis and figures

Requires Python 3.11 or later. Clone the repository and install the core dependencies:

```bash
git clone https://github.com/aghiliarash/circular-housing-renewal.git
cd circular-housing-renewal
python -m pip install -r requirements.txt
python appendix_controls_v2.py
python generate_all_figures.py
```

The calculation script creates input series, analysis tables, a verification report, a claims register, and a run log. The figure script generates the publication figures. Generated files are written to `data/` and `outputs/`; they are not tracked by Git.

### Optional live geospatial validation

The optional geospatial workflow requires Conda, internet access, and the larger dependency set in `environment.yml`:

```bash
conda env create -f environment.yml
conda activate ual_istanbul
python run_ual_validation.py
```

The script may request data from OpenStreetMap/Overpass and other external services, and can use optional VoxCity and ZenSVI sources. Review the settings at the top of `run_ual_validation.py` before enabling downloads or changing cache and output locations.

## Repository contents

| Path | Description |
|---|---|
| `appendix_controls_v2.py` | Core calculations and CHK-1..7 verification suite |
| `generate_all_figures.py` | Offline publication-figure generation |
| `run_ual_validation.py` | Optional live geospatial validation |
| `config/study_spec.yaml` | Study parameters and design decisions |
| `requirements.txt` | Core pipeline dependencies |
| `environment.yml` | Conda environment for geospatial validation |
| `data/` | Generated macroeconomic and grid-emissions input series |
| `outputs/` | Generated tables, reports, verification results, and figures |

The scripts create generated data and output directories when run; generated files are excluded from version control.

## Methodological approach

### Cost and price uncertainty

The core pipeline calibrates macroeconomic series and compares deterministic replacement-cost accounts with paired stochastic draws. It exports cost-risk summaries and quartile comparisons for the modeled alternatives.

### Carbon accounting

The carbon module accounts for upfront and replacement embodied emissions and operational emissions under rapid, delayed, and static grid-decarbonization pathways. It exports the grid vectors and carbon ledger.

### Portfolio assessment

The portfolio module enumerates project subsets and calculates bundled grant costs, agency value, and feasibility probabilities under the configured grant-cost variation.

### Verification and figures

The calculation script runs seven reconciliation checks and writes their results to `outputs/verification_report.json`. The figure script produces the core study figures. The optional live validation script generates additional geospatial tables and figures when dependencies and data sources are available.

## Generated outputs

Core outputs include `outputs/verification_report.json`, `outputs/appendix_controls_v2_log.txt`, `outputs/JUPDD_Law6306_Claims_Register.csv`, analysis tables in `outputs/tables/`, and PDF/PNG figures in `outputs/figures/`. Generated input series are saved in `data/`. The optional geospatial workflow writes its tables, report, cache, and figures under `outputs/ual_validation/`.

## Interpretation and limitations

This repository provides a reproducible computational analysis, not a field-deployment tool. Results depend on the specified model structure, parameter values, and scenario assumptions. Geospatial checks rely on external data and may vary as those sources change or become unavailable. Interpret the comparisons within these assumptions; they are not causal estimates from observed outcomes.

## License

Code: MIT. Data and tables: CC-BY 4.0.
