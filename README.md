# Circular Housing Renewal under Inflation

**Reproducible analysis of cost risk, carbon attribution, and grant portfolios for circular structural retrofits in Istanbul**

## Overview

This repository contains a simulation and verification pipeline for comparing circular structural retrofits with demolition and reconstruction under construction-price uncertainty. The study focuses on municipal renewal portfolios in the context of Türkiye's Law No. 6306 and evaluates financial costs, whole-life carbon, and grant-budget reliability.

### Research scope

The analysis combines:

- Construction-price calibration and stochastic replacement-cost scenarios
- Deterministic and simulated life-cycle cost comparisons across building alternatives
- Whole-life carbon accounting, including grid-emissions pathways
- Chance-constrained municipal grant portfolio comparisons
- Sensitivity summaries and automated reconciliation checks
- Optional geospatial validation using OpenStreetMap and VoxCity-related data

The numerical results produced by the core pipeline are model outputs under the stated assumptions; they are not estimates from a representative sample of observed building projects.

## Quick start

### Core analysis and figures

The core pipeline runs locally without live geospatial data:

```bash
python -m pip install -r requirements.txt
python appendix_controls_v2.py
python generate_all_figures.py
```

The first script generates input series, analysis tables, a verification report, a claims register, and a run log. The second generates publication figures. Outputs are written to `data/` and `outputs/`.

### Optional live geospatial validation

The geospatial workflow requires internet access and the larger dependency set in `environment.yml`:

```bash
conda env create -f environment.yml
conda activate ual_istanbul
python run_ual_validation.py
```

This script may request data from OpenStreetMap/Overpass and other external services. It can also use optional VoxCity and ZenSVI sources. Review the configuration at the top of `run_ual_validation.py` before enabling optional downloads or changing cache and output settings.

## Repository contents

| File or directory | Purpose |
|---|---|
| `appendix_controls_v2.py` | Core calculation pipeline and CHK-1..7 verification suite |
| `generate_all_figures.py` | Offline generation of publication figures |
| `run_ual_validation.py` | Optional geospatial validation workflow |
| `config/study_spec.yaml` | Study parameters and documented design decisions |
| `requirements.txt` | Dependencies for the offline pipeline |
| `environment.yml` | Conda environment for geospatial validation |
| `data/` | Generated macroeconomic and grid-emissions series |
| `outputs/` | Generated tables, reports, verification results, and figures |

Generated data and outputs are not committed; the scripts create their directories when run.

## Methodological approach

### 1. Cost and price uncertainty

The core script calibrates macroeconomic series and compares deterministic replacement-cost accounts with paired stochastic draws. It exports cost-risk summaries and quartile comparisons for the alternatives specified in the pipeline.

### 2. Carbon accounting

The carbon module accounts for upfront and replacement embodied emissions and operational emissions under rapid, delayed, and static grid-decarbonization pathways. It exports the grid vectors and carbon ledger.

### 3. Portfolio assessment

The portfolio module enumerates project subsets and calculates bundled grant costs, agency value, and feasibility probabilities under the configured grant-cost variation.

### 4. Verification and figures

The calculation script runs seven reconciliation checks and writes their results to `outputs/verification_report.json`. Figure scripts produce the core study figures; the live validation script adds optional geospatial tables and figures when its dependencies and data sources are available.

## Generated outputs

The core analysis writes:

- `outputs/verification_report.json` and `outputs/appendix_controls_v2_log.txt`
- `outputs/JUPDD_Law6306_Claims_Register.csv`
- Tables in `outputs/tables/`, including cost-risk, deterministic-account, carbon-ledger, portfolio, and sensitivity summaries
- Figures in `outputs/figures/` in PDF and PNG formats
- Generated input series in `data/`

The optional geospatial workflow writes its additional tables, report, cache, and figures under `outputs/ual_validation/`.

## Interpretation and limitations

This repository is a reproducible computational analysis, not a field-deployment tool. Results depend on the specified model structure, parameter values, and scenario assumptions. Geospatial checks rely on external data and may vary as those sources change or become unavailable. Interpret all reported comparisons within these assumptions; they should not be read as causal estimates from observed outcomes.

## License

Code: MIT. Data and tables: CC-BY 4.0.
