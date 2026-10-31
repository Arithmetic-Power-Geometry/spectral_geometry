# P100-QEC — Exact graph-state stabilizer controls
Date: 2026-10-31
Status: exploratory mathematical and computational evidence; NOT a new-code claim.

## Reproducibility
Script: papers/PAPER-04/code/p100_qec_stabilizer_controls.py. Executed locally using CPython. Uses integer bitmasks and no external dependencies.
Three illustrative seven-vertex simple graphs, NOT the graph pair studied by Henriksson–Kakkar–McPeak: empty graph, path P7, cycle C7.

## Observed output
empty: rank 7, group size 128, k=0, enumerator {0:1,1:7,2:21,3:35,4:35,5:21,6:7,7:1}
path: rank 7, group size 128, k=0, enumerator {0:1,2:2,3:9,4:17,5:38,6:44,7:17}
cycle: rank 7, group size 128, k=0, enumerator {0:1,3:7,4:21,5:42,6:42,7:15}
All pass binary-symplectic commutation checks; generator rank 7; 128 enumerated elements each.

## Formal baseline
For a simple graph with n vertices and binary adjacency A, graph-state stabilizer generators are K_i = X_i product_{j:A_ij=1} Z_j. Binary symplectic representation generator (e_i,A_i) has independent X components, hence rank n. They commute because A is symmetric: symplectic product between i,j is A_ij+A_ji=0 over GF(2). Thus the common +1 eigenspace dimension is 2^(n-n)=1 and encodes k=0 logical qubits. For n=7, group size 2^7=128. These facts hold for arbitrary simple graphs, not just the tested controls. They do not imply a logical error-correcting code or establish a distance.

## Negative / unresolved
Original seven-vertex adjacency matrices have not been recovered from connected GitHub code search; DO NOT substitute illustrated control graphs for the published A/B matrices. No Knill–Laflamme tests, encoded-qubit code, decoder, or noise-channel benchmark has been performed. Higher-genus difference cannot be interpreted as a demonstrated quantum recovery benefit.
## Next P101
Retrieve and verify the exact published graph A/B matrices, provenance and graph equivalence; independently reconstruct their invariants. Then choose an explicit [[n,k,d]] code embedding, calculate normalizer minus stabilizer distances and enumerate correctable errors. Compare operational baselines.
