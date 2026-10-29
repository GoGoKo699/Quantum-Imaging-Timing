# Converse for every collective receiver

The lower bound retains the full spatial state of every photon and the correlations induced by Brownian motion. It therefore applies before any receiver is chosen. The proof replaces the small binary source displacement by a Gaussian displacement, evaluates the resulting multimode Gaussian fidelity, and controls it using the sparse precision matrix of a Brownian path.

Definitions and the minimax error are in [Model and theorem](model-and-theorem.md). Throughout this page,

```math
T(\rho,\tau)=\tfrac12\|\rho-\tau\|_1,
\qquad
F(\rho,\tau)=\left\|\sqrt\rho\sqrt\tau\right\|_1^2.
```

Thus $`F`$ is squared fidelity and $`\sqrt F`$ is root fidelity.

## 1. A prior for the unrestricted centroid

The initial centroid is an unknown constant $`m\in\mathbb R`$. To obtain a minimax lower bound, use the same auxiliary prior $`m\sim\mathcal N(0,V)`$ under $`q=0`$ and $`q=h`$, independently of the subsequent Brownian increments. Define

```math
\bar\rho_q=\int_{\mathbb R}\rho_{q,m}^{v}\,
\frac{e^{-m^2/(2V)}}{\sqrt{2\pi V}}\,dm.
```

For every test, its worst type-I/type-II error is at least its equal-prior average error for this binary subproblem. The Helstrom variational formula therefore gives

```math
\mathcal R_Q(h;v)\ge\frac{1-T(\bar\rho_0,\bar\rho_h)}2.
```

This prior is a proof device, not an assumption about the actual initial position. It is permitted because the nuisance parameter is unrestricted.

Let $`L`$ be the $`N\times N`$ lower-triangular matrix of ones. The averaged centroid vector has the positive definite covariance

```math
C=L\mathrm{diag}(V,v_2,\ldots,v_N)L^{\mathsf T}.
```

In particular, $`V`$ here is the variance of the auxiliary initial-centroid prior. It is not an extra photon gap.

## 2. A uniform Gaussian replacement bound

Write

```math
f(x)=e^{-ixP}\lvert0\rangle\langle0\rvert e^{ixP},
```

where $`P`$ is the dimensionless momentum operator and the vacuum has $`\langle P^2\rangle=1/2`$. Let $`X`$ be $`\pm\sqrt q`$ with equal probabilities, and let $`G\sim\mathcal N(0,q)`$. Their moments agree through degree three:

```math
\mathbb EX=\mathbb EG=0,
\qquad
\mathbb EX^2=\mathbb EG^2=q,
\qquad
\mathbb EX^3=\mathbb EG^3=0.
```

The map $`f`$ is four times continuously differentiable in trace norm. This follows directly because the Gaussian vacuum lies in the domain of every power of $`P`$, and each derivative is a finite sum of rank-one operators. Conjugation preserves trace norm, so

```math
\|f^{(4)}(x)\|_1
=\|\mathrm{ad}_{-iP}^{4}(\lvert0\rangle\langle0\rvert)\|_1.
```

For any vectors $`u,w`$, $`\||u\rangle\langle w|\|_1=\|u\|\|w\|`$. The vacuum momentum moments

```math
\langle P^{2k}\rangle=\frac{(2k-1)!!}{2^k}
```

then imply

```math
\begin{aligned}
\|f^{(4)}(x)\|_1
&\le\sum_{k=0}^{4}\binom4k
\sqrt{\langle P^{2k}\rangle\langle P^{2(4-k)}\rangle}\\
&=\frac{\sqrt{105}}2+2\sqrt{15}+\frac92<18.
\end{aligned}
```

Taylor expansion through degree three, with its integral trace-norm remainder, gives

```math
\left\|f(x)-\sum_{k=0}^{3}\frac{x^k}{k!}f^{(k)}(0)\right\|_1
\le\frac{18}{24}|x|^4.
```

Since $`\mathbb EX^4=q^2`$ and $`\mathbb EG^4=3q^2`$, cancellation of the first four Taylor terms yields

```math
\left\|\mathbb Ef(X)-\mathbb Ef(G)\right\|_1
\le3q^2.
```

For density operators $`\rho,\tau`$, tensor telescoping gives
$`\|\rho^{\otimes N}-\tau^{\otimes N}\|_1\le N\|\rho-\tau\|_1`$.
Applying the same correlated Gaussian displacement channel with covariance $`C`$ contracts trace distance. If $`G_A`$ denotes the Gaussian spatial state obtained by displacing the product vacuum with a zero-mean classical Gaussian vector of covariance $`A`$, then

```math
\bar\rho_0=G_C,
\qquad
T(\bar\rho_q,G_{C+qI})\le\frac32Nq^2.
```

This estimate is uniform in the eigenvalues of $`C`$. It does not require the Brownian coordinates to be independent, and it does not identify the original binary-source state as Gaussian.

## 3. Fidelity of the Gaussian comparison states

The position and momentum covariance blocks of $`G_C`$ are

```math
\mathrm{Cov}(X)=\tfrac12 I+C,
\qquad
\mathrm{Cov}(P)=\tfrac12 I,
\qquad
\mathrm{Cov}(X,P)=0.
```

Choose a real orthogonal matrix diagonalizing $`C`$, with eigenvalues $`c_1,\ldots,c_N>0`$. The corresponding orthogonal coordinate transformation, applied to both positions and momenta, is a unitary on the spatial-register Hilbert space and leaves the product vacuum invariant. Hence the pair $`G_C,G_{C+qI}`$ is unitarily equivalent to

```math
\bigotimes_{j=1}^{N}\rho(c_j),
\qquad
\bigotimes_{j=1}^{N}\rho(c_j+q),
```

where the one-mode state $`\rho(c)`$ has covariance $`\mathrm{diag}(1/2+c,1/2)`$. The transformation is used to evaluate a state distance; no implementation assumption about that transformation is needed.

The Gaussian-state fidelity formula of [Banchi, Braunstein and Pirandola (2015)](https://doi.org/10.1103/PhysRevLett.115.260501), specialized to these covariance matrices and expressed in the squared-fidelity convention, is

```math
\begin{aligned}
F(\rho(c),\rho(c+q))
&=\frac1{\sqrt{(1+c)(1+c+q)}-\sqrt{c(c+q)}}\\
&=\mathrm{sech}\!\left[
\mathrm{asinh}\sqrt{c+q}-\mathrm{asinh}\sqrt c\right].
\end{aligned}
```

For example, at $`c=0`$ this is $`(1+q)^{-1/2}`$, equal to the vacuum overlap of a Gaussian displacement mixture. This limit fixes the fidelity convention and the displacement normalization.

Set

```math
d_c=\mathrm{asinh}\sqrt{c+q}-\mathrm{asinh}\sqrt c.
```

Since $`\mathrm{asinh}`$ is increasing and one-Lipschitz on $`[0,\infty)`$,

```math
0\le d_c\le\sqrt{c+q}-\sqrt c
=\frac q{\sqrt{c+q}+\sqrt c}
\le\frac q{\sqrt{c+q}}.
```

For $`u\ge0`$,

```math
\frac{d}{du}\left(1-\sqrt{\mathrm{sech}u}\right)
=\frac{\tanh u}{2\sqrt{\cosh u}}
\le\frac u2.
```

Integration therefore proves

```math
1-\sqrt{F(\rho(c),\rho(c+q))}
\le\frac{d_c^2}{4}
\le\frac{q^2}{4(c+q)}.
```

Root fidelity is multiplicative. Using
$`1-\prod_j a_j\le\sum_j(1-a_j)`$ for $`a_j\in[0,1]`$ and the [Fuchs–van de Graaf inequality](https://doi.org/10.1109/18.761271),

```math
\begin{aligned}
T(G_C,G_{C+qI})^2
&\le1-F(G_C,G_{C+qI})\\
&\le2\left[1-\sqrt{F(G_C,G_{C+qI})}\right]\\
&\le\frac{q^2}{2}\mathrm{tr}(C+qI)^{-1}.
\end{aligned}
```

## 4. Brownian precision controls the resolvent

Write $`u_1=V`$ and $`u_i=v_i`$ for $`i\ge2`$. The inverse $`B=L^{-1}`$ has ones on the diagonal, minus ones on the subdiagonal, and zeros elsewhere. Let $`b_i`$ be the transpose of row $`i`$ of $`B`$. Then

```math
C^{-1}=\sum_{i=1}^{N}\frac{b_i b_i^{\mathsf T}}{u_i},
\qquad
\|b_i\|^2\le2.
```

The following rank-one estimate avoids any comparison between $`C`$ and the diagonal matrix of its increments. For $`A\ge0`$, define

```math
f_q(A)=A(I+qA)^{-1}
=\frac1q\left[I-(I+qA)^{-1}\right].
```

Put $`H=(I+qA)^{-1}`$. The Woodbury identity gives

```math
\mathrm{tr}f_q(A+ww^{\mathsf T})-\mathrm{tr}f_q(A)
=\frac{w^{\mathsf T}H^2w}{1+q w^{\mathsf T}Hw}.
```

Because $`0\le H^2\le H\le I`$, the numerator is at most
$`r=w^{\mathsf T}Hw\le\|w\|^2`$. Monotonicity of $`r/(1+qr)`$ implies

```math
\mathrm{tr}f_q(A+ww^{\mathsf T})-\mathrm{tr}f_q(A)
\le\frac{\|w\|^2}{1+q\|w\|^2}.
```

Iterating from $`A=0`$ with $`w=b_i/\sqrt{u_i}`$ proves

```math
\begin{aligned}
\mathrm{tr}(C+qI)^{-1}
&=\mathrm{tr}f_q(C^{-1})\\
&\le\sum_{i=1}^{N}\frac{\|b_i\|^2}{u_i+q\|b_i\|^2}\\
&\le2\sum_{i=1}^{N}\frac1{u_i+q}.
\end{aligned}
```

The last scalar inequality holds for every $`0\le\|b_i\|^2\le2`$ and $`u_i,q>0`$.

## 5. Close the minimax bound

Combining the replacement, Gaussian fidelity and resolvent estimates yields

```math
T(\bar\rho_0,\bar\rho_q)
\le\frac32Nq^2
+\left[\frac{q^2}{V+q}+\sum_{i=2}^{N}\frac{q^2}{v_i+q}\right]^{1/2}.
```

Since every $`v_i\le V`$,

```math
\frac{q^2}{V+q}\le\frac{\mathcal I(q;v)}{N-1},
\qquad
Nq^2\le\frac{N}{N-1}(V+q)\mathcal I(q;v).
```

For $`N\ge2`$ and $`q\le q_0`$, it follows that

```math
T(\bar\rho_0,\bar\rho_q)
\le3(V+q_0)\mathcal I(q;v)+\sqrt{2\mathcal I(q;v)}.
```

Set $`q=h`$ and substitute this estimate into the binary Bayes lower bound from Section1. This is the lower half of the [resolution theorem](model-and-theorem.md#5-uniform-resolution-theorem).

The bound is on the state before any receiver processing. Trace-distance contraction therefore includes arbitrary joint POVMs, adaptive operations and independently supplied ancillas. A system revealing the hidden Brownian path would change the input experiment; it is not an independently supplied receiver ancilla.

The proof also explains why the Gaussian replacement is sufficient throughout the bounded-gap regime: its $`Nq^2`$ remainder is already bounded by a constant times the controlling schedule information. It is not necessary to assume that the Brownian motion is weak over the full observation duration.

Continue with the [pair receiver](receiver.md) for the matching upper bound or [timing regimes](timing-regimes.md) for the consequences of different arrival patterns.
