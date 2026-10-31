# P99 — Novelty and manuscript-readiness gate
Date: 2026-10-31
## Current strongest findings
P87 independently identifies seven-vertex graph-code pair with Henriksson–Kakkar–McPeak 2023 eq. 4.19: cannot claim new genus-two distinguishing pair.
P90–P92 B-sign symmetry and duality/parity scope: not a novel counterexample.
P93–P96 finite-precision ambiguity and rational height exponent 2: elementary continuity/Farey bounds; rectangular slice E_min=1/c reconstructs trivially.
P97–P98 off-diagonal G=[[2,1/3],[1/3,3]], B=bJ: exact E*=2 for b=0 vs b=1/3, multiplicity 2 vs 0. Proves inequivalence, but isolated certificate, not new general theorem.
## Prior art independently checked on 2026-10-31
Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, https://doi.org/10.1007/JHEP04(2023)011: isospectral genus-one CFTs distinguished at genus two.
Furuta, Relation between spectra of Narain CFTs and properties of associated boolean functions, JHEP 09 (2022) 146, https://doi.org/10.1007/JHEP09(2022)146: Narain code spectra and Boolean EPC distance.
These are verified constraints, not exhaustive novelty clearance for precision/cutoff theorems.
## P99 mathematical step: winding-blind lower bound
Let G be any positive-definite dxd metric and E_B(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n. For every nonzero integer n, n^T G n >= lambda_min(G) ||n||² >= lambda_min(G). Therefore every state with E<lambda_min(G) has n=0 and E=m^T G^-1 m independent of B. Hence for fixed G, any two B fields have exactly identical unlabelled spectra strictly below lambda_min(G), including multiplicities. If T<lambda_min(G), spectra through T coincide. At T=lambda_min(G), boundary may contain winding states and equality is not assured. This is an elementary but general theorem, not a new research-level contribution.
For G=[[2,1/3],[1/3,3]], lambda_min(G)=(5-sqrt(13)/3)/2=(15-sqrt(13))/6 approx 1.89907, so the P97 T=1 agreement is forced by winding blindness. E*=2 in P98 lies above this bound. This lower bound is not generally sharp and cannot be promoted to a novel result.
## P100 next
Seek a parameterized first-distinguishing threshold that exceeds the elementary winding threshold, with exact proof of optimality and nontrivial dependence on B and G. Search prior work on theta series of lattices, isospectral flat tori, and shortest vector variation before claiming novelty.
## Gate
NO-GO full manuscript. P100–P102 are research checkpoints only, not guaranteed publication dates. Manuscript drafting only after theorem, proof, independent reproducibility, and hostile prior-art audit.
