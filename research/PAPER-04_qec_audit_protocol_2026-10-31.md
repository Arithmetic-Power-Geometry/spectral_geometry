# Paper 4 QEC audit — executable research specification
Status: planned, not yet executed.

## Inputs
Verified adjacency matrices for existing graph pair; independent stabilizer-code benchmarks with known [[n,k,d]] parameters; explicit physical noise channels.

## Invariants
Stabilizer weight enumerator, complete enumerator, higher-genus polynomial invariants, logical operator weights, distance, syndrome degeneracy, and decoder success rates.

## Required falsification
- Check whether the original graph pair is equivalent under relevant graph/code equivalences.
- Test whether higher-genus differences persist after controlling for code distance and ordinary weight distributions.
- Test whether any higher-genus feature predicts logical error or decoding advantage out of sample.
- Explicitly report null findings; avoid interpreting spectral distinguishability as superior protection.
- Prove mathematical statements exactly where feasible, and provide reproducible seeded simulations for noisy performance.

## Publication readiness
NO-GO until original theorem or operational advantage established and novelty audit passed.
