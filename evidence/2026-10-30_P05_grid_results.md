# P05 rational-grid falsification, 2026-10-30

Exact Python fractions experiment, energy cutoff H=2, 54 backgrounds:
a,c in {3/2,2,5/2}; d in {0,1/4}; b in {0,1/5,2/5}.
Positive definiteness holds. Gershgorin: lambda_min(G)>=5/4 and lambda_max(G)<=11/4. ||B||<=2/5. For E<=2, ||n||<=sqrt(8/5)<1.265 and ||m||<=sqrt(11/2)+(2/5)sqrt(8/5)<2.86. Thus the script's integer search box m_i in [-3,3], n_i in [-2,2] is complete (conservative).

Result: 28 distinct exact unlabelled energy-multiplicity fingerprints, 20 groups with at least two members, 34 colliding unordered parameter pairs. At least some are trivial coordinate-permutation equivalences, e.g. G=diag(3/2,2) vs diag(2,3/2), both B=0.

**Negative gate:** No collisions have been proved distinct under full O(2,2;Z) or parity. Finite cutoff collisions cannot establish equality of full theta series. Do not claim novel isospectral nondual examples.

Relevant verified earlier references: Schiemann 1997; Conway–Sloane 1992; Giveon–Porrati–Rabinovici 1994. New source candidate Henriksson–Kakkar–McPeak, Narain CFTs and Quantum Codes at Higher Genus, JHEP04(2023)011, DOI 10.1007/JHEP04(2023)011, from arXiv 2205.00025; bibliographic record appended separately.
