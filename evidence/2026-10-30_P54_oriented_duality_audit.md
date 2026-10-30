# P54 oriented Narain duality audit — exact proof and test

## Main mathematical correction
For charge vector (m,n), energy E_{G,B}(m,n) and spin s=m·n, ordinary Narain T-duality O(2,2;Z) preserves the indefinite integral bilinear and the physical left/right energy data. Thus any two dual backgrounds have identical joint (E,s) multiplicities. At fixed G=[[2,1/3],[1/3,3]], B=bJ, b=+1/5 vs -1/5 have different joint multiplicity at E=3313/1325, s=-1 (2 vs 0). Contrapositive proves they are not O(2,2;Z) equivalent as oriented CFTs. The result is a direct corollary of known Narain duality and the already-established Paper 2 spectral discrepancy; it is NOT an independently novel Paper 4 theorem.

## Parity qualification
Exact relabeling (m,n)->(-m,n) maps E_b to E_-b and s to -s. Hence their full partition functions are related by orientation reversal, Z_-b(tau,bar tau)=Z_b(-bar tau,-tau) in the conventional modular parameter expression (with normalization conventions adjusted). If parity is included as an equivalence, the pair is not distinguishable as distinct equivalence classes. Define equivalence before experiment optimization.

## Integer B shift
b -> b+1 is a Narain T-duality. For B=bJ, x=m+bJn; b+1 may be compensated by integer shift of m, preserving spin because n·Jn=0. Exact rational spectra b=1/5 and 6/5 match through E<=3.

## Executed exact verification
Script: papers/PAPER-04/code/p54_duality_audit.py. Charge box [-5,5]^4 exhaustive for E<=3 using E>=3/20 ||v||² for |b|<=1/2; b=6/5 comparison is via exact integer B-shift relabeling, and charge-box enumeration was checked through E<=3 with K=5. State counts b=+1/5 39, -1/5 39, b=0 43. Assertions pass.

## Literature
Angelantonj, Florakis and Pioline, A new look at one-loop integrals in string theory, Commun Number Theory Phys 6 (2012), section 3 on O(d,d;Z) invariant lattice partition functions, source https://intlpress.com/site/pub/files/_fulltext/journals/cntp/2012/0006/0001/CNTP-2012-0006-0001-a004.pdf .
Narain moduli and spin: https://www.researchgate.net/publication/348682727_Free_partition_functions_and_an_averaged_holographic_duality (confirm primary bibliographic metadata before final citation).
Literature distinguishes orientation reversal from ordinary T-duality; see https://archive.ymsc.tsinghua.edu.cn/pacm_download/58/489-017-0211230.pdf .

## Gate
Exact oriented nonduality certificate PASS, but theorem uses existing invariant and Paper 2 witness. No new Paper 4 novelty. P55 should use multiple oriented nondual worlds and nontrivial cost models; prove actual cost-preserving symmetry compression or give impossibility results, not an unsupported polynomial-time claim.
