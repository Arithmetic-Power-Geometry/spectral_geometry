# P62: HKM source-level typo and independent exact small-graph controls

Primary reference: Johan Henriksson, Ashish Kakkar, Brian McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, page 24 (PDF page index 25), eqs (3.37)-(3.48). Source: https://scoap3-prod-backend.s3.cern.ch/media/files/76861/10.1007/JHEP04(2023)011_a.pdf.

Original PDF screenshot inspected: eq (3.43) has y6=x[XX]=x[ZZ]; eq (3.46) visibly has y9=x[XZ]=x[ZZ]. Thus the printed equation duplicates ZZ. Eq (3.47) complete-polynomial exponent for y9 has XZ and ZX cases, supporting y9=x[XZ]=x[ZX] as the consistent intended map. This is an apparent published typo, not a new theorem; source author confirmation is not obtained.

Exact executable script papers/PAPER-04/code/p62_hkm_exact_audit.py:
- Implements ten groups of the 16 ordered local symbol pairs with labels 0=1,1=X,2=Z,3=Y, and y9={XZ,ZX}.
- Checks y6={XX,ZZ}, y9={XZ,ZX} and all 16 pairs assigned exactly once.
- Enumerates every labelled simple graph through n=4: 1+2+8+64=75 graphs; each graph has 2^n graph words.
- Constructs the complete 16-variable two-copy enumerator and HKM-corrected ten-variable enumerator by exact integer counting.
- Verifies coefficient sums equal 4^n for every graph.
- Verifies the separating factorization of the **ordered 16-variable** polynomial into two copies of the genus-one coarse polynomial, for every graph through n=4.
- Execution PASS for n=1,2,3,4.

Scope limitations: This does NOT independently reproduce HKM's published 7-vertex pair, verify the physical genus-two theta-function numerical substitution, modular covariance, or normalized genus-two partition function. The ten-variable polynomial cannot be directly assigned arbitrary asymmetric separating values because each class merges distinct ordered pairs. The full 16-variable polynomial is needed for the separating check. The observed factorization is a definitional identity, not new physics. No published graph-example replication or Paper 3 replacement manuscript is claimed.

Next P63: retrieve original 7-vertex adjacency matrices from Paper 3 artifacts or HKM source; reproduce 16- and HKM 10-variable coefficients and differences, compare the historical 756 number; check theta substitution with rigorous analytic bounds. Novelty gate remains NO-GO for Paper 4.
