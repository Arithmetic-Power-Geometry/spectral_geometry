# Stage 09 — editorial synchronization

A 19-page editorial revision was compiled successfully from the original manuscript source. The working copy is `amir_stage09/main.tex` in the generated deliverable; this stage preserves the original AI-use declaration.

## Changes made

1. Defined the local CRT candidate lists `T_{p_i}(a)` before the general bounded-window theorem instead of referring forward to the semiprime theorem.
2. Replaced the later duplicate candidate-list definition with a cross-reference to the common definition.
3. Grouped the square-free and semiprime bounded-window material under a single main section with a semiprime subsection; retained both theorems and their specialized formulas.
4. Corrected the sentence describing the general/specialized theorem relationship, avoiding a misleading forward claim.
5. Retained all original mathematical formulas, numerical tables, bibliography entries and the truthful generative-AI declaration. No unverified novelty claims or new mathematical theorems were inserted.

## Build

`pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice: PASS. Result 19 pages. Required local assets `integers.sty` and `erdos1.pdf`.

## Outstanding work

This is **not** the full final Stage 09 submission manuscript: bibliography topical revision, mathematical additions from Stage 05, detailed prose tightening, and exhaustive source/figure/table validation remain. Journal AI-use eligibility is unresolved. Do not claim 96+/100 or submission-ready.
