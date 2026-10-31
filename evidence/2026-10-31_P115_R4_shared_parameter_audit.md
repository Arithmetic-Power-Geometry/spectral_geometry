# P115-R4: shared-parameter robustness falsification

Research question: does checking parameter endpoints suffice for fixed-decoder robustness when several independent sites share the same uncertain error rate?

Counterexample: two independent binary errors with common error rate t. Fixed success event 'even error parity' has probability P(t)=(1-t)^2+t^2. At t=0 and t=1 the success probability equals 1, while at t=1/2 it equals 1/2. Hence the endpoint-only certificate fails. This is an illustrative classical parity event; it is not presented as an independently established stabilizer-code decoder instance.

When site probabilities u,v vary independently, Q(u,v)=(1-u)(1-v)+uv is multi-affine. Its extrema over [0,1]^2 occur at vertices. Restricting to the diagonal u=v=t destroys multi-affinity in the single free parameter.

Exact Fraction tests checked endpoint and midpoint values, a 101-point diagonal sweep, and a 121-point two-parameter grid against vertex bounds. All passed. Grid tests are supporting checks; the polynomial identities give the proof.

Prior-art overlap: Molavi, Saad and Albarghouthi (2026), arXiv:2603.20127, already use constrained polynomial optimization for quantum decoder robustness. Cheng and Pan (2026), arXiv:2609.39556, address exact likelihood evaluation using rank-width; their complexity claims do not automatically apply to optimizing tied uncertain parameters. No originality claim or matched algorithm benchmark is established.

Decision: scope correction PASS; original theorem NO-GO. Next candidate: certified constrained-polynomial optimization of tied channel parameters, with explicit comparison to Molavi et al. Do not begin full original-research manuscript.
