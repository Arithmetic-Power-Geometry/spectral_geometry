# P78 — Hermetic-inspired symmetry conjecture and graph-presentation kill test
Date: 2026-10-30.

## Interpretation
Hermetic correspondence/polarity is used as a heuristic: look for symmetry information hidden by the coarse genus-one enumerator. It supplies no mathematical axiom or physical evidence. Exact enumeration and adversarial equivalence testing supply the evidence.

## Exact inputs and results
Graph A edges: 01 02 03 12 23 14 24 34 45 46 05 13 15.
Graph B edges: 01 02 03 12 23 14 24 34 45 46 56.
P63 already established equality of coarse genus-one polynomials and 756 differences in corrected HKM ten-variable genus-two coefficients.
Enumerate all 7!=5040 vertex permutations, preserve edges and check degree sequence as safe prefilter. A graph automorphism group has order 2; B has order 4. Degree histograms A: degree 1:1,3:1,4:3,5:2; B: degree 2:2,3:3,4:1,5:1. For each automorphism p, count graph-code words w fixed under coordinate permutation. A fixed-word traces {64:1,128:1}; B {32:1,64:2,128:1}. Independently executed exact standard-library Python, PASS.

## Strong adversarial limitation
These are automorphism groups of *particular graph presentations*, NOT necessarily intrinsic automorphism groups of the corresponding stabilizer codes or Narain CFTs. Local complementation and other code/CFT equivalences can alter graph automorphism counts and degree sequences. The fixed-codeword permutation traces depend on the presentation and on identifying group elements. Therefore 2 vs 4 does not establish a new physical symmetry-resolved distinction, nor prove CFT inequivalence, nor provide a novel fourth-paper theorem.

## Research gate
P79 should test graph local-complementation equivalence classes, seek a presentation-independent symmetry invariant (e.g. full code automorphism group under the physically correct equivalence, not naive graph automorphism), and verify whether a physically transported symmetry trace is defined. If this fails, terminate this symmetry route. No manuscript writing.
