# P28 exact optimality certificate

For the published Henriksson–Kakkar–McPeak seven-vertex graph-code pair (JHEP 04 (2023) 011, eq. 4.19), compute the ten-variable genus-two refined polynomial difference by P26. It has 756 supported monomials in 143 separating-image fibres. Fibre size distribution: 2:14, 3:26, 4:40, 5:10, 6:8, 7:24, 8:6, 9:4, 10:6, 16:5.

Apply P27 exact subset dynamic programming to each fibre to maximize its number of disjoint zero-sum coefficient blocks. All 143 fibres solved exactly, largest support 16. Aggregate optimal zero-sum blocks: 302. P27 fixed-support binomial certificate theorem gives minimum length 756-302=454, improving P26 valid 613-term pivot certificate by 159 terms. Exact integer test assertions PASS.

Full distribution (fibre size, optimal blocks): (2,1):14; (3,1):26; (4,1):20; (4,2):20; (5,1):4; (5,2):6; (6,2):4; (6,3):4; (7,2):4; (7,3):20; (8,3):4; (8,4):2; (9,3):4; (10,4):4; (10,5):2; (16,8):5.

Proof of global optimality follows P27 graph-component lower bound per fibre and matching star-construction upper bound; different separating images cannot mix in an allowed certificate. Scope strictly fixed support, rational coefficients, binomials of monomials with the same separating image. No minimality claim for arbitrary polynomial ideal certificates with auxiliary monomials or preselected ideal generators.

Novelty warning: zero-sum partition / flow graph argument is elementary and may be known. The example is already published. This is an exact new computation relative to our project, not established novel physics. No normalized genus-two Fourier coefficient. Q1 NO-GO pending prior-art and physically meaningful novel theorem.
