# P80 — Transfer audit of attached Boolean sensitivity cospectrality paper; exact LC-enumerator test
Date: 2026-10-30.

## User-supplied source
Akhtar, 'Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family', user-supplied 17-page PDF, SSRN-7544499. Pages 5–6: explicit Boolean functions with exact adjacency characteristic polynomial equality and active component profiles (16,4) vs (11,9), diameters (6,2) vs (4,4). Pages 8–10: parity XOR lift giving Cartesian product with hypercube and infinite separation N>=5. The methodological transfer is exact matched-observable nonidentifiability, followed by rigorous lift, not a transfer of Boolean adjacency cospectrality into physical Narain CFT spectra.

## Independent exact computation
Program papers/PAPER-04/code/p80_lc_polynomial.py. Starting from the exact seven-vertex P63 graphs A and B, compute all 128 graph-code words, genus-one coarse weight enumerator, and the corrected HKM 10-variable genus-two quotient from all 16384 ordered pairs. Test each of seven single-vertex local-complementation operations on both graphs. Original A vs B coarse equal, HKM10 differs at 756 coefficient positions. LC(A,4) and LC(A,5) each have coarse AND HKM10 exactly equal to B. LC(A,4) differs from A in exactly 756 HKM10 coefficient positions while coarse remains equal. Other local complementations often change even coarse genus-one polynomial. Assertions PASS.

## Interpretation and critical correction
The specific HKM10 polynomial computed in P63 is NOT invariant under arbitrary graph local complementation. A difference of 756 coefficients between original graph presentations is not, by itself, an invariant distinguishing their local-complementation equivalence classes or physical Narain CFTs. P79 had already shown that A and B lie in the same local-complementation-plus-relabeling graph orbit. P80 supplies a particularly direct one-step enumerator demonstration.

Graph local complementation, local Clifford graph-state equivalence, code equivalence, and Narain CFT physical duality are NOT automatically identical. To infer physical equivalence one must inspect exact graph-code-to-Narain construction, physical partition function, allowed code transformations and O(d,d;Z) action. Do not equate the graph enumerator to a physically normalized genus-two theta function without proof.

## Candidate methodological transfer
Construct a *physical* pair with equality of a specified observable, a difference in an invariant not removed by duality, and if possible a rigorously valid product lift. Direct-sum toroidal partition functions factor, but an unproved lifting claim must not be made. This paper's XOR parity lift is an analogy, not a CFT theorem.

## Strict publication gate
P80 exact calculation PASS; proposed 756-coefficient intrinsic separation FAILS. No new fourth-paper theorem. P81 should establish which graph transformations correspond to actual Narain CFT equivalence and test physical genus-two normalization and duality invariance. If impossible, terminate graph-code route. Paper 4 NO-GO.
