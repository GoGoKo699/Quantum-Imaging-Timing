# Timing and calibration crossovers

[Joint theorem](joint-model.md) · [Joint receiver](joint-receiver.md) · [Zero-jitter timing regimes](timing-regimes.md)

Timing changes how much common Brownian motion two photons experience between arrivals. Calibration changes how well an unknown independent-jitter variance is known. These resources affect different terms of the joint frontier; neither is a measurement of a signal photon's realized jitter.

## 1. General schedule

For the exact stationary calibration source in the [joint model](joint-model.md#1-experiment), write

```math
\sum_{i=2}^{N}\frac{r_0^2}{b+v_i+r_0}=1,
\qquad S_2=\sum_{i=2}^{N}(b+v_i)^{-2},
```

```math
R_Q=r_0+\min\left\{b,\sqrt{\frac bM},S_2^{-1/4}\right\}.
```

The $`b=0`$ and $`M=0`$ conventions are part of the theorem. Define the uncalibrated uncertainty scale $`U_0=\min\{b,S_2^{-1/4}\}`$. When $`U_0`$ is parametrically larger than $`r_0`$, calibration improves the resolution order once

```math
M\gg M_{\mathrm{cross}},\qquad
M_{\mathrm{cross}}=\frac b{U_0^2}
=\max\{b^{-1},b\sqrt{S_2}\}.
```

It reaches the physical floor at calibration count of order

```math
M_{\mathrm{floor}}\asymp\frac b{r_0^2}.
```

If $`U_0\lesssim r_0`$, uncertainty is already below the physical floor and calibration cannot improve the resolution order. Equality at a crossover generally changes constants; a parametric improvement requires the corresponding strict asymptotic inequality.

The calibration stream has no Brownian motion in this experiment. Adding the signal's known Brownian variance to calibration noise would overcharge its cost outside the close-doublet limit. The general [weighted receiver](joint-receiver.md#3-known-bound-and-calibration-tests) instead uses the independent calibration variance $`O(b/M)`$ directly.

## 2. Close doublets

Suppose a linear number of disjoint photon doublets have internal Brownian variances $`O(N^{-1})`$. Then

```math
R_Q\asymp N^{-1}+\min\left\{b,\sqrt{\frac bL}\right\},
\qquad
K=\frac{NM}{N+M},\qquad L=\max\{\sqrt N,K\}.
```

Set $`K=0`$ when $`M=0`$. When $`b\gg N^{-1}`$, the short gaps give $`S_2\asymp N/b^2`$, while $`r_0\asymp N^{-1}+\sqrt{b/N}`$. Minimizing the nuisance branches and including this physical floor is equivalent to the displayed harmonic-count expression. When $`b\lesssim N^{-1}`$, the known-bound branch already gives the ideal floor.

Without calibration, the squared-separation scale has three regimes:

| Jitter-variance bound | Quantum order in $`q`$ | Limiting mechanism |
|---|---|---|
| $`b\lesssim N^{-1}`$ | $`N^{-1}`$ | Ideal photon floor |
| $`N^{-1}\ll b\lesssim N^{-1/2}`$ | $`b`$ | Unknown-variance plateau |
| $`b\gg N^{-1/2}`$ | $`\sqrt b\,N^{-1/4}`$ | Fourth-order shape information |

Calibration beats intrinsic shape information at $`K\sim\sqrt N`$ when the shape branch is active. Resolving parametrically below the uncertainty scale $`q\asymp b`$ requires $`Kb\gg1`$. Therefore, where a nuisance penalty actually dominates the photon floor, parametric improvement over no calibration requires

```math
K\gg\max\{\sqrt N,b^{-1}\}.
```

In the plateau $`b^{-1}`$ exceeds $`\sqrt N`$; merely exceeding the latter is insufficient. For a threshold well below $`N`$, $`K`$ and the required calibration count $`M`$ are comparable. At saturation $`K\asymp N`$, calibration must be comparable to the signal count.

**A complete order example.** Let $`N=10^8`$ and $`b=10^{-6}`$. The ideal floor is $`10^{-8}`$, the uncalibrated plateau is $`10^{-6}`$, and $`\sqrt N=10^4`$. The plateau persists until $`K`$ reaches order $`10^6`$; a parametric exit needs $`K\gg10^6`$. Comparable signal/calibration counts attain $`q`$ of order $`10^{-7}`$. These are representative asymptotic scales, not exact error probabilities or leading constants. Physical separation is recovered by $`s=2\sqrt2\sigma\sqrt q`$.

The [four-outcome doublet construction](joint-receiver.md#5-four-outcome-close-doublet-receiver) proves this order even when motion between doublets is arbitrarily large. It still requires shrinking within-doublet gaps and joint access to those two photons. Adding more calibration photons does not supply that acquisition schedule.

## 3. Physical jitter remains after calibration

For close doublets, comparable counts $`M\asymp N`$ attain

```math
q_*\asymp N^{-1}+\sqrt{\frac bN}.
```

More calibration cannot improve this order. If the actual variance $`w`$ were known exactly, the same physical experiment would still have

```math
q_{*,\mathrm{known}}\asymp N^{-1}+\sqrt{\frac wN}.
```

At fixed positive $`w`$, this is physical separation $`s_*\asymp\sigma(w/N)^{1/4}`$. The zero-jitter close-doublet order $`s_*\asymp\sigma N^{-1/2}`$ survives only if physical jitter itself is $`O(N^{-1})`$. The reason is visible in the known-jitter SWAP null background: independent difference variance $`2w`$ persists even as the Brownian internal gap shrinks to zero.

The uniform theorem uses the supplied upper bound $`b`$, while the known-variance statement uses actual $`w`$. They are distinct assertions. No adaptation theorem replacing $`b`$ by a data-dependent estimate in every minimax branch is claimed.

## 4. Periodic and regular schedules

If all gaps satisfy $`a\le v_i\le A a`$ for fixed $`A`$, with $`a`$ allowed to depend on $`N`$, the general frontier becomes

```math
R_Q\asymp N^{-1}+\sqrt{\frac{a+b}{N}}
+\min\left\{b,\sqrt{\frac bM},\sqrt{a+b}\,N^{-1/4}\right\}.
```

For fixed positive periodic gaps, this simplifies to

```math
R_Q\asymp N^{-1/2}+
\min\{b,\sqrt{b/M},N^{-1/4}\}.
```

When common Brownian motion dominates a weak independent jitter, the signal's physical variance floor is larger than the calibration stream's variance. Reaching the floor can then require $`M\asymp bN/(a+b)`$, smaller than $`N`$, provided uncertainty was initially relevant. This does not improve the physical signal floor itself.

The quantum theorem conditions on bounded known gaps. The original [ideal Poisson theorem](poisson-arrivals.md) is a different joint random-time experiment with unbounded gaps and no independent jitter; its logarithmic conclusion is not extended here by substituting a variance into the deterministic formula. Unknown diffusion, finite timing resolution, non-Gaussian jitter, moving calibration references and nonideal spatial access similarly require their own experiments.

## 5. Relation to the sister result

[Quantum-Imaging-Calibration](https://github.com/GoGoKo699/Quantum-Imaging-Calibration) identifies the independent-noise calibration plateau and the collision hard pair. The present joint theorem retains those mechanisms while accounting for the Brownian covariance and a known nonuniform schedule. The exact shape receiver has to change because a pair's relative source distribution has three atoms. The common learning anchor, [Tsang's review](https://arxiv.org/pdf/1906.02064v2), supplies imaging and two-photon foundations; neither the review nor the independent-jitter frontier by itself establishes this correlated-record composition.
