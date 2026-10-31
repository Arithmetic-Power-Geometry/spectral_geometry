# P105 — Exhaustive local-Hadamard orbit falsification
Date: 2026-10-31
Status: EXACT COMPUTATION PASSED; NEW THEOREM NOT ESTABLISHED.
## Executed procedure
CPython standard library fractions.Fraction, full 4^5 Pauli enumeration per code and channel, 32 subsets of Hadamard gates on physical qubits. Exact syndrome and stabilizer coset ML success; no Monte Carlo.
Base generators: XZZXI, IXZZX, XIXZZ, ZXIXZ. Apply H at subset of five sites, exchanging X and Z and retaining Y up to phase. All variants have [[5,1,3]] and stabilizer weight enumerator (1,0,0,0,15,0).
Biased independent noise I=9/10,X=1/100,Y=1/100,Z=8/100: three distinct optimal success probabilities among 32 variants. Minimum 91983723/100000000 at mask 0. Maximum 2316216227/2500000000 at mask 28. Difference exactly 2316216227/2500000000 - 91983723/100000000 = 0.0066492608 (0.66492608 percentage points). Original P104 mask 1 has success 460218397/500000000, difference from mask 0 = 149891/250000000.
Independent depolarizing p=1/10, I=9/10 and X=Y=Z=1/30: all 32 have identical optimal success 155333/168750.
## Mathematical explanation
Any local Clifford U permutes single-qubit Paulis and maps stabilizer group S to USU†. The syndrome/coset probability sums are preserved under the conjugated channel U† N U. If a channel is invariant under the local Clifford permutation (depolarizing), the optimal logical success is unchanged. For fixed biased Pauli channels the same conjugation need not preserve error probabilities, so different orientations can have different success. This is a channel-orientation effect, not a new higher-genus code invariant.
## Hostile prior-art check
Rains, Polynomial invariants of quantum codes, IEEE Trans. Inf. Theory 46(1), 54–59 (2000), DOI 10.1109/18.817508; verified via CaltechAUTHORS https://authors.library.caltech.edu/records/v0a29-75k22.
Cao, Gullans, Lackey, Wang, Quantum Lego Expansion Pack: Enumerators from Tensor Networks, PRX Quantum 5, 030313 (2024), DOI 10.1103/PRXQuantum.5.030313; verified via NIST https://www.nist.gov/publications/quantum-lego-expansion-pack-enumerators-tensor-networks. Their framework includes optimal decoding for i.i.d. noise.
## Verdict
P105 baseline exact, independent reexecution; NOT a novel higher-order-invariant effect. No evidence of non-LC-equivalent matched code pair or out-of-sample improvement over prior-art enumerator decoders. Manuscript NO-GO; proceed to P106 with non-LC-equivalent codes, complete enumerator matching, explicit theorem target and null controls.
