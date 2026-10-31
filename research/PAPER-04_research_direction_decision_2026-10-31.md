# Paper 4 — Research direction selection (2026-10-31)

Status: research decision only; NOT a manuscript approval or a novelty claim.

## Ranked candidate directions

| Priority | Direction | Decision | Rationale |
|---|---|---|---|
| 1 | Quantum error-correction code auditing | PRIMARY Paper 4 research track | Directly builds on graph-code and stabilizer methods. Must establish operational information beyond genus-one / weight enumerators and established higher-genus literature. |
| 2 | Cryptographic lattice structural distinguishers | PARALLEL exploratory track, not Paper 4 by default | Possible transfer of structural invariants to correctly defined Module-LWE lattice instances, subject to rigorous baselines and reduction arguments. No demonstrated ML-KEM attack. |
| 3 | Breaking RSA using Narain lattice methods | SPECULATIVE, currently NO-GO | No known reduction from Narain inverse spectral geometry to factoring RSA integers; cannot claim ability to break RSA. Record only as a falsifiable feasibility question. |

## Paper 4 provisional title
Beyond Weight Enumerators: Higher-Order Invariants and Operational Distinguishability in Quantum Stabilizer Codes

## Primary experimental protocol
1. Load exact graph adjacency matrices and check source provenance. The seven-vertex comparison already appears in Henriksson, Kakkar, McPeak (2023), so reproduction alone is not novel.
2. Compute stabilizer generators K_i=X_i prod_{j in N(i)} Z_j and enumerate the complete stabilizer groups.
3. Separate [[n,0]] stabilizer states from [[n,k,d]] codes with k>0. Do not infer error correction from a graph state alone.
4. Define actual logical code subspaces, syndrome maps, Pauli error models, code distances, and decoders; test Knill–Laflamme conditions.
5. Compare genus-one, genus-two, ordinary weight enumerators, minimum distance, degeneracy, and operational decoder performance against strong existing baselines.
6. Search for a new theorem or independently reproducible operational benefit; include negative controls and previously known examples.
7. Run hostile prior-art audit before any manuscript writing.

## Cryptographic track
Use toy Module-LWE b=As+e (mod q), valid module/ring construction, legitimate security assumptions, and standard lattice-reduction/statistical baselines. No equivalence between Narain lattices and ML-KEM lattices is assumed. Do not claim security proof or break without explicit reduction and independently validated attack.

## RSA feasibility track
Require a mathematically explicit efficient mapping from integer factoring to the proposed Narain algorithm, complexity analysis, and controlled comparisons against established factoring baselines. Absence of a mapping is a negative finding. Do not present quantum Shor factoring as a consequence of this research.

## Manuscript gate
GO only after a novel, proved and independently reproduced operational claim with a verified prior-art distinction. Until then: RESEARCH GO, PAPER 4 MANUSCRIPT NO-GO.

## Verified starting references
- Henriksson, Kakkar, McPeak (2023), Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011. DOI 10.1007/JHEP04(2023)011.
- NIST FIPS 203 (2024), Module-Lattice-Based Key-Encapsulation Mechanism Standard. DOI 10.6028/NIST.FIPS.203.
