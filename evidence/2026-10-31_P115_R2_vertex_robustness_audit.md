# P115-R2: vertex-certificate scope and counterexample

For a fixed syndrome decoder D, its success under independently varying local Pauli distributions is multi-affine in the local probability vectors. On a product of convex polytopes, its minimum and maximum occur at combinations of local vertices. Hence checking a fixed decoder's success lower bound at all vertices is exact.

For a fixed reference ML decoder D0, every competing syndrome/coset mass difference is multi-affine. Therefore D0 remains optimal throughout a product uncertainty region if and only if all reference-winner-minus-competitor gaps are nonnegative at every product vertex. Strictly positive gaps at all vertices imply unique optimality throughout. This is a finite exact certificate, but may require exponentially many vertex checks; no polynomial runtime claim follows.

Counterexample to incorrectly applying the same vertex-minimum rule to reoptimized ML success: a single qubit with no stabilizers and only I/X errors with probabilities (t,1-t), t in [0,1], has optimal identity-decoding success max(t,1-t). Its minimum is 1/2 at t=1/2, while both vertices have success 1. Thus minimum of optimal ML success cannot in general be certified by vertex evaluation alone.

Novelty decision: mathematical consequences of multi-affinity and elementary convexity; no original central theorem established. Published-algorithm runtime comparison remains unperformed. Do not present as a new theorem or claim scalable advantage.
