# P35 exhaustive small-graph falsification benchmark

Executed Python enumeration of every labelled undirected simple graph at n=2,3,4. Graph code C(B)={(a,Ba):a in F_2^n}. Genus-one refined enumerator counts I,Y,{X,Z}. Genus-two refined enumerator counts ten classes of Henriksson, Kakkar, McPeak JHEP 04 (2023) 011, Eq. (3.47), for all ordered pairs of codewords.

Exact outputs: n=2: 2 graphs, 2 distinct genus-one fingerprints, 2 genus-two fingerprints, 0 genus-one classes split by genus two. n=3: 8 graphs, 4 genus-one and 4 genus-two fingerprints, 0 split. n=4: 64 graphs, 9 genus-one and 9 genus-two fingerprints, 0 split. Integer Counter comparisons, no floating point.

This is an exhaustive result ONLY for labelled simple graphs with n=2..4. It does not establish n=7 as minimal: n=5,6 are open in this run. A sharper minimality theorem requires exhaustive n=5,6 or an analytical reduction with independently verified completeness. The published seven-node example is known prior art; any minimal-size claim requires prior-art audit. No new physical Fourier coefficient. Q1 manuscript NO-GO.
