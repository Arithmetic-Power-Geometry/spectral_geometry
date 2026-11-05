# Stage 03 — joint-valuation theorem and genuinely useful consequences

Use p>3; D=x-y, H=x²+xy+y²; q=1/p and δ=1_{p≡1 mod 3}. Prove, rather than assume, the primitive valuation decomposition for (u,v) with min(v_p(u),v_p(v))=0. In particular show that positive v_p(u-v) and v_p(u²+uv+v²) cannot coexist, compute exact primitive measures for j≥1 and derive C_p.

Define G_p(U,V) explicitly, then justify
F_p(U,V)=G_p(U,V)/(1-q²UV²).
Check F_p(1,1)=1 and show coefficient identities at many exact capped valuations, independently enumerated modulo p^e for feasible small p,e.

**New research task:** derive, if possible, a closed rational expression for
K_p(T)=Σ_{e≥2} K_p(e)T^e
using the exact joint valuation distribution. Derive a recurrence and/or growth statement *only after* an independently checked rational expression. Include formal convergence/series interpretation, denominator, initial conditions, exceptional cases and all cancellations. Numerically test coefficients against independent strict-mask enumeration across p≡1,2 mod3 and multiple exponents. Compare results to known local Poincaré-series theory: generic rationality is not itself a novelty claim.

If this extension does not withstand complete proof checking, keep it as an internal research question; do not introduce a speculative theorem in the paper.

**Deliver:** `PROOF_JOINT_VALUATION.md`, exact symbolic derivation, independent check script and count CSV. **Gate:** every displayed identity follows from proved lemmas and checks match; otherwise FAIL/OPEN.
