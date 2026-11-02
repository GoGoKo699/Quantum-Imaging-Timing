# Related work and attribution

[Model and results](../science/model-and-theorem.md) · [Physical interface](../science/physical-interface.md) · [Bibliography](references.bib)

The original timing comparison concerns literature checked through 29 October 2026; the joint jitter/calibration comparison below extends its bounded primary-source review to 2 November 2026. The original result characterizes fixed-error one-versus-two resolution for addressable one-photon spatial registers along a common Brownian trajectory. Its central quantity is the known-schedule functional

```math
\mathcal I_{\mathbf t}(q)=\sum_{i=2}^N\frac{q^2}{v_i+q},
\qquad q=\frac{s^2}{8\sigma^2},\quad
v_i=\frac{D(t_i-t_{i-1})}{\sigma^2}.
```

The contribution is the matching characterization for all joint quantum receivers and the sufficiency, up to uniform constants, of a suitable matching of neighboring photon pairs. Static quantum superresolution, Brownian penalties for a specified receiver, two-photon comparison, Gaussian fidelity formulas and statistical testing are established ingredients.

The [joint theorem](../science/joint-model.md) additionally gives the schedule-dependent frontier for fresh independent Gaussian jitter of unknown bounded variance and a charged stabilized point-calibration sample. Its new proof steps are diagonal covariance extraction and heterogeneous relative-mode moment correction. Independent-jitter compensation, HG factorial moments and mutual-reference pair measurements retain their earlier attribution.

## 1. Static quantum imaging and fixed-error testing

Tsang, Nair and Lu (2016) establish the quantum advantage over direct imaging for two incoherent point sources and exhibit spatial-mode measurements that attain the separation-information limit. This supplies the static benchmark and the spatial-state language. [Primary paper](https://arxiv.org/abs/1511.00552), [journal](https://doi.org/10.1103/PhysRevX.6.031033). `TsangNairLu2016`

Lu et al. (2018) formulate one-versus-two source resolution as quantum hypothesis testing, derive quantum Chernoff bounds, and show optimality of B-SPADE for the static problem. Their analysis includes an exact thermal-state model and a low-brightness photon-conditioned formulation. Thus neither a decision-theoretic definition of resolution nor comparison against every quantum measurement originates here. [Primary paper](https://arxiv.org/abs/1802.02300), [open journal article](https://www.nature.com/articles/s41534-018-0114-y). `LuEtAl2018`

The present experiment retains one stochastic centroid path across the whole acquisition. The averaged state is not an independent tensor power. Its resolution therefore cannot be obtained by multiplying a separately averaged one-photon Fisher information or Chernoff exponent by $N$.

## 2. Brownian motion and dynamic-source SPADE

Schlichtholz (2025; preprint 2024) analyzes adaptive Hermite–Gaussian mode sorting for a Brownian moving pair. Section IV, Eq. (7), already gives a crossover between the $N^{-1/2}$ and $N^{-1/4}$ physical-separation scalings. Section V identifies measurement windows of order $s^2/D$ as the threshold for approximately constant separation Fisher information. These exponents and this physical timing comparison are inherited. [Primary preprint](https://arxiv.org/pdf/2407.13723v1), [journal DOI](https://doi.org/10.1063/5.0252056). `Schlichtholz2025Brownian`

That model starts each acquisition run with perfect centering, averages its counting probabilities over the subsequent window, and evaluates a specified SPADE receiver. Its conclusion explicitly identifies initial-centering error and time-binned counting as open refinements. The present model supplies no repeated exact centroid estimate and permits every joint receiver to use the correlated register state and the known schedule. The arbitrary-gap converse and pairwise attainability are the distinct assertions; recurrence of $N^{-1/4}$ by itself is not.

Schlichtholz and Rudnicki (2024) examine rotations and oscillations using SPADE Fisher information and time-averaged source states. This is a relevant antecedent for dynamical imaging, but a different motion model and measurement question. [Primary preprint](https://arxiv.org/pdf/2407.10507v1), [journal DOI](https://doi.org/10.1088/1367-2630/ad929d). `SchlichtholzRudnicki2024`

## 3. Reference-free two-photon and collective receivers

Parniak et al. (2018) already use two photons as mutual spatial references in a HOM imaging protocol. Spatially resolved output detection provides static separation and centroid information without pre-estimating the centroid. The paper also explains why a thermal-source implementation needs spatial-state-preserving capture, delay and routing. Both the architecture and that implementation burden are antecedents. [Primary paper](https://arxiv.org/pdf/1803.07096v2), [journal DOI](https://doi.org/10.1103/PhysRevLett.121.250503). `ParniakEtAl2018`

De Almeida, Lewenstein and Skotiniotis (2025) develop collective purity and weak Schur-sampling measurements for finite mixtures. Their static repeated-copy construction is robust to a common misalignment; Eq. (52) treats the same unknown unitary acting on all copies. Section V explicitly discusses distinguishable multiplexed modes and quantum memories. A Brownian path instead supplies different correlated translations at different times. The invariant comparison idea is inherited; the schedule-dependent performance theorem is not a consequence of the static tensor-power model. [Primary paper, v5](https://arxiv.org/pdf/2110.00986v5), [journal DOI](https://doi.org/10.1103/9w4p-5d9j). `deAlmeidaEtAl2025`

Muratore, Triggiani and Tamma (2025) use interference between a signal photon and a reference photon, with transverse-momentum sampling, for static two-source separation. This provides another two-photon receiver antecedent. The comparison here uses the published abstract and stated setup; it does not claim a full audit of that paper's bounds. [Primary preprint record](https://arxiv.org/abs/2412.10057), [journal](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.23.054033). `MuratoreEtAl2025`

## 4. Unknown static responses and correlated motion

Lian, Zhu and Cao's *Quantum Limits of Blind Superresolution Imaging* is a recent preprint, arXiv:2610.28089v1, submitted 20 October 2026. Its model has independent photons and one unknown static, shift-invariant pure point-spread response. It establishes a semiparametric information identity and develops momentum-resolved HOM and tomography-assisted receivers. [Primary text](https://arxiv.org/html/2610.28089v1). `LianEtAl2026`

Appendix G explains that unrestricted unknown mixed responses can make different separations exactly indistinguishable, and expressly places shared random-screen correlations outside the independent-copy model. The present response and diffusion law are known, and the common Brownian path is retained in the joint state. Its model therefore differs from both the static-pure identity and the unrestricted-mixed ambiguity. Appendix B.1 also states the nonspatial mode-matching conditions for HOM and the contrast factor for imperfect matching. These conditions are included in the [physical interface](../science/physical-interface.md).

## 5. Sister experiment and shared joint result

[Quantum-Imaging-Calibration](https://github.com/GoGoKo699/Quantum-Imaging-Calibration/tree/275c70d6fa9f5a205aab0df35cfe8a7b50aa1635) is compared at commit `275c70d6fa9f5a205aab0df35cfe8a7b50aa1635`. Its [model and results](https://github.com/GoGoKo699/Quantum-Imaging-Calibration/blob/275c70d6fa9f5a205aab0df35cfe8a7b50aa1635/science/model-and-results.md) and [quantum converse](https://github.com/GoGoKo699/Quantum-Imaging-Calibration/blob/275c70d6fa9f5a205aab0df35cfe8a7b50aa1635/science/quantum-converse.md) specify a different statistical experiment. `QuantumImagingCalibration2026`

| Feature | Quantum-Imaging-Calibration | Quantum-Imaging-Timing |
|---|---|---|
| Displacement process | A fresh independent Gaussian displacement for each photon | Samples from one common Brownian path |
| Unknown quantity besides separation | A common jitter variance | Initial centroid; diffusion is known |
| Additional resource | Independent point-source calibration photons sharing the variance | Known sampling times and joint access to signal registers |
| Input structure | Signal and calibration tensor powers | A correlated mixture of conditional tensor products |
| Attaining measurement | A fixed four-outcome spatial-mode measurement | Translation-invariant comparisons on neighboring pairs |

The table compares the original independent-jitter and Brownian-only experiments. Both use Gaussian location mixtures and fixed-error testing, but one-photon marginal broadening alone does not identify them. The adopted sister relationship concerns their explicitly combined experiment, not an equivalence of the two original theorems.

Timing owns the [joint model, theorem](../science/joint-model.md), [correlated-record converse](../science/joint-converse.md) and [relative-mode receiver](../science/joint-receiver.md). Calibration owns the imported [collision kernel at the pinned source revision](https://github.com/GoGoKo699/Quantum-Imaging-Calibration/blob/275c70d6fa9f5a205aab0df35cfe8a7b50aa1635/science/collision-kernel.md), its independent signal/calibration theorem and a self-contained account of the joint consequence. In exact notation, its squared separation and jitter variables are twice the Timing variables. Count the shared result once rather than treating the consequence note as a second proof discovery.

The joint lower bound extracts a diagonal Gaussian covariance from the Brownian path, applies the inherited compensation kernel coordinatewise, and restores the residual correlations through a common channel. The upper bound uses a relative source distribution with an atom at zero and two nonzero atoms; it therefore requires a new gap-corrected moment construction rather than importing the binary-source receiver unchanged. Weighted shape information and the finite calibration budget jointly attain the full known-schedule order. The calibration source is stationary, independent, known-position and same-variance; it supplies no trajectory realization.

Tsang's *Semiparametric estimation for incoherent optical imaging* (2019), Sec. VII.A, Eqs. (7.17)–(7.19), supplies the exact Gaussian HG probabilities and factorial-moment imaging method. These identities, and the general advantage of moment-sensitive measurements, are inherited. The locally derived items are the relative three-point distribution, heterogeneous known-gap correction and weighted statistic with its uniform fixed-error variance bound. [Primary text, arXiv v2](https://arxiv.org/pdf/1906.04578v2), [journal](https://doi.org/10.1103/PhysRevResearch.1.033006). `Tsang2019Semiparametric`

Parniak's mutual-reference mechanism and Schlichtholz's Brownian crossover precedents remain relevant to the combined model. Neither the reappearance of a fourth-root exponent nor knowledge of a noise parameter is claimed as a new mechanism. In particular, finite calibration cannot remove physical independent displacement, and ordinary HOM access is not silently upgraded to the general relative-coordinate HG POVM.

## 6. Imported mathematical tools

The Gaussian comparison in the converse uses established multimode Gaussian fidelity machinery. Banchi, Braunstein and Pirandola (2015) derive the general formula from first and second moments; the one-mode specialization and its conventions are worked out in this repository. [Primary paper](https://arxiv.org/abs/1507.01941). `BanchiBraunsteinPirandola2015`

Fidelity-to-trace-distance inequalities are due to Fuchs and van de Graaf (1999). Their use turns state overlap bounds into statements valid for every measurement. [Primary paper](https://arxiv.org/abs/quant-ph/9712042). `FuchsVanDeGraaf1999`

The Taylor comparison between binary and Gaussian displacements, rank-one inverse updates, Brownian precision-matrix representation, Hellinger product bounds and path matchings are mathematical tools used in the proof. Their role is to connect the full correlated state to the stated schedule functional; none is presented as a new general-purpose method.

## 7. Extent of the source comparison

The following records distinguish detailed model checks from bibliographic or abstract-level checks. They do not assert an exhaustive priority search or independent replication of every cited result.

| Source | Material checked for this comparison |
|---|---|
| Tsang–Nair–Lu (2016) | Primary abstract and publication record; cited for the established static quantum-imaging result. |
| Lu et al. (2018) | Primary abstract and open publication record; cited for the static testing formulation and reported receiver optimality. |
| Schlichtholz (2025) | Primary preprint Secs. II–VII, including Eqs. (7), (9), alignment assumptions and conclusion. Publisher full text was not needed for the comparison. |
| Schlichtholz–Rudnicki (2024) | Primary preprint introduction and measurement setup; source-motion and SPADE scope checked. |
| Parniak et al. (2018) | Primary preprint introduction, one-photon model and implementation discussion; publication record. |
| De Almeida et al. (2025) | Primary preprint v5 model, common-misalignment Eq. (52), collective-measurement discussion and Sec. V; journal metadata. |
| Muratore et al. (2025) | Published abstract and primary preprint abstract; no full-theorem comparison asserted. |
| Lian et al. (2026) | Primary preprint v1 Secs. II–III, Appendix B.1 and Appendix G; preprint status retained. |
| Quantum-Imaging-Calibration | Pinned model/results, quantum converse and related-work account. |
| Tsang (2019), semiparametric imaging | Primary v2 Secs. III–IV and VII–VIII, including exact HG factorial-moment Eqs. (7.17)–(7.19). Imported as a primary technical ingredient, not a second educational anchor. |
| Banchi et al.; Fuchs–van de Graaf | Primary records checked for attribution; specialized formulas and conventions are explicitly derived in the project proof. |

The November joint comparison independently rechecked the primary Brownian-SPADE and two-photon-reference mechanisms and the HG moment identities. Grace's dissertation, [*Quantum Limits and Optimal Receivers for Passive Sub-Diffraction Imaging* (2022)](https://repository.arizona.edu/handle/10150/667290), remains a relevant fast-misalignment comparator whose full text was not accessible for this comparison. The recent Lian preprint and Qian's [*Parameter-Decoupled Quantum Superresolution without Multiparameter Estimation*, arXiv:2609.21796v1](https://arxiv.org/abs/2609.21796v1), were not independently re-audited in full in that extension; earlier detailed or abstract-level comparison extents remain as stated in the source records. No absence-of-prior-work conclusion is inferred from a full-text access gap.

The contribution claim is correspondingly specific: matching arbitrary bounded-schedule resolution laws for the stated Brownian-correlated register experiment, and its combined independent-jitter/calibration extension, with disjoint-pair attainment under the specified access model. It makes no claim to the first motion penalty, static reference-free optical receiver or HG-moment technique, to exhaustive priority certification, or to a complete finite-bandwidth optical-field theorem.
