# P38 finite-order complete joint enumerator reconstruction

## Verified background
Henriksson, Kakkar and McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011: higher genus partition functions as higher-weight theta polynomials; genus-two distinguishes some genus-one isospectral code CFTs. Dymarsky and Shapere, Quantum stabilizer codes, lattices, and CFTs, JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160: quantum stabilizer codes and Narain CFTs, T-duality/code equivalences.

## Candidate theorem (complete joint enumerators only)
For binary linear C,D subset F_2^m, each of dimension k, let J_k(C) be the polynomial in 2^k independent variables indexed by F_2^k, summing over ordered k-tuples of C the monomial whose exponent at v is the number of coordinates with column v. Then J_k(C)=J_k(D) iff C,D are coordinate permutation equivalent.

## Proof
Pick an ordered basis (c_1,...,c_k) of C. Its k by m generator matrix has full row rank, so its multiset of columns spans F_2^k. The associated monomial occurs in J_k(C) with positive coefficient. Equality of polynomials implies that an ordered k-tuple (d_1,...,d_k) of D has exactly that multiset of columns. Hence its matrix has full row rank k, and d_1,...,d_k is a basis of D. Since column multisets coincide, a permutation of the m coordinate columns carries the first generator matrix to the second, giving C coordinate-permutation equivalent to D. Conversely, coordinate permutation gives a bijection on all ordered k-tuples preserving their column-pattern counts, hence J_k equal.

## Critical limits
This is an exact elementary theorem about complete joint enumerators, NOT the ten-variable refined genus-two enumerator and NOT physical genus-k partition functions. Theta specialization and modular identifications can lose information. Higher-weight and complete weight enumerator literature may already imply this result. No novelty or physics claim until strongest prior art is checked. Next task: prove/falsify transfer to graph-code refined genus g with ELC/T-duality, and locate prior art on genus-k complete weight enumerator reconstruction. Q1 NO-GO.
