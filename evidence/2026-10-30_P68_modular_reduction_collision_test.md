# P68 exact modular reduction and rectangular spectrum controls
Date: 2026-10-30.
Code locally executed: /mnt/data/p68.py, Python fractions only.
Canonical upper-half-plane reduction uses translations to Re z in [-1/2,1/2), inversion when |z|<1 or |z|=1 with Re z<0; sorted T,U pair handles mirror exchange.
30 rational upper-half-plane points and all 52 SL2Z matrices with entries -2..2 tested: 1560 exact invariance checks passed. Boundary controls i, 1+i, 2i, i/2 passed.
Rectangular T=iA,U=ir (A,r in {1,2,3,3/2}), 16 backgrounds. Exact E=m1²/(A/r)+m2²/(Ar)+(A/r)n1²+(Ar)n2², spin=m1n1+m2n2; charge components each -2..2. No identical bounded-box energy-spin Counters across different canonical representatives.
CAVEATS: The box truncation is not duality invariant, so its Counter is not a genuine invariant of orbit. Also the canonical reduction is a standard classical modular reduction and does not establish any new theorem. The no-collision finding is limited to these 16 backgrounds and this box. The group tested is SL2(T)xSL2(U) plus exchange; full O(2,2;Z) components are not classified. Novelty gate NO-GO.
Next P69: define duality-invariant energy/spin cutoffs, enumerate all charge vectors below exact energy threshold using rigorous finite bounds, and test orbit collisions. Prior art check needed before theorem claims.
