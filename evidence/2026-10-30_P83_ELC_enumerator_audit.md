# P83 — Exhaustive ELC-orbit invariance of coarse and HKM10 polynomials
Date: 2026-10-30
Inputs: original P63 seven-vertex A/B edge lists. Generate labelled edge-local-complementation orbit by BFS over all present edges, ELC(i,j)=LC_i LC_j LC_i. For each orbit graph compute 128 graph-code words, coarse genus-one enumerator and corrected HKM10 ordered-pair genus-two quotient over 16384 pairs. Exact integer Counter comparisons, no floating point.

Executed local /mnt/data/p83_elc_enumerator.py:
A orbit 15, coarse_changes 0, HKM10_changes 0, unique coarse 1, unique HKM10 1.
B orbit 15, coarse_changes 0, HKM10_changes 0, unique coarse 1, unique HKM10 1.
The 756 HKM10 coefficient differences between original A/B remain, while each enumerator is constant within its own tested ELC orbit. This is an exact finite empirical theorem for these 30 labelled graphs, not a universal invariance proof.

Primary prior art: Dymarsky & Shapere, Quantum stabilizer codes, lattices, and CFTs, JHEP03(2021)160, DOI 10.1007/JHEP03(2021)160; Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP04(2023)011 DOI 10.1007/JHEP04(2023)011. Code-to-Narain lattice and genus-one theta substitution appear in latter eqs 2.38–2.42. General-genus physical theta substitution, normalizations, and possible identities among substituted theta constants remain unchecked.

Adversarial novelty: genus-one-isospectral inequivalent code CFTs and higher-genus distinctions already established. Exact ELC orbit invariance here validates code implementation and does not itself justify a fourth paper. Need full physical specialization and independent separation of analytic theta functions. No claims of physical genus-two separation based only on formal polynomial inequality.

Publication gate: P83 computational PASS, physics and novelty NOT PASSED. Paper 4 NO-GO. Next P84 derive and independently implement physically normalized genus-two theta specialization; check nonvanishing under theta identities and genus-two modular consistency.
