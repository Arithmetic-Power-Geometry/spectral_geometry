# Stage 01 issue register

## BLOCKER — journal eligibility
The source PDF contains a declaration that generative AI assisted drafting and computational checks. *Integers*' current author instructions prohibit AI production of mathematical content, code, bibliography and other manuscript content apart from basic presentation edits. The author must not falsely certify compliance or remove a truthful declaration to conceal the process. Seek written editorial clarification before submitting; separate this from mathematical quality.

## HIGH — theorem ordering and flow
- Theorem 5 uses the local list `T_{p_i}(a)` before its definition, which is located in Section 5 ahead of Theorem 7. Move the definition before Theorem 5.
- Sections 4 and 5 each derive bounded-window formulas and repeat CRT lifting arguments. Consolidate; preserve specialized semiprime formulas only when they add explicit computational insight.
- The central joint-valuation theorem currently appears in Section 6, after bounded-window material; evaluate moving it earlier.
- The general-composite CRT proposition does not supply explicit closed formulas at p=2 and p=3; do not imply that it does.

## HIGH — research claims
- A rational bivariate valuation series is presented, but a new univariate strict-masking series and recurrence are **not** yet proved.
- Novelty relative to p-adic Poincaré series/local-zeta literature has not been independently verified.
- The finite-sum formula and joint-series formula require a separate, genuinely independent proof and boundary-case audit.
- The original and strict masking statistics must not be conflated.

## MEDIUM — bibliography and exposition
- 21 cited references versus the requested 30+; do not add irrelevant sources to meet a quota.
- Many citations concern integer factorization rather than exact local counting; prioritize appropriate primary mathematical literature.
- Abstract and conclusion are broadly consistent but too theorem-inventory-driven; create sentence-level support map.
- Three unused LaTeX labels: `eq:bridge`, `eq:coefficientcount`, `prop:bridge`; not unresolved references.
- Source-level cross-references resolve and seven of seven tables are cited, but clean compile, independent numerical reproduction and visual PDF audit remain to be completed.

## Status
**Stage 01 structural audit: completed. Research revision stages 02–10: NOT COMPLETED. Submission readiness: NO.**
