# P132 — independent exact audit and manuscript integration gate (2026-11-01)

The locally executed independent SymPy-only script p132_audit.py rebuilt all 32 supported I/Z errors from stabilizer generators, grouped 16 syndrome pairs, and proved normalization. No SciPy/MILP needed.

For the coupled line (t,t,2t,2t,2t), 0<=t<=1/2, the t=1/4 restriction leaves exactly 256 candidate deterministic decoders, collapsing to 21 distinct exact success polynomials. Optimal F(t)=16t^5-28t^4+10t^3+3t^2-2t+1, one winner decision bit string 0011011000111011. For each of the other 20 polynomials, an exact rational t=j/1000 was found where success is strictly below 749591/1000000. For F, SymPy exact real-root isolation of F-749591/1000000 finds no roots on [0,1/2], and F(0)>threshold, proving F exceeds threshold throughout. Other decoders excluded by t=1/4 cannot exceed 11/16. Thus the deterministic optimum is F's global minimum.

**Correction/clarification:** F has TWO interior stationary points: a local minimum at t≈0.2633732449103756 (F≈0.7495918985924895) and local maximum at t≈0.4207986588153863 (F≈0.7679124914156683). P131 discussed the global minimizer but did not explicitly note the second stationary point. Both are isolated by exact rational endpoints. Exact derivative F'=2(40t^4-56t^3+15t^2+3t-1). F(0)=1, F(1/2)=3/4, confirming the first stationary point is the global minimum.

Randomized fixed and adaptive ML robust success 3/4 (P130), so strict randomization advantage ≈0.0004081014075105. This is specific to this uncertainty family, not a general theorem or verified novelty against Molavi et al. and Cao et al.

**Manuscript integration recommendation:** append a clearly labeled worked example subsection after the existing fixed-versus-adaptive decoder section. State physical channel independence, coupled calibration uncertainty, exact five-region adaptive curve from P129, explicit randomized decoder certificate P130, and exhaustive deterministic optimum P131/P132. Do not overwrite original manuscript without obtaining its editable source and checking cross-references. Do not claim new general theorem, general SOS completeness, or Q1 acceptance.

The full locally executed checker and its output are conversation artifacts p132_audit.py and audit_log.txt. GitHub record is append-only; scripts are not yet committed in this step.
