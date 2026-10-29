# Reproduce the finite checks

The analytical results are proved in [the scientific account](../science/README.md). This directory checks normalization, constants, numerical identities and illustrative schedules. It does not replace the uniform proofs or certify experimental feasibility or literature priority.

## Run

From the repository root, with Python 3.12:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The committed run used **Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0**. Figure generation additionally used **Matplotlib 3.10.8**. Exact package versions are recorded in [requirements.txt](requirements.txt); the interpreter and core library versions are also in [results.json](results.json).

A successful run prints:

```text
PASS verify_converse.py
PASS verify_receiver.py
All assertions passed; saved outputs were not modified.
```

Every check uses deterministic quadrature, explicit enumeration or a fixed random seed. Failed assertions or integration warnings stop the relevant script. The runner requires a successful exit and a `passed` status from each script. Running the default command does not change the repository.

To replace the recorded report deliberately, run:

```bash
python verification/run_all.py --write
```

The JSON records each result and SHA-256 digests of the three check/runner sources. Floating-point errors can differ slightly across numerical libraries and machines; the assertions use stated tolerances rather than requiring byte-identical numeric reports.

## What is checked

| Calculation | Check and committed outcome | Proof or formula being examined |
|---|---|---|
| Brownian precision resolvent | 600 seeded cases, dimensions up to 30 and increment variances spanning 11 orders of magnitude; maximum ratio to the proved bound is about 0.999938 | [Converse, Section 4](../science/collective-converse.md#4-brownian-precision-controls-the-resolvent) |
| Fourth displacement derivative | Trace norm about 17.1564; elementary triangle bound about 17.3694, both below the proof's bound 18 | [Gaussian replacement](../science/collective-converse.md#2-a-uniform-gaussian-replacement-bound) |
| Binary versus Gaussian displacement | Five finite-Fock checks from q=10⁻⁵ to 0.1; half-trace-distance/q² approximately 0.595–0.715, below 1.5 | Same replacement bound; finite corroboration |
| Gaussian fidelity convention | Five 64-dimensional Fock calculations; absolute root-fidelity discrepancies below 6×10⁻¹⁰ in the committed run, against a 2×10⁻⁸ assertion tolerance | [Squared versus root fidelity](../science/collective-converse.md#3-fidelity-of-the-gaussian-comparison-states) |
| Direct-imaging likelihood and moments | Independent Gaussian quadrature checks three collision integrals and nine pair-variance formulas | [Classical converse and pair statistic](../science/direct-imaging.md) |
| Exact SWAP response | 30 Gaussian-quadrature cases, including zero motion; maximum absolute probability error below 3×10⁻¹⁵ | [Pair probability](../science/receiver.md#1-exact-probability-for-a-pair) |
| Pair Hellinger scale | 600 points check the proved two-sided constants, including a separate zero-motion normalization check | [Hellinger convention and bound](../science/receiver.md#2-the-pairs-testing-information) |
| Finite pair tests | Complete outcome enumeration for three schedules checks matching weights, likelihood-ratio errors and the composite-alternative monotonicity | [Matching and test](../science/receiver.md) |
| Informative pair test | An exact binomial calculation for 500 pairs, v=0.001 and h=0.05 gives type-I error about 0.000294 and type-II error about 0.000470 | Concrete finite illustration, not an optimized risk constant |
| Poisson integrals | 15 resolvent integrals and 16 joint gap–outcome Hellinger integrals | [Poisson lower and upper bounds](../science/poisson-arrivals.md) |
| Crossover and exact duration | 15 Poisson root inversions and eight equal-duration doublet/floor examples | [Uniform crossover](../science/poisson-arrivals.md#6-uniform-crossover-and-resolution-order) and [timing schedules](../science/timing-regimes.md) |

The exact scripts are [verify_converse.py](verify_converse.py) and [verify_receiver.py](verify_receiver.py). The full observed values, rather than only the rounded table, are in [results.json](results.json).

The Gaussian fidelity checks retain 64 Fock coefficients and use 160-point Gauss–Hermite quadrature. They check the retained trace and compare the numerical root fidelity with the analytic expression. Small negative eigenvalues caused by floating-point roundoff are clipped when forming square roots. This is a numerical convention check on the listed examples, not a certified infinite-dimensional error bound. The trace-norm Taylor estimate and exact Gaussian formula provide the analytical justification.

## Regenerate the figure

```bash
python verification/generate_timing_figure.py
```

This writes [timing-schedules.svg](figures/timing-schedules.svg) and [timing-schedules.csv](figures/timing-schedules.csv). The generator sets its Matplotlib cache directory to a writable temporary location if one is not already configured. To inspect a raster preview without adding it to the repository:

```bash
python verification/generate_timing_figure.py --output-dir /tmp/timing-figure --preview-png /tmp/timing-figure/preview.png
```

Each curve solves the information equation I(h)=1. The three schedules have exactly the same photon count and elapsed duration at each sample size; their between-doublet intervals are adjusted to preserve that constraint. The right panel displays the short-gap resource explicitly. The figure is neither a Monte Carlo error estimate nor an exact minimax-risk curve.

The 49-row data table and SVG were regenerated into a separate directory and matched the committed bytes exactly with the pinned environment. The generated raster preview was inspected for legible labels, unclipped equations and consistent curve meanings. The SVG has a fixed identifier salt and no creation timestamp to make regeneration deterministic.

## Limits of verification

Finite matrices and quadrature cannot establish schedule-uniform inequalities, composite minimax quantifiers or asymptotic exponents. Those follow from the written arguments. These checks do not model a complete optical field, source occupancy, memory efficiency or imperfect temporal/spectral/polarization matching. The [physical interface](../science/physical-interface.md) states which resources the receiver is assumed to receive and which implementation effects require a separate model.

[Repository overview](../README.md) · [Scientific reading route](../science/README.md)
