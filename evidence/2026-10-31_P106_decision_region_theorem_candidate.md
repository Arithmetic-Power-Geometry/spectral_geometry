# P106 — Syndrome–coset decision-region theorem candidate and novelty gate
Date: 2026-10-31

## Independent computation
The P105 32-orientation exhaustive audit was rerun independently in the local container using Python standard-library exact Fraction arithmetic. All 32 five-qubit code variants share distance 3 and stabilizer weight enumerator (1,0,0,0,15,0); three distinct optimal recovery values under channel (I,X,Y,Z)=(90,1,1,8)/100. Minimum 91983723/100000000 at mask 0, maximum 2316216227/2500000000 at mask 28, exact spread 1038947/156250000 = 0.0066492608. Depolarizing recovery invariant at 155333/168750. This is a local-Clifford orbit, not a non-LC pair.

## Theorem candidate (valid elementary formulation, NOVELTY NOT ESTABLISHED)
For any n-qubit stabilizer code with ideal syndrome measurement and independent identically distributed Pauli noise p=(p_I,p_X,p_Y,p_Z), let E_(s,c) be the phase-free Pauli errors in syndrome s and logical coset c. Define M_(s,c)(p)=sum_(E in E_(s,c)) product_(i=1)^n p_(E_i). Then P_opt(p)=sum_s max_c M_(s,c)(p) is continuous and piecewise homogeneous polynomial of degree n in the four unconstrained channel variables. Each change in winning decoder choice occurs only on a polynomial equality locus M_(s,c)=M_(s,c'). For rational p, an exhaustive exact-arithmetic evaluation certifies P_opt and all maximizing choices.

## Proof
Every error probability is a monomial of degree n; finite sums over each fixed coset are homogeneous polynomials. The maximum of finitely many continuous functions is continuous; partition the probability simplex into finitely many weak-inequality regions specifying a maximizer for every syndrome. On each such region the formula is a fixed sum of polynomials. Region boundaries at which a maximizer changes are contained in pairwise polynomial equality loci. Rational input gives rational evaluations and exact comparisons. QED.

## IMPORTANT prior art / limitations
This statement follows directly from standard maximum-likelihood syndrome/coset decoding; it is not presently an original theorem. Rains (2000), Polynomial invariants of quantum codes, DOI 10.1109/18.817508; Cao, Gullans, Lackey, Wang (2024), Quantum Lego Expansion Pack: Enumerators from Tensor Networks, DOI 10.1103/PRXQuantum.5.030313, especially Sec. III G on enumerator-based decoders and exact logical rates. A novel contribution would require provably efficient decision-region certification, a new operationally discriminating invariant beyond existing enumerators, or a nontrivial separation from strongest existing methods, with matched non-LC code families. No such result demonstrated.

## Decision
Research GO; Paper 4 manuscript NO-GO. Do not label the candidate theorem novel or assert first discovery.
