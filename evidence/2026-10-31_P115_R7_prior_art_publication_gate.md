# P115-R7: direct literature overlap and writing gate (31 October 2026)

## Verified prior art
1. Molavi, Abtin; Saad, Feras; Albarghouthi, Aws (2026). *Analyzing Decoders for Quantum Error Correction*. arXiv:2603.20127. https://arxiv.org/abs/2603.20127 . Abstract explicitly states structured search, constrained polynomial optimization, decoder accuracy, and robustness over error-rate intervals. **The preprint's abstract and metadata were checked; the authors' implementation was not executed.**
2. Cao, ChunJun; Gullans, Michael J.; Lackey, Brad; Wang, Zitao (2024). *Quantum Lego Expansion Pack: Enumerators from Tensor Networks*. PRX Quantum 5, 030313. https://doi.org/10.1103/PRXQuantum.5.030313 . Published paper establishes optimal decoders from enumerators and exact logical error probabilities for iid channels, including nontrivial code families. The paper explicitly notes that summing exact ML success over exponentially many syndromes can remain difficult.

## Our demonstrated results and correct scope
P104-P105: orientation-sensitive ML success for [[5,1,3]], standard Clifford/noise covariance.
P106-P109: exact coset polynomials, coupling bounds, affine directional ties, standard probability and polynomial properties.
P115-R2: product-polytope vertex checks certify fixed-decoder performance and ML-decision gaps, but **not** worst-case reoptimized ML success.
P115-R4: tied channel parameters invalidate naive vertex-only minima.
P115-R5/R6: exact five-qubit shared-dephasing polynomial P(t)=(1-t)^3(6t^2+3t+1), nominal decoder remains ML over [0,1/2], and minimum over [0,1/4] equals 459/512.

## Novelty matrix
- Decoder coset enumeration: known, overlaps Cao et al.
- Robustness over uncertain error rates: known in broad form, overlaps Molavi et al.
- Exact symbolic five-qubit optimality certificate: independently reproducible worked case, **not evidence of new general method**.
- Proven computational advantage over strong published baselines: not shown.
- Independent hostile reviewer audit: not done.

## Publication gate
**NO-GO for submission as a new theorem/method.**
**GO for drafting a clearly labelled internal/provisional research manuscript** containing definitions, verified results, reproducibility protocol, exact scope, and explicit prior-art attribution. A pedagogical computational note or tutorial is a possible alternative only if the venue welcomes it; no acceptance prediction is justified.

## P115-R8 target
Choose a precisely defined capability gap from a detailed method-level reading of Molavi et al. (not merely its abstract), obtain their code if released, construct matched examples and compare certified accuracy, robustness intervals, runtime, scaling, and failure cases. Only after a genuinely distinct claim survives direct comparison should the manuscript be positioned as original research. Negative results must be retained.
