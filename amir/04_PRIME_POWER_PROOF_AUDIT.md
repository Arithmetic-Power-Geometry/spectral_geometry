# Stage 04 — theorem-by-theorem prime-power proof audit

1. Check p>3 assumptions and explain why p=3 differs (repeated cyclotomic root), why p=2 belongs to the no-nontrivial-root case, and distinguish unit-root counts from all-pair counts.
2. Verify Theorem 10's exact conditions t=min(v_p(x),v_p(y)), m=e-t, h=e-2t, L=max(0,e-3t), 1≤t≤floor((e-1)/2), and every power of p in C_{p,e}(t).
3. Derive both L≥1 and L=0 branches from independent primitive-pair counting. Check 3t<e, 3t=e, 3t>e; t and e at extreme allowable values; e=2,3,4,5,6 and both p≡1,2 mod 3.
4. Derive K_p(e) a second way by extracting finite-valuation coefficients of F_p(U,V); prove equivalence to the finite sum, not merely a numerical match.
5. Run a direct brute-force checker with original modular divisibility predicates, and a mathematically distinct coefficient/formula checker. Include boundary-case unit tests, exact integer arithmetic and explicit stop/resource limits.
6. Audit every displayed closed example, including K_p(2)=0 and the two K_p(3) cases.

**Deliver:** `PRIME_POWER_PROOF_AUDIT.md`, scripts, test vectors, actual test logs. **Gate:** no proof gap or conflicting exact value; if found, amend theorem and downstream claims.
