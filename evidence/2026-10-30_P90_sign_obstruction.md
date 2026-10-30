# P90 — Fermat-style exact obstruction and cross-domain inverse-problem gate
Date: 2026-10-30

## Proof
For symmetric positive definite G and antisymmetric B, E_{G,B}(m,n)=(m+Bn)^T G^{-1}(m+Bn)+n^T G n. Under B -> -B and m -> -m, (-m+Bn)=-(m-Bn), so E_{G,-B}(m,n)=E_{G,B}(-m,n). The map m -> -m is a bijection on Z^d and preserves every symmetric box cutoff |m_i|,|n_i|<=K. Hence exact energy multisets agree for all cutoffs and in the full spectrum. Spin s=m.n reverses sign, so spin-resolved spectra may differ. This is an elementary previously known type of sign-symmetry and NOT claimed as a novel theorem.
## Exact independent computation
G=[[2,1/3],[1/3,3]], B=b[[0,1],[-1,0]], b=+/-1/3. Python Fraction exact arithmetic.
K=1: 81 charge tuples; unlabelled energy equality TRUE; joint energy-spin equality FALSE; 46 differing coefficient keys.
K=2: 625 tuples; TRUE/FALSE; 410 differing keys.
K=3: 2401 tuples; TRUE/FALSE; 1382 differing keys.
Code tests signed-spin reflection identity. These finite charge boxes are not invariant under arbitrary O(2,2;Z) duality; they serve as algebraic regression tests only.
## Critical physical issue
Do not identify (G,B) and (G,-B) as physically inequivalent merely because spin-resolved spectra differ. Parity, orientation reversal, and O(2,2;Z) dualities require explicit treatment. 'No precision distinguishes them by unlabelled energies' is a statement about a non-injective observation map, not about inequivalent physical CFTs.
## Novelty and prior art
Benjamin, Collier, Fitzpatrick, Maloney, Perlmutter, 'Harmonic analysis of 2d CFT partition functions', JHEP 09 (2021) 174, DOI 10.1007/JHEP09(2021)174: physical primary partition functions and O(d,d;Z) moduli, spectral observables. Yahagi, 'Narain CFTs and error-correcting codes on finite fields', JHEP 08 (2022) 058 DOI 10.1007/JHEP08(2022)058. P90 sign identity is a basic symmetry, not new.
## Next gate P91
Replace presentation-level sign-pair with an explicit O(2,2;Z)-inequivalent pair, independently prove inequivalence, then establish a finite-precision spectral separation lower bound for physically invariant observations. Search and eliminate parity-related pairs. If no such pair or nontrivial bound exists, STOP. No manuscript.
