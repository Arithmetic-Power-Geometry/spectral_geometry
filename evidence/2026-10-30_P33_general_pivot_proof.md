# P33 arbitrary-n edge-pivot invariance theorem

Let B be a symmetric zero-diagonal binary matrix, and e=(i,j) an edge. Let C(B)={(a,Ba):a in F_2^n}. Let S_e exchange X and Z bits at coordinates i and j in each binary Pauli vector. Then S_e(C(B))=C(B'), where B' is the binary edge pivot on e.

Proof. Define a'=a with a'_i=(Ba)_i, a'_j=(Ba)_j, other entries unchanged. Because B_ij=1 and B_ii=B_jj=0, the 2x2 linear map from (a_i,a_j) to (a'_i,a'_j) at fixed remaining coordinates is invertible (it swaps the two unknown bits up to known offsets). Hence a->a' is bijective. Direct substitution shows the swapped Z vector equals B'a' with B'_{ij}=1, B'_{ik}=B_{jk}, B'_{jk}=B_{ik}, and B'_{kl}=B_{kl}+B_{ik}B_{jl}+B_{jk}B_{il} for k,l outside {i,j}. Therefore the codes coincide after swap.

The ten genus-two refined classes of Henriksson, Kakkar, McPeak, JHEP 04 (2023) 011, Eq. (3.47), are invariant under simultaneous X/Z exchange on the two codewords at any one coordinate: I and Y are fixed, X and Z exchanged, and all pairs of classes are unions of such exchange orbits. Thus S_e preserves every monomial associated with each ordered codeword pair. Since S_e bijects C(B)^2 and C(B')^2, W_B^(2)=W_B'^(2) coefficientwise for arbitrary n.

Independent executable check enumerated ALL simple labelled graphs for n=2,3,4,5 (1098 graphs) and ALL 5325 oriented-by-unique-edge pivot tests; code-set bijection PASS 5325/5325. This is corroboration, not a replacement for the proof.

Prior-art limitation: graph ELC and X/Z local equivalence are established in Dymarsky and Shapere, Quantum stabilizer codes, lattices, and CFTs, JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160. Higher-genus polynomial invariance is a direct extension of these known mechanisms and likely implicit in Henriksson et al. Novelty not established. No original physical Fourier coefficient. Q1 manuscript NO-GO.
