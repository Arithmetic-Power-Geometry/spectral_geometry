# Exact cubic-collision formulas: new research notes

Let D=x-y and H=x²+xy+y². All counts are over ordered residue pairs.

## 1. Arbitrary square-free moduli

Let N=∏_{i=1}^r p_i, r≥2, with distinct primes p_i>3. Write δ_i=1 if p_i≡1 (mod 3), and δ_i=0 otherwise. Local type 10 means p_i|D and p_i∤H, type 01 means p_i|H and p_i∤D, and type 11 means both. A residue pair is masked if every prime divides DH and the local type labels are not all identical.

Define R_N⊂{1,…,N}² as the masked ordered residue pairs, A_N=|R_N|, B_N(s)=Σ_{(a,b)∈R_N}(1_{a≤s}+1_{b≤s}), and C_N(s)=Σ_{(a,b)∈R_N}1_{a≤s}1_{b≤s}. If X=kN+s with 0≤s<N, then

M_N(X)=k²A_N+kB_N(s)+C_N(s)-E_N(X),

where E_N(X)=Σ_{∅≠S⊆[r]} (-1)^{|S|+1} floor(X/d_S)-floor(X/N), and d_S=∏_{i∈S}p_i.

**Proof.** Each a∈{1,…,N} occurs k+1_{a≤s} times in the window. Multiplication gives the first three terms. For the diagonal x=y, D=0, H=3x²; because N is square-free and coprime to 3, gcd(H,N)=gcd(x,N). Thus masked diagonals are multiples of at least one but not all p_i, counted by inclusion–exclusion as E_N(X).

For a∈{1,…,N}, write S(a)={i:p_i|a}. The masked partner count is m_∅=∏_i(1+2δ_i)-1-2^r∏_iδ_i; m_S=∏_{i∉S}(1+2δ_i) when ∅≠S≠[r]; and m_[r]=0. The count of a≤s with S(a)=S is F_S(s)=Σ_{T⊆[r]\S}(-1)^{|T|}floor(s/(d_Sd_T)). Then

B_N(s)=2Σ_{S⊆[r]}m_S F_S(s).

**Proof.** For p_i|a, local partner b must be 0 (type 11). For p_i∤a, b=a has type 10 and when δ_i=1 two other partners (nontrivial third roots) have type 01. An intermediate nonempty pattern S ensures differing types automatically. If S is empty, exclude all-10 and all-01 labels. If S=[r], all labels are 11. By symmetry, B_N counts first-coordinate partners twice. Inclusion–exclusion evaluates F_S.

The remaining coefficient C_N(s) is evaluated by CRT joining these local lists for a=1,…,s and retaining partners b≤s with nonconstant labels. For each a there are at most 3^r−2^r−1 masked candidates (maximized when every local prime is 1 mod 3), so at most s(3^r−2^r−1) CRT evaluations suffice, after supplying factorization and cube roots. For r=2 the bound is 4s. This is not a bit-complexity statement.

## 2. Strict prime-power masking for p>3

For e≥1, let K_p(e) count (x,y) modulo p^e satisfying p^e|DH, p^e∤D and p^e∤H. It is 0 for e≤2. Put δ=1 if p≡1 mod3, otherwise 0. For e≥3,

K_p(e)=Σ_{t=1}^{⌊(e−1)/2⌋} W_p(e,t).

Write n=e−t, m=e−2t and L=e−3t. If L≤0, set

W_p(e,t)=p^{2n}−p^{2n−2}−(p−1)p^{n−1}−2δ(p−1)p^{2n−m−1}.

If L>0, set

W_p(e,t)=(p−1)(p^{2n−L−1}−p^{n−1})+2δ(p−1)(p^{2n−L−1}−p^{2n−m−1}).

**Proof.** Both D and H are divisible by p in a strict masked pair. For p>3, this forces p|x,y. Let t=min(v_p(x),v_p(y))≥1 and write x=p^t u,y=p^t v, with primitive (u,v) modulo p^n. Then D=p^t(u−v), H=p^{2t}Q(u,v), Q=u²+uv+v². Properness of H gives 2t<e. The congruence demands v_p((u−v)Q)≥L, and both D and H must remain nonzero modulo p^e. On primitive pairs, u−v and Q cannot both vanish modulo p, since Q(v,v)=3v² and p>3. Thus the residue classes partition into D-vanishing, Q-vanishing and neither-vanishing branches. Each D-vanishing class has (p−1)p^{2n−h−1} lifts for valuation at least h≥1, and must exclude the (p−1)p^{n−1} pairs with u=v modulo p^n. Each of the 2δ Hensel-lifted Q roots has the same count, with h=m excluded. For L>0 use h=L in the appropriate branch. For L≤0 all primitive pairs qualify except those making D or H wholly divisible by p^e. The displayed formulas follow.

At e=3 this specializes to K_p(3)=p^4−2p²+p for p≡2 mod3, and p^4−2p³+p for p≡1 mod3.

For p≡2 mod3, the binary quadratic form Q is anisotropic modulo p, proving v_p(Q(x,y))=2min(v_p(x),v_p(y)) for nonzero x,y.

## 3. The exceptional prime p=3

Let K_3(e) be the same *strict* count. For each t, put n=e−t and L=max(1,e−3t−1). Then

K_3(e)=Σ_{1≤t≤⌊(e−1)/2⌋,3t≥e} 6·3^{2n−2}
      +Σ_{0≤t≤⌊(e−2)/2⌋,e>3t+1} 2(3^{2n−L−1}−3^{n−1}).

**Proof.** Let x=3^t u,y=3^t v, where (u,v) is primitive modulo 3^n. If u≠v modulo 3, Q is a unit; if u=v modulo 3, u and v are units and v_3(Q)=1. Thus in the first branch v_3(DH)=3t and 3t≥e, with t≥1 and 2t<e; the 6 primitive unequal-residue pairs modulo 3 each have 3^{2n−2} lifts. In the second branch let h=v_3(u−v)≥1; then v_3(DH)=3t+h+1. The constraints are h≥max(1,e−3t−1)=L, h<n, and 2t+1<e. The 2 nonzero equal-residue choices modulo 3 yield exactly 2(3^{2n−L−1}−3^{n−1}) lifts.

For p=3, strict masking already occurs for e=2.

## 4. Distinct definitions

The manuscript-style property is p^e|DH and (1<gcd(D,p^e)<p^e **or** 1<gcd(H,p^e)<p^e). This is broader than strict masking, because exactly one factor may be fully divisible by p^e. Define full-D and full-H residual counts, J_D and J_H, then

O_p(e)=K_p(e)+J_D(p,e)+J_H(p,e).

The additional exact finite formulas and exhaustive numerical checks are implemented in verify_bridge.py. For p=5,e=3, K_p=580 but O_p=620. For p=3,e=2, K_3=12 but O_3=24. The definitions and counts must not be conflated.

## 5. Mixed-prime first occurrence

For N=35, (x,y)=(9,4) yields D=5 and H=133=7·19. Thus gcd(D,35)=5 and gcd(H,35)=7, while 35|DH. Exhaustion of smaller windows gives M_35(8)=0 and M_35(9)=2. Therefore the semiprime (2,2) mod3 first-occurrence law N+min(p,q) does not apply to mixed classes.

## Reproducibility and status

Run `python3 verify.py` and `python3 verify_bridge.py` in this folder. Tests compare formulas against exhaustive integer enumeration for the listed small moduli. These are mathematical research derivations with finite tests; they do not establish literature priority, nor have they been integrated into the original journal manuscript.
