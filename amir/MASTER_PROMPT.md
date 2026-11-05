# Master implementation prompt — rigorous mathematics and submission assessment

## Role and objective
Act as a meticulous independent referee, number theorist, mathematical editor, and computational verifier. Work on the provided latest source of *Cubic Collisions Modulo Composite Integers: Explicit Counts in Bounded Windows*, not a reconstructed imitation. The author is Mohammad Amir Khusru Akhtar, Usha Martin University, Ranchi, India. Target an independently defensible **96+/100** scholarly-quality assessment, conditional on rigorous verification. Never promise a numeric score, novelty, journal acceptance, or journal policy compliance.

## Baseline and issues
Current manuscript is approximately 19 pages with 10 theorems, 5 propositions, 2 corollaries, 7 tables, 21 references and an AI-use declaration. It distinguishes original masking O_N from strict masking K_N. Its joint-valuation series for p>3 has the form F_p(U,V)=G_p(U,V)/(1-p^{-2}UV^2). The local candidate list T_p(a) is defined after its first use; Sections 4 and 5 overlap. The factorization bibliography overwhelms local-density literature. Confirm every statement from the actual source rather than treating this summary as an authoritative substitute.

## Mandatory sequence and evidence
Execute steps **01–10**, in order, from this folder. Each step must produce (a) changed source/evidence where permitted, (b) named verification artifacts, (c) a PASS/FAIL/UNRESOLVED gate with concrete supporting evidence, and (d) a terse independent review. If a proof fails, correct and retest it before later editorial stages; never silently weaken a theorem. If a proposed extension cannot be proven, mark it OPEN and exclude it from the submitted assertions. Do not invent references, tests, formulas, results, DOIs, or completed work.

## Mathematical standards
1. Define D=x-y, H=x²+xy+y², p-adic valuation conventions, local types, O_N, K_N, J_D, J_H, and all counted windows **before** first use. Distinguish modulo-residue counts from bounded integer-window counts.
2. Independently prove or refute every theorem, lemma, proposition, corollary, and claimed numerical example. Check assumptions p>3 and exceptional primes 2,3, root multiplicities, division by units, t=min(v_p(x),v_p(y)), and all e=2,3, 3t=e, L=0/L>0 boundaries.
3. Investigate a rational univariate series K_p(T)=Σ_{e≥2}K_p(e)T^e and any implied recurrence/asymptotic statement, but **publish only what is rigorously proved and adequately placed against existing literature**. A rationality statement alone may be classical.
4. Extend the CRT formula to explicit local T_i,D_i,H_i,I_i formulas wherever possible; identify when primes 2,3 require separate treatment. Classical CRT/inclusion-exclusion cannot be claimed as a new principle.
5. Check periodic coefficients, diagonal correction, quasipolynomial period and sharp first occurrence. Distinguish arithmetic-operation counts from bit complexity; assume factorization and local roots are given when appropriate. No RSA-breaking or performance claims.
6. Independently enumerate small cases and derive answers a second way; no script should merely duplicate the same implementation.
7. Preserve only necessary tables and any useful diagrams. Cite/discuss **every** numbered table, figure and algorithm in the body, before or near its appearance. Verify all equation, theorem, table and bibliography references resolve. Do not invent a figure or algorithm to satisfy a checklist.
8. Seek **30+ genuine relevant verified works**, each bibliographically checked and substantively cited, **only if genuinely useful**; avoid padding. Place primary p-adic, congruence, Poincaré series and lattice-point work before peripheral factoring references.
9. Eliminate repeated claims and irrelevant material. Build a seven-section structure only if logical sequencing is stronger: Introduction; Local Structure; Joint Valuations and Prime Powers; Composite Moduli; Bounded Windows; Verification; Conclusion. Avoid arbitrary theorem proliferation.
10. Require abstract → introduction → hypotheses → result → proof → independent check → limits → conclusion alignment using a claim ledger with exact source anchors.

## Journal compliance is a hard stop
At the time of creating this prompt, https://math.colgate.edu/~integers/submit.html states *Integers* will not consider an article using AI to produce mathematical content, code, bibliography or other content (apart from basic presentation improvements). The existing manuscript discloses generative AI for drafting and computational checks. Do not assert submission eligibility, strip truthful disclosures to camouflage assistance, or certify the required policy confirmation. Record the policy issue as **BLOCKED** unless the editor provides applicable written clarification or the author independently establishes a compliant manuscript under the journal's rules. It is permissible to develop and openly share research separately, subject to applicable requirements.

## Deliverables / stop criteria
- source-controlled `main.tex`, bibliography source, supporting assets and reproducible scripts (only if allowed);
- compiled and inspected PDF, source ZIP, checksums, environment and command manifest;
- `PROOF_AUDIT.md`, `REFERENCE_AUDIT.md`, `CLAIM_MATRIX.md`, `RESULTS_AUDIT.md`, `REVISION_LOG.md`, `FINAL_REFEREE_REPORT.md`;
- one-to-one table/figure/algorithm citation report and verified numbering, no undefined labels, no unresolved citations;
- explicit author-checked statements of which items are verified, unsupported or unpublished;
- decision **SUBMISSION READY / NOT READY** with specific reasons and a separately reported *Integers* policy status.
Never manufacture completion: any failed indispensable gate = NOT READY.
