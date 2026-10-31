# P103 — Exact maximum-likelihood logical-coset decoding audit
Date 2026-10-31. Executed CPython 3 locally, standard library only.
Model: independent depolarizing Pauli channel on each physical qubit: I probability 1-p, X/Y/Z probability p/3 each. Ideal noiseless syndrome extraction; decoder chooses maximum probability stabilizer coset conditional on each syndrome. Enumerate all 4^n physical Pauli strings and aggregate exact syndrome/coset masses. Thus success probability = sum_s max_{logical coset c} P(s,c). No Monte Carlo, no circuit noise.
Code definitions:
[[5,1,3]] generators XZZXI, IXZZX, XIXZZ, ZXIXZ
[[4,2,2]] generators XXXX, ZZZZ
[[3,1,1]] bit-flip repetition generators ZZI, IZZ (distance 1 under arbitrary Pauli noise).
At p=.01: success 0.999022044919, 0.970299111111, 0.980199111111 respectively.
At p=.05: success 0.977668148148, 0.857388888889, 0.904888888889 respectively.
At p=.10: success 0.920491851852, 0.729111111111, 0.819111111111 respectively.
Exact enumeration sizes 1024, 256, 64 physical Paulis per code. Verified n,k,d respectively (5,1,3),(4,2,2),(3,1,1). Numerical probabilities use Python floating-point aggregation, while group/normalizer/distance are exact binary arithmetic. Comparison is NOT matched for n, k, rate or distance. Therefore cannot infer any advantage from higher-order invariants.
## Prior-art novelty kill test
Rains (1998), Quantum Weight Enumerators, IEEE Trans. Inform. Theory 44(4), 1388-1394, DOI 10.1109/18.681316: quantum enumerator theory.
Rains (2000), Polynomial invariants of quantum codes, IEEE Trans. Inform. Theory: higher-degree polynomial invariants already established.
Cao, Gullans, Lackey, Wang (2024), Quantum Lego Expansion Pack: Enumerators from Tensor Networks, PRX Quantum 5, 030313, DOI 10.1103/PRXQuantum.5.030313: optimal decoding via enumerators for i.i.d. noise already established.
Ashikhmin, Barg, Knill, Litsyn (2000), Quantum Error Detection I, IEEE Trans. Inform. Theory 46(3), 778-788, DOI 10.1109/18.841162: operational detection linked to enumerators.
Therefore no claim that optimal coset decoding or higher-degree invariants are original.
## Next
P104 must construct MATCHED pairs of [[n,k,d]] codes with identical conventional enumerators but different operational decoder performance under precisely specified noise, and show whether proposed higher-order features predict the difference beyond known complete weight enumerators and established tensor-network methods. If not, record NO-GO.
