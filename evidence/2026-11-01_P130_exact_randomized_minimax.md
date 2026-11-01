# P130 — exact robust values on coupled dephasing family (2026-11-01)

Same manuscript and code as P127–P129. Five-qubit stabilizer, perfect syndrome extraction, independent I/Z errors with site rates (t,t,2t,2t,2t), 0<=t<=1/2.

Exact exhaustive symbolic enumeration gives nominal homogeneous-channel deterministic decoder success F(t)=-(2t-1)(24t^4-30t^3+4t^2+2t+1), with F(0)=1 and F(1/2)=0, so its worst case is zero.

An explicit *fixed randomized* syndrome decoder chooses the nominal winner coset for syndrome integers 0,2,4,6,9,11,13; nominal rival for all other syndromes except syndrome 14; at syndrome 14 chooses nominal winner with probability 2/3 and rival with probability 1/3. This decoder has success R(t)=(t-1)(64t^4-48t^3-4t^2+3t-3)/3, with exact identity R(t)-3/4=(2t-1)(4t-1)^2(8t^2-6t-3)/12 >=0 on the entire physical interval. At t=1/4, independent syndrome-wise ML maximization yields 3/4, so R_ML=3/4 and optimal fixed randomized robust success=3/4 by matching lower/upper bounds.

Crucial limitation: the **best fixed deterministic robust success is NOT established**; only the nominal deterministic decoder's zero worst case is established. The randomized certificate does not imply a deterministic minimax gap. No prior-art novelty or Q1 acceptance is claimed. A numerical LP guided the randomized construction, but the final polynomial identity and inequalities are exact and do not depend on LP accuracy. The Python verification was run locally and passed. Preserve earlier evidence append-only.
