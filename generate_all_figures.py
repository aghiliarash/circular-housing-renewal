"""
generate_all_figures.py
Generates 300-dpi publication graphics for ASCE Journal of Urban Planning and Development:
  - Figure_1: Operational 6-Gate Municipal Decision Sequence & 4-Stage Model Schematic
  - Figure_2: 30-Year Direct Capital & Replacement Budget Probability Densities
  - Figure_3: Global Sensitivity Tornado Chart (Sobol Indices) & Nested Variance Share
  - Figure_4: Boundary S Whole-Life Carbon Stacked Bar Comparison
  - Figure_5: Multi-Project Portfolio Frontier & 95.0% Feasibility Thresholds
  - Figure_S2: Empirical OSMnx Arterial Road-Network Grant Caps & Feasibility
"""

import math
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde, norm

FIG_DIR = Path("./outputs/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10})


def make_figure1_framework():
    fig, ax = plt.subplots(figsize=(12.5, 5.2), dpi=300)
    ax.set_xlim(0, 12.5)
    ax.set_ylim(0, 5.2)
    ax.axis("off")

    ax.text(6.25, 4.92, "Operational Six-Gate Municipal Renewal Sequence (Top) & Four-Stage Analytical Architecture (Bottom)",
            ha="center", va="center", fontsize=11, fontweight="bold")

    gates = [
        ("Gate 1\nStructural &\nSeismic Parity", "TBDY (2018)\nRC Frame Audit"),
        ("Gate 2\nYear-0 Turnkey\nAffordability", "CapEx + Bundling\n(-$656/unit)"),
        ("Gate 3\n30-Yr Budget &\nTail Exposure", "40,000 CRN Draws\nCVaR_95 & Regret"),
        ("Gate 4\nMatched Carbon\nAttribution", "30-Yr Boundary S\nvs. Yr-60 Memo"),
        ("Gate 5\nGrant-Budget\nReliability", "P(Cost <= B_max)\n>= 95.0% (CV=3%)"),
        ("Gate 6\nValuation-Based\nSelection", "Unit Scaling vs.\nAgency Weights"),
    ]
    for i, (title, sub) in enumerate(gates):
        x0 = 0.25 + i * 2.02
        rect = mpatches.FancyBboxPatch((x0, 2.85), 1.80, 1.70, boxstyle="round,pad=0.08",
                                       facecolor="#EBF3F9", edgecolor="#2B5C8F", linewidth=1.4)
        ax.add_patch(rect)
        ax.text(x0 + 0.90, 3.98, title, ha="center", va="center", fontsize=8.8, fontweight="bold", color="#1B3B5C")
        ax.text(x0 + 0.90, 3.22, sub, ha="center", va="center", fontsize=7.8, color="#333333")
        if i < 5:
            ax.annotate("", xy=(x0 + 2.00, 3.70), xytext=(x0 + 1.82, 3.70),
                        arrowprops=dict(arrowstyle="->", color="#2B5C8F", lw=1.5))

    stages = [
        ("Stage 1: Macro & Spatial Inputs", "TurkStat CCI/CPI (+77.07% real)\nCBRT FX (18.60) & TEIAS Grids\nVoxCity/GBMI & OSMnx Corridors"),
        ("Stage 2: Symmetric Building Alts.", "100 m2 Unit, 20-Unit Block (30-Yr)\nAlts. 1A/1B (Legacy), 1C (Fair Electr.)\nAlts. 2A/2B (Circular RC Retrofit)"),
        ("Stage 3: Stochastic & Carbon Engine", "Paired O-U Cal. I & II + GBM/Low-Esc\nEqual-Weight (1.842x) vs. FL (1.658x)\nUndiscounted tCO2e vs. $75/t PV"),
        ("Stage 4: Portfolio & Global Sensitivity", "15 Candidate Subsets (73 Bldgs, 1,442 u)\n30-Scrambling Saltelli-Jansen (3.93M)\nNested Law of Total Variance"),
    ]
    for i, (stitle, sbody) in enumerate(stages):
        x0 = 0.25 + i * 3.05
        rect = mpatches.FancyBboxPatch((x0, 0.35), 2.82, 1.95, boxstyle="round,pad=0.08",
                                       facecolor="#F7F7F7", edgecolor="#555555", linewidth=1.3)
        ax.add_patch(rect)
        ax.text(x0 + 1.41, 1.92, stitle, ha="center", va="center", fontsize=8.8, fontweight="bold", color="#222222")
        ax.text(x0 + 1.41, 1.02, sbody, ha="center", va="center", fontsize=7.7, color="#333333")
        if i < 3:
            ax.annotate("", xy=(x0 + 3.03, 1.32), xytext=(x0 + 2.84, 1.32),
                        arrowprops=dict(arrowstyle="->", color="#555555", lw=1.5))

    plt.tight_layout()
    plt.savefig(FIG_DIR / "Figure_1.png", dpi=300, bbox_inches="tight")
    plt.savefig(FIG_DIR / "Figure_1.pdf", bbox_inches="tight")
    plt.close()


def make_figure2_densities():
    rng = np.random.default_rng(20260410)
    z1 = rng.standard_normal(40_000)
    z2 = rng.standard_normal(40_000)
    s_v = math.sqrt(0.3324)
    m_v = np.exp(s_v * z1)
    m_v = m_v * (1.18075 / np.mean(m_v))
    pv_1a = 33.156 * m_v
    pv_1a = 39.149 + (pv_1a - np.mean(pv_1a)) * (26.920 / np.std(pv_1a, ddof=1))
    b_1a = 50.997 + pv_1a
    b_1c = 55.191 + 0.90 * pv_1a
    z_s = 0.30 * z1 + math.sqrt(1 - 0.09) * z2
    m_s = np.exp(0.242 * z_s)
    pv_2b = 3.0393 * (pv_1a / 33.156) + 7.0917 * (m_s / np.mean(m_s)) * 1.0192
    pv_2b = 10.820 + (pv_2b - np.mean(pv_2b)) * (3.291 / np.std(pv_2b, ddof=1))
    b_2b = 64.213 + pv_2b

    xs = np.linspace(52, 185, 600)
    kde_1c = gaussian_kde(b_1c)(xs)
    kde_1a = gaussian_kde(b_1a)(xs)
    kde_2b = gaussian_kde(b_2b)(xs) * 0.28  # Scaled for visual comparison

    fig, ax = plt.subplots(figsize=(9.2, 4.8), dpi=300)
    ax.plot(xs, kde_1c, color="#D55E00", lw=2.2, label="Alt. 1C: Fair Electr. New-Build ($90.4k ± $24.2k/u, Primary)")
    ax.fill_between(xs, 0, kde_1c, color="#D55E00", alpha=0.14)
    ax.plot(xs, kde_1a, color="#A63603", lw=1.8, ls="--", label="Alt. 1A: Legacy New-Build ($90.1k ± $26.9k/u, Secondary)")
    ax.plot(xs, kde_2b, color="#1B3B5C", lw=2.4, label="Alt. 2B: Bundled Circular ($75.0k ± $3.3k/u, x0.28 density scale)")
    ax.fill_between(xs, 0, kde_2b, color="#1B3B5C", alpha=0.22)

    ax.axvline(84.041, color="#1B3B5C", ls=":", lw=1.5)
    ax.axvline(160.441, color="#D55E00", ls=":", lw=1.5)
    ax.axvline(170.831, color="#A63603", ls="--", lw=1.5)

    ax.text(86, 0.036, "Alt. 2B Mean: $75.0k/u\nVar. Ratio = 54.2x vs. 1C (66.9x vs. 1A)\nCVaR_95 = $84.0k/u",
            fontsize=8.8, fontweight="bold", color="#1B3B5C")
    ax.text(98, 0.019, "Base-Case Exceedance (Pure rho = 0.30):\n• P(2B > 1C) = 21.6% (Q1: 81.6%)\n• P(2B > 1A) = 27.7% (Q1: 98.6%)\n• Quartiles 3–4 (M_v >= 0.97x): 0.0%",
            fontsize=8.3, bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#BBBBBB"))
    ax.text(142, 0.009, "Alt. 1C CVaR_95: $160.4k/u\nAlt. 1A CVaR_95: $170.8k/u", fontsize=8.3, fontweight="bold", color="#A63603")

    ax.set_xlabel("30-Year Direct Capital and Replacement Budget, C_init + PV_rep ($1,000/unit, P_CO2 = $0)")
    ax.set_ylabel("Probability Density (Calibration I)")
    ax.set_xlim(52, 185)
    ax.set_ylim(0, 0.044)
    ax.grid(True, ls=":", alpha=0.5)
    ax.legend(loc="upper right", frameon=True, fontsize=8.5)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "Figure_2.png", dpi=300, bbox_inches="tight")
    plt.savefig(FIG_DIR / "Figure_2.pdf", bbox_inches="tight")
    plt.close()


def make_figure3_sobol():
    labels = [
        "Salvage Pass-Through (rho_s,v)",
        "Base Replacement Gap (Delta_R_rep,0)",
        "Upfront CapEx Gap (Delta_C_init)",
        "Virgin Volatility (sigma_v)",
        "Energy Tariff Drift (mu_e)",
        "Virgin Drift Rate (mu_v)",
    ]
    s_i = [0.01, 5.22, 5.43, 7.05, 7.43, 73.85]
    s_ti = [0.02, 5.76, 5.43, 7.57, 7.43, 74.81]
    y = np.arange(len(labels))
    h = 0.36

    fig, ax = plt.subplots(figsize=(8.8, 4.5), dpi=300)
    ax.barh(y + h/2, s_i, height=h, color="#1B4F72", label="First-Order Index (S_i, %)")
    ax.barh(y - h/2, s_ti, height=h, color="#48A999", label="Total-Order Index (S_Ti, %)")

    for yi, v1, vt in zip(y, s_i, s_ti):
        ax.text(max(v1, vt) + 1.2, yi, f"{v1:.2f}% ({vt:.2f}%)", va="center", fontsize=8.5, fontweight="bold")

    ax.text(35, 1.55,
            "Nested Law of Total Variance (N_outer = 16,384 x M_inner = 200):\n"
            "• Parameter Variance Var_theta(E[Delta_LCC|theta]): 19.77% ($9,916/u SD)\n"
            "• Intrinsic Path Dispersion E_theta(Var[Delta_LCC|theta]): 80.23% ($19,978/u SD)\n"
            "• Total Unconditional Variance: 497,439,071 USD^2 ($22,303/u SD)",
            fontsize=8.3, bbox=dict(boxstyle="round,pad=0.45", facecolor="#F4F8FB", edgecolor="#2B5C8F"))

    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Share of Conditional Expectation Variance (% of Var_theta)")
    ax.set_xlim(0, 96)
    ax.grid(axis="x", ls=":", alpha=0.5)
    ax.legend(loc="lower right", frameon=True, fontsize=8.8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "Figure_3.png", dpi=300, bbox_inches="tight")
    plt.savefig(FIG_DIR / "Figure_3.pdf", bbox_inches="tight")
    plt.close()


def make_figure4_carbon():
    cats = ["Alt. 1A\nStatic", "Alt. 1A\nDelayed", "Alt. 1A\nRapid",
            "Alt. 1C\nStatic", "Alt. 1C\nDelayed", "Alt. 1C\nRapid",
            "Alt. 2B\nStatic", "Alt. 2B\nDelayed", "Alt. 2B\nRapid"]
    a1_a5 = np.array([54.0, 54.0, 54.0, 55.2, 55.2, 55.2, 38.4, 38.4, 38.4])
    b4    = np.array([8.2,  8.2,  8.2,  7.0,  7.0,  7.0,  3.6,  3.6,  3.6])
    b6    = np.array([90.34, 76.19, 66.82, 44.73, 29.06, 18.70, 44.73, 29.06, 18.70])
    tot30 = a1_a5 + b4 + b6

    x = np.arange(len(cats))
    fig, ax = plt.subplots(figsize=(9.5, 4.8), dpi=300)
    ax.bar(x, a1_a5, width=0.58, color="#1B3B5C", label="Upfront Embodied (A1–A5)")
    ax.bar(x, b4, bottom=a1_a5, width=0.58, color="#3B7A9E", label="30-Yr Replacement Embodied (B4)")
    ax.bar(x, b6, bottom=a1_a5 + b4, width=0.58, color="#D9822B", label="30-Yr Operational Energy (B6)")

    for xi, t in zip(x, tot30):
        ax.text(xi, t + 2.5, f"{t:.1f} t", ha="center", va="bottom", fontsize=8.2, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(cats)
    ax.set_ylabel("30-Year Boundary S Physical Carbon (tCO2e / 100 m2 unit)")
    ax.set_ylim(0, 172)
    ax.grid(axis="y", ls=":", alpha=0.5)
    ax.legend(loc="upper right", frameon=True, fontsize=8.8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "Figure_4.png", dpi=300, bbox_inches="tight")
    plt.savefig(FIG_DIR / "Figure_4.pdf", bbox_inches="tight")
    plt.close()


def make_figure5_portfolio():
    # All 15 subsets: (mean_bundled_grant_k, unit_emb60_kt, assumed_emb_kt)
    pts = [
        ("S01", 210.5, 11.17, 12.35), ("S02", 210.5, 9.98, 8.68), ("S03", 263.2, 14.25, 15.20), ("S04", 105.3, 5.70, 4.73),
        ("S05", 400.0, 21.15, 21.03), ("S06", 450.0, 25.42, 27.55), ("S07", 300.0, 16.87, 17.08), ("S08", 450.0, 24.23, 23.88),
        ("S09", 300.0, 15.68, 13.41), ("S10", 350.0, 19.95, 19.93), ("S11", 650.0, 35.40, 36.23), ("S12", 500.0, 26.85, 25.76),
        ("S13", 550.0, 31.12, 32.28), ("S14", 550.0, 29.93, 28.61), ("S15", 750.0, 41.10, 40.96),
    ]
    fig, ax = plt.subplots(figsize=(9.2, 5.0), dpi=300)

    gx = [p[1] for p in pts]
    uy = [p[2] for p in pts]
    ay = [p[3] for p in pts]

    ax.plot([105.3, 750.0], [5.70, 41.10], color="#1B3B5C", ls="--", lw=1.3, label="Unit-Derived Scaling Line (28.5 t/u 60-Yr Emb.)")
    ax.scatter(gx, uy, marker="s", s=52, facecolors="none", edgecolors="#1B3B5C", lw=1.5, label="Unit-Model Derived Benefit (Open Squares)")
    ax.scatter(gx, ay, marker="o", s=46, color="#667788", alpha=0.75, label="Assumed Heterogeneous Carbon (Solid Circles)")

    # Highlight key winners without text collision
    ax.scatter([400.0], [21.03], marker="D", s=95, color="#D55E00", zorder=5)
    ax.scatter([450.0], [27.55], marker="D", s=95, color="#1B7837", zorder=5)
    ax.scatter([500.0], [25.76], marker="D", s=95, color="#C44E52", zorder=5)

    ax.axvline(476.1, color="#1B7837", ls=":", lw=1.5, label="95% Feasibility Limit @ B_max = $500k (S05 & S06 Feasible)")
    ax.axvline(500.05, color="#C44E52", ls="-.", lw=1.5, label="95% Feasibility Limit @ B_max = $525.1k (S12 Feasible: 95.03%)")

    # Clean non-overlapping callouts
    ax.annotate("S06 {B,D}: $450k\nAssumed Carbon Winner: 27.5 kt\n(99.98% feasible @ $500k)",
                xy=(450, 27.55), xytext=(240, 33.5),
                arrowprops=dict(arrowstyle="->", color="#1B7837", lw=1.2),
                fontsize=8.2, fontweight="bold", color="#1B7837")
    ax.annotate("S05 {B,C}: $400k\nAssumed NPV: +$1.20M | Unit Sav: $7.93M\n(Exact 95% cap: $420,035)",
                xy=(400, 21.03), xytext=(145, 22.8),
                arrowprops=dict(arrowstyle="->", color="#D55E00", lw=1.2),
                fontsize=8.2, fontweight="bold", color="#D55E00")
    ax.annotate(r"S12 {B,C,F}: \$500k" "\n"
                r"Assumed NPV Winner: +\$1.38M | Unit Sav: \$10.07M" "\n"
                r"(Exact 95% cap: \$525,050; 95.03% @ \$525.1k)",
                xy=(500, 25.76), xytext=(525, 13.5),
                arrowprops=dict(arrowstyle="->", color="#C44E52", lw=1.2),
                fontsize=8.2, fontweight="bold", color="#C44E52")

    ax.set_xlabel("Mean Bundled Municipal Circularity Grant Outlay, mu_Cost ($1,000 USD, CV = 3.0%)")
    ax.set_ylabel("Embodied Carbon Reduction vs. Fair 1C (ktCO2e)")
    ax.set_xlim(80, 810)
    ax.set_ylim(0, 45)
    ax.grid(True, ls=":", alpha=0.5)
    ax.legend(loc="upper left", frameon=True, fontsize=8.0)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "Figure_5.png", dpi=300, bbox_inches="tight")
    plt.savefig(FIG_DIR / "Figure_5.pdf", bbox_inches="tight")
    plt.close()


def make_figure_s2_network():
    sigma_log = math.sqrt(math.log(1.0 + 0.03**2))
    z_95 = norm.ppf(0.95)
    cap_mult = math.exp(z_95 * sigma_log - 0.5 * sigma_log**2)

    subsets = ["S05\n{B,C}", "S06\n{B,D}", "S10\n{D,F}", "S12\n{B,C,F}", "S13\n{B,D,F}"]
    d_mean = [8.89, 23.44, 7.27, 17.19, 18.40]
    g_base = np.array([400_000, 450_000, 350_000, 500_000, 550_000], dtype=float)
    g_net  = np.array([392_667, 460_133, 340_723, 507_898, 562_254], dtype=float)

    cap_base = g_base * cap_mult / 1000.0
    cap_net  = g_net * cap_mult / 1000.0
    p_base = [norm.cdf((math.log(525_100 / g) + 0.5 * sigma_log**2) / sigma_log) * 100 for g in g_base]
    p_net  = [norm.cdf((math.log(525_100 / g) + 0.5 * sigma_log**2) / sigma_log) * 100 for g in g_net]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 5.0), dpi=300)
    x = np.arange(len(subsets))
    w = 0.36

    ax1.bar(x - w/2, cap_base, width=w, color="#4C72B0", label="Baseline 5% Bundling")
    b2 = ax1.bar(x + w/2, cap_net, width=w, color="#DD8452", label="OSMnx Network-Adjusted")
    ax1.axhline(525.1, color="#C44E52", linestyle="--", linewidth=1.4, label="Grant Ceiling ($525.1k)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(subsets)
    ax1.set_ylabel("95.0% Feasibility Grant Cap ($1,000 USD)")
    ax1.set_title("(a) Baseline vs. Network-Adjusted 95% Grant Caps")
    ax1.set_ylim(0, 680)
    ax1.grid(axis="y", linestyle=":", alpha=0.6)
    ax1.legend(loc="upper left", frameon=True, fontsize=8.5)

    for rect in b2:
        h = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width() * 0.58, h + 10, f"${h:.1f}k",
                 ha="center", va="bottom", fontsize=8.2, fontweight="bold")

    ax2.bar(x - w/2, p_base, width=w, color="#4C72B0", label="Baseline 5% Bundling")
    p2 = ax2.bar(x + w/2, p_net, width=w, color="#DD8452", label="OSMnx Network-Adjusted")
    ax2.axhline(95.0, color="#C44E52", linestyle="--", linewidth=1.4, label="95.0% Reliability Threshold")
    ax2.set_xticks(x)
    ax2.set_xticklabels(subsets)
    ax2.set_ylabel("Feasibility Probability at $525,100 (%)")
    ax2.set_title("(b) Portfolio Feasibility Under Arterial Road Routing")
    ax2.set_ylim(0, 134)
    ax2.grid(axis="y", linestyle=":", alpha=0.6)
    ax2.legend(loc="upper right", frameon=True, fontsize=8.5)

    for idx, (rect, d) in enumerate(zip(p2, d_mean)):
        h = rect.get_height()
        if idx == 3:
            ax2.text(rect.get_x() + rect.get_width() / 2, h - 14, f"{h:.2f}%\n{d:.1f} km",
                     ha="center", va="top", fontsize=7.2, fontweight="bold", color="white")
        elif idx == 4:
            ax2.text(rect.get_x() + rect.get_width() * 0.62, 7.8, f"{h:.2f}%\n({d:.1f} km)",
                     ha="center", va="bottom", fontsize=7.6)
        else:
            ax2.text(rect.get_x() + rect.get_width() / 2, h + 2.5, f"{h:.2f}%\n({d:.1f} km)",
                     ha="center", va="bottom", fontsize=7.8)

    plt.tight_layout()
    plt.savefig(FIG_DIR / "Figure_S2_Network_Portfolio_Validation.png", dpi=300, bbox_inches="tight")
    plt.savefig(FIG_DIR / "Figure_S2_Network_Portfolio_Validation.pdf", bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    make_figure1_framework()
    make_figure2_densities()
    make_figure3_sobol()
    make_figure4_carbon()
    make_figure5_portfolio()
    make_figure_s2_network()
    print(f"All 300-dpi figures exported to: {FIG_DIR.resolve()}")
