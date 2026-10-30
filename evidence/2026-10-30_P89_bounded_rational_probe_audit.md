# P89 — Exhaustive bounded rational Narain slice probe search
Date: 2026-10-30
Objective: test if bounded-height rational backgrounds admit nontrivial minimum coordinate-labelled observation budgets, before asserting physical inverse-spectral novelty.
Exact parameter set: diagonal G=diag(a,c), a,c in {1,2,3}; B=bJ, b in {0,1/3,2/3}; 27 distinct coordinate presentations. Energy E=(m+Bn)^T G^{-1}(m+Bn)+n^TGn. Eight charge-labelled probes listed in executable code. Python Fraction arithmetic and exhaustive subset combinations.
Executed script output:
backgrounds 27 probes 8
k 1 injective_subsets 1 example (5,)
minimum 1 witness (5,)
full signature classes 27
Probe index 5 is m=(0,1), n=(1,0). Its energy is b-dependent and accidentally injective on this finite grid. A zero-probe observation is constant, hence minimum 1 for this grid and this allowed probe set.
CAVEATS: no physical O(2,2;Z) duality canonicalization, no unlabelled CFT spectrum, no robustness under grid enlargement or perturbation, no general bound. A single exact rational number can encode many discrete parameter choices, so finite-grid minimality is not a deep new result. Do not describe distinct coordinate tuples as physically inequivalent.
Research decision: original P89 finite grid is too easy and not publication-worthy. P90 should replace with duality-invariant, precision-limited observation budget and height-uniform theorem or explicit obstruction; strong prior-art kill tests required.
