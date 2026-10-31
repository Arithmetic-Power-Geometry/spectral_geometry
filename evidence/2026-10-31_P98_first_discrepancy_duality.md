# P98 — First unlabelled spectral discrepancy and duality inequivalence certificate
Date: 2026-10-31.

## Exact setup
G=[[2,1/3],[1/3,3]], B=bJ, J=[[0,1],[-1,0]], b=0,1/3,2/3.
E_b(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n, with integer m,n.
## Complete spectrum to E<=4
Gershgorin bounds eigenvalues G in [5/3,10/3], so E<=4 implies ||n||²<=12/5 and |n_i|<=1; ||m+Bn||²<=40/3, hence |m_i|<=sqrt(40/3)+2/3<5 for |b|<=2/3. Exhaustive integer [-5,5]^4 is therefore complete (larger than necessary). Exact Fraction script computes full multiplicities.
## First discrepancy
At E<2, b=0 and b=1/3 spectra coincide, with levels and multiplicities: 0 (1), 18/53 (2), 27/53 (2), 39/53 (2), 51/53 (2), 72/53 (2), 87/53 (2).
At E=2: b=0 has multiplicity 2, arising from (m1,m2,n1,n2)=(0,0,±1,0); b=1/3 has multiplicity 0. Thus E*=2 is an exact first unlabelled spectral discrepancy. Total states through T=4: 75 vs 73. b=1/3 and b=2/3 spectra agree to T=4.
## Duality implication
Narain CFT isomorphisms preserving the conformal Hamiltonian preserve the unlabelled energy spectrum and its multiplicities. A mismatch at E=2 proves b=0 and b=1/3 cannot be related by such a duality, regardless of any proposed modular transformation. This is a necessary-invariant obstruction, not a complete classification of O(2,2;Z). The energy formula normalization is the one consistently used in P90-P97; if another paper uses a factor 1/2, the threshold rescales correspondingly.
## Novelty and limitations
This is a specific exact certificate and an elementary finite-enumeration argument, not a new general inverse-spectral theorem. b=1/3 and b=2/3 equality is expected from B shifts and B sign energy symmetry and must not be claimed as a new isospectral phenomenon. Future P99 should target a genuinely new theorem about first distinguishing thresholds across non-diagonal families, with strong prior-art falsification, not just more isolated examples.
## Reproducibility
Script papers/PAPER-04/code/p98_first_spectral_discrepancy.py; executed independently in /mnt/data/p98.py with output first=2, multiplicities 2 vs 0, complete level list, counts 75,73,73.
