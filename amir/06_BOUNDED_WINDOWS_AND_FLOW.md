# Stage 06 — consolidate bounded-window results and repair section flow

1. Define the local candidate list T_p(a), labels and CRT representative **before** the first theorem that uses them.
2. Merge overlapping existing Sections 4 and 5 into one coherent bounded-window progression: square-free general theorem; floor-function coefficient; semiprime simplification; short CRT coefficient; both-primes-2-mod-3 threshold.
3. Keep specialized semiprime results only when they simplify the general theorem or add insight. Shorten repetitive proofs to a precise specialization argument.
4. Independently prove M_N(kN+s)=k²A_N+kB_N(s)+C_N(s)−E_N(kN+s); distinguish diagonal-included residues from x≠y counts.
5. Verify for all r≥2 the proposed bound s(3^r−2^r−1) under its stated assumptions, including cases where some primes divide a.
6. Test exact B_N(s), C_N(s), E_N(X), M_N(X), periodic/quasipolynomial claims and the sharp threshold when p≡q≡2 mod3, using genuinely different algorithms.
7. Place limitations beside complexity claims: arithmetic operations, factored modulus supplied, local roots supplied, no RSA-breaking or factorization runtime claim.

**Deliver:** `FLOW_AND_CROSSREF_AUDIT.md`, revised theorem outline, symbolic and numerical checks. **Gate:** each term first defined before use, and proofs not duplicated.
