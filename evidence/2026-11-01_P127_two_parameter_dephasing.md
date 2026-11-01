# P127 — coupled two-parameter dephasing stress test (2026-11-01)

## Model
Same five-qubit stabilizer generators as main (65).pdf; ideal independent I/Z noise. Sites 1–2 have error probability t; sites 3–5 have probability u. The parameters may be coupled by a calibration constraint such as u=2t, 0<=t<=1/2. This is parameter coupling, NOT correlated physical-site errors.

## Exact executable result
The attached script enumerates all 32 supported I/Z strings, 16 syndromes, and two supported cosets per syndrome using exact SymPy arithmetic. At nominal t=u=1/10, the 16 selected winner-versus-rival polynomials have **6 distinct exact expressions** in (t,u), versus **3** when restricted to u=t. This is a concrete loss of gap-expression compression when noise heterogeneity is introduced, NOT an improvement over prior methods.

For syndrome 1111, nominal winner canonical key 3 and rival key 28, the gap is:
g(t,u)=-2t²u³+3t²u²-3t²u+t²+2tu³-u³.
At (t,u)=(1/10,1/10), g=81/12500>0. At (1/10,1/5), g=-17/12500<0. Thus the nominal decoder is not ML-optimal over the coupled line u=2t. This is a *verified decoder-switching counterexample*, not a general theorem and not evidence of new method novelty.

## Scope and next gate
The calculation is a mathematical exact-arithmetic test, not a matched Molavi/Cao benchmark. It does not prove a general symmetry reduction or certificate-size advantage. Further work must characterize the switching boundary and verify novelty against prior work. No changes to manuscript claims until externally and independently checked.

## Reproduction
Run `python p127_two_parameter_dephasing.py` with SymPy installed. Expected first output line: PASS 16 syndromes; 6 two-parameter gap expressions vs 3 shared; syndrome 1111 decoder switch.
