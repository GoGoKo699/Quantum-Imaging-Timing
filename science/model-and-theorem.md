# Model and resolution theorem

Two equally bright incoherent point sources move together while photons are collected. Their separation is fixed, but their common centroid follows Brownian motion. Photons arriving close together have almost the same centroid. The question is how much this temporal information helps distinguish one source from two when every spatial measurement is allowed.

The answer depends on the list of arrival gaps. For a known schedule with bounded Brownian increments, one scalar function determines the resolution order. A receiver comparing disjoint adjacent photon pairs attains that order, and a bound on the complete spatial-register state applies to every collective receiver.

## 1. Optical normalization

The physical amplitude point-spread function of a photon emitted at position $`c`$ is

```math
\psi_c(x)=\frac{1}{(2\pi\sigma^2)^{1/4}}
\exp\!\left[-\frac{(x-c)^2}{4\sigma^2}\right].
```

Thus direct imaging of a stationary point source has position variance $`\sigma^2`$. Introduce the dimensionless image coordinate $`z=x/(\sqrt2\sigma)`$. A photon centered at dimensionless position $`a`$ occupies the normalized state

```math
\langle z\mid a\rangle=\pi^{-1/4}e^{-(z-a)^2/2},
\qquad
|\langle a\mid b\rangle|^2=e^{-(a-b)^2/2}.
```

In this normalization, $`\lvert0\rangle`$ is a one-mode Gaussian vacuum with position and momentum variances $`1/2`$. The oscillator notation describes the transverse spatial wavefunction of one photon; oscillator excitation number is not the number of detected photons.

For physical source separation $`s\ge0`$, define

```math
q=\frac{s^2}{8\sigma^2},
\qquad
s=2\sqrt2\sigma\sqrt q.
```

The two source positions relative to the centroid are consequently $`\pm\sqrt q`$. Equal incoherent brightness gives the single-photon state

```math
\omega_{q,a}
=\frac12\lvert a+\sqrt q\rangle\langle a+\sqrt q\rvert
+\frac12\lvert a-\sqrt q\rangle\langle a-\sqrt q\rvert.
```

The usual stationary Gaussian two-source model is part of the quantum imaging framework developed by [Tsang, Nair and Lu (2016)](https://doi.org/10.1103/PhysRevX.6.031033). Here the centroid is a temporally correlated nuisance, and the operational task is finite-error hypothesis testing.

## 2. Known arrival schedule and hidden motion

Consider $`N\ge2`$ photons with known ordered timestamps $`t_1<\cdots<t_N`$. Each photon occupies a labeled temporal register with the spatial state above. These temporal-register labels are classical information available to the receiver; the emitting-source labels remain hidden.

The initial dimensionless centroid $`m\in\mathbb R`$ is unknown and unrestricted. Write

```math
B_1=0,
\qquad
B_i=\sum_{j=2}^{i}W_j,
\qquad
W_j\sim\mathcal N(0,v_j)
\quad\text{independently}.
```

The gap variances $`v=(v_2,\ldots,v_N)`$ are known and satisfy

```math
0\lt v_i\le V,
\qquad i=2,\ldots,N,
```

for a fixed finite $`V>0`$. With the physical Brownian convention
$`\mathbb E[(c(t)-c(u))^2]=2D|t-u|`$, these variances are

```math
v_i=\frac{D(t_i-t_{i-1})}{\sigma^2}.
```

The diffusion coefficient $`D`$ and point-spread width $`\sigma`$ are known. Conditional on the centroid trajectory, different photons have independent source labels with probabilities $`1/2,1/2`$. Equivalently, let $`S_i\in\{-1,+1\}`$ be independent fair signs, independent of the motion. The complete input state is

```math
\rho_{q,m}^{v}
=\mathbb E_{W,S}
\bigotimes_{i=1}^{N}
\lvert m+B_i+\sqrt q S_i\rangle
\langle m+B_i+\sqrt q S_i\rvert
=\mathbb E_W\bigotimes_{i=1}^{N}\omega_{q,m+B_i}.
```

The state contains the correlations produced by one common Brownian trajectory. Replacing it by a product of separately averaged single-photon states would define a different experiment.

All statements below are conditional on the supplied deterministic schedule. The fixed-count Poisson arrival model is derived separately in [Poisson arrivals](poisson-arrivals.md).

## 3. Receiver and testing risk

The receiver knows $`N,v,\sigma`$ and a proposed threshold $`h>0`$. It may perform any joint quantum measurement on all spatial registers, use independent ancillas, store photons, or implement adaptive processing. It has no access to the hidden trajectory, source labels, or an environment revealing them.

The hypotheses are

```math
H_0:q=0,
\qquad
H_1:q\ge h.
```

A test is an effect $`0\le M\le I`$; outcome $`1`$ means that the test reports two separated sources. Its type-I and worst alternative errors are

```math
\alpha(M)=\sup_{m\in\mathbb R}\mathrm{tr}(M\rho_{0,m}^{v}),
```

```math
\beta_h(M)
=\sup_{m\in\mathbb R,\ q\ge h}
\mathrm{tr}[(I-M)\rho_{q,m}^{v}].
```

Define the minimax error

```math
\mathcal R_Q(h;v)
=\inf_{0\le M\le I}\max\{\alpha(M),\beta_h(M)\}.
```

The initial centroid is the same physical nuisance under either hypothesis, but uniform validity is required for every possible value. A coin-flip decision gives $`\mathcal R_Q\le1/2`$. The alternative is unbounded: the local parameter restriction below applies to the design threshold $`h`$, not to the actual separation $`q\ge h`$.

The resolution considered here is the separation needed to achieve a specified testing error. It is not a claim about mean-squared estimation risk, unbiased estimators, or a local Cramér–Rao bound.

## 4. Schedule information

Define

```math
\mathcal I(h;v)
=\sum_{i=2}^{N}\frac{h^2}{v_i+h}.
```

A gap with $`v_i\ll h`$ contributes approximately $`h`$: its two photons nearly share their centroid. A gap with $`v_i\gg h`$ contributes approximately $`h^2/v_i`$, because relative Brownian motion creates a nonzero background in the pair comparison.

This sum includes all adjacent gaps. A disjoint-pair receiver can retain at least half of it: the odd and even adjacent-edge matchings partition the sum, and one has weight at least $`\mathcal I/2`$.

## 5. Uniform resolution theorem

**Theorem.** Fix $`V>0`$ and $`q_0>0`$. For every $`N\ge2`$, every known schedule $`0<v_i\le V`$, and every threshold $`0<h\le q_0`$,

```math
\frac12\left[1-3(V+q_0)\mathcal I(h;v)
-\sqrt{2\mathcal I(h;v)}\right]_+
\ \le\ \mathcal R_Q(h;v)
\ \le\
\min\!\left\{\frac12,
\exp[-c_{V,q_0}\mathcal I(h;v)]\right\},
```

where $`[x]_+=\max\{x,0\}`$ and one admissible constant is

```math
c_{V,q_0}=\frac{e^{-4q_0}}{32(1+V)^3}.
```

The upper bound holds uniformly for all $`m\in\mathbb R`$ and all actual alternatives $`q\ge h`$.

The [collective converse](collective-converse.md) proves the lower bound by comparing the complete available quantum states. The [pair receiver](receiver.md) proves the upper bound using the better adjacent-edge matching and a likelihood-ratio test. Its decision rule is increasing in the antisymmetric outcomes. Since their probabilities increase with $`q`$, error control at $`q=h`$ also controls every larger separation.

For any fixed desired error in $`(0,1/2)`$, the transition occurs at

```math
\mathcal I(h;v)\asymp1,
```

with constants depending only on $`V,q_0`$ and the target error. This is an order statement; the displayed constants are sufficient finite-sample bounds.

One can define a schedule scale $`h_*(v)`$ as the unique solution of $`\mathcal I(h_*;v)=1`$. The function is continuous and strictly increasing from zero to infinity. For $`a\ge1`$,

```math
a\mathcal I(h;v)\le\mathcal I(ah;v)\le a^2\mathcal I(h;v).
```

Consequently changing a fixed error target changes $`h_*`$ by at most a constant factor, once the relevant thresholds lie in $`(0,q_0]`$. Physical separation is proportional to $`\sqrt{h_*}`$.

## 6. Direct imaging benchmark

Direct imaging measures the position of every photon and then permits arbitrary classical processing of the entire position record and timestamps. Let $`\mathcal R_{\rm DI}`$ denote the same minimax risk restricted to this experiment. The [direct imaging proof](direct-imaging.md) establishes

```math
\frac12(1-h\sqrt N)_+
\le\mathcal R_{\rm DI}(h;v)
\le
\min\!\left\{\frac12,
\frac{K_{V,q_0}}{\lfloor N/2\rfloor h^2}\right\},
```

where

```math
K_{V,q_0}=2(1+V)^2+8(1+V)q_0+4q_0^2.
```

The upper bound is uniform over the unbounded alternative $`q\ge h`$. Hence bounded-gap direct imaging has testing scale $`h\asymp N^{-1/2}`$, or physical separation $`s\asymp\sigma N^{-1/4}`$, regardless of how many very short gaps the schedule contains.

## 7. Physical scope and reading route

The model assumes a known one-dimensional real Gaussian amplitude response, equal independent incoherent source labels, a rigid source pair with known Brownian diffusion, a complete spatial image plane, and temporally labeled photons. The schedule is supplied to the receiver. Source timing control, discarded photons, losses, detector dead time, imperfect interference and finite temporal-mode duration require their own resource accounting when implementing a schedule or receiver.

The receiver's pair measurement compares spatial states from different timestamps, so its implementation requires suitable storage or delay and temporal-mode matching. The theorem gives the optimal statistical order under the permitted quantum measurement model; it does not assign zero engineering cost to those operations.

Continue with [Collective converse](collective-converse.md) for the lower bound, [Pair receiver](receiver.md) for attainment, [Direct imaging](direct-imaging.md) for the classical-data benchmark, or [Timing regimes](timing-regimes.md) for periodic, doublet and random schedules. [Related work](../references/related-work.md) identifies the inherited imaging and information-theoretic tools and the contribution of the schedule-dependent result.
