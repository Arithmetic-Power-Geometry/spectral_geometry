# P81 — Primary-literature correction: ELC versus LC and exact inequivalence test
Date 2026-10-30.

## Crucial verified prior art
Dymarsky and Shapere, 'Quantum stabilizer codes, lattices, and CFTs', JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160, https://inspirehep.net/files/e1c8fef55dad42ec3e182c10003415ff , especially equations (4.45)–(4.46), discussion following them and section 4.4 around pp.39–41: edge local complementation (ELC) is the triple vertex-LC pivot i,j,i on an existing edge. Graph isomorphism plus ELC corresponds to the B-form code CFT T-equivalence. Broader vertex-LC equivalence corresponds to local Clifford code equivalence, which need not preserve physical CFT equivalence. The paper explicitly says C-equivalent codes may have the same unrefined enumerator but different refined enumerators and physically distinct code CFTs. Henriksson, Kakkar and McPeak, 'Narain CFTs and quantum codes at higher genus', JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, studies higher-genus distinctions, including genus-one-isospectral code CFTs.

## Exact independent experiment
papers/PAPER-04/code/p81_elc_orbit.py: implement graph edge-pivot ELC(i,j)=LC_i LC_j LC_i on existing edge (i,j), exhaust labelled orbit via BFS; canonicalize each graph under ALL degree-respecting vertex permutations (complete graph isomorphism). Original seven-vertex P63 graphs A and B each have 15 labelled ELC states, with disjoint labelled orbits. A ELC orbit has 9 unlabeled graph classes, B has 10, with zero intersection. All assertions PASS in local execution. The graphs are NOT ELC-equivalent, although P79 proved LC-equivalence. This distinction is mathematically consistent.

## Consequences and correction ledger
P79 and P80 were correct about LC but any implication of physical equivalence was expressly unproven. P81 supplies the missing physically relevant distinction. The P80 HKM10 changes under vertex LC do not contradict physical genus-two distinctions; vertex LC is not necessarily a T-duality. A/B ELC inequivalence supplies an exact graph-level T-equivalence obstruction within the B-form code-CFT classification, not an independent demonstration of all conceivable O(d,d;Z) identifications outside that framework. The existence of isospectral physically inequivalent code CFTs and higher-genus separation is PRIOR ART, not a new fourth-paper theorem.

## Attached Boolean sensitivity paper
Akhtar, 'Cospectral Boolean Sensitivity Graphs Can Have Different Global Geometry: An Exact Separation and Infinite Family', SSRN-7544499, user-supplied PDF. Its exact cospectrality-plus-structural-separation proof pattern is useful, but sensitivity adjacency spectra do not equal physical Narain partition functions and its parity lift cannot be transferred without a separate CFT proof.

## Strict gate
P81 exact computational PASS and primary-source equivalence correction PASS. Novel fourth-paper theorem NOT found. Next P82: check ELC invariance of precise physical refined code enumerator, implement genus-two theta specialization with physical normalization, and kill-test any claimed new finite observation certificate against 2021 and 2023 papers. Do not write Paper 4.
