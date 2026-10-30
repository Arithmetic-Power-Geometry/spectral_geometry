# P01 prior-art and novelty audit — 2026-10-30

Status: bounded audit, NOT exhaustive; independently checked public source metadata. Source papers: three PDFs inventoried in papers/source_manuscripts/MANIFEST.md.

## Theorem-level strongest precedents and kill tests
1. **Narain geometry and equivalence:** Narain (1986) and Giveon–Porrati–Rabinovici (1994) establish toroidal backgrounds and target-space dualities. All proposed recovery claims must specify fixed integral basis versus full O(d,d;Z) orbit, and orientation/parity conventions. A spin-labelled discrepancy under B↦-B does not automatically distinguish unoriented CFTs.
2. **Unlabelled theta rigidity:** Schiemann (1997) proves ternary positive-definite quadratic forms determined by theta series (including finite coefficient methods); Conway–Sloane (1992) exhibit distinct four-dimensional lattices with the same theta series. Neither transfers automatically to the constrained 2d×2d Narain generalized-metric locus; blanket 'theta uniquely determines geometry' is untenable.
3. **Labelled measurements:** Evaluating E(v)=vᵀQ(G,B)v is a linear functional of the ambient symmetric Q but nonlinear in four d=2 background parameters. Classical polarization and matrix sensing/rank-one measurements are important prior art. Kueng–Rauhut–Terstiege (2017) treats low-rank matrix recovery from rank-one measurements under distinct assumptions. Source five-probe formula is a simple explicit inversion, not an established minimum or automatically novel.
4. **Higher-genus/code CFT:** Dymarsky–Shapere (2021) establish code/CFT links; source manuscript reports a pre-existing seven-vertex genus-two comparison. Any future higher-genus novelty must surpass prior examples and verify physical normalization and duality equivalence.
5. **Finite spectral cutoffs:** Existing source has a bounded rectangular-domain inverse and no uniform cutoff on unrestricted moduli; cannot claim universal finite-window reconstruction. Local stability under spectral collisions requires precise conditions.

## Precise candidate theorem questions (UNPROVED)
C1: For a predeclared set V⊂Z⁴, characterize injectivity of F_V(G,b)=(E(v))_{v∈V} over all SPD(2)×R modulo integral B-shifts, or over a specified fundamental interval; find smallest |V|. First determine whether four probes suffice globally, generically or only locally.
C2: Prove sharp lower bounds for nonadaptive continuous observation maps and compare adaptive integer-charge decision trees. State allowed adaptivity, real-exact oracle model and continuity assumptions; do not transfer nonadaptive lower bounds to adaptive procedures without proof.
C3: Establish a condition-number theorem for a chosen four/five-probe reconstruction under bounded noise, away from singular metric and spectral-collision loci; compare to the explicit five-probe inverse.
C4: Find genuinely non-product d≥3 isospectral Narain generalized metrics and check complete O(d,d;Z) orbits, not merely GL(d,Z) congruence.
C5: Prove a new *restricted-family* unlabelled finite-cutoff rigidity result beyond the existing rectangular example, or find explicit counterexamples.

## First mathematical lower-bound observation (not new)
SPD(2) has 3 real degrees of freedom and b one, so fixed-basis parameter domain has dimension 4. A continuous globally injective measurement map from an open subset of R⁴ to Rᵏ requires k≥4 by invariance of dimension. This only excludes k≤3 **nonadaptive continuous scalar observations**, not k=4; it does not settle restricted families, discontinuous adaptive schemes, orbit quotient subtleties, or information in full unlabelled multisets. It is classical topology, not a new theorem.

## Critical falsification and internal consistency issue
The first source manuscript reports a spin witness at 3373/1325, while later source manuscripts establish first discrepancy at 3313/1325 for b=1/5. This is compatible only if the former is explicitly a nonminimal witness. All citations must state which energy and role. The source manuscripts are not independent external confirmation.

## P01 ranked gates
C1 minimal fixed-label probe characterization: REVISE / priority for P02, contingent on checking 4-probe counterexamples and literature.
C3 quantitative stability: REVISE / secondary, risk of standard inverse-function-theorem repackaging.
C2 adaptive lower bound: REVISE / high conceptual difficulty and information-model sensitivity.
C5 unlabelled restricted-family theorem: REVISE / significant collision and prior-art risk.
C4 higher-dimension nonproduct: REVISE / computational and duality-classification heavy.

## Remaining literature blockers
Search was targeted, not systematic across MathSciNet/zbMATH/full citation graphs; no exhaustive prior-art claim. In particular, dedicated papers on minimal integral quadratic-form evaluation sets, arithmetic tomography, marked length spectra and effective theta bounds require deeper review. No theorem novelty verified; no paper writing authorized.

## Source URLs consulted
https://academic.oup.com/imrn/article-abstract/1992/4/93/660616
https://cir.nii.ac.jp/crid/1361699994081036544
https://cris.huji.ac.il/en/publications/target-space-duality-in-string-theory/
https://www.sciencedirect.com/science/article/pii/S1063520315001037
https://link.springer.com/article/10.1007/JHEP03(2021)160
