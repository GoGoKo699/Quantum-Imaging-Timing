# Scientific account

The central question is whether Brownian motion imposes a fundamental imaging limit even when the receiver retains the complete time-labelled spatial-register record. The answer depends on how that record was acquired: close pairs can preserve useful relative-position information despite a large total centroid excursion.

The sister project [Quantum-Imaging-Calibration](https://github.com/GoGoKo699/Quantum-Imaging-Calibration) asks how independent unknown jitter and a charged calibration sample change resolution. Their combined experiment has a [joint schedule-dependent frontier](joint-model.md): a physical timing/jitter floor plus the best of supplied-bound, calibration and shape information. This repository owns its full proof; the imported collision kernel remains owned and version-pinned to Calibration.

## Reading route

1. [Model and theorem](model-and-theorem.md) fixes the physical normalization, available quantum state, nuisance parameter and minimax testing criterion. It states the uniform deterministic-schedule result.
2. [Collective converse](collective-converse.md) replaces the binary source displacement by a Gaussian displacement at controlled trace distance, evaluates Gaussian fidelity, and bounds the Brownian covariance resolvent by the gap functional.
3. [Pair receiver](receiver.md) derives the exact SWAP outcome probability, independent matching outcomes and the likelihood-ratio test that attains the same scale for the composite alternative.
4. [Timing regimes](timing-regimes.md) solves the periodic boundary and compares periodic and doublet schedules at equal count and duration, with timing precision charged explicitly.
5. [Poisson arrivals](poisson-arrivals.md) treats a separate random-schedule, fixed-count experiment. Averaging over short gaps produces a logarithm under its ideal register assumptions.
6. [Direct imaging](direct-imaging.md) proves the classical benchmark for all position-processing rules and constructs an attaining pair-difference statistic.
7. [Physical interface](physical-interface.md) connects the abstract access model to photon storage, routing and mode matching, and identifies the material limits of that connection.

## Joint timing, jitter and calibration route

1. [Joint model](joint-model.md) specifies the same-jitter stationary point calibration source, the bounded nuisance class and the full fixed-error theorem for known bounded schedules.
2. [Joint converse](joint-converse.md) extracts independent Gaussian covariance from a Brownian record and applies the inherited exact compensation kernel before restoring the residual correlations.
3. [Joint receiver](joint-receiver.md) derives the relative three-point source distribution, corrects HG moments for heterogeneous known gaps, and proves a globally controlled weighted shape test.
4. [Jitter/calibration regimes](jitter-calibration-regimes.md) explains the general calibration crossover, close-doublet plateau, periodic regime and physical jitter floor.

The general joint receiver resolves the full HG mode index. The four-category version applies to controlled close doublets; it is not an implementation claim for an ordinary HOM apparatus. The general direct-imaging law has a separate position-moment proof in the joint receiver page.

The [related-work account](../references/related-work.md) credits static superresolution, Brownian SPADE and collective pair measurements separately from the full-record timing characterization. The [verification guide](../verification/README.md) records the finite checks and their relationship to the proof.

## Proof dependencies

The deterministic theorem uses two independent parts. Its impossibility statement uses the binary-to-Gaussian comparison, Gaussian fidelity and a rank-one resolvent inequality. Its attainability statement uses a translation-invariant pair measurement and product testing. The unknown centroid is averaged only as a device in the lower-bound proof; the receiver needs neither that prior nor a tracked centroid.

The periodic and doublet consequences follow from substituting their gaps into the deterministic theorem. The Poisson statement is proved for its own joint time-and-quantum experiment, since exponentially distributed gaps have no deterministic upper bound. The direct-imaging comparison has a separate classical proof and retains all spatial correlations in its lower bound.

## Physical conclusion

Photon count and mean acquisition rate do not specify a quantum imaging resolution limit by themselves. The distribution of short intervals is an additional resource. Within the stated model, pairwise comparisons extract all the order-level benefit of that resource, even though the input is a correlated many-photon record and unrestricted collective measurements are allowed.

[Repository overview](../README.md)
