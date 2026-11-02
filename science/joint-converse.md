# Converse with independent jitter and finite calibration

[Joint model and theorem](joint-model.md) · [Attaining receiver](joint-receiver.md)

The joint frontier has a physical floor and a nuisance-variance obstruction. The first extends the Brownian timing converse to known jitter. The second extracts independent Gaussian noise from the Brownian covariance, applies the sister repository's exact collision kernel coordinatewise, and then restores the residual correlations through a parameter-independent channel. Both statements concern the full available quantum record before a receiver is chosen.

## 1. Known-jitter physical floor

Suppose the actual independent jitter variance $`w`$ is known. Use the same Gaussian prior $`m\sim\mathcal N(0,V)`$ for the unrestricted initial centroid as in the [original converse](collective-converse.md). Its Brownian displacement covariance is

```math
C=L\operatorname{diag}(V,v_2,\ldots,v_N)L^{\mathsf T}.
```

Let $`\bar\rho_q`$ denote the prior-averaged signal state; the identical calibration factors may be omitted from state-distance comparisons. The averaged null Gaussian spatial state has displacement covariance $`C+wI`$. Replacing each binary source shift $`\pm\sqrt q`$ by an independent Gaussian of variance $`q`$ gives the comparison state with covariance $`C+(w+q)I`$. The original trace-norm replacement estimate still gives

```math
T(\bar\rho_q,G_{C+(w+q)I})\le\frac32Nq^2,
\qquad T(\rho,\tau)=\frac12\|\rho-\tau\|_1.
```

Additional Gaussian jitter is a parameter-independent channel and cannot increase this remainder. Calibration factors are identical under the two hypotheses when $`w`$ is supplied.

The same Gaussian fidelity calculation and Brownian precision argument, now with regularizer $`w+q`$, yield

```math
T(G_{C+wI},G_{C+(w+q)I})^2
\le\frac{q^2}{2}\operatorname{tr}(C+(w+q)I)^{-1},
```

```math
\operatorname{tr}(C+(w+q)I)^{-1}
\le2\sum_{i=1}^{N}\frac1{u_i+w+q},
\qquad u_1=V,\quad u_i=v_i\ (i\ge2).
```

The initial-prior term is bounded by the real-gap sum since $`v_i\le V`$. For $`0\lt q\le q_0`$,

```math
Nq^2\le\frac{N}{N-1}(V+b_{\max}+q_0)
\sum_{i=2}^{N}\frac{q^2}{v_i+w+q}.
```

Thus small $`\mathcal I_w(q;v)=\sum_{i=2}^{N}q^2/(v_i+w+q)`$ makes the entire-state trace distance small. The Helstrom bound gives a fixed-error lower obstruction at its unit root.

For completeness, the exact adjacent-pair SWAP response is

```math
p_-(q;v,w)=\frac12-
\frac{1+e^{-2q/(1+v+2w)}}{4\sqrt{1+v+2w}}.
```

Independent jitters add variance $`2w`$ to the within-pair difference. The original independent-matching likelihood-ratio argument therefore attains $`\sum q^2/(v_i+2w+q)`$, comparable to $`\mathcal I_w`$ on the bounded range. The known-jitter operational law is

```math
\mathcal I_w(h;v)=\Theta(1).
```

Giving the value $`w=b`$ to the receiver can only make the unknown-jitter problem easier. Consequently the root $`r_0`$ in the [joint theorem](joint-model.md#3-joint-frontier) is a lower bound even with arbitrarily many calibration photons. This bound does not interpret calibration as cancellation of a realized displacement.

## 2. Independent noise inside the Brownian covariance

For the nuisance lower bound, again give the unknown initial centroid a common prior of variance $`V`$. Set

```math
u_1=V,\quad u_i=v_i\ (2\le i\le N),\quad
u_{N+1}=\infty.
```

For $`x_0=0`$, Brownian precision has quadratic form

```math
x^{\mathsf T}C^{-1}x
=\frac{x_1^2}{u_1}
+\sum_{i=2}^{N}\frac{(x_i-x_{i-1})^2}{u_i}
\le2\sum_{i=1}^{N}
\left(\frac1{u_i}+\frac1{u_{i+1}}\right)x_i^2.
```

Define

```math
c_i=\left[2\left(\frac1{u_i}+\frac1{u_{i+1}}\right)\right]^{-1}.
```

Order reversal under inversion gives $`C\succeq\operatorname{diag}(c_i)`$. Therefore the prior-averaged correlated signal is a Gaussian displacement channel of positive covariance $`C-\operatorname{diag}(c_i)`$ applied to independent signal registers whose Gaussian noises have variances $`c_i+w`$. The channel is independent of $`q,w`$ and acts only on signal registers. Calibration remains the original stationary point source of noise variance $`w`$.

For $`i\lt N`$, $`c_i`$ lies between one quarter and one half of $`\min(u_i,u_{i+1})`$; $`c_N=u_N/2`$. Hence, for $`p=1,2`$,

```math
\sum_{i=1}^{N}(b+c_i)^{-p}
\asymp\sum_{i=2}^{N}(b+v_i)^{-p}.
```

Each neighboring minimum contributes at most the sum of two inverse powers, so an edge is counted at most twice. Conversely $`c_i\le u_i/2`$ for $`i\ge2`$. The auxiliary $`u_1=V`$ adds only a harmless endpoint term. Constants are uniform in the individual positive gaps.

This is an experiment comparison for a lower bound. It does not reveal any noise coordinate or Brownian path to the actual receiver.

## 3. Exact compensated comparison

Let $`\tau_v`$ be the one-mode Gaussian displacement mixture of the spatial vacuum, and $`\rho_{a,v}`$ the equal binary-source mixture with shifts $`\pm a`$ and Gaussian variance $`v`$. Here the vacuum position variance is $`u=1/2`$. The sister repository's [exact sandwiched collision identity](https://github.com/GoGoKo699/Quantum-Imaging-Calibration/blob/275c70d6fa9f5a205aab0df35cfe8a7b50aa1635/science/collision-kernel.md) states, for $`v\gt 0`$, $`a\ge0`$, $`0\le\omega\le1`$, $`v-\omega a^2\ge0`$ and $`z=a^2/\sqrt{v(u+v)}`$,

```math
1+\chi^2_{1/2}(\rho_{a,v-\omega a^2}\Vert\tau_v)
=\frac{\exp[z/(1+\omega z)]+\exp[-z/(1-\omega z)]}
{2\sqrt{1-\omega^2z^2}},
```

```math
1+\chi^2_{1/2}(\tau_{v-\omega a^2}\Vert\tau_v)
=\frac1{\sqrt{1-\omega^2z^2}}.
```

The divergence is defined by the weighted operator

```math
\chi^2_{1/2}(\rho\Vert\tau)
=\operatorname{Tr}\!\left[(\tau^{-1/4}\rho\tau^{-1/4})^2\right]-1.
```

The cited proof constructs the positive trace-class weighted integral, justifies its inverse-operator domains and proves both tensor factorization and $`T(\rho,\tau)\le\tfrac12\sqrt{\chi^2_{1/2}(\rho\Vert\tau)}`$. A bounded inverse is not assumed. Its local estimates for $`|z|\le1/2`$ are

```math
\chi^2_{\mathrm{sig}}
\le\frac12(1-\omega)^2z^2+200z^4,
\qquad
\chi^2_{\mathrm{cal}}\le\omega^2z^2.
```

Assume $`b\gt 0`$. Choose actual null jitter $`w_0=b/2`$ and alternative jitter $`w_1=w_0-q`$. For $`q\le b/4`$ these are allowed. Signal coordinate $`i`$ has reference variance $`c_i+w_0`$, squared half-separation $`a^2=q`$ and compensation coefficient $`\omega=1`$. Thus

```math
(c_i+w_1)+q=c_i+w_0,
\qquad
z_i=\frac{q}{\sqrt{(c_i+b/2)(1/2+c_i+b/2)}}.
```

The quadratic signal cost vanishes exactly. Uniformly on the bounded range,

```math
z_i^4\le C\frac{q^4}{(b+c_i)^2}.
```

Calibration instead has reference variance $`b/2`$ and variance shift $`q`$, so its cost is at most $`Cq^2/b`$ per photon. Choosing $`q\le cb`$ with sufficiently small fixed $`c`$, depending only on the fixed bounds, ensures both admissibility and every $`|z_i|\le1/2`$.

Tensor factorization in the independent reference experiment gives

```math
\log(1+\chi^2_{\mathrm{ind}})
\le C\left[q^4S_2(v,b)+\frac{Mq^2}{b}\right].
```

The calibration term is absent at $`M=0`$. Trace distance of the actual correlated states is at most $`\tfrac12\sqrt{\chi^2_{\mathrm{ind}}}`$, by the residual Gaussian channel and trace-distance contractivity. This proof does not need to assert a collision-divergence bound after that channel.

## 4. Close the uniform lower bound

Let $`U=\min\{b,\sqrt{b/M},S_2^{-1/4}\}`$, with the endpoint conventions in the [model](joint-model.md#3-joint-frontier). A sufficiently small multiple of $`U`$ is admissible and makes the independent collision exponent uniformly small. It therefore gives a nuisance lower obstruction at scale $`U`$.

The physical obstruction at $`r_0`$ and nuisance obstruction at $`U`$ may use different hard pairs. Select the larger one: their maximum is comparable to $`r_0+U`$. Equivalently, construct an alternative at a sufficiently small multiple of $`r_0+U`$ using the physical pair when $`r_0\ge U`$, and the compensated pair otherwise. It belongs to every separated alternative with a smaller threshold. The Helstrom bound then gives risk above the prescribed $`\epsilon`$.

At $`b=0`$ only the known-jitter argument is used. Bounded gaps give $`r_0=O(N^{-1/2})`$ and $`S_2^{-1/4}=O(N^{-1/4})`$ uniformly, so all lower alternatives fit below fixed $`q_0`$ once $`N\ge N_0`$. This completes the all-collective converse. [The weighted pair receiver](joint-receiver.md) supplies the other direction.
