# Stage 10 — compiled submission package and adversarial referee decision

Build LaTeX from a clean checkout (at least twice, or as required by the build system); inspect the rendered PDF visually page by page, including every formula, table, page break and bibliography entry. Audit the compile log for undefined refs/citations, errors, missing files, overfull boxes and font glyph issues. Generate reproducible ZIP, PDF, scripts, checksums, dependency manifest, `REVISION_LOG.md`, `FINAL_REFEREE_REPORT.md` and all earlier gate reports.

Independently score as a **subjective referee rubric**, not an acceptance probability: correctness 30, originality 25, mathematical significance 15, clarity/flow 10, literature grounding 10, reproducibility 10. Aim for >=96/100 only if evidence warrants; make scores and criticisms specific. Reassess how much of each result is classical vs distinct.

**Hard rejection gates:** missing proof; unverifiable table; unsupported novelty; fictitious reference; unresolved source cross-reference; abstract/conclusion contradiction; hidden limitation; or false publication-compliance statement. If any fails, output NOT READY with a prioritized repair list rather than a fabricated certificate.

**Journal-policy gate:** confirm the current official *Integers* instructions, particularly the ban on use of AI for producing mathematical work, code, bibliography or other content except basic presentation correction. The source manuscript has disclosed AI drafting/computational assistance. An otherwise excellent manuscript is **not eligible to be certified for *Integers* submission on current facts**. Do not strip this declaration merely for appearance. Author should seek applicable written editorial guidance or independently prepare a genuinely compliant work under the journal policy; do not submit a false confirmation.

**Deliver final:** ready-to-review PDF + TeX ZIP (when built), completed audit documents and explicit statuses: MATHEMATICAL QUALITY, REPRODUCIBILITY, EDITORIAL READINESS, JOURNAL ELIGIBILITY. Only label 'submission-ready for *Integers*' if every gate, including eligibility, is demonstrably satisfied.
