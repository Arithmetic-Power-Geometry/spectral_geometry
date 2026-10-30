# P50 observation-separation geometry: exact prototype and strict novelty gate

## Definition
For a finite candidate set X and observation f:X->Y_f, D(f)={unordered {x,y}:f(x)!=f(y)}. For observation family F, D(F)=union_f D(f). The unresolved equivalence relation is x~_F y iff f(x)=f(y) for every f in F.

## Proven identities
D(F union G)=D(F) union D(G) (direct definition).
F subset G implies D(F) subset D(G).
D(F)=all unordered pairs iff combined observation map x -> (f(x))_f is injective.
Minimum-cardinality observation family separating all X is a set-cover problem on the universe of unordered pairs, with subsets D(f). Consequently this construct is classical in substance: distinguishing/identifying test sets, feature selection, test cover and partition refinement. It is NOT yet a novel mathematical invariant.

## Executed reproducible toy test
Program /mnt/data/p50_observation_geometry.py (copy into repository separately).
X={A,B,C,D}. energy constant 0. spin_1 partitions AB|CD, spin_2 partitions AC|BD. Each spin observation separates 4 of 6 unordered pairs; jointly they separate all 6. Assertions PASS. These are abstract objects, not demonstrated Narain backgrounds.

## Critical correction to prospective novelty
The partition lattice and test-cover problem are established. In particular 'new separation geometry' is a proposed framing, not a mathematically new discovery. Claiming this alone as a new branch would be misleading.

## Next P51 gate
Replace abstract X with verified, physically nondual Narain backgrounds; construct actual spin-sensitive observables and certified energy/spin coefficients; compute distinguishing test covers, compare standard set cover, and search for an original structural theorem under Narain duality and modular invariance. If no theorem survives, NO-GO.
