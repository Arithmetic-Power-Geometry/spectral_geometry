# P126 — same-manuscript novelty gate and soundness specification (2026-11-01)

## Scope and prior evidence
Continue main (65).pdf, not a separate paper. Preserve P118 negative novelty finding and P125 full-interval example. P118 states Molavi 2026 overlaps constrained-polynomial robustness and Cao 2024 covers exact enumerator methods. No matched executable benchmark is available. No new originality claim is warranted yet.

## Candidate general certificate — mathematically sound but not yet novel
Let Theta be a compact basic semialgebraic set of channel parameters, with nonnegative normalized polynomial Pauli probabilities p_i(P;theta) and independent site errors conditional on theta. For any stabilizer code and a fixed deterministic syndrome decoder D, define polynomial gaps g_{s,c}(theta)=M_{s,D(s)}(theta)-M_{s,c}(theta). Then D is ML optimal for every theta in Theta iff every g_{s,c} is nonnegative on Theta. Proof: ML objective is sum of independent per-syndrome maxima, so a fixed D achieves ML at a given theta iff every selected coset maximizes its syndrome mass; nonnegative gaps are exactly these conditions. This is a direct reformulation of standard ML optimality, NOT an original theorem.

A proposed proof-carrying sufficient certificate is an exact polynomial identity g_{s,c}=sigma_0+sum_j sigma_j h_j, where Theta={theta:h_j(theta)>=0} and sigma_j are explicitly provided sums of squares over rationals. Checking identities and SOS decompositions verifies nonnegativity. This is a standard Positivstellensatz/SOS-style certificate, not novel by itself; not every nonnegative polynomial necessarily admits a certificate of this restricted form. Do not assert completeness or complexity improvement.

## Research hypothesis to test within same manuscript
Can stabilizer automorphisms and coset symmetries provably reduce the number/degree/size of exact polynomial certificates under *coupled heterogeneous* uncertainty, beyond ordinary orbit reduction and the existing Molavi/Cao methods? Required: formal symmetry action preserving Theta and channel model, exact orbit proof, negative controls where symmetry is broken, fair benchmarks, independent checker.

## Stop conditions
NO-GO for originality if reduction merely groups identical five-qubit gap polynomials, uses generic SOS without a distinct advance, or lacks comparative evidence. Do not label this as a new algorithm/theorem until proved. Keep all older evidence append-only.
