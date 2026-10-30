# P36 exhaustive sharp threshold for refined enumerator separation

Executed exact Python enumeration of NetworkX graph_atlas_g representatives of every simple unlabeled graph at n=5 (34 representatives) and n=6 (156 representatives). Construct C(B)={(a,Ba)} for every binary a and computed genus-one refined and genus-two ten-variable Eq. (3.47) polynomial fingerprints using integer counters.

Results: n=5, 34 graphs, 21 distinct genus-one fingerprints, 21 distinct genus-two fingerprints, zero genus-one classes split by genus two. n=6, 156 graphs, 64 distinct genus-one fingerprints, 64 genus-two fingerprints, zero split. Previous P35 n=2,3,4 exhaustive labelled enumeration also yielded zero splits. Since simultaneous vertex relabelling permutes coordinate positions but leaves enumerator monomials invariant, the graph-atlas representatives cover all labelled simple graphs up to isomorphism.

The seven-vertex example in Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, Eq. (4.19), has identical genus-one refined enumerators and different genus-two refined enumerators (reproduced P19-P24). Therefore the minimal number of vertices for a genus-one-equal/genus-two-refined-unequal pair of simple graph codes is exactly seven. This statement is about these refined polynomials, not the first Fourier coefficient of normalized physical partition functions.

Methodological limitations: relies on NetworkX graph atlas correctness/completeness; an independent graph-generation implementation and published prior-art novelty audit remain desirable. The seven-vertex example is known prior art; sharp minimality may also be known. No novelty claim or Q1 manuscript GO.
