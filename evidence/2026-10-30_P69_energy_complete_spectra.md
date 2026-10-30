# P69 — Exact energy-complete spectral enumeration
Date: 2026-10-30
Scope: rectangular 2D Narain family G=diag(A/r,Ar), B=0; A,r positive rationals.
E=m1^2/(A/r)+m2^2/(Ar)+(A/r)n1^2+(Ar)n2^2, spin=m1*n1+m2*n2.
Let c=min(A/r,Ar,r/A,1/(Ar)). Since E >= c*sum of squared integer charge components, all E<=L charges lie in |m_i|,|n_i|<=floor(sqrt(L/c)). Exact Fraction arithmetic and integer square root give exhaustive enumeration. This proof is elementary, not novel.
Executed /mnt/data/p69_energy_cutoff.py: A,r in {1,3/2,2,3}, 16 models; L=2,4,6. All three cutoffs: 0 cross-orbit collisions, 0 same-orbit mismatches, maximum bounds R=4,6,7. Exact spin-refined Counter(E,spin).
Orbit labels use unordered pair {max(A,1/A),max(r,1/r)} appropriate for purely imaginary T=iA,U=ir under independent S inversions and mirror; full modular-orbit boundary details and disconnected O(2,2;Z) action not independently proved here.
Important: finite sample with no collisions cannot imply global injectivity. Need negative controls for low L and enlarged rational grids, compare energy-only vs spin-refined spectra, and check exact duality normalization before new theorem.
Next P70: exhaustive larger grids with varying cutoffs and counterexample-first search; calculate first separating energy, seek finite-window collisions, compare spin added value. Literature novelty audit. Publication NO-GO.
