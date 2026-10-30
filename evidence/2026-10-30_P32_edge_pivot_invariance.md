# P32 finite edge-pivot equivalence stress test

Primary source: Dymarsky and Shapere, Quantum stabilizer codes, lattices, and CFTs, JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160. Published seven-node pair: Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011.

Implementation: binary principal pivot on each existing edge of symmetric zero-diagonal adjacency matrix; reconstruct the 128 codewords and 16384 ordered pairs and ten-variable refined genus-two enumerator by Eq. (3.47). Locally executed independent Python test. All 10 edges of graph B1 and 11 edges of graph B2 preserve the complete refined genus-two polynomial coefficientwise. PASS 21/21. Therefore the specific delta polynomial and its P28 fixed-coordinate 454 minimum are unchanged by these 21 transformations.

Limitations: This checks single-edge pivots on two seven-node graphs. It does not establish a theorem for arbitrary graph sizes, entire pivot orbits, graph relabellings (which preserve the enumerator by direct coordinate permutation), or all Narain dualities. The underlying genus-two distinction is already published. A general proof might follow from local coordinate permutation/symplectic action but must be derived precisely; do not assert it here.

Scientific significance: tests whether a proposed algebraic diagnostic is stable under graph-code equivalence rather than arbitrary polynomial reparametrization. Q1 novelty gate remains NO-GO pending a new general theorem and physical Fourier coefficient.
