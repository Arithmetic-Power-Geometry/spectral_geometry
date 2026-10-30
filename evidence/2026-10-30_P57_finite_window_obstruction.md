# P57 finite-resolution observation obstruction

## Theorem
Fix positive definite G and a compact parameter interval I for B=bJ. For any finite set of fixed bounded energy windows [a_j,c_j] and spin indices s_j, the map b -> (N_b([a_j,c_j],s_j)) has finite range. Thus it is not injective on any nondegenerate I, and cannot distinguish all oriented Narain duality classes.

Proof: compactness of I, positivity of G, and invertibility of the Narain quadratic charge form yield a uniform positive coercivity constant alpha_I with E_b(m,n)>=alpha_I (||m||²+||n||²) for all b in I. Consequently all charge vectors appearing below max_j c_j lie in a common finite integer box. Each observed count is an integer between zero and the size of this box; the vector of finitely many counts takes finitely many values. O(2,2;Z) is countable, so each duality orbit is countable. A finite-range map on an uncountable interval must assign the same signature to uncountably many parameters, containing infinitely many nondual classes. QED.

Caveat: observations are unlabelled spectral window counts at fixed windows, not continuously valued observables, labelled state tracking, or arbitrary adaptive infinite protocols. Finite observation signatures may be locally constant away from the finite set of energy-window boundary crossings; this is a stronger piecewise-constant statement. The theorem is elementary and prior-art novelty NOT established.

## Exact experiment
Fixed G=[[2,1/3],[1/3,3]], b=0,1/10,1/5,-1/5. Exact rational enumeration for E<=3. Counts N_b([2,201/100],0) are respectively 2,2,0,0. Thus finite windows can distinguish some worlds while never identifying a full continuous family with finitely many fixed integer counts.

Labelled winding (m,n)=(0,(1,0)) energy is E=2+18b²/53. At b=0,1/10,1/5 the energies are 2,5309/2650,2668/1325. These are labelled-state examples, not a claim that the corresponding unlabelled spectral level is uniquely trackable.

Script papers/PAPER-04/code/p57_finite_window_audit.py executed PASS. For |b|<=1/5, E>=3/20||v||², so K=5 enumeration is exhaustive through E<=3.

## Publication gate
Theorem mathematically correct but too elementary to justify Paper 4 alone. A novel result would require sharp quantitative complexity/precision tradeoffs for physically valid Narain observations, an original structural algorithm, or a nontrivial family-level inverse theorem with proof and independent prior-art audit. P58 should be a publication-feasibility gate, not automatic manuscript drafting.
