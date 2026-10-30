# P40 exact Hilbert rank and nullity of formal separating map

Let R=Q[y0,...,y9], S=Q[x0,x1,x2,z0,z1,z2]. The degree-n restriction Phi_n of the P39 map sends ten variables to the nine products x_i z_j, with y6 and y9 both mapped to x2 z2. Then image(Phi_n) is the full bidegree (n,n) component of S, because every x_i z_j has a preimage and every pair of exponent vectors alpha,beta of sum n can be realized as row/column sums of a nonnegative integer 3x3 matrix. Hence rank(Phi_n)=binom(n+2,2)^2 and dim ker(Phi_n)=binom(n+9,9)-binom(n+2,2)^2.

Exact independently executed Python verification: enumerated images of every degree-n source monomial n=1..4; found ranks 9,36,100,225 matching formula. At n=7: source dimension 11440, image rank 1296, kernel dimension 10144. Script papers/PAPER-03/code/p40_hilbert_rank.py. This is the unrestricted formal polynomial space, NOT the modular-invariant code-CFT enumerator subspace and NOT the full theta specialization kernel.

Prior art: Segre coordinate ring Hilbert function is classical; Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, Eq. (3.48) gives separating substitution. No claim of novel physical theorem.

Next research: compute the rank restricted to the actual span of graph-code refined enumerators and modular-invariant polynomials, then investigate full theta-function relations. Strict Q1 novelty gate remains NO-GO.
