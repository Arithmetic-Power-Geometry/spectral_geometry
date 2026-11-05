# Stage 05 — explicit general-composite local-to-global counting

Let N=∏p_i^{e_i}. Precisely define capped valuation cells c_i(a,b), T_i=Σ_{a+b≥e_i}c_i(a,b), D_i=Σ_b c_i(e_i,b), H_i=Σ_a c_i(a,e_i), I_i=c_i(e_i,e_i). Establish by CRT/inclusion-exclusion
K_N=∏T_i−∏D_i−∏H_i+∏I_i.
Do not claim this elementary identity is an original theorem of CRT.

**Substantive task:** obtain explicit valid local expressions for T_i,D_i,H_i,I_i for p_i>3 from the proved joint series and, if rigorously possible, for the exceptional primes 2,3 by separate valuation analyses. Verify whether all results are residue-ring counts and handle e_i=1 correctly.

Recover prime-power and square-free special cases algebraically. Independently compare direct original masking O_N, strict K_N, JD(N), JH(N), and the local CRT products for small mixed moduli with repeated prime factors (e.g. 45, 75, 175, 225, 245) and additional cases including 2,3 when feasible.

State an arithmetic-operation bound only with given factorization, prescribed roots and cost-model assumptions; do not claim efficient factoring of unknown N.

**Deliver:** `GENERAL_COMPOSITE_PROOF.md`, explicit formulas or a clearly marked limitation, and independent count tables. **Gate:** formulas reproduce all tested specializations and each proof is complete.
