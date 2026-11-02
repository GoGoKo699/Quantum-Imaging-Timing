# Background and derivation route

This directory connects the quantum imaging framework to the Brownian timing law and the joint timing–jitter–calibration frontier. It uses one background anchor: Mankei Tsang's [*Resolving starlight: a quantum perspective*, accepted arXiv version 2](https://arxiv.org/pdf/1906.02064v2).

1. [TSANG_BRIDGE.md](TSANG_BRIDGE.md) fixes the PSF and separation conventions, builds the correlated Brownian record and works through an invariant pair. Its joint extension specifies the independent point-calibration source, explains the three-point relative source and corrected HG moments, and distinguishes physical jitter from uncertainty about its variance.
2. [MILESTONES.md](MILESTONES.md) contains exactly 30 project-defined understanding targets: 12 background milestones and 18 narrative milestones progressing from a local pair to both complete theorems and their scope.
3. [The scientific account](../science/README.md) provides direct routes to the original theorem, the [joint model and result](../science/joint-model.md), their proofs, acquisition regimes and receiver access assumptions. Those sources remain authoritative for exact claims.

The first destination is a fixed-error law for the complete timestamped quantum record without independent jitter. The second adds fresh per-photon Gaussian jitter of unknown bounded variance and a finite, explicitly charged calibration sample. The source's optical and moment framework supplies the entry point; the local proofs establish the correlated-state converse and weighted receiver guarantees.

The general joint receiver uses full HG mode resolution on relative spatial registers. Its four-outcome simplification is established for controlled close doublets. Calibration learns a distributional parameter and leaves physical signal jitter intact. The [sister calibration project](https://github.com/GoGoKo699/Quantum-Imaging-Calibration) develops the independent-jitter experiment and collision kernel inherited by the joint converse; the shared theorem's authoritative home is this repository.

The single anchor does not replace primary attribution. [Related work](../references/related-work.md) and [references.bib](../references/references.bib) distinguish established imaging and mathematical ingredients from the timing and joint-frontier contributions.

[Repository overview](../README.md)
