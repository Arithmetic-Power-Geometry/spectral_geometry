# P96 — Complete unlabelled low-energy reconstruction on rectangular rational slice
Date 2026-10-30.
## Exact statement and proof
For G=diag(2,c), B=0, c in [3,4], Narain energy E=m1²/2+m2²/c+2n1²+c*n2². The smallest nonzero term is 1/c, achieved precisely by (m1,m2,n1,n2)=(0,+/-1,0,0), since 1/c<=1/3<1/2 and all other nonzero primitive charge contributions are >=1/2. Thus the complete unlabelled spectrum truncated at T=1/2 recovers c=1/E_min with multiplicity 2. This is a family-specific elementary observation, not a general reconstruction theorem.
For c=p/q in lowest terms with 1<=p,q<=H, 1/c=q/p. Distinct values have gap >=1/H². A nearest-grid quantizer of step <1/H² distinguishes the first positive energies; a step equal to half the actual minimum gap also distinguishes them.
## Executed exact tests
Independent local script /mnt/data/p96.py with Fraction arithmetic, complete energy-derived charge enumeration, and assertions. H=12: 5 c values, min gap 1/77. H=24: 16 c values, min gap 1/437. H=48: 61 c values, min gap 1/2021. For each c, minimum positive E=1/c with multiplicity exactly two; all rounded minima at half minimum gap are unique. All PASS. Initial local isqrt(Fraction) implementation error fixed before successful execution.
## Physical and novelty limits
This is an unlabelled energy cutoff, which is invariant under energy-preserving duality. The family is a restricted rectangular slice with fixed first radius; uniqueness of c within the slice follows immediately from E_min. It does not classify all O(2,2;Z) equivalences outside the slice or recover a general (G,B). The exponent 2 is classical Farey/Diophantine separation, not novel. No claim of a new theorem suitable for a fourth paper.
## Next P97
Stop using this trivial slice. Construct a genuinely non-diagonal B!=0 bounded-height family with multiple low-lying level crossings; prove duality inequivalence, seek a nontrivial minimal invariant spectral cutoff and optimal precision. Run prior-art kill tests before any paper writing.
