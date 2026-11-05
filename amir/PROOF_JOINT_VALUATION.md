# Stage 03 — joint-valuation proof audit and count verification

**Status: PARTIAL PASS** for the existing rational bivariate series and the nine listed exact counts; **OPEN** for the proposed univariate rational generating function and recurrence. This is an internal proof note, not a publication-ready novelty certificate.

Let p>3, q=1/p, δ=1 if p≡1 mod 3 and 0 otherwise. Set D=x−y and H=x²+xy+y². Write (x,y)=p^t(u,v) with min(v_p(u),v_p(v))=0, outside a null set. The measure of each scaled primitive stratum is q^(2t) times its primitive measure. Its valuation shift is (t,2t).

For primitive (u,v), the events p|u−v and p|u²+uv+v² cannot both occur: if u=v mod p, then H=3v² mod p, forcing v=u=0 mod p, contradicting primitivity.

For j≥1, the Haar measure (relative to the full Z_p² ambient measure, not conditional on primitivity) of primitive pairs with v_p(u−v)=j is (1−q)²q^j. This follows from measure p^(-j)(1−q) for u−v≡0 mod p^j with v a unit, minus the corresponding j+1 event. The quadratic factor has 2δ simple nontrivial roots modulo p and hence exact-j primitive measure 2δ(1−q)²q^j. The remaining primitive mass is C_p=1−q²−(1+2δ)(1−q)q. Consequently

F_p(U,V) = [C_p+(1−q)² qU/(1−qU)+2δ(1−q)² qV/(1−qV)]/(1−q²UV²).

At U=V=1, the numerator equals 1−q², so F_p(1,1)=1. Coefficients represent exact valuation probabilities. For a,b<e, p^(2e)[U^a V^b]F_p is an integer counting the corresponding residue pairs modulo p^e. Thus K_p(e)=p^(2e) Σ_{0≤a,b<e,a+b≥e}[U^a V^b]F_p.

## Verified numerical results
Run `python3 verify_stage03.py`. It uses three distinct calculation routes: (i) finite-sum formula, (ii) coefficient-level rational arithmetic derived from the primitive valuation branches, and (iii) direct modular divisibility enumeration for p^e≤625. All 9 formula/series pairs agreed; 4 smaller cases also agreed with direct enumeration. See `STAGE03_RESULTS.csv`.

## Open research target
Derive and rigorously simplify the univariate series K_p(T)=Σ_{e≥2}K_p(e)T^e and any resulting recurrence. **No closed rational formula or recurrence has been established in this stage.** Do not insert a theorem claiming one, or inflate the novelty score, before independent proof and verification.

## Scope limitations
p=2,3 are outside this proof. Numerical agreement is not proof of all cases; proof above supports the existing F_p identity, while the finite-sum equivalence should receive the independent boundary-case audit in Stage 04. The paper remains ineligible for a positive *Integers* compliance certification without resolving the journal's AI-use restrictions.
