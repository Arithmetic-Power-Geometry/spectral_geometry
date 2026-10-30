# P13 exact d=3 falsification (2026-10-30)

G=[[2,1/4,0],[1/4,2,1/4],[0,1/4,2]], B12=1/5, B23=1/7, B13=0. All energies evaluated with exact rational arithmetic. For H=2, fingerprint has 10 distinct energies and 27 states. For H=4, fingerprint has 104 energies and 281 states. Under B->-B, unlabelled fingerprints coincide exactly at both cutoffs (charge bijection (m,n)->(-m,n)). Replacing B with zero changes fingerprint, first discrepancy at energy 2.

Completeness: Gershgorin bounds eigenvalues G in [3/2,5/2]. Antisymmetric B has spectral norm <= max row absolute sum=12/35<2/5. Thus for H<=4, ||n||<=sqrt(8/3)<2 and ||m||<=sqrt(10)+(2/5)sqrt(8/3)<4, so integer search over n_i=-2..2 and m_i=-4..4 is exhaustive. The implemented box is conservative.

Limits: off-diagonal G is NOT certified intrinsically nonproduct under integral or O(3,3;Z) equivalence; this is a coupled chosen-basis example only. Parity equality is known, not new. The B=0 comparison is a finite-cutoff distinction, not a proof of inequivalence. No full O(3,3;Z) orbit classification, no generic rigidity theorem and no breakthrough.
