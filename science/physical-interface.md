# Physical interface and scope

[Model and results](model-and-theorem.md) · [Related work](../references/related-work.md)

The result concerns a stream of **individually addressable one-photon spatial registers**, sampled at known times from two incoherent emitters with a common Brownian centroid. This page specifies the physical resources represented by those registers and the additional requirements of an optical implementation of the attaining pair measurement.

## 1. What is supplied to the receiver

There are exactly $N$ signal registers. Register $i$ contains one photon and carries a known label associated with its sampling time $t_i$. The register's spatial state is available for quantum processing; obtaining the label has not already measured the photon's transverse position or destroyed that state. Orthogonal temporal bins, separate input paths, or storage locations can supply such labels.

In physical image-plane coordinates, the known point-spread amplitude is

```math
\psi_x(y)=(2\pi\sigma^2)^{-1/4}
\exp\!\left[-\frac{(y-x)^2}{4\sigma^2}\right].
```

Its intensity has variance $\sigma^2$. The real amplitude, including its phase convention, is part of the model. The two equally bright incoherent emitters have fixed separation $s$ along a known axis. Their common centroid is $C(t)=m+B(t)$, where $m$ is an unknown fixed initial position and $B$ is Brownian motion with

```math
\mathrm{Var}[B(t)-B(u)]=2D|t-u|.
```

The diffusion coefficient $D$ is known. Conditional on the trajectory, the source choice for each photon is an independent fair sign. Thus

```math
\rho_{s,c}=\frac12\left(
|\psi_{c+s/2}\rangle\langle\psi_{c+s/2}|
+|\psi_{c-s/2}\rangle\langle\psi_{c-s/2}|
\right),\qquad
\Omega_{s,m,\mathbf t}
=\mathbb E_B\!\left[\bigotimes_{i=1}^N\rho_{s,C(t_i)}\right].
```

The expectation is outside the tensor product. A common random trajectory correlates different registers. Replacing this state by a product of averaged one-photon states changes the experiment.

The dimensionless variables are

```math
q=\frac{s^2}{8\sigma^2},\qquad
v_i=\frac{D(t_i-t_{i-1})}{\sigma^2}\quad(i=2,\ldots,N).
```

The all-receiver bound permits arbitrary joint measurements, ancillary systems independent of the unknown source, quantum storage, adaptive operations, and classical processing of the supplied timing record. The receiver receives neither the Brownian trajectory nor the source-choice signs. In particular, an independently monitored moving fiducial or an external stream that reports the instantaneous centroid would supply additional information and define another experiment.

## 2. Why a neighboring pair can serve as a spatial reference

Let $S$ exchange two spatial registers. The ideal pair measurement has effects

```math
\Pi_\pm=\frac{I\pm S}{2}.
```

Both effects commute with a common translation of the two inputs. The measurement therefore responds to their relative displacement and does not require an estimate of their absolute centroid.

For a pair with gap variance $v$, averaging over its Brownian increment gives

```math
K(q,v):=\mathbb E\mathrm{Tr}(\rho_{s,C_1}\rho_{s,C_2})
=\frac{1+e^{-2q/(1+v)}}{2\sqrt{1+v}},
\qquad
p_-(q,v)=\frac{1-K(q,v)}2.
```

The wavepacket identity behind this expression is
$|\langle\psi_a|\psi_b\rangle|^2=e^{-(a-b)^2/(4\sigma^2)}$.
For disjoint neighboring pairs, translation invariance removes each pair's common position. Their outcomes then depend only on Brownian increments over disjoint time intervals and independent source signs, so the outcomes are independent after trajectory averaging.

Two-photon interference as a mutual spatial reference is established technology and theory. Parniak et al. already use it for static centroid/separation estimation; collective purity and Schur measurements provide a broader version of the same idea. The contribution here is its sufficiency for the schedule-dependent correlated-state resolution law. See [the attribution account](../references/related-work.md). [Parniak et al. (2018)](https://arxiv.org/pdf/1803.07096), [de Almeida et al. (2025)](https://arxiv.org/pdf/2110.00986v5).

## 3. Spatial SWAP and its HOM realization

The theorem specifies the spatial SWAP measurement as an allowed quantum measurement. A Hong–Ou–Mandel (HOM) implementation interferes one photon in each input port of a balanced beam splitter, with any reflection-induced spatial inversion compensated. The output port pattern distinguishes symmetric and antisymmetric spatial sectors when the other degrees of freedom are suitably matched.

Input addressability and indistinguishability at the beam splitter have different roles. Separate time bins or paths identify the two input registers. Delay, routing, and mode matching subsequently bring their nonspatial waveforms into overlap for interference. Source incoherence concerns the mixture of the two spatial source branches; it does not itself establish temporal or spectral matching between photons.

The ideal HOM identification requires identical pure nonspatial states, independent of the spatial variables. This requirement, including the contrast correction for mixed nonspatial states, is stated explicitly in Appendix B.1 of [Lian, Zhu and Cao (2026)](https://arxiv.org/html/2610.28089v1), a current preprint.

If the two independent nonspatial states are $\tau_1$ and $\tau_2$, write

```math
\eta=\mathrm{Tr}(\tau_1\tau_2).
```

For the ordinary unresolved HOM port measurement, the spatial-overlap term is multiplied by $\eta$:

```math
p_-^{(\eta)}(q,v)=\frac{1-\eta K(q,v)}2.
```

Consequently, a fixed contrast defect creates a nonzero null background even when $v=0$. For small $q,v$, with $\eta$ bounded away from zero, the null background is of order $v+(1-\eta)$ and the signal change is of order $q$. This identifies an implementation requirement for the stated ideal receiver. It does not establish a lower bound for receivers that can access, resolve, or correct additional internal degrees of freedom.

## 4. Capture, storage, occupancy and loss

For known occupied periodic pulses, an implementation can route alternating pulses into two paths, delay the first photon of each pair by one period, and interfere the pair. The ideal storage resource in this case is one-period preservation of the spatial wavepacket. The optical delay must preserve the relevant spatial modes and produce the required nonspatial matching.

For random arrivals, pairing successive occupied registers requires an interface that captures the earlier photon while preserving its spatial state, identifies the next occupied register, and routes the pair. A destructive arrival-time detector does not by itself provide that interface. Parniak et al. explicitly discuss photon-number quantum-nondemolition capture, spatially multimode memories, delay and routing for thermal-source implementations. [Primary paper, introduction](https://arxiv.org/pdf/1803.07096).

Exactly one received photon per scheduled register is a model assumption. A physical train of weak pulses generally has vacant bins, and a full optical model can also contain multiphoton sectors. Pairing adjacent clock bins is then different from pairing adjacent received photons. If occupancy is heralded or otherwise supplied without disturbing the spatial state, the theorem can be applied to the resulting occupied-register schedule. Establishing that interface and its efficiency remains part of the physical implementation.

The budget $N$ counts the supplied signal photons. Photons used for heralding, a centroid reference, or a separate calibration experiment are not silently included. A parameter-independent loss model can sometimes be handled by conditioning on the retained count and schedule, but the theorem does not derive such a reduction for arbitrary losses. In particular, position-dependent collection efficiency or loss correlated with the Brownian trajectory can change the conditional state.

## 5. What timing means

For periodic sampling with spacing $\delta$, the theorem gives

```math
q_*\asymp\frac1N+\sqrt{\frac{D\delta}{N\sigma^2}}
```

within its bounded-motion-per-gap regime. This is a statement about an actual schedule of available photon registers. A pulse source, a heralded protocol, and a thinned random stream need not realize the same schedule even if their average photon rates agree.

Three changes to the timing model must be distinguished:

| Change | What changes in the experiment |
|---|---|
| A positive minimum actual interphoton gap | The set or distribution of available schedules changes. Arbitrarily close pairs are excluded. |
| Coarse recorded timestamps | The receiver has less classical information about a possibly unchanged physical schedule. The conditional state must be averaged over the unresolved times. |
| Finite temporal coherence or overlapping wavepackets | The optical tensor-factor description, nonspatial matching, or multiphoton state may change. This is a quantum optical modeling question. |

These changes are not interchangeable. In particular, coarse timestamps do not imply that the photons were physically separated by a minimum time.

The ideal Poisson illustration assumes labeled independent photon registers even for arbitrarily small positive gaps. Its logarithmic gain uses progressively smaller gaps as the target separation shrinks. Applying that illustration to a finite-bandwidth optical field requires a separate derivation. The deterministic schedule theorem and its periodic example do not rely on a Poisson approximation.

## 6. Connection to weak-light models

The one-photon spatial state is a standard building block of incoherent imaging. For example, Appendix C of Tsang's review derives it from weak thermal temporal modes while explicitly keeping track of the vacuum sector and the neglected multiphoton terms. [Tsang (2019/2020), Appendix C](https://arxiv.org/pdf/1906.02064v2).

That derivation does not automatically prove that an arbitrary moving-source optical field supplies the exact labeled-register state used here, uniformly in every timing limit. Finite emission duration can correlate spatial and temporal variables, and the centroid can move during a wavepacket. Thermal bunching, fluorescence intermittency, spectral diffusion and photon capture must be modeled if they affect the supplied state. The present result is exact for its stated register model; it is not a complete weak-field or finite-bandwidth imaging theorem.

The same boundary applies to rotational diffusion, unequal source brightness, unknown diffusion, a spatially varying point-spread amplitude, finite field of view, and access to a trajectory monitor. Each changes either the state family, the side information, or the attaining measurement. The [model and results](model-and-theorem.md) gives the precise theorem assumptions.
