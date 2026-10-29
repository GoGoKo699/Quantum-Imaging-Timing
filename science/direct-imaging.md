# Direct imaging: optimal order from position data

Direct imaging measures each photon's position. The complete ordered position record and all timestamps may then be processed jointly, adaptively or with arbitrary classical computation. This page bounds the best test within that observation model and supplies a uniform attaining order.

The benchmark concerns arbitrary classical processing **after position measurement**. It does not identify every possible single-photon optical measurement with direct imaging.

## 1. Observation law and minimax risk

Use the dimensionless conventions of [Model and theorem](model-and-theorem.md). Direct imaging produces

```math
Z_i=m+B_i+\sqrt q S_i+\varepsilon_i,
\qquad
\varepsilon_i\sim\mathcal N(0,1/2),
```

where the $`\varepsilon_i`$ and fair source signs $`S_i`$ are independent of each other and of the Brownian increments. The initial centroid $`m\in\mathbb R`$ is unrestricted and the known schedule satisfies $`0<v_i\le V`$.

For a randomized decision rule $`\phi(Z_1,\ldots,Z_N)\in[0,1]`$, define

```math
\mathcal R_{\rm DI}(h;v)
=\inf_\phi\max\left\{
\sup_m\mathbb E_{0,m}\phi,
\sup_{m,\ q\ge h}\mathbb E_{q,m}(1-\phi)
\right\}.
```

The decision $`1`$ means two separated sources. The alternative $`q\ge h`$ is unbounded.

## 2. Converse for all position-data processing

First omit the Brownian path and fix the allowed nuisance value $`m=0`$. A single raw position under $`q=0`$ has the density

```math
p_0(z)=\pi^{-1/2}e^{-z^2}.
```

Under separation parameter $`q`$, the density is

```math
p_q(z)=\tfrac12p_0(z-\sqrt q)+\tfrac12p_0(z+\sqrt q).
```

Its likelihood ratio is

```math
\frac{p_q(z)}{p_0(z)}=e^{-q}\cosh(2\sqrt q\,z).
```

Using the Gaussian moment-generating function gives the exact collision integral

```math
\int\frac{p_q(z)^2}{p_0(z)}\,dz
=\cosh(2q).
```

With natural logarithms, Jensen's inequality under $`p_q`$ therefore gives

```math
D(p_q\|p_0)
\le\log\!\int\frac{p_q^2}{p_0}
=\log\cosh(2q)
\le2q^2.
```

The last inequality follows from $`\tanh x\le x`$ for $`x\ge0`$ by integration. For $`N`$ independent observations before the common motion is added,

```math
D(p_q^{\otimes N}\|p_0^{\otimes N})\le2Nq^2.
```

The actual Brownian vector is subsequently added using the same probability kernel under both hypotheses. Relative entropy contracts under this common kernel. Pinsker's inequality thus bounds the total variation distance between the actual position records, still at the fixed allowed centroid $`m=0`$, by

```math
\mathrm{TV}(P_{q,0}^{v},P_{0,0}^{v})\le q\sqrt N.
```

Every classical decision rule is a further stochastic map. Restricting the composite alternative to $`q=h`$ and using the optimal equal-prior binary testing error gives

```math
\boxed{\displaystyle
\mathcal R_{\rm DI}(h;v)\ge\frac12(1-h\sqrt N)_+.}
```

This lower bound needs no maximum-gap assumption. It remains valid when the complete timestamps are known, and even when the initial centroid is revealed. Brownian motion can only reduce the distinguishability of these already measured position records.

## 3. A centroid-independent pair statistic

Take the disjoint adjacent pairs $`(1,2),(3,4),\ldots`$. Put $`M=\lfloor N/2\rfloor`$, and let $`v_j^{\rm pair}`$ denote the variance of the Brownian increment within pair $`j`$. Define

```math
Y_j=Z_{2j}-Z_{2j-1},
\qquad
w_j=1+v_j^{\rm pair}.
```

The unknown initial position cancels. Conditional absolute centroid positions also cancel. Each difference has the representation

```math
Y_j=G_j+\sqrt q\,(S_{2j}-S_{2j-1}),
\qquad
G_j\sim\mathcal N(0,w_j).
```

The pair differences are independent: they use disjoint shot-noise variables, source signs and within-pair Brownian increments. They can have different known $`w_j`$, with $`1<w_j\le1+V`$.

The source-sign difference is zero with probability $`1/2`$ and $`\pm2`$ with probability $`1/4`$ each. Its second and fourth moments are $`2`$ and $`8`$. Consequently

```math
\mathbb E_qY_j^2=w_j+2q,
```

```math
\mathbb E_qY_j^4=3w_j^2+12w_jq+8q^2,
```

and

```math
\mathrm{Var}_q(Y_j^2)=2w_j^2+8w_jq+4q^2.
```

No small-separation approximation is used in these identities.

## 4. Uniform test for every $`q\ge h`$

Consider the centered statistic

```math
\widehat A=\frac1M\sum_{j=1}^{M}(Y_j^2-w_j),
\qquad
\text{report }H_1\text{ when }\widehat A\ge h.
```

It has mean $`0`$ under the null and mean $`2q`$ under the alternative. Let $`W=1+V`$. Independence and the variance formula give

```math
\mathrm{Var}_q(\widehat A)
\le\frac{2W^2+8Wq+4q^2}{M}.
```

Chebyshev's inequality bounds the type-I error by

```math
\sup_m\Pr_{0,m}(\widehat A\ge h)
\le\frac{2W^2}{Mh^2}.
```

For any actual $`q\ge h`$, the distance from the alternative mean to the threshold is $`2q-h\ge q`$. Hence

```math
\begin{aligned}
\sup_m\Pr_{q,m}(\widehat A<h)
&\le\frac{2W^2+8Wq+4q^2}{M(2q-h)^2}\\
&\le\frac1M\left(\frac{2W^2}{q^2}+\frac{8W}{q}+4\right)\\
&\le\frac1M\left(\frac{2W^2}{h^2}+\frac{8W}{h}+4\right).
\end{aligned}
```

The bound is uniform as $`q\to\infty`$; no bounded-alternative assumption is required. In particular, for a design threshold $`0<h\le q_0`$,

```math
\boxed{\displaystyle
\mathcal R_{\rm DI}(h;v)
\le\min\!\left\{\frac12,
\frac{2(1+V)^2+8(1+V)q_0+4q_0^2}{\lfloor N/2\rfloor h^2}\right\}.}
```

The minimum with $`1/2`$ is attained by choosing the better of this test and a coin-flip decision using the known values of $`N,V,h,q_0`$.

## 5. What the benchmark implies

For fixed $`V,q_0`$ and any fixed target error strictly between zero and $`1/2`$, the lower and upper bounds match at

```math
h\asymp N^{-1/2},
\qquad
s\asymp\sigma N^{-1/4}.
```

Arbitrarily short Brownian gaps do not remove the position-measurement noise: every pair difference still contains the variance-one shot-noise term in $`w_j=1+v_j^{\rm pair}`$. This explains why timing can change the exponent attainable by the [quantum pair receiver](receiver.md) while the optimal order from direct position data remains unchanged.

This comparison charges the same detected photons and uses the same schedule, point-spread response and Brownian law for both receiver classes. It concerns spatial resolution from those inputs. It does not assume that a chosen acquisition schedule is free to generate, or that any particular physical implementation of the quantum pair comparison is lossless.

Return to [Model and theorem](model-and-theorem.md) or continue to [Timing regimes](timing-regimes.md).
