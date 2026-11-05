# Stage 07 — Reproducibility audit (2026-11-05)

**Result: supplied-code reruns PASS.** This stage executes the source package accompanying the 19-page manuscript, not a full independent reimplementation of every table. No manuscript text was changed.

## Source package

Local working source: `integers_final_work/main.tex`; verification files in the same directory. Source archive supplied by the user. The original uploaded source package has not been pushed to the public GitHub repository in this stage.

## Executed commands and results

| Script | Observed result | Manuscript evidence |
|---|---|---|
| `python verify.py` | PASS bibliography key use, cross-reference targets, selected prime-power/CRT tests | All seven tables and citations |
| `python verify_explicit.py` | PASS 78 independent coefficient comparisons | Table 4; explicit B,C formulas |
| `python verify_threshold.py` | PASS 80 full-window threshold comparisons | Theorem 8 |
| `python verify_squarefree.py` | PASS five three-/four-prime window cases | Table 6 |
| `python verify_primecube.py` | PASS p=5 (580), p=7 (1722) | Table 7 |
| `python verify_primepower_general.py` | Listed cases PASS, larger brute-force cases explicitly skipped | Table 7 |
| `python sensitivity.py` | Reproduced all five sensitivity rows | Tables 2 and 5 |
| `python verification/verify_composites.py` | Listed mixed-composite checks agree | General composite proposition |
| `python verification/verify_joint_valuations.py` | Listed state and strict-mask checks PASS | Theorem 9 |
| `python verification/verify_coefficient.py` | Listed coefficient checks PASS | Theorem 9 / Corollary 2 |

### Reproduced sensitivity table

| Design | Total | Neither | Difference only | Cofactor only | Both |
|---|---:|---:|---:|---:|---:|
| [1,15] | 32130 | 29808 | 196 | 2118 | 8 |
| [1,30] | 133110 | 122400 | 2582 | 7990 | 138 |
| [1,60] | 541620 | 490972 | 18446 | 30860 | 1342 |
| [1,120] | 2184840 | 1953412 | 102748 | 120860 | 7820 |
| scaled 15 | 32130 | 29410 | 606 | 2090 | 24 |

Every row sums exactly to its reported total. Table 2 is the first row.

### Other table checks

- Table 1: local formula checks included in `verify.py` and joint-valuation tests; no discrepancy observed.
- Table 3: semiprime complete-window checks supported by `verify.py` and earlier independent Stage 06 checks.
- Table 4: 78 coefficient comparisons PASS.
- Table 5: five regenerated sensitivity rows match the source.
- Table 6: all five listed square-free cases PASS.
- Table 7: exact formula/series/direct checks from Stage 04, including eight displayed rows, support the reported values. Note the manuscript says *direct enumeration* for large cases; the supplied `verify_primepower_general.py` explicitly skips some large brute-force checks. This should be disclosed precisely, or all eight direct enumerations rerun separately with documented timings.

## Defects and cautions

1. No disagreement was observed in executed tests, but the statement “all seven tables independently regenerated” would be too strong: several scripts share the manuscript's derivations or source.
2. Existing scripts have different dependency assumptions (SymPy required for explicit CRT checks); pin Python and dependency versions before a public reproducibility release.
3. Some brute-force computations were skipped by size; distinguish those from formula-versus-formula checks.
4. The source file has not been modified; manuscript changes must be synchronized after independent validation.
5. The journal's AI-use eligibility question remains a submission blocker.

**Stage gate:** source-package reproducibility PASS; full independent all-table audit PARTIAL.
