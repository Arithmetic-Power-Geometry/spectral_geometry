# Stage 08 — references, citations and cross-reference audit

**Status: structural checks PASS; bibliography relevance NEEDS REVISION; bibliographic verification PARTIAL.** Audited supplied source `integers_final_work/main.tex`, not a newly revised manuscript.

## Source-level counts (executed Python regex audit)
- Bibliography entries: **21**.
- Citation commands: **13**.
- Unique cited keys: **21/21**.
- Undefined citation keys: **0**.
- Uncited bibliography entries: **0**.
- Declared LaTeX labels: **52**.
- Undefined reference targets: **0**.
- Unreferenced labels: `eq:bridge`, `eq:coefficientcount`, `prop:bridge` (not build errors).
- Tables: **7**; source cross-references to all seven previously confirmed.
- No figure or algorithm environments in this baseline.
- Important: **all citation commands occur before line 129 of the 19-page manuscript's TeX source**. The valuation section, computational experiments, and conclusion do not contain literature citations. This is a topical-context weakness, not an undefined-citation error.

## Bibliography relevance

**Retain when actually supporting the nearby proof:** Ireland–Rosen; Washington; Hardy–Wright; Bach–Shallit; Cohen; Apostol. Narkiewicz can support general algebraic number theory but requires a specific reason.

**Reassess or remove unless a clear comparison is made:** Pollard (1974, 1975), Brent, Lehman, Lehmer, Lenstra, Montgomery, Pomerance, Williams, Crandall–Pomerance. They are established factoring literature, but the manuscript is about counting specified collisions, not constructing a factoring algorithm. One compact paragraph with a few representative sources is sufficient; a long factoring catalogue weakens topical focus.

**Reassess:** Davenport, Vinogradov, Burgess, Wooley. These concern analytic number theory and incomplete sums; the manuscript uses exact finite CRT enumeration, not character-sum estimates or efficient congruencing. Retain only if a concrete distinction is necessary.

## Independently verified candidate additions

1. Jan Denef, “Report on Igusa's local zeta function,” *Astérisque* **201–203** (1991), 359–386, Exposé Bourbaki 741. DOI: **10.24033/ast.122**. Verified by Société Mathématique de France and Numdam: https://smf.emath.fr/node/42036 ; https://www.numdam.org/item/SB_1990-1991__33__359_0/ . Directly relevant to congruence solution counts and rationality of local Poincaré series.
2. Jan Denef and Kathleen Hoornaert, “Newton Polyhedra and Igusa's Local Zeta Function,” *Journal of Number Theory* **89** (2001), 31–64. DOI: **10.1006/jnth.2000.2606**. Publisher: https://www.sciencedirect.com/science/article/pii/S0022314X00926064 . Relevant background for explicit p-adic local-zeta formulas; not a direct proof of the manuscript's exact statistic.
3. Matthias Beck and Sinai Robins, *Computing the Continuous Discretely: Integer-Point Enumeration in Polyhedra*, 2nd ed., Springer, 2015. DOI: **10.1007/978-1-4939-2969-6**. Publisher: https://link.springer.com/book/10.1007/978-1-4939-2969-6 . Broad background on quasipolynomial enumeration; explicitly distinguish from the paper's residue-class setting.

## Citation-placement recommendations (not edits)

- Introduction: retain only enough factoring context to explain why counting is not a factorization speedup.
- Theorem 2 / cyclotomic lifting: keep appropriate elementary/Hensel references.
- Joint-valuation section: contextualize rationality with Denef and Denef–Hoornaert; **do not** imply their papers contain the same formula.
- Bounded-window section: cite Beck–Robins only as general quasipolynomial background, not as an exact source for the CRT candidate formula.
- Tables: cite each table in the manuscript prose and identify the exact computation/proof being checked; bibliography citations are not required merely because a table exists.
- Avoid any fabricated bibliography entries or arbitrary 30+ target.

## Remaining blockers

Not all 21 existing entries have been independently cross-checked against publisher catalogues. This stage did not modify `main.tex`, recompile the PDF, or certify compliance with *Integers* AI-use policy. A 96+/100 rating is not supported by these structural checks.
