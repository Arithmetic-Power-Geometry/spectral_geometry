# Stage 04 — independent prime-power proof audit (2026-11-05)

**Status: PASS for the p>3 finite-sum theorem and its coefficient-level counterpart, subject to full independent peer review.** This is a mathematical verification report, not journal submission certification.

## Argument and boundary cases

Let e≥2 and p>3. For strict masking p^e|DH, p^e∤D and p^e∤H, both v_p(D),v_p(H)>0. By the common-divisibility lemma, p|x,y. Write t=min(v_p(x),v_p(y)), x=p^tu, y=p^tv, m=e−t, with (u,v) primitive modulo p^m. Then v_p(D)=t+a and v_p(H)=2t+b, where a=v_p(u−v), b=v_p(u²+uv+v²). At most one of a,b can be positive.

The strict inequalities are 3t+a+b≥e, a<m, b<h=e−2t. Therefore 1≤t≤floor((e−1)/2). Define L=max(0,e−3t) and φ_m=(p−1)p^(m−1).

For L>0, the product requires a≥L or b≥L. Counting primitive u,v modulo p^m gives the D branch φ_m[p^(m−L)−1], and the H branch 2δφ_m[p^(m−L)−p^(m−h)]. The branches are disjoint. For L=0, the product condition is automatic; subtract the disjoint forbidden a≥m and b≥h branches from all p^(2m)−p^(2m−2) primitive pairs. Thus
C_{p,e}(t)=
  φ_m[p^(m−L)−1+2δ(p^(m−L)−p^(m−h))], if L>0;
  p^(2m)−p^(2m−2)−φ_m−2δφ_m p^(m−h), if L=0.
K_p(e)=Σ_{t=1}^{floor((e−1)/2)}C_{p,e}(t).

**Boundary checks:** e=2 has empty t range and K_p(2)=0. At 3t=e, L=0; 3t>e also L=0. At 2t≥e the H strict bound fails, so t is excluded. e=3 has t=1 and gives K_p(3)=p^4−2p²+p for p≡2 mod3, or p^4−2p³+p for p≡1 mod3. The finite sum and coefficient extraction agree across all tested cases.

## Actual tests executed

A fresh local script `stage04_check.py` used:
1. independent integer finite-sum evaluation;
2. exact rational coefficient aggregation from the primitive branches of F_p(U,V);
3. direct modular evaluation of (x−y)(x²+xy+y²) and both strict exclusions, iterating x,y divisible by p (a necessary condition proved above).

Tested p=5,7,11,13 and e=2..7: **24/24 formula–series checks PASS**. Direct enumeration was run when (p^(e−1))²≤350000: **10/10 PASS**. Larger direct enumerations were explicitly skipped, not counted as passes. Exact values are in `STAGE04_RESULTS.csv`. Local SHA-256 of the executed script: `ea90c68ac2dee7c07c55ed9b03310688eae2773155a440b84b3e7356cf586f7c`.

## Scope and unresolved matters

This proves the stated p>3 branch decomposition but **does not prove corresponding exceptional-prime formulas for p=2,3**, nor the new univariate K_p(T) generating function. No source manuscript changes were made in this stage. The overall 96+/100 quality goal and *Integers* journal eligibility remain unresolved.
