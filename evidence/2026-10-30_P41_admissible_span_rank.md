# P41 graph-code span rank under separating factorization

Locally executed exact modular arithmetic over prime 1000000007 on NetworkX graph_atlas_g representatives of all unlabeled simple graphs n=2..6. For each graph, enumerated all binary graph-code words and ordered codeword pairs; constructed ten-variable refined genus-two polynomial W2 and separating image Phi(W2). Verified Phi(W2)=W1(x)W1(z) for every graph.

n=2: 2 graphs, rank(W2)=2, rank(Phi W2)=2, kernel on span=0.
n=3: 4 graphs, rank(W2)=4, rank(Phi W2)=4, kernel on span=0.
n=4: 11 graphs, rank(W2)=8, rank(Phi W2)=8, kernel on span=0.
n=5: 34 graphs, rank(W2)=14, rank(Phi W2)=13, kernel on span=1.
n=6: 156 graphs, rank(W2)=27, rank(Phi W2)=23, kernel on span=4.

Interpretation: a nonzero kernel on the LINEAR SPAN of admissible graph-code enumerators emerges at n=5. This does NOT imply any two individual physical code CFTs have the same genus-one partition function but different genus-two partition functions. P36 pairwise n<=6 result is consistent. These are modular ranks, not yet independently certified rational ranks; they supply lower bounds for rational ranks individually, not automatically the exact rational kernel dimension. Next: rational-rank verification and explicit integer relations. This experiment is not a novel physical theorem yet.

Executable local script: /mnt/data/p41_admissible_span.py. Source: Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011.