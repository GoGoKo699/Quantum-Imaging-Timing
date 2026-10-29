# From Tsang's imaging model to the Brownian timing theorem

**Background anchor:** Mankei Tsang, [*Resolving starlight: a quantum perspective*](https://arxiv.org/pdf/1906.02064v2), *Contemporary Physics* **60**, 279–298 (2019), [doi:10.1080/00107514.2020.1736375](https://doi.org/10.1080/00107514.2020.1736375). Section and equation references below use the accepted arXiv version 2, revised 25 February 2020.

The bridge develops the project's normalization, correlated state and testing problem from the one-photon imaging framework. The Brownian schedule theorem is established in the linked [project proofs](../science/README.md). The review supplies the background framework; it does not establish that theorem.

## 1. Source map

| Location in the anchor | Topic to connect | Local destination |
| --- | --- | --- |
| Sections III–V; Eqs. (3.1), (4.1), (5.3)–(5.8) | Direct imaging, spatial modes and Fisher information | The distinction between a spatial quantum state and its position-measurement data |
| Section VI.G; Section VIII.A | Two-photon measurements and centroid alignment | The translation-invariant pair receiver |
| Sections VIII.J–K; Appendices A–B | Estimator bias, hypothesis testing and quantum measurement bounds | A uniform fixed-error criterion |
| Appendix C; Eqs. (C7)–(C14) | Thermal temporal modes and the one-photon state | The precise conditional state and the optical interface |

The relevant physical setting is one-dimensional paraxial incoherent imaging. The Gaussian formulas below are the project's explicit specialization of the review's general amplitude response $`\psi`$.

## 2. Fix the units before translating the symbols

The project uses the physical amplitude point-spread function

```math
\psi_c(x)=(2\pi\sigma^2)^{-1/4}
 \exp\!\left[-\frac{(x-c)^2}{4\sigma^2}\right].
```

Its intensity is a normal density with mean $`c`$ and variance $`\sigma^2`$. Thus $`\sigma`$ is the **intensity standard deviation**. The amplitude exponent has denominator $`4\sigma^2`$, while the intensity exponent has denominator $`2\sigma^2`$. If an amplitude is instead written as proportional to $`\exp[-x^2/(2w^2)]`$, the equivalent width is $`w=\sqrt2\sigma`$.

Introduce dimensionless coordinates and centers

```math
z=\frac{x}{\sqrt2\sigma},\qquad a=\frac{c}{\sqrt2\sigma}.
```

The change of variable includes the normalization factor:

```math
\widetilde\psi_a(z)
=(\sqrt2\sigma)^{1/2}\psi_{\sqrt2\sigma a}(\sqrt2\sigma z)
=\pi^{-1/4}e^{-(z-a)^2/2}.
```

With $`P=-i\partial_z`$, write $`|a\rangle=e^{-iaP}|0\rangle`$. The position and momentum variances of this reference wave packet are both $`1/2`$. Two useful overlap checks are

```math
|\langle\psi_c|\psi_d\rangle|^2
=e^{-(c-d)^2/(4\sigma^2)},\qquad
|\langle a|b\rangle|^2=e^{-(a-b)^2/2}.
```

The spatial oscillator state $`|0\rangle`$ here describes the shape of **one photon**. It is different from the optical no-photon state $`|\mathrm{vac}\rangle`$ used in a weak-light expansion.

### Notation dictionary

| Anchor notation | Project notation or conversion |
| --- | --- |
| $`x,X`$ in Section V | Use a common physical length unit first; then divide image and source coordinates by $`\sqrt2\sigma`$. Magnification must be accounted for in that common unit. |
| Separation $`\theta`$ | $`s`$ in physical units. If $`\theta`$ is expressed in units of a length $`\ell`$, then $`s=\ell\theta`$. The project parameter is $`q=s^2/(8\sigma^2)`$. |
| $`\psi(x-X)`$ | The Gaussian $`\psi_c(x)`$ above, or the dimensionless state $`\lvert a\rangle`$. |
| $`\widehat k`$ in Eq. (C14) | Physical spatial momentum; $`P=\sqrt2\sigma\widehat k`$ after changing coordinates. |
| $`F(X)`$, Eq. (5.3) | For a fixed centroid, two equal point masses at $`c\pm s/2`$. Along a trajectory, this distribution changes with the sampling time. |
| $`\rho_1`$, Eqs. (C13)–(C14) | The instantaneous one-photon state $`\omega_{q,a}`$. The full record is $`\rho^v_{q,m}`$, defined below. |
| $`q`$ in $`\phi_q,g_q`$ | A spatial-mode index in the anchor. It is unrelated to the project's squared-separation parameter $`q`$. A mode index can be renamed $`j`$ during translation. |
| $`N=M\epsilon`$ in Appendix C | An expected photon count, denoted $`\bar N`$ here. The project conditions on exactly $`N`$ supplied photon registers. |
| $`\sigma`$ in Appendix C | A thermal density operator. It is unrelated to the project's scalar PSF width $`\sigma`$. Write the thermal operator as $`\tau_\epsilon`$ below. |
| Centered object in Section V; centroid issue in VIII.A | An unrestricted initial dimensionless centroid $`m`$ and subsequent hidden Brownian displacements. |

These conversions fix all factors of two in the [canonical model](../science/model-and-theorem.md). In particular, physical source offsets $`\pm s/2`$ become dimensionless offsets $`\pm\sqrt q`$.

## 3. From an incoherent source distribution to one occupied register

The source equations needed here are the weak-light expansion (C12) and the translated-state mixture (C14). In the notation just defined, they take the form

```math
\tau_\epsilon
=(1-\epsilon)|\mathrm{vac}\rangle\langle\mathrm{vac}|
 +\epsilon\rho_1+O(\epsilon^2),
```

```math
\rho_1[F]
=\int F(X)e^{-i\widehat kX}|\psi\rangle\langle\psi|
 e^{i\widehat kX}\,dX.
```

Here $`\epsilon`$ is the mean occupancy per temporal mode; the ultraviolet limit keeps $`\bar N=M\epsilon`$ fixed. The leading one-photon component is conditional on occupancy. Appendix C also identifies the omitted multiphoton and bunching contributions.

For the project's static pair, insert

```math
F_{c,s}(X)=\frac12\delta(X-c-s/2)+\frac12\delta(X-c+s/2).
```

The integral becomes

```math
\rho_1[F_{c,s}]
=\frac12|\psi_{c+s/2}\rangle\langle\psi_{c+s/2}|
 +\frac12|\psi_{c-s/2}\rangle\langle\psi_{c-s/2}|.
```

After the coordinate transformation, this is exactly

```math
\omega_{q,a}
=\frac12|a+\sqrt q\rangle\langle a+\sqrt q|
 +\frac12|a-\sqrt q\rangle\langle a-\sqrt q|.
```

The incoherent source labels produce a mixture of projectors. Adding the two wavefunctions coherently and then squaring would produce cross terms and a different source model.

The supplied-register model retains $`\omega_{q,a}`$ as an exact input state. It additionally assumes that each occupied register is labeled and that its spatial state survives until the receiver acts. Conditioning a mathematical description on occupancy does not specify a nondestructive heralding or storage procedure. A detector that consumes the photon cannot simultaneously provide it for a later pair measurement.

An optical derivation of the whole experiment would also need to control the neglected sectors across the complete acquisition, establish the relation between temporal modes and recorded timestamps, and account for motion during each wave packet. A per-mode approximation alone does not establish uniform accuracy in an asymptotic family with more photons and shrinking gaps. These are the interface requirements in [physical-interface.md](../science/physical-interface.md).

## 4. The change that produces temporal correlations

Let $`c(t)`$ be a physical Brownian centroid with increment variance $`2D\Delta t`$. The dimensionless centroid at the first photon is an unknown fixed number $`m`$. For known ordered timestamps, define

```math
B_1=0,\qquad B_i=\sum_{j=2}^iW_j,\qquad
W_j\sim N(0,v_j),\qquad
v_j=\frac{D(t_j-t_{j-1})}{\sigma^2}.
```

The increments are independent, and $`D,\sigma`$ and the gaps are known. The complete state is

```math
\rho^v_{q,m}
=\mathbb E_W\left[\bigotimes_{i=1}^N\omega_{q,m+B_i}\right].
```

The expectation is **outside** the tensor product. For example, with the initial centroid fixed,

```math
B_2=W_2,\qquad B_3=W_2+W_3,\qquad
\operatorname{Cov}(B_2,B_3)=v_2.
```

Replacing the joint state by $`\bigotimes_i\mathbb E_W\omega_{q,m+B_i}`$ removes that correlation. The one-photon marginals do not determine the joint experiment. The actual joint state is a classical mixture of product states, so entanglement in the input is not needed for this temporal correlation.

There are two different random mechanisms: independent fair source labels select the two emitters, while one common path moves their shared centroid. Spatial incoherence specifies the first mechanism; it does not make the path positions at different times independent.

The receiver is not supplied with $`m`$ or the path. It receives the spatial registers and their times. A pair comparison commutes with a common translation of its two inputs, which is why their relative Brownian increment can matter even when their absolute position is unknown. The Gaussian centroid prior in the [converse](../science/collective-converse.md) is only a device for proving a minimax lower bound. It is not calibration information available to the receiver.

## 5. Translate the statistical question as well as the state

For a smooth probability model away from its boundary, Fisher information transforms under reparametrization according to

```math
\mathrm{FI}_s
=\left(\frac{dq}{ds}\right)^2\mathrm{FI}_q
=\left(\frac{s}{4\sigma^2}\right)^2\mathrm{FI}_q.
```

Thus an information quantity that is singular in $`q`$ near zero can correspond to finite information in physical separation $`s`$. The parameter and the statistical criterion must be specified together. A pointwise information value does not itself give a test that controls both errors for an unrestricted centroid and every alternative $`q\ge h`$.

The project's operational question is whether one measurement effect $`0\le E\le I`$ can keep both

```math
\alpha=\sup_m\operatorname{tr}(E\rho^v_{0,m}),\qquad
\beta_h=\sup_{m,\ q\ge h}\operatorname{tr}[(I-E)\rho^v_{q,m}]
```

below a chosen error level. The threshold $`h`$ is fixed when designing the receiver; the true $`q`$ is unknown. Resolution means the smallest order of $`s_h=\sqrt{8h}\,\sigma`$ for which this is possible. No unbiased estimator is required.

The suitable quantities in the proofs are trace distance for the complete quantum state and Hellinger affinity for the pair outcomes. Use the convention

```math
A(P,Q)=\sum_y\sqrt{P(y)Q(y)},\qquad H^2(P,Q)=1-A(P,Q).
```

For independent pair records, affinities multiply. This gives finite-error guarantees at nonzero $`h`$, including the transition where a null outcome probability approaches zero. The review's treatment of estimation and testing motivates keeping these tasks distinct; the project's [model and theorem](../science/model-and-theorem.md) fixes the latter task precisely.

## 6. Worked pair: a zero null probability and a Brownian background

Take two adjacent spatial registers. Let $`S`$ exchange them and measure the antisymmetric effect $`\Pi_-=(I-S)/2`$. For two particular displaced wave packets,

```math
\Pr(-\mid a,b)=\frac{1-|\langle a|b\rangle|^2}{2}
=\frac{1-e^{-(a-b)^2/2}}2.
```

The Brownian displacement difference is $`Z\sim N(0,v)`$. Independent source labels add zero with probability $`1/2`$ and each of $`\pm2\sqrt q`$ with probability $`1/4`$. Using

```math
\mathbb E e^{-(Z+d)^2/2}
=\frac{e^{-d^2/[2(1+v)]}}{\sqrt{1+v}}
```

gives the canonical [exact response](../science/receiver.md#1-exact-probability-for-a-pair)

```math
p_v(q)=\frac12-\frac{1+e^{-2q/(1+v)}}{4\sqrt{1+v}}.
```

The absolute centroid has canceled. This calculation specifies the ideal spatial SWAP measurement; an optical realization still needs the storage and nonspatial mode matching described in the [physical interface](../science/physical-interface.md).

### No motion within the pair

At $`v=0`$,

```math
p_0(0)=0,\qquad
p_0(q)=\frac{1-e^{-2q}}4=\frac q2+O(q^2).
```

The subscript denotes motion variance; the argument denotes squared separation. The single-source null therefore produces **no antisymmetric event**, even for an unknown centroid. The pair Hellinger distance is

```math
H^2(\operatorname{Ber}(0),\operatorname{Ber}(p_0(q)))
=1-\sqrt{1-p_0(q)}=\frac q4+O(q^2).
```

For $`M`$ independent zero-motion pairs, an any-antisymmetric-event decision has type-I error zero and type-II error $`[1-p_0(q)]^M`$. Its fixed-error scale is $`Mq=\Theta(1)`$. Since $`N=2M`$, this means $`s/\sigma=\Theta(N^{-1/2})`$. This is a limiting example for intuition; the main deterministic theorem states strictly positive gaps.

### A positive Brownian increment

For $`v>0`$,

```math
p_v(0)=\frac{1-(1+v)^{-1/2}}2>0,
```

and, at fixed $`v`$ as $`q\to0`$,

```math
p_v(q)-p_v(0)
=\frac{q}{2(1+v)^{3/2}}+O(q^2),
```

```math
H^2(\operatorname{Ber}(p_v(0)),\operatorname{Ber}(p_v(q)))
=\frac{q^2}{8v(1+v)^2}+O(q^3).
```

The expansion on the last line is for fixed positive $`v`$; it is not uniform down to $`v=0`$. When both parameters are small, $`p_v(0)\sim v/4`$ and the signal increment is approximately $`q/2`$. The rigorous uniform interpolation is the [pair bound](../science/receiver.md#2-the-pairs-testing-information)

```math
H^2\asymp\frac{q^2}{v+q}
```

on the stated bounded parameter ranges. A fixed positive $`v`$ gives a null background and eventually the scale $`Mq^2=\Theta(1)`$, hence separation order $`N^{-1/4}`$. The background is not an absolute resolution floor: collecting more independent pairs still improves resolution.

For a concrete comparison, set $`q=0.01`$, or $`s=0.282843\sigma`$:

| Internal variance $`v`$ | Null probability $`p_v(0)`$ | Alternative probability $`p_v(0.01)`$ | Pair $`H^2`$ |
| --- | ---: | ---: | ---: |
| $`0`$ | 0 | 0.00495033 | 0.00247824 |
| $`0.04`$ | 0.00970966 | 0.01437895 | 0.000231196 |

The second row has a physical centroid-increment root-mean-square displacement $`\sqrt{2v}\sigma=0.282843\sigma`$. A single antisymmetric event can now occur under the null, so the any-event decision no longer has zero type-I error. The likelihood-ratio rule accounts for the known background; repeated counts remain informative. These numbers illustrate one pair, not an optimized full-record error probability.

## 7. The local steps needed for a schedule theorem

The worked pair establishes a receiver response. Establishing optimality for the entire correlated record requires additional arguments:

| Local step | Why it is needed | Canonical derivation |
| --- | --- | --- |
| Keep the common Brownian path inside the joint state | Preserves all correlations available to a collective receiver | [Model and theorem](../science/model-and-theorem.md) |
| Use disjoint pairs and choose the better parity at $`h`$ | Makes the measured outcomes independent while retaining at least half of the adjacent-gap information | [Pair receiver](../science/receiver.md) |
| Multiply affinities and use a monotone likelihood-ratio decision | Controls finite errors uniformly over every $`q\ge h`$ and every initial centroid | [Pair receiver](../science/receiver.md) |
| Compare binary source shifts with Gaussian shifts in trace distance | Enables a controlled calculation on the complete quantum record | [Collective converse](../science/collective-converse.md) |
| Evaluate Gaussian fidelity and bound the Brownian covariance resolvent | Converts a state-distance obstruction for every receiver into a sum over the actual gaps | [Collective converse](../science/collective-converse.md) |
| Average an allowed centroid prior only for the lower bound | Establishes an unrestricted-centroid minimax obstruction | [Collective converse](../science/collective-converse.md) |
| Retain the complete position record in the classical comparison | Gives a direct-imaging benchmark that permits arbitrary classical processing | [Direct imaging](../science/direct-imaging.md) |

Together the quantum upper and lower bounds yield

```math
\mathcal I(h;v)=\sum_{i=2}^{N}\frac{h^2}{v_i+h}\asymp1
```

as the fixed-error boundary for $`0<v_i\le V`$ and $`0<h\le q_0`$. This is the bridge's destination. For regular gaps it gives the diffusion crossover; for controlled doublets it quantifies the benefit of short internal intervals. Those consequences are worked out in [timing-regimes.md](../science/timing-regimes.md).

The [fixed-count Poisson result](../science/poisson-arrivals.md) needs a further argument because its gaps have unbounded support. Its proof works with the joint timestamp-and-quantum experiment and average risk. Integrating the nonzero-threshold pair information produces $`\log(1+\kappa/h)`$. Formally averaging the zero-threshold pair Fisher information would instead encounter the divergent integral $`\mathbb E(1/v)`$ and would not prove that finite-error statement.

## 8. Where the bridge stops

The exact claims concern a known Gaussian response, known diffusion, equal independent source labels, unrestricted initial centroid, and supplied spatial registers with known timestamps. A finite-bandwidth field model, unresolved timestamps, an uncertain diffusion coefficient, imperfect interference, or a trajectory-reference stream changes the statistical experiment. The [physical interface](../science/physical-interface.md) distinguishes those changes and the resources needed to realize the pair receiver.

The [milestone map](MILESTONES.md) organizes the background and local derivations into a complete route through the project. The review is the single background anchor for that route. Attribution for static superresolution, two-photon interference, Gaussian fidelity and the other inherited tools remains in [related work](../references/related-work.md) and the [bibliography](../references/references.bib).
