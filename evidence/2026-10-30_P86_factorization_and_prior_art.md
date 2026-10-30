# P86 — Exact genus-two separating-factorization regression and prior-art collision
Date 2026-10-30.
Primary source: Henriksson, Kakkar & McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, eq (3.48) (genus-two y-variable factorization) and Section 4.4 (explicit genus-one-isospectral, genus-two-distinct n=7 code CFTs). Source: https://inspirehep.net/files/a4114600f231e0b863f9b88bc7333031

## Exact execution
Local Python script /mnt/data/p86_factorization.py executed successfully. Independent 128 codewords for each graph, 16384 ordered pairs, corrected ten-variable HKM quotient. Substitute y0=x0 x0', y1=x0 x1', y2=x1 x0', y3=x1 x1', y4=x0 x2', y5=x2 x0', y6=x2 x2', y7=x1 x2', y8=x2 x1', y9=x2 x2'. Both resulting integer coefficient polynomials exactly equal the product of the corresponding genus-one refined enumerators. A and B each 16 genus-one terms and 1251 genus-two terms. PASS.

## Key publication-novelty kill
HKM section 4.4 explicitly studies an n=7 pair with identical genus-one partition function but distinct genus-two enumerators, plus other n=8 pairs and triples. This is not a hypothetical closest precedent; it directly establishes the phenomenon we have been testing. Our A/B graph edge lists have not been independently matched by an explicit graph isomorphism/ELC witness to their eq (4.19) matrices, so do not assert exact identity of pair. Regardless, a claim merely reproducing n=7 genus-one isospectrality and genus-two distinction is already prior art.

## Limits
The exact polynomial factorization check is not the physical analytic genus-two nonzero certificate; no theta numerical evaluation with error bounds or modular covariance computation is claimed. The checked factorization is a necessary internal consistency condition, not a new physical theorem.

## Next step
P87: perform a strict original-pair identification against HKM eq (4.19), then either abandon graph-code distinction as fourth-paper novelty or define a genuinely stronger new question (e.g. minimal distinguishing observable with proven optimality and duality invariance). No manuscript until prior-art novelty gate passes.