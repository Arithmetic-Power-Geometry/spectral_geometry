# P55 Paper 4 four-world exact minimum-observation benchmark

Exact rational code in /mnt/data/p55_paper4_design.py (user-visible attachment). Fixed G=[[2,1/3],[1/3,3]], B=bJ with b in {0,1/10,1/5,-1/5}; charge enumeration [-5,5]^4, E<=3. Coercive lower bound E>=3/20 ||v||² for |b|<=1/2 makes this exhaustive at E<=3. Observation = one scalar joint energy-spin multiplicity N_b(E,s), cost = one per scalar coefficient; allowed rows have E<=3. Distinct physical oriented CFTs: every pair has differing joint (E,s) multiplicity, so ordinary O(2,2;Z) duality is ruled out for each pair.

Exhaustive combination search found minimum 3 scalar coefficient observations:
(E,s)=(2,0) -> signatures (2,0,0,0);
(5309/2650,0) -> (0,2,0,0);
(3313/1325,-1) -> (0,0,2,0).
Hence four worlds have distinct 3-coordinate signatures.
Pair first differing joint levels: (0,1/10): (2,0); (1/10,1/5): (5309/2650,0); (0,-1/5): (2,0); (1/5,-1/5): (3313/1325,-1); (0,1/5): (2,0); (1/10,-1/5): (5309/2650,0).
30 informative scalar rows, 6 distinct multiplicity patterns.

Caveat: minimum 3 is a verified finite enumeration result, not a Narain-specific theorem. Ordinary information bound ceil(log_2 4)=2 does NOT prove 3; exhaustive enumeration of all 1- and 2-row combinations does. The proof is algorithmic and needs independently reproducible source/verification; the search currently uses Python combinations over 30 rows. A complete spin-vector at one energy has different cost semantics. A single maximum-energy-threshold observation has another cost semantics. No global experiment optimum claim.

Novelty audit: Crowston et al., Parameterized Study of the Test Cover Problem (MFCS 2012), DOI 10.1007/978-3-642-32589-2_27; Chakraborty et al., Tight (Double) Exponential Bounds for Identification Problems: Locating-Dominating Set and Test Cover, SIAM J Discrete Math (2026), DOI 10.1137/24M1692009. These show mature classical theory. Narain-specific prior art includes Angelinos et al., Optimal Narain CFTs from codes, JHEP 11 (2022) 118. No general new theorem yet. NO-GO writing Paper 4 as research article. Next P56: derive symbolic family-level theorem or a nontrivial cost-separation result not reducible to standard test cover; audit modular and duality symmetries.
