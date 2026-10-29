# Ideal fixed-count Poisson arrivals

This page proves a random-schedule consequence directly. It does **not** apply the deterministic bounded-gap theorem to an exponential distribution with unbounded support. The data include the exact timestamps and all spatial registers; errors are averaged over the arrival process as well as the Brownian path and source labels.

The result concerns a fixed number of recorded photons. Conditioning a Poisson process on a fixed observation duration gives a different gap distribution and is outside this statement.

## 1. Experiment and risk

Set the time origin at the first recorded photon, $`t_1=0`$, and acquire $`N\ge2`$ photons in total. The subsequent waiting times are independent exponentials of rate $`\lambda`$, independent of the Brownian path and source labels. The initial centroid at the first recorded photon is an unrestricted nuisance parameter $`m\in\mathbb R`$. Write

```math
n=N-1,\qquad
v_i=\frac{D}{\sigma^2}(t_i-t_{i-1}),\qquad
\kappa=\frac{D}{\lambda\sigma^2},\qquad
v_i\overset{\rm iid}{\sim}\mathrm{Exp}(\text{mean }\kappa),\quad i=2,\ldots,N.
```

Here $`D>0`$, $`\lambda>0`$, and the intensity point-spread function has physical variance $`\sigma^2`$. The separation parameter remains $`q=s^2/(8\sigma^2)`$. The time between the first and last recorded photons has mean $`n/\lambda`$ and no deterministic upper bound.

A receiver may use all timestamps and all photon spatial registers jointly. For a test $`\phi`$, with rejection denoted by $`\phi=1`$, define

```math
R_N^{\rm Pois}(h;\phi)
 =\max\left\{
 \sup_m\mathbb E_v\Pr_{0,m}(\phi=1\mid v),\;
 \sup_{m,\ q\ge h}\mathbb E_v\Pr_{q,m}(\phi=0\mid v)
 \right\}.
```

Let $`R_N^{\rm Pois,*}(h)`$ be the infimum over all permitted receivers. This is an average risk for the joint timestamp-and-photon experiment. It is not a bound conditional on every realized schedule, nor a fixed-duration guarantee.

Fix $`\kappa_0,q_0>0`$. The constants below are uniform for

```math
0<\kappa\le\kappa_0,\qquad 0<h\le q_0.
```

Only the design threshold is restricted to $`h\le q_0`$. The alternative $`q\ge h`$ is unbounded.

Define

```math
J(h,\kappa)=\frac{h^2}{\kappa}\log\left(1+\frac\kappa h\right),\qquad
\mathcal I_N(h,\kappa)=nJ(h,\kappa).
```

## 2. Fixed-error theorem

For any fixed target error $`\eta\in(0,1/2)`$, there are positive constants $`c_\eta,C_\eta`$, depending only on $`\eta,\kappa_0,q_0`$, such that

```math
\mathcal I_N(h,\kappa)\le c_\eta
 \quad\Longrightarrow\quad R_N^{\rm Pois,*}(h)\ge\eta,
```

whereas a receiver measuring disjoint adjacent pairs satisfies

```math
\mathcal I_N(h,\kappa)\ge C_\eta
 \quad\Longrightarrow\quad R_N^{\rm Pois}(h;\phi)\le\eta.
```

Thus the fixed-error boundary is $`\mathcal I_N(h,\kappa)=\Theta(1)`$. The proof covers unbounded exponential gaps through integration, with no high-probability maximum-gap truncation.

## 3. The resolvent average

For $`v\sim\mathrm{Exp}(\text{mean }\kappa)`$,

```math
\mathbb E\frac1{v+h}
 =\frac1\kappa e^{h/\kappa}E_1(h/\kappa),\qquad
E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du.
```

The following elementary comparison is more useful than the special function:

```math
\frac{e^{-1}}\kappa\log\left(1+\frac\kappa h\right)
 \le\mathbb E\frac1{v+h}
 \le\frac1\kappa\log\left(1+\frac\kappa h\right).
```

For the lower bound, restrict the integral to $`0\le v\le\kappa`$, where its density is at least $`e^{-1}/\kappa`$. For the upper bound, an exponential variable of mean one stochastically dominates a uniform variable on $`[0,1]`$: on that interval, $`1-e^{-x}\le x`$. Applying the decreasing function $`x\mapsto(h+\kappa x)^{-1}`$ gives the result. Both comparisons hold for every positive $`h,\kappa`$.

## 4. Converse for the complete random record

For a minimax lower bound, average the allowed initial centroid under the same prior $`m\sim N(0,\kappa_0)`$ under both hypotheses. This prior is a proof device, not an assumption about the actual source. Conditional on the observed gaps, the Brownian covariance is

```math
C_v=L\mathrm{diag}(\kappa_0,v_2,\ldots,v_N)L^{\mathsf T},
```

where $`L`$ is the lower-triangular cumulative-sum matrix. The conditional state bound proved in the [collective converse](collective-converse.md) holds for **all positive increment variances**, with no upper bound on them:

```math
T(\bar\rho_0(v),\bar\rho_h(v))
 \le\frac32Nh^2
 +h\sqrt{\frac1{\kappa_0+h}+\sum_{i=2}^{N}\frac1{v_i+h}}.
```

Here $`T(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$ and the bar denotes the initial-centroid prior. This bound combines the binary-to-Gaussian source comparison with the Brownian covariance resolvent estimate. The maximum-gap condition in the deterministic theorem is used later to control the scale, not to prove this conditional inequality.

The timestamp marginal is the same under both hypotheses. Trace distance for the joint classical–quantum states is therefore the average of the conditional trace distances. Jensen's inequality and the resolvent average give

```math
T(\bar\Omega_0,\bar\Omega_h)
 \le\frac32Nh^2
 +\sqrt{\frac{h^2}{\kappa_0+h}+nJ(h,\kappa)}.
```

The elementary inequality $`\log(1+x)\ge x/(1+x)`$ implies

```math
J(h,\kappa)\ge\frac{h^2}{\kappa+h}
 \ge\frac{h^2}{\kappa_0+h},\qquad
Nh^2\le\frac Nn(\kappa+h)\mathcal I_N.
```

Since $`N/n\le2`$, this yields the explicit uniform bound

```math
\boxed{\displaystyle
T(\bar\Omega_0,\bar\Omega_h)
 \le3(\kappa_0+q_0)\mathcal I_N+\sqrt{2\mathcal I_N}.}
```

For every receiver, the maximum error of the composite minimax problem is at least the equal-prior Bayes error for $`q=0`$ versus $`q=h`$ under the chosen centroid prior. Hence

```math
R_N^{\rm Pois,*}(h)
 \ge\frac{1-3(\kappa_0+q_0)\mathcal I_N-\sqrt{2\mathcal I_N}}2.
```

If the right-hand side is negative, the inequality is simply uninformative. Choosing $`c_\eta>0`$ sufficiently small proves the impossibility part. It applies to every collective measurement and to arbitrary receiver ancillas independent of the unknown source and path.

## 5. Attainment with independent gap–outcome pairs

Choose the fixed matching $`(1,2),(3,4),\ldots`$, containing $`M=\lfloor N/2\rfloor\ge n/2`$ pairs. Unlike the deterministic construction, no parity optimization is needed. Retain each pair's exact internal gap and measure its antisymmetric outcome.

The records $`(v,Y)`$ for these pairs are independent and identically distributed, with joint density

```math
f_q(v,y)=\frac{e^{-v/\kappa}}\kappa\,
 p_v(q)^y[1-p_v(q)]^{1-y},\qquad v>0,\quad y\in\{0,1\},
```

where

```math
p_v(q)=\frac12-\frac{1+e^{-2q/(1+v)}}{4\sqrt{1+v}}.
```

The independence argument and Hellinger convention $`H^2=1-A`$ are established in the [receiver proof](receiver.md). The gap density is identical under both hypotheses, so the Hellinger distance of a single joint record is exactly

```math
H^2(f_0,f_h)
 =\mathbb E_v\,H^2(\mathrm{Ber}(p_v(0)),\mathrm{Ber}(p_v(h))).
```

Restrict the integral to $`0\le v\le\kappa\le\kappa_0`$. The bounded-interval pair estimate, together with the density lower bound on this interval, gives

```math
H^2(f_0,f_h)
 \ge\frac{c^{\rm pair}_{\kappa_0,q_0}e^{-1}}\kappa
 \int_0^\kappa\frac{h^2}{v+h}\,dv
 =e^{-1}c^{\rm pair}_{\kappa_0,q_0}J(h,\kappa),
```

where $`c^{\rm pair}_{\kappa_0,q_0}=e^{-4q_0}/[16(1+\kappa_0)^3]`$ is one valid constant. Gaps greater than $`\kappa`$ still occur and are measured; discarding their nonnegative contribution in this lower bound causes no problem.

Affinities multiply for the $`M`$ independent records. The likelihood-ratio test between $`f_h^{\otimes M}`$ and $`f_0^{\otimes M}`$, with threshold one, therefore has each simple-hypothesis error at most

```math
\boxed{\displaystyle
\exp\left[-\frac{c^{\rm pair}_{\kappa_0,q_0}}{2e}\mathcal I_N(h,\kappa)\right].}
```

For each realized set of pair gaps, its rejection event is increasing in every antisymmetric bit. Since $`p_v(q)`$ increases for every $`q\ge0`$, its type-II error at any $`q\ge h`$ is no larger than at $`h`$, first conditionally on those gaps and then after averaging. The measurement law is independent of $`m`$. This proves the full composite, unrestricted-centroid upper bound.

## 6. Uniform crossover and resolution order

Let $`h_*`$ be the unique positive solution of $`\mathcal I_N(h_*,\kappa)=1`$. It is an information-scale marker, not an exact fixed-error threshold. Define

```math
\bar h_n=\frac1n+
 \sqrt{\frac{\kappa}{n\log(2+n\kappa)}}.
```

Then, for every $`n\ge1`$ and $`\kappa>0`$,

```math
\frac{\bar h_n}{5}\le h_*\le4\bar h_n.
```

Here is an explicit inversion check. Put $`x=n\kappa`$, $`L=\log(2+x)`$, and $`y=n\bar h_n=1+\sqrt{x/L}`$. At $`h=\bar h_n`$,

```math
\mathcal I_N=\frac{y^2}{x}\log\left(1+\frac xy\right).
```

For $`0<x\le1`$, $`y\ge1`$, $`y\le1+1/\sqrt{\log2}`$, and $`\log(1+z)`$ lies between $`z/(1+z)`$ and $`z`$. These give a lower bound $`1/2`$ and an upper bound less than $`5`$. For $`x\ge1`$, $`y\le2\sqrt x`$, $`y^2/x\ge1/L`$, and

```math
\log(1+x/y)\ge\log(1+\sqrt x/2)\ge\tfrac14\log(2+x).
```

The last inequality is equivalent to $`(1+\sqrt x/2)^4\ge2+x`$, which follows by expanding the left-hand side for $`x\ge1`$. Also

```math
\frac{y^2}{x}\le\frac2x+\frac2L,\qquad
\log(1+x/y)\le L,\qquad L/x\le\log3.
```

Thus $`1/4\le\mathcal I_N(\bar h_n,\kappa)\le5`$ for all $`x>0`$. For any factor $`a\ge1`$, concavity of the logarithm gives

```math
aJ(h,\kappa)\le J(ah,\kappa)\le a^2J(h,\kappa).
```

Monotonicity then proves the displayed bounds on $`h_*`$.

Combining this inversion with the fixed-error theorem, in the local regime where the boundary lies below $`q_0`$,

```math
h_{\rm res}=\Theta\left(
 \frac1N+\sqrt{\frac{\kappa}{N\log(2+N\kappa)}}\right),
```

and therefore

```math
\boxed{\displaystyle
\frac{s_{\rm res}}\sigma
 =\Theta\left(
 N^{-1/2}
 +\left[\frac{\kappa}{N\log(2+N\kappa)}\right]^{1/4}\right).}
```

Constants may depend on the target error and the fixed upper bounds $`\kappa_0,q_0`$. At fixed positive $`\kappa`$, this gives the order $`(N\log N)^{-1/4}`$. The static order $`N^{-1/2}`$ is available precisely when $`N\kappa=O(1)`$ within this schedule family, equivalently $`\lambda=\Omega(DN/\sigma^2)`$. This is a statement about the specified Poisson family; [controlled doublet schedules](timing-regimes.md) show why it is not a universal requirement on average flux.

## 7. First-arrival conventions

The proof above has $`t_1=0`$ at the first recorded photon and an unknown centroid there. It does not introduce a fictitious exponential increment before that photon. The variance $`\kappa_0`$ in the converse is the explicit nuisance prior.

Two different conventions can also be treated, but they must be stated:

- **External start time, known initial centroid.** If the Brownian motion starts from a known centroid at an external time zero and the first photon arrives after an observed exponential wait, that first wait is a genuine random increment. There are then $`N`$ exponential increments in the covariance, and the same converse gives $`\tfrac32Nh^2+\sqrt{NJ(h,\kappa)}`$. The pair upper bound is unchanged; using $`N`$ instead of $`N-1`$ does not change the order. The expected external-start exposure is $`N/\lambda`$.
- **Known centroid at the first photon.** If the first photon is at time zero and its centroid is known, the first Brownian coordinate has variance zero. It contributes a pure mode and must be handled separately. The corresponding bound is $`\tfrac32Nh^2+\sqrt{h/2+nJ(h,\kappa)}`$. The additional term tends to zero at the local asymptotic boundary, so it does not change that order. It is not an exponential-gap contribution.

An unknown initial centroid at an external start time can be treated by the same nuisance prior as above; adding the first waiting-time variance only decreases its resolvent contribution. None of these conventions reveals the subsequent Brownian trajectory to the receiver.

## 8. What creates the logarithm

The factor $`\log(1+\kappa/h)`$ is an integral over the distribution of exact internal pair gaps. When $`h\ll\kappa`$, gaps between the scales $`h`$ and $`\kappa`$ contribute through the integral of $`1/v`$. The nonzero design threshold regularizes the contribution of still smaller gaps. An infinite Fisher information evaluated exactly at $`q=0`$ would not supply this fixed-error result.

The theorem assumes separately addressable spatial copies and exact gap information even for arbitrarily close arrivals. It therefore does not by itself establish this logarithmic improvement for finite-bandwidth overlapping optical pulses. A positive physical minimum gap changes the schedule law and removes the integral's zero-gap endpoint. Coarsening timestamps instead creates a different observation channel and is not equivalent to imposing a minimum gap or thinning detections. These interfaces are discussed in [physical-interface.md](physical-interface.md).

The [receiver verification](../verification/verify_receiver.py) checks the resolvent integral, joint-record Hellinger integral, and uniform crossover on curated parameter values. The proofs above, rather than those finite calculations, establish the stated uniform risk bounds.
