# P97 — Non-diagonal metric, nonzero B: exact low-energy comparison
Date: 2026-10-31
G=[[2,1/3],[1/3,3]], B=bJ, b in {0,1/3,2/3}. E=(m+Bn)^T G^-1(m+Bn)+n^T G n, J=[[0,1],[-1,0]].
## Rigorous finite enumeration
Gershgorin bounds lambda_min(G)>=5/3, lambda_max(G)<=10/3. E<=4 implies ||n||²<=12/5 (hence |n_i|<=1) and ||m+Bn||²<=40/3. With |b|<=2/3 and |n_i|<=1, |m_i|<=sqrt(40/3)+2/3<5. Therefore exhaustive [-5,5]^4 includes every state below T=4, no untested high-charge states.
## Exact findings
For T<=1 all three spectra agree: 9 states, energies 0 (1), 18/53 (2), 27/53 (2), 39/53 (2), 51/53 (2). This follows because n=0 for E<=1 (n!=0 implies E>=5/3). At T=4, state counts b=0:75; b=1/3:73; b=2/3:73. First exact spectral difference between b=0 and b=1/3 (also b=2/3) at energy E=2. b=1/3 and b=2/3 have identical unlabelled energy spectra through T=4. All calculations use exact Fraction.
## Equivalence and novelty gate
b=2/3 is congruent to -1/3 modulo integral B shift. Energy isospectrality between ±b follows charge relabeling m->-m (P90); hence agreement of 1/3 and 2/3 is expected for all energies, not new. This does NOT establish inequivalence of the ±b pair under full Narain duality. Low-energy B blindness is elementary. The E=2 first difference for b=0 versus b=1/3 is an exact example, not a new theorem. Do not write manuscript.
## Next P98
Use the full exact first-difference certificate and independently audit full O(2,2;Z) equivalence of b=0 vs 1/3. Seek a family-dependent lower bound on B-detection threshold that is not a tautological winding gap. Prior art before publication gate.
