# P59 — Three-manuscript synthesis and fourth-paper discovery reset (2026-10-30)

## Primary manuscripts inspected
1. Finite Spectral Reconstruction and Robust Non-Identifiability in Two-Dimensional Narain Compactifications (13 pages; reviewed abstract, definitions, Theorems 3.1 and 4.1).
2. The First Spin-Resolved Spectral Discrepancy in a Narain Two-Torus Family: Exact Thresholds, Symmetry Boundaries, and Stability (13 pages; reviewed abstract, general propositions and threshold theorem introduction).
3. Exact Certificates and Falsification Controls for Narain Spectra, Graph Codes, and Integral Lattice Splitting (18 pages; reviewed abstract, definitions and graph-code enumerator conventions).
The review was based on the available copies of these manuscripts, not a fresh line-by-line verification of every proof, equation and reference.

## Overlap and hard constraints
Paper 1 already proves a no-background-independent finite cutoff and five labelled energies reconstruct the 2D background, plus rectangular unlabelled onset. Paper 2 already proves an exact first spin discrepancy for the b versus -b family and an interval stability result. Paper 3 explicitly treats genus-one/genus-two code-CFT distinctions as prior art, reports previously published 7-vertex pair, and standard integral splitting certificates. Therefore P51-P58 four-world test-cover, exact-energy and finite-window obstructions, labelled quadratic precision, and repeated b-sign witnesses are too incremental. Do not write Paper 4 from them.

## High-priority mathematical audit before any new theorem
Paper 3 section 2.4 defines 16 ordered two-copy local symbols; past computational ten-variable quotients identify ordered pairs under a simultaneous X/Z swap. Compare with the precise 10-variable invariant conventions in Henriksson, Kakkar and McPeak (2023); do not assume those are identical. Check physical theta normalization and separating/nonseparating genus-two statements.
Check how parity, O(d,d;Z), spin and full oscillator-completed partition functions are used; separate zero-mode claims from full CFT. Verify analytical completeness for all first-level claims.

## Broad direction scan (rank provisional; no established novelty)
A. **Exact information-lift hierarchy** (priority 1): formalize maps from coarse genus-one partition data to refined spin or symmetry data, then higher-genus, with physical quotient. Seek new nonliftability theorem, minimal genus/refinement for explicit infinite family, exact nontrivial certificate. Strong collision with HKM 2023; kill-test before building.
B. **Duality-invariant finite determinacy on arithmetic subfamilies** (priority 2): bounded-denominator, bounded-height rational Narain backgrounds; derive explicit finite cutoff or sample complexity sufficient for physical orbit identification, sharp lower bound. Need separate from Paper 1 rectangular family and classical reduction theory. Beware rational height restrictions, nonuniqueness of full theta.
C. **Integral splitting / indecomposability with coupled Q,J** (priority 3): construct new infinite families where standard short-vector certificates fail but new local-global obstructions decide splitting. Collision with classical Kneser decomposition and Paper 3.
D. **Genus-two separating degeneration and exact nonvanishing** (priority 4): reconcile enumerator variables and establish full normalized genus-two partition function distinction, not merely polynomial mismatch; likely substantial prior art and normalization difficulty.
E. **Experiment cost / test cover** (priority 5): retain as application only; classical NP-hard optimization and elementary precision/finite-range bounds insufficient.

## Primary prior-art
Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011 — explicit genus-two polynomial and isospectral genus-one examples.
Henriksson, Kakkar, McPeak, Classical codes and chiral CFTs at higher genus, JHEP 05 (2022) 159, DOI 10.1007/JHEP05(2022)159.
Yahagi, Narain CFTs and error-correcting codes on finite fields, JHEP 08 (2022) 058, DOI 10.1007/JHEP08(2022)058.
Aharony, Dymarsky, Shapere, Holographic description of Narain CFTs and their code-based ensembles, JHEP 05 (2024) 343.
Ando, Kawabata, Nishioka, Gauging Z_N symmetries of Narain CFTs, JHEP 02 (2026) 058, DOI 10.1007/JHEP02(2026)058.
Mizoguchi, Oikawa, Unifying error-correcting code/Narain CFT correspondences via lattices over integers of cyclotomic fields, Physics Letters B 862 (2025) 139308, DOI 10.1016/j.physletb.2025.139308.

## New decision protocol
P60: full source-level audit of all three manuscripts and reconcile genus-two 10-variable conventions; verify claims and tests. P61: hostile prior-art audit of information-lift hierarchy versus HKM and modern modular bootstrap. P62: select one falsifiable open theorem, construct smallest nontrivial counterexample/witness with exact arithmetic. P63: general proof + proof assistant/independent implementation or counterexample and NO-GO. P64: novelty/physics gate. Manuscript only after P64 GO. If none, pivot to arithmetic finite determinacy; no indefinite automatic writing promise.

## Decision
P59 research direction reset GO; fourth-paper manuscript NO-GO. Novelty candidates, not claims.
