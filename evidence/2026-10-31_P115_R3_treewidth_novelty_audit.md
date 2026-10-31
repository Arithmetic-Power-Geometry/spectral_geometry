# P115-R3 bounded-treewidth algorithm audit

A direct sum of independent stabilizer-code blocks under product Pauli noise has factored syndrome-logical-coset probabilities. Therefore its optimal ML success is the product of the individual block ML successes. This is a standard structural property, not a new theorem.

Executed independent exact Fraction test for two five-qubit blocks with different Pauli channels: block A 91983723/100000000; block B 1006969111/1250000000; combined 92624767775780253/125000000000000000. All assertions passed. The test computes combined syndrome/coset maxima by products of independently enumerated block masses; it does not enumerate all 4^10 errors.

Counts for m copies: full enumeration 4^(5m) versus m*1024 for separately enumerated blocks. These are theoretical string counts, not wall-clock timings, and assume block independence.

Prior art novelty controls: Cao et al., Quantum Lego Expansion Pack: Enumerators from Tensor Networks, PRX Quantum 5 030313 (2024), DOI 10.1103/PRXQuantum.5.030313; Molavi, Saad, Albarghouthi, Analyzing Decoders for Quantum Error Correction, arXiv:2603.20127 (2026); Cheng and Pan, Exact Maximum Likelihood Decoding beyond Treewidth via Rank-Decomposition Dynamic Programming, arXiv:2609.39556 (2026). The latter reports exact rank-width parameterization, a particularly strong novelty obstacle for a simple treewidth-based method. Published method implementations were not run in this audit.

Decision: correct local factorization and clean numerical test PASS. Original theorem and direct state-of-the-art comparison NO-GO. Next target must be a specific certificate capability not already covered by tensor networks, rank-width DP, or constrained polynomial optimization, with explicit matching baselines.
