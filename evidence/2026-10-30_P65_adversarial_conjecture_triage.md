# P65 — Adversarial conjecture triage and executed exact tests

Research question: For Narain/code-CFT observables, can one characterize the minimal additional spectral information needed to distinguish physically inequivalent theories, beyond known genus-one versus genus-two examples?

## Three competing conjectures and gates
C1 (strong universal lift): Equality of coarse genus-one graph-code enumerators forces equality of HKM ten-variable genus-two enumerators. **FALSE**: published seven-vertex Dymarsky–Shapere pair; exact P65 program independently reruns 128 words/graph, 16,384 ordered word pairs and finds identical coarse polynomials but 756 differing corrected HKM coefficients. This is known prior art, not a new theorem.

C2 (generic finite evaluation as novel finite determinacy): Every bounded-degree ten-variable enumerator can be recovered from finitely many algebraic evaluation values. **TRUE in a trivial classical sense and not novel**: Kronecker substitution with weights (n+1)^i encodes exponent vectors injectively for degree n; coefficients may be read by sufficiently large-base substitution. Exact program checks distinct encodings for all nonzero monomials of both degree-7 polynomials. Crucial distinction: algebraically free variable evaluation is NOT the constrained theta-function evaluation at physically admissible period matrices. No physical conclusion follows.

C3 (potential open direction): Construct an infinite family of oriented inequivalent Narain/code CFTs for which the least genus or symmetry refinement required for a physically normalized distinguishing partition function grows or admits a sharp structural characterization. **UNPROVED AND NOVELTY UNKNOWN**. Need define admissible physical families, prove genus-one and all lower-genus equalities and higher-genus inequality, and exclude prior art. A single seven-vertex pair does not suffice.

## Reproducibility
Code papers/PAPER-04/code/p65_adversarial_gates.py is self-contained standard-library Python; locally executed PASS. No physically normalized theta calculation has been run. Known reference: Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011; Dymarsky and Shapere prior seven-vertex example (verify full bibliographic metadata before formal citation).

## Recommendation
Do NOT write fourth paper based on C1 or C2. C3 is a high-risk conjecture; test its plausibility and prior art with explicit graph-code families before proceeding. In parallel evaluate arithmetic finite determinacy under bounded-height rational Narain backgrounds as alternative. Do not conflate polynomial differences, analytic theta nonvanishing, or CFT inequivalence.
