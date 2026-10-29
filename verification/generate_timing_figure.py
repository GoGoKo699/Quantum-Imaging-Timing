#!/usr/bin/env python3
"""Generate the equal-duration information-marker figure and its exact data.

The plotted marker solves I_N(h)=1; it is not an exact fixed-error risk.
Default outputs are verification/figures/timing-schedules.{svg,csv}.
An optional --preview-png PATH produces a raster preview for visual inspection.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/quantum-imaging-mpl")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq


def doublet_marker(count: int, kappa: float, short: float) -> tuple[float, float]:
    pairs = count // 2
    long = ((count - 1) * kappa - pairs * short) / (pairs - 1)
    assert 0.0 < short <= kappa and long > 0.0

    def information(h: float) -> float:
        return pairs * h * h / (short + h) + (pairs - 1) * h * h / (long + h)

    root = brentq(lambda h: information(h) - 1.0, 1e-16, 1.0, xtol=1e-16, rtol=2e-14)
    assert abs(information(root) - 1.0) < 1e-9
    return root, long


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "figures")
    parser.add_argument("--preview-png", type=Path)
    args = parser.parse_args()

    kappa, b, floor = 0.05, 1.0, 0.001
    counts = np.unique(2 * np.rint(np.geomspace(100, 1_000_000, 49) / 2).astype(int))
    rows = []
    for count_np in counts:
        count = int(count_np)
        n = count - 1
        short, floored_short = b / count, max(b / count, floor)
        regular_h = (1.0 + math.sqrt(1.0 + 4.0 * n * kappa)) / (2.0 * n)
        doublet_h, long = doublet_marker(count, kappa, short)
        floored_h, floored_long = doublet_marker(count, kappa, floored_short)
        rows.append({
            "N": count,
            "total_dimensionless_duration": n * kappa,
            "regular_gap": kappa,
            "doublet_short_gap": short,
            "doublet_long_gap": long,
            "floored_short_gap": floored_short,
            "floored_long_gap": floored_long,
            "h_regular": regular_h,
            "h_doublet": doublet_h,
            "h_floored": floored_h,
            "s_over_sigma_regular": math.sqrt(8.0 * regular_h),
            "s_over_sigma_doublet": math.sqrt(8.0 * doublet_h),
            "s_over_sigma_floored": math.sqrt(8.0 * floored_h),
        })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    data_path = args.output_dir / "timing-schedules.csv"
    with data_path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        for row in rows:
            writer.writerow({key: value if isinstance(value, int) else format(value, ".17g") for key, value in row.items()})

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "svg.hashsalt": "quantum-imaging-timing-v1",
    })
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.9), gridspec_kw={"width_ratios": [1.1, 1.0]})
    colors = {"regular": "#475569", "doublet": "#166da6", "floored": "#c46c11"}
    styles = {"regular": "-", "doublet": "-", "floored": "--"}
    labels = {"regular": "Regular gaps", "doublet": "Shrinking doublets", "floored": "Doublets with a fixed gap floor"}

    for key in ("regular", "doublet", "floored"):
        axes[0].loglog(counts, [row[f"s_over_sigma_{key}"] for row in rows], color=colors[key], linestyle=styles[key], linewidth=2.5, label=labels[key])
    axes[0].set_title("A  Resolution information marker", loc="left", pad=13)
    axes[0].set_xlabel("Recorded photons, $N$")
    axes[0].set_ylabel(r"$s_*/\sigma=\sqrt{8h_*}$, where $I_N(h_*)=1$")
    axes[0].legend(loc="lower left", frameon=False, fontsize=9.5, handlelength=2.6)

    for key, column in (("regular", "regular_gap"), ("doublet", "doublet_short_gap"), ("floored", "floored_short_gap")):
        axes[1].loglog(counts, [row[column] for row in rows], color=colors[key], linestyle=styles[key], linewidth=2.5)
    axes[1].axvline(b / floor, color="#999999", linestyle=":", linewidth=1.2)
    axes[1].annotate("Floor becomes active", xy=(b / floor, floor), xytext=(2200, 0.004), fontsize=9.5, color="#7b4b1b", arrowprops={"arrowstyle": "-", "color": "#7b4b1b", "lw": 0.8})
    axes[1].set_title("B  Supplied within-pair gap", loc="left", pad=13)
    axes[1].set_xlabel("Recorded photons, $N$")
    axes[1].set_ylabel(r"Dimensionless Brownian variance, $D\Delta t/\sigma^2$")
    axes[1].text(0.98, 0.87, r"Regular: $\kappa=0.05$" + "\n" + r"Doublet: $1/N$" + "\n" + r"Floor: $10^{-3}$", transform=axes[1].transAxes, ha="right", va="top", fontsize=9.5, bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85})

    for axis in axes:
        axis.grid(which="major", color="#dbe0e6", linewidth=0.7)
        axis.grid(which="minor", color="#edf0f3", linewidth=0.45)
        axis.set_xlim(100, 1_000_000)
        axis.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Same photon count and duration; different timing resources", fontsize=16, x=0.065, ha="left", y=0.99)
    fig.text(0.065, 0.045, r"Every curve has $\sum_{i=2}^{N}v_i=(N-1)\kappa$.  The plotted $I_N=1$ marker is not an exact error probability.", fontsize=10, color="#3f4854")
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.19, top=0.83, wspace=0.32)

    svg_path = args.output_dir / "timing-schedules.svg"
    fig.savefig(svg_path, format="svg", metadata={"Date": None, "Creator": "Quantum-Imaging-Timing: generate_timing_figure.py", "Description": "Information marker I_N=1 and supplied timing gaps for equal-duration schedules; not an exact fixed-error risk."})
    if args.preview_png is not None:
        args.preview_png.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.preview_png, dpi=180)
    plt.close(fig)
    print(f"Wrote {svg_path}\nWrote {data_path}")


if __name__ == "__main__":
    main()
