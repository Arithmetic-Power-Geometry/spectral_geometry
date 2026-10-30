# P21 independent exact audit — 2026-10-30

Independently recomputed published seven-vertex graph-code pair of Henriksson, Kakkar, McPeak (JHEP 04 (2023) 011), Eq. (4.19), using direct enumeration over all binary vectors and all ordered codeword pairs.

B1 rows: 0100010,1010001,0101111,0010100,0011000,1010001,0110010.
B2 rows: 0100011,1010001,0101111,0010100,0011000,1010001,1110010.

Exact output: genus-one 16 nonzero refined monomials for each, equal; complete genus-two 16-variable joint enumerators have 5186 and 5246 nonzero monomials, union support 8864, and total multiplicity 16384 each. Lexicographically first difference is exponent tuple (0,0,0,0,0,0,0,0,0,0,0,3,0,1,2,1), coefficient 0 versus 1. Both handle marginals equal 128 times genus-one enumerator; each genus-two enumerator is handle-exchange invariant. All independent assertions passed.

Interpretation: this verifies a FORMAL 16-variable code polynomial difference, not a physically distinguishing genus-two Fourier coefficient. Distinct polynomials can become equal after a noninjective theta-constant substitution; an actual nonzero physical coefficient must be exhibited. The published source reports physical genus-two distinctions, but our independent reproduction has not checked them.

P20 GitHub writes were blocked; its exact tests were independently rerun here. The full physical theta substitution, oscillator determinant, modular covariance and a new minimal coefficient theorem remain OPEN. No new theorem, no Q1 manuscript.
