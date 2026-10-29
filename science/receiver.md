# A receiver using disjoint photon pairs

The schedule information scale in the [main theorem](model-and-theorem.md) is attainable by pair measurements that require no centroid estimate. The construction chooses one of two disjoint adjacent-pair matchings from the known schedule, measures the antisymmetric projector on each selected pair, and applies a likelihood-ratio test to the independent binary outcomes. The matching and the test use the design threshold $`h`$, not the unknown actual separation parameter $`q`$.

Throughout this page,

```math
q=\frac{s^2}{8\sigma^2},\qquad
v_i=\frac{D}{\sigma^2}(t_i-t_{i-1}),\qquad
I_N(h;v)=\sum_{i=2}^{N}\frac{h^2}{v_i+h}.
```

The Gaussian intensity point-spread function has physical variance $`\sigma^2`$; physical Brownian increments have variance $`2D\Delta t`$. The receiver has the timestamped spatial registers described in the [model](model-and-theorem.md). For the deterministic result, $`0<v_i\le V`$ and $`0<h\le q_0`$, with $`V,q_0`$ fixed. The actual alternative may be any $`q\ge h`$.

## 1. Exact probability for a pair

In dimensionless position coordinates, the displaced Gaussian wave packet is $`|z\rangle=e^{-izP}|0\rangle`$ and

```math
|\langle z|z'\rangle|^2=e^{-(z-z')^2/2}.
```

Let $`S`$ interchange two spatial registers. Measure the projectors

```math
\Pi_- =\frac{\mathbf 1-S}{2},\qquad
\Pi_+ =\frac{\mathbf 1+S}{2}.
```

Write the antisymmetric outcome as $`Y=1`$. For a particular pair of pure wave packets, its probability is

```math
\Pr(Y=1\mid z,z')=\frac{1-e^{-(z-z')^2/2}}2.
```

The Brownian displacement difference within a pair is $`Z\sim N(0,v)`$. The source-label difference is zero with probability $`1/2`$ and is each of $`\pm2\sqrt q`$ with probability $`1/4`$. The Gaussian integral

```math
\mathbb E\,e^{-(Z+a)^2/2}
 =\frac{e^{-a^2/[2(1+v)]}}{\sqrt{1+v}}
```

therefore gives the exact response

```math
\boxed{\displaystyle
p_v(q):=\Pr_q(Y=1)
 =\frac12-\frac{1+e^{-2q/(1+v)}}{4\sqrt{1+v}}.}
```

In particular,

```math
p_v(0)=\frac{1-(1+v)^{-1/2}}2,
\qquad
p_v(q)-p_v(0)
 =\frac{1-e^{-2q/(1+v)}}{4\sqrt{1+v}},
```

and

```math
\frac{\partial p_v(q)}{\partial q}
 =\frac{e^{-2q/(1+v)}}{2(1+v)^{3/2}}>0.
```

The common centroid cancels from this response exactly. No small-motion expansion has been used.

### Why the selected outcomes are independent

Given the complete Brownian path and source labels, the photon state is a tensor product, so measurements on disjoint pairs have conditionally independent outcomes. The conditional probability for a pair depends only on that pair's internal Brownian increment and its two independent source labels. Disjoint adjacent pairs use disjoint Brownian increments and disjoint labels. Averaging consequently preserves the product distribution

```math
\Pr_q\{Y_i=y_i:i\in M\mid v\}
 =\prod_{i\in M}p_{v_i}(q)^{y_i}[1-p_{v_i}(q)]^{1-y_i}.
```

Here $`M`$ is a matching of adjacent edges, and edge $`i`$ denotes the pair $`(i-1,i)`$. The absolute centroid values of different pairs remain correlated; that correlation does not enter these invariant measurement probabilities. Conditioning only on timestamps does **not** make arbitrary measurements on different photons independent.

## 2. The pair's testing information

Use the squared Hellinger convention

```math
H^2(P,Q)=1-A(P,Q),\qquad
A(P,Q)=\sum_y\sqrt{P(y)Q(y)}.
```

For $`p=p_v(0)`$, $`r=p_v(h)`$, and $`\delta=r-p`$,

```math
H^2(\operatorname{Ber}(p),\operatorname{Ber}(r))
 =\frac{\delta^2}{2}
 \left\{\frac{1}{(\sqrt p+\sqrt r)^2}
       +\frac{1}{(\sqrt{1-p}+\sqrt{1-r})^2}\right\}.
```

The expression is interpreted by continuity if $`v=0`$. For $`0\le v\le V`$ and $`0<h\le q_0`$, set

```math
a=\frac{e^{-2q_0}}{2(1+V)^{3/2}},\qquad
b=\min\left\{a,
 \frac{1}{2\sqrt{1+V}(\sqrt{1+V}+1)}\right\}.
```

The response formula gives

```math
ah\le\delta\le\frac h2,\qquad
b(v+h)\le r\le\frac v4+\frac h2\le\frac{v+h}{2},
\qquad r\le\frac12.
```

For the lower bound on $`p_v(0)`$, use the identity

```math
p_v(0)=\frac{v}{2\sqrt{1+v}(\sqrt{1+v}+1)}.
```

Substitution in the Hellinger expression proves

```math
\boxed{\displaystyle
c^{\rm pair}_{V,q_0}\frac{h^2}{v+h}
 \le H^2(\operatorname{Ber}(p_v(0)),\operatorname{Ber}(p_v(h)))
 \le C^{\rm pair}_{V,q_0}\frac{h^2}{v+h},}
```

where one valid, conservative choice is

```math
c^{\rm pair}_{V,q_0}=\frac{a^2}{4}
 =\frac{e^{-4q_0}}{16(1+V)^3},\qquad
C^{\rm pair}_{V,q_0}=\frac1{8b}+\frac{V+q_0}{16}.
```

Indeed, the first squared-root term is at least $`\delta^2/(8r)`$. For the upper bound, its denominator is at least $`r`$, and the second denominator is at least $`2`$. These inequalities remain uniform as both $`v`$ and $`h`$ tend to zero. The constants establish the order law; they are not proposed as optimized experimental performance constants.

## 3. Choose the matching at the design threshold

The adjacent edges partition into

```math
M_{\rm even}=\{2,4,6,\ldots\}\cap\{2,\ldots,N\},\qquad
M_{\rm odd}=\{3,5,7,\ldots\}\cap\{2,\ldots,N\}.
```

Both are matchings. At the specified threshold $`h`$, choose the matching with the larger weight

```math
W_M(h)=\sum_{i\in M}\frac{h^2}{v_i+h}.
```

Because the two weights sum to $`I_N(h;v)`$, the chosen matching satisfies

```math
W_M(h)\ge\frac12 I_N(h;v).
```

This choice needs the known schedule and the desired testing threshold. It requires no estimate of the centroid, Brownian trajectory, or true separation. The model permits storing the spatial registers until the matching is selected; an implementation must supply the corresponding routing and storage capabilities.

## 4. A complete test and its error guarantee

For the measured bits, calculate the log likelihood ratio for the simple hypotheses $`q=h`$ and $`q=0`$:

```math
\ell_h(Y)=\sum_{i\in M}
 \left[Y_i\log\frac{p_{v_i}(h)}{p_{v_i}(0)}
 +(1-Y_i)\log\frac{1-p_{v_i}(h)}{1-p_{v_i}(0)}\right].
```

Reject the null if $`\ell_h(Y)\ge0`$. Ties may instead be randomized; the bounds below hold for either convention. Since the selected outcomes are independent, the affinity of their distributions is

```math
A_M(0,h)=\prod_{i\in M}
 A(\operatorname{Ber}(p_{v_i}(0)),\operatorname{Ber}(p_{v_i}(h)))
 \le \exp\left[-\sum_{i\in M}H_i^2\right].
```

The likelihood-ratio test with threshold one has

```math
\Pr_0(\ell_h\ge0)+\Pr_h(\ell_h<0)
 =\sum_y\min\{P_0(y),P_h(y)\}
 \le A_M(0,h).
```

Consequently, each of its two errors is at most

```math
\boxed{\displaystyle
\exp[-c^{\rm pair}_{V,q_0}I_N(h;v)/2].}
```

In particular, both errors are at most a prescribed $`\eta\in(0,1/2)`$ whenever

```math
I_N(h;v)\ge\frac{2}{c^{\rm pair}_{V,q_0}}\log\frac1\eta.
```

The probability law and bound are uniform over every initial centroid $`m\in\mathbb R`$.

### The same test handles every larger separation

The coefficient of each $`Y_i`$ in $`\ell_h`$ is positive, because $`p_{v_i}(h)>p_{v_i}(0)`$. Thus the rejection event is increasing in every bit. For any actual $`q\ge h`$, the independent Bernoulli variables with probabilities $`p_{v_i}(q)`$ stochastically dominate those with probabilities $`p_{v_i}(h)`$. The acceptance probability can only decrease. Therefore

```math
\sup_{m\in\mathbb R,\ q\ge h}\Pr_{q,m}(\text{accept null})
 \le \exp[-c^{\rm pair}_{V,q_0}I_N(h;v)/2].
```

Only the **design threshold** is restricted to $`h\le q_0`$; the actual composite alternative has no upper bound. Pairing at the unknown actual $`q`$ is unnecessary.

## 5. Optical meaning and scope

For compatible optical modes, two-photon interference can realize the symmetric/antisymmetric comparison. Its use for static imaging and centroid-independent spectrum information is inherited; see [de Almeida, Lewenstein, and Skotiniotis](https://doi.org/10.1103/9w4p-5d9j) and the [related-work comparison](../references/related-work.md). The added result here is its schedule-dependent performance under shared Brownian motion, together with the [collective converse](collective-converse.md) for the entire correlated record.

The formal receiver acts on supplied spatial registers. A physical realization must make the selected photons compatible in their other degrees of freedom, implement any required delays or storage, and account for loss. Exact timestamps alone do not provide those capabilities. The [physical interface](physical-interface.md) records these assumptions, including why arbitrarily close Poisson arrivals require a separate temporal-mode qualification.

The deterministic calculations in [verify_receiver.py](../verification/verify_receiver.py) check the Gaussian integration, Hellinger normalization and bounds, finite likelihood-ratio risks, and the random-gap calculations. They corroborate these formulas; the uniform guarantees follow from the arguments above.
