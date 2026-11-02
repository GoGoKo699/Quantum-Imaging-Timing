# Relative-mode receiver with unknown independent jitter

[Joint model and theorem](joint-model.md) · [Converse](joint-converse.md) · [Crossover regimes](jitter-calibration-regimes.md)

Common translations can be removed by comparing two photons, but independent jitter remains in their relative coordinate. The remaining three-point source distribution has a fourth-order shape signature. This page constructs a receiver that uses that signature or the charged calibration sample, according to the known schedule and budgets.

The general construction is a joint spatial measurement followed by full Hermite–Gaussian (HG) mode-index detection. Section 5 gives a four-outcome version for close doublets. Neither construction is identified with an ordinary HOM port measurement alone; see the [physical interface](physical-interface.md#7-relative-coordinate-access-for-the-joint-frontier).

## 1. Independent relative spatial modes

The odd and even adjacent-edge matchings partition all $`N-1`$ photon gaps. Choose one matching using the design rule below. For each selected edge $`i`$, apply the orthogonal coordinate unitary that maps two pure displacement centers to

```math
(a_1,a_2)\longmapsto
\left(\frac{a_1+a_2}{\sqrt2},\frac{a_2-a_1}{\sqrt2}\right).
```

The product vacuum is invariant under this transformation. Discard the sum mode and retain the relative mode. Its displacement is

```math
X_i=G_i+R_i,\qquad G_i\sim\mathcal N(0,d_i+w),\qquad d_i=\frac{v_i}{2},
```

```math
\Pr(R_i=0)=\frac12,\qquad
\Pr(R_i=\sqrt{2q})=\Pr(R_i=-\sqrt{2q})=\frac14.
```

The unknown absolute centroid cancels exactly. Selected relative modes are independent because they depend only on disjoint internal Brownian increments, independent jitter variables and source signs. The discarded sum modes and pair centroids may remain correlated; their independence is not required.

This three-point distribution has variance $`q`$ and fourth cumulant $`-q^2`$. It is not the binary displacement distribution of a single signal photon in the independent-jitter model.

## 2. Exact corrected HG moments

For a relative displacement $`X_i=x`$, the HG mode index satisfies the established Gaussian overlap identity

```math
Q_i\mid X_i=x\sim\mathrm{Poisson}(x^2/2).
```

Here $`Q_i`$ counts oscillator excitation of the supplied transverse spatial register, not additional photons. Resolving its mode index consumes the same two input photons. The HG factorial-moment identity and its imaging use are inherited from [Tsang's semiparametric analysis](https://arxiv.org/pdf/1906.04578v2), Eqs. (7.17)–(7.19).

Set $`\mu=w+q`$. The relative displacement moments are

```math
\mathbb E X_i^2=d_i+\mu,\qquad
\mathbb E X_i^4=3(d_i+\mu)^2-q^2.
```

Define observed, gap-corrected variables

```math
A_i=2Q_i-d_i,
\qquad
B_i=\frac43Q_i(Q_i-1)-4d_iQ_i+d_i^2.
```

Poisson factorial moments give the exact identities

```math
\mathbb E A_i=\mu,\qquad
\mathbb E B_i=\mu^2-\frac{q^2}{3}.
```

The means have no unknown gap dependence. The exact first variance, writing $`t=d_i+w+q`$, is

```math
\mathrm{Var}(A_i)=2t+2t^2-q^2\le C t.
```

All constants below depend only on the fixed bounded parameter ranges. For $`1\le k\le4`$, the source moments $`\mathbb E R_i^{2k}=2^{k-1}q^k`$ are no larger than the corresponding Gaussian moments of variance $`q`$. Gaussian convolution consequently gives $`\mathbb E X_i^{2k}\le(2k-1)!!t^k`$. Using

```math
[Q(Q-1)]^2=(Q)_4+4(Q)_3+2(Q)_2
```

and $`d_i\le t`$ shows

```math
\mathrm{Var}(A_i)\le C(b+d_i+q),\qquad
\mathrm{Var}(B_i)\le C(b+d_i+q)^2.
```

The calibration HG index satisfies

```math
\mathbb E(2Q_c)=w,\qquad
\mathrm{Var}(2Q_c)=2w+2w^2\le Cw.
```

Thus $`2\overline Q_c`$ estimates the variance with mean-square error at most $`Cb/M`$. No signal Brownian variance is charged to this stationary calibration source, and no realized signal jitter is inferred.

## 3. Known-bound and calibration tests

For design threshold $`h`$, select the adjacent matching maximizing

```math
Z_h=\sum_{i\in\mathcal M}\frac1{b+d_i+h},\qquad
\lambda_i=\frac{(b+d_i+h)^{-1}}{Z_h}.
```

The two matchings partition the edge sum, so the selected matching captures at least half. Since $`d_i=v_i/2`$, $`h^2Z_h`$ is comparable to the full timing information $`\mathcal I_b(h;v)`$. Also $`\sum\lambda_i=1`$ and

```math
\sum_i\lambda_i^2\le\frac1{(b+h)Z_h}.
```

For every actual alternative $`q\ge h`$,

```math
b+d_i+q\le\frac qh(b+d_i+h),
\qquad
\mathrm{Var}\!\left(\sum_i\lambda_i A_i\right)
\le\frac{Cq}{hZ_h}.
```

Under the null the variance is at most $`C/Z_h`$. The corrected weighted signal mean has null mean at most $`b`$ and alternative mean $`w+q\ge q`$.

**Known-bound branch.** Reject above $`h/2`$, using $`h\ge4b`$. Both mean gaps are at least a fixed multiple of $`h`$ under the null and of $`q`$ under the alternative. Chebyshev bounds both errors by $`C/(h^2Z_h)`$. Since $`\mathcal I_b(ar_0;v)\ge a\mathcal I_b(r_0;v)=a`$ for $`a\ge1`$, this branch succeeds at

```math
h\ge C(r_0+b).
```

**Calibration branch.** For $`M\gt 0`$, reject when

```math
\sum_i\lambda_i A_i-2\overline Q_c\gt \frac h2.
```

Its null mean is zero and alternative mean $`q`$. The extra independent variance is at most $`Cb/M`$. Both errors are therefore controlled when

```math
h\ge C\left(r_0+\sqrt{\frac bM}\right).
```

These are uniform tests over the full local separated alternative; the weights depend on the supplied schedule, bound and design threshold, never on actual $`q,w`$.

## 4. Weighted shape information

Select the parity matching maximizing

```math
S=\sum_{i\in\mathcal M}(b+d_i)^{-2},\qquad
\lambda_i=\frac{(b+d_i)^{-2}}S,\qquad
\tau=S^{-1/4},\qquad P_2=\sum_i\lambda_i^2.
```

$`S`$ is comparable to the full $`S_2(v,b)`$. Use this branch only if $`\tau\le b`$; otherwise the known-bound branch attains the needed order near the crossover. Form

```math
U_{\mathrm{pair}}
=\frac{\sum_{i\ne j}\lambda_i\lambda_j A_iA_j}{1-P_2},
\qquad
T=\sum_i\lambda_i B_i-U_{\mathrm{pair}}.
```

Independence gives $`\mathbb E U_{\mathrm{pair}}=\mu^2`$ and $`\mathbb E T=-q^2/3`$. Excluding the diagonal and retaining $`1-P_2`$ remove the bias of squaring a sample mean. They cannot be dropped for a heterogeneous schedule.

Let $`t_i=b+d_i`$ and $`A_3=\sum\lambda_i^2t_i`$. In the useful shape regime,

```math
\max_i\lambda_i\le\frac1{b^2S}\le\tau^2,\qquad
P_2\le\tau^2,\qquad
\sum_i\lambda_i^2t_i^2=\frac1S=\tau^4,
```

```math
A_3=\frac{\sum_i t_i^{-3}}{S^2}\le S^{-1/2}=\tau^2,
\qquad b^2A_3\le\frac bS,\qquad b^2P_2\le\frac1S.
```

The bound on $`A_3`$ is the finite-sequence norm inequality $`\sum x_i^3\le(\sum x_i^2)^{3/2}`$. Bounded gaps give $`S\ge cN`$; hence $`P_2\le1/2`$ for sufficiently large uniform $`N_0`$. No unmentioned effective-sample-size promise is needed.

To bound variance write $`A_i=\mu+\xi_i`$, with centered independent $`\xi_i`$. The linear and degenerate parts of $`U_{\mathrm{pair}}-\mu^2`$ are

```math
\frac{2\mu}{1-P_2}\sum_i\lambda_i(1-\lambda_i)\xi_i,
\qquad
\frac1{1-P_2}\sum_{i\ne j}\lambda_i\lambda_j\xi_i\xi_j.
```

They are uncorrelated. The weighted $`B`$ variance is at most $`C(\tau^4+q^2P_2)`$. The linear variance is at most $`C(b+q)^2(A_3+qP_2)`$, and the degenerate variance at most $`C(A_3+qP_2)^2`$. Expanding these terms and applying the displayed bounds, with bounded $`b,q`$, gives

```math
\boxed{\mathrm{Var}(T)\le C(\tau^4+q^2\tau^2)}
```

for every $`0\le q\le q_0`$. Covariance with the weighted $`B`$ term is absorbed by Cauchy–Schwarz. In particular, the bound is valid even when $`q`$ is much larger than $`b`$.

Reject when $`T\lt-h^2/6`$. The alternative mean-to-threshold gap is at least $`q^2/6`$, so the null and worst alternative errors are bounded by

```math
C\left[\left(\frac\tau h\right)^4+
\left(\frac\tau h\right)^2\right].
```

Thus $`h\ge C\tau`$ suffices. The same matching and HG records implement the whole shape test; no second incompatible pair measurement is required.

Choose the smallest certified bound, calibration or shape threshold from known data. Use the actual selected-matching $`S`$ in the shape branch. If $`S_2^{-1/4}\le b`$ but its constant-factor matching scale exceeds $`b`$, then $`b\le C S_2^{-1/4}`$ and the bound branch already has the desired order. This proves attainment at $`r_0+\min\{b,\sqrt{b/M},S_2^{-1/4}\}`$ with the endpoint conventions in the model.

## 5. Four-outcome close-doublet receiver

Suppose $`N=2n`$ photons arrive in disjoint doublets with internal variances $`\delta_j\le c/N`$. Set $`d=\max_j\delta_j/2`$. After the relative transformation, add independent receiver-controlled Gaussian variance $`d-\delta_j/2`$ to each signal relative mode and variance $`d`$ to each calibration photon. Both streams now share an effective Gaussian variance $`r=w+d`$. This operation adds known noise; it removes none and discards no photons.

Retain four outcomes, HG0, HG1, HG2 and all remaining modes. Put $`D=1+r`$, $`e=e^{-q/D}`$, $`a=r/(2D)`$, $`z=q/D^2`$ and $`c_r=D^{-1/2}`$. Exact probabilities are

```math
p_0=\frac{c_r(1+e)}2,\qquad
p_1=\frac{c_r[a(1+e)+ez]}2,
```

```math
p_2=\frac{c_r[\tfrac32a^2(1+e)+3eaz+\tfrac12ez^2]}2.
```

Their invariant is

```math
\theta=p_0p_2-\frac32p_1^2
=-\frac{q^2e(2e-1)}{8D^5}.
```

For $`q\le q_0\le1/4\lt\log2`$, this is uniformly negative and comparable to $`-q^2`$. The unbiased statistic $`[n_0n_2-\tfrac32n_1(n_1-1)]/[n(n-1)]`$ has variance at most $`3(r+q)^2/n`$: the usual degree-two U-statistic decomposition applies, with $`p_1\le(r+q)/2`$ and $`p_2\le3(r+q)^2/8`$.

Known-bound excitation, signal-minus-calibration excitation and this shape statistic respectively have sufficient thresholds

```math
n^{-1}+b+d,\qquad
n^{-1}+\sqrt{\frac{b+d}{K_n}},\qquad
n^{-1/2}+\sqrt{b+d}\,n^{-1/4},
\qquad K_n=\frac{nM}{n+M}.
```

Disable calibration at $`M=0`$. If $`b\le1/n`$, the bound branch is $`O(1/n)`$ because $`d=O(1/n)`$. If $`b\ge1/n`$, then $`b+d=O(b)`$; minimizing the three branches gives

```math
R_Q=N^{-1}+\min\left\{b,
\sqrt{\frac b{\max\{\sqrt N,NM/(N+M)\}}}\right\}.
```

The matching lower bound follows by applying common Brownian translations to the sister repository's independent-jitter experiment. Its parameter conversion is $`q_{\mathrm{Calibration}}=2q`$ and $`b_{\mathrm{Calibration}}=2b`$, which changes constants only. This direct corollary needs no upper bound on between-doublet motion. The finite invariant's local sign domain is essential; no all-separation four-category claim is made.

## 6. Direct position detection

Measure each photon in position and take the same disjoint relative differences. For edge $`i`$, their distribution is $`Y_i=G_i^{\mathrm{pos}}+R_i`$, with Gaussian variance $`1/2+w+d_i`$. Known classical Gaussian randomization may equalize all selected $`d_i`$ to their maximum $`d\le V/2`$; it changes only bounded constants. Let $`t=1/2+w+d`$. Then

```math
\mathbb E Y^2=t+q,\qquad
\mathbb E Y^4=3(t+q)^2-q^2,
\qquad \mathbb E Y^8\le105(t+q)^4.
```

There is a fixed positive optical variance even at zero physical jitter. A sample second moment, with its known optical and Brownian terms subtracted, has $`O(1/n)`$ variance. The known-bound test therefore needs $`b+n^{-1/2}`$. Subtract the independent calibration position second moment, with its known optical baseline accounted for, to obtain threshold $`n^{-1/2}+M^{-1/2}`$. The unbiased fourth-cumulant statistic has mean $`-q^2`$ and variance $`O(1/n)`$, giving threshold $`n^{-1/4}`$. These bounds are uniform on the fixed local range.

Selecting the best branch yields $`N^{-1/2}+\min\{b,[\max(\sqrt N,K)]^{-1/2}\}`$, where $`K=NM/(N+M)`$. A classical channel adds the same correlated Brownian vector to both hypotheses of the sister repository's independent position experiment, so its all-processing lower bound transfers. This proves the matching DI law for every bounded schedule. A known variance estimate removes uncertainty in a moment, not the positive variance of each observed position.
