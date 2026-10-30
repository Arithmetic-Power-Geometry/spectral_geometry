# P58 — Quantitative precision and publication feasibility

## Exact branch
For G=[[2,1/3],[1/3,3]], B=bJ, m=(0,0), n=(1,0), the labelled state energy is E(b)=2+(18/53)b². This is a labelled state branch; its observation is NOT automatically an experimentally accessible unlabelled spectral line.

## Precision theorem (bounded adversarial absolute error)
If a scalar observation reports y with |y-E(b)|<=delta and the candidate set is {b1,b2}, the two possibilities can be distinguished with certainty for all permitted errors iff |E(b1)-E(b2)|>2delta. Necessity: intervals overlap if <=2delta. Sufficiency: disjoint intervals. This is a classical elementary measurement-error bound, not a new theorem.

For b=0 vs 1/10, |ΔE|=9/2650 and delta<9/5300.
For b=1/10 vs 1/5, |ΔE|=27/2650 and delta<27/5300.
For b=-1/5 vs +1/5, ΔE=0: no finite precision resolves sign from this branch.
At b near zero, E(b)-E(0)=18b²/53; the error requirement scales quadratically in b. On |b|>=b_min>0, inverse local derivative db/dE=53/(36|b|). The sign ambiguity remains.

## What this does and does not show
Exact rational arithmetic verified in papers/PAPER-04/code/p58_resolution_complexity.py.
The quadratic conditioning is familiar inverse-problem theory; the result does not establish a novel Narain-specific complexity theorem. A labelled level is an idealized oracle; to claim physical observability requires isolating and tracking that level from an unlabelled partition function, with crossings and degeneracies addressed.
P56-P57 obstructions are also elementary countability/finite-range observations. Paper 4 should NOT be drafted as an original research article yet.

## Stronger next discovery question
Find a physically invariant, unlabelled observation family and prove a nontrivial sharp cost-vs-resolution lower bound plus matching algorithm, ideally with a duality-invariant obstruction or modularly constrained observable family not reducible to ordinary test-cover. First verify accessible literature on inverse spectral stability, Narain partition functions, and information-based complexity. If no novelty survives, terminate this fourth-paper direction or change the problem rather than force a manuscript.
