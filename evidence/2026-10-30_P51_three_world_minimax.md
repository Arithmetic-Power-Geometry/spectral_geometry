# P51 exact three-world distinguishing experiment

Worlds: fixed G=[[2,1/3],[1/3,3]], b=-1/5,0,+1/5. Energy E=(27x²-6xy+18y²)/53+2n1²+(2/3)n1n2+3n2², x=m1+b n2,y=m2-b n1, spin s=m.n.

Exact rational enumeration of all charges in [-5,5]^4 with E<=3 gives 39,43,39 states respectively. This is exhaustive: E >= (3/20)||v||², so E<=3 implies ||v||²<=20, and every coordinate |v_i|<=4.

First differing joint energy-spin levels:
b=-1/5 vs 0: E=2, s=0 multiplicity 0 vs 2.
b=0 vs +1/5: E=2, s=0 multiplicity 2 vs 0.
b=-1/5 vs +1/5: E=3313/1325, spin +1 multiplicity 2 vs 0, spin -1 multiplicity 0 vs 2.

At E*=3313/1325 the complete (s=-1,s=0,s=+1) signatures are:
b=-1/5: (0,0,2); b=0: (0,0,0); b=+1/5: (2,0,0).
Thus ONE exact joint-energy/spin-level observation at E* distinguishes all three. In the admissible model where an experiment resolves the full spin multiplicity at one energy E<=T and cost is maximum accessible energy T, no T<E* suffices to distinguish the opposite-sign pair; T=E* suffices. Therefore exact minimax energy threshold is E*. If each individual spin multiplicity is charged as a separate measurement, one spin channel at E* does not distinguish all three, and cost optimum depends on that altered model.

This is an exact conditional three-candidate optimization, NOT a novel fourth-paper theorem; opposite-sign threshold already in Paper 2. Physical inequivalence modulo O(2,2;Z) of all three worlds is not independently established here. Finite charge model is mathematically exhaustive only up to E<=3. Computational script saved as /mnt/data/p51_three_world_minimax.py. Need physical duality audit and broader families for Paper 4 novelty.

Gate: exact arithmetic PASS; optimality under stated energy-cost model PASS; independent novelty NO-GO.
