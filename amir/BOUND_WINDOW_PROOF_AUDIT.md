# Stage 06 — bounded-window theorem and flow audit

**Status:** nine independent formula-versus-direct checks passed; five exhaustive candidate-bound scans passed. This does not establish originality or final submission readiness.

Let N be square-free with r≥2 distinct primes p_i>3. Define the labelled local candidate set T_p(a) **before** stating the window theorem:
- if p|a: {(11,0)};
- if p∤a and p≡2 mod3: {(10,a mod p)};
- if p∤a and p≡1 mod3: {(10,a),(01,ω_pa),(01,ω_p²a)} mod p.

For a tuple of local choices, use the CRT representative R∈{1,…,N}. Retain the tuple precisely when not all labels agree. This defines a set of masked residue pairs with no duplicate CRT representatives.

Write X=kN+s, 0≤s<N. Each residue a∈{1,…,N} appears k+1_{a≤s} times among 1,…,X. Summing the product of coordinate multiplicities over masked residue pairs gives k²A_N+kB_N(s)+C_N(s), where B_N(s)=2Σ_{a≤s}m_N(a) and C_N(s)=Σ_{a≤s}Σ_{retained choices}1_{R≤s}. The diagonal correction E_N(X) counts x≤X divisible by at least one but not all primes dividing N (since D=0, H=3x² and 3∤N). Thus M_N(X)=k²A_N+kB_N(s)+C_N(s)−E_N(X).

For a<N, m_N(a)=∏_{p_i∤a}(1+2δ_i)−1_{gcd(a,N)=1}[1+∏_i(2δ_i)]. The excluded uniform labels are all-10, all-01, or all-11; the latter is impossible for a<N.

**Candidate bound:** if no p_i divides a, at most 3^r−1−2^r retained choices occur, with equality when all δ_i=1. If at least one p_i divides a and a<N, at most 3^(r−1) choices occur; for r≥2, 3^(r−1)≤3^r−2^r−1. Hence C_N(s) uses at most s(3^r−2^r−1) CRT evaluations when factors and local roots are supplied. This is an arithmetic-operation count, not a bit-complexity or factorization claim.

## Independent verification
The test uses local labelled CRT enumeration for the formula, and separately enumerates all integer x,y with the original congruence and gcd predicates. Tested N=35,55,91,385,455,5005 at selected windows (nine cases), all exact matches. It exhaustively checked the candidate bound for every a∈{1,…,N−1} for prime sets (5,7), (7,13), (5,7,11), (5,7,13), (5,7,11,13); all passed. Source test script and results committed separately.

## Required manuscript edits (not yet performed)
1. Move T_p(a) definitions ahead of current Theorem 5.
2. Merge Sections 4 and 5 into a single bounded-window section, keeping the general square-free theorem followed by explicit semiprime specialization.
3. Keep the diagonal correction clearly separate from residue counts.
4. Preserve the special first-occurrence result and its restricted p,q≡2 mod3 hypotheses.
5. Ensure abstract and conclusion reflect the strongest verified result without suggesting factor-blind RSA factorization.

**Open:** no complete exhaustive audit of every possible square-free modulus or all manuscript proofs; no revision of the source TeX yet.
