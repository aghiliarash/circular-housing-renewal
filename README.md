# Circular Housing Renewal under Inflation

Companion code for the ASCE *Journal of Urban Planning and Development* study on cost risk, carbon attribution, and grant portfolios for circular structural retrofits versus demolition and reconstruction in Istanbul.

## Core pipeline

The deterministic and stochastic analyses and publication figures run offline:

```bash
python -m pip install -r requirements.txt
python appendix_controls_v2.py
python generate_all_figures.py
```

The calculation pipeline writes its inputs to `data/` and tables, figures, a verification report, claims register, and execution log to `outputs/`. Figure generation also writes to `outputs/figures/`.

## Optional live geospatial validation

The geospatial workflow requires internet access and the additional dependencies in `environment.yml`:

```bash
conda env create -f environment.yml
conda activate ual_istanbul
python run_ual_validation.py
```

This workflow uses OpenStreetMap/Overpass and optional VoxCity and ZenSVI data sources. ZenSVI street-view screening and cached corridor reuse are controlled by settings at the top of `run_ual_validation.py`. See that script before enabling optional downloads or changing the default output/cache location.

## Repository layout

```text
config/study_spec.yaml       Study parameters and design decisions
appendix_controls_v2.py      Calculation pipeline and CHK-1..7 verification
generate_all_figures.py      Offline publication-figure generation
run_ual_validation.py        Optional live geospatial validation
data/                        Generated macro and grid-vector series
outputs/                     Generated tables, reports, and figures
```

Generated data and outputs are not checked in; the scripts create their output directories when run.

## License

Code: MIT. Data and tables: CC-BY 4.0.
