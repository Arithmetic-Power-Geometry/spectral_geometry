# P48 spin-odd logarithmic spectral-threshold estimator and novelty audit

## Candidate construct
D_b(t)=sum_{m,n in Z²} s(m,n)[exp(-tE_{G,b})-exp(-tE_{G,-b})], s=m.n. By parity D_b(t)=2 sum s exp(-tE_{G,b}). If D_b(t)=c0 exp(-E0 t)(1+r(t)) with c0 nonzero, next nonzero exponent at least E0+delta, define S_h(t)=h^-1 log|D_b(t)/D_b(t+h)|.

## Rigorous conditional convergence
Fix t0>0. Define C0=sum_{E>E0}|c_E/c0| exp(-t0(E-E0))<infinity, delta=min_{c_E !=0,E>E0}(E-E0)>0. Then |r(t)|<=C0 exp(-delta(t-t0))=eps(t). Whenever eps(t)<1, D(t),D(t+h) nonzero and
|S_h(t)-E0| <= [-log(1-eps(t))-log(1-eps(t+h))]/h.
Proof: factor out c0 exp(-E0 t), bound the remainder termwise and use |log|1+r||<=-log(1-|r|). Thus convergence is exponentially fast in t with gap delta. This is classical exponential-sum asymptotics in a new Narain notation, NOT established as novel.

## Exact finite benchmark
For G=[[2,1/3],[1/3,3]], b=1/5, enumerate n_i=-3..3, m_i=-7..7 and collect spin-odd signed coefficients. First terms: E0=3313/1325,c0=-4; E1=3373/1325,c1=+4; E2=3493/1325,c2=+4. First threshold E0 certified by paper 2 independently of this finite box. Delta=60/1325 among the finite observed terms; do not assert globally without a full-charge bound.
For h=2: t=10 S=2.303082853993314; t=20 S=2.455877637269692; t=40 S=2.4913341728863307; t=80 S=2.499188238548839; E0=2.500377358490566. The finite box produces a rapidly improving estimate but convergence is slow for a small gap and sign cancellation. It does not certify the full infinite sum.

## Novelty kill test
Log-ratio effective mass estimators for exponential spectral sums are classical in lattice field theory, e.g. Phys Rev D 107 (2023) 014504 and Phys Rev D 110 (2024) 074509. Prony exponential recovery is classical and accuracy bounds for close exponents appear in Katz, Diab, Batenkov, Applied and Computational Harmonic Analysis 73 (2024), 101687, DOI 10.1016/j.acha.2024.101687. Therefore S_h itself is NOT a new formula in substance. Specific Narain spin-odd application and certified tail/threshold bounds are candidate research directions but novelty unverified.

## Next gate
Construct computable uniform upper bound C0 from the Narain coercivity and spin growth; avoid catastrophic cancellation using interval arithmetic. Compare directly against first-level enumeration and Prony/GEVP; find a theorem that is not an effective-mass restatement. NO-GO for breakthrough claim.
