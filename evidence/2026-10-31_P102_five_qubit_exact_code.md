# P102-QEC — Verified logical code and single-error recovery
Date: 2026-10-31
## Research objective
Replace P100–P101 [[7,0]] graph states with a genuine encoded [[n,k,d]] code. Reproduce a strong established benchmark before attempting higher-order invariant operational predictions.
## Primary verified literature
Laflamme, R.; Miquel, C.; Paz, J. P.; Zurek, W. H. (1996). Perfect Quantum Error Correcting Code. Physical Review Letters 77, 198–201. DOI 10.1103/PhysRevLett.77.198. Publisher https://doi.org/10.1103/PhysRevLett.77.198
Independent generator confirmation: Experimental exploration of five-qubit quantum error-correcting code with superconducting qubits. National Science Review 9(1), 2022, DOI 10.1093/nsr/nwab011, eq (1), https://doi.org/10.1093/nsr/nwab011
## Executed exact script
papers/PAPER-04/code/p102_five_qubit_code_exact.py, Python 3, stdlib only; tested locally.
Four commuting generators XZZXI, IXZZX, XIXZZ, ZXIXZ.
Stabilizer size 16, normalizer size 64, 48 normalizer elements outside stabilizer, min nontrivial logical weight 3, hence [[5,1,3]].
Stabilizer support weight enumerator {0:1,4:15}.
Identity plus 15 single-qubit Pauli errors map bijectively onto 16 four-bit syndromes. All 16x16=256 error-pair differences obey the stabilizer error-correction criterion (nonzero syndrome or in stabilizer).
For independent per-qubit Pauli depolarizing error probability p, events of weight <=1 have probability (1-p)^5+5p(1-p)^4; at p=.01 result .9990198504. This is a guaranteed-correctable-event lower bound, not total logical success probability for any specific decoder.
## Formal justification
Binary Pauli representation (x,z) in GF(2)^10, symplectic commutation x·z'+z·x'=0. Four independent commuting generators give codespace dimension 2^(5-4)=2. The normalizer has 2^(2*5-4)=64 elements. Distance is min Pauli weight in N(S)\S =3 by exhaustive search of all 4^5=1024 phase-free Paulis. Distinct syndromes for identity and all 15 weight-one errors verify perfect single-error correction. This reproduces the established 1996 perfect code; not a novel theorem.
## Falsification and blockers
No higher-order invariant operational advantage was demonstrated. P101 original graph pair encodes k=0 and cannot be compared directly as two [[n,k,d]] logical codes. Decoder simulations and code-family matched comparisons still absent. Claim of publication-ready novel result: NO.
## Next P103
Build multiple independently sourced [[n,k,d]] code families; specify operational loss and noise; compare invariant features against distance, weight enumerator, and decoder baselines, including adversarial null controls. Require out-of-sample prediction or exact theorem before Paper 4 writing.
