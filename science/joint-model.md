# Joint timing, jitter and calibration model

The common Brownian centroid and fresh per-photon jitter have different experimental meanings. Close photons can share almost the same Brownian position while retaining independent displacements. A calibration source can identify the displacement distribution without reporting any signal photon's realized displacement.

This page states the combined experiment and its matching resolution laws. The [converse](joint-converse.md) retains the full correlated input. The [receiver](joint-receiver.md) uses disjoint relative spatial modes. [Crossover regimes](jitter-calibration-regimes.md) explain when calibration improves the order. The original [timing theorem](model-and-theorem.md) remains the zero-independent-jitter result, with its own unbounded alternative; the joint theorem below uses a fixed local alternative.

## 1. Experiment

Use the known real Gaussian amplitude and the Timing normalization

```math
\langle z\mid a\rangle=\pi^{-1/4}e^{-(z-a)^2/2},
\qquad z=\frac{x}{\sqrt2\sigma},\qquad
q=\frac{s^2}{8\sigma^2}.
```

The physical intensity variance is $`\sigma^2`$. There are $`N`$ labeled signal registers at a known ordered schedule. Register $`i`$ has latent dimensionless center

```math
m+B_i+J_i+S_i\sqrt q.
```

Here $`m\in\mathbb R`$ is unrestricted and unknown; $`B_1=0`$ and $`B_i-B_{i-1}\sim\mathcal N(0,v_i)`$ are independent known Brownian increments; $`S_i`$ are independent fair signs; and $`J_i\sim\mathcal N(0,w)`$ are fresh independent jitters. All variables are independent except the common Brownian temporal correlations. Under the convention $`\mathrm{Var}[C(t)-C(u)]=2D|t-u|`$,

```math
v_i=\frac{D(t_i-t_{i-1})}{\sigma^2},\qquad
0\lt v_i\le V\quad (i=2,\ldots,N).
```

Diffusion and the schedule are known. The jitter variance is unknown in the supplied class

```math
0\le w\le b\le b_{\max}.
```

If the physical independent displacement variance is $`\nu`$, then $`w=\nu/(2\sigma^2)`$. The bound $`b`$ may depend on the photon budgets; $`V`$ and $`b_{\max}`$ are fixed finite constants. Statements in $`b`$ are uniform minimax statements over this nuisance class, rather than pointwise adaptation claims at the actual $`w`$.

**Calibration source.** Supply exactly $`M`$ separate one-photon registers from an externally stabilized point source at known coordinate zero, with the same real Gaussian amplitude and the same unknown variance $`w`$. Its jitters are mutually independent and independent of all signal variables. It neither follows nor monitors the signal Brownian path. Matching jitter transfer and the stabilized known point are assumptions of the theorem.

Writing $`\tau_w=\mathbb E_J|J\rangle\langle J|`$, the joint state is

```math
\Omega_{q,w,m}^{v}
=\mathbb E_{B,J,S}\!\left[
\bigotimes_{i=1}^{N}
|m+B_i+J_i+S_i\sqrt q\rangle
\langle m+B_i+J_i+S_i\sqrt q|
\right]\otimes\tau_w^{\otimes M}.
```

The expectation outside the signal tensor product retains the Brownian correlations. Counts and timestamps are conditioned upon, or have matched parameter-independent laws. Source signs, Brownian path and individual jitters are inaccessible. A co-moving reference or a record of instantaneous jitter defines another experiment.

## 2. Testing task

Fix $`\epsilon\in(0,1/2)`$ and $`0\lt q_0\le1/4`$. For a design threshold $`h\in(0,q_0]`$, test

```math
H_0:q=0,\quad m\in\mathbb R,\quad 0\le w\le b,
\qquad
H_1:h\le q\le q_0,\quad m\in\mathbb R,\quad 0\le w\le b.
```

The quantum minimax risk is

```math
\mathcal R_Q(h;v,N,M,b)
=\inf_{0\le E\le I}\max\left\{
\sup_{m,w}\mathrm{Tr}(E\Omega_{0,w,m}^{v}),\;
\sup_{m,w,\ h\le q\le q_0}
\mathrm{Tr}[(I-E)\Omega_{q,w,m}^{v}]
\right\}.
```

Each supremum obeys the stated nuisance range. The effect $`E`$ may act on all signal and calibration registers and independent ancillas. Signal and calibration share one jitter variance within each world; admissible lower-bound comparisons may use different variances across the two hypotheses. Direct imaging measures every photon's position and then permits arbitrary classical processing of all positions and timestamps.

## 3. Joint frontier

Let $`r_0`$ be the unique positive solution

```math
\mathcal I_b(r_0;v):=
\sum_{i=2}^{N}\frac{r_0^2}{b+v_i+r_0}=1,
\qquad
S_2(v,b)=\sum_{i=2}^{N}\frac1{(b+v_i)^2}.
```

For $`b\gt 0`$ define

```math
U(v,M,b)=\min\left\{b,\sqrt{\frac bM},S_2(v,b)^{-1/4}\right\},
\qquad
R_Q=r_0+U.
```

Omit the calibration branch when $`M=0`$. At $`b=0`$, define $`U=0`$ explicitly without evaluating $`0/0`$.

**Theorem.** There are constants $`0\lt c\lt C\lt\infty`$ and $`N_0\ge4`$, depending only on $`\epsilon,V,b_{\max},q_0`$, such that for every $`N\ge N_0`$, every integer $`M\ge0`$, every allowed $`b`$ and every known schedule $`0\lt v_i\le V`$:

1. If $`0\lt h\le cR_Q`$, then $`\mathcal R_Q(h)\gt \epsilon`$.
2. If $`CR_Q\le h\le q_0`$, then $`\mathcal R_Q(h)\le\epsilon`$.

The upper assertion applies only when its interval is nonempty. These are uniform orders, not leading minimax constants. The exact conversion to physical separation is $`s=2\sqrt2\sigma\sqrt q`$.

The root $`r_0`$ is the physical timing and jitter floor at worst-case variance $`b`$. The three terms in $`U`$ are the supplied variance bound, calibration information and a fourth-order shape signature. A [covariance extraction argument](joint-converse.md#2-independent-noise-inside-the-brownian-covariance) proves the nuisance converse for the whole correlated record. A [weighted relative-mode statistic](joint-receiver.md#4-weighted-shape-information) attains it. The general attaining construction resolves the full Hermite–Gaussian mode index; the four-outcome claim is restricted to the [close-doublet corollary](joint-receiver.md#5-four-outcome-close-doublet-receiver).

If the actual variance $`w`$ is known, the timing law instead is

```math
\sum_{i=2}^{N}\frac{h^2}{h+w+v_i}=\Theta(1).
```

The [known-jitter proof](joint-converse.md#1-known-jitter-physical-floor) extends the original timing argument. Perfect knowledge of $`w`$ does not remove physical jitter.

## 4. Direct imaging

Put $`K=NM/(N+M)`$, with $`K=0`$ when $`M=0`$, and $`L=\max\{\sqrt N,K\}`$. For every bounded schedule, matching position-detection orders are

```math
R_{\mathrm{DI}}=N^{-1/2}+\min\{b,L^{-1/2}\}.
```

The same lower/upper testing convention applies. A classical Brownian-addition channel transfers the independent-jitter lower bound. Relative-position second moments and a fourth cumulant attain the order; [the derivation](joint-receiver.md#6-direct-position-detection) retains the optical variance baseline. Hence the quantum order has additional schedule dependence, while the position-data order does not under the fixed upper gap bound.

## 5. Ownership and reading route

This repository is the authoritative home of the joint schedule-dependent theorem and receiver. Its sister [Quantum-Imaging-Calibration](https://github.com/GoGoKo699/Quantum-Imaging-Calibration) owns the independent unknown-jitter experiment and exact Gaussian collision kernel imported in the converse. The imported kernel is pinned at [commit 275c70d6](https://github.com/GoGoKo699/Quantum-Imaging-Calibration/blob/275c70d6fa9f5a205aab0df35cfe8a7b50aa1635/science/collision-kernel.md). The notation conversion is $`q_{\mathrm{Calibration}}=2q`$, $`B_{\mathrm{Calibration}}=2w`$. A shared theorem has one proof home; each repository retains its own model and consequences.

Read the [joint converse](joint-converse.md), [joint receiver](joint-receiver.md), [crossover regimes](jitter-calibration-regimes.md) and [physical interface](physical-interface.md). The [related-work account](../references/related-work.md) credits Brownian-imaging, two-photon-reference and HG-moment antecedents separately. Unknown diffusion, non-Gaussian jitter, calibration mismatch, unbounded general schedules, trajectory-monitor references and optical mode/visibility restrictions are outside this theorem.
