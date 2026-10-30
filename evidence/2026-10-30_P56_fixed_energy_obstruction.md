# P56 — Fixed-energy obstruction for continuous Narain B-field family

## Research question
Can countably many predetermined exact energy/spin multiplicity probes identify a generic B-field parameter b, with G fixed positive definite and B=bJ?

## Proven proposition
Let A be any countable subset of R, fixed independently of b. Define N_b(E,s)=#{(m,n) in Z^2×Z^2: E_b(m,n)=E and m·n=s}, with E_b=(m+bJn)^T G^-1(m+bJn)+n^T G n and positive-definite G. There exists a countable set Z_A subset R such that for all b outside Z_A, for every E in A and integer s, N_b(E,s)=#{m in Z²: m^T G^-1 m=E} if s=0, and zero otherwise. In particular, every pair of b outside Z_A produces identical outcomes for all these fixed-energy probes.

## Proof
For each n≠0 and m, b↦E_b(m,n) is a degree-two polynomial with strictly positive leading coefficient (Jn)^T G^-1(Jn). For each E in A, equation E_b(m,n)=E has at most two roots. Union of root sets over countably many E,m,n is countable. Outside this union, no winding state occurs at any probed energy. States n=0 have E=m^T G^-1 m independent of b and spin zero. Finiteness of multiplicities follows positive definiteness for fixed b. QED.

## Strong corollary
If G has rational entries and A=Q, then every transcendental b has the same complete rational-energy spin-multiplicity profile, namely the pure momentum contribution. Proof: E_b(m,n) is a nonconstant rational-coefficient quadratic for n≠0, so E_b=E rational implies b algebraic. This is a statement about pointwise exact energy coefficients, NOT finite-resolution windows, heat traces, full partition functions or physically achievable experiments.

## Exact symbolic test
Code papers/PAPER-04/code/p56_fixed_energy_obstruction.py; 625 charge tuples (m_i,n_i from -2..2) checked by SymPy. Leading coefficient for G=[[2,1/3],[1/3,3]] is 3(6n1²+2n1n2+9n2²)/53>0 for n≠0. Script passed.

## Novelty and limitations
This proposition is a rigorous family-level obstruction, but its proof is elementary countability and polynomial roots. It does not establish literature novelty or publishability. It is sensitive to exact singleton-energy measurements; physical experiments measure finite resolution intervals, and spectral-level tracking may recover b. The proposition does not assert that generic b backgrounds are pairwise nondual; O(2,2;Z) orbits are countable, so uncountably many nondual generic backgrounds remain even after quotient. No complexity-class or Hecke claim.

## Next
P57: test finite energy windows with certified lower bounds; compare adaptive level-location and heat-trace measurements; hostile prior-art audit of spectral inverse and sampling-obstruction results. No Paper 4 drafting until a genuinely new theorem is established and checked.
