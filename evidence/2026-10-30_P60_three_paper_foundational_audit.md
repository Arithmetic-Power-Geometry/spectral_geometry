# P60 three-paper audit — verified genus-two quotient discrepancy

## Inspected
Paper 1: Finite Spectral Reconstruction and Robust Non-Identifiability in Two-Dimensional Narain Compactifications, 13 pp, sections 1-4 and 6-9.
Paper 2: The First Spin-Resolved Spectral Discrepancy in a Narain Two-Torus Family, 13 pp, sections 1-8.
Paper 3: Exact Certificates and Falsification Controls for Narain Spectra, Graph Codes, and Integral Lattice Splitting, 18 pp, sections 1-4. This is a targeted review, not full verification of every equation and code artifact.

## High-priority discrepancy
Paper 3 section 2.4 page 4 explicitly states that the ten variables U_ab identify (a,b) and (b,a), the exchange of two copies. Earlier P24-P43 computational ten-variable convention instead identified 16 ordered pairs under simultaneous local X/Z exchange (1<->2; 0 and 3 fixed). These are different equivalence relations despite both producing 10 orbits. Exact script papers/PAPER-04/code/p60_genus_two_convention_audit.py verifies:
- copy exchange orbit of (0,1) is {(0,1),(1,0)};
- X/Z exchange orbit of (0,1) is {(0,1),(0,2)};
- two partitions differ, both have 10 classes.
HKM 2023 section 3.2.3 eqs (3.37)-(3.46) identifies variables x[1X]=x[1Z] and x[X1]=x[Z1] separately, consistent with local X/Z identification, not blanket exchange of copies. SOURCE: Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, primary https://scoap3-prod-backend.s3.cern.ch/media/files/76861/10.1007/JHEP04%282023%29011_a.pdf.

## Immediate impact
Paper 3's statement 'ten exchange classes specified in HKM' is unsupported as written. Its ten-variable polynomial and any P24-P43 ranks/kernels must not be equated with the HKM physical genus-two theta variables until an explicit linear/substitution map is derived and verified. Do not infer a physical genus-two distinction from an arbitrary ten-variable polynomial mismatch. The ordered sixteen-variable separating factorization can remain valid independently, as an algebraic identity, if its code enumerator definition is correct.

## Other audit points
Paper 1: labelled five-probe inversion distinct from unlabelled inverse; no universal finite cutoff already proven. Paper 2: first threshold b-vs-minus-b already established, so not new Paper 4 result. Paper 3: genus-two Gaussian expression explicitly disclaims physical normalization; any claim about full CFT must respect that limitation. Manuscripts explicitly treat orientation-reversal differently from O(2,2;Z).

## Gate and next actions
P60 PARTIAL PASS: quotient inconsistency proven and independently executable; complete manuscript and code provenance audit still outstanding. Prioritize correcting Paper 3 convention and regenerating all affected genus-two outputs under HKM's actual theta map. Then re-evaluate Direction A information-lift novelty. Do not write Paper 4 before this correction and hostile prior-art audit.