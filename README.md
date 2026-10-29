# Quantum Imaging Timing

**When an unresolved source pair moves, how much does the timing of the photons matter?** For a known Gaussian point-spread function and a Brownian common centroid, the full quantum resolution limit depends on the individual gaps between photons. Measurements on disjoint adjacent pairs attain its resolution order, even when arbitrary collective processing of the whole record is allowed.

The experiment supplies $`N`$ separately addressable one-photon spatial registers at known times. The two sources are equally bright and mutually incoherent, their separation $`s`$ is fixed, and their source labels are independent. The initial centroid is arbitrary and unknown; the diffusion coefficient $`D`$ and Gaussian intensity variance $`\sigma^2`$ are known. This is an explicit photon-register model with [physical access requirements](science/physical-interface.md).

## The timing law

Write

```math
q=\frac{s^2}{8\sigma^2},\qquad
v_i=\frac{D(t_i-t_{i-1})}{\sigma^2},\qquad
\mathcal I_N(q;\mathbf v)=\sum_{i=2}^{N}\frac{q^2}{q+v_i}.
```

For known deterministic schedules with $`0<v_i\le V`$, fixed $`V`$, and a design threshold $`0<h\le q_0`$, the fixed-error minimax boundary for distinguishing one source from two is

```math
\mathcal I_N(h;\mathbf v)=\Theta(1).
```

Here the null hypothesis is $`q=0`$ and the alternative is $`q\ge h`$, uniformly over the unknown centroid. The constants depend on the error target and fixed bounds, not on the photon count or individual schedule. This functional is an operational testing scale, not a Fisher-information formula.

The [collective converse](science/collective-converse.md) bounds distinguishability of the entire correlated quantum state. The [attaining receiver](science/receiver.md) chooses one of the two adjacent-pair matchings and measures each pair's SWAP symmetry. Translation invariance removes the absolute centroid, and independent internal Brownian increments make the selected outcomes independent.

## What the law implies

The following separation scales suppress fixed physical constants. Each comparison uses the resource convention stated in its first column.

| Acquisition regime | Quantum separation scale |
|---|---|
| Periodic arrivals, fixed positive motion per gap; duration grows with $`N`$ | $`s_*/\sigma=\Theta(N^{-1/4})`$ |
| Close doublets with internal motion $`O(N^{-1})`$, at the same count and duration as the periodic schedule above | $`s_*/\sigma=\Theta(N^{-1/2})`$ |
| Periodic arrivals, fixed total duration and increasing photon count | $`s_*/\sigma=\Theta(N^{-1/2})`$ |
| Ideal Poisson arrivals, fixed positive mean motion per gap and fixed photon-count stopping | $`s_*/\sigma=\Theta((N\log N)^{-1/4})`$ |

The close-doublet comparison changes the supplied acquisition schedule. It requires shrinking within-pair intervals and the corresponding timing and temporal-mode resources. For schedules with a fixed upper bound on their gaps, a fixed positive minimum gap restores the slower asymptotic exponent. The Poisson logarithm assumes that arbitrarily close arrivals remain independently addressable; it is not a claim about an unspecified finite-bandwidth optical field.

![Resolution proxy for periodic and doublet schedules at equal photon count and duration](verification/figures/timing-schedules.svg)

The figure solves $`\mathcal I_N(q)=1`$ to illustrate the scaling. It does not give exact fixed-error constants. See [timing regimes](science/timing-regimes.md) and the [Poisson experiment](science/poisson-arrivals.md) for the complete statements.

For **direct imaging**, even optimal processing of all detected positions and timestamps has $`q_*=\Theta(N^{-1/2})`$, hence $`s_*/\sigma=\Theta(N^{-1/4})`$, throughout the bounded-gap setting. The [direct-imaging proof](science/direct-imaging.md) includes both a lower bound for every classical processing rule and an attaining pair-difference statistic.

## Read the science

Start with the [scientific reading route](science/README.md), or go directly to the precise question you want to inspect.

| Question | Authoritative account |
|---|---|
| What exactly is supplied, and what is the testing task? | [Model and theorem](science/model-and-theorem.md) |
| Why can no collective quantum receiver do better in order? | [Collective converse](science/collective-converse.md) |
| How do photon pairs attain the boundary? | [Pair receiver](science/receiver.md) |
| How do count, duration, peak timing and timing floors differ? | [Timing regimes](science/timing-regimes.md) |
| Where does the Poisson logarithm come from? | [Poisson arrivals](science/poisson-arrivals.md) |
| What can positions and timestamps alone achieve? | [Direct imaging](science/direct-imaging.md) |
| What optical access does the register model require? | [Physical interface](science/physical-interface.md) |
| Which ingredients are inherited? | [Related work](references/related-work.md) and [bibliography](references/references.bib) |

The Brownian crossover exponents and static two-photon interference receivers have prior precedents. The contribution developed here is the schedule-dependent characterization for the correlated record, its converse against all collective receivers, and adjacent-pair sufficiency. The related-work account gives the source-level comparison and its limits.

## Reproduce the checks

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The [verification guide](verification/README.md) explains the numerical tolerances, committed results, figure generation and the limits of finite checks. The analytic theorems rely on the written proofs; the checks examine fidelity conventions, the Brownian precision bound, exact pair probabilities, classical moments and the schedule examples.

## Scope

The theorem assumes a known real Gaussian amplitude response, known diffusion, equal brightness, a fixed known separation axis and independent source labels. Receiver ancillas may be arbitrary but cannot reveal the hidden source labels or Brownian path. Count and timing statistics carry no additional separation information. The results concern fixed-error one-versus-two testing, not a global estimation-risk theorem. Temporal overlap, mode matching, loss and occupancy must be accounted for when connecting an optical source to the stated register interface.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
