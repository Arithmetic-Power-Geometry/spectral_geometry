# Stage 05 — explicit formulas for all prime powers and arbitrary composites

**Status: exact local formulas derived and tested; independent journal referee review pending.** This strengthens the existing Proposition 5 without pretending that CRT is new.

For a prime p and e≥1, define T_{p,e}=#\{(x,y) mod p^e : p^e | x³−y³\}, D_{p,e}=#\{p^e|x−y\}, H_{p,e}=#\{p^e|x²+xy+y²\}, I_{p,e}=#\{p^e|x−y and p^e|x²+xy+y²\}. Let φ(p^h)=(p−1)p^{h−1}.

Define primitive solution counts for h≥1:
- R_p(h)=φ(p^h)ρ_p(h), with ρ_p(h)=1 for p=2; ρ_3(1)=1 and ρ_3(h)=3 for h≥2; and ρ_p(h)=3 for p>3 with p≡1 mod3, otherwise 1.
- S_p(h)=0 for p=2; S_3(1)=2, S_3(h)=0 for h≥2; for p>3, S_p(h)=2φ(p^h) when p≡1 mod3 and 0 otherwise.

Here R counts primitive pairs satisfying x³≡y³ (mod p^h), and S counts primitive pairs satisfying H≡0 (mod p^h). For p=3, the 3-adic unit cube-root count is 3 at h≥2; this is not the same as the root count of the quadratic factor, which has no unit roots modulo 9.

Set a=ceil(e/3), b=ceil(e/2). Then the explicit formulas are

T_{p,e}=p^{2(e−a)}+Σ_{t=0}^{a−1}p^{4t}R_p(e−3t),

D_{p,e}=p^e,

H_{p,e}=p^{2(e−b)}+Σ_{t=0}^{b−1}p^{2t}S_p(e−2t),

I_{p,e}=p^{e−ceil(max(0,e−v_p(3))/2)}, where v_p(3)=1 for p=3 and 0 otherwise.

**Proof.** For T, partition pairs by t=min(v_p(x),v_p(y)). If t≥a, x³−y³ is automatically divisible by p^e, giving p^{2(e−a)} pairs. Otherwise, write x=p^tu, y=p^tv with primitive u,v modulo p^{e−t}. The remaining congruence is u³≡v³ mod p^{e−3t}; each primitive solution modulo p^{e−3t} has p^{4t} lifts to the two coordinates modulo p^{e−t}. This proves T. For H, the same partition at b=ceil(e/2) leaves H(u,v)≡0 mod p^{e−2t}, with p^{2t} lifts per primitive solution, proving H. D is the diagonal count. On D=0, H=3x²; hence the simultaneous condition is p^e|3x², giving I.

The primitive root counts follow from the cyclicity of (Z/p^hZ)^× for odd p, the fact that cubing is an automorphism of (Z/2^hZ)^×, and Hensel lifting of the two distinct roots of z²+z+1 when p≡1 mod3. For p=3, H has exactly two primitive roots modulo 3 as a pair equation (u=v nonzero), and none modulo 9. For primitive cube collisions both coordinates must be units; for p=3 the kernel of cubing on units has size 1 at h=1 and size 3 for h≥2.

For N=∏p_i^{e_i}, CRT and inclusion–exclusion give the **explicit computable formula**

K_N=∏T_{p_i,e_i}−∏D_{p_i,e_i}−∏H_{p_i,e_i}+∏I_{p_i,e_i}.

The formula requires the prime-power factorization as input; it does not factor N or imply a sublinear factorization algorithm.

**Tests:** `verify_stage05.py` independently computes all four local quantities by direct modular enumeration for p^e≤300, then checks strict K_N by direct pair enumeration on a collection of mixed and repeated-prime moduli. See `STAGE05_RESULTS.csv`. The derivation above is a candidate manuscript addition **subject to author-led independent review and journal eligibility**.

**Status of originality:** the decomposition, cyclic unit groups, and CRT are classical. Whether this packaged closed formula for the particular masking statistic is previously published remains unresolved.
