# Thirty milestones for Quantum Imaging Timing

This map connects the optical model, the testing problem, the proofs and the acquisition resources that determine the result. Its single educational anchor is Mankei Tsang, [*Resolving starlight: a quantum perspective*, arXiv:1906.02064v2][tsang]. All anchor section numbers refer to that version. The [Tsang bridge](TSANG_BRIDGE.md) translates the review's notation and assumptions into this project's experiment.

The allocation follows the scientific structure:

| Phase | Milestones | Progression and integrative endpoint |
|---|---|---|
| Background/preliminaries | M01–M12 | From one photon's spatial state and a statistical task to the complete correlated experiment, its access assumptions and its proof requirements. M12 integrates these ingredients. |
| Narrative/innovation | M13–M30 | From one invariant pair comparison to matching upper and lower bounds, then to acquisition regimes and the physical meaning of the result. M30 integrates the contribution and its limits. |

Twelve preliminary milestones provide the shared optical, probabilistic and decision-theoretic language. Eighteen narrative milestones are needed because the result joins two substantial arguments—an attaining receiver and an all-receiver converse—and then distinguishes several acquisition experiments. The map identifies the main understanding targets; specialist calculations remain in the canonical science pages.

An **anchor context** pointer identifies an entry into an idea, without attributing a project proof to the review. The Brownian record, binary-to-Gaussian comparison, Gaussian-fidelity specialization, precision-matrix bound, pair Hellinger inequalities and composite likelihood-ratio argument are supplied in the local science. Their mathematical antecedents remain credited in [related work](../references/related-work.md#6-imported-mathematical-tools).

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

**Understanding target:** Relate independent increments $`W_i`$, cumulative positions $`B_i`$ and known variances $`v_i=D\Delta t_i/\sigma^2`$. Explain why neighboring relative displacements can be simple even when absolute positions throughout the record are strongly correlated.

**Dependencies and story role:** Requires M05–M06. Introduces the temporal structure that will support both the invariant receiver and the precision-matrix converse.

**Conceptual connection:** Connects random spatial displacements to a specified stochastic process. The Brownian law and its schedule dependence are local model ingredients.

**Source pointers:** Anchor context: [Tsang §VIII.I][tsang], for the random-displacement viewpoint; local construction: [model §2](../science/model-and-theorem.md#2-known-arrival-schedule-and-hidden-motion).

### M08 — Fixed-error minimax risk

**Phase:** Background/preliminaries.

**Central question:** What exactly must a test guarantee for an unknown centroid and an unknown separation?

**Understanding target:** Interpret the maximum of worst type-I and type-II errors for $`q=0`$ versus $`q\ge h`$. Keep a local restriction on the chosen threshold $`h`$ separate from the unbounded alternative, and distinguish this criterion from Fisher information or an unbiased-estimation bound.

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

**Understanding target:** Distinguish a fixed received count, an expected photon count, a total acquisition duration and a list of occupied-register times. Explain why a timestamp, a preserved spatial state and the ability to interfere two stored photons are separate resources.

**Dependencies and story role:** Requires M06–M07 and M09. Adds the resource accounting needed to interpret schedule comparisons without changing the experiment silently.

**Conceptual connection:** Connects a statistical sample budget to the optical interface that supplies it. The review's mean photon number and this project's exact register count have different roles.

**Source pointers:** [Tsang §VI.G and Appendix C][tsang]; [physical interface §§3–6](../science/physical-interface.md); [timing regimes §§2–3](../science/timing-regimes.md); [notation bridge](TSANG_BRIDGE.md).

### M12 — The complete problem and the required proof

**Phase:** Background/preliminaries.

**Central question:** How do the state, nuisance, timing record, receiver class and error criterion fit into one experiment?

**Understanding target:** Assemble the supplied register state, its Brownian correlations, the known schedule and the composite minimax task. Explain why establishing an optimal resolution order requires both a receiver achieving it and a converse for the same state and the same risk.

**Dependencies and story role:** Integrates M01–M11. Ends the preliminary phase with one coherent specification and a clear explanation of what the narrative phase must establish.

**Conceptual connection:** Connects optics, stochastic motion and decision theory into the precise question: how much does the list of gaps change the best attainable testing scale?

**Source pointers:** Anchor synthesis: [Tsang §§II, VIII.A and VIII.K][tsang]; [model §§1–4](../science/model-and-theorem.md); [physical interface §1](../science/physical-interface.md#1-what-is-supplied-to-the-receiver); [Tsang bridge](TSANG_BRIDGE.md).

## Phase 2 — Narrative/innovation

### M13 — A pair as its own spatial reference

**Phase:** Narrative/innovation.

**Central question:** How can two photons reveal separation information without locating their common centroid?

**Understanding target:** Explain the symmetric and antisymmetric SWAP sectors and their invariance under a common translation. Relate the antisymmetric probability for two pure spatial states to their overlap, while keeping the abstract measurement distinct from its optical realization.

**Dependencies and story role:** Requires M02, M05, M09 and M12. Starts the new mechanism at the level of one pair rather than the full acquisition.

**Conceptual connection:** Connects relative spatial information to an invariant quantum comparison; the reference-free comparison idea has static precedents.

**Source pointers:** Anchor context: [Tsang §VI.G][tsang]; local calculation: [receiver §1](../science/receiver.md#1-exact-probability-for-a-pair); [physical interface §§2–3](../science/physical-interface.md).

### M14 — The exact response to a moving pair

**Phase:** Narrative/innovation.

**Central question:** How do source separation and motion during a gap enter the same measurement outcome?

**Understanding target:** Follow the averaging over the three possible source-label differences and the Gaussian Brownian increment. Interpret the exact response $`p_v(q)`$, its motion-induced null background and its monotone increase with separation.

**Dependencies and story role:** Requires M03, M07 and M13. Converts the invariant pair idea into a quantitative probability law that is valid before any small-parameter approximation.

**Conceptual connection:** Connects Gaussian wave-packet overlaps to the competition between relative source displacement and relative centroid motion.

**Source pointers:** Anchor context: [Tsang §V][tsang]; local pair law and Gaussian integration: [receiver §1](../science/receiver.md#1-exact-probability-for-a-pair).

### M15 — Independence recovered by the measurement

**Phase:** Narrative/innovation.

**Central question:** Why can selected pair outcomes be independent when the quantum input record is correlated?

**Understanding target:** Trace each outcome to its pair's internal Brownian increment and two source signs. Explain why disjoint adjacent pairs use independent ingredients after common translations cancel, and why this argument does not justify independence for arbitrary photon measurements.

**Dependencies and story role:** Requires M06–M07 and M14. Lifts the single-pair response to a usable collection of classical observations without discarding the original correlations by assumption.

**Conceptual connection:** Connects symmetry of a measurement with conditional independence in a latent stochastic model.

**Source pointers:** Anchor context: [Tsang Appendix C][tsang], for the role of product assumptions; local independence proof: [receiver §1, independence subsection](../science/receiver.md#why-the-selected-outcomes-are-independent).

### M16 — The information carried by one gap

**Phase:** Narrative/innovation.

**Central question:** Why does one pair contribute the scale $`h^2/(v+h)`$?

**Understanding target:** Relate the pair's signal change, null background and Hellinger distance. Distinguish the nearly static regime $`v\ll h`$ from the motion-dominated regime $`v\gg h`$, and recognize that the estimate is uniform across their crossover.

**Dependencies and story role:** Requires M10 and M14. Identifies the local quantity whose sum will govern the complete schedule.

**Conceptual connection:** Connects the physical background in a binary measurement to finite-error testing information, without substituting Fisher information evaluated exactly at the null.

**Source pointers:** Anchor context: [Tsang §VIII.K][tsang]; locally supplied Hellinger bounds: [receiver §2](../science/receiver.md#2-the-pairs-testing-information); [model §4](../science/model-and-theorem.md#4-schedule-information).

### M17 — From pair information to a composite test

**Phase:** Narrative/innovation.

**Central question:** How can one executable receiver exploit a general known schedule and cover every $`q\ge h`$?

**Understanding target:** Explain why the two parity matchings retain at least half the total gap weight. Connect their independent outcomes to a likelihood-ratio test designed at $`h`$, and use the increasing rejection event to extend its guarantee to every larger actual separation.

**Dependencies and story role:** Requires M08, M12 and M15–M16. Completes the attaining branch, including the distinction between a chosen threshold and an unknown parameter.

**Conceptual connection:** Connects a simple path matching, product affinities and stochastic ordering to a uniform composite error guarantee.

**Source pointers:** Anchor context: [Tsang §VIII.K and Appendix B][tsang]; local matching and testing proofs: [receiver §§3–4](../science/receiver.md#3-choose-the-matching-at-the-design-threshold).

### M18 — A controlled Gaussian comparison

**Phase:** Narrative/innovation.

**Central question:** Why is a Gaussian surrogate useful, and what makes replacing binary source signs legitimate?

**Understanding target:** Explain the matching displacement moments through third order and the fourth-order trace-norm remainder. Account for the accumulated $`Nq^2`$ cost under tensor telescoping and the common Brownian channel, without treating the original binary-source state as Gaussian.

**Dependencies and story role:** Requires M02–M03, M06, M10 and M12. Starts the converse branch by reducing a non-Gaussian correlated state to a comparison whose error is explicitly controlled.

**Conceptual connection:** Connects the physical two-branch mixture to moment comparison and stability under a common quantum channel.

**Source pointers:** Anchor context: [Tsang §V and Appendix C][tsang]; locally supplied comparison: [collective converse §2](../science/collective-converse.md#2-a-uniform-gaussian-replacement-bound).

### M19 — Fidelity without discarding correlations

**Phase:** Narrative/innovation.

**Central question:** How does the Gaussian comparison make a bound on the entire record tractable?

**Understanding target:** Explain how a common orthogonal coordinate transformation diagonalizes the displacement covariance and preserves the spatial vacuum. Track squared versus root fidelity and the conversion to a resolvent bound on trace distance. Recognize the diagonalization as a mathematical comparison, without requiring the attaining receiver to implement it.

**Dependencies and story role:** Requires M07, M10 and M18. Converts the full correlated Gaussian state into a computable distinguishability bound.

**Conceptual connection:** Connects covariance eigenmodes to a measurement-independent limit; the correlations are represented and transformed, rather than omitted.

**Source pointers:** Anchor context: [Tsang §II and Appendix B][tsang]; local fidelity specialization: [collective converse §3](../science/collective-converse.md#3-fidelity-of-the-gaussian-comparison-states); mathematical attribution: [related work §6](../references/related-work.md#6-imported-mathematical-tools). The review does not supply this Gaussian-fidelity proof.

### M20 — Brownian precision reveals the gap functional

**Phase:** Narrative/innovation.

**Central question:** How can a global covariance bound be expressed using individual arrival gaps?

**Understanding target:** Explain the cumulative-sum covariance and the first-difference precision matrix. Identify how rank-one inverse updates control $`\operatorname{tr}(C+hI)^{-1}`$ by a sum of regularized inverse increments, and why this step is uniform over uneven positive gaps.

**Dependencies and story role:** Requires M07 and M19. Connects the converse's global spectral quantity to the same local timing weights already found by the pair receiver.

**Conceptual connection:** Connects the Markov structure of Brownian motion to a matrix inequality that exposes acquisition resources.

**Source pointers:** Anchor context: [Tsang §II][tsang], for the goal of a receiver-independent limit; locally supplied precision and resolvent proof: [collective converse §4](../science/collective-converse.md#4-brownian-precision-controls-the-resolvent). Brownian precision is outside the anchor's derivation.

### M21 — Closing the nuisance-uniform converse

**Phase:** Narrative/innovation.

**Central question:** How does a Gaussian prior on an unrestricted nuisance establish a worst-case lower bound?

**Understanding target:** Explain why the same auxiliary centroid prior under both hypotheses gives a valid Bayes subproblem of the minimax task. Identify its covariance contribution, distinguish it from a physical first waiting time, and show how bounded gap variances absorb the Gaussian-replacement cost into the schedule scale.

**Dependencies and story role:** Requires M05, M08, M12 and M18–M20. Completes the all-receiver branch with the original nuisance quantifiers intact.

**Conceptual connection:** Connects a proof prior to a uniform impossibility result without imposing that prior on the source or the receiver.

**Source pointers:** Anchor context: [Tsang §§VIII.A and VIII.J][tsang]; local minimax reduction and closure: [collective converse §§1 and 5](../science/collective-converse.md).

### M22 — The matching resolution theorem

**Phase:** Narrative/innovation.

**Central question:** What is established when the receiver and the converse produce the same schedule scale?

**Understanding target:** State the fixed-error transition $`\mathcal I(h;v)\asymp1`$ with its bounded-gap assumptions and uniform constants. Explain the role of the marker solving $`\mathcal I(h_*;v)=1`$, and distinguish an optimal order from an exact error-calibrated threshold or an estimation-risk theorem.

**Dependencies and story role:** Requires M17 and M21. Joins both proof branches into the central result before drawing acquisition-specific consequences.

**Conceptual connection:** Connects a practical pair construction and an unrestricted collective bound to the sufficiency of neighboring-pair information in this model.

**Source pointers:** Anchor context: [Tsang §§II and VIII.K][tsang]; [model §§4–5](../science/model-and-theorem.md#4-schedule-information); [receiver §4](../science/receiver.md#4-a-complete-test-and-its-error-guarantee); [collective converse §5](../science/collective-converse.md#5-close-the-minimax-bound).

### M23 — The complete direct-imaging benchmark

**Phase:** Narrative/innovation.

**Central question:** What is lost when every spatial register is measured in position before further processing?

**Understanding target:** Explain the lower bound for every processing rule using the position record, including contraction after adding the correlated Brownian displacement. Connect independent pair differences and their exact second and fourth moments to an upper bound uniform over all $`q\ge h`$. Translate $`h\asymp N^{-1/2}`$ into physical separation order $`N^{-1/4}`$.

**Dependencies and story role:** Requires M02, M04, M07–M08 and M22. Establishes the operational benchmark against which the timing-dependent quantum advantage is interpreted.

**Conceptual connection:** Connects position shot noise, classical data processing and translation-invariant statistics to a fully matched classical comparison.

**Source pointers:** Anchor context: [Tsang §§III and VIII.J–K][tsang]; local Brownian benchmark: [direct imaging §§1–5](../science/direct-imaging.md); [model §6](../science/model-and-theorem.md#6-direct-imaging-benchmark).

### M24 — Reading the periodic crossover

**Phase:** Narrative/innovation.

**Central question:** How does the gap functional recover the two periodic separation exponents?

**Understanding target:** Connect the periodic quadratic equation for $`h_*`$ to the competition between the motion increment and $`1/N`$. Translate the result into physical separation and arrival spacing, keeping a fixed positive mean interval distinct from a duration held fixed as count grows.

**Dependencies and story role:** Requires M07, M11 and M22. Provides the first transparent acquisition consequence of the general theorem.

**Conceptual connection:** Connects the global testing law to a motion-versus-sampling crossover. The familiar exponents alone do not identify the new all-receiver result.

**Source pointers:** Anchor context: [Tsang §VIII.A][tsang], for the centering issue; local periodic analysis: [timing regimes §1](../science/timing-regimes.md#1-regular-sampling-diffusion-competes-with-the-next-photon); attribution: [related work §2](../references/related-work.md#2-brownian-motion-and-dynamic-source-spade).

### M25 — Equal budgets, different short-gap structure

**Phase:** Narrative/innovation.

**Central question:** How can two schedules with the same count and duration have different resolution orders?

**Understanding target:** Follow the exact close-doublet construction and the compensating between-doublet gaps. Explain why a fixed fraction of $`1/N`$-scale internal gaps supports $`h\asymp1/N`$ while the common duration grows proportionally to $`N`$.

**Dependencies and story role:** Requires M11, M15, M22 and M24. Demonstrates why count and average rate do not determine the schedule's information by themselves.

**Conceptual connection:** Connects invariant relative measurements to controlled acquisition timing. The improvement changes the supplied schedule and requires shrinking actual internal intervals.

**Source pointers:** Anchor context: [Tsang §VI.G][tsang]; local construction and resource comparison: [timing regimes §2](../science/timing-regimes.md#2-equal-photon-count-and-duration-at-fixed-mean-rate); [physical interface §5](../science/physical-interface.md#5-what-timing-means).

### M26 — Which timing constraint changes the exponent?

**Phase:** Narrative/innovation.

**Central question:** How do fixed duration and a positive actual-gap floor alter the doublet comparison?

**Understanding target:** Explain the fixed-duration bound obtained from convexity and why all positive-gap schedules then share the same quantum separation order. Separately explain why a fixed positive floor, together with a fixed upper-gap bound, restores the slower asymptotic order, and why a fixed duration plus a floor limits the possible count.

**Dependencies and story role:** Requires M11 and M22–M25. Resolves the resource qualifications needed to interpret the schedule contrast globally.

**Conceptual connection:** Connects constraints on the sum and minimum of the gaps to different asymptotic experiments; mean rate, total duration and short-gap capability are distinct resources.

**Source pointers:** Anchor context: [Tsang §I and §V][tsang], for photon-budgeted statistical resolution; local constraint analysis: [timing regimes §§3–4](../science/timing-regimes.md#3-a-fixed-total-duration-changes-the-comparison).

### M27 — A random schedule is a new experiment

**Phase:** Narrative/innovation.

**Central question:** What must be specified before averaging the timing law over Poisson arrivals?

**Understanding target:** Define the exact recorded count, the first-photon time origin, the observed exponential gaps and the risk averaged over timestamps. Explain why unbounded gaps require a separate argument and why fixed-count stopping differs from a fixed-duration experiment.

**Dependencies and story role:** Requires M06–M08, M11 and M22. Sets up the random-schedule consequence without importing an invalid maximum-gap assumption.

**Conceptual connection:** Connects conditional quantum states to a joint classical–quantum record. Counting conventions in a weak-light model do not by themselves specify this stopping rule.

**Source pointers:** Anchor context: [Tsang §V and Appendix C][tsang]; local experiment: [Poisson arrivals §§1–2 and 7](../science/poisson-arrivals.md); [notation bridge](TSANG_BRIDGE.md).

### M28 — The Poisson logarithm and uniform crossover

**Phase:** Narrative/innovation.

**Central question:** How do rare short gaps produce a logarithm without a worst-schedule guarantee?

**Understanding target:** Connect the resolvent average and the joint gap–outcome affinity to the same factor $`h^2\kappa^{-1}\log(1+\kappa/h)`$. Explain why the converse handles the full exponential distribution, why the receiver still covers every larger separation, and how the root inversion distinguishes fixed positive $`\kappa`$ from $`N\kappa=O(1)`$.

**Dependencies and story role:** Requires M17, M19–M21 and M27. Integrates the random experiment's lower and upper bounds into its complete crossover, including the family-specific meaning of its rate requirement.

**Conceptual connection:** Connects short-gap statistics to finite-error distinguishability. The logarithm comes from the distribution of useful intervals, with the design threshold regularizing the small-gap contribution.

**Source pointers:** Anchor context: [Tsang §VIII.K][tsang]; locally supplied random-schedule proof and inversion: [Poisson arrivals §§3–6 and 8](../science/poisson-arrivals.md); [timing regimes §5](../science/timing-regimes.md#5-relation-to-ideal-poisson-sampling-and-direct-imaging).

### M29 — Translating the result into an optical interface

**Phase:** Narrative/innovation.

**Central question:** Which physical capabilities are required for the stated quantum advantage to apply?

**Understanding target:** Connect supplied register addressability to spatial-state-preserving capture, delay, routing and nonspatial mode matching. Distinguish an actual minimum gap, timestamp coarsening and overlapping optical pulses. Identify why ideal arbitrarily close Poisson registers do not automatically describe a finite-bandwidth field.

**Dependencies and story role:** Requires M11, M13, M25–M28. Collects the implementation assumptions that determine the meaning and limits of the schedule consequences.

**Conceptual connection:** Connects a statistically optimal abstract measurement to an optical experiment with specified occupancy, coherence and loss resources.

**Source pointers:** [Tsang §VI.G and Appendix C][tsang]; [physical interface §§3–6](../science/physical-interface.md); [Poisson arrivals §8](../science/poisson-arrivals.md#8-what-creates-the-logarithm); [receiver §5](../science/receiver.md#5-optical-meaning-and-scope).

### M30 — The contribution as a complete scientific statement

**Phase:** Narrative/innovation.

**Central question:** What has the project established, how do its parts support one another, and where does the claim end?

**Understanding target:** Explain the path from the correlated register model through the pair receiver and collective converse to the timing functional, direct-imaging benchmark and acquisition consequences. Separate inherited imaging and mathematical ingredients from the schedule-dependent characterization. Distinguish analytical guarantees, finite numerical corroboration and physical implementation assumptions.

**Dependencies and story role:** Integrates M12 and M13–M29. Ends the narrative with the theorem, mechanism, resource tradeoffs, attribution and scope understood as one connected result.

**Conceptual connection:** Connects the anchor's quantum-imaging perspective to this project's specific conclusion: neighboring-pair information attains the resolution order of the complete Brownian-correlated spatial-register record, while timing resources determine what that order is.

**Source pointers:** Anchor synthesis: [Tsang §§II and X][tsang]; [model §§5–7](../science/model-and-theorem.md#5-uniform-resolution-theorem); [timing regimes](../science/timing-regimes.md); [physical interface](../science/physical-interface.md); [related work §§1–7](../references/related-work.md); [verification limits](../verification/README.md#limits-of-verification).

[tsang]: https://arxiv.org/pdf/1906.02064v2
