# P67 — Rational modular orbit witnesses: first exact controls
Date: 2026-10-30.
Research scope: connected modular subgroup PSL(2,Z)_T x PSL(2,Z)_U with mirror exchange T<->U; this is NOT the entire O(2,2;Z) including CP-like components. No spectral reconstruction claim yet.

Primary references:
- https://d-nb.info/1233573373/34 (JHEP 2021 Narain modular transformations T and U, mirror and CP-like action).
- https://inspirehep.net/files/184f416ecb43d225c8911446f14edf25 (Narain generalized metric and explicit modular transformations).
- https://cds.cern.ch/record/298744/files/9603074.pdf (T-duality modular group and mirror exchange).

Implementation: rational pairs x+iy with Fraction x,y; fractional linear action (az+b)/(cz+d) exactly, determinant ad-bc=1; enumerate matrices with entries |a|,|b|,|c|,|d|<=B and optionally exchange T and U.
Exact controls PASS:
(2i,i)->(i/2,i) via S: [0,-1;1,0].
(2i,i)->(i,2i) via mirror swap.
(i,i)->(1+i,i) via modular translation.
No witness (i,i)->(2i,i) at B=2; explicitly NOT a proof of non-equivalence.
All checked exact, no floating point.

Proof gate: Need canonical fundamental-domain reduction with exact rational/quadratic arithmetic and boundary handling, then prove orbit classification for the chosen subgroup; include CP-like and other disconnected components only after stating exact equivalence notion. Need an independent direct Narain 4x4 generalized metric action check. No claim about full spectral data injectivity.
Novelty gate: classical modular reduction and orbit membership are known; these controls are baseline engineering, not a new theorem. Paper 4 NO-GO.
Next P68: implement exact upper-half-plane reduction, handle modular boundary ties and elliptic fixed points, cross-check with bounded witnesses; test spectral collisions across canonical orbit representatives before proposing novel certificate.
