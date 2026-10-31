# P104 — Exact matched-code operational counterexample (2026-10-31)
## Status
Research finding, NOT a new higher-genus theorem or cryptographic claim. Independently executed in Python 3 with fractions.Fraction, no numerical approximation in core probabilities.
## Construction
A: standard five-qubit [[5,1,3]] code with generators XZZXI, IXZZX, XIXZZ, ZXIXZ.
B: conjugate A by a Hadamard gate on physical qubit 1 (zero-based index 0): interchange X and Z at that site; Y remains Y up to irrelevant phase.
This local Clifford transformation preserves n=5, k=1, d=3 and ordinary Pauli support weight enumerator 1+15 y^4.
## Channel
Independent identical Pauli probabilities at each qubit: P(I)=9/10, P(X)=1/100, P(Y)=1/100, P(Z)=8/100.
Ideal noiseless stabilizer syndrome and maximum likelihood over logical cosets. Exhaustive 4^5=1024 Pauli errors per code, aggregate exact rational probabilities by syndrome and stabilizer coset, sum maximal coset probability over syndromes.
## Exact result
A success 91983723/100000000 = 0.91983723.
B success 460218397/500000000 = 0.920436794.
B minus A = 149891/250000000 = 0.000599564 (0.0599564 percentage points).
Both code distances 3 and stabilizer enumerator {0:1,4:15}. Thus ordinary support weight enumerator together with n,k,d does not fix optimal recovery probability for a specified biased Pauli channel.
Under depolarizing p=0.1, both optimal successes 0.920491851851852 (floating benchmark); expected because local Clifford permutations preserve channel.
## Mathematical caveat / novelty kill
This is a controlled illustrative counterexample and established local-Clifford/noise-orientation phenomenon, not proof that a genus-two invariant adds predictive information. A and B are locally Clifford equivalent; they need not be operationally different if physical noise and recovery are transformed together. Established literature on complete weight distributions, higher-degree invariants, and optimal decoding already treats related questions. Do not claim original theorem or superior code design.
## Sources
Rains, Polynomial invariants of quantum codes, IEEE Transactions on Information Theory 46(1), 54-59 (2000), DOI 10.1109/18.817508.
Cao et al., Quantum Lego Expansion Pack: Enumerators from Tensor Networks, PRX Quantum 5, 030313 (2024), DOI 10.1103/PRXQuantum.5.030313.
## Next P105
Seek non-local-Clifford-equivalent matched codes with identical ordinary AND relevant complete enumerators, and test higher-order features under matched channels; run full prior-art theorem audit before any novelty claim.
