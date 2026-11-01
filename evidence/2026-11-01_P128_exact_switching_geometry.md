# P128 — exact decoder-switching geometry, same manuscript (2026-11-01)

## Model and baseline
Five-qubit stabilizer XZZXI, IXZZX, XIXZZ, ZXIXZ; independent I/Z site noise conditional on a common calibration parameter. Sites 1–2: dephasing probability t; sites 3–5: 2t; physical domain 0<=t<=1/2. Nominal fixed decoder is selected at the homogeneous point t=u=1/10, *not* at a point on the coupled line.

## Verified exact result
Independent symbolic re-enumeration of 32 supported I/Z errors gives 16 syndrome pairs, total mass identically 1, and 6 distinct gap polynomials along u=2t. Exact rational root isolation establishes 13 syndrome-level interior switches, in 4 distinct threshold values: about 0.085258229520 (syndrome 1111), 0.25 (8 syndromes), 0.313772057751 (syndrome 0000), and 0.370972063761 (3 syndromes). Syndromes 0110, 1011, 1101 have no interior winner/rival crossing. Every root is a zero of an exact integer polynomial, not merely a floating-point fit.

Representative exact gap: syndrome 1111, winner coset key 3 vs rival 28: -t^2(16t^3-28t^2+14t-1). Its first positive interior root is approximately 0.085258229520; at t=0.1, u=0.2 the gap is negative.

## Cautions
The switch counts refer to the originally nominal decoder's syndrome-wise comparisons, not necessarily the number of distinct globally optimal decoders. Endpoints and zero-mass ties require careful interpretation. This is a new verified *instance calculation* but not yet a general theorem or established literature novelty. No Molavi/Cao executable comparison was performed. Preserve earlier P127 findings unchanged.

## Reproducibility
Script code/p128_exact_switching.py rebuilds masses from scratch, tests normalization and 16-syndrome structure, factors every gap, and isolates roots with exact rational endpoints. Requires Python 3 and SymPy. Local execution returned PASS.
