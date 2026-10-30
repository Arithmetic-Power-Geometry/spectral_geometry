# P95 — Height-precision quantitative gate (exact arithmetic)
Date 2026-10-30
Family G=diag(2,c), B=0, reduced c=p/q in [3,4], positive p,q<=H.
## Rigorous statement (labelled observation only)
For distinct rationals p/q,p'/q' with bounded numerator and denominator H, |c-c'|=|pq'-p'q|/(qq')>=H^-2. Charge-labelled probe (m,n)=(0,(0,1)) yields E=c. Quantization to nearest multiple of step eta<=H^-2 separates distinct c, since equality of rounded bins implies |c-c'|<eta (strict for half-open nearest-bin convention). Hence one labelled probe at resolution H^-2 suffices. This does not imply a duality-invariant unlabelled spectrum can identify c.
## Optimal exponent witness
c_k=(3k+1)/k, c'_k=(3k+4)/(k+1), gap=1/[k(k+1)], H=3k+4, so gap=Theta(H^-2). Exact test k=3,7,15,31,63 passes, and the rounded probe separates at eta=H^-2.
## Energy stability lemma
For c,c' in [3,4], E_c=m1²/2+m2²/c+2n1²+c*n2². For a charge with E_c<=T,
|E_c'-E_c|=|c-c'|*|n2²-m2²/(cc')| <= |c-c'|*(n2²+m2²/(cc')) <= (2T/3)|c-c'|.
Proof: c*n2²<=T => n2²<=T/3; m2²/c<=T => m2²/(cc')<=T/c'<=T/3. The same estimate holds if E_c'<=T. This controls level motion, but quantization collisions also depend on bin-boundary margins and whether levels cross cutoff T. It is NOT a universal guarantee of rounded spectral equality.
## Exact tests
Executable /mnt/data/p95_height_precision.py tested all above with Fraction. Cutoffs T=2,4,8,12 have 19,83,325,703 complete states respectively; checked per-state Lipschitz bounds for all, PASS. Initial temporary test box [-5,5]^4 missed 6 states at T=12; corrected to rigorous energy-derived charge bounds before committing.
## Novelty
Rational height gap H^-2 is a standard elementary Diophantine/Farey separation, not a new theorem. The Lipschitz estimate is elementary. No duality-invariant optimal spectral reconstruction bound is proven; Paper 4 remains NO-GO. Next P96: seek optimal *unlabelled* spectral identification on a height-bounded, duality-reduced family; account for accidental degeneracies, exact cutoff, bin boundaries, and strong prior art.
