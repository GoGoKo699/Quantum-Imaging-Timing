# Thirty milestones for Quantum Imaging Timing

This map connects the optical model, the testing problem and the acquisition resources to two linked results: the Brownian timing law and the joint timing–jitter–calibration frontier. Its single educational anchor is Mankei Tsang, [*Resolving starlight: a quantum perspective*, arXiv:1906.02064v2][tsang]. All anchor section numbers refer to that version. The [Tsang bridge](TSANG_BRIDGE.md) translates the review's notation and assumptions into this project's experiment.

The allocation follows the scientific structure:

| Phase | Milestones | Progression and integrative endpoint |
|---|---|---|
| Background/preliminaries | M01–M12 | From one photon's spatial state and a statistical task to the complete correlated experiment, its access assumptions and its proof requirements. M12 integrates these ingredients. |
| Narrative/innovation | M13–M30 | From one invariant pair comparison to the timing law, then to a joint receiver and converse with unknown jitter and charged calibration. M30 integrates the contribution and its limits. |

Twelve preliminary milestones provide the shared optical, probabilistic and decision-theoretic language. Eighteen narrative milestones join the original pair/fidelity timing proof to the relative-mode moment construction and covariance-extraction converse for the joint experiment. The final milestones distinguish learning a jitter variance from removing physical jitter. The map identifies the main understanding targets; specialist calculations remain in the canonical science pages.

An **anchor context** pointer identifies an entry into an idea, without attributing a project proof to the review. The Brownian record, binary-to-Gaussian comparison, Gaussian-fidelity specialization, precision-matrix bound, pair Hellinger inequalities, composite likelihood-ratio argument and the joint covariance/moment proofs are supplied in the local science. Their mathematical antecedents remain credited in [related work](../references/related-work.md#6-imported-mathematical-tools).

## Phase 1 — Background/preliminaries

### M01 — Resolution as a statistical task

**Phase:** Background/preliminaries.

**Central question:** What does it mean to resolve two sources with a finite photon budget?

**Understanding target:** Distinguish an optical width criterion, an estimation error and a one-versus-two decision error. Identify which quantity this project controls and why a prescribed error probability is needed before assigning a resolution scale.

**Dependencies and story role:** No earlier milestone. Establishes the question that gives the later states, measurements and bounds their operational meaning.

**Conceptual connection:** Connects blurred images and photon noise to a statement about what observed data can reliably distinguish.

**Source pointers:** [Tsang §§I and VIII.K][tsang]; [model §3](../science/model-and-theorem.md#3-receiver-and-testing-risk).

### M02 — One Gaussian spatial wave packet

**Phase:** Background/preliminaries.

**Central question:** Which spatial state represents one photon, and what sets its length scale?

**Understanding target:** Translate between the physical Gaussian amplitude, its intensity variance $`\sigma^2`$, and the dimensionless displacement state. Keep the separation parameter $`q=s^2/(8\sigma^2)`$ distinct from a spatial-mode index and from the design threshold $`h`$.

**Dependencies and story role:** Requires M01. Introduces the smallest quantum object in the experiment and fixes the normalization used throughout the proofs.

**Conceptual connection:** Connects physical image-plane coordinates to Hilbert-space overlaps. The Gaussian normalization is this project's specialization of the review's more general wave-packet description.

**Source pointers:** [Tsang §V][tsang]; [model §1](../science/model-and-theorem.md#1-optical-normalization); [notation bridge](TSANG_BRIDGE.md).

### M03 — Incoherence as a statistical mixture

**Phase:** Background/preliminaries.

**Central question:** How do two incoherent emitters produce a one-photon state?

**Understanding target:** Explain the fair source sign, the two displaced branches and the average of their projectors. Separate incoherent source selection from a coherent superposition, and distinguish hidden source labels from available temporal-register labels.

**Dependencies and story role:** Requires M02. Builds the two-source state before adding motion or several photons.

**Conceptual connection:** Joins an optical assumption—equal incoherent brightness—to the latent-variable representation used by both the receiver calculation and the converse.

**Source pointers:** [Tsang §V and Appendix C, especially Eq. (C14)][tsang]; [model §§1–2](../science/model-and-theorem.md#1-optical-normalization).

### M04 — What is changed by measuring position?

**Phase:** Background/preliminaries.

**Central question:** Why can different measurements of the same photon produce different resolution limits?

**Understanding target:** Identify direct imaging as a position measurement followed by classical processing. Explain why retaining the spatial quantum state permits different measurements, and why an arbitrary computation on recorded positions remains within the direct-imaging experiment.

**Dependencies and story role:** Requires M02–M03. Moves from the emitted state to the choice of observation channel.

**Conceptual connection:** Connects the review's spatial-mode viewpoint to the project's comparison between pair measurements and the complete detected-position record.

**Source pointers:** [Tsang §§III–V][tsang]; [direct imaging §1](../science/direct-imaging.md#1-observation-law-and-minimax-risk); [model §3](../science/model-and-theorem.md#3-receiver-and-testing-risk).

### M05 — Centroid and separation play different roles

**Phase:** Background/preliminaries.

**Central question:** What changes when the initial centroid is arbitrary and unknown?

**Understanding target:** Distinguish the separation of interest from the nuisance translation $`m\in\mathbb R`$. Recognize the difference between a known centered source, an estimated centroid and a measurement whose probabilities are invariant under a common translation.

**Dependencies and story role:** Requires M02–M04. Introduces the nuisance that the attaining receiver must handle without a supplied trajectory estimate.

**Conceptual connection:** Connects alignment concerns in static imaging to the possibility of extracting relative spatial information from two registers.

**Source pointers:** [Tsang §VIII.A][tsang]; [model §§2–3](../science/model-and-theorem.md#2-known-arrival-schedule-and-hidden-motion); [physical interface §2](../science/physical-interface.md#2-why-a-neighboring-pair-can-serve-as-a-spatial-reference).

### M06 — From a photon to a correlated record

**Phase:** Background/preliminaries.

**Central question:** When does averaging a hidden variable create correlations between photons?

**Understanding target:** Read the conditional product state and the expectation outside its tensor product. Explain why independent source choices do not make the trajectory-averaged registers independent, and why a product of one-photon marginals describes a different experiment.

**Dependencies and story role:** Requires M03–M05. Assembles many local states while preserving the hidden variable shared across the record.

**Conceptual connection:** Connects weak-light one-photon models to the project's explicit temporal-register interface. The review's independent temporal-mode construction does not itself derive the moving-source record.

**Source pointers:** [Tsang Appendix C, especially Eqs. (C7) and (C12)–(C14)][tsang]; [model §2](../science/model-and-theorem.md#2-known-arrival-schedule-and-hidden-motion); [physical interface §§1 and 6](../science/physical-interface.md).

### M07 — Independent increments, correlated positions

**Phase:** Background/preliminaries.

**Central question:** How does a known list of arrival gaps specify the Brownian part of the experiment?

**Understanding target:** Relate independent increments $`W_i`$, cumulative positions $`B_i`$ and known variances $`v_i=D\Delta t_i/\sigma^2`$. Explain why neighboring relative displacements can be simple even when absolute positions throughout the record are strongly correlated. Distinguish this common motion from a fresh independent displacement on each photon.

**Dependencies and story role:** Requires M05–M06. Introduces the temporal structure that will support both the invariant receiver and the precision-matrix converse.

**Conceptual connection:** Connects random spatial displacements to a specified stochastic process. The Brownian law and its schedule dependence are local model ingredients.

**Source pointers:** Anchor context: [Tsang §VIII.I][tsang], for the random-displacement viewpoint; local construction: [model §2](../science/model-and-theorem.md#2-known-arrival-schedule-and-hidden-motion).

### M08 — Fixed-error minimax risk

**Phase:** Background/preliminaries.

**Central question:** What exactly must a test guarantee for an unknown centroid and an unknown separation?

**Understanding target:** Interpret the maximum of worst type-I and type-II errors for $`q=0`$ versus $`q\ge h`$. Keep the original timing theorem's local threshold and unbounded separated alternative distinct from the joint theorem's fixed local alternative $`h\le q\le q_0`$. Distinguish both testing criteria from Fisher information or an unbiased-estimation bound.

**Dependencies and story role:** Requires M01, M04 and M05. Turns the physical question into precise quantifiers that every subsequent upper and lower bound must preserve.

**Conceptual connection:** Connects the review's estimation and testing viewpoints to a uniform composite decision problem.

**Source pointers:** [Tsang Appendix A and §§VIII.J–K][tsang]; [model §3](../science/model-and-theorem.md#3-receiver-and-testing-risk).

### M09 — What an all-receiver claim includes

**Phase:** Background/preliminaries.

**Central question:** What does it mean to rule out every permitted quantum receiver?

**Understanding target:** Describe a binary test as a quantum effect acting on the whole register state. Account for independent ancillas, storage and adaptive processing, while recognizing that trajectory monitors or revealed source signs would change the supplied experiment.

**Dependencies and story role:** Requires M04, M06 and M08. Expands the measurement class from concrete optical observations to the class used in the converse.

**Conceptual connection:** Connects quantum measurement notation to a physical boundary on available information. A general measurement bound needs the complete state family, including its correlations.

**Source pointers:** [Tsang §II and Appendix B, especially Eq. (B1)][tsang]; [model §3](../science/model-and-theorem.md#3-receiver-and-testing-risk); [physical interface §1](../science/physical-interface.md#1-what-is-supplied-to-the-receiver).

### M10 — State closeness and testing information

**Phase:** Background/preliminaries.

**Central question:** Which comparison quantities connect quantum states and classical outcomes to decision errors?

**Understanding target:** Keep the conventions for trace distance, squared quantum fidelity, classical affinity and $`H^2=1-A`$ separate. Identify the role of state closeness in a converse and of multiplying affinities for independent outcomes in an attaining test.

**Dependencies and story role:** Requires M08–M09. Supplies the conceptual interface between operational risk and the mathematical estimates used in the two proof branches.

**Conceptual connection:** Connects indistinguishability of quantum inputs to indistinguishability of every possible output, and connects independent classical records to accumulated testing evidence.

**Source pointers:** Anchor context: [Tsang §VIII.K and Appendix B][tsang]; locally supplied tools: [collective converse §§1 and 3](../science/collective-converse.md), [receiver §§2 and 4](../science/receiver.md). The fidelity and Hellinger arguments are not derived in the anchor.

### M11 — Count, duration and quantum access

**Phase:** Background/preliminaries.

**Central question:** Which resources must be specified before comparing imaging protocols?

**Understanding target:** Distinguish a fixed received count, an expected photon count, a total acquisition duration and a list of occupied-register times. Explain why a timestamp, a preserved spatial state and the ability to perform a joint spatial measurement are separate resources. Count calibration photons separately; a source revealing a distributional parameter is not a free trajectory monitor.

**Dependencies and story role:** Requires M06–M07 and M09. Adds the resource accounting needed to interpret schedule comparisons without changing the experiment silently.

**Conceptual connection:** Connects a statistical sample budget to the optical interface that supplies it. The review's mean photon number and this project's exact register count have different roles.

**Source pointers:** [Tsang §VI.G and Appendix C][tsang]; [physical interface §§3–6](../science/physical-interface.md); [timing regimes §§2–3](../science/timing-regimes.md); [notation bridge](TSANG_BRIDGE.md).

### M12 — The complete problem and the required proof

**Phase:** Background/preliminaries.

**Central question:** How do the state, nuisance, timing record, receiver class and error criterion fit into one experiment?

**Understanding target:** Assemble the supplied register state, its Brownian correlations, the known schedule and the composite minimax task. Identify the additional nuisance class and point-calibration source needed for the joint experiment. Explain why establishing an optimal resolution order requires both a receiver achieving it and a converse for the same state and the same risk.

**Dependencies and story role:** Integrates M01–M11. Ends the preliminary phase with one coherent specification and a clear explanation of what the narrative phase must establish.

**Conceptual connection:** Connects optics, stochastic motion and decision theory into the precise question: how much does the list of gaps change the best attainable testing scale?

**Source pointers:** Anchor synthesis: [Tsang §§II, VIII.A and VIII.K][tsang]; [model §§1–4](../science/model-and-theorem.md); [joint experiment](../science/joint-model.md); [physical interface §1](../science/physical-interface.md#1-what-is-supplied-to-the-receiver); [Tsang bridge](TSANG_BRIDGE.md).

## Phase 2 — Narrative/innovation

### M13 — A pair as its own spatial reference

**Phase:** Narrative/innovation.

**Central question:** How can two photons carry separation information without a known absolute centroid?

**Understanding target:** Explain why a common translation leaves a SWAP comparison unchanged. Identify the relative source-sign displacement and distinguish the invariant measurement from estimating and subtracting a centroid.

**Dependencies and story role:** Requires M02–M07 and M09. Starts the narrative with one local measurement whose nuisance invariance is exact.

**Conceptual connection:** Connects the anchor's two-photon viewpoint to the unknown-centroid Brownian experiment.

**Source pointers:** [Tsang §§VI.G and VIII.A][tsang]; [pair receiver §1](../science/receiver.md#1-exact-probability-for-a-pair); [worked pair](TSANG_BRIDGE.md#6-worked-pair-a-zero-null-probability-and-a-brownian-background).

### M14 — The exact moving-pair response

**Phase:** Narrative/innovation.

**Central question:** What makes an antisymmetric event possible under a single-source null?

**Understanding target:** Read the exact SWAP probability as a Gaussian average. Distinguish the zero-motion dark outcome from the positive background produced by an internal Brownian increment; identify how a known independent jitter variance changes that background.

**Dependencies and story role:** Requires M07 and M13. Turns the invariant measurement into an explicit observation law before applying approximations.

**Conceptual connection:** Connects spatial overlap to the contrast between a separation signal and physical random displacement.

**Source pointers:** [Tsang §VI.G][tsang]; [exact pair response](../science/receiver.md#1-exact-probability-for-a-pair); [known-jitter law](../science/joint-converse.md); [bridge worked pair](TSANG_BRIDGE.md#6-worked-pair-a-zero-null-probability-and-a-brownian-background).

### M15 — Independence recovered by a matching

**Phase:** Narrative/innovation.

**Central question:** Why may selected pair outcomes be independent even though the full photon record is correlated?

**Understanding target:** Identify the disjoint internal Brownian increments and source signs used by one adjacent matching. Explain why the two parity matchings partition the edges and why one captures at least half of a supplied nonnegative information sum.

**Dependencies and story role:** Requires M06–M07 and M13–M14. Assembles local comparisons into a record suitable for an attaining test.

**Conceptual connection:** Connects stochastic-process structure to a measurement-induced product experiment without falsely factorizing the original state.

**Source pointers:** Anchor context: [Tsang Appendix C][tsang]; local proof: [receiver §§1 and 3](../science/receiver.md); [joint relative states](../science/joint-receiver.md).

### M16 — One gap and its testing information

**Phase:** Narrative/innovation.

**Central question:** Why does one gap contribute an interpolation between a dark-event and a noisy-background scale?

**Understanding target:** Explain the role of $`q^2/(q+v_i)`$ in finite-error testing. Keep a uniform interpolation distinct from a fixed-positive-gap Taylor expansion or a Fisher-information formula.

**Dependencies and story role:** Requires M08, M10 and M14–M15. Establishes the local information quantity that the schedule theorem sums.

**Conceptual connection:** Connects a physical null background to Hellinger affinity and its accumulation over independent outcomes.

**Source pointers:** [Tsang §§VIII.J–K][tsang]; [pair information](../science/receiver.md#2-the-pairs-testing-information); [bridge §6](TSANG_BRIDGE.md#6-worked-pair-a-zero-null-probability-and-a-brownian-background).

### M17 — A converse that retains the correlated state

**Phase:** Narrative/innovation.

**Central question:** How can a lower bound cover every receiver rather than only the proposed pair apparatus?

**Understanding target:** Explain the controlled replacement of binary source shifts by Gaussian shifts, its trace-distance remainder and the Gaussian-fidelity comparison on the full covariance. Identify the allowed centroid prior as a converse device, not supplied information.

**Dependencies and story role:** Requires M09–M10 and M12. Builds the all-receiver proof independently of the attaining pair measurement.

**Conceptual connection:** Connects quantum state closeness, data processing and a tractable Gaussian comparison while preserving temporal correlations.

**Source pointers:** Anchor context: [Tsang §II and Appendix B][tsang]; [collective converse §§1–3](../science/collective-converse.md); [related mathematical tools](../references/related-work.md#6-imported-mathematical-tools).

### M18 — Brownian precision closes the timing law

**Phase:** Narrative/innovation.

**Central question:** How do upper and lower proofs lead to the same function of the supplied gaps?

**Understanding target:** Explain how sparse Brownian precision bounds the covariance resolvent and controls the Gaussian-replacement remainder. Combine this lower bound with the matching receiver to interpret $`\sum_i h^2/(h+v_i)=\Theta(1)`$ as a minimax testing boundary.

**Dependencies and story role:** Requires M15–M17. Integrates the original receiver and converse into the first complete theorem.

**Conceptual connection:** Connects local gap structure to the best distinguishability of the entire correlated quantum record.

**Source pointers:** [Tsang §§II and VIII.K][tsang]; [collective converse §§4–5](../science/collective-converse.md); [uniform timing theorem](../science/model-and-theorem.md#5-uniform-resolution-theorem).

### M19 — Which acquisition experiment is being compared?

**Phase:** Narrative/innovation.

**Central question:** Which change of timing resources can change the physical-separation exponent?

**Understanding target:** Compare periodic arrivals, close doublets and fixed-total-duration acquisition at their stated count and duration budgets. Explain why the fixed-count Poisson logarithm is a separate unbounded-gap, average-risk experiment and needs close arrivals to remain addressable.

**Dependencies and story role:** Requires M11 and M18. Derives acquisition meaning from the timing law before adding another nuisance.

**Conceptual connection:** Connects a mathematical gap list to bandwidth, temporal modes, count stopping and experimental duration.

**Source pointers:** [Tsang §VI.G and Appendix C][tsang]; [timing regimes](../science/timing-regimes.md); [Poisson experiment](../science/poisson-arrivals.md); [physical interface](../science/physical-interface.md).

### M20 — A jitter scale and a charged calibration source

**Phase:** Narrative/innovation.

**Central question:** What information does a finite point-source calibration sample actually supply?

**Understanding target:** Specify the Gaussian nuisance class $`0\le w\le b`$ and the independent stabilized known-centroid calibration photons with the same variance. Distinguish a bound on an unknown variance, a known actual variance and a measurement of each realized displacement.

**Dependencies and story role:** Requires M05–M12 and M18. Defines the joint experiment without silently supplying a trajectory reference.

**Conceptual connection:** Connects the independent-jitter sister experiment to the Brownian record while keeping physical noise and uncertainty about it separate.

**Source pointers:** [Tsang §§VIII.A and VIII.K][tsang]; [joint experiment §§1–2](../science/joint-model.md); [calibration sister](https://github.com/GoGoKo699/Quantum-Imaging-Calibration); [bridge joint extension](TSANG_BRIDGE.md#8-adding-independent-jitter-and-a-finite-calibration-sample).

### M21 — The relative mode has a three-point source

**Phase:** Narrative/innovation.

**Central question:** What remains after the common translation is removed from a doublet?

**Understanding target:** Derive the relative Gaussian variance $`w+v_i/2`$ and source shift that is zero with probability one half and each of $`\pm\sqrt{2q}`$ with probability one quarter. Explain why this differs from the original binary source and why disjoint relative states are independent.

**Dependencies and story role:** Requires M13–M15 and M20. Finds a centroid-free observation experiment to which the calibration mechanism can validly transfer.

**Conceptual connection:** Connects two-register spatial coordinates to a new source distribution whose moments carry the joint signal.

**Source pointers:** Anchor context: [Tsang §VI.G][tsang]; local derivation: [joint relative-mode receiver](../science/joint-receiver.md); [physical interface](../science/physical-interface.md).

### M22 — Corrected Hermite–Gaussian moments

**Phase:** Narrative/innovation.

**Central question:** How can a known, different Brownian gap be removed from each pair's moment formula?

**Understanding target:** Interpret the conditional HG index law and the corrected observables $`A_i=2Q_i-d_i`$ and $`B_i=(4/3)Q_i(Q_i-1)-4d_iQ_i+d_i^2`$, with $`d_i=v_i/2`$. Explain their common means $`w+q`$ and $`(w+q)^2-q^2/3`$.

**Dependencies and story role:** Requires M02–M04 and M21. Supplies the local identities needed for heterogeneous weighted tests.

**Conceptual connection:** Connects spatial moments to observed mode indices; the index measures the relative spatial register's oscillator excitation, not an additional photon resource.

**Source pointers:** Anchor context: [Tsang §§VII.A–B][tsang]; exact HG identities and attribution: [joint receiver](../science/joint-receiver.md); [related work](../references/related-work.md).

### M23 — Bound and calibration tests with schedule weights

**Phase:** Narrative/innovation.

**Central question:** How do the receiver's supplied bounds and calibration counts become two different detection routes?

**Understanding target:** Explain inverse-variance weighting of corrected relative moments and why one parity matching retains a fixed fraction of the timing information. Contrast the known-bound threshold with subtracting an independent calibration estimate whose variance is $`O(b/M)`$.

**Dependencies and story role:** Requires M15–M16 and M20–M22. Builds two attaining branches without estimating the Brownian path.

**Conceptual connection:** Connects finite calibration information to physical signal fluctuations; the calibration stream does not inherit the signal's Brownian variance.

**Source pointers:** [Tsang §§VII.A–B and VIII.K][tsang]; [joint receiver](../science/joint-receiver.md); [joint frontier](../science/joint-model.md#3-joint-frontier).

### M24 — A weighted shape statistic removes variance ambiguity

**Phase:** Narrative/innovation.

**Central question:** How can separation remain detectable without enough calibration photons?

**Understanding target:** Explain why a cross-product of distinct corrected moments removes $`(w+q)^2`$ but retains $`-q^2/3`$. Identify the inverse-square gap weights, the normalization excluding diagonal products and the global variance bound that controls every separated alternative.

**Dependencies and story role:** Requires M10 and M21–M23. Establishes the shape branch as a valid uniform test rather than an identifiability heuristic.

**Conceptual connection:** Connects the non-Gaussian fourth cumulant to a measured statistic even when second moments confound separation and jitter.

**Source pointers:** Anchor context: [Tsang §§VII.A–B and VIII.K][tsang]; local weighted-statistic proof: [joint receiver](../science/joint-receiver.md); [joint frontier](../science/joint-model.md#3-joint-frontier).

### M25 — Extracting independent noise from Brownian covariance

**Phase:** Narrative/innovation.

**Central question:** How can a correlated-record converse use an independent-jitter collision calculation?

**Understanding target:** Explain the diagonal covariance extraction from sparse Brownian precision and the positive residual Gaussian translation channel. Identify why the extracted independent experiment is more informative and why neighboring-gap sums retain the schedule dependence.

**Dependencies and story role:** Requires M10, M17–M18 and M20. Opens the joint converse without assuming that the actual signal photons are independent.

**Conceptual connection:** Connects a matrix order relation to a comparison of statistical experiments and a valid transfer boundary between the sister results.

**Source pointers:** Anchor context: [Tsang §II and Appendix B][tsang]; local extraction proof: [joint converse](../science/joint-converse.md); [original Brownian precision proof](../science/collective-converse.md#4-brownian-precision-controls-the-resolvent).

### M26 — Compensated hard worlds and an all-receiver obstruction

**Phase:** Narrative/innovation.

**Central question:** Why may a minimax converse compare a null and alternative with different jitter variances?

**Understanding target:** Describe the admissible comparison $`w_0=b/2`$, $`w_1=w_0-q`$ and exact signal-variance compensation. Explain the signal shape cost and finite-calibration variance cost, while keeping one common variance within each physical world.

**Dependencies and story role:** Requires M08–M10, M20 and M25. Establishes the nuisance lower bound against every joint receiver using the inherited collision identity with its exact conventions.

**Conceptual connection:** Connects composite-hypothesis geometry, channel contraction and the cost of learning an unknown noise scale.

**Source pointers:** [Tsang §§VIII.J–K][tsang]; [joint converse](../science/joint-converse.md); [Calibration collision kernel](https://github.com/GoGoKo699/Quantum-Imaging-Calibration/blob/main/science/collision-kernel.md).

### M27 — The complete joint frontier and classical benchmark

**Phase:** Narrative/innovation.

**Central question:** How do a physical timing floor and three uncertainty routes combine into one matching result?

**Understanding target:** Interpret $`R_Q=r_0+\min\{b,\sqrt{b/M},S_2^{-1/4}\}`$ with its endpoint conventions, uniform constants and fixed local alternative. Explain why the direct-imaging law has no additional schedule dependence under bounded gaps, and why lower bounds and attaining branches describe the same experiment.

**Dependencies and story role:** Requires M18 and M20–M26. Integrates the full quantum construction and converse before interpreting crossover regimes.

**Conceptual connection:** Connects physical noise, finite calibration and shape sensitivity without multiplying pre-existing bounds or replacing noise by a learned parameter.

**Source pointers:** [Tsang §§III–V and VIII.K][tsang]; [joint theorem §§3–4](../science/joint-model.md#3-joint-frontier); [joint converse](../science/joint-converse.md); [joint receiver](../science/joint-receiver.md).

### M28 — Close doublets expose two calibration crossovers

**Phase:** Narrative/innovation.

**Central question:** When does more calibration improve resolution, and when does the physical jitter floor take over?

**Understanding target:** Derive the close-doublet reduction with $`K=NM/(N+M)`$. Distinguish the shape/calibration crossover $`K\asymp\sqrt N`$ from escaping a plateau, which needs $`Kb\gg1`$, and identify when calibration is irrelevant because the ideal photon floor is already reached.

**Dependencies and story role:** Requires M19–M20 and M27. Converts the general theorem into an acquisition design rule with all calibration photons charged.

**Conceptual connection:** Connects short internal Brownian intervals to the uncertainty plateau and shows why a comparable calibration budget reaches the known-jitter order.

**Source pointers:** [Tsang §§VI.G and VIII.K][tsang]; [close-doublet regimes](../science/jitter-calibration-regimes.md#2-close-doublets); [physical floor](../science/jitter-calibration-regimes.md#3-physical-jitter-remains-after-calibration); [timing resources](../science/timing-regimes.md).

### M29 — The receiver capability and its physical boundary

**Phase:** Narrative/innovation.

**Central question:** Which parts of the mathematical receiver must a physical experiment actually supply?

**Understanding target:** Distinguish the spatial SWAP bit, the full relative-HG joint POVM and the four-outcome construction proved for controlled close doublets. Account for addressability, storage, coherent operations, noise matching, all photon counts and the absence of a path monitor; identify limits of finite numerical checks.

**Dependencies and story role:** Requires M09, M11, M19 and M21–M28. Tests the physical interpretation of the entire attaining construction rather than inferring hardware from an abstract POVM.

**Conceptual connection:** Connects the review's weak-light framework to actual temporal and spatial access, while keeping physical jitter after calibration visible.

**Source pointers:** [Tsang §VI.G and Appendix C][tsang]; [physical interface](../science/physical-interface.md); [joint receiver](../science/joint-receiver.md); [verification guide](../verification/README.md).

### M30 — Timing and calibration as one scientific statement

**Phase:** Narrative/innovation.

**Central question:** What has the project established, which ingredients are inherited, and where does the joint claim end?

**Understanding target:** Explain the complete route from correlated Brownian registers to the original timing law and the joint schedule-dependent frontier. Separate physical jitter from uncertainty about its scale, state the calibration source assumptions and distinguish the full general receiver from the close-doublet simplification. Credit the timing and independent-calibration contributions once and keep theorem, finite checks and optical implementation claims distinct.

**Dependencies and story role:** Integrates M12 and M13–M29. Ends the narrative with the result, mechanism, acquisition resources, sister ownership and limitations understood together.

**Conceptual connection:** Connects the anchor's quantum-imaging framework to the project's conclusion: known timing can suppress common motion, while independent physical displacement survives even perfect calibration.

**Source pointers:** Anchor synthesis: [Tsang §§II, VIII.K and X][tsang]; [scientific route](../science/README.md); [joint model §5](../science/joint-model.md#5-ownership-and-reading-route); [regime synthesis](../science/jitter-calibration-regimes.md); [related work](../references/related-work.md); [verification limits](../verification/README.md).

[tsang]: https://arxiv.org/pdf/1906.02064v2
